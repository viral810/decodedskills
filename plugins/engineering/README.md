# Engineering

Original engineering skills for agentic software development.

Version 0.2.0 is a preview release. Structural validation has passed; live installation and end-to-end behavior remain untested.

## Skills

| Skill | Use it when |
| --- | --- |
| [pr-description](skills/pr-description/SKILL.md) | Drafting or updating a PR/MR description that explains why, includes recorded insights, and describes existing evidence. |

## Usage

After loading the plugin, ask your agent:

- “Use pr-description to draft a description for this branch against develop.”
- “Use pr-description to update PR 42’s description.”

Drafting leaves remote descriptions untouched. Explicitly requesting publication authorizes the requested description update; it does not authorize commits, pushes, or merges. Host tools must be available for publication.

The skill follows the repository’s applicable template. It investigates linked tickets and supporting references, then commit history, and asks when intent remains unclear. Implementation insights come only from recorded discoveries. Missing evidence is flagged without blocking the draft.

Verification and screenshot capture are separate work. This skill reuses existing evidence and can add explanatory diagrams; it does not run checks or capture screenshots.

Install from the `decodedskills` marketplace as `engineering@decodedskills`. See the [repository README](../../README.md) for host-specific commands and [compatibility notes](../../docs/compatibility.md) for validation limits.

To add skills, follow the [contribution guide](../../CONTRIBUTING.md).
