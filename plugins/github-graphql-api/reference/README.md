# GitHub GraphQL API Reference

Comprehensive reference documentation for the GitHub GraphQL API, organized for fast AI agent navigation.

**Endpoint:** `https://api.github.com/graphql` | **Auth:** `Authorization: bearer TOKEN` | **Method:** POST

## Where to Start

| Goal | File |
|------|------|
| Learn how the API works (auth, pagination, rate limits) | [guide.md](guide.md) |
| Find a specific query, mutation, type, or enum | [index.md](index.md) |
| Get full field-level details for a topic area | [domains/](#domain-reference-files) (see table below) |
| Check recent schema changes | [changelog.md](changelog.md) |

## Domain Reference Files

Each file contains complete type definitions, mutations, queries, enums, and input objects for its topic area.

| Domain | File | Contents |
|--------|------|----------|
| Repositories & settings | [domains/repositories.md](domains/repositories.md) | Repository, BranchProtectionRule, DeployKey, RepositoryRule, Topic, License + 44 mutations |
| Issues, labels, milestones | [domains/issues.md](domains/issues.md) | Issue, Label, Milestone, IssueType, IssueTemplate + 39 mutations |
| Pull requests & reviews | [domains/pull-requests.md](domains/pull-requests.md) | PullRequest, PullRequestReview, MergeQueue, ReviewRequest + 27 mutations |
| Git objects | [domains/git-objects.md](domains/git-objects.md) | Commit, Ref, Tree, Blob, Tag, Blame, Push + 7 mutations |
| Users, organizations, teams | [domains/users-and-orgs.md](domains/users-and-orgs.md) | User, Organization, Team, Bot, Gist, ExternalIdentity + 28 mutations |
| Projects (classic & V2) | [domains/projects.md](domains/projects.md) | ProjectV2, ProjectV2Item, ProjectV2Field, DraftIssue + 34 mutations |
| GitHub Actions & CI | [domains/actions-and-ci.md](domains/actions-and-ci.md) | Workflow, CheckRun, CheckSuite, Deployment, Environment + 14 mutations |
| Security advisories | [domains/security.md](domains/security.md) | SecurityAdvisory, SecurityVulnerability, CVSS, CWE, DependencyGraph |
| Discussions | [domains/discussions.md](domains/discussions.md) | Discussion, DiscussionComment, DiscussionCategory + 11 mutations |
| Packages | [domains/packages.md](domains/packages.md) | Package, PackageVersion, PackageFile + 1 mutation |
| Sponsors | [domains/sponsors.md](domains/sponsors.md) | Sponsorship, SponsorsListing, SponsorsTier + 8 mutations |
| Enterprise admin | [domains/enterprise.md](domains/enterprise.md) | Enterprise, EnterpriseOwnerInfo, EnterpriseBillingInfo + 16 mutations |
| Releases | [domains/releases.md](domains/releases.md) | Release, ReleaseAsset |
| Audit log events | [domains/audit-log.md](domains/audit-log.md) | 63 audit entry types (Org*, Repo* events) |
| Apps & marketplace | [domains/apps-and-marketplace.md](domains/apps-and-marketplace.md) | App, MarketplaceListing + 2 mutations |
| Common/shared types | [domains/common.md](domains/common.md) | PageInfo, Reaction, Actor, SearchResultItemConnection, shared enums (MergeableState, LockReason, etc.) + 33 mutations |

## Quick Lookup

| Looking for... | Where to find it |
|----------------|-----------------|
| All 31 root queries listed | [index.md → Root Queries](index.md#root-queries) |
| All 264 mutations listed | [index.md → Mutations](index.md#mutations) |
| All 721 object types listed | [index.md → Objects](index.md#objects) |
| All 245 enums with values | [index.md → Enums](index.md#enums) |
| Shared enums (used across domains) | [domains/common.md → Enums](domains/common.md#enums) |
| All 18 scalar types | [index.md → Scalars](index.md#scalars) |
| Authentication methods | [guide.md → Authenticating with GraphQL](guide.md#authenticating-with-graphql) |
| Pagination (cursors, pageInfo) | [guide.md → About pagination](guide.md#about-pagination) |
| Rate limits & point calculation | [guide.md → Primary rate limit](guide.md#primary-rate-limit) |
| Variables in queries | [guide.md → Working with variables](guide.md#working-with-variables) |
| Node IDs (REST ↔ GraphQL) | [guide.md → Putting global node IDs to use](guide.md#putting-global-node-ids-to-use) |

## Scope

This reference covers the **GitHub.com (free-pro-team)** GraphQL API only.

**Not covered:**
- GitHub REST API (separate API with different endpoints)
- GitHub Enterprise Server-specific schema differences
- General GraphQL concepts (see [graphql.org](https://graphql.org/learn/) for that)
- GitHub CLI (`gh`) usage beyond `gh api graphql` examples
