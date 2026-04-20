# Security Advisories & Vulnerability Alerts

## Queries

### securityAdvisories

**Returns:** `SecurityAdvisoryConnection!`

GitHub Security Advisories.

**Arguments:**

- `after` (`String`): Returns the elements in the list that come after the specified cursor.
- `before` (`String`): Returns the elements in the list that come before the specified cursor.
- `classifications` (`[SecurityAdvisoryClassification!]`): A list of classifications to filter advisories by.
- `epssPercentage` (`Float`): The EPSS percentage to filter advisories by.
- `epssPercentile` (`Float`): The EPSS percentile to filter advisories by.
- `first` (`Int`): Returns the first _n_ elements from the list.
- `identifier` (`SecurityAdvisoryIdentifierFilter`): Filter advisories by identifier, e.g. GHSA or CVE.
- `last` (`Int`): Returns the last _n_ elements from the list.
- `orderBy` (`SecurityAdvisoryOrder`): Ordering options for the returned topics.
- `publishedSince` (`DateTime`): Filter advisories to those published since a time in the past.
- `updatedSince` (`DateTime`): Filter advisories to those updated since a time in the past.

### securityAdvisory

**Returns:** `SecurityAdvisory`

Fetch a Security Advisory by its GHSA ID.

**Arguments:**

- `ghsaId` (`String!`): GitHub Security Advisory ID.

### securityVulnerabilities

**Returns:** `SecurityVulnerabilityConnection!`

Software Vulnerabilities documented by GitHub Security Advisories.

**Arguments:**

- `after` (`String`): Returns the elements in the list that come after the specified cursor.
- `before` (`String`): Returns the elements in the list that come before the specified cursor.
- `classifications` (`[SecurityAdvisoryClassification!]`): A list of advisory classifications to filter vulnerabilities by.
- `ecosystem` (`SecurityAdvisoryEcosystem`): An ecosystem to filter vulnerabilities by.
- `first` (`Int`): Returns the first _n_ elements from the list.
- `last` (`Int`): Returns the last _n_ elements from the list.
- `orderBy` (`SecurityVulnerabilityOrder`): Ordering options for the returned topics.
- `package` (`String`): A package name to filter vulnerabilities by.
- `severities` (`[SecurityAdvisorySeverity!]`): A list of severities to filter vulnerabilities by.

## Types

### CVSS

The Common Vulnerability Scoring System.

**Fields:**

- **score** (`Float!`): The CVSS score associated with this advisory.
- **vectorString** (`String`): The CVSS vector string associated with this advisory.

### CWE

A common weakness enumeration.

**Implements:** Node

**Fields:**

- **cweId** (`String!`): The id of the CWE.
- **description** (`String!`): A detailed description of this CWE.
- **id** (`ID!`): The Node ID of the CWE object.
- **name** (`String!`): The name of this CWE.

### CodeScanningParameters

Choose which tools must provide code scanning results before the reference is
updated. When configured, code scanning must be enabled and have results for
both the commit and the reference being updated.

**Fields:**

- **codeScanningTools** (`[CodeScanningTool!]!`): Tools that must provide code scanning results for this rule to pass.

### CodeScanningTool

A tool that must provide code scanning results for this rule to pass.

**Fields:**

- **alertsThreshold** (`String!`): The severity level at which code scanning results that raise alerts block a
reference update. For more information on alert severity levels, see "[About code scanning alerts]($%7BexternalDocsUrl%7D/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).".
- **securityAlertsThreshold** (`String!`): The severity level at which code scanning results that raise security alerts
block a reference update. For more information on security severity levels,
see "[About code scanning alerts]($%7BexternalDocsUrl%7D/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).".
- **tool** (`String!`): The name of a code scanning tool.

### DependabotUpdate

A Dependabot Update for a dependency in a repository.

**Implements:** RepositoryNode

**Fields:**

- **error** (`DependabotUpdateError`): The error from a dependency update.
- **pullRequest** (`PullRequest`): The associated pull request.
- **repository** (`Repository!`): The repository associated with this node.

### DependabotUpdateError

An error produced from a Dependabot Update.

**Fields:**

- **body** (`String!`): The body of the error.
- **errorType** (`String!`): The error code.
- **title** (`String!`): The title of the error.

### DependencyGraphDependency

A dependency manifest entry.

**Fields:**

- **hasDependencies** (`Boolean!`): Does the dependency itself have dependencies?.
- **packageLabel** (`String!`): The original name of the package, as it appears in the manifest.
- **packageManager** (`String`): The dependency package manager.
- **packageName** (`String!`): The name of the package in the canonical form used by the package manager.
- **packageUrl** (`URI`): Public preview: The dependency package URL.
- **relationship** (`String!`): Public preview: The relationship of the dependency. Can be direct, transitive, or unknown.
- **repository** (`Repository`): The repository containing the package.
- **requirements** (`String!`): The dependency version requirements.

