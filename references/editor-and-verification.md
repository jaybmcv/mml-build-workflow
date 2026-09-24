# Editor and verification

Observed with MML Editor on 2026-09-19; controls can change.

## Private project workflow

1. Open [MML Editor](https://mmleditor.com/) in the user's authorized session. Create a fresh project for experiments. Do not overwrite unrelated work.
2. **INFO → edit name** renames the project and may change the human-readable part of its URL. The project ID remains the useful identity. Keep its private URL in local project notes.
3. Focus **CODE**, select the document, and paste the complete local source as text. This is an intended code editor. Check **SCENE** and **EDIT** for structure, then **PLAY** and **DEBUG** for runtime behavior. Confirm the saved document survives a reload before treating it as durable.
4. **ASSETS → Upload** opens an intermediate dialog. **Select a file** opens the actual file chooser. The observed uploader says **up to 25 MB**. Choose a GLB, confirm the upload, then use the returned asset URL in `m-model`. A local filesystem path and local `/assets/...` URL are not remote editor asset URLs.
5. **Share** shows the play link and document WebSocket URL. The observed private-project setting protects source visibility; the dialog still describes a public play URL. Do not put secrets in scene state or assume private source means private runtime access.
6. **Static Versions** is the route to publish static content, per the official guide. It was inspected but not published in the initial session. Publishing, changing source visibility, or placing content in Otherside follows the user's authorization; do not do it merely to finish a preview.

The initial online project temporarily showed geometry in EDIT but an empty PLAY viewport after rename/reload. Later it regained its **Broadcasting live MML document** indicator and **Document restarted** log; both online clicks and reset then worked. The exact cause was not isolated. Check broadcast ownership/state, use a saved-source reload when safe, and compare a local runtime before diagnosing the MML code. Do not record a specific causal fix that was not established.

Chrome's file chooser rejected the GLB selection with a permission error in the initial session. The browser extension requires **Allow access to file URLs** for this upload route. This is a user-controlled browser setting, not a model or MML parse failure. After the user enabled it, selection/upload succeeded and the model rendered in EDIT and PLAY, including after reload. Use the asset row copy icon to obtain its URL; do not assume upload automatically populated the clipboard. Preserve the GLB and continue independent local work if the setting is unavailable.

## Local runtime

The initial lab pins `@mml-io/mml-cli` 0.26.1 and Three.js 0.186.0. CLI help/package documentation is the command source of truth.

```sh
npx @mml-io/mml-cli@0.26.1 validate scene.html
npx @mml-io/mml-cli@0.26.1 serve scene.html --assets assets --host 127.0.0.1 --port 7079
npx @mml-io/mml-cli@0.26.1 serve-dir examples --assets assets --host 127.0.0.1 --port 7079
```

For repeated work, use a local pinned package/lockfile instead of downloading a moving version. Single-document mode exposes `/ws`. Directory mode exposes a dashboard, document viewer pages and one endpoint per document. The default assets mount is `/assets/`. A local server remains local; it cannot be referenced by someone else's remote world as `localhost`.

The default standalone preview needed scene lighting in the initial test. Black silhouettes were fixed by adding two supported point lights; the editor's preview had supplied different lighting. Inspect geometry loading, materials and lights before assuming the exporter broke the file. Disable unnecessary shadow casting in the browser preview, but verify whether the target honors that attribute.

## Evidence levels

| Evidence | Establishes | Does not establish |
|---|---|---|
| Schema validation | Accepted markup/attributes for validator version | Visual or target platform support |
| Khronos GLB validation | Asset format validity | Material/animation parity in Unreal |
| Triangle inventory | Count for inventoried content/placements | Whole-world performance |
| Local viewer screenshot | A rendered scene at capture time | Multiplayer behavior or animation by itself |
| Real browser clicks | End-to-end browser input and feedback | Otherside input delivery |
| Separate WebSocket test clients | Shared protocol state and tested join behavior | Multiple actual player accounts or full avatar networking |
| Target-world playtest | The recorded cases on that build | Untested tags, devices, permissions or future builds |

Keep date, source hashes, versions, expected/result cases, screenshot provenance and open limitations. For animations, observe distinct frames or a short recording; one still is not animation proof.
