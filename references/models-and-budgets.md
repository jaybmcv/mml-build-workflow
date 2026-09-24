# Models and performance

## When the hybrid helps

MML primitives are fast to edit and independently animate. A large collection of decorative primitives can create excessive scene elements and draw work. Build detailed static decoration in Three.js or Blender, merge compatible static geometry by material, export GLB, and load through `m-model`. Keep separately interactive/moving pieces separate. This is a workflow recommendation, not a measured speed comparison across renderers.

[Three.js GLTFExporter](https://threejs.org/docs/pages/GLTFExporter.html) exports glTF 2.0, with `binary: true` for GLB and explicit animation clips when needed. Start with simple PBR materials, embedded textures, named parts and predictable units/pivots. Custom ShaderMaterial code, postprocessing and JavaScript behavior do not travel in the GLB. Extensions supported by the exporter may be unsupported by the destination importer.

Do not optimize transport compression before import compatibility is proved. Test the baseline GLB first; then test Draco, Meshopt, KTX2 or material extensions individually if the actual host supports them. Check texture dimensions, UVs, normal direction, alpha mode, double-sided cost, skeletons and animation clips. Use only assets the user is entitled to use and preserve third-party attribution.

The initial procedural beacon uses three merged material parts, ordinary PBR, no textures, 1,360 triangles and 133,676 bytes. It passed Khronos glTF validation with zero errors/warnings and rendered in the local MML viewer. This specific result does not prove import into Unreal.

## Count the scene, not just the file

The bundled standard-library Python helper inspects GLB/glTF JSON/accessor metadata:

```sh
python scripts/audit_glb.py /path/to/model.glb --instances 12 --limit 1000000
```

Paths above are relative to the skill folder. Output includes triangle counts for mesh references reachable in the selected default scene, repeated nodes, GPU instancing, and whole-asset placement multiplicity. It counts indexed/non-indexed triangle lists and conservatively counts strips/fans including degenerates. It fails at **equal to** the supplied limit. Exit codes: 0 below the exclusive ceiling; 1 over/equal; 2 uncountable/error. Use `--scene` if a multi-scene asset has no default.

Run a real glTF validator separately: this helper is not one. Its primitive instance count is **not** a measured draw-call count. It inventories one selected asset scene; it does not inspect an MML document, download remote assets, estimate texture memory, infer LOD choice, or count client-generated geometry. Unknown required extensions fail rather than silently lowering the total.

Maintain a scene ledger:

`peak authored triangles = sum(asset scene triangles × placements at peak) + MML primitive triangles + other generated content`

Count copies even when they share buffers or a URL. Do not subtract hidden meshes unless an enforced maximum-visible combination is established. Account for nested documents, alternate states and dynamically spawned objects. Skeletal animation does not add topology by itself, but skinning and material cost still matter.

For our initial pinned Three.js renderer, a basic cube has 12 triangles and a label plane has 2. Cylinder/sphere tessellation and target-renderer primitive meshes must be checked rather than assumed. For Otherside, use imported low-poly assets when a deterministic authored mesh count matters, and profile the actual target.

The user's exclusive ceiling is 1,000,000 triangles. An internal planning target around 750,000–800,000 leaves room for iteration; this is a suggested allocation, not a platform rule. Small props should usually be far below that ceiling. Also budget draw calls/materials, texture memory, collision, lights/shadows, active scripts, document mutation rate and asset download size. Profile frame time and loading at the expected device/player count before claiming performance.
