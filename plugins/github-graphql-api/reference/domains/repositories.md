# Repositories & Repository Settings

## Queries

### codeOfConduct

**Returns:** `CodeOfConduct`

Look up a code of conduct by its key.

**Arguments:**

- `key` (`String!`): The code of conduct's key.

### codesOfConduct

**Returns:** `[CodeOfConduct]`

Look up a code of conduct by its key.

### license

**Returns:** `License`

Look up an open source license by its key.

**Arguments:**

- `key` (`String!`): The license's downcased SPDX ID.

### licenses

**Returns:** `[License]!`

Return a list of known open source licenses.

### repository

**Returns:** `Repository`

Lookup a given repository by the owner and repository name.

**Arguments:**

- `followRenames` (`Boolean`): Follow repository renames. If disabled, a repository referenced by its old name will return an error.
- `name` (`String!`): The name of the repository.
- `owner` (`String!`): The login field of a user or organization.

### repositoryOwner

**Returns:** `RepositoryOwner`

Lookup a repository owner (ie. either a User or an Organization) by login.

**Arguments:**

- `login` (`String!`): The username to lookup the owner by.

### topic

**Returns:** `Topic`

Look up a topic by name.

**Arguments:**

- `name` (`String!`): The topic's name.

## Mutations

### abortRepositoryMigration

Abort a repository migration queued or in progress.

**Input fields:**

