"""Count rendered mesh instances in a glTF/GLB default scene. Python stdlib only.

This is a geometry inventory, not an MML world profiler or a glTF validator.
Run Khronos glTF validation separately. Unknown required extensions fail closed.
"""
import argparse
import json
import struct
import sys
from pathlib import Path


def read_asset(path):
    raw = Path(path).read_bytes()
    if raw[:4] != b'glTF':
        return json.loads(raw)
    magic, version, length = struct.unpack_from('<III', raw)
    if version != 2 or length != len(raw):
        raise ValueError('Invalid GLB version or length')
    offset = 12
    while offset + 8 <= len(raw):
        size, kind = struct.unpack_from('<II', raw, offset)
        offset += 8
        if offset + size > len(raw):
            raise ValueError('Truncated GLB chunk')
        if kind == 0x4E4F534A:
            return json.loads(raw[offset:offset + size])
        offset += size
    raise ValueError('GLB has no JSON chunk')


def audit(document, scene=None):
    # These extensions do not alter the topology count obtained from accessors.
    supported = {'KHR_draco_mesh_compression', 'EXT_meshopt_compression',
                 'KHR_mesh_quantization', 'EXT_mesh_gpu_instancing',
                 'KHR_texture_transform', 'KHR_texture_basisu', 'EXT_texture_webp',
                 'KHR_lights_punctual'}
    unsupported = [x for x in document.get('extensionsRequired', [])
                   if x not in supported and not x.startswith('KHR_materials_')]
    if unsupported:
        raise ValueError('Unreviewed required extensions: ' + ', '.join(unsupported))
    if not document.get('scenes'):
        raise ValueError('No scene: cannot choose rendered roots')
    if scene is None:
        scene = document.get('scene')
        if scene is None:
            if len(document['scenes']) != 1:
                raise ValueError('Multiple scenes without a default; specify --scene')
            scene = 0
    accessors = document.get('accessors', [])
    meshes = document.get('meshes', [])
    nodes = document.get('nodes', [])
    result = {'scene': scene, 'triangles': 0, 'primitive_instances': 0,
              'mesh_instances': 0, 'materials': len(document.get('materials', [])),
              'images': len(document.get('images', [])), 'non_triangle_primitives': 0}
    visited = set()

    def mesh_count(index):
        triangles, primitives, non_triangles = 0, 0, 0
        for primitive in meshes[index]['primitives']:
            mode = primitive.get('mode', 4)
            accessor = primitive.get('indices', primitive['attributes'].get('POSITION'))
            if accessor is None:
                raise ValueError('Primitive has no countable geometry')
            count = accessors[accessor]['count']
            if not isinstance(count, int) or count < 0:
                raise ValueError('Invalid accessor count')
            if mode == 4:
                if count % 3:
                    raise ValueError('TRIANGLES count is not divisible by three')
                triangles += count // 3
            elif mode in (5, 6):
                triangles += max(0, count - 2)
            elif mode in (0, 1, 2, 3):
                non_triangles += 1
            else:
                raise ValueError('Unknown primitive mode')
            primitives += 1
        return triangles, primitives, non_triangles

    def walk(index):
        if index in visited:
            raise ValueError('Cycle or reused node in scene; invalid glTF hierarchy')
        visited.add(index)
        node = nodes[index]
        instancing = node.get('extensions', {}).get('EXT_mesh_gpu_instancing')
        instances = 1
        if instancing:
            counts = {accessors[a]['count'] for a in instancing['attributes'].values()}
            if len(counts) != 1:
                raise ValueError('Inconsistent GPU instance counts')
            instances = counts.pop()
            if instances < 1:
                raise ValueError('Empty GPU instance set')
        if 'mesh' in node:
            triangles, primitives, non_triangles = mesh_count(node['mesh'])
            result['triangles'] += triangles * instances
            result['primitive_instances'] += primitives * instances
            result['mesh_instances'] += instances
            result['non_triangle_primitives'] += non_triangles * instances
        for child in node.get('children', []):
            walk(child)

    for root in document['scenes'][scene].get('nodes', []):
        walk(root)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('asset')
    parser.add_argument('--scene', type=int)
    parser.add_argument('--instances', type=int, default=1,
                        help='Number of placements of this whole asset in the MML scene')
    parser.add_argument('--limit', type=int, default=1_000_000,
                        help='Exclusive triangle ceiling; equal to the limit fails')
    args = parser.parse_args()
    try:
        if args.instances < 1 or args.limit < 1:
            raise ValueError('Instances and limit must be positive')
        result = audit(read_asset(args.asset), args.scene)
        result.update(asset=Path(args.asset).name, bytes=Path(args.asset).stat().st_size,
                      placements=args.instances, total_triangles=result['triangles'] * args.instances,
                      exclusive_limit=args.limit)
        result['under_limit'] = result['total_triangles'] < args.limit
        result['scope'] = 'This asset only; add other models, MML primitives and runtime spawns separately.'
        print(json.dumps(result, indent=2))
        return 0 if result['under_limit'] else 1
    except (ValueError, KeyError, IndexError, TypeError, OSError, struct.error) as error:
        print(json.dumps({'error': str(error), 'under_limit': None}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