### DependencyGraphManifest

Dependency manifest for a repository.

**Implements:** Node

**Fields:**

- **blobPath** (`String!`): Path to view the manifest file blob.
- **dependencies** (`DependencyGraphDependencyConnection`): A list of manifest dependencies.
- **dependenciesCount** (`Int`): The number of dependencies listed in the manifest.
- **exceedsMaxSize** (`Boolean!`): Is the manifest too big to parse?.
- **filename** (`String!`): Fully qualified manifest filename.
- **id** (`ID!`): The Node ID of the DependencyGraphManifest object.
- **parseable** (`Boolean!`): Were we able to parse the manifest?.
- **repository** (`Repository!`): The repository containing the manifest.

### EPSS

The Exploit Prediction Scoring System.

**Fields:**

- **percentage** (`Float`): The EPSS percentage represents the likelihood of a CVE being exploited.
- **percentile** (`Float`): The EPSS percentile represents the relative rank of the CVE's likelihood of being exploited compared to other CVEs.

### SecurityAdvisory

A GitHub Security Advisory.

**Implements:** Node

**Fields:**

- **classification** (`SecurityAdvisoryClassification!`): The classification of the advisory.
- **cvss** (`CVSS!`): The CVSS associated with this advisory.
- **cvssSeverities** (`CvssSeverities!`): The CVSS associated with this advisory.
- **cwes** (`CWEConnection!`): CWEs associated with this Advisory.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **description** (`String!`): This is a long plaintext description of the advisory.
- **epss** (`EPSS`): The Exploit Prediction Scoring System.
- **ghsaId** (`String!`): The GitHub Security Advisory ID.
- **id** (`ID!`): The Node ID of the SecurityAdvisory object.
- **identifiers** (`[SecurityAdvisoryIdentifier!]!`): A list of identifiers for this advisory.
- **notificationsPermalink** (`URI`): The permalink for the advisory's dependabot alerts page.
- **origin** (`String!`): The organization that originated the advisory.
- **permalink** (`URI`): The permalink for the advisory.
- **publishedAt** (`DateTime!`): When the advisory was published.
- **references** (`[SecurityAdvisoryReference!]!`): A list of references for this advisory.
- **severity** (`SecurityAdvisorySeverity!`): The severity of the advisory.
- **summary** (`String!`): A short plaintext summary of the advisory.
- **updatedAt** (`DateTime!`): When the advisory was last updated.
- **vulnerabilities** (`SecurityVulnerabilityConnection!`): Vulnerabilities associated with this Advisory.
- **withdrawnAt** (`DateTime`): When the advisory was withdrawn, if it has been withdrawn.

### SecurityAdvisoryIdentifier

A GitHub Security Advisory Identifier.

**Fields:**

- **type** (`String!`): The identifier type, e.g. GHSA, CVE.
- **value** (`String!`): The identifier.

### SecurityAdvisoryPackage

An individual package.

**Fields:**

- **ecosystem** (`SecurityAdvisoryEcosystem!`): The ecosystem the package belongs to, e.g. RUBYGEMS, NPM.
- **name** (`String!`): The package name.

### SecurityAdvisoryPackageVersion

An individual package version.

**Fields:**

- **identifier** (`String!`): The package name or version.

### SecurityVulnerability

An individual vulnerability within an Advisory.

**Fields:**

- **advisory** (`SecurityAdvisory!`): The Advisory associated with this Vulnerability.
- **firstPatchedVersion** (`SecurityAdvisoryPackageVersion`): The first version containing a fix for the vulnerability.
- **package** (`SecurityAdvisoryPackage!`): A description of the vulnerable package.
- **severity** (`SecurityAdvisorySeverity!`): The severity of the vulnerability within this package.
- **updatedAt** (`DateTime!`): When the vulnerability was last updated.
- **vulnerableVersionRange** (`String!`): A string that describes the vulnerable package versions.
This string follows a basic syntax with a few forms.

`= 0.2.0` denotes a single vulnerable version.
`&#x3C;= 1.0.8` denotes a version range up to and including the specified version
`&#x3C; 0.1.11` denotes a version range up to, but excluding, the specified version
`>= 4.3.0, &#x3C; 4.3.5` denotes a version range with a known minimum and maximum version.
`>= 0.0.1` denotes a version range with a known minimum, but no known maximum.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **CWEConnection** (4 fields): The connection type for CWE.
- **CWEEdge** (2 fields): An edge in a connection.
- **DependencyGraphDependencyConnection** (4 fields): The connection type for DependencyGraphDependency.
- **DependencyGraphDependencyEdge** (2 fields): An edge in a connection.
- **DependencyGraphManifestConnection** (4 fields): The connection type for DependencyGraphManifest.
- **DependencyGraphManifestEdge** (2 fields): An edge in a connection.
- **SecurityAdvisoryConnection** (4 fields): The connection type for SecurityAdvisory.
- **SecurityAdvisoryEdge** (2 fields): An edge in a connection.
- **SecurityVulnerabilityConnection** (4 fields): The connection type for SecurityVulnerability.
- **SecurityVulnerabilityEdge** (2 fields): An edge in a connection.

