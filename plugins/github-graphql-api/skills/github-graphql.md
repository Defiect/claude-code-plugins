---
name: github-graphql
description: >
  This skill should be used when the user is working with the GitHub GraphQL
  API -- for example, writing GraphQL queries or mutations for GitHub, using
  @octokit/graphql, calling api.github.com/graphql, looking up GitHub GraphQL
  schema types or fields (e.g. "what fields does Repository have"), asking
  about GitHub API pagination or rate limits, or building integrations that
  read or write GitHub data via GraphQL.
---

# GitHub GraphQL API Expert

You are working with the GitHub GraphQL API. This plugin provides comprehensive
reference documentation. Follow the workflow below to find and use the right
information.

## Key facts

- **Endpoint:** `POST https://api.github.com/graphql`
- **Auth:** `Authorization: bearer TOKEN` header (PAT, GitHub App token, or OAuth token)
- **All requests are POST** (the only GET is schema introspection)
- **Pagination:** Relay-style cursor pagination. Always use `first`/`last` (1-100) on connections. Use `pageInfo { hasNextPage endCursor }` to paginate.
- **Rate limit:** Points-based, not request-based. 5,000 points/hour for users. Query the `rateLimit` field to check.
- **Node limit:** Max 500,000 nodes per call. `first`/`last` values max 100.
- **Timeout:** 10 seconds max per request.

## How to use the reference files

### Step 1: Understand the API (if needed)
Read the usage guide for auth, pagination, variables, rate limits:
```
${CLAUDE_PLUGIN_ROOT}/reference/guide.md
```

### Step 2: Find what you need
Read the index to discover available queries, mutations, types, and enums.
The index maps every type to its domain, so use it to identify which domain
file to read next:
```
${CLAUDE_PLUGIN_ROOT}/reference/index.md
```

### Step 3: Get full details
Read the domain-specific reference file for complete field definitions:

| Domain | File |
|--------|------|
| Repositories & settings | `${CLAUDE_PLUGIN_ROOT}/reference/domains/repositories.md` |
| Issues, labels, milestones | `${CLAUDE_PLUGIN_ROOT}/reference/domains/issues.md` |
| Pull requests & reviews | `${CLAUDE_PLUGIN_ROOT}/reference/domains/pull-requests.md` |
| Git objects (commits, refs) | `${CLAUDE_PLUGIN_ROOT}/reference/domains/git-objects.md` |
| Users, orgs, teams | `${CLAUDE_PLUGIN_ROOT}/reference/domains/users-and-orgs.md` |
| Projects (classic & V2) | `${CLAUDE_PLUGIN_ROOT}/reference/domains/projects.md` |
| Actions, CI, deployments | `${CLAUDE_PLUGIN_ROOT}/reference/domains/actions-and-ci.md` |
| Security advisories | `${CLAUDE_PLUGIN_ROOT}/reference/domains/security.md` |
| Discussions | `${CLAUDE_PLUGIN_ROOT}/reference/domains/discussions.md` |
| Packages | `${CLAUDE_PLUGIN_ROOT}/reference/domains/packages.md` |
| Sponsors | `${CLAUDE_PLUGIN_ROOT}/reference/domains/sponsors.md` |
| Enterprise admin | `${CLAUDE_PLUGIN_ROOT}/reference/domains/enterprise.md` |
| Releases | `${CLAUDE_PLUGIN_ROOT}/reference/domains/releases.md` |
| Audit log events | `${CLAUDE_PLUGIN_ROOT}/reference/domains/audit-log.md` |
| Apps & marketplace | `${CLAUDE_PLUGIN_ROOT}/reference/domains/apps-and-marketplace.md` |
| Common/shared types | `${CLAUDE_PLUGIN_ROOT}/reference/domains/common.md` |

### Step 4: Check recent changes (if relevant)
```
${CLAUDE_PLUGIN_ROOT}/reference/changelog.md
```

## Common patterns

### Basic query structure
```graphql
query {
  repository(owner: "owner", name: "repo") {
    issues(first: 10, states: OPEN) {
      nodes {
        title
        number
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```

### Using variables (always prefer this)
```graphql
query($owner: String!, $name: String!, $first: Int!) {
  repository(owner: $owner, name: $name) {
    issues(first: $first) {
      nodes { title number }
      pageInfo { hasNextPage endCursor }
    }
  }
}
```

### Mutation pattern
```graphql
mutation($input: AddCommentInput!) {
  addComment(input: $input) {
    commentEdge {
      node {
        body
      }
    }
  }
}
```

### Node lookup by ID
```graphql
query($id: ID!) {
  node(id: $id) {
    ... on Issue {
      title
      state
    }
  }
}
```

### Using the GitHub CLI (`gh`)
```bash
gh api graphql -f query='
  query($owner: String!, $name: String!) {
    repository(owner: $owner, name: $name) {
      description
      stargazerCount
    }
  }
' -f owner=octocat -f name=Hello-World
```

## Important gotchas

1. **Connection fields require `first` or `last`** — the API will reject queries without them
2. **Enum values are UNQUOTED** in queries (`states: OPEN`) but **quoted in JSON variables** (`"states": "OPEN"`)
3. **Mutations need `input:` wrapper** — always `mutation { name(input: {...}) { ... } }`
4. **IDs are opaque strings** — get them from queries or REST API's `node_id` field
5. **Search with GitHub Apps:** use separate queries with `is:issue` or `is:pull-request` filters — combining them returns empty results
6. **Rate limit points, not requests** — a deeply nested query costs more points. Calculate: count all connection requests, divide by 100, round up (minimum 1)
7. **Pause 1 second between mutations** to avoid secondary rate limits
