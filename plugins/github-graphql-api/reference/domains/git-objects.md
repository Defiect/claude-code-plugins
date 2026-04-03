# Git Objects (Commits, Refs, Trees, Blobs)

[← Back to Reference Index](../README.md) | [Full Type Index](../index.md) | [Usage Guide](../guide.md)


## Queries

### meta

**Returns:** `GitHubMetadata!`

Return information about the GitHub instance.

## Mutations

### createRef

Create a new Git Ref.

**Input fields:**

- **input** (`CreateRefInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ref** (`Ref`): The newly created ref.

### deleteRef

Delete a Git Ref.

**Input fields:**

- **input** (`DeleteRefInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### updateCheckSuitePreferences

Modifies the settings of an existing check suite.

**Input fields:**

- **input** (`UpdateCheckSuitePreferencesInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The updated repository.

### updateOrganizationWebCommitSignoffSetting

Sets whether contributors are required to sign off on web-based commits for repositories in an organization.

**Input fields:**

- **input** (`UpdateOrganizationWebCommitSignoffSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **message** (`String`): A message confirming the result of updating the web commit signoff setting.
- **organization** (`Organization`): The organization with the updated web commit signoff setting.

### updateRef

Update a Git Ref.

**Input fields:**

- **input** (`UpdateRefInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ref** (`Ref`): The updated Ref.

### updateRefs

Creates, updates and/or deletes multiple refs in a repository.
This mutation takes a list of `RefUpdate`s and performs these updates
on the repository. All updates are performed atomically, meaning that
if one of them is rejected, no other ref will be modified.
`RefUpdate.beforeOid` specifies that the given reference needs to point
to the given value before performing any updates. A value of
`0000000000000000000000000000000000000000` can be used to verify that
the references should not exist.
`RefUpdate.afterOid` specifies the value that the given reference
will point to after performing all updates. A value of
`0000000000000000000000000000000000000000` can be used to delete a
reference.
If `RefUpdate.force` is set to `true`, a non-fast-forward updates
for the given reference will be allowed.

**Input fields:**

- **input** (`UpdateRefsInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### updateSponsorshipPreferences

Change visibility of your sponsorship and opt in or out of email updates from the maintainer.

**Input fields:**

- **input** (`UpdateSponsorshipPreferencesInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **sponsorship** (`Sponsorship`): The sponsorship that was updated.

## Types

### Blame

Represents a Git blame.

**Fields:**

- **ranges** (`[BlameRange!]!`): The list of ranges from a Git blame.

### BlameRange

Represents a range of information from a Git blame.

**Fields:**

- **age** (`Int!`): Identifies the recency of the change, from 1 (new) to 10 (old). This is
calculated as a 2-quantile and determines the length of distance between the
median age of all the changes in the file and the recency of the current
range's change.
- **commit** (`Commit!`): Identifies the line author.
- **endingLine** (`Int!`): The ending line for the range.
- **startingLine** (`Int!`): The starting line for the range.

### Blob

Represents a Git blob.

**Implements:** GitObject, Node

**Fields:**

- **abbreviatedOid** (`String!`): An abbreviated version of the Git object ID.
- **byteSize** (`Int!`): Byte size of Blob object.
- **commitResourcePath** (`URI!`): The HTTP path for this Git object.
- **commitUrl** (`URI!`): The HTTP URL for this Git object.
- **id** (`ID!`): The Node ID of the Blob object.
- **isBinary** (`Boolean`): Indicates whether the Blob is binary or text. Returns null if unable to determine the encoding.
- **isTruncated** (`Boolean!`): Indicates whether the contents is truncated.
- **oid** (`GitObjectID!`): The Git object ID.
- **repository** (`Repository!`): The Repository the Git object belongs to.
- **text** (`String`): UTF8 text data or null if the Blob is binary.

### BypassForcePushAllowance

A user, team, or app who has the ability to bypass a force push requirement on a protected branch.

**Implements:** Node

**Fields:**

- **actor** (`BranchActorAllowanceActor`): The actor that can force push.
- **branchProtectionRule** (`BranchProtectionRule`): Identifies the branch protection rule associated with the allowed user, team, or app.
- **id** (`ID!`): The Node ID of the BypassForcePushAllowance object.

### Commit

Represents a Git commit.

**Implements:** GitObject, Node, Subscribable, UniformResourceLocatable

**Fields:**

- **abbreviatedOid** (`String!`): An abbreviated version of the Git object ID.
- **additions** (`Int!`): The number of additions in this commit.
- **associatedPullRequests** (`PullRequestConnection`): The merged Pull Request that introduced the commit to the repository. If the
commit is not present in the default branch, additionally returns open Pull
Requests associated with the commit.
- **author** (`GitActor`): Authorship details of the commit.
- **authoredByCommitter** (`Boolean!`): Check if the committer and the author match.
- **authoredDate** (`DateTime!`): The datetime when this commit was authored.
- **authors** (`GitActorConnection!`): The list of authors for this commit based on the git author and the Co-authored-by
message trailer. The git author will always be first.
- **blame** (`Blame!`): Fetches `git blame` information.
- **changedFiles** (`Int!`): We recommend using the `changedFilesIfAvailable` field instead of
`changedFiles`, as `changedFiles` will cause your request to return an error
if GitHub is unable to calculate the number of changed files.
- **changedFilesIfAvailable** (`Int`): The number of changed files in this commit. If GitHub is unable to calculate
the number of changed files (for example due to a timeout), this will return
`null`. We recommend using this field instead of `changedFiles`.
- **checkSuites** (`CheckSuiteConnection`): The check suites associated with a commit.
- **comments** (`CommitCommentConnection!`): Comments made on the commit.
- **commitResourcePath** (`URI!`): The HTTP path for this Git object.
- **commitUrl** (`URI!`): The HTTP URL for this Git object.
- **committedDate** (`DateTime!`): The datetime when this commit was committed.
- **committedViaWeb** (`Boolean!`): Check if committed via GitHub web UI.
- **committer** (`GitActor`): Committer details of the commit.
- **deletions** (`Int!`): The number of deletions in this commit.
- **deployments** (`DeploymentConnection`): The deployments associated with a commit.
- **file** (`TreeEntry`): The tree entry representing the file located at the given path.
- **history** (`CommitHistoryConnection!`): The linear commit history starting from (and including) this commit, in the same order as `git log`.
- **id** (`ID!`): The Node ID of the Commit object.
- **message** (`String!`): The Git commit message.
- **messageBody** (`String!`): The Git commit message body.
- **messageBodyHTML** (`HTML!`): The commit message body rendered to HTML.
- **messageHeadline** (`String!`): The Git commit message headline.
- **messageHeadlineHTML** (`HTML!`): The commit message headline rendered to HTML.
- **oid** (`GitObjectID!`): The Git object ID.
- **onBehalfOf** (`Organization`): The organization this commit was made on behalf of.
- **parents** (`CommitConnection!`): The parents of a commit.
- **pushedDate** (`DateTime`): The datetime when this commit was pushed.
- **repository** (`Repository!`): The Repository this commit belongs to.
- **resourcePath** (`URI!`): The HTTP path for this commit.
- **signature** (`GitSignature`): Commit signing information, if present.
- **status** (`Status`): Status information for this commit.
- **statusCheckRollup** (`StatusCheckRollup`): Check and Status rollup information for this commit.
- **submodules** (`SubmoduleConnection!`): Returns a list of all submodules in this repository as of this Commit parsed from the .gitmodules file.
- **tarballUrl** (`URI!`): Returns a URL to download a tarball archive for a repository.
Note: For private repositories, these links are temporary and expire after five minutes.
- **tree** (`Tree!`): Commit's root Tree.
- **treeResourcePath** (`URI!`): The HTTP path for the tree of this commit.
- **treeUrl** (`URI!`): The HTTP URL for the tree of this commit.
- **url** (`URI!`): The HTTP URL for this commit.
- **viewerCanSubscribe** (`Boolean!`): Check if the viewer is able to change their subscription status for the repository.
- **viewerSubscription** (`SubscriptionState`): Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.
- **zipballUrl** (`URI!`): Returns a URL to download a zipball archive for a repository.
Note: For private repositories, these links are temporary and expire after five minutes.

### CommitAuthorEmailPatternParameters

Parameters to be used for the commit_author_email_pattern rule.

**Fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean!`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### CommitComment

Represents a comment on a given Commit.

**Implements:** Comment, Deletable, Minimizable, Node, Reactable, RepositoryNode, Updatable, UpdatableComment

**Fields:**

- **author** (`Actor`): The actor who authored the comment.
- **authorAssociation** (`CommentAuthorAssociation!`): Author's association with the subject of the comment.
- **body** (`String!`): Identifies the comment body.
- **bodyHTML** (`HTML!`): The body rendered to HTML.
- **bodyText** (`String!`): The body rendered to text.
- **commit** (`Commit`): Identifies the commit associated with the comment, if the commit exists.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **createdViaEmail** (`Boolean!`): Check if this comment was created via an email reply.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **editor** (`Actor`): The actor who edited the comment.
- **id** (`ID!`): The Node ID of the CommitComment object.
- **includesCreatedEdit** (`Boolean!`): Check if this comment was edited and includes an edit with the creation data.
- **isMinimized** (`Boolean!`): Returns whether or not a comment has been minimized.
- **lastEditedAt** (`DateTime`): The moment the editor made the last edit.
- **minimizedReason** (`String`): Returns why the comment was minimized. One of `abuse`, `off-topic`,
`outdated`, `resolved`, `duplicate`, `spam`, and `low-quality`. Note that the
case and formatting of these values differs from the inputs to the
`MinimizeComment` mutation.
- **path** (`String`): Identifies the file path associated with the comment.
- **position** (`Int`): Identifies the line position associated with the comment.
- **publishedAt** (`DateTime`): Identifies when the comment was published at.
- **reactionGroups** (`[ReactionGroup!]`): A list of reactions grouped by content left on the subject.
- **reactions** (`ReactionConnection!`): A list of Reactions left on the Issue.
- **repository** (`Repository!`): The repository associated with this node.
- **resourcePath** (`URI!`): The HTTP path permalink for this commit comment.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL permalink for this commit comment.
- **userContentEdits** (`UserContentEditConnection`): A list of edits to this content.
- **viewerCanDelete** (`Boolean!`): Check if the current viewer can delete this object.
- **viewerCanMinimize** (`Boolean!`): Check if the current viewer can minimize this object.
- **viewerCanReact** (`Boolean!`): Can user react to this subject.
- **viewerCanUnminimize** (`Boolean!`): Check if the current viewer can unminimize this object.
- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.
- **viewerCannotUpdateReasons** (`[CommentCannotUpdateReason!]!`): Reasons why the current viewer can not update this comment.
- **viewerDidAuthor** (`Boolean!`): Did the viewer author this comment.

### CommitCommentThread

A thread of comments on a commit.

**Implements:** Node, RepositoryNode

**Fields:**

- **comments** (`CommitCommentConnection!`): The comments that exist in this thread.
- **commit** (`Commit`): The commit the comments were made on.
- **id** (`ID!`): The Node ID of the CommitCommentThread object.
- **path** (`String`): The file the comments were made on.
- **position** (`Int`): The position in the diff for the commit that the comment was made on.
- **repository** (`Repository!`): The repository associated with this node.

### CommitMessagePatternParameters

Parameters to be used for the commit_message_pattern rule.

**Fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean!`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### CommitterEmailPatternParameters

Parameters to be used for the committer_email_pattern rule.

**Fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean!`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### Comparison

Represents a comparison between two commit revisions.

**Implements:** Node

**Fields:**

- **aheadBy** (`Int!`): The number of commits ahead of the base branch.
- **baseTarget** (`GitObject!`): The base revision of this comparison.
- **behindBy** (`Int!`): The number of commits behind the base branch.
- **commits** (`ComparisonCommitConnection!`): The commits which compose this comparison.
- **headTarget** (`GitObject!`): The head revision of this comparison.
- **id** (`ID!`): The Node ID of the Comparison object.
- **status** (`ComparisonStatus!`): The status of this comparison.

### CreatedCommitContribution

Represents the contribution a user made by committing to a repository.

**Implements:** Contribution

**Fields:**

- **commitCount** (`Int!`): How many commits were made on this day to this repository by the user.
- **isRestricted** (`Boolean!`): Whether this contribution is associated with a record you do not have access to. For
example, your own 'first issue' contribution may have been made on a repository you can no
longer access.
- **occurredAt** (`DateTime!`): When this contribution was made.
- **repository** (`Repository!`): The repository the user made a commit in.
- **resourcePath** (`URI!`): The HTTP path for this contribution.
- **url** (`URI!`): The HTTP URL for this contribution.
- **user** (`User!`): The user who made this contribution.

### CrossReferencedEvent

Represents a mention made by one issue or pull request to another.

**Implements:** Node, UniformResourceLocatable

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the CrossReferencedEvent object.
- **isCrossRepository** (`Boolean!`): Reference originated in a different repository.
- **referencedAt** (`DateTime!`): Identifies when the reference was made.
- **resourcePath** (`URI!`): The HTTP path for this pull request.
- **source** (`ReferencedSubject!`): Issue or pull request that made the reference.
- **target** (`ReferencedSubject!`): Issue or pull request to which the reference was made.
- **url** (`URI!`): The HTTP URL for this pull request.
- **willCloseTarget** (`Boolean!`): Checks if the target will be closed when the source is merged.

### GitActor

Represents an actor in a Git commit (ie. an author or committer).

**Fields:**

- **avatarUrl** (`URI!`): A URL pointing to the author's public avatar.
- **date** (`GitTimestamp`): The timestamp of the Git action (authoring or committing).
- **email** (`String`): The email in the Git commit.
- **name** (`String`): The name in the Git commit.
- **user** (`User`): The GitHub user corresponding to the email field. Null if no such user exists.

### GitHubMetadata

Represents information about the GitHub instance.

**Fields:**

- **gitHubServicesSha** (`GitObjectID!`): Returns a String that's a SHA of `github-services`.
- **gitIpAddresses** (`[String!]`): IP addresses that users connect to for git operations.
- **githubEnterpriseImporterIpAddresses** (`[String!]`): IP addresses that GitHub Enterprise Importer uses for outbound connections.
- **hookIpAddresses** (`[String!]`): IP addresses that service hooks are sent from.
- **importerIpAddresses** (`[String!]`): IP addresses that the importer connects from.
- **isPasswordAuthenticationVerifiable** (`Boolean!`): Whether or not users are verified.
- **pagesIpAddresses** (`[String!]`): IP addresses for GitHub Pages' A records.

### GpgSignature

Represents a GPG signature on a Commit or Tag.

**Implements:** GitSignature

**Fields:**

- **email** (`String!`): Email used to sign this object.
- **isValid** (`Boolean!`): True if the signature is valid and verified by GitHub.
- **keyId** (`String`): Hex-encoded ID of the key that signed this object.
- **payload** (`String!`): Payload for GPG signing object. Raw ODB object without the signature header.
- **signature** (`String!`): ASCII-armored signature header from object.
- **signer** (`User`): GitHub user corresponding to the email signing this commit.
- **state** (`GitSignatureState!`): The state of this signature. `VALID` if signature is valid and verified by
GitHub, otherwise represents reason why signature is considered invalid.
- **verifiedAt** (`DateTime`): The date the signature was verified, if valid.
- **wasSignedByGitHub** (`Boolean!`): True if the signature was made with GitHub's signing key.

### PackageTag

A version tag contains the mapping between a tag name and a version.

**Implements:** Node

**Fields:**

- **id** (`ID!`): The Node ID of the PackageTag object.
- **name** (`String!`): Identifies the tag name of the version.
- **version** (`PackageVersion`): Version that the tag is associated with.

### Push

A Git push.

**Implements:** Node

**Fields:**

- **id** (`ID!`): The Node ID of the Push object.
- **nextSha** (`GitObjectID`): The SHA after the push.
- **permalink** (`URI!`): The permalink for this push.
- **previousSha** (`GitObjectID`): The SHA before the push.
- **pusher** (`Actor!`): The actor who pushed.
- **repository** (`Repository!`): The repository that was pushed to.

### PushAllowance

A team, user, or app who has the ability to push to a protected branch.

**Implements:** Node

**Fields:**

- **actor** (`PushAllowanceActor`): The actor that can push.
- **branchProtectionRule** (`BranchProtectionRule`): Identifies the branch protection rule associated with the allowed user, team, or app.
- **id** (`ID!`): The Node ID of the PushAllowance object.

### Ref

Represents a Git reference.

**Implements:** Node

**Fields:**

- **associatedPullRequests** (`PullRequestConnection!`): A list of pull requests with this ref as the head ref.
- **branchProtectionRule** (`BranchProtectionRule`): Branch protection rules for this ref.
- **compare** (`Comparison`): Compares the current ref as a base ref to another head ref, if the comparison can be made.
- **id** (`ID!`): The Node ID of the Ref object.
- **name** (`String!`): The ref name.
- **prefix** (`String!`): The ref's prefix, such as `refs/heads/` or `refs/tags/`.
- **refUpdateRule** (`RefUpdateRule`): Branch protection rules that are viewable by non-admins.
- **repository** (`Repository!`): The repository the ref belongs to.
- **rules** (`RepositoryRuleConnection`): A list of rules from active Repository and Organization rulesets that apply to this ref.
- **target** (`GitObject`): The object the ref points to. Returns null when object does not exist.

### RefNameConditionTarget

Parameters to be used for the ref_name condition.

**Fields:**

- **exclude** (`[String!]!`): Array of ref names or patterns to exclude. The condition will not pass if any of these patterns match.
- **include** (`[String!]!`): Array of ref names or patterns to include. One of these patterns must match
for the condition to pass. Also accepts `~DEFAULT_BRANCH` to include the
default branch or `~ALL` to include all branches.

### RefUpdateRule

Branch protection rules that are enforced on the viewer.

**Fields:**

- **allowsDeletions** (`Boolean!`): Can this branch be deleted.
- **allowsForcePushes** (`Boolean!`): Are force pushes allowed on this branch.
- **blocksCreations** (`Boolean!`): Can matching branches be created.
- **pattern** (`String!`): Identifies the protection rule pattern.
- **requiredApprovingReviewCount** (`Int`): Number of approving reviews required to update matching branches.
- **requiredStatusCheckContexts** (`[String]`): List of required status check contexts that must pass for commits to be accepted to matching branches.
- **requiresCodeOwnerReviews** (`Boolean!`): Are reviews from code owners required to update matching branches.
- **requiresConversationResolution** (`Boolean!`): Are conversations required to be resolved before merging.
- **requiresLinearHistory** (`Boolean!`): Are merge commits prohibited from being pushed to this branch.
- **requiresSignatures** (`Boolean!`): Are commits required to be signed.
- **viewerAllowedToDismissReviews** (`Boolean!`): Is the viewer allowed to dismiss reviews.
- **viewerCanPush** (`Boolean!`): Can the viewer push to the branch.

### ReferencedEvent

Represents a`referenced`event on a given `ReferencedSubject`.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **commit** (`Commit`): Identifies the commit associated with the`referenced`event.
- **commitRepository** (`Repository!`): Identifies the repository associated with the`referenced`event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the ReferencedEvent object.
- **isCrossRepository** (`Boolean!`): Reference originated in a different repository.
- **isDirectReference** (`Boolean!`): Checks if the commit message itself references the subject. Can be false in the case of a commit comment reference.
- **subject** (`ReferencedSubject!`): Object referenced by event.

### SecurityAdvisoryReference

A GitHub Security Advisory Reference.

**Fields:**

- **url** (`URI!`): A publicly accessible reference.

### SmimeSignature

Represents an S/MIME signature on a Commit or Tag.

**Implements:** GitSignature

**Fields:**

- **email** (`String!`): Email used to sign this object.
- **isValid** (`Boolean!`): True if the signature is valid and verified by GitHub.
- **payload** (`String!`): Payload for GPG signing object. Raw ODB object without the signature header.
- **signature** (`String!`): ASCII-armored signature header from object.
- **signer** (`User`): GitHub user corresponding to the email signing this commit.
- **state** (`GitSignatureState!`): The state of this signature. `VALID` if signature is valid and verified by
GitHub, otherwise represents reason why signature is considered invalid.
- **verifiedAt** (`DateTime`): The date the signature was verified, if valid.
- **wasSignedByGitHub** (`Boolean!`): True if the signature was made with GitHub's signing key.

### SshSignature

Represents an SSH signature on a Commit or Tag.

**Implements:** GitSignature

**Fields:**

- **email** (`String!`): Email used to sign this object.
- **isValid** (`Boolean!`): True if the signature is valid and verified by GitHub.
- **keyFingerprint** (`String`): Hex-encoded fingerprint of the key that signed this object.
- **payload** (`String!`): Payload for GPG signing object. Raw ODB object without the signature header.
- **signature** (`String!`): ASCII-armored signature header from object.
- **signer** (`User`): GitHub user corresponding to the email signing this commit.
- **state** (`GitSignatureState!`): The state of this signature. `VALID` if signature is valid and verified by
GitHub, otherwise represents reason why signature is considered invalid.
- **verifiedAt** (`DateTime`): The date the signature was verified, if valid.
- **wasSignedByGitHub** (`Boolean!`): True if the signature was made with GitHub's signing key.

### Tag

Represents a Git tag.

**Implements:** GitObject, Node

**Fields:**

- **abbreviatedOid** (`String!`): An abbreviated version of the Git object ID.
- **commitResourcePath** (`URI!`): The HTTP path for this Git object.
- **commitUrl** (`URI!`): The HTTP URL for this Git object.
- **id** (`ID!`): The Node ID of the Tag object.
- **message** (`String`): The Git tag message.
- **name** (`String!`): The Git tag name.
- **oid** (`GitObjectID!`): The Git object ID.
- **repository** (`Repository!`): The Repository the Git object belongs to.
- **tagger** (`GitActor`): Details about the tag author.
- **target** (`GitObject!`): The Git object the tag points to.

### TagNamePatternParameters

Parameters to be used for the tag_name_pattern rule.

**Fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean!`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### Tree

Represents a Git tree.

**Implements:** GitObject, Node

**Fields:**

- **abbreviatedOid** (`String!`): An abbreviated version of the Git object ID.
- **commitResourcePath** (`URI!`): The HTTP path for this Git object.
- **commitUrl** (`URI!`): The HTTP URL for this Git object.
- **entries** (`[TreeEntry!]`): A list of tree entries.
- **id** (`ID!`): The Node ID of the Tree object.
- **oid** (`GitObjectID!`): The Git object ID.
- **repository** (`Repository!`): The Repository the Git object belongs to.

### TreeEntry

Represents a Git tree entry.

**Fields:**

- **extension** (`String`): The extension of the file.
- **isGenerated** (`Boolean!`): Whether or not this tree entry is generated.
- **language** (`Language`): The programming language this file is written in.
- **lineCount** (`Int`): Number of lines in the file.
- **mode** (`Int!`): Entry file mode.
- **name** (`String!`): Entry file name.
- **nameRaw** (`Base64String!`): Entry file name. (Base64-encoded).
- **object** (`GitObject`): Entry file object.
- **oid** (`GitObjectID!`): Entry file Git object ID.
- **path** (`String`): The full path of the file.
- **pathRaw** (`Base64String`): The full path of the file. (Base64-encoded).
- **repository** (`Repository!`): The Repository the tree entry belongs to.
- **size** (`Int!`): Entry byte size.
- **submodule** (`Submodule`): If the TreeEntry is for a directory occupied by a submodule project, this returns the corresponding submodule.
- **type** (`String!`): Entry file type.

### UnknownSignature

Represents an unknown signature on a Commit or Tag.

**Implements:** GitSignature

**Fields:**

- **email** (`String!`): Email used to sign this object.
- **isValid** (`Boolean!`): True if the signature is valid and verified by GitHub.
- **payload** (`String!`): Payload for GPG signing object. Raw ODB object without the signature header.
- **signature** (`String!`): ASCII-armored signature header from object.
- **signer** (`User`): GitHub user corresponding to the email signing this commit.
- **state** (`GitSignatureState!`): The state of this signature. `VALID` if signature is valid and verified by
GitHub, otherwise represents reason why signature is considered invalid.
- **verifiedAt** (`DateTime`): The date the signature was verified, if valid.
- **wasSignedByGitHub** (`Boolean!`): True if the signature was made with GitHub's signing key.

### WorkflowFileReference

A workflow that must run for this rule to pass.

**Fields:**

- **path** (`String!`): The path to the workflow file.
- **ref** (`String`): The ref (branch or tag) of the workflow file to use.
- **repositoryId** (`Int!`): The ID of the repository where the workflow is defined.
- **sha** (`String`): The commit SHA of the workflow file to use.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **BypassForcePushAllowanceConnection** (4 fields): The connection type for BypassForcePushAllowance.
- **BypassForcePushAllowanceEdge** (2 fields): An edge in a connection.
- **CommitCommentConnection** (4 fields): The connection type for CommitComment.
- **CommitCommentEdge** (2 fields): An edge in a connection.
- **CommitConnection** (4 fields): The connection type for Commit.
- **CommitEdge** (2 fields): An edge in a connection.
- **CommitHistoryConnection** (4 fields): The connection type for Commit.
- **ComparisonCommitConnection** (5 fields): The connection type for Commit.
- **CreatedCommitContributionConnection** (4 fields): The connection type for CreatedCommitContribution.
- **CreatedCommitContributionEdge** (2 fields): An edge in a connection.
- **GitActorConnection** (4 fields): The connection type for GitActor.
- **GitActorEdge** (2 fields): An edge in a connection.
- **PushAllowanceConnection** (4 fields): The connection type for PushAllowance.
- **PushAllowanceEdge** (2 fields): An edge in a connection.
- **RefConnection** (4 fields): The connection type for Ref.
- **RefEdge** (2 fields): An edge in a connection.

## Enums

### CommitContributionOrderField

Properties by which commit contribution connections can be ordered.

**Values:**

- `COMMIT_COUNT`: Order commit contributions by how many commits they represent.
- `OCCURRED_AT`: Order commit contributions by when they were made.

### ComparisonStatus

The status of a git comparison between two refs.

**Values:**

- `AHEAD`: The head ref is ahead of the base ref.
- `BEHIND`: The head ref is behind the base ref.
- `DIVERGED`: The head ref is both ahead and behind of the base ref, indicating git history has diverged.
- `IDENTICAL`: The head ref and base ref are identical.

### MergeCommitMessage

The possible default commit messages for merges.

**Values:**

- `BLANK`: Default to a blank commit message.
- `PR_BODY`: Default to the pull request's body.
- `PR_TITLE`: Default to the pull request's title.

### MergeCommitTitle

The possible default commit titles for merges.

**Values:**

- `MERGE_MESSAGE`: Default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).
- `PR_TITLE`: Default to the pull request's title.

### RefOrderField

Properties by which ref connections can be ordered.

**Values:**

- `ALPHABETICAL`: Order refs by their alphanumeric name.
- `TAG_COMMIT_DATE`: Order refs by underlying commit date if the ref prefix is refs/tags/.

### SquashMergeCommitMessage

The possible default commit messages for squash merges.

**Values:**

- `BLANK`: Default to a blank commit message.
- `COMMIT_MESSAGES`: Default to the branch's commit messages.
- `PR_BODY`: Default to the pull request's body.

### SquashMergeCommitTitle

The possible default commit titles for squash merges.

**Values:**

- `COMMIT_OR_PR_TITLE`: Default to the commit's title (if only one commit) or the pull request's title (when more than one commit).
- `PR_TITLE`: Default to the pull request's title.

## Input Objects

### CommitAuthor

Specifies an author for filtering Git commits.

**Input fields:**

- **emails** (`[String!]`): Email addresses to filter by. Commits authored by any of the specified email addresses will be returned.
- **id** (`ID`): ID of a User to filter by. If non-null, only commits authored by this user
will be returned. This field takes precedence over emails.

### CommitAuthorEmailPatternParametersInput

Parameters to be used for the commit_author_email_pattern rule.

**Input fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### CommitContributionOrder

Ordering options for commit contribution connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`CommitContributionOrderField!`): The field by which to order commit contributions.

### CommitMessage

A message to include with a new commit.

**Input fields:**

- **body** (`String`): The body of the message.
- **headline** (`String!`): The headline of the message.

### CommitMessagePatternParametersInput

Parameters to be used for the commit_message_pattern rule.

**Input fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### CommittableBranch

A git ref for a commit to be appended to.
The ref must be a branch, i.e. its fully qualified name must start
with `refs/heads/` (although the input is not required to be fully
qualified).
The Ref may be specified by its global node ID or by the
`repositoryNameWithOwner` and `branchName`.
Examples
Specify a branch using a global node ID:
`{ "id": "MDM6UmVmMTpyZWZzL2hlYWRzL21haW4=" }
`
Specify a branch using `repositoryNameWithOwner` and `branchName`:
`{
  "repositoryNameWithOwner": "github/graphql-client",
  "branchName": "main"
}.
`

**Input fields:**

- **branchName** (`String`): The unqualified name of the branch to append the commit to.
- **id** (`ID`): The Node ID of the Ref to be updated.
- **repositoryNameWithOwner** (`String`): The nameWithOwner of the repository to commit to.

### CommitterEmailPatternParametersInput

Parameters to be used for the committer_email_pattern rule.

**Input fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### CreateCommitOnBranchInput

Autogenerated input type of CreateCommitOnBranch.

**Input fields:**

- **branch** (`CommittableBranch!`): The Ref to be updated.  Must be a branch.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **expectedHeadOid** (`GitObjectID!`): The git commit oid expected at the head of the branch prior to the commit.
- **fileChanges** (`FileChanges`): A description of changes to files in this commit.
- **message** (`CommitMessage!`): The commit message the be included with the commit.

### CreateRefInput

Autogenerated input type of CreateRef.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **name** (`String!`): The fully qualified name of the new Ref (ie: `refs/heads/my_new_branch`).
- **oid** (`GitObjectID!`): The GitObjectID that the new Ref shall target. Must point to a commit.
- **repositoryId** (`ID!`): The Node ID of the Repository to create the Ref in.

### DeleteRefInput

Autogenerated input type of DeleteRef.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **refId** (`ID!`): The Node ID of the Ref to be deleted.

### RefNameConditionTargetInput

Parameters to be used for the ref_name condition.

**Input fields:**

- **exclude** (`[String!]!`): Array of ref names or patterns to exclude. The condition will not pass if any of these patterns match.
- **include** (`[String!]!`): Array of ref names or patterns to include. One of these patterns must match
for the condition to pass. Also accepts `~DEFAULT_BRANCH` to include the
default branch or `~ALL` to include all branches.

### RefOrder

Ways in which lists of git refs can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order refs by the specified field.
- **field** (`RefOrderField!`): The field in which to order refs by.

### RefUpdate

A ref update.

**Input fields:**

- **afterOid** (`GitObjectID!`): The value this ref should be updated to.
- **beforeOid** (`GitObjectID`): The value this ref needs to point to before the update.
- **force** (`Boolean`): Force a non fast-forward update.
- **name** (`GitRefname!`): The fully qualified name of the ref to be update. For example `refs/heads/branch-name`.

### TagNamePatternParametersInput

Parameters to be used for the tag_name_pattern rule.

**Input fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### UpdateOrganizationWebCommitSignoffSettingInput

Autogenerated input type of UpdateOrganizationWebCommitSignoffSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organizationId** (`ID!`): The ID of the organization on which to set the web commit signoff setting.
- **webCommitSignoffRequired** (`Boolean!`): Enable signoff on web-based commits for repositories in the organization?.

### UpdateRefInput

Autogenerated input type of UpdateRef.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **force** (`Boolean`): Permit updates of branch Refs that are not fast-forwards?.
- **oid** (`GitObjectID!`): The GitObjectID that the Ref shall be updated to target.
- **refId** (`ID!`): The Node ID of the Ref to be updated.

### UpdateRefsInput

Autogenerated input type of UpdateRefs.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **refUpdates** (`[RefUpdate!]!`): A list of ref updates.
- **repositoryId** (`ID!`): The Node ID of the repository.

### WorkflowFileReferenceInput

A workflow that must run for this rule to pass.

**Input fields:**

- **path** (`String!`): The path to the workflow file.
- **ref** (`String`): The ref (branch or tag) of the workflow file to use.
- **repositoryId** (`Int!`): The ID of the repository where the workflow is defined.
- **sha** (`String`): The commit SHA of the workflow file to use.

## Unions

### PushAllowanceActor

Types that can be an actor.

**Possible types:** App, Team, User

### ReferencedSubject

Any referencable object.

**Possible types:** Issue, PullRequest


---

**See also:** [Repositories](repositories.md) | [Pull Requests](pull-requests.md) | [Actions & CI](actions-and-ci.md)
