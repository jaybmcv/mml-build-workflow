# Field notes

## 2026-09-19 — Initial learning lab

- Official MML CLI 0.26.1, Three.js 0.186.0; model export and asset audit exercised locally.
- Three examples passed MML schema validation: script-free animated scene, JavaScript sequence puzzle, GLB-plus-MML scene.
- Browser puzzle completed by real clicks in both the local viewer and MML Editor play view. Reset was exercised locally and online.
- Three separate protocol clients tested wrong-order recovery, cooperative input, gate opening, late-join reconstruction and reset. This is not a full avatar-world or adversarial gameplay test.
- Procedural beacon GLB: 1,360 triangles, 133,676 bytes, three material parts, zero textures, zero Khronos errors/warnings. Rendered in local MML; not yet tested in Otherside.
- Geometry audit regression cases: repeated mesh placements, non-indexed geometry, strips/fans, GPU instances, unused meshes, invalid hierarchy and unknown required extensions.
- Editor project creation, rename, source editing, saved-source reload and play-link discovery observed. Temporary blank live preview recovered; no proven root cause.
- Initial online GLB selection was blocked by browser-extension file access; resolved in the follow-up below.
- Still open: exact target-world tag/event behavior, actual quota scope, terrain placement, model import/material parity, collision, ODK runtime bridge and live-world performance.

For future entries record the smallest reproducible behavior, exact target/version, evidence location and status. Avoid treating a proposed workaround or user recollection as a verified rule.

## 2026-09-19 � Online GLB upload follow-up

After the user enabled the Chrome extension Allow access to file URLs setting, file selection and upload succeeded. Copied the asset URL using the asset row copy button, added one m-model with a rotation animation beside the existing puzzle, and observed it in both EDIT and PLAY. It survived a page reload; distinct observed orientations support rotation. Consuming-project evidence: evidence/editor-uploaded-beacon.png and private .local/editor-hybrid-game.html. Combined authored content: 1,478 triangles (1,360 model + 118 puzzle). Otherside testing remains pending.

## 2026-09-19 — Swamp Gatehouse layout prototype

- Six walls × eight door instances; 75,686 authored triangles including 57 labels. Separate colliding structure (956 triangles), noncolliding decorative GLB (60,408) and reusable door (296 × 48).
- Three GLBs: zero Khronos errors/warnings; MML schema passed CLI 0.26.1. Exported GLB tests check openings across width/height, floor support at 100 sample grid positions and path points, and per-door collide flags.
- All 48 panels are visually identical; selected panels have collide=false. No break/reveal, randomization or scoring yet. Geometry rays are not an avatar or capacity test.
- Actual rendering verified locally and in private MML Editor. Consumer evidence lives under MML-Lab/evidence/gatehouse-*.png; reproducible source at scripts/build-gatehouse.mjs and build guide under builds/swamp-gatehouse-v1.
- CLI 0.26.1 rejects directional m-light; point lights used for preview, host lighting still requires tuning. Copy-asset clipboard reads should occur after the copy UI action has settled; immediate read returned stale clipboard text once.
- Existing Otherside Swamp remains the deployment target; placement, jump bypass, player triggers and 100-user load remain unverified. Solid barriers currently limit spectator sightlines.

## 2026-09-19 — Shared door discovery

MML CLI 0.26.1 shared-document click listeners drive shuffled safe-door sets, red wrong-door markers, noncolliding dropped correct panels, six ordered stages and reset. Three protocol clients passed discovery, late join and reset checks; actual local browser clicks produced red X and open GO states. Source and evidence are in the consuming lab under scripts/gatehouse-round.js, tests/gatehouse-rounds.test.mjs and evidence/gatehouse-rounds-discovery.png. This proves browser input/shared-document behavior only. No host identity, proximity enforcement, scoring, avatar finish or Swamp trigger support is claimed. XML schema parsing rejects raw less-than operators in script bodies; this small script uses equivalent loop conditions without raw less-than signs.

## 2026-09-19 — Animated timed rounds