## Enums

### DependencyGraphEcosystem

The possible ecosystems of a dependency graph package.

**Values:**

- `ACTIONS`: GitHub Actions.
- `COMPOSER`: PHP packages hosted at packagist.org.
- `GO`: Go modules.
- `MAVEN`: Java artifacts hosted at the Maven central repository.
- `NPM`: JavaScript packages hosted at npmjs.com.
- `NUGET`: .NET packages hosted at the NuGet Gallery.
- `PIP`: Python packages hosted at PyPI.org.
- `PUB`: Dart packages hosted at pub.dev.
- `RUBYGEMS`: Ruby gems hosted at RubyGems.org.
- `RUST`: Rust crates.
- `SWIFT`: Swift packages.

### SecurityAdvisoryClassification

Classification of the advisory.

**Values:**

- `GENERAL`: Classification of general advisories.
- `MALWARE`: Classification of malware advisories.

### SecurityAdvisoryEcosystem

The possible ecosystems of a security vulnerability's package.

**Values:**

- `ACTIONS`: GitHub Actions.
- `COMPOSER`: PHP packages hosted at packagist.org.
- `ERLANG`: Erlang/Elixir packages hosted at hex.pm.
- `GO`: Go modules.
- `MAVEN`: Java artifacts hosted at the Maven central repository.
- `NPM`: JavaScript packages hosted at npmjs.com.
- `NUGET`: .NET packages hosted at the NuGet Gallery.
- `PIP`: Python packages hosted at PyPI.org.
- `PUB`: Dart packages hosted at pub.dev.
- `RUBYGEMS`: Ruby gems hosted at RubyGems.org.
- `RUST`: Rust crates.
- `SWIFT`: Swift packages.

### SecurityAdvisoryIdentifierType

Identifier formats available for advisories.

**Values:**

- `CVE`: Common Vulnerabilities and Exposures Identifier.
- `GHSA`: GitHub Security Advisory ID.

### SecurityAdvisoryOrderField

Properties by which security advisory connections can be ordered.

**Values:**

- `EPSS_PERCENTAGE`: Order advisories by EPSS percentage.
- `EPSS_PERCENTILE`: Order advisories by EPSS percentile.
- `PUBLISHED_AT`: Order advisories by publication time.
- `UPDATED_AT`: Order advisories by update time.

### SecurityAdvisorySeverity

Severity of the vulnerability.

**Values:**

- `CRITICAL`: Critical.
- `HIGH`: High.
- `LOW`: Low.
- `MODERATE`: Moderate.

### SecurityVulnerabilityOrderField

Properties by which security vulnerability connections can be ordered.

**Values:**

- `UPDATED_AT`: Order vulnerability by update time.

## Input Objects

### CodeScanningParametersInput

Choose which tools must provide code scanning results before the reference is
updated. When configured, code scanning must be enabled and have results for
both the commit and the reference being updated.

**Input fields:**

- **codeScanningTools** (`[CodeScanningToolInput!]!`): Tools that must provide code scanning results for this rule to pass.

### CodeScanningToolInput

A tool that must provide code scanning results for this rule to pass.

**Input fields:**

- **alertsThreshold** (`String!`): The severity level at which code scanning results that raise alerts block a
reference update. For more information on alert severity levels, see "[About code scanning alerts]($%7BexternalDocsUrl%7D/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).".
- **securityAlertsThreshold** (`String!`): The severity level at which code scanning results that raise security alerts
block a reference update. For more information on security severity levels,
see "[About code scanning alerts]($%7BexternalDocsUrl%7D/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).".
- **tool** (`String!`): The name of a code scanning tool.

### SecurityAdvisoryIdentifierFilter

An advisory identifier to filter results on.

**Input fields:**

- **type** (`SecurityAdvisoryIdentifierType!`): The identifier type.
- **value** (`String!`): The identifier string. Supports exact or partial matching.

### SecurityAdvisoryOrder

Ordering options for security advisory connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`SecurityAdvisoryOrderField!`): The field to order security advisories by.

### SecurityVulnerabilityOrder

Ordering options for security vulnerability connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`SecurityVulnerabilityOrderField!`): The field to order security vulnerabilities by.
