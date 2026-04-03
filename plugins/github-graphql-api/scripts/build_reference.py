"""
Build script that compiles GitHub's GraphQL API docs into LLM-friendly
markdown reference files for use in a Claude Code plugin.

Sources (local mode — default if github/docs clone exists):
  - schema.json from github/docs repo (src/graphql/data/fpt/schema.json)
  - Guide markdown from github/docs repo (content/graphql/)
  - changelog.json from github/docs repo (src/graphql/data/fpt/changelog.json)

Sources (remote mode — `--fetch` flag, or automatic if no local clone):
  - Fetches files directly from raw.githubusercontent.com/github/docs/main/
  - No local clone of the docs repo needed

Outputs:
  - reference/guide.md          — cleaned usage guide
  - reference/index.md          — quick-reference index of all types
  - reference/domains/*.md      — domain-organized schema reference
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
import textwrap
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Where the github/docs clone lives relative to this repo root
DOCS_ROOT_ENV = "DOCS_ROOT"  # override via env var
DEFAULT_DOCS_ROOT = Path(__file__).resolve().parent.parent.parent / "github-docs-site-source"

SCHEMA_JSON = "src/graphql/data/fpt/schema.json"
CHANGELOG_JSON = "src/graphql/data/fpt/changelog.json"
GUIDES_DIR = "content/graphql/guides"
OVERVIEW_DIR = "content/graphql/overview"

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "reference"

# ---------------------------------------------------------------------------
# Domain classification
# ---------------------------------------------------------------------------

# Order matters: first match wins.  Patterns are matched against type names.
DOMAIN_RULES: list[tuple[str, list[str]]] = [
    ("repositories", [
        "Repository", "Repo", "DeployKey", "BranchProtection",
        "License", "Topic", "Submodule", "Codeowner", "RepositoryRule",
        "RepositoryInvitation", "RepositoryMigration", "RepositoryPlan",
        "RepositoryVisibility", "RepositoryInteraction", "RepositoryContact",
        "RepositoryCustomProperty", "RepositoryProperty",
        "LinkedBranch", "ContributingGuideline",
        "Stargazer", "StarredRepository", "UserNamespaceRepository",
        "VerifiableDomain", "FundingLink", "CodeOfConduct",
    ]),
    ("issues", [
        "Issue", "Label", "Milestone", "SubIssue", "ParentIssue",
        "IssueTemplate", "PinnedIssue",
    ]),
    ("pull-requests", [
        "PullRequest", "ReviewRequest", "ReviewDismissal",
        "MergeQueue", "SuggestedReviewer", "AutoMerge", "AutoRebase",
        "AutoSquash", "AutomaticBaseChange",
        "BaseRef", "HeadRef", "ConvertToDraft", "ConvertedFromDraft",
        "ReadyForReview",
    ]),
    ("git-objects", [
        "Commit", "Blob", "Tree", "Tag", "Ref", "Blame",
        "GitActor", "Push", "Comparison", "GpgSignature", "SmimeSignature",
        "SshSignature", "UnknownSignature", "GitHubMetadata",
    ]),
    ("users-and-orgs", [
        "User", "Organization", "Team", "Mannequin", "Bot",
        "ExternalIdentity", "OIDCProvider", "OrganizationIdentity",
        "OrganizationInvitation", "OrganizationMember",
        "OrganizationEnterprise", "Follower", "Following",
        "MemberFeatureRequest", "ProfileItemShowcase",
        "SocialAccount", "UserStatus", "UserList", "UserEmail",
        "UserBlock", "SavedReply", "PublicKey", "Hovercard",
        "GenericHovercard", "OrganizationsHovercard", "OrganizationTeamsHovercard",
        "ViewerHovercard", "ReviewStatusHovercard",
        "IpAllowList", "Gist",
    ]),
    ("projects", [
        "Project", "DraftIssue",
    ]),
    ("actions-and-ci", [
        "Workflow", "CheckRun", "CheckSuite", "CheckAnnotation", "CheckStep",
        "Status", "Deployment", "Environment", "PinnedEnvironment",
    ]),
    ("security", [
        "SecurityAdvisory", "SecurityVulnerability", "CVSS", "CWE", "EPSS",
        "RepositoryVulnerabilityAlert", "Dependabot", "DependencyGraph",
        "CodeScanning",
    ]),
    ("discussions", [
        "Discussion", "PinnedDiscussion",
    ]),
    ("packages", [
        "Package",
    ]),
    ("sponsors", [
        "Sponsor", "Sponsorship", "StripeConnectAccount",
    ]),
    ("enterprise", [
        "Enterprise",
    ]),
    ("releases", [
        "Release", "ReleaseAsset",
    ]),
    ("audit-log", [
        "AuditEntry", "Org", "Repo",  # Org*AuditEntry, Repo*AuditEntry
    ]),
    ("apps-and-marketplace", [
        "App", "Marketplace", "Oauth",
    ]),
]

# Anything not matched goes here
DEFAULT_DOMAIN = "common"

# Nicer titles for domain files
DOMAIN_TITLES: dict[str, str] = {
    "repositories": "Repositories & Repository Settings",
    "issues": "Issues, Labels & Milestones",
    "pull-requests": "Pull Requests, Reviews & Merge Queues",
    "git-objects": "Git Objects (Commits, Refs, Trees, Blobs)",
    "users-and-orgs": "Users, Organizations & Teams",
    "projects": "Projects (Classic & V2)",
    "actions-and-ci": "GitHub Actions, CI & Deployments",
    "security": "Security Advisories & Vulnerability Alerts",
    "discussions": "Discussions",
    "packages": "GitHub Packages",
    "sponsors": "GitHub Sponsors",
    "enterprise": "Enterprise Administration",
    "releases": "Releases & Release Assets",
    "audit-log": "Audit Log Events",
    "apps-and-marketplace": "GitHub Apps & Marketplace",
    "common": "Common Types & Shared Interfaces",
}

# ---------------------------------------------------------------------------
# Template resolution for guide markdown
# ---------------------------------------------------------------------------

# Map of data variable paths to their fpt values
TEMPLATE_VARS: dict[str, str] = {
    "variables.product.prodname_dotcom": "GitHub",
    "variables.product.prodname_dotcom_the_website": "GitHub.com",
    "variables.product.company_short": "GitHub",
    "variables.product.prodname_github_app": "GitHub App",
    "variables.product.prodname_github_apps": "GitHub Apps",
    "variables.product.prodname_oauth_app": "OAuth app",
    "variables.product.prodname_oauth_apps": "OAuth apps",
    "variables.product.pat_generic": "personal access token",
    "variables.product.pat_v1": "personal access token (classic)",
    "variables.product.pat_v2": "fine-grained personal access token",
    "variables.product.graphql_url": "https://api.github.com/graphql",
    "variables.product.rest_url": "https://api.github.com",
    "variables.product.prodname_ghe_server": "GitHub Enterprise Server",
    "variables.product.prodname_ghe_cloud": "GitHub Enterprise Cloud",
    "variables.product.prodname_free_user": "GitHub Free",
    "variables.product.prodname_actions": "GitHub Actions",
    "variables.product.prodname_discussions": "GitHub Discussions",
    "variables.product.github": "GitHub",
    "variables.enterprise.data_residency_example_domain": "octocorp.ghe.com",
}


def resolve_templates(text: str) -> str:
    """Resolve GitHub docs Liquid-style templates to plain text."""
    # Replace {% data variables.x.y %} with known values
    def replace_data(m: re.Match) -> str:
        key = m.group(1).strip()
        return TEMPLATE_VARS.get(key, key.split(".")[-1])

    text = re.sub(r"\{%\s*data\s+([\w.]+)\s*%\}", replace_data, text)

    # Strip ifversion blocks: keep fpt content, remove ghes/ghec-only
    # Simple approach: remove {% ifversion ghes %}...{% endif %} blocks
    # and keep {% ifversion fpt %}...{% endif %} content (unwrapped)
    # This handles the common case; nested blocks are rare in these docs.

    # Remove ghes-only blocks
    text = re.sub(
        r"\{%\s*ifversion\s+ghes\s*%\}.*?\{%\s*endif\s*%\}",
        "", text, flags=re.DOTALL,
    )
    # Remove 'not ghes' negation blocks - keep fpt content
    text = re.sub(
        r"\{%\s*ifversion\s+not\s+ghes\s*%\}(.*?)\{%\s*endif\s*%\}",
        r"\1", text, flags=re.DOTALL,
    )
    # Keep fpt blocks (unwrap)
    text = re.sub(
        r"\{%\s*ifversion\s+fpt\s*%\}(.*?)(?:\{%\s*endif\s*%\})",
        r"\1", text, flags=re.DOTALL,
    )
    # Keep 'fpt or ghec' blocks
    text = re.sub(
        r"\{%\s*ifversion\s+fpt\s+or\s+ghec\s*%\}(.*?)(?:\{%\s*endif\s*%\})",
        r"\1", text, flags=re.DOTALL,
    )
    # Remove ghec-only blocks
    text = re.sub(
        r"\{%\s*ifversion\s+ghec\s*%\}.*?\{%\s*endif\s*%\}",
        "", text, flags=re.DOTALL,
    )
    # Remove enterprise-installed-apps blocks
    text = re.sub(
        r"\{%\s*ifversion\s+enterprise-installed-apps\s*%\}.*?\{%\s*endif\s*%\}",
        "", text, flags=re.DOTALL,
    )

    # Catch any remaining {% ifversion ... %} ... {% endif %} and unwrap
    text = re.sub(
        r"\{%\s*ifversion\s+[^%]*%\}(.*?)\{%\s*endif\s*%\}",
        r"\1", text, flags=re.DOTALL,
    )

    # Replace [AUTOTITLE](path) with just the path description
    def replace_autotitle(m: re.Match) -> str:
        path = m.group(1)
        # Extract a readable title from the path
        parts = path.strip("/").split("/")
        if parts:
            title = parts[-1].replace("-", " ").title()
            return f"[{title}]({path})"
        return path

    text = re.sub(r"\[AUTOTITLE\]\(([^)]+)\)", replace_autotitle, text)

    # Remove remaining Liquid tags we don't handle
    text = re.sub(r"\{%\s*[^%]*%\}", "", text)

    # Remove octicon tags
    text = re.sub(r"\{%\s*octicon\s+[^%]*%\}", "", text)

    # Clean up excessive blank lines
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    return text


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML frontmatter from markdown body."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return {}, text[end + 3:].strip()
    return {}, text.strip()


# ---------------------------------------------------------------------------
# Schema processing
# ---------------------------------------------------------------------------

def classify_type(name: str) -> str:
    """Determine which domain a type belongs to based on its name."""
    # Special handling for audit entries - they have diverse prefixes
    if "AuditEntry" in name and not name.startswith("Organization"):
        return "audit-log"

    for domain, patterns in DOMAIN_RULES:
        for pattern in patterns:
            if name.startswith(pattern) or pattern in name:
                return domain
    return DEFAULT_DOMAIN


def classify_mutation(name: str) -> str:
    """Classify a mutation into a domain based on its name."""
    name_lower = name.lower()

    mutation_domain_keywords = [
        ("repositories", ["repository", "repo", "branch", "branchprotection", "topic", "deploykey", "ruleset"]),
        ("issues", ["issue", "label", "milestone"]),
        ("pull-requests", ["pullrequest", "review", "mergequeue", "merge"]),
        ("git-objects", ["commit", "ref"]),
        ("users-and-orgs", ["user", "organization", "org", "team", "invitation"]),
        ("projects", ["project", "draftissue"]),
        ("actions-and-ci", ["workflow", "check", "deployment", "environment"]),
        ("security", ["securityadvisory", "vulnerability", "dependabot"]),
        ("discussions", ["discussion"]),
        ("packages", ["package"]),
        ("sponsors", ["sponsor", "sponsorship"]),
        ("enterprise", ["enterprise"]),
        ("releases", ["release"]),
        ("apps-and-marketplace", ["app", "marketplace"]),
    ]

    for domain, keywords in mutation_domain_keywords:
        for kw in keywords:
            if kw in name_lower:
                return domain
    return DEFAULT_DOMAIN


def strip_html(text: str) -> str:
    """Remove HTML tags from description text."""
    if not text:
        return ""
    text = re.sub(r"</?p>", "", text)
    text = re.sub(r"</?code>", "`", text)
    text = re.sub(r"</?em>", "_", text)
    text = re.sub(r"</?strong>", "**", text)
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"<a\s+href=\"([^\"]+)\"[^>]*>([^<]+)</a>", r"[\2](\1)", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def format_type_ref(type_str: str) -> str:
    """Format a type reference for display."""
    return f"`{type_str}`"


def render_field(field: dict, indent: int = 0) -> str:
    """Render a single field definition."""
    prefix = "  " * indent
    name = field["name"]
    type_str = field.get("type", "")
    desc = strip_html(field.get("description", ""))

    line = f"{prefix}- **{name}** ({format_type_ref(type_str)})"
    if desc:
        line += f": {desc}"

    # Render arguments if present
    args = field.get("args", [])
    if args:
        line += "\n"
        for arg in args:
            arg_desc = strip_html(arg.get("description", ""))
            arg_line = f"{prefix}  - `{arg['name']}` ({format_type_ref(arg.get('type', ''))})"
            if arg_desc:
                arg_line += f": {arg_desc}"
            line += arg_line + "\n"

    return line


def render_object(obj: dict) -> str:
    """Render a full object/type definition as markdown."""
    lines = []
    name = obj["name"]
    kind = obj.get("kind", "")
    desc = strip_html(obj.get("description", ""))

    lines.append(f"### {name}\n")
    if desc:
        lines.append(f"{desc}\n")

    # Show implements
    implements = obj.get("implements", [])
    if implements:
        iface_names = [i.get("name", str(i)) if isinstance(i, dict) else str(i) for i in implements]
        lines.append(f"**Implements:** {', '.join(iface_names)}\n")

    # Fields
    fields = obj.get("fields", [])
    if fields:
        lines.append("**Fields:**\n")
        for f in fields:
            lines.append(render_field(f))
        lines.append("")

    # For enums: values
    values = obj.get("values", [])
    if values:
        lines.append("**Values:**\n")
        for v in values:
            v_desc = strip_html(v.get("description", ""))
            line = f"- `{v['name']}`"
            if v_desc:
                line += f": {v_desc}"
            lines.append(line)
        lines.append("")

    # For input objects: input fields
    input_fields = obj.get("inputFields", [])
    if input_fields:
        lines.append("**Input fields:**\n")
        for f in input_fields:
            lines.append(render_field(f))
        lines.append("")

    return "\n".join(lines)


def render_mutation(mut: dict) -> str:
    """Render a mutation definition as markdown."""
    lines = []
    name = mut["name"]
    desc = strip_html(mut.get("description", ""))

    lines.append(f"### {name}\n")
    if desc:
        lines.append(f"{desc}\n")

    input_fields = mut.get("inputFields", [])
    if input_fields:
        lines.append("**Input fields:**\n")
        for f in input_fields:
            lines.append(render_field(f))
        lines.append("")

    return_fields = mut.get("returnFields", [])
    if return_fields:
        lines.append("**Return fields:**\n")
        for f in return_fields:
            lines.append(render_field(f))
        lines.append("")

    return "\n".join(lines)


def render_query(q: dict) -> str:
    """Render a root query definition as markdown."""
    lines = []
    name = q["name"]
    type_str = q.get("type", "")
    desc = strip_html(q.get("description", ""))

    lines.append(f"### {name}\n")
    lines.append(f"**Returns:** {format_type_ref(type_str)}\n")
    if desc:
        lines.append(f"{desc}\n")

    args = q.get("args", [])
    if args:
        lines.append("**Arguments:**\n")
        for a in args:
            a_desc = strip_html(a.get("description", ""))
            line = f"- `{a['name']}` ({format_type_ref(a.get('type', ''))})"
            if a_desc:
                line += f": {a_desc}"
            lines.append(line)
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Build functions
# ---------------------------------------------------------------------------

def build_guide(docs_root: Path, output_dir: Path) -> None:
    """Compile the guides and overview docs into a single guide.md."""
    output_dir.mkdir(parents=True, exist_ok=True)

    guide_files = [
        # Overview
        ("overview", "about-the-graphql-api.md"),
        # Guides in logical order
        ("guides", "introduction-to-graphql.md"),
        ("guides", "forming-calls-with-graphql.md"),
        ("guides", "using-pagination-in-the-graphql-api.md"),
        ("guides", "using-global-node-ids.md"),
        ("guides", "migrating-from-rest-to-graphql.md"),
        ("guides", "using-the-graphql-api-for-discussions.md"),
        ("guides", "managing-enterprise-accounts.md"),
        # Overview docs
        ("overview", "rate-limits-and-query-limits-for-the-graphql-api.md"),
        ("overview", "breaking-changes.md"),
    ]

    sections = []
    sections.append("# GitHub GraphQL API — Usage Guide\n")
    sections.append(textwrap.dedent("""\
        This guide covers everything you need to know to work with the GitHub
        GraphQL API: authentication, forming queries and mutations, pagination,
        rate limits, and more.

        **Endpoint:** `https://api.github.com/graphql`
        **Method:** Always `POST` (except introspection `GET`)
        **Auth:** `Authorization: bearer TOKEN` header

    """))

    for subdir, filename in guide_files:
        filepath = docs_root / f"content/graphql/{subdir}/{filename}"
        if not filepath.exists():
            print(f"  Warning: {filepath} not found, skipping")
            continue

        text = filepath.read_text()
        _fm, body = extract_frontmatter(text)
        body = resolve_templates(body)

        # Skip autogenerated stub pages
        if "<!-- Content after this section is automatically generated -->" in body:
            body = body.split("<!-- Content after this section is automatically generated -->")[0]

        # Clean up
        body = body.strip()
        if body:
            sections.append(body)
            sections.append("\n---\n")

    guide_text = "\n".join(sections)
    (output_dir / "guide.md").write_text(guide_text)
    print(f"  Wrote guide.md ({len(guide_text)} bytes)")


def build_index(schema: dict, output_dir: Path) -> None:
    """Build a quick-reference index of all types."""
    output_dir.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# GitHub GraphQL API — Quick Reference Index\n")
    lines.append(textwrap.dedent("""\
        This index lists every type in the GitHub GraphQL API schema.
        Use it to find what exists, then look up details in the domain-specific
        reference files.

    """))

    # Root queries
    lines.append("## Root Queries\n")
    lines.append("These are the entry points for reading data.\n")
    for q in schema["queries"]:
        desc = strip_html(q.get("description", ""))
        lines.append(f"- **{q['name']}** → `{q.get('type', '')}`: {desc}")
    lines.append("")

    # Mutations (grouped alphabetically, one-line each)
    lines.append("## Mutations\n")
    lines.append(f"Total: {len(schema['mutations'])} mutations.\n")
    for m in sorted(schema["mutations"], key=lambda x: x["name"]):
        desc = strip_html(m.get("description", ""))
        if len(desc) > 120:
            desc = desc[:117] + "..."
        lines.append(f"- **{m['name']}**: {desc}")
    lines.append("")

    # Objects (just names and one-line descriptions)
    lines.append("## Objects\n")
    lines.append(f"Total: {len(schema['objects'])} object types.\n")
    for obj in sorted(schema["objects"], key=lambda x: x["name"]):
        desc = strip_html(obj.get("description", ""))
        if len(desc) > 120:
            desc = desc[:117] + "..."
        field_count = len(obj.get("fields", []))
        lines.append(f"- **{obj['name']}** ({field_count} fields): {desc}")
    lines.append("")

    # Interfaces
    lines.append("## Interfaces\n")
    lines.append(f"Total: {len(schema['interfaces'])} interfaces.\n")
    for iface in sorted(schema["interfaces"], key=lambda x: x["name"]):
        desc = strip_html(iface.get("description", ""))
        if len(desc) > 120:
            desc = desc[:117] + "..."
        lines.append(f"- **{iface['name']}**: {desc}")
    lines.append("")

    # Enums
    lines.append("## Enums\n")
    lines.append(f"Total: {len(schema['enums'])} enums.\n")
    for enum in sorted(schema["enums"], key=lambda x: x["name"]):
        desc = strip_html(enum.get("description", ""))
        values = [v["name"] for v in enum.get("values", [])]
        val_str = ", ".join(values[:8])
        if len(values) > 8:
            val_str += f", ... ({len(values)} total)"
        lines.append(f"- **{enum['name']}**: {val_str}")
    lines.append("")

    # Unions
    lines.append("## Unions\n")
    lines.append(f"Total: {len(schema['unions'])} unions.\n")
    for union in sorted(schema["unions"], key=lambda x: x["name"]):
        desc = strip_html(union.get("description", ""))
        members = union.get("possibleTypes", [])
        member_names = [m.get("name", str(m)) if isinstance(m, dict) else str(m) for m in members]
        lines.append(f"- **{union['name']}**: {', '.join(member_names[:6])}"
                     + (f" ... ({len(member_names)} total)" if len(member_names) > 6 else ""))
    lines.append("")

    # Input objects
    lines.append("## Input Objects\n")
    lines.append(f"Total: {len(schema['inputObjects'])} input types.\n")
    for inp in sorted(schema["inputObjects"], key=lambda x: x["name"]):
        desc = strip_html(inp.get("description", ""))
        if len(desc) > 120:
            desc = desc[:117] + "..."
        lines.append(f"- **{inp['name']}**: {desc}")
    lines.append("")

    # Scalars
    lines.append("## Scalars\n")
    for s in sorted(schema["scalars"], key=lambda x: x["name"]):
        desc = strip_html(s.get("description", ""))
        lines.append(f"- **{s['name']}**: {desc}")
    lines.append("")

    index_text = "\n".join(lines)
    (output_dir / "index.md").write_text(index_text)
    print(f"  Wrote index.md ({len(index_text)} bytes)")


def build_domains(schema: dict, output_dir: Path) -> None:
    """Build domain-organized reference files."""
    domains_dir = output_dir / "domains"
    domains_dir.mkdir(parents=True, exist_ok=True)

    # Classify everything into domains
    domain_objects: dict[str, list[dict]] = {}
    domain_mutations: dict[str, list[dict]] = {}
    domain_enums: dict[str, list[dict]] = {}
    domain_interfaces: dict[str, list[dict]] = {}
    domain_input_objects: dict[str, list[dict]] = {}
    domain_unions: dict[str, list[dict]] = {}

    for obj in schema["objects"]:
        domain = classify_type(obj["name"])
        domain_objects.setdefault(domain, []).append(obj)

    for mut in schema["mutations"]:
        domain = classify_mutation(mut["name"])
        domain_mutations.setdefault(domain, []).append(mut)

    for enum in schema["enums"]:
        domain = classify_type(enum["name"])
        domain_enums.setdefault(domain, []).append(enum)

    for iface in schema["interfaces"]:
        domain = classify_type(iface["name"])
        domain_interfaces.setdefault(domain, []).append(iface)

    for inp in schema["inputObjects"]:
        domain = classify_type(inp["name"])
        domain_input_objects.setdefault(domain, []).append(inp)

    for union in schema["unions"]:
        domain = classify_type(union["name"])
        domain_unions.setdefault(domain, []).append(union)

    # Get all domain names
    all_domains = set()
    for d in [domain_objects, domain_mutations, domain_enums,
              domain_interfaces, domain_input_objects, domain_unions]:
        all_domains.update(d.keys())

    # Render each domain file
    for domain in sorted(all_domains):
        title = DOMAIN_TITLES.get(domain, domain.replace("-", " ").title())
        lines = []
        lines.append(f"# {title}\n")

        # Queries that return types in this domain
        domain_obj_names = {o["name"] for o in domain_objects.get(domain, [])}
        related_queries = [
            q for q in schema["queries"]
            if q.get("type", "").rstrip("!").rstrip("]").lstrip("[") in domain_obj_names
            or classify_type(q.get("type", "").rstrip("!").rstrip("]").lstrip("[")) == domain
        ]
        if related_queries:
            lines.append("## Queries\n")
            for q in sorted(related_queries, key=lambda x: x["name"]):
                lines.append(render_query(q))

        # Mutations
        muts = domain_mutations.get(domain, [])
        if muts:
            lines.append("## Mutations\n")
            for m in sorted(muts, key=lambda x: x["name"]):
                lines.append(render_mutation(m))

        # Objects (skip Connection/Edge types for cleaner output - note them briefly)
        objs = domain_objects.get(domain, [])
        core_objs = [o for o in objs if not o["name"].endswith(("Connection", "Edge"))]
        conn_objs = [o for o in objs if o["name"].endswith(("Connection", "Edge"))]

        if core_objs:
            lines.append("## Types\n")
            for obj in sorted(core_objs, key=lambda x: x["name"]):
                lines.append(render_object(obj))

        if conn_objs:
            lines.append("## Connection & Edge Types\n")
            lines.append("_These follow the standard Relay connection pattern "
                         "(see the guide for pagination details)._\n")
            for obj in sorted(conn_objs, key=lambda x: x["name"]):
                desc = strip_html(obj.get("description", ""))
                field_count = len(obj.get("fields", []))
                lines.append(f"- **{obj['name']}** ({field_count} fields): {desc}")
            lines.append("")

        # Interfaces
        ifaces = domain_interfaces.get(domain, [])
        if ifaces:
            lines.append("## Interfaces\n")
            for iface in sorted(ifaces, key=lambda x: x["name"]):
                lines.append(render_object(iface))

        # Enums
        enums = domain_enums.get(domain, [])
        if enums:
            lines.append("## Enums\n")
            for enum in sorted(enums, key=lambda x: x["name"]):
                lines.append(render_object(enum))

        # Input objects
        inps = domain_input_objects.get(domain, [])
        if inps:
            lines.append("## Input Objects\n")
            for inp in sorted(inps, key=lambda x: x["name"]):
                lines.append(render_object(inp))

        # Unions
        unions = domain_unions.get(domain, [])
        if unions:
            lines.append("## Unions\n")
            for union in sorted(unions, key=lambda x: x["name"]):
                desc = strip_html(union.get("description", ""))
                members = union.get("possibleTypes", [])
                member_names = [m.get("name", str(m)) if isinstance(m, dict) else str(m) for m in members]
                lines.append(f"### {union['name']}\n")
                if desc:
                    lines.append(f"{desc}\n")
                lines.append(f"**Possible types:** {', '.join(member_names)}\n")

        domain_text = "\n".join(lines)
        out_path = domains_dir / f"{domain}.md"
        out_path.write_text(domain_text)
        print(f"  Wrote domains/{domain}.md ({len(domain_text)} bytes, "
              f"{len(core_objs)} types, {len(muts)} mutations)")


def build_changelog_summary(docs_root: Path, output_dir: Path) -> None:
    """Build a recent changelog summary."""
    changelog_path = docs_root / CHANGELOG_JSON
    if not changelog_path.exists():
        print("  Warning: changelog.json not found, skipping")
        return

    with open(changelog_path) as f:
        changelog = json.load(f)

    lines = []
    lines.append("# GitHub GraphQL API — Recent Schema Changes\n")
    lines.append("Last 50 changelog entries (most recent first).\n")

    for entry in changelog[:50]:
        date = entry.get("date", "unknown")
        lines.append(f"## {date}\n")

        for change_group in entry.get("schemaChanges", []):
            title = change_group.get("title", "")
            if title:
                lines.append(f"**{title}**\n")
            for change in change_group.get("changes", []):
                lines.append(f"- {strip_html(change)}")
            lines.append("")

        for preview in entry.get("previewChanges", []):
            title = preview.get("title", "")
            if title:
                lines.append(f"**{title}**\n")
            for change in preview.get("changes", []):
                lines.append(f"- {strip_html(change)}")
            lines.append("")

    changelog_text = "\n".join(lines)
    (output_dir / "changelog.md").write_text(changelog_text)
    print(f"  Wrote changelog.md ({len(changelog_text)} bytes)")


# ---------------------------------------------------------------------------
# Remote fetch support
# ---------------------------------------------------------------------------

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/github/docs/main"

# Files to fetch in remote mode
REMOTE_FILES = [
    "src/graphql/data/fpt/schema.json",
    "src/graphql/data/fpt/changelog.json",
    "content/graphql/overview/about-the-graphql-api.md",
    "content/graphql/guides/introduction-to-graphql.md",
    "content/graphql/guides/forming-calls-with-graphql.md",
    "content/graphql/guides/using-pagination-in-the-graphql-api.md",
    "content/graphql/guides/using-global-node-ids.md",
    "content/graphql/guides/migrating-from-rest-to-graphql.md",
    "content/graphql/guides/using-the-graphql-api-for-discussions.md",
    "content/graphql/guides/managing-enterprise-accounts.md",
    "content/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api.md",
    "content/graphql/overview/breaking-changes.md",
]


def fetch_remote_docs(target_dir: Path) -> None:
    """Fetch required files from GitHub's docs repo into target_dir."""
    for rel_path in REMOTE_FILES:
        url = f"{GITHUB_RAW_BASE}/{rel_path}"
        dest = target_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)

        print(f"  Fetching {rel_path}...")
        try:
            urllib.request.urlretrieve(url, dest)
        except urllib.error.HTTPError as e:
            print(f"    Warning: failed to fetch {rel_path}: {e}")
            continue


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    import os

    force_fetch = "--fetch" in sys.argv

    docs_root = Path(os.environ.get(DOCS_ROOT_ENV, DEFAULT_DOCS_ROOT))
    use_remote = force_fetch or not docs_root.exists()

    if use_remote:
        # Fetch files to a temp directory
        tmp_dir = Path(tempfile.mkdtemp(prefix="gh-graphql-docs-"))
        print(f"Fetching latest docs from GitHub (no local clone found)...")
        print(f"Temp dir: {tmp_dir}")
        fetch_remote_docs(tmp_dir)
        docs_root = tmp_dir
        print()
    else:
        print(f"Using local docs clone: {docs_root}")

    schema_path = docs_root / SCHEMA_JSON
    if not schema_path.exists():
        print(f"Error: schema.json not found at {schema_path}")
        sys.exit(1)

    print(f"Output dir: {OUTPUT_DIR}")
    print()

    # Load schema
    print("Loading schema...")
    with open(schema_path) as f:
        schema = json.load(f)
    print(f"  Loaded: {sum(len(v) for v in schema.values())} total items")
    print()

    # Build guide
    print("Building usage guide...")
    build_guide(docs_root, OUTPUT_DIR)
    print()

    # Build index
    print("Building quick reference index...")
    build_index(schema, OUTPUT_DIR)
    print()

    # Build domain reference files
    print("Building domain reference files...")
    build_domains(schema, OUTPUT_DIR)
    print()

    # Build changelog
    print("Building changelog summary...")
    build_changelog_summary(docs_root, OUTPUT_DIR)
    print()

    print("Done!")


if __name__ == "__main__":
    main()
