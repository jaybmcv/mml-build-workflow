# Detailed scene production

## Author and assemble
- Define meters, Y-up, origin, ground height, door clearance and local push direction before export. Put moving assets' pivots at a useful hinge or floor reference. Apply transforms once; don't bake and reapply them in MML.
- Build reusable visual modules: panel, pillar, roof, lantern, stair and wall bay. Merge static geometry by compatible material; keep independently moving parts separate.
- Use glTF standard PBR materials, restrained metalness/emissive, real UVs and embedded textures. Custom Three.js shaders, lights and game code do not automatically survive GLB export. Inspect roughness and colours in each host.
- Overlay trims need real separation from base surfaces. Thin grain strips and coplanar faces can shimmer in distant views. Prefer texture detail and mipmaps for fine grain. Avoid fixing a model's overlap solely with a video renderer trick.
- Use noncolliding decorative models with simple MML collision proxies where suitable. Invisible collision, visible model and trigger extents must align. Include posts, gaps, floor overlap and small-avatar clearance. GLB collider naming alone does not establish host support.

## Gameplay and tests
Keep geometry generation and shared logic in separate sources. Generate a single complete artifact, with a visible build ID and a manifest listing local asset hashes, row/door counts, bounds and motion parameters. Test one module before repetition. Preserve the user-selected baseline before new experiments.

Observe three independent things: input receipt, scene animation and avatar movement. Test standing, forward movement, strafing, jumping, small avatars, repeated triggers, two players, late join and reset. Debounce contact events; bound cooldowns and avoid stale timers changing a reset state. Diagnostic connection IDs are not authenticated host identity. A password in shipped source is a convenience gate, not secure authorization.

For moving colliders, the user-tested reference setting was 350ms out and return, with collision disabled 60ms before through 60ms after the apex; no apex pause. Test both wall and riser contacts. These are empirical Swamp settings, not a portable launch API. Lift/distance and collider thickness change reliability. Do not promise deterministic launch or 100-player support from a few manual trials.

## Budget and release
Count every rendered model placement, not only unique GLB meshes. Add native MML primitives, generated geometry and host-dependent labels explicitly. Audit asset byte sizes independently of triangles. The reference course's authored inventory was 242,056 triangles; that is a build ledger, not a measured whole-world draw count.

Store the exact source, dependency lockfile, validated GLBs, triangle ledger, target-world test results and open issues together. Keep static presentation snapshots apart from live script versions. Reopen the editor and verify the actual saved version before claiming persistence. If an editor returns to an older three-door test or restarts unexpectedly, stop repeated overwrites, preserve source and compare project identity, active sessions and broadcast state. The reference session did not isolate a universal cause or fix.
