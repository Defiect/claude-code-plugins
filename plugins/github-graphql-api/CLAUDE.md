# GitHub GraphQL API Plugin

This plugin equips Claude Code with deep knowledge of the GitHub GraphQL API.

## What's included

- **Usage guide** (`reference/guide.md`): Authentication, forming queries/mutations, pagination, rate limits, variables, node IDs, error handling
- **Quick reference index** (`reference/index.md`): One-line listing of all 31 queries, 264 mutations, 721 objects, 245 enums, etc.
- **Domain reference files** (`reference/domains/*.md`): Full schema details organized by topic area (repositories, issues, PRs, users, projects, actions, etc.)
- **Changelog** (`reference/changelog.md`): Recent schema changes

## How to use the reference files

When working with the GitHub GraphQL API:

1. Read `reference/guide.md` to understand how the API works (auth, pagination, rate limits)
2. Read `reference/index.md` to find what types/mutations/queries exist
3. Read the relevant `reference/domains/<topic>.md` file for full field-level detail
4. The domain files cover: repositories, issues, pull-requests, git-objects, users-and-orgs, projects, actions-and-ci, security, discussions, packages, sponsors, enterprise, releases, audit-log, apps-and-marketplace, common

## Rebuilding reference docs

If the GitHub GraphQL schema has been updated, re-run the build script:

```bash
cd scripts && uv run build_reference.py --fetch
```

The `--fetch` flag downloads the latest schema and guide docs directly from
GitHub — no local clone needed. If you have a local clone of
https://github.com/github/docs, omit `--fetch` to use it instead (faster).
