# Issues, Labels & Milestones

[← Back to Reference Index](../README.md) | [Full Type Index](../index.md) | [Usage Guide](../guide.md)


## Mutations

### addLabelsToLabelable

Adds labels to a labelable object.

**Input fields:**

- **input** (`AddLabelsToLabelableInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **labelable** (`Labelable`): The item that was labeled.

### addProjectV2DraftIssue

Creates a new draft issue and add it to a Project.

**Input fields:**

- **input** (`AddProjectV2DraftIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectItem** (`ProjectV2Item`): The draft issue added to the project.

### addSubIssue

Adds a sub-issue to a given issue.

**Input fields:**

- **input** (`AddSubIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The parent issue that the sub-issue was added to.
- **subIssue** (`Issue`): The sub-issue of the parent.

### clearLabelsFromLabelable

Clears all labels from a labelable object.

**Input fields:**

- **input** (`ClearLabelsFromLabelableInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **labelable** (`Labelable`): The item that was unlabeled.

### closeIssue

Close an issue.

**Input fields:**

- **input** (`CloseIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue that was closed.

### convertProjectCardNoteToIssue

Convert a project note card to one associated with a newly created issue.

**Input fields:**

- **input** (`ConvertProjectCardNoteToIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectCard** (`ProjectCard`): The updated ProjectCard.

### convertProjectV2DraftIssueItemToIssue

Converts a projectV2 draft issue item to an issue.

**Input fields:**

- **input** (`ConvertProjectV2DraftIssueItemToIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **item** (`ProjectV2Item`): The updated project item.

### createIssue

Creates a new issue.

**Input fields:**

- **input** (`CreateIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The new issue.

### createIssueField

Creates a new issue field.

**Input fields:**

- **input** (`CreateIssueFieldInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueField** (`IssueFields`): The newly created issue field.

### createIssueFieldValue

Creates a new issue field value for an issue.

**Input fields:**

- **input** (`CreateIssueFieldValueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue object.
- **issueFieldValue** (`IssueFieldValue`): The newly created issue field value.

### createIssueType

Creates a new issue type.

**Input fields:**

- **input** (`CreateIssueTypeInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueType** (`IssueType`): The newly created issue type.

### createLabel

Creates a new label.

**Input fields:**

- **input** (`CreateLabelInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **label** (`Label`): The new label.

### createProjectV2IssueField

Create a new project issue field.

**Input fields:**

- **input** (`CreateProjectV2IssueFieldInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2Field** (`ProjectV2FieldConfiguration`): The new field.

### deleteIssue

Deletes an Issue object.

**Input fields:**

- **input** (`DeleteIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repository** (`Repository`): The repository the issue belonged to.

### deleteIssueComment

Deletes an IssueComment object.

**Input fields:**

- **input** (`DeleteIssueCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### deleteIssueField

Deletes an issue field.

**Input fields:**

- **input** (`DeleteIssueFieldInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueField** (`IssueFields`): The deleted issue field.

### deleteIssueFieldValue

Deletes an issue field value from an issue.

**Input fields:**

- **input** (`DeleteIssueFieldValueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue object.
- **success** (`Boolean`): Whether the field value was successfully deleted.

### deleteIssueType

Delete an issue type.

**Input fields:**

- **input** (`DeleteIssueTypeInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deletedIssueTypeId** (`ID`): The ID of the deleted issue type.

### deleteLabel

Deletes a label.

**Input fields:**

- **input** (`DeleteLabelInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### pinIssue

Pin an issue to a repository.

**Input fields:**

- **input** (`PinIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue that was pinned.

### pinIssueComment

Pins an Issue Comment.

**Input fields:**

- **input** (`PinIssueCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueComment** (`IssueComment`): The Issue Comment that was pinned.

### removeLabelsFromLabelable

Removes labels from a Labelable object.

**Input fields:**

- **input** (`RemoveLabelsFromLabelableInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **labelable** (`Labelable`): The Labelable the labels were removed from.

### removeSubIssue

Removes a sub-issue from a given issue.

**Input fields:**

- **input** (`RemoveSubIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The parent of the sub-issue.
- **subIssue** (`Issue`): The sub-issue of the parent.

### reopenIssue

Reopen a issue.

**Input fields:**

- **input** (`ReopenIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue that was opened.

### reprioritizeSubIssue

Reprioritizes a sub-issue to a different position in the parent list.

**Input fields:**

- **input** (`ReprioritizeSubIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The parent issue that the sub-issue was reprioritized in.

### setIssueFieldValue

Sets the value of an IssueFieldValue.

**Input fields:**

- **input** (`SetIssueFieldValueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue where the field values were set.
- **issueFieldValues** (`[IssueFieldValue!]`): The issue field values that were created or updated.

### transferIssue

Transfer an issue to a different repository.

**Input fields:**

- **input** (`TransferIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue that was transferred.

### unmarkIssueAsDuplicate

Unmark an issue as a duplicate of another issue.

**Input fields:**

- **input** (`UnmarkIssueAsDuplicateInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **duplicate** (`IssueOrPullRequest`): The issue or pull request that was marked as a duplicate.

### unpinIssue

Unpin a pinned issue from a repository.

**Input fields:**

- **input** (`UnpinIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID`): The id of the pinned issue that was unpinned.
- **issue** (`Issue`): The issue that was unpinned.

### unpinIssueComment

Unpins an Issue Comment.

**Input fields:**

- **input** (`UnpinIssueCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueComment** (`IssueComment`): The Issue Comment that was unpinned.

### updateEnterpriseMembersCanDeleteIssuesSetting

Sets the members can delete issues setting for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseMembersCanDeleteIssuesSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated members can delete issues setting.
- **message** (`String`): A message confirming the result of updating the members can delete issues setting.

### updateIssue

Updates an Issue.

**Input fields:**

- **input** (`UpdateIssueInput!`)

**Return fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue.

### updateIssueComment

Updates an IssueComment object.

**Input fields:**

- **input** (`UpdateIssueCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueComment** (`IssueComment`): The updated comment.

### updateIssueField

Updates an issue field.

**Input fields:**

- **input** (`UpdateIssueFieldInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueField** (`IssueFields`): The updated issue field.

### updateIssueFieldValue

Updates an existing issue field value for an issue.

**Input fields:**

- **input** (`UpdateIssueFieldValueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue object.
- **issueFieldValue** (`IssueFieldValue`): The updated issue field value.

### updateIssueIssueType

Updates the issue type on an issue.

**Input fields:**

- **input** (`UpdateIssueIssueTypeInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The updated issue.

### updateIssueType

Update an issue type.

**Input fields:**

- **input** (`UpdateIssueTypeInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueType** (`IssueType`): The updated issue type.

### updateLabel

Updates an existing label.

**Input fields:**

- **input** (`UpdateLabelInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **label** (`Label`): The updated label.

### updateProjectV2DraftIssue

Updates a draft issue within a Project.

**Input fields:**

- **input** (`UpdateProjectV2DraftIssueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **draftIssue** (`DraftIssue`): The draft issue updated in the project.

## Types

### ConvertedNoteToIssueEvent

Represents a`converted_note_to_issue`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the ConvertedNoteToIssueEvent object.
- **project** (`Project`): Project referenced by event.
- **projectCard** (`ProjectCard`): Project card referenced by this project event.
- **projectColumnName** (`String!`): Column name referenced by this project event.

### CreatedIssueContribution

Represents the contribution a user made on GitHub by opening an issue.

**Implements:** Contribution

**Fields:**

- **isRestricted** (`Boolean!`): Whether this contribution is associated with a record you do not have access to. For
example, your own 'first issue' contribution may have been made on a repository you can no
longer access.
- **issue** (`Issue!`): The issue that was opened.
- **occurredAt** (`DateTime!`): When this contribution was made.
- **resourcePath** (`URI!`): The HTTP path for this contribution.
- **url** (`URI!`): The HTTP URL for this contribution.
- **user** (`User!`): The user who made this contribution.

### DraftIssue

A draft issue within a project.

**Implements:** Node

**Fields:**

- **assignees** (`UserConnection!`): A list of users to assigned to this draft issue.
- **body** (`String!`): The body of the draft issue.
- **bodyHTML** (`HTML!`): The body of the draft issue rendered to HTML.
- **bodyText** (`String!`): The body of the draft issue rendered to text.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created this draft issue.
- **id** (`ID!`): The Node ID of the DraftIssue object.
- **projectV2Items** (`ProjectV2ItemConnection!`): List of items linked with the draft issue (currently draft issue can be linked to only one item).
- **projectsV2** (`ProjectV2Connection!`): Projects that link to this draft issue (currently draft issue can be linked to only one project).
- **title** (`String!`): The title of the draft issue.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### Issue

An Issue is a place to discuss ideas, enhancements, tasks, and bugs for a project.

**Implements:** Assignable, Closable, Comment, Deletable, Labelable, Lockable, Node, ProjectV2Owner, Reactable, RepositoryNode, Subscribable, SubscribableThread, UniformResourceLocatable, Updatable, UpdatableComment

**Fields:**

- **activeLockReason** (`LockReason`): Reason that the conversation was locked.
- **assignedActors** (`AssigneeConnection!`): A list of actors assigned to this object.
- **assignees** (`UserConnection!`): A list of Users assigned to this object.
- **author** (`Actor`): The actor who authored the comment.
- **authorAssociation** (`CommentAuthorAssociation!`): Author's association with the subject of the comment.
- **blockedBy** (`IssueConnection!`): A list of issues that are blocking this issue.
- **blocking** (`IssueConnection!`): A list of issues that this issue is blocking.
- **body** (`String!`): Identifies the body of the issue.
- **bodyHTML** (`HTML!`): The body rendered to HTML.
- **bodyResourcePath** (`URI!`): The http path for this issue body.
- **bodyText** (`String!`): Identifies the body of the issue rendered to text.
- **bodyUrl** (`URI!`): The http URL for this issue body.
- **closed** (`Boolean!`): Indicates if the object is closed (definition of closed may depend on type).
- **closedAt** (`DateTime`): Identifies the date and time when the object was closed.
- **closedByPullRequestsReferences** (`PullRequestConnection`): List of open pull requests referenced from this issue.
- **comments** (`IssueCommentConnection!`): A list of comments associated with the Issue.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **createdViaEmail** (`Boolean!`): Check if this comment was created via an email reply.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **duplicateOf** (`Issue`): A reference to the original issue that this issue has been marked as a duplicate of.
- **editor** (`Actor`): The actor who edited the comment.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **hovercard** (`Hovercard!`): The hovercard information for this issue.
- **id** (`ID!`): The Node ID of the Issue object.
- **includesCreatedEdit** (`Boolean!`): Check if this comment was edited and includes an edit with the creation data.
- **isPinned** (`Boolean`): Indicates whether or not this issue is currently pinned to the repository issues list.
- **isReadByViewer** (`Boolean`): Is this issue read by the viewer.
- **issueDependenciesSummary** (`IssueDependenciesSummary!`): Summary of the state of an issue's dependencies.
- **issueFieldValues** (`IssueFieldValueConnection`): Fields that are set on this issue.
- **issueType** (`IssueType`): The issue type for this Issue.
- **labels** (`LabelConnection`): A list of labels associated with the object.
- **lastEditedAt** (`DateTime`): The moment the editor made the last edit.
- **linkedBranches** (`LinkedBranchConnection!`): Branches linked to this issue.
- **locked** (`Boolean!`): `true` if the object is locked.
- **milestone** (`Milestone`): Identifies the milestone associated with the issue.
- **number** (`Int!`): Identifies the issue number.
- **parent** (`Issue`): The parent entity of the issue.
- **participants** (`UserConnection!`): A list of Users that are participating in the Issue conversation.
- **pinnedIssueComment** (`PinnedIssueComment`): The pinned comment for this issue.
- **projectCards** (`ProjectCardConnection!`): List of project cards associated with this issue.
- **projectItems** (`ProjectV2ItemConnection`): List of project items associated with this issue.
- **projectV2** (`ProjectV2`): Find a project by number.
- **projectsV2** (`ProjectV2Connection!`): A list of projects under the owner.
- **publishedAt** (`DateTime`): Identifies when the comment was published at.
- **reactionGroups** (`[ReactionGroup!]`): A list of reactions grouped by content left on the subject.
- **reactions** (`ReactionConnection!`): A list of Reactions left on the Issue.
- **repository** (`Repository!`): The repository associated with this node.
- **resourcePath** (`URI!`): The HTTP path for this issue.
- **state** (`IssueState!`): Identifies the state of the issue.
- **stateReason** (`IssueStateReason`): Identifies the reason for the issue state.
- **subIssues** (`IssueConnection!`): A list of sub-issues associated with the Issue.
- **subIssuesSummary** (`SubIssuesSummary!`): Summary of the state of an issue's sub-issues.
- **suggestedActors** (`AssigneeConnection!`): A list of suggested actors to assign to this object.
- **timeline** (`IssueTimelineConnection!`): A list of events, comments, commits, etc. associated with the issue.
- **timelineItems** (`IssueTimelineItemsConnection!`): A list of events, comments, commits, etc. associated with the issue.
- **title** (`String!`): Identifies the issue title.
- **titleHTML** (`String!`): Identifies the issue title rendered to HTML.
- **trackedInIssues** (`IssueConnection!`): A list of issues that track this issue.
- **trackedIssues** (`IssueConnection!`): A list of issues tracked inside the current issue.
- **trackedIssuesCount** (`Int!`): The number of tracked issues for this issue.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this issue.
- **userContentEdits** (`UserContentEditConnection`): A list of edits to this content.
- **viewerCanClose** (`Boolean!`): Indicates if the object can be closed by the viewer.
- **viewerCanDelete** (`Boolean!`): Check if the current viewer can delete this object.
- **viewerCanLabel** (`Boolean!`): Indicates if the viewer can edit labels for this object.
- **viewerCanReact** (`Boolean!`): Can user react to this subject.
- **viewerCanReopen** (`Boolean!`): Indicates if the object can be reopened by the viewer.
- **viewerCanSetFields** (`Boolean`): Check if the current viewer can set fields on the issue.
- **viewerCanSubscribe** (`Boolean!`): Check if the viewer is able to change their subscription status for the repository.
- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.
- **viewerCannotUpdateReasons** (`[CommentCannotUpdateReason!]!`): Reasons why the current viewer can not update this comment.
- **viewerDidAuthor** (`Boolean!`): Did the viewer author this comment.
- **viewerSubscription** (`SubscriptionState`): Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.
- **viewerThreadSubscriptionFormAction** (`ThreadSubscriptionFormAction`): Identifies the viewer's thread subscription form action.
- **viewerThreadSubscriptionStatus** (`ThreadSubscriptionState`): Identifies the viewer's thread subscription status.

### IssueComment

Represents a comment on an Issue.

**Implements:** Comment, Deletable, Minimizable, Node, Pinnable, Reactable, RepositoryNode, Updatable, UpdatableComment

**Fields:**

- **author** (`Actor`): The actor who authored the comment.
- **authorAssociation** (`CommentAuthorAssociation!`): Author's association with the subject of the comment.
- **body** (`String!`): The body as Markdown.
- **bodyHTML** (`HTML!`): The body rendered to HTML.
- **bodyText** (`String!`): The body rendered to text.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **createdViaEmail** (`Boolean!`): Check if this comment was created via an email reply.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **editor** (`Actor`): The actor who edited the comment.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **id** (`ID!`): The Node ID of the IssueComment object.
- **includesCreatedEdit** (`Boolean!`): Check if this comment was edited and includes an edit with the creation data.
- **isMinimized** (`Boolean!`): Returns whether or not a comment has been minimized.
- **isPinned** (`Boolean`): Indicates whether or not this entity is currently pinned.
- **issue** (`Issue!`): Identifies the issue associated with the comment.
- **lastEditedAt** (`DateTime`): The moment the editor made the last edit.
- **minimizedReason** (`String`): Returns why the comment was minimized. One of `abuse`, `off-topic`,
`outdated`, `resolved`, `duplicate`, `spam`, and `low-quality`. Note that the
case and formatting of these values differs from the inputs to the
`MinimizeComment` mutation.
- **pinnedAt** (`DateTime`): Identifies the date and time when this entity was pinned.
- **pinnedBy** (`User`): The user who pinned this entity.
- **publishedAt** (`DateTime`): Identifies when the comment was published at.
- **pullRequest** (`PullRequest`): Returns the pull request associated with the comment, if this comment was made on a
pull request.
- **reactionGroups** (`[ReactionGroup!]`): A list of reactions grouped by content left on the subject.
- **reactions** (`ReactionConnection!`): A list of Reactions left on the Issue.
- **repository** (`Repository!`): The repository associated with this node.
- **resourcePath** (`URI!`): The HTTP path for this issue comment.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this issue comment.
- **userContentEdits** (`UserContentEditConnection`): A list of edits to this content.
- **viewerCanDelete** (`Boolean!`): Check if the current viewer can delete this object.
- **viewerCanMinimize** (`Boolean!`): Check if the current viewer can minimize this object.
- **viewerCanPin** (`Boolean!`): Check if the current viewer can pin this entity.
- **viewerCanReact** (`Boolean!`): Can user react to this subject.
- **viewerCanUnminimize** (`Boolean!`): Check if the current viewer can unminimize this object.
- **viewerCanUnpin** (`Boolean!`): Check if the current viewer can unpin this entity.
- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.
- **viewerCannotUpdateReasons** (`[CommentCannotUpdateReason!]!`): Reasons why the current viewer can not update this comment.
- **viewerDidAuthor** (`Boolean!`): Did the viewer author this comment.

### IssueCommentPinnedEvent

Represents a`issue_comment_pinned`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IssueCommentPinnedEvent object.
- **issueComment** (`IssueComment`): Identifies the issue comment associated with the`issue_comment_pinned`event.

### IssueCommentUnpinnedEvent

Represents a`issue_comment_unpinned`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IssueCommentUnpinnedEvent object.
- **issueComment** (`IssueComment`): Identifies the issue comment associated with the`issue_comment_unpinned`event.

### IssueDependenciesSummary

Summary of the state of an issue's dependencies.

**Fields:**

- **blockedBy** (`Int!`): Count of issues this issue is blocked by.
- **blocking** (`Int!`): Count of issues this issue is blocking.
- **totalBlockedBy** (`Int!`): Total count of issues this issue is blocked by (open and closed).
- **totalBlocking** (`Int!`): Total count of issues this issue is blocking (open and closed).

### IssueFieldAddedEvent

Represents a`issue_field_added`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **color** (`String`): The color if it is a single-select field.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IssueFieldAddedEvent object.
- **issueField** (`IssueFields`): The issue field added.
- **value** (`String`): The value of the added field.

### IssueFieldChangedEvent

Represents a`issue_field_changed`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IssueFieldChangedEvent object.
- **issueField** (`IssueFields`): The issue field changed.
- **newColor** (`String`): The new color if it is a single-select field.
- **newValue** (`String`): The new value of the field.
- **previousColor** (`String`): The previous color if it was a single-select field.
- **previousValue** (`String`): The previous value of the field.

### IssueFieldDate

Represents a date issue field.

**Implements:** IssueFieldCommon, Node

**Fields:**

- **createdAt** (`DateTime!`): The issue field's creation timestamp.
- **dataType** (`IssueFieldDataType!`): The issue field's data type.
- **description** (`String`): The issue field's description.
- **id** (`ID!`): The Node ID of the IssueFieldDate object.
- **name** (`String!`): The issue field's name.
- **visibility** (`IssueFieldVisibility!`): The issue field's visibility.

### IssueFieldDateValue

The value of a date field in an Issue item.

**Implements:** IssueFieldValueCommon, Node

**Fields:**

- **field** (`IssueFields`): The issue field that contains this value.
- **id** (`ID!`): The Node ID of the IssueFieldDateValue object.
- **value** (`String!`): Value of the field.

### IssueFieldNumber

Represents a number issue field.

**Implements:** IssueFieldCommon, Node

**Fields:**

- **createdAt** (`DateTime!`): The issue field's creation timestamp.
- **dataType** (`IssueFieldDataType!`): The issue field's data type.
- **description** (`String`): The issue field's description.
- **id** (`ID!`): The Node ID of the IssueFieldNumber object.
- **name** (`String!`): The issue field's name.
- **visibility** (`IssueFieldVisibility!`): The issue field's visibility.

### IssueFieldNumberValue

The value of a number field in an Issue item.

**Implements:** IssueFieldValueCommon, Node

**Fields:**

- **field** (`IssueFields`): The issue field that contains this value.
- **id** (`ID!`): The Node ID of the IssueFieldNumberValue object.
- **value** (`Float!`): Value of the field.

### IssueFieldRemovedEvent

Represents a`issue_field_removed`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IssueFieldRemovedEvent object.
- **issueField** (`IssueFields`): The issue field removed.

### IssueFieldSingleSelect

Represents a single select issue field.

**Implements:** IssueFieldCommon, Node

**Fields:**

- **createdAt** (`DateTime!`): The issue field's creation timestamp.
- **dataType** (`IssueFieldDataType!`): The issue field's data type.
- **description** (`String`): The issue field's description.
- **id** (`ID!`): The Node ID of the IssueFieldSingleSelect object.
- **name** (`String!`): The issue field's name.
- **options** (`[IssueFieldSingleSelectOption!]!`): Options for the single select field.
- **visibility** (`IssueFieldVisibility!`): The issue field's visibility.

### IssueFieldSingleSelectOption

Represents an option in a single-select issue field.

**Implements:** Node

**Fields:**

- **color** (`IssueFieldSingleSelectOptionColor!`): The option's display color.
- **description** (`String`): The option's plain-text description.
- **id** (`ID!`): The Node ID of the IssueFieldSingleSelectOption object.
- **name** (`String!`): The option's name.
- **priority** (`Int`): The option's priority order.

### IssueFieldSingleSelectValue

The value of a single select field in an Issue item.

**Implements:** IssueFieldValueCommon, Node

**Fields:**

- **color** (`IssueFieldSingleSelectOptionColor!`): The option's display color.
- **description** (`String`): The option's plain-text description.
- **field** (`IssueFields`): The issue field that contains this value.
- **id** (`ID!`): The Node ID of the IssueFieldSingleSelectValue object.
- **name** (`String!`): The option's name.
- **optionId** (`String`): The selected option's global relay ID.
- **value** (`String!`): The option's name text (alias for `name`, for consistency with other field value types).

### IssueFieldText

Represents a text issue field.

**Implements:** IssueFieldCommon, Node

**Fields:**

- **createdAt** (`DateTime!`): The issue field's creation timestamp.
- **dataType** (`IssueFieldDataType!`): The issue field's data type.
- **description** (`String`): The issue field's description.
- **id** (`ID!`): The Node ID of the IssueFieldText object.
- **name** (`String!`): The issue field's name.
- **visibility** (`IssueFieldVisibility!`): The issue field's visibility.

### IssueFieldTextValue

The value of a text field in an Issue item.

**Implements:** IssueFieldValueCommon, Node

**Fields:**

- **field** (`IssueFields`): The issue field that contains this value.
- **id** (`ID!`): The Node ID of the IssueFieldTextValue object.
- **value** (`String!`): Value of the field.

### IssueTemplate

A repository issue template.

**Fields:**

- **about** (`String`): The template purpose.
- **assignees** (`UserConnection!`): The suggested assignees.
- **body** (`String`): The suggested issue body.
- **filename** (`String!`): The template filename.
- **labels** (`LabelConnection`): The suggested issue labels.
- **name** (`String!`): The template name.
- **title** (`String`): The suggested issue title.
- **type** (`IssueType`): The suggested issue type.

### IssueType

Represents the type of Issue.

**Implements:** Node

**Fields:**

- **color** (`IssueTypeColor!`): The issue type's color.
- **description** (`String`): The issue type's description.
- **id** (`ID!`): The Node ID of the IssueType object.
- **isEnabled** (`Boolean!`): The issue type's enabled state.
- **isPrivate** (`Boolean!`): Whether the issue type is publicly visible.
- **issues** (`IssueConnection!`): The issues with this issue type in the given repository.
- **name** (`String!`): The issue type's name.
- **pinnedFields** (`[IssueFields!]`): An ordered list of issue fields pinned to this type.

### IssueTypeAddedEvent

Represents a`issue_type_added`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IssueTypeAddedEvent object.
- **issueType** (`IssueType`): The issue type added.

### IssueTypeChangedEvent

Represents a`issue_type_changed`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IssueTypeChangedEvent object.
- **issueType** (`IssueType`): The issue type added.
- **prevIssueType** (`IssueType`): The issue type removed.

### IssueTypeRemovedEvent

Represents a`issue_type_removed`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IssueTypeRemovedEvent object.
- **issueType** (`IssueType`): The issue type removed.

### Label

A label for categorizing Issues, Pull Requests, Milestones, or Discussions with a given Repository.

**Implements:** Node

**Fields:**

- **color** (`String!`): Identifies the label color.
- **createdAt** (`DateTime`): Identifies the date and time when the label was created.
- **description** (`String`): A brief description of this label.
- **id** (`ID!`): The Node ID of the Label object.
- **isDefault** (`Boolean!`): Indicates whether or not this is a default label.
- **issues** (`IssueConnection!`): A list of issues associated with this label.
- **name** (`String!`): Identifies the label name.
- **pullRequests** (`PullRequestConnection!`): A list of pull requests associated with this label.
- **repository** (`Repository!`): The repository associated with this label.
- **resourcePath** (`URI!`): The HTTP path for this label.
- **updatedAt** (`DateTime`): Identifies the date and time when the label was last updated.
- **url** (`URI!`): The HTTP URL for this label.

### LabeledEvent

Represents a`labeled`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the LabeledEvent object.
- **label** (`Label!`): Identifies the label associated with the`labeled`event.
- **labelable** (`Labelable!`): Identifies the `Labelable` associated with the event.

### Milestone

Represents a Milestone object on a given repository.

**Implements:** Closable, Node, UniformResourceLocatable

**Fields:**

- **closed** (`Boolean!`): Indicates if the object is closed (definition of closed may depend on type).
- **closedAt** (`DateTime`): Identifies the date and time when the object was closed.
- **closedIssueCount** (`Int!`): Identifies the number of closed issues associated with the milestone.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): Identifies the actor who created the milestone.
- **description** (`String`): Identifies the description of the milestone.
- **descriptionHTML** (`String`): The HTML rendered description of the milestone using GitHub Flavored Markdown.
- **dueOn** (`DateTime`): Identifies the due date of the milestone.
- **id** (`ID!`): The Node ID of the Milestone object.
- **issues** (`IssueConnection!`): A list of issues associated with the milestone.
- **number** (`Int!`): Identifies the number of the milestone.
- **openIssueCount** (`Int!`): Identifies the number of open issues associated with the milestone.
- **progressPercentage** (`Float!`): Identifies the percentage complete for the milestone.
- **pullRequests** (`PullRequestConnection!`): A list of pull requests associated with the milestone.
- **repository** (`Repository!`): The repository associated with this milestone.
- **resourcePath** (`URI!`): The HTTP path for this milestone.
- **state** (`MilestoneState!`): Identifies the state of the milestone.
- **title** (`String!`): Identifies the title of the milestone.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this milestone.
- **viewerCanClose** (`Boolean!`): Indicates if the object can be closed by the viewer.
- **viewerCanReopen** (`Boolean!`): Indicates if the object can be reopened by the viewer.

### MilestonedEvent

Represents a`milestoned`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the MilestonedEvent object.
- **milestoneTitle** (`String!`): Identifies the milestone title associated with the`milestoned`event.
- **subject** (`MilestoneItem!`): Object referenced by event.

### ParentIssueAddedEvent

Represents a`parent_issue_added`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the ParentIssueAddedEvent object.
- **parent** (`Issue`): The parent issue added.

### ParentIssueRemovedEvent

Represents a`parent_issue_removed`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the ParentIssueRemovedEvent object.
- **parent** (`Issue`): The parent issue removed.

### PinnedIssue

A Pinned Issue is a issue pinned to a repository's index page.

**Implements:** Node

**Fields:**

- **databaseId** (`Int`): Identifies the primary key from the database.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **id** (`ID!`): The Node ID of the PinnedIssue object.
- **issue** (`Issue!`): The issue that was pinned.
- **pinnedBy** (`Actor!`): The actor that pinned this issue.
- **repository** (`Repository!`): The repository that this issue was pinned to.

### PinnedIssueComment

A comment pinned to an Issue.

**Implements:** Node

**Fields:**

- **databaseId** (`Int`): Identifies the primary key from the database.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **id** (`ID!`): The Node ID of the PinnedIssueComment object.
- **issue** (`Issue!`): The issue that this comment belongs to.
- **issueComment** (`IssueComment!`): The comment that was pinned.
- **pinnedAt** (`DateTime!`): Identifies when the comment was pinned.
- **pinnedBy** (`Actor!`): The actor that pinned this comment.

### ProjectV2ItemFieldLabelValue

The value of the labels field in a Project item.

**Fields:**

- **field** (`ProjectV2FieldConfiguration!`): The field that contains this value.
- **labels** (`LabelConnection`): Labels value of a field.

### ProjectV2ItemFieldMilestoneValue

The value of a milestone field in a Project item.

**Fields:**

- **field** (`ProjectV2FieldConfiguration!`): The field that contains this value.
- **milestone** (`Milestone`): Milestone value of a field.

### ProjectV2ItemIssueFieldValue

The value of an issue field in a Project item.

**Fields:**

- **field** (`ProjectV2FieldConfiguration!`): Field that contains this value.
- **issueFieldValue** (`ProjectV2IssueFieldValues`): Value of the Issue Field.

### SubIssueAddedEvent

Represents a`sub_issue_added`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the SubIssueAddedEvent object.
- **subIssue** (`Issue`): The sub-issue added.

### SubIssueRemovedEvent

Represents a`sub_issue_removed`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the SubIssueRemovedEvent object.
- **subIssue** (`Issue`): The sub-issue removed.

### SubIssuesSummary

Summary of the state of an issue's sub-issues.

**Fields:**

- **completed** (`Int!`): Count of completed sub-issues.
- **percentCompleted** (`Int!`): Percent of sub-issues which are completed.
- **total** (`Int!`): Count of total number of sub-issues.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **CreatedIssueContributionConnection** (4 fields): The connection type for CreatedIssueContribution.
- **CreatedIssueContributionEdge** (2 fields): An edge in a connection.
- **IssueCommentConnection** (4 fields): The connection type for IssueComment.
- **IssueCommentEdge** (2 fields): An edge in a connection.
- **IssueConnection** (4 fields): The connection type for Issue.
- **IssueEdge** (2 fields): An edge in a connection.
- **IssueFieldValueConnection** (4 fields): The connection type for IssueFieldValue.
- **IssueFieldValueEdge** (2 fields): An edge in a connection.
- **IssueFieldsConnection** (4 fields): The connection type for IssueFields.
- **IssueFieldsEdge** (2 fields): An edge in a connection.
- **IssueTimelineConnection** (4 fields): The connection type for IssueTimelineItem.
- **IssueTimelineItemEdge** (2 fields): An edge in a connection.
- **IssueTimelineItemsConnection** (7 fields): The connection type for IssueTimelineItems.
- **IssueTimelineItemsEdge** (2 fields): An edge in a connection.
- **IssueTypeConnection** (4 fields): The connection type for IssueType.
- **IssueTypeEdge** (2 fields): An edge in a connection.
- **LabelConnection** (4 fields): The connection type for Label.
- **LabelEdge** (2 fields): An edge in a connection.
- **MilestoneConnection** (4 fields): The connection type for Milestone.
- **MilestoneEdge** (2 fields): An edge in a connection.
- **PinnedIssueConnection** (4 fields): The connection type for PinnedIssue.
- **PinnedIssueEdge** (2 fields): An edge in a connection.

## Interfaces

### IssueFieldCommon

Common fields across different issue field types.

**Fields:**

- **createdAt** (`DateTime!`): The issue field's creation timestamp.
- **dataType** (`IssueFieldDataType!`): The issue field's data type.
- **description** (`String`): The issue field's description.
- **name** (`String!`): The issue field's name.
- **visibility** (`IssueFieldVisibility!`): The issue field's visibility.

### IssueFieldValueCommon

Common fields across different issue field value types.

**Fields:**

- **field** (`IssueFields`): The issue field that contains this value.

### Labelable

An object that can have labels assigned to it.

**Fields:**

- **labels** (`LabelConnection`): A list of labels associated with the object.
- **viewerCanLabel** (`Boolean!`): Indicates if the viewer can edit labels for this object.

## Enums

### IssueClosedStateReason

The possible state reasons of a closed issue.

**Values:**

- `COMPLETED`: An issue that has been closed as completed.
- `DUPLICATE`: An issue that has been closed as a duplicate.
- `NOT_PLANNED`: An issue that has been closed as not planned.

### IssueCommentOrderField

Properties by which issue comment connections can be ordered.

**Values:**

- `UPDATED_AT`: Order issue comments by update time.

### IssueDependencyOrderField

Properties by which issue dependencies can be ordered.

**Values:**

- `CREATED_AT`: Order issue dependencies by the creation time of the dependent issue.
- `DEPENDENCY_ADDED_AT`: Order issue dependencies by time of when the dependency relationship was added.

### IssueFieldDataType

The type of an issue field.

**Values:**

- `DATE`: Date.
- `NUMBER`: Number.
- `SINGLE_SELECT`: Single Select.
- `TEXT`: Text.

### IssueFieldOrderField

Properties by which issue field connections can be ordered.

**Values:**

- `CREATED_AT`: Order issue fields by creation time.
- `NAME`: Order issue fields by name.

### IssueFieldSingleSelectOptionColor

The display color of a single-select field option.

**Values:**

- `BLUE`: blue.
- `GRAY`: gray.
- `GREEN`: green.
- `ORANGE`: orange.
- `PINK`: pink.
- `PURPLE`: purple.
- `RED`: red.
- `YELLOW`: yellow.

### IssueFieldVisibility

The visibility of an issue field.

**Values:**

- `ALL`: All.
- `ORG_ONLY`: Org Only.

### IssueOrderField

Properties by which issue connections can be ordered.

**Values:**

- `COMMENTS`: Order issues by comment count.
- `CREATED_AT`: Order issues by creation time.
- `UPDATED_AT`: Order issues by update time.

### IssueSearchType

Type of issue search performed.

**Values:**

- `HYBRID`: Hybrid search combining lexical and semantic approaches.
- `LEXICAL`: Lexical (keyword-based) search.
- `SEMANTIC`: Semantic (meaning-based) search using embeddings.

### IssueState

The possible states of an issue.

**Values:**

- `CLOSED`: An issue that has been closed.
- `OPEN`: An issue that is still open.

### IssueStateReason

The possible state reasons of an issue.

**Values:**

- `COMPLETED`: An issue that has been closed as completed.
- `DUPLICATE`: An issue that has been closed as a duplicate.
- `NOT_PLANNED`: An issue that has been closed as not planned.
- `REOPENED`: An issue that has been reopened.

### IssueTimelineItemsItemType

The possible item types found in a timeline.

**Values:**

- `ADDED_TO_PROJECT_EVENT`: Represents a`added_to_project`event on a given issue or pull request.
- `ADDED_TO_PROJECT_V2_EVENT`: Represents a`added_to_project_v2`event on a given issue or pull request.
- `ASSIGNED_EVENT`: Represents an`assigned`event on any assignable object.
- `BLOCKED_BY_ADDED_EVENT`: Represents a`blocked_by_added`event on a given issue.
- `BLOCKED_BY_REMOVED_EVENT`: Represents a`blocked_by_removed`event on a given issue.
- `BLOCKING_ADDED_EVENT`: Represents a`blocking_added`event on a given issue.
- `BLOCKING_REMOVED_EVENT`: Represents a`blocking_removed`event on a given issue.
- `CLOSED_EVENT`: Represents a`closed`event on any `Closable`.
- `COMMENT_DELETED_EVENT`: Represents a`comment_deleted`event on a given issue or pull request.
- `CONNECTED_EVENT`: Represents a`connected`event on a given issue or pull request.
- `CONVERTED_FROM_DRAFT_EVENT`: Represents a`converted_from_draft`event on a given issue or pull request.
- `CONVERTED_NOTE_TO_ISSUE_EVENT`: Represents a`converted_note_to_issue`event on a given issue or pull request.
- `CONVERTED_TO_DISCUSSION_EVENT`: Represents a`converted_to_discussion`event on a given issue.
- `CROSS_REFERENCED_EVENT`: Represents a mention made by one issue or pull request to another.
- `DEMILESTONED_EVENT`: Represents a`demilestoned`event on a given issue or pull request.
- `DISCONNECTED_EVENT`: Represents a`disconnected`event on a given issue or pull request.
- `ISSUE_COMMENT`: Represents a comment on an Issue.
- `ISSUE_COMMENT_PINNED_EVENT`: Represents a`issue_comment_pinned`event on a given issue.
- `ISSUE_COMMENT_UNPINNED_EVENT`: Represents a`issue_comment_unpinned`event on a given issue.
- `ISSUE_FIELD_ADDED_EVENT`: Represents a`issue_field_added`event on a given issue.
- `ISSUE_FIELD_CHANGED_EVENT`: Represents a`issue_field_changed`event on a given issue.
- `ISSUE_FIELD_REMOVED_EVENT`: Represents a`issue_field_removed`event on a given issue.
- `ISSUE_TYPE_ADDED_EVENT`: Represents a`issue_type_added`event on a given issue.
- `ISSUE_TYPE_CHANGED_EVENT`: Represents a`issue_type_changed`event on a given issue.
- `ISSUE_TYPE_REMOVED_EVENT`: Represents a`issue_type_removed`event on a given issue.
- `LABELED_EVENT`: Represents a`labeled`event on a given issue or pull request.
- `LOCKED_EVENT`: Represents a`locked`event on a given issue or pull request.
- `MARKED_AS_DUPLICATE_EVENT`: Represents a`marked_as_duplicate`event on a given issue or pull request.
- `MENTIONED_EVENT`: Represents a`mentioned`event on a given issue or pull request.
- `MILESTONED_EVENT`: Represents a`milestoned`event on a given issue or pull request.
- `MOVED_COLUMNS_IN_PROJECT_EVENT`: Represents a`moved_columns_in_project`event on a given issue or pull request.
- `PARENT_ISSUE_ADDED_EVENT`: Represents a`parent_issue_added`event on a given issue.
- `PARENT_ISSUE_REMOVED_EVENT`: Represents a`parent_issue_removed`event on a given issue.
- `PINNED_EVENT`: Represents a`pinned`event on a given issue or pull request.
- `PROJECT_V2_ITEM_STATUS_CHANGED_EVENT`: Represents a`project_v2_item_status_changed`event on a given issue or pull request.
- `REFERENCED_EVENT`: Represents a`referenced`event on a given `ReferencedSubject`.
- `REMOVED_FROM_PROJECT_EVENT`: Represents a`removed_from_project`event on a given issue or pull request.
- `REMOVED_FROM_PROJECT_V2_EVENT`: Represents a`removed_from_project_v2`event on a given issue or pull request.
- `RENAMED_TITLE_EVENT`: Represents a`renamed`event on a given issue or pull request.
- `REOPENED_EVENT`: Represents a`reopened`event on any `Closable`.
- `SUBSCRIBED_EVENT`: Represents a`subscribed`event on a given `Subscribable`.
- `SUB_ISSUE_ADDED_EVENT`: Represents a`sub_issue_added`event on a given issue.
- `SUB_ISSUE_REMOVED_EVENT`: Represents a`sub_issue_removed`event on a given issue.
- `TRANSFERRED_EVENT`: Represents a`transferred`event on a given issue or pull request.
- `UNASSIGNED_EVENT`: Represents an`unassigned`event on any assignable object.
- `UNLABELED_EVENT`: Represents an`unlabeled`event on a given issue or pull request.
- `UNLOCKED_EVENT`: Represents an`unlocked`event on a given issue or pull request.
- `UNMARKED_AS_DUPLICATE_EVENT`: Represents an`unmarked_as_duplicate`event on a given issue or pull request.
- `UNPINNED_EVENT`: Represents an`unpinned`event on a given issue or pull request.
- `UNSUBSCRIBED_EVENT`: Represents an`unsubscribed`event on a given `Subscribable`.
- `USER_BLOCKED_EVENT`: Represents a`user_blocked`event on a given user.

### IssueTypeColor

The possible color for an issue type.

**Values:**

- `BLUE`: blue.
- `GRAY`: gray.
- `GREEN`: green.
- `ORANGE`: orange.
- `PINK`: pink.
- `PURPLE`: purple.
- `RED`: red.
- `YELLOW`: yellow.

### IssueTypeOrderField

Properties by which issue type connections can be ordered.

**Values:**

- `CREATED_AT`: Order issue types by creation time.
- `NAME`: Order issue types by name.

### LabelOrderField

Properties by which label connections can be ordered.

**Values:**

- `CREATED_AT`: Order labels by creation time.
- `ISSUE_COUNT`: Order labels by issue count.
- `NAME`: Order labels by name.

### MilestoneOrderField

Properties by which milestone connections can be ordered.

**Values:**

- `CREATED_AT`: Order milestones by when they were created.
- `DUE_DATE`: Order milestones by when they are due.
- `NUMBER`: Order milestones by their number.
- `UPDATED_AT`: Order milestones by when they were last updated.

### MilestoneState

The possible states of a milestone.

**Values:**

- `CLOSED`: A milestone that has been closed.
- `OPEN`: A milestone that is still open.

### TrackedIssueStates

The possible states of a tracked issue.

**Values:**

- `CLOSED`: The tracked issue is closed.
- `OPEN`: The tracked issue is open.

## Input Objects

### AddLabelsToLabelableInput

Autogenerated input type of AddLabelsToLabelable.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **labelIds** (`[ID!]!`): The ids of the labels to add.
- **labelableId** (`ID!`): The id of the labelable object to add labels to.

### AddProjectV2DraftIssueInput

Autogenerated input type of AddProjectV2DraftIssue.

**Input fields:**

- **assigneeIds** (`[ID!]`): The IDs of the assignees of the draft issue.
- **body** (`String`): The body of the draft issue.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the Project to add the draft issue to.
- **title** (`String!`): The title of the draft issue. A project item can also be created by providing
the URL of an Issue or Pull Request if you have access.

### AddSubIssueInput

Autogenerated input type of AddSubIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The id of the issue.
- **replaceParent** (`Boolean`): Option to replace parent issue if one already exists.
- **subIssueId** (`ID`): The id of the sub-issue.
- **subIssueUrl** (`String`): The url of the sub-issue.

### ClearLabelsFromLabelableInput

Autogenerated input type of ClearLabelsFromLabelable.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **labelableId** (`ID!`): The id of the labelable object to clear the labels from.

### CloseIssueInput

Autogenerated input type of CloseIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **duplicateIssueId** (`ID`): ID of the issue that this is a duplicate of.
- **issueId** (`ID!`): ID of the issue to be closed.
- **stateReason** (`IssueClosedStateReason`): The reason the issue is to be closed.

### ConvertProjectCardNoteToIssueInput

Autogenerated input type of ConvertProjectCardNoteToIssue.

**Input fields:**

- **body** (`String`): The body of the newly created issue.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectCardId** (`ID!`): The ProjectCard ID to convert.
- **repositoryId** (`ID!`): The ID of the repository to create the issue in.
- **title** (`String`): The title of the newly created issue. Defaults to the card's note text.

### ConvertProjectV2DraftIssueItemToIssueInput

Autogenerated input type of ConvertProjectV2DraftIssueItemToIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **itemId** (`ID!`): The ID of the draft issue ProjectV2Item to convert.
- **repositoryId** (`ID!`): The ID of the repository to create the issue in.

### CreateIssueFieldInput

Autogenerated input type of CreateIssueField.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **dataType** (`IssueFieldDataType!`): The data type of the issue field.
- **description** (`String`): A description of the issue field.
- **name** (`String!`): The name of the issue field.
- **options** (`[IssueFieldSingleSelectOptionInput!]`): The options for the issue field if applicable.
- **ownerId** (`ID!`): The ID of the organization where the issue field will be created.
- **visibility** (`IssueFieldVisibility`): The visibility of the issue field.

### CreateIssueFieldValueInput

Autogenerated input type of CreateIssueFieldValue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueField** (`IssueFieldCreateOrUpdateInput!`): The field value to create.
- **issueId** (`ID!`): The ID of the issue.

### CreateIssueInput

Autogenerated input type of CreateIssue.

**Input fields:**

- **agentAssignment** (`AgentAssignmentInput`): Configuration for assigning Copilot to this issue.
- **assigneeIds** (`[ID!]`): The Node ID of assignees for this issue.
- **body** (`String`): The body for the issue description.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueFields** (`[IssueFieldCreateOrUpdateInput!]`): An array of issue fields to set on the issue during creation.
- **issueTemplate** (`String`): The name of an issue template in the repository, assigns labels and assignees from the template to the issue.
- **issueTypeId** (`ID`): The Node ID of the issue type for this issue.
- **labelIds** (`[ID!]`): An array of Node IDs of labels for this issue.
- **milestoneId** (`ID`): The Node ID of the milestone for this issue.
- **parentIssueId** (`ID`): The Node ID of the parent issue to add this new issue to.
- **projectIds** (`[ID!]`): An array of Node IDs for projects associated with this issue.
- **projectV2Ids** (`[ID!]`): An array of Node IDs for Projects V2 associated with this issue.
- **repositoryId** (`ID!`): The Node ID of the repository.
- **title** (`String!`): The title for the issue.

### CreateIssueTypeInput

Autogenerated input type of CreateIssueType.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **color** (`IssueTypeColor`): Color for the issue type.
- **description** (`String`): Description of the new issue type.
- **isEnabled** (`Boolean!`): Whether or not the issue type is enabled on the org level.
- **name** (`String!`): Name of the new issue type.
- **ownerId** (`ID!`): The ID for the organization on which the issue type is created.

### CreateLabelInput

Autogenerated input type of CreateLabel.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **color** (`String!`): A 6 character hex code, without the leading #, identifying the color of the label.
- **description** (`String`): A brief description of the label, such as its purpose.
- **name** (`String!`): The name of the label.
- **repositoryId** (`ID!`): The Node ID of the repository.

### CreateProjectV2IssueFieldInput

Autogenerated input type of CreateProjectV2IssueField.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueFieldId** (`ID!`): The ID of the IssueField to create the field for.
- **projectId** (`ID!`): The ID of the Project to create the field in.

### DeleteIssueCommentInput

Autogenerated input type of DeleteIssueComment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The ID of the comment to delete.

### DeleteIssueFieldInput

Autogenerated input type of DeleteIssueField.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **fieldId** (`ID!`): The ID of the field to delete.

### DeleteIssueFieldValueInput

Autogenerated input type of DeleteIssueFieldValue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **fieldId** (`ID!`): The ID of the field to delete.
- **issueId** (`ID!`): The ID of the issue.

### DeleteIssueInput

Autogenerated input type of DeleteIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The ID of the issue to delete.

### DeleteIssueTypeInput

Autogenerated input type of DeleteIssueType.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueTypeId** (`ID!`): The ID of the issue type to delete.

### DeleteLabelInput

Autogenerated input type of DeleteLabel.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The Node ID of the label to be deleted.

### IssueCommentOrder

Ways in which lists of issue comments can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order issue comments by the specified field.
- **field** (`IssueCommentOrderField!`): The field in which to order issue comments by.

### IssueDependencyOrder

Ordering options issue dependencies.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`IssueDependencyOrderField!`): The field to order issue dependencies by.

### IssueFieldCreateOrUpdateInput

Represents an issue field value that must be set on an issue during issue creation.

**Input fields:**

- **dateValue** (`String`): The date value, for a date field.
- **delete** (`Boolean`): Set to true to delete the field value.
- **fieldId** (`ID!`): The ID of the issue field.
- **numberValue** (`Float`): The numeric value, for a number field.
- **singleSelectOptionId** (`ID`): The ID of the selected option, for a single select field.
- **textValue** (`String`): The text value, for a text field.

### IssueFieldOrder

Ordering options for issue field connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`IssueFieldOrderField!`): The field to order issue fields by.

### IssueFieldSingleSelectOptionInput

A single selection option for an issue field.

**Input fields:**

- **color** (`IssueFieldSingleSelectOptionColor!`): The color associated with the option.
- **description** (`String`): A description of the option.
- **name** (`String!`): The name of the option.
- **priority** (`Int!`): The priority of the option in the list.

### IssueFilters

Ways in which to filter lists of issues.

**Input fields:**

- **assignee** (`String`): List issues assigned to given name. Pass in `null` for issues with no assigned
user, and `*` for issues assigned to any user.
- **createdBy** (`String`): List issues created by given name.
- **labels** (`[String!]`): List issues where the list of label names exist on the issue.
- **mentioned** (`String`): List issues where the given name is mentioned in the issue.
- **milestone** (`String`): List issues by given milestone argument. If an string representation of an
integer is passed, it should refer to a milestone by its database ID. Pass in
`null` for issues with no milestone, and `*` for issues that are assigned to any milestone.
- **milestoneNumber** (`String`): List issues by given milestone argument. If an string representation of an
integer is passed, it should refer to a milestone by its number field. Pass in
`null` for issues with no milestone, and `*` for issues that are assigned to any milestone.
- **since** (`DateTime`): List issues that have been updated at or after the given date.
- **states** (`[IssueState!]`): List issues filtered by the list of states given.
- **type** (`String`): List issues filtered by the type given, only supported by searches on repositories.
- **viewerSubscribed** (`Boolean`): List issues subscribed to by viewer.

### IssueOrder

Ways in which lists of issues can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order issues by the specified field.
- **field** (`IssueOrderField!`): The field in which to order issues by.

### IssueTypeOrder

Ordering options for issue types connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`IssueTypeOrderField!`): The field to order issue types by.

### LabelOrder

Ways in which lists of labels can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order labels by the specified field.
- **field** (`LabelOrderField!`): The field in which to order labels by.

### MilestoneOrder

Ordering options for milestone connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`MilestoneOrderField!`): The field to order milestones by.

### PinIssueCommentInput

Autogenerated input type of PinIssueComment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueCommentId** (`ID!`): The ID of the Issue Comment to pin. Comment pinning is not supported on Pull Requests.

### PinIssueInput

Autogenerated input type of PinIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The ID of the issue to be pinned.

### RemoveLabelsFromLabelableInput

Autogenerated input type of RemoveLabelsFromLabelable.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **labelIds** (`[ID!]!`): The ids of labels to remove.
- **labelableId** (`ID!`): The id of the Labelable to remove labels from.

### RemoveSubIssueInput

Autogenerated input type of RemoveSubIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The id of the issue.
- **subIssueId** (`ID!`): The id of the sub-issue.

### ReopenIssueInput

Autogenerated input type of ReopenIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): ID of the issue to be opened.

### ReprioritizeSubIssueInput

Autogenerated input type of ReprioritizeSubIssue.

**Input fields:**

- **afterId** (`ID`): The id of the sub-issue to be prioritized after (either positional argument after OR before should be specified).
- **beforeId** (`ID`): The id of the sub-issue to be prioritized before (either positional argument after OR before should be specified).
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The id of the parent issue.
- **subIssueId** (`ID!`): The id of the sub-issue to reprioritize.

### SetIssueFieldValueInput

Autogenerated input type of SetIssueFieldValue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueFields** (`[IssueFieldCreateOrUpdateInput!]!`): The issue fields to set on the issue.
- **issueId** (`ID!`): The ID of the Issue to set the field value on.

### TransferIssueInput

Autogenerated input type of TransferIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **createLabelsIfMissing** (`Boolean`): Whether to create labels if they don't exist in the target repository (matched by name).
- **issueId** (`ID!`): The Node ID of the issue to be transferred.
- **repositoryId** (`ID!`): The Node ID of the repository the issue should be transferred to.

### UnmarkIssueAsDuplicateInput

Autogenerated input type of UnmarkIssueAsDuplicate.

**Input fields:**

- **canonicalId** (`ID!`): ID of the issue or pull request currently considered canonical/authoritative/original.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **duplicateId** (`ID!`): ID of the issue or pull request currently marked as a duplicate.

### UnpinIssueCommentInput

Autogenerated input type of UnpinIssueComment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueCommentId** (`ID!`): The ID of the Issue Comment to unpin. Comment pinning is not supported on Pull Requests.

### UnpinIssueInput

Autogenerated input type of UnpinIssue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The ID of the issue to be unpinned.

### UpdateEnterpriseMembersCanDeleteIssuesSettingInput

Autogenerated input type of UpdateEnterpriseMembersCanDeleteIssuesSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the members can delete issues setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the members can delete issues setting on the enterprise.

### UpdateIssueCommentInput

Autogenerated input type of UpdateIssueComment.

**Input fields:**

- **body** (`String!`): The updated text of the comment.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The ID of the IssueComment to modify.

### UpdateIssueFieldInput

Autogenerated input type of UpdateIssueField.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **description** (`String`): A description of the issue field.
- **id** (`ID!`): The ID of the issue field to update.
- **name** (`String`): The name of the issue field.
- **options** (`[IssueFieldSingleSelectOptionInput!]`): The options for the issue field if applicable.
- **visibility** (`IssueFieldVisibility`): The visibility of the issue field.

### UpdateIssueFieldValueInput

Autogenerated input type of UpdateIssueFieldValue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueField** (`IssueFieldCreateOrUpdateInput!`): The field value to update.
- **issueId** (`ID!`): The ID of the issue.

### UpdateIssueInput

Autogenerated input type of UpdateIssue.

**Input fields:**

- **agentAssignment** (`AgentAssignmentInput`): Configuration for assigning an AI agent to this issue.
- **assigneeIds** (`[ID!]`): An array of Node IDs of users or bots for this issue.
- **body** (`String`): The body for the issue description.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The ID of the Issue to modify.
- **issueTypeId** (`ID`): The ID of the Issue Type for this issue.
- **labelIds** (`[ID!]`): An array of Node IDs of labels for this issue.
- **milestoneId** (`ID`): The Node ID of the milestone for this issue.
- **projectIds** (`[ID!]`): An array of Node IDs for projects associated with this issue.
- **state** (`IssueState`): The desired issue state.
- **title** (`String`): The title for the issue.

### UpdateIssueIssueTypeInput

Autogenerated input type of UpdateIssueIssueType.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The ID of the issue to update.
- **issueTypeId** (`ID`): The ID of the issue type to update on the issue.

### UpdateIssueTypeInput

Autogenerated input type of UpdateIssueType.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **color** (`IssueTypeColor`): Color for the issue type.
- **description** (`String`): The description of the issue type.
- **isEnabled** (`Boolean`): Whether or not the issue type is enabled for the organization.
- **issueTypeId** (`ID!`): The ID of the issue type to update.
- **name** (`String`): The name of the issue type.

### UpdateLabelInput

Autogenerated input type of UpdateLabel.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **color** (`String`): A 6 character hex code, without the leading #, identifying the updated color of the label.
- **description** (`String`): A brief description of the label, such as its purpose.
- **id** (`ID!`): The Node ID of the label to be updated.
- **name** (`String`): The updated name of the label.

### UpdateProjectV2DraftIssueInput

Autogenerated input type of UpdateProjectV2DraftIssue.

**Input fields:**

- **assigneeIds** (`[ID!]`): The IDs of the assignees of the draft issue.
- **body** (`String`): The body of the draft issue.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **draftIssueId** (`ID!`): The ID of the draft issue to update.
- **title** (`String`): The title of the draft issue.

## Unions

### CreatedIssueOrRestrictedContribution

Represents either a issue the viewer can access or a restricted contribution.

**Possible types:** CreatedIssueContribution, RestrictedContribution

### IssueFieldValue

Issue field values.

**Possible types:** IssueFieldDateValue, IssueFieldNumberValue, IssueFieldSingleSelectValue, IssueFieldTextValue

### IssueFields

Possible issue fields.

**Possible types:** IssueFieldDate, IssueFieldNumber, IssueFieldSingleSelect, IssueFieldText

### IssueOrPullRequest

Used for return value of Repository.issueOrPullRequest.

**Possible types:** Issue, PullRequest

### IssueTimelineItem

An item in an issue timeline.

**Possible types:** AssignedEvent, ClosedEvent, Commit, CrossReferencedEvent, DemilestonedEvent, IssueComment, LabeledEvent, LockedEvent, MilestonedEvent, ReferencedEvent, RenamedTitleEvent, ReopenedEvent, SubscribedEvent, TransferredEvent, UnassignedEvent, UnlabeledEvent, UnlockedEvent, UnsubscribedEvent, UserBlockedEvent

### IssueTimelineItems

An item in an issue timeline.

**Possible types:** AddedToProjectEvent, AddedToProjectV2Event, AssignedEvent, BlockedByAddedEvent, BlockedByRemovedEvent, BlockingAddedEvent, BlockingRemovedEvent, ClosedEvent, CommentDeletedEvent, ConnectedEvent, ConvertedFromDraftEvent, ConvertedNoteToIssueEvent, ConvertedToDiscussionEvent, CrossReferencedEvent, DemilestonedEvent, DisconnectedEvent, IssueComment, IssueCommentPinnedEvent, IssueCommentUnpinnedEvent, IssueFieldAddedEvent, IssueFieldChangedEvent, IssueFieldRemovedEvent, IssueTypeAddedEvent, IssueTypeChangedEvent, IssueTypeRemovedEvent, LabeledEvent, LockedEvent, MarkedAsDuplicateEvent, MentionedEvent, MilestonedEvent, MovedColumnsInProjectEvent, ParentIssueAddedEvent, ParentIssueRemovedEvent, PinnedEvent, ProjectV2ItemStatusChangedEvent, ReferencedEvent, RemovedFromProjectEvent, RemovedFromProjectV2Event, RenamedTitleEvent, ReopenedEvent, SubIssueAddedEvent, SubIssueRemovedEvent, SubscribedEvent, TransferredEvent, UnassignedEvent, UnlabeledEvent, UnlockedEvent, UnmarkedAsDuplicateEvent, UnpinnedEvent, UnsubscribedEvent, UserBlockedEvent

### MilestoneItem

Types that can be inside a Milestone.

**Possible types:** Issue, PullRequest

### ProjectV2IssueFieldValues

Possible issue field values for a Project item.

**Possible types:** IssueFieldDateValue, IssueFieldNumberValue, IssueFieldSingleSelectValue, IssueFieldTextValue


---

**See also:** [Repositories](repositories.md) | [Pull Requests](pull-requests.md) | [Projects](projects.md) | [Users & Orgs](users-and-orgs.md)
