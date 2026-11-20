# DecodedSkills

Original, composable skills for agentic software development.

**Status:** foundation only. No skills ship yet. Our engineering philosophy and first workflows will be developed here.

## Local development

Requires Python 3.11+ for repository checks. The plugin itself has no runtime dependencies.

```sh
python3 scripts/validate.py
claude plugin validate plugins/engineering
claude --plugin-dir ./plugins/engineering
```

The last command opens Claude Code with the local plugin. Until skills are added, it exposes no workflows.

## Installation

### Claude Code

Run these inside Claude Code:

```text
/plugin marketplace add viral810/decodedskills
/plugin install engineering@decodedskills
```

For local development, replace `viral810/decodedskills` with the absolute path to your clone.

### Codex

Run in your terminal:

```sh
codex plugin marketplace add viral810/decodedskills
codex plugin add engineering@decodedskills
```

For local development, replace `viral810/decodedskills` with the absolute path to your clone.

### Cursor and other agents

Each plugin’s `plugin.json` uses the Agent Plugins format. A Cursor manifest is also included. Cursor marketplace publication is a separate step; this repository has not been listed there.

Agents supporting Agent Skills can consume individual `plugins/engineering/skills/<name>/` directories once skills exist. Agent-specific installation instructions will be added after testing. Install through one method per agent to avoid duplicate skills.

## Repository layout

- `plugins/engineering/`: empty engineering plugin, with portable and host manifests.
- `plugins/engineering/skills/`: canonical engineering skills, shared across agents.
- `.claude-plugin/marketplace.json`: Claude Code plugin catalog.
- `.cursor-plugin/marketplace.json`: Cursor plugin catalog.
- `.agents/plugins/marketplace.json`: Codex plugin catalog.
- `templates/skill/`: authoring template, excluded from the installed skill collection.
- `scripts/validate.py`: dependency-free repository checks.
- `docs/`: compatibility notes and release checklist.

See [contributing](CONTRIBUTING.md) to add a skill and [compatibility](docs/compatibility.md) for validation limits.

## Inspiration

We study the usability and distribution ideas behind [Matt Pocock’s skills](https://github.com/mattpocock/skills), [pstack](https://github.com/cursor/plugins/tree/main/pstack), [Superpowers](https://github.com/obra/superpowers), and [Han](https://github.com/testdouble/han). Our skill content and engineering approach will be authored independently.

## License

[MIT](LICENSE).
