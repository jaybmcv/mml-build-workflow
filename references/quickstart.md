# Runnable Three.js to GLB to MML starter

Requires Node.js 22+ with npm, and Python 3 for the optional geometry audit. The pinned packages match the reference lab; review upgrades deliberately.

Copy `assets/starter/` to a new project directory, then run there:

```sh
npm install
npm run build
npm run validate
npm run serve
```

On Windows PowerShell use `npm.cmd` if script execution policy blocks npm.ps1. Open the local server dashboard at http://localhost:7079 and select scene.html. Keep the generated package-lock.json with the project. Never overwrite an existing project's package.json with this starter.

The build writes `assets/beacon.glb` and `evidence/beacon-gltf-validation.json`. Edit build.mjs to replace the beacon with your geometry. It demonstrates material buckets, merged geometry, binary GLB export, and Khronos validation. The small FileReader adapter supports texture-free export only; browser export or a complete image pipeline is needed for textures.

The scene uses the host's lighting, a noncolliding visual model, and a separate transparent box collider. This collider is an example approximation, not suitable for arbitrary models. If the preview is dark, add preview-only lights and tune them separately from the native world.

Run `python PATH_TO_SKILL/scripts/audit_glb.py assets/beacon.glb` for GLB geometry inventory. Count MML primitives and repeated placements separately. Upload the generated GLB through the authorized editor's Assets UI, then replace `/assets/beacon.glb` with the actual returned asset URL. Paste the complete scene from disk. Reload and confirm source and geometry persist. A local URL cannot be used as a remote asset URL.

Example agent request: Use $mml-build-workflow to create a Japanese timber gatehouse with eight reusable doors per row. Start with one playable row, preserve a 1-million triangle ceiling, then expand only after the target-world collision test passes. Deliver source, GLBs, MML, a budget report and a short detail-tour video.
