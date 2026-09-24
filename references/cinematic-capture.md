# Smooth detail-tour video

Use the real generated geometry; exclude credentials, debug panels and private editor URLs. Label presentation renders separately from native gameplay. Do not export or execute arbitrary game scripts merely to create a static beauty render.

## Look
Use warm key light, cooler fill and moderate hemisphere light with standard PBR materials. Ground contact shadows help scale. Fit a directional shadow frustum tightly around the model; start with 4096 resolution, tune bias against acne and detached shadows. Cache shadows only if geometry and lights are static. Use ACES tone mapping and inspect both shadowed timber and pale walls.

Use the largest sensible near plane and bounded far plane for depth precision, but keep near clipping outside all close-ups. Enable mipmaps and anisotropic texture filtering. Render at 3840x2160 and downsample to 1920x1080 to reduce edge shimmer. Remove redundant coplanar surfaces; simplify subpixel detail for presentation only, keeping the source build intact.

## Camera
Use `assets/camera-tour.mjs` in a Three.js renderer. Supply project-specific camera and target keyframes; smoothstep interpolation gives gentle acceleration. Wide introduction, gate close-up, walkway detail, castle ornament, wide ending is a useful pattern. Keep 1-2 seconds of slow drift at each detail and a 2-second final hold. Inspect transition frames too: interpolating endpoints can pass through walls. Adapt framing to the actual model, not the reference course coordinates.

## Deterministic export
Drive the renderer with frame index: `t = frame / fps`, not wall-clock elapsed time. For a 30-second film at 30fps, save exactly frames 0..899. Await each image write before advancing. A browser page can use its own explicit render button and a loopback-only capture endpoint; validate frame indices, limit body size, restrict origins and stop the receiver afterward. Do not expose the capture server publicly.

A 900-frame offline sequence avoids missing or repeated frames from real-time screen recording. Encode with an available FFmpeg installation:

```sh
ffmpeg -framerate 30 -i frames/%04d.png -frames:v 900 -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -movflags +faststart film.mp4
```

Check duration/resolution/fps, inspect wide and close-up frames, and review playback for shimmer and camera collisions. Encoding success alone does not prove smooth presentation. Keep captions clear of focal details; use brief Three.js / GLB / MML / world-test explanations. Leave native-world footage to an actual capture, not a simulated substitute.