- **input** (`AbortRepositoryMigrationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **success** (`Boolean`): Did the operation succeed?.

### acceptTopicSuggestion

Applies a suggested topic to the repository.

**Input fields:**

- **input** (`AcceptTopicSuggestionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **topic** (`Topic`): The accepted topic.

### accessUserNamespaceRepository

Access user namespace repository for a temporary duration.

**Input fields:**

- **input** (`AccessUserNamespaceRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **expiresAt** (`DateTime`): The time that repository access expires at.
- **repository** (`Repository`): The repository that is temporarily accessible.

### archiveRepository

Marks a repository as archived.

**Input fields:**

- **input** (`ArchiveRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The repository that was marked as archived.

### cloneTemplateRepository

Create a new repository with the same files and directory structure as a template repository.

**Input fields:**

- **input** (`CloneTemplateRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The new repository.

### createBranchProtectionRule

Create a new branch protection rule.

**Input fields:**

- **input** (`CreateBranchProtectionRuleInput!`)

**Return fields:**

- **branchProtectionRule** (`BranchProtectionRule`): The newly created BranchProtectionRule.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### createCommitOnBranch

Appends a commit to the given branch as the authenticated user.
This mutation creates a commit whose parent is the HEAD of the provided
branch and also updates that branch to point to the new commit.
It can be thought of as similar to `git commit`.
Locating a Branch
Commits are appended to a `branch` of type `Ref`.
This must refer to a git branch (i.e.  the fully qualified path must
begin with `refs/heads/`, although including this prefix is optional.
Callers may specify the `branch` to commit to either by its global node
ID or by passing both of `repositoryNameWithOwner` and `refName`.  For
more details see the documentation for `CommittableBranch`.
Describing Changes
`fileChanges` are specified as a `FilesChanges` object describing
`FileAdditions` and `FileDeletions`.
Please see the documentation for `FileChanges` for more information on
how to use this argument to describe any set of file changes.
Authorship
Similar to the web commit interface, this mutation does not support
specifying the author or committer of the commit and will not add
support for this in the future.
A commit created by a successful execution of this mutation will be
authored by the owner of the credential which authenticates the API
request.  The committer will be identical to that of commits authored
using the web interface.
If you need full control over author and committer information, please
use the Git Database REST API instead.
Commit Signing
Commits made using this mutation are automatically signed by GitHub if
supported and will be marked as verified in the user interface.

**Input fields:**

- **input** (`CreateCommitOnBranchInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **commit** (`Commit`): The new commit.
- **ref** (`Ref`): The ref which has been updated to point to the new commit.

### createLinkedBranch

Create a branch linked to an issue.

**Input fields:**

- **input** (`CreateLinkedBranchInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue that was linked to.
- **linkedBranch** (`LinkedBranch`): The new branch issue reference.

### createRepository

Create a new repository.

**Input fields:**

- **input** (`CreateRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The new repository.

### createRepositoryCustomProperty

Create a repository custom property.

**Input fields:**

- **input** (`CreateRepositoryCustomPropertyInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryCustomProperty** (`RepositoryCustomProperty`): The newly created repository custom property.

### createRepositoryRuleset

Create a repository ruleset.

**Input fields:**

- **input** (`CreateRepositoryRulesetInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ruleset** (`RepositoryRuleset`): The newly created Ruleset.

### declineTopicSuggestion

Rejects a suggested topic for the repository.

**Input fields:**

- **input** (`DeclineTopicSuggestionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **topic** (`Topic`): The declined topic.

### deleteBranchProtectionRule

Delete a branch protection rule.

**Input fields:**

- **input** (`DeleteBranchProtectionRuleInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### deleteLinkedBranch

Unlink a branch from an issue.

**Input fields:**

- **input** (`DeleteLinkedBranchInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue the linked branch was unlinked from.

### deleteRepositoryCustomProperty

Delete a repository custom property.

**Input fields:**

- **input** (`DeleteRepositoryCustomPropertyInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryCustomProperty** (`RepositoryCustomProperty`): The deleted custom property.

### deleteRepositoryRuleset

Delete a repository ruleset.

**Input fields:**

- **input** (`DeleteRepositoryRulesetInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### dismissRepositoryVulnerabilityAlert

Dismisses the Dependabot alert.

**Input fields:**

- **input** (`DismissRepositoryVulnerabilityAlertInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryVulnerabilityAlert** (`RepositoryVulnerabilityAlert`): The Dependabot alert that was dismissed.

### linkProjectV2ToRepository

Links a project to a repository.

**Input fields:**

- **input** (`LinkProjectV2ToRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The repository the project is linked to.

### linkRepositoryToProject

Creates a repository link for a project.

**Input fields:**

- **input** (`LinkRepositoryToProjectInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **project** (`Project`): The linked Project.
- **repository** (`Repository`): The linked Repository.

### mergeBranch

Merge a head into a branch.

**Input fields:**

- **input** (`MergeBranchInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **mergeCommit** (`Commit`): The resulting merge Commit.

### promoteRepositoryCustomProperty

Promote a repository custom property to the enterprise level.

**Input fields:**

- **input** (`PromoteRepositoryCustomPropertyInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryCustomProperty** (`RepositoryCustomProperty`): The repository custom property that has been promoted.

### setRepositoryCustomPropertyValues

Set repository custom property values for a repository.

**Input fields:**

- **input** (`SetRepositoryCustomPropertyValuesInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The repository that the custom properties were set for.

### setRepositoryInteractionLimit

Sets an interaction limit setting for a repository.

**Input fields:**

- **input** (`SetRepositoryInteractionLimitInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The repository that the interaction limit was set for.

### startRepositoryMigration

Starts a GitHub Enterprise Importer (GEI) repository migration.

**Input fields:**

- **input** (`StartRepositoryMigrationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryMigration** (`RepositoryMigration`): The new repository migration.

### unarchiveRepository

Unarchives a repository.

**Input fields:**

- **input** (`UnarchiveRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The repository that was unarchived.

### unlinkProjectV2FromRepository

Unlinks a project from a repository.

**Input fields:**

- **input** (`UnlinkProjectV2FromRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The repository the project is no longer linked to.

### unlinkRepositoryFromProject

Deletes a repository link from a project.

**Input fields:**

- **input** (`UnlinkRepositoryFromProjectInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **project** (`Project`): The linked Project.
- **repository** (`Repository`): The linked Repository.

### updateBranchProtectionRule

Update a branch protection rule.

**Input fields:**

- **input** (`UpdateBranchProtectionRuleInput!`)

**Return fields:**

- **branchProtectionRule** (`BranchProtectionRule`): The newly created BranchProtectionRule.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### updateEnterpriseAllowPrivateRepositoryForkingSetting

Sets whether private repository forks are enabled for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated allow private repository forking setting.
- **message** (`String`): A message confirming the result of updating the allow private repository forking setting.

### updateEnterpriseDefaultRepositoryPermissionSetting

Sets the base repository permission for organizations in an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseDefaultRepositoryPermissionSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated base repository permission setting.
- **message** (`String`): A message confirming the result of updating the base repository permission setting.

### updateEnterpriseDeployKeySetting

Sets whether deploy keys are allowed to be created and used for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseDeployKeySettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated deploy key setting.
- **message** (`String`): A message confirming the result of updating the deploy key setting.

### updateEnterpriseMembersCanChangeRepositoryVisibilitySetting

Sets whether organization members with admin permissions on a repository can change repository visibility.

**Input fields:**

- **input** (`UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated members can change repository visibility setting.
- **message** (`String`): A message confirming the result of updating the members can change repository visibility setting.

### updateEnterpriseMembersCanCreateRepositoriesSetting

Sets the members can create repositories setting for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseMembersCanCreateRepositoriesSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated members can create repositories setting.
- **message** (`String`): A message confirming the result of updating the members can create repositories setting.

### updateEnterpriseMembersCanDeleteRepositoriesSetting

Sets the members can delete repositories setting for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated members can delete repositories setting.
- **message** (`String`): A message confirming the result of updating the members can delete repositories setting.

### updateEnterpriseMembersCanUpdateProtectedBranchesSetting

Sets the members can update protected branches setting for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated members can update protected branches setting.
- **message** (`String`): A message confirming the result of updating the members can update protected branches setting.

### updateEnterpriseRepositoryProjectsSetting

Sets whether repository projects are enabled for a enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseRepositoryProjectsSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated repository projects setting.
- **message** (`String`): A message confirming the result of updating the repository projects setting.

### updateOrganizationAllowPrivateRepositoryForkingSetting

Sets whether private repository forks are enabled for an organization.

**Input fields:**

- **input** (`UpdateOrganizationAllowPrivateRepositoryForkingSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **message** (`String`): A message confirming the result of updating the allow private repository forking setting.
- **organization** (`Organization`): The organization with the updated allow private repository forking setting.

### updatePullRequestBranch

Merge or Rebase HEAD from upstream branch into pull request branch.

**Input fields:**

- **input** (`UpdatePullRequestBranchInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **pullRequest** (`PullRequest`): The updated pull request.

### updateRepository

Update information about a repository.

**Input fields:**

- **input** (`UpdateRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The updated repository.

### updateRepositoryCustomProperty

Update a repository custom property.

**Input fields:**

- **input** (`UpdateRepositoryCustomPropertyInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryCustomProperty** (`RepositoryCustomProperty`): The updated repository custom property.

### updateRepositoryRuleset

Update a repository ruleset.

**Input fields:**

- **input** (`UpdateRepositoryRulesetInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ruleset** (`RepositoryRuleset`): The newly created Ruleset.

### updateRepositoryWebCommitSignoffSetting

Sets whether contributors are required to sign off on web-based commits for a repository.

**Input fields:**

- **input** (`UpdateRepositoryWebCommitSignoffSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **message** (`String`): A message confirming the result of updating the web commit signoff setting.
- **repository** (`Repository`): The updated repository.

### updateTeamsRepository

Update team repository.

**Input fields:**

- **input** (`UpdateTeamsRepositoryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The repository that was updated.
- **teams** (`[Team!]`): The teams granted permission on the repository.

### updateTopics

Replaces the repository's topics with the given topics.

**Input fields:**

- **input** (`UpdateTopicsInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invalidTopicNames** (`[String!]`): Names of the provided topics that are not valid.
- **repository** (`Repository`): The updated repository.

## Types

### BranchProtectionRule

A branch protection rule.

**Implements:** Node

**Fields:**

- **allowsDeletions** (`Boolean!`): Can this branch be deleted.
- **allowsForcePushes** (`Boolean!`): Are force pushes allowed on this branch.
- **blocksCreations** (`Boolean!`): Is branch creation a protected operation.
- **branchProtectionRuleConflicts** (`BranchProtectionRuleConflictConnection!`): A list of conflicts matching branches protection rule and other branch protection rules.
- **bypassForcePushAllowances** (`BypassForcePushAllowanceConnection!`): A list of actors able to force push for this branch protection rule.
- **bypassPullRequestAllowances** (`BypassPullRequestAllowanceConnection!`): A list of actors able to bypass PRs for this branch protection rule.
- **creator** (`Actor`): The actor who created this branch protection rule.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **dismissesStaleReviews** (`Boolean!`): Will new commits pushed to matching branches dismiss pull request review approvals.
- **id** (`ID!`): The Node ID of the BranchProtectionRule object.
- **isAdminEnforced** (`Boolean!`): Can admins override branch protection.
- **lockAllowsFetchAndMerge** (`Boolean!`): Whether users can pull changes from upstream when the branch is locked. Set to
`true` to allow fork syncing. Set to `false` to prevent fork syncing.
- **lockBranch** (`Boolean!`): Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.
- **matchingRefs** (`RefConnection!`): Repository refs that are protected by this rule.
- **pattern** (`String!`): Identifies the protection rule pattern.
- **pushAllowances** (`PushAllowanceConnection!`): A list push allowances for this branch protection rule.
- **repository** (`Repository`): The repository associated with this branch protection rule.
- **requireLastPushApproval** (`Boolean!`): Whether the most recent push must be approved by someone other than the person who pushed it.
- **requiredApprovingReviewCount** (`Int`): Number of approving reviews required to update matching branches.
- **requiredDeploymentEnvironments** (`[String]`): List of required deployment environments that must be deployed successfully to update matching branches.
- **requiredStatusCheckContexts** (`[String]`): List of required status check contexts that must pass for commits to be accepted to matching branches.
- **requiredStatusChecks** (`[RequiredStatusCheckDescription!]`): List of required status checks that must pass for commits to be accepted to matching branches.
- **requiresApprovingReviews** (`Boolean!`): Are approving reviews required to update matching branches.
- **requiresCodeOwnerReviews** (`Boolean!`): Are reviews from code owners required to update matching branches.
- **requiresCommitSignatures** (`Boolean!`): Are commits required to be signed.
- **requiresConversationResolution** (`Boolean!`): Are conversations required to be resolved before merging.
- **requiresDeployments** (`Boolean!`): Does this branch require deployment to specific environments before merging.
- **requiresLinearHistory** (`Boolean!`): Are merge commits prohibited from being pushed to this branch.
- **requiresStatusChecks** (`Boolean!`): Are status checks required to update matching branches.
- **requiresStrictStatusChecks** (`Boolean!`): Are branches required to be up to date before merging.
- **restrictsPushes** (`Boolean!`): Is pushing to matching branches restricted.
- **restrictsReviewDismissals** (`Boolean!`): Is dismissal of pull request reviews restricted.
- **reviewDismissalAllowances** (`ReviewDismissalAllowanceConnection!`): A list review dismissal allowances for this branch protection rule.

### BranchProtectionRuleConflict

A conflict between two branch protection rules.

**Fields:**

- **branchProtectionRule** (`BranchProtectionRule`): Identifies the branch protection rule.
- **conflictingBranchProtectionRule** (`BranchProtectionRule`): Identifies the conflicting branch protection rule.
- **ref** (`Ref`): Identifies the branch ref that has conflicting rules.

### CodeOfConduct

The Code of Conduct for a repository.

**Implements:** Node

**Fields:**

- **body** (`String`): The body of the Code of Conduct.
- **id** (`ID!`): The Node ID of the CodeOfConduct object.
- **key** (`String!`): The key for the Code of Conduct.
- **name** (`String!`): The formal name of the Code of Conduct.
- **resourcePath** (`URI`): The HTTP path for this Code of Conduct.
- **url** (`URI`): The HTTP URL for this Code of Conduct.

### CommitContributionsByRepository

This aggregates commits made by a user within one repository.

**Fields:**

- **contributions** (`CreatedCommitContributionConnection!`): The commit contributions, each representing a day.
- **repository** (`Repository!`): The repository in which the commits were made.
- **resourcePath** (`URI!`): The HTTP path for the user's commits to the repository in this time range.
- **url** (`URI!`): The HTTP URL for the user's commits to the repository in this time range.

### ContributingGuidelines

The Contributing Guidelines for a repository.

**Fields:**

- **body** (`String`): The body of the Contributing Guidelines.
- **resourcePath** (`URI`): The HTTP path for the Contributing Guidelines.
- **url** (`URI`): The HTTP URL for the Contributing Guidelines.

### CreatedRepositoryContribution

Represents the contribution a user made on GitHub by creating a repository.

**Implements:** Contribution

**Fields:**

- **isRestricted** (`Boolean!`): Whether this contribution is associated with a record you do not have access to. For
example, your own 'first issue' contribution may have been made on a repository you can no
longer access.
- **occurredAt** (`DateTime!`): When this contribution was made.
- **repository** (`Repository!`): The repository that was created.
- **resourcePath** (`URI!`): The HTTP path for this contribution.
- **url** (`URI!`): The HTTP URL for this contribution.
- **user** (`User!`): The user who made this contribution.

### DeployKey

A repository deploy key.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **enabled** (`Boolean!`): Whether or not the deploy key is enabled by policy at the Enterprise or Organization level.
- **id** (`ID!`): The Node ID of the DeployKey object.
- **key** (`String!`): The deploy key.
- **readOnly** (`Boolean!`): Whether or not the deploy key is read only.
- **title** (`String!`): The deploy key title.
- **verified** (`Boolean!`): Whether or not the deploy key has been verified.

### EnterpriseRepositoryInfo

A subset of repository information queryable from an enterprise.

**Implements:** Node

**Fields:**

- **id** (`ID!`): The Node ID of the EnterpriseRepositoryInfo object.
- **isPrivate** (`Boolean!`): Identifies if the repository is private or internal.
- **name** (`String!`): The repository's name.
- **nameWithOwner** (`String!`): The repository's name with owner.

### FundingLink

A funding platform link for a repository.

**Fields:**

- **platform** (`FundingPlatform!`): The funding platform this link is for.
- **url** (`URI!`): The configured URL for this funding link.

### IssueContributionsByRepository

This aggregates issues opened by a user within one repository.

**Fields:**

- **contributions** (`CreatedIssueContributionConnection!`): The issue contributions.
- **repository** (`Repository!`): The repository in which the issues were opened.

### License

A repository's open source license.

**Implements:** Node

**Fields:**

- **body** (`String!`): The full text of the license.
- **conditions** (`[LicenseRule]!`): The conditions set by the license.
- **description** (`String`): A human-readable description of the license.
- **featured** (`Boolean!`): Whether the license should be featured.
- **hidden** (`Boolean!`): Whether the license should be displayed in license pickers.
- **id** (`ID!`): The Node ID of the License object.
- **implementation** (`String`): Instructions on how to implement the license.
- **key** (`String!`): The lowercased SPDX ID of the license.
- **limitations** (`[LicenseRule]!`): The limitations set by the license.
- **name** (`String!`): The license full name specified by [https://spdx.org/licenses](https://spdx.org/licenses).
- **nickname** (`String`): Customary short name if applicable (e.g, GPLv3).
- **permissions** (`[LicenseRule]!`): The permissions set by the license.
- **pseudoLicense** (`Boolean!`): Whether the license is a pseudo-license placeholder (e.g., other, no-license).
- **spdxId** (`String`): Short identifier specified by [https://spdx.org/licenses](https://spdx.org/licenses).
- **url** (`URI`): URL to the license on [https://choosealicense.com](https://choosealicense.com).

### LicenseRule

Describes a License's conditions, permissions, and limitations.

**Fields:**

- **description** (`String!`): A description of the rule.
- **key** (`String!`): The machine-readable rule key.
- **label** (`String!`): The human-readable rule label.

### LinkedBranch

A branch linked to an issue.

**Implements:** Node

**Fields:**

- **id** (`ID!`): The Node ID of the LinkedBranch object.
- **ref** (`Ref`): The branch's ref.

### ProjectV2ItemFieldRepositoryValue

The value of a repository field in a Project item.

**Fields:**

- **field** (`ProjectV2FieldConfiguration!`): The field that contains this value.
- **repository** (`Repository`): The repository for this field.

### PullRequestContributionsByRepository

This aggregates pull requests opened by a user within one repository.

**Fields:**

- **contributions** (`CreatedPullRequestContributionConnection!`): The pull request contributions.
- **repository** (`Repository!`): The repository in which the pull requests were opened.

### PullRequestReviewContributionsByRepository

This aggregates pull request reviews made by a user within one repository.

**Fields:**

- **contributions** (`CreatedPullRequestReviewContributionConnection!`): The pull request review contributions.
- **repository** (`Repository!`): The repository in which the pull request reviews were made.

### Repository

A repository contains the content for a project.

**Implements:** Node, PackageOwner, ProjectOwner, ProjectV2Recent, RepositoryInfo, Starrable, Subscribable, UniformResourceLocatable

**Fields:**

- **allowUpdateBranch** (`Boolean!`): Whether or not a pull request head branch that is behind its base branch can
always be updated even if it is not required to be up to date before merging.
- **archivedAt** (`DateTime`): Identifies the date and time when the repository was archived.
- **assignableUsers** (`UserConnection!`): A list of users that can be assigned to issues in this repository.
- **autoMergeAllowed** (`Boolean!`): Whether or not Auto-merge can be enabled on pull requests in this repository.
- **branchProtectionRules** (`BranchProtectionRuleConnection!`): A list of branch protection rules for this repository.
- **codeOfConduct** (`CodeOfConduct`): Returns the code of conduct for this repository.
- **codeowners** (`RepositoryCodeowners`): Information extracted from the repository's `CODEOWNERS` file.
- **collaborators** (`RepositoryCollaboratorConnection`): A list of collaborators associated with the repository.
- **commitComments** (`CommitCommentConnection!`): A list of commit comments associated with the repository.
- **contactLinks** (`[RepositoryContactLink!]`): Returns a list of contact links associated to the repository.
- **contributingGuidelines** (`ContributingGuidelines`): Returns the contributing guidelines for this repository.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **defaultBranchRef** (`Ref`): The Ref associated with the repository's default branch.
- **deleteBranchOnMerge** (`Boolean!`): Whether or not branches are automatically deleted when merged in this repository.
- **dependencyGraphManifests** (`DependencyGraphManifestConnection`): A list of dependency manifests contained in the repository.
- **deployKeys** (`DeployKeyConnection!`): A list of deploy keys that are on this repository.
- **deployments** (`DeploymentConnection!`): Deployments associated with the repository.
- **description** (`String`): The description of the repository.
- **descriptionHTML** (`HTML!`): The description of the repository rendered to HTML.
- **discussion** (`Discussion`): Returns a single discussion from the current repository by number.
- **discussionCategories** (`DiscussionCategoryConnection!`): A list of discussion categories that are available in the repository.
- **discussionCategory** (`DiscussionCategory`): A discussion category by slug.
- **discussions** (`DiscussionConnection!`): A list of discussions that have been opened in the repository.
- **diskUsage** (`Int`): The number of kilobytes this repository occupies on disk.
- **environment** (`Environment`): Returns a single active environment from the current repository by name.
- **environments** (`EnvironmentConnection!`): A list of environments that are in this repository.
- **forkCount** (`Int!`): Returns how many forks there are of this repository in the whole network.
- **forkingAllowed** (`Boolean!`): Whether this repository allows forks.
- **forks** (`RepositoryConnection!`): A list of direct forked repositories.
- **fundingLinks** (`[FundingLink!]!`): The funding links for this repository.
- **hasDiscussionsEnabled** (`Boolean!`): Indicates if the repository has the Discussions feature enabled.
- **hasIssuesEnabled** (`Boolean!`): Indicates if the repository has issues feature enabled.
- **hasProjectsEnabled** (`Boolean!`): Indicates if the repository has the Projects feature enabled.
- **hasPullRequestsEnabled** (`Boolean!`): Indicates if the repository has the pull requests feature enabled.
- **hasSponsorshipsEnabled** (`Boolean!`): Indicates if the repository displays a Sponsor button for financial contributions.
- **hasVulnerabilityAlertsEnabled** (`Boolean!`): Whether vulnerability alerts are enabled for the repository.
- **hasWikiEnabled** (`Boolean!`): Indicates if the repository has wiki feature enabled.
- **homepageUrl** (`URI`): The repository's URL.
- **id** (`ID!`): The Node ID of the Repository object.
- **interactionAbility** (`RepositoryInteractionAbility`): The interaction ability settings for this repository.
- **isArchived** (`Boolean!`): Indicates if the repository is unmaintained.
- **isBlankIssuesEnabled** (`Boolean!`): Returns true if the viewer can create a blank issue in this repository.
- **isDisabled** (`Boolean!`): Returns whether or not this repository disabled.
- **isEmpty** (`Boolean!`): Returns whether or not this repository is empty.
- **isFork** (`Boolean!`): Identifies if the repository is a fork.
- **isInOrganization** (`Boolean!`): Indicates if a repository is either owned by an organization, or is a private fork of an organization repository.
- **isLocked** (`Boolean!`): Indicates if the repository has been locked or not.
- **isMirror** (`Boolean!`): Identifies if the repository is a mirror.
- **isPrivate** (`Boolean!`): Identifies if the repository is private or internal.
- **isSecurityPolicyEnabled** (`Boolean`): Returns true if this repository has a security policy.
- **isTemplate** (`Boolean!`): Identifies if the repository is a template that can be used to generate new repositories.
- **isUserConfigurationRepository** (`Boolean!`): Is this repository a user configuration repository?.
- **issue** (`Issue`): Returns a single issue from the current repository by number.
- **issueOrPullRequest** (`IssueOrPullRequest`): Returns a single issue-like object from the current repository by number.
- **issueTemplates** (`[IssueTemplate!]`): Returns a list of issue templates associated to the repository.
- **issueType** (`IssueType`): Returns a single issue type by name.
- **issueTypes** (`IssueTypeConnection`): A list of the repository's issue types.
- **issues** (`IssueConnection!`): A list of issues that have been opened in the repository.
- **label** (`Label`): Returns a single label by name.
- **labels** (`LabelConnection`): A list of labels associated with the repository.
- **languages** (`LanguageConnection`): A list containing a breakdown of the language composition of the repository.
- **latestRelease** (`Release`): Get the latest release for the repository if one exists.
- **licenseInfo** (`License`): The license associated with the repository.
- **lockReason** (`RepositoryLockReason`): The reason the repository has been locked.
- **mentionableUsers** (`UserConnection!`): A list of Users that can be mentioned in the context of the repository.
- **mergeCommitAllowed** (`Boolean!`): Whether or not PRs are merged with a merge commit on this repository.
- **mergeCommitMessage** (`MergeCommitMessage!`): How the default commit message will be generated when merging a pull request.
- **mergeCommitTitle** (`MergeCommitTitle!`): How the default commit title will be generated when merging a pull request.
- **mergeQueue** (`MergeQueue`): The merge queue for a specified branch, otherwise the default branch if not provided.
- **milestone** (`Milestone`): Returns a single milestone from the current repository by number.
- **milestones** (`MilestoneConnection`): A list of milestones associated with the repository.
- **mirrorUrl** (`URI`): The repository's original mirror URL.
- **name** (`String!`): The name of the repository.
- **nameWithOwner** (`String!`): The repository's name with owner.
- **object** (`GitObject`): A Git object in the repository.
- **openGraphImageUrl** (`URI!`): The image used to represent this repository in Open Graph data.
- **owner** (`RepositoryOwner!`): The User owner of the repository.
- **packages** (`PackageConnection!`): A list of packages under the owner.
- **parent** (`Repository`): The repository parent, if this is a fork.
- **pinnedDiscussions** (`PinnedDiscussionConnection!`): A list of discussions that have been pinned in this repository.
- **pinnedEnvironments** (`PinnedEnvironmentConnection`): A list of pinned environments for this repository.
- **pinnedIssues** (`PinnedIssueConnection`): A list of pinned issues for this repository.
- **planFeatures** (`RepositoryPlanFeatures!`): Returns information about the availability of certain features and limits based on the repository's billing plan.
- **primaryLanguage** (`Language`): The primary language of the repository's code.
- **project** (`Project`): Find project by number.
- **projectV2** (`ProjectV2`): Finds and returns the Project according to the provided Project number.
- **projects** (`ProjectConnection!`): A list of projects under the owner.
- **projectsResourcePath** (`URI!`): The HTTP path listing the repository's projects.
- **projectsUrl** (`URI!`): The HTTP URL listing the repository's projects.
- **projectsV2** (`ProjectV2Connection!`): List of projects linked to this repository.
- **pullRequest** (`PullRequest`): Returns a single pull request from the current repository by number.
- **pullRequestCreationPolicy** (`PullRequestCreationPolicy`): The policy controlling who can create pull requests in this repository.
- **pullRequestTemplates** (`[PullRequestTemplate!]`): Returns a list of pull request templates associated to the repository.
- **pullRequests** (`PullRequestConnection!`): A list of pull requests that have been opened in the repository.
- **pushedAt** (`DateTime`): Identifies the date and time when the repository was last pushed to.
- **rebaseMergeAllowed** (`Boolean!`): Whether or not rebase-merging is enabled on this repository.
- **recentProjects** (`ProjectV2Connection!`): Recent projects that this user has modified in the context of the owner.
- **ref** (`Ref`): Fetch a given ref from the repository.
- **refs** (`RefConnection`): Fetch a list of refs from the repository.
- **release** (`Release`): Lookup a single release given various criteria.
- **releases** (`ReleaseConnection!`): List of releases which are dependent on this repository.
- **repositoryCustomPropertyValue** (`RepositoryCustomPropertyValue`): A custom property value for the repository.
- **repositoryCustomPropertyValues** (`RepositoryCustomPropertyValueConnection`): A list of custom properties and their associated values for a repository.
- **repositoryTopics** (`RepositoryTopicConnection!`): A list of applied repository-topic associations for this repository.
- **resourcePath** (`URI!`): The HTTP path for this repository.
- **ruleset** (`RepositoryRuleset`): Returns a single ruleset from the current repository by ID.
- **rulesets** (`RepositoryRulesetConnection`): A list of rulesets for this repository.
- **securityPolicyUrl** (`URI`): The security policy URL.
- **shortDescriptionHTML** (`HTML!`): A description of the repository, rendered to HTML without any links in it.
- **squashMergeAllowed** (`Boolean!`): Whether or not squash-merging is enabled on this repository.
- **squashMergeCommitMessage** (`SquashMergeCommitMessage!`): How the default commit message will be generated when squash merging a pull request.
- **squashMergeCommitTitle** (`SquashMergeCommitTitle!`): How the default commit title will be generated when squash merging a pull request.
- **squashPrTitleUsedAsDefault** (`Boolean!`): Whether a squash merge commit can use the pull request title as default.
- **sshUrl** (`GitSSHRemote!`): The SSH URL to clone this repository.
- **stargazerCount** (`Int!`): Returns a count of how many stargazers there are on this object.
- **stargazers** (`StargazerConnection!`): A list of users who have starred this starrable.
- **submodules** (`SubmoduleConnection!`): Returns a list of all submodules in this repository parsed from the
.gitmodules file as of the default branch's HEAD commit.
- **suggestedActors** (`ActorConnection!`): A list of suggested actors that can be attributed to content in this repository.
- **tempCloneToken** (`String`): Temporary authentication token for cloning this repository.
- **templateRepository** (`Repository`): The repository from which this repository was generated, if any.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this repository.
- **usesCustomOpenGraphImage** (`Boolean!`): Whether this repository has a custom image to use with Open Graph as opposed to being represented by the owner's avatar.
- **viewerCanAdminister** (`Boolean!`): Indicates whether the viewer has admin permissions on this repository.
- **viewerCanCreateProjects** (`Boolean!`): Can the current viewer create new projects on this owner.
- **viewerCanSeeIssueFields** (`Boolean!`): Indicates whether the current user can see issue fields in this repository.
- **viewerCanSubscribe** (`Boolean!`): Check if the viewer is able to change their subscription status for the repository.
- **viewerCanUpdateTopics** (`Boolean!`): Indicates whether the viewer can update the topics of this repository.
- **viewerDefaultCommitEmail** (`String`): The last commit email for the viewer.
- **viewerDefaultMergeMethod** (`PullRequestMergeMethod!`): The last used merge method by the viewer or the default for the repository.
- **viewerHasStarred** (`Boolean!`): Returns a boolean indicating whether the viewing user has starred this starrable.
- **viewerPermission** (`RepositoryPermission`): The users permission level on the repository. Will return null if authenticated as an GitHub App.
- **viewerPossibleCommitEmails** (`[String!]`): A list of emails this viewer can commit with.
- **viewerSubscription** (`SubscriptionState`): Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.
- **visibility** (`RepositoryVisibility!`): Indicates the repository's visibility level.
- **vulnerabilityAlert** (`RepositoryVulnerabilityAlert`): Returns a single vulnerability alert from the current repository by number.
- **vulnerabilityAlerts** (`RepositoryVulnerabilityAlertConnection`): A list of vulnerability alerts that are on this repository.
- **watchers** (`UserConnection!`): A list of users watching the repository.
- **webCommitSignoffRequired** (`Boolean!`): Whether contributors are required to sign off on web-based commits in this repository.

### RepositoryCodeowners

Information extracted from a repository's `CODEOWNERS` file.

**Fields:**

- **errors** (`[RepositoryCodeownersError!]!`): Any problems that were encountered while parsing the `CODEOWNERS` file.

### RepositoryCodeownersError

An error in a `CODEOWNERS` file.

**Fields:**

- **column** (`Int!`): The column number where the error occurs.
- **kind** (`String!`): A short string describing the type of error.
- **line** (`Int!`): The line number where the error occurs.
- **message** (`String!`): A complete description of the error, combining information from other fields.
- **path** (`String!`): The path to the file when the error occurs.
- **source** (`String!`): The content of the line where the error occurs.
- **suggestion** (`String`): A suggestion of how to fix the error.

### RepositoryContactLink

A repository contact link.

**Fields:**

- **about** (`String!`): The contact link purpose.
- **name** (`String!`): The contact link name.
- **url** (`URI!`): The contact link URL.

### RepositoryCustomProperty

A repository custom property.

**Implements:** Node

**Fields:**

- **allowedValues** (`[String!]`): The allowed values for the custom property. Required if `value_type` is `single_select` or `multi_select`.
- **defaultValue** (`CustomPropertyValue`): The default value of the custom property, if the property is `required`.
- **description** (`String`): The description of the custom property.
- **id** (`ID!`): The Node ID of the RepositoryCustomProperty object.
- **propertyName** (`String!`): The name of the custom property.
- **regex** (`String`): The regex pattern that the value of the custom property must match, if the `value_type` is `string`.
- **requireExplicitValues** (`Boolean`): Whether this repository custom property requires explicit values.
- **required** (`Boolean`): Whether the custom property is required.
- **source** (`CustomPropertySource!`): The source type of the custom property.
- **valueType** (`CustomPropertyValueType!`): The value type of the custom property.
- **valuesEditableBy** (`RepositoryCustomPropertyValuesEditableBy!`): Who can edit the values of this repository custom property.

### RepositoryCustomPropertyValue

A value associated with a repository custom property.

**Fields:**

- **propertyName** (`String!`): The name of the custom property.
- **value** (`CustomPropertyValue!`): The value of the custom property.

### RepositoryIdConditionTarget

Parameters to be used for the repository_id condition.

**Fields:**

- **repositoryIds** (`[ID!]!`): One of these repo IDs must match the repo.

### RepositoryInteractionAbility

Repository interaction limit that applies to this object.

**Fields:**

- **expiresAt** (`DateTime`): The time the currently active limit expires.
- **limit** (`RepositoryInteractionLimit!`): The current limit that is enabled on this object.
- **origin** (`RepositoryInteractionLimitOrigin!`): The origin of the currently active interaction limit.

### RepositoryInvitation

An invitation for a user to be added to a repository.

**Implements:** Node

**Fields:**

- **email** (`String`): The email address that received the invitation.
- **id** (`ID!`): The Node ID of the RepositoryInvitation object.
- **invitee** (`User`): The user who received the invitation.
- **inviter** (`User!`): The user who created the invitation.
- **permalink** (`URI!`): The permalink for this repository invitation.
- **permission** (`RepositoryPermission!`): The permission granted on this repository by this invitation.
- **repository** (`RepositoryInfo`): The Repository the user is invited to.

### RepositoryMigration

A GitHub Enterprise Importer (GEI) repository migration.

**Implements:** Migration, Node

**Fields:**

- **continueOnError** (`Boolean!`): The migration flag to continue on error.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`String`): Identifies the primary key from the database.
- **failureReason** (`String`): The reason the migration failed.
- **id** (`ID!`): The Node ID of the RepositoryMigration object.
- **migrationLogUrl** (`URI`): The URL for the migration log (expires 1 day after migration completes).
- **migrationSource** (`MigrationSource!`): The migration source.
- **repositoryName** (`String!`): The target repository name.
- **sourceUrl** (`URI!`): The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.
- **state** (`MigrationState!`): The migration state.
- **warningsCount** (`Int!`): The number of warnings encountered for this migration. To review the warnings,
check the [Migration Log](https://docs.github.com/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/accessing-your-migration-logs-for-github-enterprise-importer).

### RepositoryNameConditionTarget

Parameters to be used for the repository_name condition.

**Fields:**

- **exclude** (`[String!]!`): Array of repository names or patterns to exclude. The condition will not pass if any of these patterns match.
- **include** (`[String!]!`): Array of repository names or patterns to include. One of these patterns must
match for the condition to pass. Also accepts `~ALL` to include all repositories.
- **protected** (`Boolean!`): Target changes that match these patterns will be prevented except by those with bypass permissions.

### RepositoryPlanFeatures

Information about the availability of features and limits for a repository based on its billing plan.

**Fields:**

- **codeowners** (`Boolean!`): Whether reviews can be automatically requested and enforced with a CODEOWNERS file.
- **draftPullRequests** (`Boolean!`): Whether pull requests can be created as or converted to draft.
- **maximumAssignees** (`Int!`): Maximum number of users that can be assigned to an issue or pull request.
- **maximumManualReviewRequests** (`Int!`): Maximum number of manually-requested reviews on a pull request.
- **teamReviewRequests** (`Boolean!`): Whether teams can be requested to review pull requests.

### RepositoryPropertyConditionTarget

Parameters to be used for the repository_property condition.

**Fields:**

- **exclude** (`[PropertyTargetDefinition!]!`): Array of repository properties that must not match.
- **include** (`[PropertyTargetDefinition!]!`): Array of repository properties that must match.

### RepositoryRule

A repository rule.

**Implements:** Node

**Fields:**

- **id** (`ID!`): The Node ID of the RepositoryRule object.
- **parameters** (`RuleParameters`): The parameters for this rule.
- **repositoryRuleset** (`RepositoryRuleset`): The repository ruleset associated with this rule configuration.
- **type** (`RepositoryRuleType!`): The type of rule.

### RepositoryRuleConditions

Set of conditions that determine if a ruleset will evaluate.

**Fields:**

- **organizationProperty** (`OrganizationPropertyConditionTarget`): Configuration for the organization_property condition.
- **refName** (`RefNameConditionTarget`): Configuration for the ref_name condition.
- **repositoryId** (`RepositoryIdConditionTarget`): Configuration for the repository_id condition.
- **repositoryName** (`RepositoryNameConditionTarget`): Configuration for the repository_name condition.
- **repositoryProperty** (`RepositoryPropertyConditionTarget`): Configuration for the repository_property condition.

### RepositoryRuleset

A repository ruleset.

**Implements:** Node

**Fields:**

- **bypassActors** (`RepositoryRulesetBypassActorConnection`): The actors that can bypass this ruleset.
- **conditions** (`RepositoryRuleConditions!`): The set of conditions that must evaluate to true for this ruleset to apply.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **enforcement** (`RuleEnforcement!`): The enforcement level of this ruleset.
- **id** (`ID!`): The Node ID of the RepositoryRuleset object.
- **name** (`String!`): Name of the ruleset.
- **rules** (`RepositoryRuleConnection`): List of rules.
- **source** (`RuleSource!`): Source of ruleset.
- **target** (`RepositoryRulesetTarget`): Target of the ruleset.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### RepositoryRulesetBypassActor

A team or app that has the ability to bypass a rules defined on a ruleset.

**Implements:** Node

**Fields:**

- **actor** (`BypassActor`): The actor that can bypass rules.
- **bypassMode** (`RepositoryRulesetBypassActorBypassMode`): The mode for the bypass actor.
- **deployKey** (`Boolean!`): This actor represents the ability for a deploy key to bypass.
- **enterpriseOwner** (`Boolean!`): This actor represents the ability for an enterprise owner to bypass.
- **id** (`ID!`): The Node ID of the RepositoryRulesetBypassActor object.
- **organizationAdmin** (`Boolean!`): This actor represents the ability for an organization owner to bypass.
- **repositoryRoleDatabaseId** (`Int`): If the actor is a repository role, the repository role's ID that can bypass.
- **repositoryRoleName** (`String`): If the actor is a repository role, the repository role's name that can bypass.
- **repositoryRuleset** (`RepositoryRuleset`): Identifies the ruleset associated with the allowed actor.

### RepositoryTopic

A repository-topic connects a repository to a topic.

**Implements:** Node, UniformResourceLocatable

**Fields:**

- **id** (`ID!`): The Node ID of the RepositoryTopic object.
- **resourcePath** (`URI!`): The HTTP path for this repository-topic.
- **topic** (`Topic!`): The topic.
- **url** (`URI!`): The HTTP URL for this repository-topic.

### RepositoryVulnerabilityAlert

A Dependabot alert for a repository with a dependency affected by a security vulnerability.

**Implements:** Node, RepositoryNode

**Fields:**

- **autoDismissedAt** (`DateTime`): When was the alert auto-dismissed?.
- **createdAt** (`DateTime!`): When was the alert created?.
- **dependabotUpdate** (`DependabotUpdate`): The associated Dependabot update.
- **dependencyRelationship** (`RepositoryVulnerabilityAlertDependencyRelationship`): The relationship of an alert's dependency.
- **dependencyScope** (`RepositoryVulnerabilityAlertDependencyScope`): The scope of an alert's dependency.
- **dismissComment** (`String`): Comment explaining the reason the alert was dismissed.
- **dismissReason** (`String`): The reason the alert was dismissed.
- **dismissedAt** (`DateTime`): When was the alert dismissed?.
- **dismisser** (`User`): The user who dismissed the alert.
- **fixedAt** (`DateTime`): When was the alert fixed?.
- **id** (`ID!`): The Node ID of the RepositoryVulnerabilityAlert object.
- **number** (`Int!`): Identifies the alert number.
- **repository** (`Repository!`): The associated repository.
- **securityAdvisory** (`SecurityAdvisory`): The associated security advisory.
- **securityVulnerability** (`SecurityVulnerability`): The associated security vulnerability.
- **state** (`RepositoryVulnerabilityAlertState!`): Identifies the state of the alert.
- **vulnerableManifestFilename** (`String!`): The vulnerable manifest filename.
- **vulnerableManifestPath** (`String!`): The vulnerable manifest path.
- **vulnerableRequirements** (`String`): The vulnerable requirements.

### Submodule

A pointer to a repository at a specific revision embedded inside another repository.

**Fields:**

- **branch** (`String`): The branch of the upstream submodule for tracking updates.
- **gitUrl** (`URI!`): The git URL of the submodule repository.
- **name** (`String!`): The name of the submodule in .gitmodules.
- **nameRaw** (`Base64String!`): The name of the submodule in .gitmodules (Base64-encoded).
- **path** (`String!`): The path in the superproject that this submodule is located in.
- **pathRaw** (`Base64String!`): The path in the superproject that this submodule is located in (Base64-encoded).
- **subprojectCommitOid** (`GitObjectID`): The commit revision of the subproject repository being tracked by the submodule.

### Topic

A topic aggregates entities that are related to a subject.

**Implements:** Node, Starrable

**Fields:**

- **id** (`ID!`): The Node ID of the Topic object.
- **name** (`String!`): The topic's name.
- **relatedTopics** (`[Topic!]!`): A list of related topics, including aliases of this topic, sorted with the most relevant
first. Returns up to 10 Topics.
- **repositories** (`RepositoryConnection!`): A list of repositories.
- **stargazerCount** (`Int!`): Returns a count of how many stargazers there are on this object.
- **stargazers** (`StargazerConnection!`): A list of users who have starred this starrable.
- **viewerHasStarred** (`Boolean!`): Returns a boolean indicating whether the viewing user has starred this starrable.

### UserNamespaceRepository

A repository owned by an Enterprise Managed user.

**Implements:** Node

**Fields:**

- **id** (`ID!`): The Node ID of the UserNamespaceRepository object.
- **name** (`String!`): The name of the repository.
- **nameWithOwner** (`String!`): The repository's name with owner.
- **owner** (`RepositoryOwner!`): The user owner of the repository.

### VerifiableDomain

A domain that can be verified or approved for an organization or an enterprise.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **dnsHostName** (`URI`): The DNS host name that should be used for verification.
- **domain** (`URI!`): The unicode encoded domain.
- **hasFoundHostName** (`Boolean!`): Whether a TXT record for verification with the expected host name was found.
- **hasFoundVerificationToken** (`Boolean!`): Whether a TXT record for verification with the expected verification token was found.
- **id** (`ID!`): The Node ID of the VerifiableDomain object.
- **isApproved** (`Boolean!`): Whether or not the domain is approved.
- **isRequiredForPolicyEnforcement** (`Boolean!`): Whether this domain is required to exist for an organization or enterprise policy to be enforced.
- **isVerified** (`Boolean!`): Whether or not the domain is verified.
- **owner** (`VerifiableDomainOwner!`): The owner of the domain.
- **punycodeEncodedDomain** (`URI!`): The punycode encoded domain.
- **tokenExpirationTime** (`DateTime`): The time that the current verification token will expire.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **verificationToken** (`String`): The current verification token for the domain.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **BranchProtectionRuleConflictConnection** (4 fields): The connection type for BranchProtectionRuleConflict.
- **BranchProtectionRuleConflictEdge** (2 fields): An edge in a connection.
- **BranchProtectionRuleConnection** (4 fields): The connection type for BranchProtectionRule.
- **BranchProtectionRuleEdge** (2 fields): An edge in a connection.
- **CreatedRepositoryContributionConnection** (4 fields): The connection type for CreatedRepositoryContribution.
- **CreatedRepositoryContributionEdge** (2 fields): An edge in a connection.
- **DeployKeyConnection** (4 fields): The connection type for DeployKey.
- **DeployKeyEdge** (2 fields): An edge in a connection.
- **EnterpriseRepositoryInfoConnection** (4 fields): The connection type for EnterpriseRepositoryInfo.
- **EnterpriseRepositoryInfoEdge** (2 fields): An edge in a connection.
- **LinkedBranchConnection** (4 fields): A list of branches linked to an issue.
- **LinkedBranchEdge** (2 fields): An edge in a connection.
- **RepositoryCollaboratorConnection** (4 fields): The connection type for User.
- **RepositoryCollaboratorEdge** (4 fields): Represents a user who is a collaborator of a repository.
- **RepositoryConnection** (5 fields): A list of repositories owned by the subject.
- **RepositoryCustomPropertyConnection** (4 fields): The connection type for RepositoryCustomProperty.
- **RepositoryCustomPropertyEdge** (2 fields): An edge in a connection.
- **RepositoryCustomPropertyValueConnection** (4 fields): The connection type for RepositoryCustomPropertyValue.
- **RepositoryCustomPropertyValueEdge** (2 fields): An edge in a connection.
- **RepositoryEdge** (2 fields): An edge in a connection.
- **RepositoryInvitationConnection** (4 fields): A list of repository invitations.
- **RepositoryInvitationEdge** (2 fields): An edge in a connection.
- **RepositoryMigrationConnection** (4 fields): A list of migrations.
- **RepositoryMigrationEdge** (2 fields): Represents a repository migration.
- **RepositoryRuleConnection** (4 fields): The connection type for RepositoryRule.
- **RepositoryRuleEdge** (2 fields): An edge in a connection.
- **RepositoryRulesetBypassActorConnection** (4 fields): The connection type for RepositoryRulesetBypassActor.
- **RepositoryRulesetBypassActorEdge** (2 fields): An edge in a connection.
- **RepositoryRulesetConnection** (4 fields): The connection type for RepositoryRuleset.
- **RepositoryRulesetEdge** (2 fields): An edge in a connection.
- **RepositoryTopicConnection** (4 fields): The connection type for RepositoryTopic.
- **RepositoryTopicEdge** (2 fields): An edge in a connection.
- **RepositoryVulnerabilityAlertConnection** (4 fields): The connection type for RepositoryVulnerabilityAlert.
- **RepositoryVulnerabilityAlertEdge** (2 fields): An edge in a connection.
- **StargazerConnection** (4 fields): The connection type for User.
- **StargazerEdge** (3 fields): Represents a user that's starred a repository.
- **StarredRepositoryConnection** (5 fields): The connection type for Repository.
- **StarredRepositoryEdge** (3 fields): Represents a starred repository.
- **SubmoduleConnection** (4 fields): The connection type for Submodule.
- **SubmoduleEdge** (2 fields): An edge in a connection.
- **TeamRepositoryConnection** (4 fields): The connection type for Repository.
- **TeamRepositoryEdge** (3 fields): Represents a team repository.
- **UserNamespaceRepositoryConnection** (4 fields): A list of repositories owned by users in an enterprise with Enterprise Managed Users.
- **UserNamespaceRepositoryEdge** (2 fields): An edge in a connection.
- **VerifiableDomainConnection** (4 fields): The connection type for VerifiableDomain.
- **VerifiableDomainEdge** (2 fields): An edge in a connection.

## Interfaces

### RepositoryDiscussionAuthor

Represents an author of discussions in repositories.

**Fields:**

- **repositoryDiscussions** (`DiscussionConnection!`): Discussions this user has started.

### RepositoryDiscussionCommentAuthor

Represents an author of discussion comments in repositories.

**Fields:**

- **repositoryDiscussionComments** (`DiscussionCommentConnection!`): Discussion comments this user has authored.

### RepositoryInfo

A subset of repository info.

**Fields:**

- **archivedAt** (`DateTime`): Identifies the date and time when the repository was archived.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **description** (`String`): The description of the repository.
- **descriptionHTML** (`HTML!`): The description of the repository rendered to HTML.
- **forkCount** (`Int!`): Returns how many forks there are of this repository in the whole network.
- **hasDiscussionsEnabled** (`Boolean!`): Indicates if the repository has the Discussions feature enabled.
- **hasIssuesEnabled** (`Boolean!`): Indicates if the repository has issues feature enabled.
- **hasProjectsEnabled** (`Boolean!`): Indicates if the repository has the Projects feature enabled.
- **hasPullRequestsEnabled** (`Boolean!`): Indicates if the repository has the pull requests feature enabled.
- **hasSponsorshipsEnabled** (`Boolean!`): Indicates if the repository displays a Sponsor button for financial contributions.
- **hasWikiEnabled** (`Boolean!`): Indicates if the repository has wiki feature enabled.
- **homepageUrl** (`URI`): The repository's URL.
- **isArchived** (`Boolean!`): Indicates if the repository is unmaintained.
- **isFork** (`Boolean!`): Identifies if the repository is a fork.
- **isInOrganization** (`Boolean!`): Indicates if a repository is either owned by an organization, or is a private fork of an organization repository.
- **isLocked** (`Boolean!`): Indicates if the repository has been locked or not.
- **isMirror** (`Boolean!`): Identifies if the repository is a mirror.
- **isPrivate** (`Boolean!`): Identifies if the repository is private or internal.
- **isTemplate** (`Boolean!`): Identifies if the repository is a template that can be used to generate new repositories.
- **licenseInfo** (`License`): The license associated with the repository.
- **lockReason** (`RepositoryLockReason`): The reason the repository has been locked.
- **mirrorUrl** (`URI`): The repository's original mirror URL.
- **name** (`String!`): The name of the repository.
- **nameWithOwner** (`String!`): The repository's name with owner.
- **openGraphImageUrl** (`URI!`): The image used to represent this repository in Open Graph data.
- **owner** (`RepositoryOwner!`): The User owner of the repository.
- **pullRequestCreationPolicy** (`PullRequestCreationPolicy`): The policy controlling who can create pull requests in this repository.
- **pushedAt** (`DateTime`): Identifies the date and time when the repository was last pushed to.
- **resourcePath** (`URI!`): The HTTP path for this repository.
- **shortDescriptionHTML** (`HTML!`): A description of the repository, rendered to HTML without any links in it.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this repository.
- **usesCustomOpenGraphImage** (`Boolean!`): Whether this repository has a custom image to use with Open Graph as opposed to being represented by the owner's avatar.
- **visibility** (`RepositoryVisibility!`): Indicates the repository's visibility level.

### RepositoryNode

Represents a object that belongs to a repository.

**Fields:**

- **repository** (`Repository!`): The repository associated with this node.

### RepositoryOwner

Represents an owner of a Repository.

**Fields:**

- **avatarUrl** (`URI!`): A URL pointing to the owner's public avatar.
- **id** (`ID!`): The Node ID of the RepositoryOwner object.
- **login** (`String!`): The username used to login.
- **repositories** (`RepositoryConnection!`): A list of repositories that the user owns.
- **repository** (`Repository`): Find Repository.
- **resourcePath** (`URI!`): The HTTP URL for the owner.
- **url** (`URI!`): The HTTP URL for the owner.

## Enums

### DefaultRepositoryPermissionField

The possible base permissions for repositories.

**Values:**

- `ADMIN`: Can read, write, and administrate repos by default.
- `NONE`: No access.
- `READ`: Can read repos by default.
- `WRITE`: Can read and write repos by default.

### EnterpriseAllowPrivateRepositoryForkingPolicyValue

The possible values for the enterprise allow private repository forking policy value.

**Values:**

- `ENTERPRISE_ORGANIZATIONS`: Members can fork a repository to an organization within this enterprise.
- `ENTERPRISE_ORGANIZATIONS_USER_ACCOUNTS`: Members can fork a repository to their enterprise-managed user account or an organization inside this enterprise.
- `EVERYWHERE`: Members can fork a repository to their user account or an organization, either inside or outside of this enterprise.
- `SAME_ORGANIZATION`: Members can fork a repository only within the same organization (intra-org).
- `SAME_ORGANIZATION_USER_ACCOUNTS`: Members can fork a repository to their user account or within the same organization.
- `USER_ACCOUNTS`: Members can fork a repository to their user account.

### EnterpriseDefaultRepositoryPermissionSettingValue

The possible values for the enterprise base repository permission setting.

**Values:**

- `ADMIN`: Organization members will be able to clone, pull, push, and add new collaborators to all organization repositories.
- `NONE`: Organization members will only be able to clone and pull public repositories.
- `NO_POLICY`: Organizations in the enterprise choose base repository permissions for their members.
- `READ`: Organization members will be able to clone and pull all organization repositories.
- `WRITE`: Organization members will be able to clone, pull, and push all organization repositories.

### EnterpriseMembersCanCreateRepositoriesSettingValue

The possible values for the enterprise members can create repositories setting.

**Values:**

- `ALL`: Members will be able to create public and private repositories.
- `DISABLED`: Members will not be able to create public or private repositories.
- `NO_POLICY`: Organization owners choose whether to allow members to create repositories.
- `PRIVATE`: Members will be able to create only private repositories.
- `PUBLIC`: Members will be able to create only public repositories.

### OrganizationMembersCanCreateRepositoriesSettingValue

The possible values for the members can create repositories setting on an organization.

**Values:**

- `ALL`: Members will be able to create public and private repositories.
- `DISABLED`: Members will not be able to create public or private repositories.
- `INTERNAL`: Members will be able to create only internal repositories.
- `PRIVATE`: Members will be able to create only private repositories.

### ReportedContentClassifiers

The reasons a piece of content can be reported or minimized.

**Values:**

- `ABUSE`: An abusive or harassing piece of content.
- `DUPLICATE`: A duplicated piece of content.
- `OFF_TOPIC`: An irrelevant piece of content.
- `OUTDATED`: An outdated piece of content.
- `RESOLVED`: The content has been resolved.
- `SPAM`: A spammy piece of content.

### RepositoryAffiliation

The affiliation of a user to a repository.

**Values:**

- `COLLABORATOR`: Repositories that the user has been added to as a collaborator.
- `ORGANIZATION_MEMBER`: Repositories that the user has access to through being a member of an
organization. This includes every repository on every team that the user is on.
- `OWNER`: Repositories that are owned by the authenticated user.

### RepositoryContributionType

The reason a repository is listed as 'contributed'.

**Values:**

- `COMMIT`: Created a commit.
- `ISSUE`: Created an issue.
- `PULL_REQUEST`: Created a pull request.
- `PULL_REQUEST_REVIEW`: Reviewed a pull request.
- `REPOSITORY`: Created the repository.

### RepositoryCustomPropertyValuesEditableBy

The allowed actors who can edit the values of a custom property.

**Values:**

- `ORG_ACTORS`: The organization actors.
- `ORG_AND_REPO_ACTORS`: The organization and repository actors.

### RepositoryInteractionLimit

A repository interaction limit.

**Values:**

- `COLLABORATORS_ONLY`: Users that are not collaborators will not be able to interact with the repository.
- `CONTRIBUTORS_ONLY`: Users that have not previously committed to a repository’s default branch will be unable to interact with the repository.
- `EXISTING_USERS`: Users that have recently created their account will be unable to interact with the repository.
- `NO_LIMIT`: No interaction limits are enabled.

### RepositoryInteractionLimitExpiry

The length for a repository interaction limit to be enabled for.

**Values:**

- `ONE_DAY`: The interaction limit will expire after 1 day.
- `ONE_MONTH`: The interaction limit will expire after 1 month.
- `ONE_WEEK`: The interaction limit will expire after 1 week.
- `SIX_MONTHS`: The interaction limit will expire after 6 months.
- `THREE_DAYS`: The interaction limit will expire after 3 days.

### RepositoryInteractionLimitOrigin

Indicates where an interaction limit is configured.

**Values:**

- `ORGANIZATION`: A limit that is configured at the organization level.
- `REPOSITORY`: A limit that is configured at the repository level.
- `USER`: A limit that is configured at the user-wide level.

### RepositoryInvitationOrderField

Properties by which repository invitation connections can be ordered.

**Values:**

- `CREATED_AT`: Order repository invitations by creation time.

### RepositoryLockReason

The possible reasons a given repository could be in a locked state.

**Values:**

- `BILLING`: The repository is locked due to a billing related reason.
- `MIGRATING`: The repository is locked due to a migration.
- `MOVING`: The repository is locked due to a move.
- `RENAME`: The repository is locked due to a rename.
- `TRADE_RESTRICTION`: The repository is locked due to a trade controls related reason.
- `TRANSFERRING_OWNERSHIP`: The repository is locked due to an ownership transfer.

### RepositoryMigrationOrderDirection

Possible directions in which to order a list of repository migrations when provided an `orderBy` argument.

**Values:**

- `ASC`: Specifies an ascending order for a given `orderBy` argument.
- `DESC`: Specifies a descending order for a given `orderBy` argument.

### RepositoryMigrationOrderField

Properties by which repository migrations can be ordered.

**Values:**

- `CREATED_AT`: Order mannequins why when they were created.

### RepositoryOrderField

Properties by which repository connections can be ordered.

**Values:**

- `CREATED_AT`: Order repositories by creation time.
- `NAME`: Order repositories by name.
- `PUSHED_AT`: Order repositories by push time.
- `STARGAZERS`: Order repositories by number of stargazers.
- `UPDATED_AT`: Order repositories by update time.

### RepositoryPermission

The access level to a repository.

**Values:**

- `ADMIN`: Can read, clone, and push to this repository. Can also manage issues, pull
requests, and repository settings, including adding collaborators.
- `MAINTAIN`: Can read, clone, and push to this repository. They can also manage issues, pull requests, and some repository settings.
- `READ`: Can read and clone this repository. Can also open and comment on issues and pull requests.
- `TRIAGE`: Can read and clone this repository. Can also manage issues and pull requests.
- `WRITE`: Can read, clone, and push to this repository. Can also manage issues and pull requests.

### RepositoryPrivacy

The privacy of a repository.

**Values:**

- `PRIVATE`: Private.
- `PUBLIC`: Public.

### RepositoryRuleOrderField

Properties by which repository rule connections can be ordered.

**Values:**

- `CREATED_AT`: Order repository rules by created time.
- `TYPE`: Order repository rules by type.
- `UPDATED_AT`: Order repository rules by updated time.

### RepositoryRuleType

The rule types supported in rulesets.

**Values:**

- `AUTHORIZATION`: Authorization.
- `BRANCH_NAME_PATTERN`: Branch name pattern.
- `CODE_SCANNING`: Choose which tools must provide code scanning results before the reference is
updated. When configured, code scanning must be enabled and have results for
both the commit and the reference being updated.
- `COMMITTER_EMAIL_PATTERN`: Committer email pattern.
- `COMMIT_AUTHOR_EMAIL_PATTERN`: Commit author email pattern.
- `COMMIT_MESSAGE_PATTERN`: Commit message pattern.
- `COPILOT_CODE_REVIEW`: Request Copilot code review for new pull requests automatically if the author
has access to Copilot code review and their premium requests quota has not
reached the limit.
- `CREATION`: Only allow users with bypass permission to create matching refs.
- `DELETION`: Only allow users with bypass permissions to delete matching refs.
- `FILE_EXTENSION_RESTRICTION`: Prevent commits that include files with specified file extensions from being pushed to the commit graph.
- `FILE_PATH_RESTRICTION`: Prevent commits that include changes in specified file and folder paths from
being pushed to the commit graph. This includes absolute paths that contain file names.
- `LOCK_BRANCH`: Branch is read-only. Users cannot push to the branch.
- `MAX_FILE_PATH_LENGTH`: Prevent commits that include file paths that exceed the specified character limit from being pushed to the commit graph.
- `MAX_FILE_SIZE`: Prevent commits with individual files that exceed the specified limit from being pushed to the commit graph.
- `MAX_REF_UPDATES`: Max ref updates.
- `MERGE_QUEUE`: Merges must be performed via a merge queue.
- `MERGE_QUEUE_LOCKED_REF`: Merge queue locked ref.
- `NON_FAST_FORWARD`: Prevent users with push access from force pushing to refs.
- `PULL_REQUEST`: Require all commits be made to a non-target branch and submitted via a pull request before they can be merged.
- `REQUIRED_DEPLOYMENTS`: Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule.
- `REQUIRED_LINEAR_HISTORY`: Prevent merge commits from being pushed to matching refs.
- `REQUIRED_REVIEW_THREAD_RESOLUTION`: When enabled, all conversations on code must be resolved before a pull request
can be merged into a branch that matches this rule.
- `REQUIRED_SIGNATURES`: Commits pushed to matching refs must have verified signatures.
- `REQUIRED_STATUS_CHECKS`: Choose which status checks must pass before the ref is updated. When enabled,
commits must first be pushed to another ref where the checks pass.
- `REQUIRED_WORKFLOW_STATUS_CHECKS`: Require all commits be made to a non-target branch and submitted via a pull
request and required workflow checks to pass before they can be merged.
- `SECRET_SCANNING`: Secret scanning.
- `TAG`: Tag.
- `TAG_NAME_PATTERN`: Tag name pattern.
- `UPDATE`: Only allow users with bypass permission to update matching refs.
- `WORKFLOWS`: Require all changes made to a targeted branch to pass the specified workflows before they can be merged.
- `WORKFLOW_UPDATES`: Workflow files cannot be modified.

### RepositoryRulesetBypassActorBypassMode

The bypass mode for a specific actor on a ruleset.

**Values:**

- `ALWAYS`: The actor can always bypass rules.
- `EXEMPT`: The actor is exempt from rules without generating a pass / fail result.
- `PULL_REQUEST`: The actor can only bypass rules via a pull request.

### RepositoryRulesetTarget

The targets supported for rulesets.

**Values:**

- `BRANCH`: Branch.
- `PUSH`: Push.
- `REPOSITORY`: repository.
- `TAG`: Tag.

### RepositorySuggestedActorFilter

The possible filters for suggested actors in a repository.

**Values:**

- `CAN_BE_ASSIGNED`: Actors that can be assigned to issues and pull requests.
- `CAN_BE_AUTHOR`: Actors that can be the author of issues and pull requests.

### RepositoryVisibility

The repository's visibility level.

**Values:**

- `INTERNAL`: The repository is visible only to users in the same enterprise.
- `PRIVATE`: The repository is visible only to those with explicit access.
- `PUBLIC`: The repository is visible to everyone.

### RepositoryVulnerabilityAlertDependencyRelationship

The possible relationships of an alert's dependency.

**Values:**

- `DIRECT`: A direct dependency of your project.
- `INCONCLUSIVE`: The relationship could not be determined.
- `TRANSITIVE`: A transitive dependency of your project.
- `UNKNOWN`: The relationship is unknown.

### RepositoryVulnerabilityAlertDependencyScope

The possible scopes of an alert's dependency.

**Values:**

- `DEVELOPMENT`: A dependency that is only used in development.
- `RUNTIME`: A dependency that is leveraged during application runtime.

### RepositoryVulnerabilityAlertState

The possible states of an alert.

**Values:**

- `AUTO_DISMISSED`: An alert that has been automatically closed by Dependabot.
- `DISMISSED`: An alert that has been manually closed by a user.
- `FIXED`: An alert that has been resolved by a code change.
- `OPEN`: An alert that is still open.

### TeamRepositoryOrderField

Properties by which team repository connections can be ordered.

**Values:**

- `CREATED_AT`: Order repositories by creation time.
- `NAME`: Order repositories by name.
- `PERMISSION`: Order repositories by permission.
- `PUSHED_AT`: Order repositories by push time.
- `STARGAZERS`: Order repositories by number of stargazers.
- `UPDATED_AT`: Order repositories by update time.

### TopicSuggestionDeclineReason

Reason that the suggested topic is declined.

**Values:**

- `NOT_RELEVANT`: The suggested topic is not relevant to the repository.
- `PERSONAL_PREFERENCE`: The viewer does not like the suggested topic.
- `TOO_GENERAL`: The suggested topic is too general for the repository.
- `TOO_SPECIFIC`: The suggested topic is too specific for the repository (e.g. #ruby-on-rails-version-4-2-1).

### VerifiableDomainOrderField

Properties by which verifiable domain connections can be ordered.

**Values:**

- `CREATED_AT`: Order verifiable domains by their creation date.
- `DOMAIN`: Order verifiable domains by the domain name.

## Input Objects

### AbortRepositoryMigrationInput

Autogenerated input type of AbortRepositoryMigration.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **migrationId** (`ID!`): The ID of the migration to be aborted.

### AcceptTopicSuggestionInput

Autogenerated input type of AcceptTopicSuggestion.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **name** (`String`): The name of the suggested topic.
**Upcoming Change on 2024-04-01 UTC**
**Description:** `name` will be removed.
**Reason:** Suggested topics are no longer supported.
- **repositoryId** (`ID`): The Node ID of the repository.
**Upcoming Change on 2024-04-01 UTC**
**Description:** `repositoryId` will be removed.
**Reason:** Suggested topics are no longer supported.

### AccessUserNamespaceRepositoryInput

Autogenerated input type of AccessUserNamespaceRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise owning the user namespace repository.
- **repositoryId** (`ID!`): The ID of the user namespace repository to access.

### AddVerifiableDomainInput

Autogenerated input type of AddVerifiableDomain.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **domain** (`URI!`): The URL of the domain.
- **ownerId** (`ID!`): The ID of the owner to add the domain to.

### ApproveVerifiableDomainInput

Autogenerated input type of ApproveVerifiableDomain.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The ID of the verifiable domain to approve.

### ArchiveRepositoryInput

Autogenerated input type of ArchiveRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryId** (`ID!`): The ID of the repository to mark as archived.

### CloneTemplateRepositoryInput

Autogenerated input type of CloneTemplateRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **description** (`String`): A short description of the new repository.
- **includeAllBranches** (`Boolean`): Whether to copy all branches from the template to the new repository. Defaults
to copying only the default branch of the template.
- **name** (`String!`): The name of the new repository.
- **ownerId** (`ID!`): The ID of the owner for the new repository.
- **repositoryId** (`ID!`): The Node ID of the template repository.
- **visibility** (`RepositoryVisibility!`): Indicates the repository's visibility level.

### CreateBranchProtectionRuleInput

Autogenerated input type of CreateBranchProtectionRule.

**Input fields:**

- **allowsDeletions** (`Boolean`): Can this branch be deleted.
- **allowsForcePushes** (`Boolean`): Are force pushes allowed on this branch.
- **blocksCreations** (`Boolean`): Is branch creation a protected operation.
- **bypassForcePushActorIds** (`[ID!]`): A list of User, Team, or App IDs allowed to bypass force push targeting matching branches.
- **bypassPullRequestActorIds** (`[ID!]`): A list of User, Team, or App IDs allowed to bypass pull requests targeting matching branches.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **dismissesStaleReviews** (`Boolean`): Will new commits pushed to matching branches dismiss pull request review approvals.
- **isAdminEnforced** (`Boolean`): Can admins override branch protection.
- **lockAllowsFetchAndMerge** (`Boolean`): Whether users can pull changes from upstream when the branch is locked. Set to
`true` to allow fork syncing. Set to `false` to prevent fork syncing.
- **lockBranch** (`Boolean`): Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.
- **pattern** (`String!`): The glob-like pattern used to determine matching branches.
- **pushActorIds** (`[ID!]`): A list of User, Team, or App IDs allowed to push to matching branches.
- **repositoryId** (`ID!`): The global relay id of the repository in which a new branch protection rule should be created in.
- **requireLastPushApproval** (`Boolean`): Whether the most recent push must be approved by someone other than the person who pushed it.
- **requiredApprovingReviewCount** (`Int`): Number of approving reviews required to update matching branches.
- **requiredDeploymentEnvironments** (`[String!]`): The list of required deployment environments.
- **requiredStatusCheckContexts** (`[String!]`): List of required status check contexts that must pass for commits to be accepted to matching branches.
- **requiredStatusChecks** (`[RequiredStatusCheckInput!]`): The list of required status checks.
- **requiresApprovingReviews** (`Boolean`): Are approving reviews required to update matching branches.
- **requiresCodeOwnerReviews** (`Boolean`): Are reviews from code owners required to update matching branches.
- **requiresCommitSignatures** (`Boolean`): Are commits required to be signed.
- **requiresConversationResolution** (`Boolean`): Are conversations required to be resolved before merging.
- **requiresDeployments** (`Boolean`): Are successful deployments required before merging.
- **requiresLinearHistory** (`Boolean`): Are merge commits prohibited from being pushed to this branch.
- **requiresStatusChecks** (`Boolean`): Are status checks required to update matching branches.
- **requiresStrictStatusChecks** (`Boolean`): Are branches required to be up to date before merging.
- **restrictsPushes** (`Boolean`): Is pushing to matching branches restricted.
- **restrictsReviewDismissals** (`Boolean`): Is dismissal of pull request reviews restricted.
- **reviewDismissalActorIds** (`[ID!]`): A list of User, Team, or App IDs allowed to dismiss reviews on pull requests targeting matching branches.

### CreateLinkedBranchInput

Autogenerated input type of CreateLinkedBranch.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): ID of the issue to link to.
- **name** (`String`): The name of the new branch. Defaults to issue number and title.
- **oid** (`GitObjectID!`): The commit SHA to base the new branch on.
- **repositoryId** (`ID`): ID of the repository to create the branch in. Defaults to the issue repository.

### CreateRepositoryCustomPropertyInput

Autogenerated input type of CreateRepositoryCustomProperty.

**Input fields:**

- **allowedValues** (`[String!]`): The allowed values for the custom property.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **defaultValue** (`String`): The default value for the custom property if the property is required.
- **description** (`String`): The description of the custom property.
- **propertyName** (`String!`): The name of the custom property.
- **regex** (`String`): The regex pattern that the value of the custom property must match, if the `value_type` is `string`.
- **requireExplicitValues** (`Boolean`): Whether this repository custom property requires explicit values.
- **required** (`Boolean`): Whether the custom property is required.
- **sourceId** (`ID!`): The global relay id of the source in which a new custom property should be created in.
- **valueType** (`CustomPropertyValueType!`): The value type for the custom property.
- **valuesEditableBy** (`RepositoryCustomPropertyValuesEditableBy`): The allowed actors who can edit the values of a custom property.

### CreateRepositoryInput

Autogenerated input type of CreateRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **description** (`String`): A short description of the new repository.
- **hasIssuesEnabled** (`Boolean`): Indicates if the repository should have the issues feature enabled.
- **hasWikiEnabled** (`Boolean`): Indicates if the repository should have the wiki feature enabled.
- **homepageUrl** (`URI`): The URL for a web page about this repository.
- **name** (`String!`): The name of the new repository.
- **ownerId** (`ID`): The ID of the owner for the new repository.
- **teamId** (`ID`): When an organization is specified as the owner, this ID identifies the team
that should be granted access to the new repository.
- **template** (`Boolean`): Whether this repository should be marked as a template such that anyone who
can access it can create new repositories with the same files and directory structure.
- **visibility** (`RepositoryVisibility!`): Indicates the repository's visibility level.

### CreateRepositoryRulesetInput

Autogenerated input type of CreateRepositoryRuleset.

**Input fields:**

- **bypassActors** (`[RepositoryRulesetBypassActorInput!]`): A list of actors that are allowed to bypass rules in this ruleset.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **conditions** (`RepositoryRuleConditionsInput!`): The set of conditions for this ruleset.
- **enforcement** (`RuleEnforcement!`): The enforcement level for this ruleset.
- **name** (`String!`): The name of the ruleset.
- **rules** (`[RepositoryRuleInput!]`): The list of rules for this ruleset.
- **sourceId** (`ID!`): The global relay id of the source in which a new ruleset should be created in.
- **target** (`RepositoryRulesetTarget`): The target of the ruleset.

### DeclineTopicSuggestionInput

Autogenerated input type of DeclineTopicSuggestion.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **name** (`String`): The name of the suggested topic.
**Upcoming Change on 2024-04-01 UTC**
**Description:** `name` will be removed.
**Reason:** Suggested topics are no longer supported.
- **reason** (`TopicSuggestionDeclineReason`): The reason why the suggested topic is declined.
**Upcoming Change on 2024-04-01 UTC**
**Description:** `reason` will be removed.
**Reason:** Suggested topics are no longer supported.
- **repositoryId** (`ID`): The Node ID of the repository.
**Upcoming Change on 2024-04-01 UTC**
**Description:** `repositoryId` will be removed.
**Reason:** Suggested topics are no longer supported.

### DeleteBranchProtectionRuleInput

Autogenerated input type of DeleteBranchProtectionRule.

**Input fields:**

- **branchProtectionRuleId** (`ID!`): The global relay id of the branch protection rule to be deleted.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### DeleteLinkedBranchInput

Autogenerated input type of DeleteLinkedBranch.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **linkedBranchId** (`ID!`): The ID of the linked branch.

### DeleteRepositoryCustomPropertyInput

Autogenerated input type of DeleteRepositoryCustomProperty.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The global relay id of the custom property to be deleted.

### DeleteRepositoryRulesetInput

Autogenerated input type of DeleteRepositoryRuleset.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryRulesetId** (`ID!`): The global relay id of the repository ruleset to be deleted.

### DeleteVerifiableDomainInput

Autogenerated input type of DeleteVerifiableDomain.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The ID of the verifiable domain to delete.

### DismissRepositoryVulnerabilityAlertInput

Autogenerated input type of DismissRepositoryVulnerabilityAlert.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **dismissReason** (`DismissReason!`): The reason the Dependabot alert is being dismissed.
- **repositoryVulnerabilityAlertId** (`ID!`): The Dependabot alert ID to dismiss.

### LinkProjectV2ToRepositoryInput

Autogenerated input type of LinkProjectV2ToRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the project to link to the repository.
- **repositoryId** (`ID!`): The ID of the repository to link to the project.

### LinkRepositoryToProjectInput

Autogenerated input type of LinkRepositoryToProject.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the Project to link to a Repository.
- **repositoryId** (`ID!`): The ID of the Repository to link to a Project.

### PromoteRepositoryCustomPropertyInput

Autogenerated input type of PromoteRepositoryCustomProperty.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryCustomPropertyId** (`ID!`): The ID of the repository custom property to be promoted.

### RegenerateVerifiableDomainTokenInput

Autogenerated input type of RegenerateVerifiableDomainToken.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The ID of the verifiable domain to regenerate the verification token of.

### RepositoryIdConditionTargetInput

Parameters to be used for the repository_id condition.

**Input fields:**

- **repositoryIds** (`[ID!]!`): One of these repo IDs must match the repo.

### RepositoryInvitationOrder

Ordering options for repository invitation connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`RepositoryInvitationOrderField!`): The field to order repository invitations by.

### RepositoryMigrationOrder

Ordering options for repository migrations.

**Input fields:**

- **direction** (`RepositoryMigrationOrderDirection!`): The ordering direction.
- **field** (`RepositoryMigrationOrderField!`): The field to order repository migrations by.

### RepositoryNameConditionTargetInput

Parameters to be used for the repository_name condition.

**Input fields:**

- **exclude** (`[String!]!`): Array of repository names or patterns to exclude. The condition will not pass if any of these patterns match.
- **include** (`[String!]!`): Array of repository names or patterns to include. One of these patterns must
match for the condition to pass. Also accepts `~ALL` to include all repositories.
- **protected** (`Boolean`): Target changes that match these patterns will be prevented except by those with bypass permissions.

### RepositoryOrder

Ordering options for repository connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`RepositoryOrderField!`): The field to order repositories by.

### RepositoryPropertyConditionTargetInput

Parameters to be used for the repository_property condition.

**Input fields:**

- **exclude** (`[PropertyTargetDefinitionInput!]!`): Array of repository properties that must not match.
- **include** (`[PropertyTargetDefinitionInput!]!`): Array of repository properties that must match.

### RepositoryRuleConditionsInput

Specifies the conditions required for a ruleset to evaluate.

**Input fields:**

- **organizationProperty** (`OrganizationPropertyConditionTargetInput`): Configuration for the organization_property condition.
- **refName** (`RefNameConditionTargetInput`): Configuration for the ref_name condition.
- **repositoryId** (`RepositoryIdConditionTargetInput`): Configuration for the repository_id condition.
- **repositoryName** (`RepositoryNameConditionTargetInput`): Configuration for the repository_name condition.
- **repositoryProperty** (`RepositoryPropertyConditionTargetInput`): Configuration for the repository_property condition.

### RepositoryRuleInput

Specifies the attributes for a new or updated rule.

**Input fields:**

- **id** (`ID`): Optional ID of this rule when updating.
- **parameters** (`RuleParametersInput`): The parameters for the rule.
- **type** (`RepositoryRuleType!`): The type of rule to create.

### RepositoryRuleOrder

Ordering options for repository rules.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`RepositoryRuleOrderField!`): The field to order repository rules by.

### RepositoryRulesetBypassActorInput

Specifies the attributes for a new or updated ruleset bypass actor. Only one of
`actor_id`, `repository_role_database_id`, `organization_admin`, or `deploy_key`
should be specified.

**Input fields:**

- **actorId** (`ID`): For Team and Integration bypasses, the Team or Integration ID.
- **bypassMode** (`RepositoryRulesetBypassActorBypassMode!`): The bypass mode for this actor.
- **deployKey** (`Boolean`): For deploy key bypasses, true. Can only use ALWAYS as the bypass mode.
- **enterpriseOwner** (`Boolean`): For enterprise owner bypasses, true.
- **organizationAdmin** (`Boolean`): For organization owner bypasses, true.
- **repositoryRoleDatabaseId** (`Int`): For role bypasses, the role database ID.

### SetRepositoryCustomPropertyValuesInput

Autogenerated input type of SetRepositoryCustomPropertyValues.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **properties** (`[CustomPropertyValueInput!]!`): A list of custom property names and associated values to apply.
- **repositoryId** (`ID!`): The ID of the repository to set properties for.

### SetRepositoryInteractionLimitInput

Autogenerated input type of SetRepositoryInteractionLimit.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **expiry** (`RepositoryInteractionLimitExpiry`): When this limit should expire.
- **limit** (`RepositoryInteractionLimit!`): The limit to set.
- **repositoryId** (`ID!`): The ID of the repository to set a limit for.

### StartRepositoryMigrationInput

Autogenerated input type of StartRepositoryMigration.

**Input fields:**

- **accessToken** (`String`): The migration source access token.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **continueOnError** (`Boolean`): Whether to continue the migration on error. Defaults to `true`.
- **gitArchiveUrl** (`String`): The signed URL to access the user-uploaded git archive.
- **githubPat** (`String`): The GitHub personal access token of the user importing to the target repository.
- **lockSource** (`Boolean`): Whether to lock the source repository.
- **metadataArchiveUrl** (`String`): The signed URL to access the user-uploaded metadata archive.
- **ownerId** (`ID!`): The ID of the organization that will own the imported repository.
- **repositoryName** (`String!`): The name of the imported repository.
- **skipReleases** (`Boolean`): Whether to skip migrating releases for the repository.
- **sourceId** (`ID!`): The ID of the migration source.
- **sourceRepositoryUrl** (`URI!`): The URL of the source repository.
- **targetRepoVisibility** (`String`): The visibility of the imported repository.

### TeamRepositoryOrder

Ordering options for team repository connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`TeamRepositoryOrderField!`): The field to order repositories by.

### UnarchiveRepositoryInput

Autogenerated input type of UnarchiveRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryId** (`ID!`): The ID of the repository to unarchive.

### UnlinkProjectV2FromRepositoryInput

Autogenerated input type of UnlinkProjectV2FromRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the project to unlink from the repository.
- **repositoryId** (`ID!`): The ID of the repository to unlink from the project.

### UnlinkRepositoryFromProjectInput

Autogenerated input type of UnlinkRepositoryFromProject.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the Project linked to the Repository.
- **repositoryId** (`ID!`): The ID of the Repository linked to the Project.

### UpdateBranchProtectionRuleInput

Autogenerated input type of UpdateBranchProtectionRule.

**Input fields:**

- **allowsDeletions** (`Boolean`): Can this branch be deleted.
- **allowsForcePushes** (`Boolean`): Are force pushes allowed on this branch.
- **blocksCreations** (`Boolean`): Is branch creation a protected operation.
- **branchProtectionRuleId** (`ID!`): The global relay id of the branch protection rule to be updated.
- **bypassForcePushActorIds** (`[ID!]`): A list of User, Team, or App IDs allowed to bypass force push targeting matching branches.
- **bypassPullRequestActorIds** (`[ID!]`): A list of User, Team, or App IDs allowed to bypass pull requests targeting matching branches.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **dismissesStaleReviews** (`Boolean`): Will new commits pushed to matching branches dismiss pull request review approvals.
- **isAdminEnforced** (`Boolean`): Can admins override branch protection.
- **lockAllowsFetchAndMerge** (`Boolean`): Whether users can pull changes from upstream when the branch is locked. Set to
`true` to allow fork syncing. Set to `false` to prevent fork syncing.
- **lockBranch** (`Boolean`): Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.
- **pattern** (`String`): The glob-like pattern used to determine matching branches.
- **pushActorIds** (`[ID!]`): A list of User, Team, or App IDs allowed to push to matching branches.
- **requireLastPushApproval** (`Boolean`): Whether the most recent push must be approved by someone other than the person who pushed it.
- **requiredApprovingReviewCount** (`Int`): Number of approving reviews required to update matching branches.
- **requiredDeploymentEnvironments** (`[String!]`): The list of required deployment environments.
- **requiredStatusCheckContexts** (`[String!]`): List of required status check contexts that must pass for commits to be accepted to matching branches.
- **requiredStatusChecks** (`[RequiredStatusCheckInput!]`): The list of required status checks.
- **requiresApprovingReviews** (`Boolean`): Are approving reviews required to update matching branches.
- **requiresCodeOwnerReviews** (`Boolean`): Are reviews from code owners required to update matching branches.
- **requiresCommitSignatures** (`Boolean`): Are commits required to be signed.
- **requiresConversationResolution** (`Boolean`): Are conversations required to be resolved before merging.
- **requiresDeployments** (`Boolean`): Are successful deployments required before merging.
- **requiresLinearHistory** (`Boolean`): Are merge commits prohibited from being pushed to this branch.
- **requiresStatusChecks** (`Boolean`): Are status checks required to update matching branches.
- **requiresStrictStatusChecks** (`Boolean`): Are branches required to be up to date before merging.
- **restrictsPushes** (`Boolean`): Is pushing to matching branches restricted.
- **restrictsReviewDismissals** (`Boolean`): Is dismissal of pull request reviews restricted.
- **reviewDismissalActorIds** (`[ID!]`): A list of User, Team, or App IDs allowed to dismiss reviews on pull requests targeting matching branches.

### UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput

Autogenerated input type of UpdateEnterpriseAllowPrivateRepositoryForkingSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the allow private repository forking setting.
- **policyValue** (`EnterpriseAllowPrivateRepositoryForkingPolicyValue`): The value for the allow private repository forking policy on the enterprise.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the allow private repository forking setting on the enterprise.

### UpdateEnterpriseDefaultRepositoryPermissionSettingInput

Autogenerated input type of UpdateEnterpriseDefaultRepositoryPermissionSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the base repository permission setting.
- **settingValue** (`EnterpriseDefaultRepositoryPermissionSettingValue!`): The value for the base repository permission setting on the enterprise.

### UpdateEnterpriseDeployKeySettingInput

Autogenerated input type of UpdateEnterpriseDeployKeySetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the deploy key setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the deploy key setting on the enterprise.

### UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput

Autogenerated input type of UpdateEnterpriseMembersCanChangeRepositoryVisibilitySetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the members can change repository visibility setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the members can change repository visibility setting on the enterprise.

### UpdateEnterpriseMembersCanCreateRepositoriesSettingInput

Autogenerated input type of UpdateEnterpriseMembersCanCreateRepositoriesSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the members can create repositories setting.
- **membersCanCreateInternalRepositories** (`Boolean`): Allow members to create internal repositories. Defaults to current value.
- **membersCanCreatePrivateRepositories** (`Boolean`): Allow members to create private repositories. Defaults to current value.
- **membersCanCreatePublicRepositories** (`Boolean`): Allow members to create public repositories. Defaults to current value.
- **membersCanCreateRepositoriesPolicyEnabled** (`Boolean`): When false, allow member organizations to set their own repository creation member privileges.
- **settingValue** (`EnterpriseMembersCanCreateRepositoriesSettingValue`): Value for the members can create repositories setting on the enterprise. This
or the granular public/private/internal allowed fields (but not both) must be provided.

### UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput

Autogenerated input type of UpdateEnterpriseMembersCanDeleteRepositoriesSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the members can delete repositories setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the members can delete repositories setting on the enterprise.

### UpdateEnterpriseRepositoryProjectsSettingInput

Autogenerated input type of UpdateEnterpriseRepositoryProjectsSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the repository projects setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the repository projects setting on the enterprise.

### UpdateOrganizationAllowPrivateRepositoryForkingSettingInput

Autogenerated input type of UpdateOrganizationAllowPrivateRepositoryForkingSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **forkingEnabled** (`Boolean!`): Enable forking of private repositories in the organization?.
- **organizationId** (`ID!`): The ID of the organization on which to set the allow private repository forking setting.

### UpdateRepositoryCustomPropertyInput

Autogenerated input type of UpdateRepositoryCustomProperty.

**Input fields:**

- **allowedValues** (`[String!]`): The updated allowed values for the custom property.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **defaultValue** (`String`): The updated default value for the custom property if the property is required.
- **description** (`String`): The updated description of the custom property.
- **regex** (`String`): The regex pattern that the value of the custom property must match, if the `value_type` is `string`.
- **repositoryCustomPropertyId** (`ID!`): The global relay id of the source of the custom property.
- **requireExplicitValues** (`Boolean`): Whether this repository custom property requires explicit values.
- **required** (`Boolean`): Whether the updated custom property is required.
- **valuesEditableBy** (`RepositoryCustomPropertyValuesEditableBy`): The updated actors who can edit the values of the custom property.

### UpdateRepositoryInput

Autogenerated input type of UpdateRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **description** (`String`): A new description for the repository. Pass an empty string to erase the existing description.
- **hasDiscussionsEnabled** (`Boolean`): Indicates if the repository should have the discussions feature enabled.
- **hasIssuesEnabled** (`Boolean`): Indicates if the repository should have the issues feature enabled.
- **hasProjectsEnabled** (`Boolean`): Indicates if the repository should have the project boards feature enabled.
- **hasPullRequestsEnabled** (`Boolean`): Indicates if the repository should have the pull requests feature enabled.
- **hasSponsorshipsEnabled** (`Boolean`): Indicates if the repository displays a Sponsor button for financial contributions.
- **hasWikiEnabled** (`Boolean`): Indicates if the repository should have the wiki feature enabled.
- **homepageUrl** (`URI`): The URL for a web page about this repository. Pass an empty string to erase the existing URL.
- **name** (`String`): The new name of the repository.
- **pullRequestCreationPolicy** (`PullRequestCreationPolicy`): The policy controlling who can create pull requests in this repository.
- **repositoryId** (`ID!`): The ID of the repository to update.
- **template** (`Boolean`): Whether this repository should be marked as a template such that anyone who
can access it can create new repositories with the same files and directory structure.

### UpdateRepositoryRulesetInput

Autogenerated input type of UpdateRepositoryRuleset.

**Input fields:**

- **bypassActors** (`[RepositoryRulesetBypassActorInput!]`): A list of actors that are allowed to bypass rules in this ruleset.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **conditions** (`RepositoryRuleConditionsInput`): The list of conditions for this ruleset.
- **enforcement** (`RuleEnforcement`): The enforcement level for this ruleset.
- **name** (`String`): The name of the ruleset.
- **repositoryRulesetId** (`ID!`): The global relay id of the repository ruleset to be updated.
- **rules** (`[RepositoryRuleInput!]`): The list of rules for this ruleset.
- **target** (`RepositoryRulesetTarget`): The target of the ruleset.

### UpdateRepositoryWebCommitSignoffSettingInput

Autogenerated input type of UpdateRepositoryWebCommitSignoffSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryId** (`ID!`): The ID of the repository to update.
- **webCommitSignoffRequired** (`Boolean!`): Indicates if the repository should require signoff on web-based commits.

### UpdateTeamsRepositoryInput

Autogenerated input type of UpdateTeamsRepository.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **permission** (`RepositoryPermission!`): Permission that should be granted to the teams.
- **repositoryId** (`ID!`): Repository ID being granted access to.
- **teamIds** (`[ID!]!`): A list of teams being granted access. Limit: 10.

### UpdateTopicsInput

Autogenerated input type of UpdateTopics.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryId** (`ID!`): The Node ID of the repository.
- **topicNames** (`[String!]!`): An array of topic names.

### VerifiableDomainOrder

Ordering options for verifiable domain connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`VerifiableDomainOrderField!`): The field to order verifiable domains by.

### VerifyVerifiableDomainInput

Autogenerated input type of VerifyVerifiableDomain.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The ID of the verifiable domain to verify.

## Unions

### CreatedRepositoryOrRestrictedContribution

Represents either a repository the viewer can access or a restricted contribution.

**Possible types:** CreatedRepositoryContribution, RestrictedContribution

### VerifiableDomainOwner

Types that can own a verifiable domain.

**Possible types:** Enterprise, Organization
