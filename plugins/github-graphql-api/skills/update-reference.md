---
name: update-reference
description: >
  This skill should be used when the user asks to update, refresh, or rebuild
  the GitHub GraphQL API reference documentation, or when the reference docs
  may be stale and need regeneration from the latest schema.
allowed-tools:
  - Bash
  - Read
argument-hint: "[--fetch] to force fetching from GitHub even if local docs clone exists"
---

# Update GitHub GraphQL API Reference

Run the build script to regenerate the reference documentation from the latest
GitHub GraphQL schema.

## Steps

1. Run the build script:
```bash
cd ${CLAUDE_PLUGIN_ROOT}/scripts && uv run build_reference.py --fetch
```

2. The `--fetch` flag downloads the latest schema.json and guide markdown
   directly from GitHub's docs repository — no local clone needed.

3. After running, verify the output:
```bash
ls -lh ${CLAUDE_PLUGIN_ROOT}/reference/*.md ${CLAUDE_PLUGIN_ROOT}/reference/domains/*.md
```

4. Report what was updated, including file sizes and counts from the build output.

## Notes

- The script fetches from `raw.githubusercontent.com/github/docs/main/`
- Schema changes are published frequently (often daily)
- If a local clone of github/docs exists at `../../github-docs-site-source`, it
  will be used by default (faster). Pass `--fetch` to force remote fetch.