CLI 0.26.1 accepts JavaScript-commented CDATA inside script (//<![CDATA[ and //]]>), allowing XML-sensitive operators while remaining executable. m-attr-lerp attr=y duration=650 gives a visible panel slide in the real browser; mid-slide evidence captured. Short authoritative ry updates with a 45ms lerp give wrong-door wobble. Absolute deadlines drive ready/countdown/running/complete/expired/reset-warning states. Three-client protocol and deterministic-clock tests cover reset spam, ignored countdown input, late join, timeout and shake cleanup. Reset warning is not an occupancy check. Assets/triangles unchanged. These are browser findings only.

## 2026-09-19 — Collision-trigger preparation and Swamp diagnostic

Added collision-interval=250 with collisionstart/collisionmove handlers to door models; clicks retained separately. Contact-move retries can handle a player who touched during countdown, but a stationary host may require a fresh contact. Three protocol clients passed contact-driven discovery, duplicate suppression, late join and reset. These are simulated events, not avatar physics.

Created a 766-triangle two-door diagnostic with independent contact counters, CLICK/CONTACT result labels, reference steps, barrier, reset and no attr-lerp dependency. Click tests do not increment contact counts. The official m-model compatibility table checked 2026-09-19 marks collision attributes/events unsupported in its generic Unreal table; actual existing-Swamp behavior remains untested. No portable player impulse command found; no player knockback implemented, and a moving collider must not be claimed as a reliable substitute. Source: https://mml.io/docs/reference/elements/m-model and https://mml.io/docs/guides/mml-collide-events-guide . World test plan stays in the consuming build.

## 2026-09-19 — Moving-collider knockback investigation

Official 3d-web-experience commit b3fed99f3bae267a23c66e195794ac22e2b81107 explicitly carries avatars with supporting surfaces (LocalController.getMovementFromSurfaces) and resolves capsule penetration (CollisionsManager.applyCollider). These support moving-floor and slow-piston hypotheses for that reference browser host. They do not prove Otherside Swamp behavior. Host methods setHorizontalVelocity/jump are not portable MML document APIs. m-link opens a URL, not a player-coordinate teleport.

Consumer research/swamp-knockback.md records pinned sources and integration conditions. examples/swamp-push-test.html isolates a 1.5m piston and platform motion without scripts or contact events; 44 authored triangles, CLI 0.26.1 schema validation passed. No avatar-motion or Swamp test performed. Keep animated collision response separate from trigger-event delivery. A shared pusher can affect multiple players. Production return must account for overlap and platform release; cyclic diagnostic motion is not finished knockback logic.

## 2026-09-19 — Moving-collider editor trial

The script-free piston/platform probe renders in a private MML Editor project, with visibly changing object positions in PLAY. Final source validates with CLI 0.26.1. The preview exposes no playable-avatar controls; this is animation evidence only, not player displacement. Consumer evidence: swamp-push-preview-a.png and swamp-push-preview-b.png. Swamp physics trial remains pending. Renaming again produced duplicate presence and lost broadcast; closing the created tab and reopening the saved project restored broadcasting and persisted source.

## 2026-09-19 — Official local avatar host

Built the official 3d-web-experience multi-user client/server at b3fed99f3bae267a23c66e195794ac22e2b81107 (0.28.0), Node 24.21.0 and npm 11.8.0. Twelve required builds passed. Source-backed fix: MMLDocumentsServer must match normalized relative paths rather than absolute paths when its ancestor includes a dot-directory; normalize document keys for Windows too. Local avatar, probe geometry, hot reload and camera input observed. Brief automated key taps did not establish walking; push/carry remains a manual avatar test. Do not present a rendered avatar as evidence of knockback. Consuming project includes restart script and LOCAL-AVATAR-WORLD.md; server binds loopback only.

## Swamp V2 correction — 2026-09-19

User reported slow push (no flight) and extreme glare from the placed original probe; screenshot confirms overexposure. Removed m-light intensity=450 entirely, applied script-free 3m/0.6s red stroke and overhead instructions to the existing live editor document. Source examples/swamp-push-world-test.html passes schema validation. Observed actual Swamp after update: V2 labels present, red panel and ground no longer white-clipped. This proves live document changes reached Swamp and lighting improved; fast-stroke player response remains unverified. User's slow-push report is the current target-world collision evidence. Exact local host flight is still not an MML feature.

## 2026-09-19 - Native Swamp carry/release trial
User reports timed MML pad carried the avatar up/back and released it successfully in the native Swamp client. The tested motion was 3m back + 2m up in 400ms, then collide=false before the return. This is target-world user evidence, not a measured impulse API or proof of free-flight momentum. A follow-up adds a countdown and pre-kick colour cue while retaining the same stroke; schema validation and native-world rendering confirmed, ride feel pending. Contact-trigger delivery and crowd behaviour remain unverified. Earlier notes describing Swamp displacement as wholly untested are superseded by this bounded user result.

## 2026-09-20 - Controlled Swamp lab
Built selectable trigger, proximity, carry/release, door, sequence, multiplayer and bounded static-load trials. Prior shared-document receipt test showed touch/click/prompt counts in native Swamp after user actions, but editor previews share the document. New lab selects a connection via an in-world click and separates selected-source counts from background traffic; source selection still needs target verification. Always distinguish received input, scene motion and avatar displacement. Schema and simulated state-machine checks are not world compatibility. Earlier blanket unsupported-contact conclusion is withdrawn. Source identity here is diagnostic, not authentication.

## 2026-09-20 - Contact-driven carry confirmed by user in Swamp
Controlled lab selected the user's connection through an in-world Identify click. User subsequently confirmed that test 07 appeared and touching the yellow tile pushed the avatar up and backward. Baseline: 400ms linear stroke, 3m backward and 2m upward, always-solid collider, 1s top hold, 1s return, 1s cooldown. This establishes a user-tested contact-to-motion path in that Swamp configuration; no free-flight impulse, repetition reliability or crowd capacity claim. Preserve diagnostic separation of event receipt, scene movement and avatar movement.

### 2026-09-22: procedural PBR texture pass
A visual-only course pass embedded a small PNG wood/stone atlas in GLBs, retaining vertex colours and standard rough PBR materials. Two assets passed glTF validation without errors/warnings; MML schema passed and editor save/reload matched source. Chrome rendering showed texture detail; this is not native-world texture/performance confirmation. Exact script and solid-collider comparisons protected the approved gameplay. Asset byte size matters separately from triangle count: combined scenery approached the observed editor upload limit even at under 180k total authored triangles.

## 2026-09-24 — Reusable production and presentation workflow
The reference course reached 10 rows and 80 doors with a generated ledger of 242,056 authored triangles. User selected 60/60 ms collider release timing after manual Swamp trials; different avatar sizes and movement exposed tunneling in earlier variants. These observations do not establish a portable impulse API. A 900-frame deterministic 4K-to-1080p video pipeline replaced a real-time recording after reported glitches; precision, texture filtering and subpixel detail were adjusted. Gate, walkway and castle close-ups were inspected. Live editor version reversion remained unresolved; keep source backups and verify persistence instead of claiming an unconditional fix.
