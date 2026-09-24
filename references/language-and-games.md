# Language and game design

Checked 2026-09-19 against the [MML documentation](https://mml.io/docs) and CLI 0.26.1.

## What runs where

MML is HTML-shaped scene description. The host renders its supported custom elements. A static document is served as HTTPS content; a dynamic session runs script on an authoritative document host and sends DOM changes over WebSockets. The editor can be that temporary host while its tab remains running. Publishing a static snapshot does not preserve executable game logic.

Use one enclosing `m-group` or an appropriate HTML document for the validator. CLI 0.26.1 rejected adjacent top-level `m-group` and `script` as extra content; nesting the script inside the group passed and ran. Use explicit closing tags for MML elements. XML-sensitive script text may require CDATA for schema validation; inspect the validator output instead of assuming browser HTML acceptance proves validity.

See [Get Started](https://mml.io/docs/guides/get-started). This is an execution architecture, not persistent storage: restart can reset state, and separate documents generally own separate state. A single shared endpoint placed in several worlds can intentionally share one session; use separate sessions when those worlds need independent rounds.

## Scene authoring essentials

| Need | Tool and caution |
|---|---|
| Local hierarchy | `m-group`; transform children as a unit |
| Basic geometry | `m-cube`, `m-sphere`, `m-cylinder`, `m-plane`; tessellation is renderer-owned |
| Authored geometry | `m-model src="...glb"`; format/extensions depend on host |
| Repeating motion | `m-attr-anim` child animates a parent attribute; `start`, `end`, `duration`, `start-time`, `loop`, `ping-pong` |
| Transition after state update | `m-attr-lerp` where supported; verify destination |
| Text | `m-label` uses `content`, `font-color`, `font-size`, dimensions and alignment |
| Audio/video/image | Separate media elements; codecs, autoplay, loading, and platform support differ |
| Clicks/actions | `click` on rendered objects or `m-interaction` where supported |
| Proximity/collision | `m-position-probe` / collision events; receiving events is distinct from physical collision |
| Composition | `m-frame` where supported; avoid sharing unintended state |
| Avatars | `m-character`; avatar rigs and animation are host-specific |
| Overlays, prompts, links, chat | Check host restrictions; a web feature is not an Unreal guarantee |

MML positions/dimensions use meters, rotations use degrees. Three.js normally works with radians for Euler rotation. Use a consistent ground-level pivot and root transform. For native Unreal placement, confirm meter/centimeter and Y-up/Z-up conversion at the boundary; do not blindly copy raw coordinate triples or double-convert a loader's transforms.

`m-attr-anim` follows document time in milliseconds. Prefer it to per-frame server attribute updates for predictable repeating motion. Static does not mean motionless: declarative animation can work without scripts. References: [m-model](https://mml.io/docs/reference/elements/m-model), [m-attr-anim](https://mml.io/docs/reference/elements/m-attr-anim), [m-label](https://mml.io/docs/reference/elements/m-label).

## Game logic

Use ordinary DOM operations: find elements, add event listeners, update attributes, create/remove elements. Make state transitions in one authoritative document. For example, a cooperative sequence owns a single progress counter; all players advance the same sequence and a joining client receives its current gate state.

`MMLClickEvent.detail.connectionId` identifies a connection; it is not a durable account identity. The click position is relative to the element. A client-supplied event is a request, not proof of eligibility or proximity. A serious game needs host-supported identity, authoritative prerequisites and movement/range verification where required. See [MMLClickEvent](https://mml.io/docs/reference/events/MMLClickEvent).

Keep browser-only APIs and renderer objects out of document logic unless the exact host exposes them. UI, player movement, physics, camera and DOM scene state are not interchangeable responsibilities. Host customization should remain a separate layer.

## Web world choices

The [3D Web Experience](https://mml.io/3d-web-experience) provides a browser-world starting point with avatars and networking. Its player-presence networking and MML document synchronization are separate systems. Use its official CLI/templates for a full walkable multiplayer web world; a standalone MML viewer is sufficient for an object or interaction test. Pin tested versions and inspect the current package help rather than assuming an old GitHub example matches a new CLI.

React is optional authoring/composition assistance, not an Otherside compatibility layer. Start with plain MML/JavaScript when that is simpler. See the [official repositories](https://github.com/mml-io).
