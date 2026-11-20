# Compatibility

All plugin formats use the same per-plugin `skills/` directory. Metadata is duplicated in small manifests and checked for consistency by CI.

| Surface | Packaging | Verification |
| --- | --- | --- |
| Agent Plugins | Per-plugin `plugin.json`, standard skill discovery | Local structural checks |
| Claude Code | `.claude-plugin/plugin.json` and marketplace | Run `claude plugin validate plugins/engineering`; installation smoke test required before release |
| Codex | `.agents/plugins/marketplace.json` pointing to engineering Agent Plugin | Installation smoke test required before release |
| Cursor | `.cursor-plugin/plugin.json` and marketplace | Installation smoke test required before release |
| Other skill-aware agents | Individual skill directories | Not tested yet |

The engineering plugin includes `pr-description` and `prove-it-works`. There are no hooks, MCP servers, or required provider-specific tools. Manifest checks do not prove installation, discovery, or skill behavior in any host.

The [authoring validation record](validation/pr-description.md) contains synthetic walkthroughs and structural-check results. These do not establish installation or live behavior across hosts.

The [prove-it-works validation record](validation/prove-it-works.md) distinguishes author-run checks from installation and independent behavioral testing.

Authoring references checked November 19, 2026:

- [Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Claude Code manifest reference](https://code.claude.com/docs/en/plugins-reference)
- [Cursor plugin reference](https://cursor.com/docs/reference/plugins)
