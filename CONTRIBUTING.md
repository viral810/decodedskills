# Contributing

Start with a real development problem and a repeatable way to improve its outcome.

## Add a skill

1. Copy `templates/skill/` to `plugins/<plugin>/skills/<kebab-case-name>/`.
2. Match the frontmatter `name` to the directory name. Write a clear, single-line `description` explaining when to use it.
3. Replace the template with original instructions, a concrete outcome, and realistic examples. Put supporting material in that skill’s `references/`, `scripts/`, or `assets/` only when needed.
4. Exercise it on a real task in a target agent. Report the agent/version, request, observed behavior, and limitations in the PR.
5. Run `python3 scripts/validate.py` and `claude plugin validate plugins/engineering` when available.

Keep skills focused and composable. Explain tool dependencies and graceful fallbacks. Changes to instructions need behavioral evidence; passing structural checks alone does not establish quality.

## Pull requests

Explain the problem, resulting behavior, validation, and limitations. Include attribution for external ideas; do not submit copied third-party skill content.

By contributing, you agree that your contribution is distributed under this repository’s MIT license.
