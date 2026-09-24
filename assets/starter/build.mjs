import * as THREE from 'three';
import { GLTFExporter } from 'three/addons/exporters/GLTFExporter.js';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { mkdir, writeFile } from 'node:fs/promises';
import { validateBytes } from 'gltf-validator';

// GLTFExporter uses FileReader even for a texture-free binary export.
globalThis.FileReader = class {
  readAsArrayBuffer(blob) {
    blob.arrayBuffer().then(result => {
      this.result = result;
      this.onloadend?.();
    }).catch(error => this.onerror?.(error));
  }
};
const group = new THREE.Group();
group.name = 'Beacon';
const buckets = [[], [], []];
function part(geometry, material, x, y, z, rx = 0, ry = 0, rz = 0) {
  const matrix = new THREE.Matrix4().compose(
    new THREE.Vector3(x,y,z),
    new THREE.Quaternion().setFromEuler(new THREE.Euler(rx,ry,rz)),
    new THREE.Vector3(1,1,1)
  );
  const plain = geometry.index ? geometry.toNonIndexed() : geometry;
  plain.applyMatrix4(matrix);
  buckets[material].push(plain);
}
part(new THREE.CylinderGeometry(1.5,1.65,0.25,12),0,0,0.125,0);
part(new THREE.CylinderGeometry(0.8,1.2,0.35,12),0,0,0.425,0);
part(new THREE.CylinderGeometry(0.16,0.3,2.1,8),0,0,1.6,0);
part(new THREE.OctahedronGeometry(0.75,0),1,0,2.75,0);
for (let i=0;i<3;i++) {
  part(new THREE.TorusGeometry(1.1,0.055,6,32),2,0,2.75,0,Math.PI/2,i*Math.PI/3,0);
}
for (let i=0;i<6;i++) {
  const a=i*Math.PI/3;
  part(new THREE.BoxGeometry(0.16,0.7,0.2),1,1.3*Math.cos(a),0.55,1.3*Math.sin(a),0,-a,0);
}
const materials = [
  new THREE.MeshStandardMaterial({color:0x244b5e,metalness:0.5,roughness:0.55}),
  new THREE.MeshStandardMaterial({color:0x45d6cf,emissive:0x124f4b,metalness:0.15,roughness:0.4}),
  new THREE.MeshStandardMaterial({color:0xe8bc65,metalness:0.65,roughness:0.3})
];
buckets.forEach((geometries,i)=>{
  const mesh = new THREE.Mesh(mergeGeometries(geometries),materials[i]);
  mesh.name = ['Structure','Core','Orbits'][i];
  group.add(mesh);
});
const binary = await new GLTFExporter().parseAsync(group,{binary:true,onlyVisible:true});
const bytes = new Uint8Array(binary);
const validation = await validateBytes(bytes,{uri:'beacon.glb'});
await mkdir('assets',{recursive:true});
await mkdir('evidence',{recursive:true});
await writeFile('evidence/beacon-gltf-validation.json',JSON.stringify(validation,null,2));
if(validation.issues.numErrors) throw new Error('GLB validation failed');
await writeFile('assets/beacon.glb',bytes);
console.log(JSON.stringify({bytes:bytes.length,meshParts:3,errors:validation.issues.numErrors,warnings:validation.issues.numWarnings}));
