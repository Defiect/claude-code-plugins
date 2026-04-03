# Claude Code Plugins

A marketplace of Claude Code plugins by Sean.

## Installation

In Claude Code, run:

```
/plugins:add defiect/claude-code-plugins
```

Then enable the plugins you want from the plugin list.

## Plugins

| Plugin | Description |
|--------|-------------|
| **github-graphql-api** | Comprehensive GitHub GraphQL API reference — equips Claude Code with full schema knowledge, query patterns, pagination, rate limits, and 264 mutations across 16 domain files |
| **docs-optimizer** | Optimizes documentation directories for AI agent navigation efficiency using parallel subagent reviews |

## Automation

The **github-graphql-api** reference docs are automatically refreshed weekly via GitHub Actions. The workflow checks the specific upstream files in [github/docs](https://github.com/github/docs) that the build script depends on and only rebuilds if those files have changed.

You can also trigger a manual refresh from the Actions tab, or use the `/update-reference` skill within Claude Code.
