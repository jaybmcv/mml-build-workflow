---
name: mml-build-workflow
description: Build and test Metaverse Markup Language objects and browser games, export Three.js assets to GLB, and prepare MML for Otherside Vibe Maker or ODK. Use for MML scenes, model imports, shared document logic, compatibility checks, and geometry budgets. Does not replace native ODK gameplay or establish live-world support from a browser preview.
metadata:
  version: "0.2.0"
  maturity: "experimental"
---

# MML build workflow

Produce portable content and executable evidence. Distinguish documented support, installed capability, browser-tested behavior, and target-world-tested behavior. The initial knowledge was checked on 2026-09-19; recheck platform-sensitive details for the target build.

## Choose the execution target first

- **Objects, scenery, signs, repeating animation:** script-free MML, plus GLB assets where useful.
- **Browser puzzles and shared interactive toys:** MML elements plus JavaScript in an authoritative Networked DOM session. A multiplayer world/avatars are a separate host concern.
- **Detailed or procedural geometry:** author in Three.js or a modeling tool, export GLB, load with `m-model`, and let MML own portable transforms and supported interactions.
- **Otherside gameplay requiring player input, inventory, combat, reliable physics or persistent progress:** plan ODK/Morpheus gameplay with MML as optional presentation. Vibe Maker support is narrower than the general MML specification.
- **Custom web renderer/shaders/camera:** host-level Three.js code may be appropriate for a web experience, but it is not portable MML content.

Do not port a complete Three.js application into a script tag and expect Otherside to run it. GLB carries supported asset data, not JavaScript, arbitrary shader programs, postprocessing, or gameplay state.

## References to load as needed

- [Language and shared game state](references/language-and-games.md): document structure, transforms, event/state ownership, static vs dynamic hosting.
- [Otherside integration](references/otherside.md): Vibe Maker placement, the ODK route, compatibility conflicts, and target-world tests.
- [Models and budgets](references/models-and-budgets.md): export decisions, model audits, repeated placements, materials and performance.
- [Editor and verification](references/editor-and-verification.md): observed editor workflow, local CLI, practical failure recovery, and evidence boundaries.
- [Field notes](references/field-notes.md): demonstrated behavior and unresolved checks. Read when relying on a technique as established.

The small examples in `assets/` are starting points, not finished game architecture. `beacon-static.html` contains no script; `beacon-game.html` is a browser-only cooperative sequence; `beacon-hybrid.html` loads the included `beacon.glb` at `/assets/beacon.glb`. Copy these into a consuming project and configure its assets mount, or replace the URL with an uploaded asset URL in the editor.

## Build and verify

1. Read the consuming project's instructions and current work. Establish the destination, smallest player-visible result, state owner, asset rights, and budget. Set the user's triangle budget explicitly; 1,000,000 was the reference project's ceiling, not a verified platform maximum.
2. Check the target's supported tags **and attributes/events** before depending on them. Record conflicts; do not silently let a generic compatibility table override a platform-specific restriction.
3. Keep a local source file. Start with a minimal scene; add models and behavior independently so rendering failures and scripting failures can be isolated.
4. Run the official MML schema validator and glTF validation as applicable. A valid file does not establish runtime or platform compatibility.
5. Preview with real input. For shared state, use separate connections and test a late join into changed state. Distinguish a protocol-driven test from a person clicking in the world. For persistent/reward-bearing systems, add authority, identity, rate, replay and storage checks appropriate to the design; the example puzzle makes none of those production claims.
6. Audit total authored content including repeated placements, procedural/runtime spawns and primitives. Unknown models or host-generated geometry remain unknown, never zero. Keep margin for the destination world and test its actual performance.
7. Before calling content Otherside-compatible, run the target-world checks in the integration reference. Browser-only success stays labeled browser-only until then.

Keep source code and private-editor URLs separate from a future public package. Preparing or testing a private project does not imply publishing a static version, exposing project source, registering an MML in Otherside, or placing it in a live world.

## Improve the skill from builds

The owner intends this skill to improve through use. After a relevant build, add a concise dated field note: environment/version, attempted behavior, evidence, result, and remaining uncertainty. Promote a workaround into the workflow only when it is demonstrated or source-backed. Remove obsolete guidance when superseded instead of accumulating conflicting rules. Keep account IDs, credentials, private project links, machine paths, and brand/game-specific lore in the consuming project. Changes to unrelated memory stores are outside this skill's scope.

## Replicate the complete pipeline

For a new build, start with [the runnable starter](references/quickstart.md). For a detailed course, follow [production workflow](references/production-workflow.md). For a presentation video, use [cinematic capture](references/cinematic-capture.md). These resources are self-contained; the original project is not required.

Keep the visual GLB, simple colliders, shared logic, target-world evidence, and video renderer separate. Improve one without silently replacing the approved others. Read the latest field notes before adopting Swamp collision timings. Ship a build manifest and evidence record with each release.
