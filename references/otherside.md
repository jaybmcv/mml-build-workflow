# Otherside: distinguish the actual placement and runtime route

Fetched 2026-09-19. Vibe Maker pages describe March 2026 support; the supported-tags table explicitly says 3 March 2026. Treat these as the current published baseline, not proof of the user's running server version.

## Establish the target before applying platform restrictions

Existing-world MML placement, Vibe Maker and a developer-owned ODK world must not be treated as interchangeable. Record the actual world/build and authorized ingest route in the consuming project. Published Vibe Maker restrictions are evidence for that documented product scope, not proof that a different existing-world route has identical support. Test uncertain events, collision, moving-platform behavior and reset in the actual target. If the user scopes work to MML/GLB, keep native ODK work separate; propose MML adaptations rather than silently changing implementation platforms.

## Vibe Maker / placement into a world

The documented route is: author in MML Editor, obtain a static URL or running dynamic WebSocket URL, register URL/name at [Otherside MMLs](https://www.otherside.xyz/mmls), then choose the registered item in-world. If the placement dropdown is missing, the guide points to the MML Director role. World access and permitted placement area still need to be established. Source: [Create your first MML](https://docs.otherside.xyz/odk-docs/otherside-vibe-maker/create-your-first-mml).

Static versions omit JavaScript and need a newly published link after changes. Dynamic documents can update live, but this deployment guide requires the editor browser to remain running. General MML also supports your own persistent server; do not infer that any self-hosted endpoint is accepted by Otherside until tested. The published Vibe Maker restriction explicitly excludes player click/interaction events for dynamic MML. Source: [Supported MML Types](https://docs.otherside.xyz/odk-docs/otherside-vibe-maker/supported-mml-types).

| Published Vibe Maker tag status | Tags |
|---|---|
| Supported | `m-group`, `m-cube`, `m-sphere`, `m-cylinder`, `m-light`, `m-plane`, `m-model`, `m-character`, `m-image`, `m-video`, `m-label`, `m-prompt`, `m-attr-anim` |
| Not supported | `m-audio`, `m-position-probe`, `m-link`, `m-interaction`, `m-chat-probe`, `m-attr-lerp` |
| Not listed; verify | `m-frame`, `m-animation`, `m-overlay` |

Source: [Supported Tags](https://docs.otherside.xyz/odk-docs/otherside-vibe-maker/supported-tags). A supported tag does not establish every attribute or event. In particular, `m-prompt` appearing in this table does not resolve the broader interaction restriction.

## ODK / a game built in Unreal

The platform documents MML object spawning and removal through Blueprints. Its diagrams show `M2M MMLSpawner Singleton` with `Server Create Document` (URL, caller, transform) or server-side `Create Document`; the returned document reference is retained for later removal. Inspect installed equivalents and caller handling before copying the diagram. The sample's native clickable mesh that spawns MML does **not** prove that a spawned MML object receives MML click events.

MML can also describe an avatar: one root `m-character`, compatible UE5 skeletons, and optional model parts/attachments. The platform's avatar animation system drives these characters; arbitrary authored avatar animations are not promised. See [MML integration and diagrams](https://docs.otherside.xyz/platform-documentation/creation/unreal-development/features-and-tutorials/mml).

For gameplay, use the project's established Morpheus networking and ODK lifecycle, validation and pooling guidance. Keep durable game state outside pooled visual actors. Normal downstream authoring is Blueprint/content work; an MML task is not a reason to introduce a bespoke compiled plugin. See [ODK getting started](https://docs.otherside.xyz/platform-documentation/creation/unreal-development/getting-started).

Read-only inspection of one Chapter 10-associated installation found MMLEngine, glTFRuntime dependencies, ODK MML document/spawner/proxy assets, and inventory/handler components. That establishes installed content only. It does not validate a gameplay bridge, audio support, permissions, or live-world behavior. Discover the user's current build instead of treating those names as universal.

## Conflicting evidence

The general [MML model compatibility table](https://mml.io/docs/reference/elements/m-model#compatibility) marks Unreal `onclick` supported, while the Vibe Maker guide says player clicks/interactions are not supported. Preserve both claims with their scope. Default to the narrower Vibe Maker contract for deployment there; test a tiny click probe on the exact target build before promising more. Installed audio/interaction assets likewise do not override a published product restriction.

## First target-world test

Use an authorized test space and the smallest content object. Record build/date, URL type and source hash, world/session identity privately, permissions, transform and results.

1. Spawn/place a meter-scale cube and the script-free beacon. Check actual avatar scale, orientation, terrain contact, ground pivot and bounds.
2. Check materials, color/exposure, light cost, backfaces, labels, textures, animation and collision. Do not assume preview lighting equals world lighting.
3. Load the authored GLB separately. Inspect mesh/material import and collision cost before combining it with game logic.
4. If testing dynamic input, use one isolated event probe and record actual delivery or absence. Avoid building a whole game around an unverified event.
5. Observe from a second client and then a joining/rejoining client as applicable. Check cleanup/despawn, session restart behavior, runtime-spawn peak geometry and performance.

Placement can align an object to terrain; that does not establish permission or support to edit the host terrain itself. Keep entry/exit space, collision and spawn overlap intentional.

## Limits

No authoritative 1,000,000 vs 10,000,000 geometry maximum was established in this research. Those figures came from the user's recollection. Use under 1,000,000 for our authored content and verify whether any platform quota applies per asset, document, placement, player, or world. Avatars, terrain and other creators' objects consume separate host resources; an asset audit is not a whole-world frame-budget guarantee.
