# Working in DecodedSkills

This repository distributes original agent skills. The engineering plugin currently includes `pr-description` and `prove-it-works`.

- Keep canonical skills in `plugins/<plugin>/skills/<kebab-case-name>/SKILL.md`.
- Do not copy third-party skill text. Attribute external ideas and references.
- Keep instructions portable. Document any required agent tools or fallback behavior.
- Keep templates outside `skills/` so they are not discovered as usable skills.
- Keep shared manifest metadata consistent across all plugin formats.
- Do not add hooks, MCP servers, agents, or dependencies without a concrete use case.
- Run `python3 scripts/validate.py` after changes. When available, also run `claude plugin validate plugins/engineering`.
- Distinguish structural validation from real installation and behavioral testing.
