# MML Build Workflow agent skill

Reusable Three.js -> GLB -> MML workflow, with an executable starter, asset audit and cinematic capture guidance. Version 0.2.0. Tested reference dependencies: Three.js 0.186.0 / MML CLI 0.26.1.

## Install
Copy this entire `mml-build-workflow` folder into `~/.codex/skills/` (Windows: `%USERPROFILE%\.codex\skills\`). Back up an existing version before replacing it. Restart or refresh skill discovery in your agent. Other agents that support SKILL.md can load the folder through their documented skill mechanism.

Invoke: **Use $mml-build-workflow to build a detailed 3D scene with Three.js assets, export GLBs and assemble it in MML.**

Start with [SKILL.md](SKILL.md) and [the runnable starter](references/quickstart.md). No access to the original course, accounts or private editor project is needed. This package includes a small generic beacon, not the full castle or private world source. Video guidance supports a reusable process; it is not a bundled video encoder or one-command renderer.

Swamp collision findings are dated, limited playtest observations. Verify your own platform and current SDK. No native-world reliability or crowd-capacity guarantee is implied.

Maintain improvements as short dated field notes: environment, change, test, evidence, result and limitation. Keep private account details and scene credentials out of the skill. Repository: https://github.com/jaybmcv/mml-build-workflow. Installation does not upload scenes or change live worlds.

[Package validation](references/package-validation.md) records what was checked and what remains target-specific.


## Full example build

[Swamp Gatehouse](https://github.com/jaybmcv/swamp-gatehouse) is a complete worked example: ten rows, eighty doors, detailed timber architecture, procedural Three.js-to-GLB build scripts, MML runtime, local preview instructions and geometry validation. It includes generic public demo reset handling rather than a live world's access code. Target-world physics still needs testing for each deployed revision.
