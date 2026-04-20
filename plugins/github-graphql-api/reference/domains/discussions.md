# Discussions

## Mutations

### addDiscussionComment

Adds a comment to a Discussion, possibly as a reply to another comment.

**Input fields:**

- **input** (`AddDiscussionCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **comment** (`DiscussionComment`): The newly created discussion comment.

### addDiscussionPollVote

Vote for an option in a discussion poll.

**Input fields:**

- **input** (`AddDiscussionPollVoteInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **pollOption** (`DiscussionPollOption`): The poll option that a vote was added to.

### closeDiscussion

Close a discussion.

**Input fields:**

- **input** (`CloseDiscussionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussion** (`Discussion`): The discussion that was closed.

### createDiscussion

Create a discussion.

**Input fields:**

- **input** (`CreateDiscussionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussion** (`Discussion`): The discussion that was just created.

### deleteDiscussion

Delete a discussion and all of its replies.

**Input fields:**

- **input** (`DeleteDiscussionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussion** (`Discussion`): The discussion that was just deleted.

### deleteDiscussionComment

Delete a discussion comment. If it has replies, wipe it instead.

**Input fields:**

- **input** (`DeleteDiscussionCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **comment** (`DiscussionComment`): The discussion comment that was just deleted.

### markDiscussionCommentAsAnswer

Mark a discussion comment as the chosen answer for discussions in an answerable category.

**Input fields:**

- **input** (`MarkDiscussionCommentAsAnswerInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussion** (`Discussion`): The discussion that includes the chosen comment.

### reopenDiscussion

Reopen a discussion.

**Input fields:**

- **input** (`ReopenDiscussionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussion** (`Discussion`): The discussion that was reopened.

### unmarkDiscussionCommentAsAnswer

Unmark a discussion comment as the chosen answer for discussions in an answerable category.

**Input fields:**

- **input** (`UnmarkDiscussionCommentAsAnswerInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussion** (`Discussion`): The discussion that includes the comment.

### updateDiscussion

Update a discussion.

**Input fields:**

- **input** (`UpdateDiscussionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussion** (`Discussion`): The modified discussion.

### updateDiscussionComment

Update the contents of a comment on a Discussion.

**Input fields:**

- **input** (`UpdateDiscussionCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **comment** (`DiscussionComment`): The modified discussion comment.

## Types

### ConvertedToDiscussionEvent

Represents a`converted_to_discussion`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **discussion** (`Discussion`): The discussion that the issue was converted into.
- **id** (`ID!`): The Node ID of the ConvertedToDiscussionEvent object.

### Discussion

A discussion in a repository.

**Implements:** Closable, Comment, Deletable, Labelable, Lockable, Node, Reactable, RepositoryNode, Subscribable, Updatable, Votable

**Fields:**

- **activeLockReason** (`LockReason`): Reason that the conversation was locked.
- **answer** (`DiscussionComment`): The comment chosen as this discussion's answer, if any.
- **answerChosenAt** (`DateTime`): The time when a user chose this discussion's answer, if answered.
- **answerChosenBy** (`Actor`): The user who chose this discussion's answer, if answered.
- **author** (`Actor`): The actor who authored the discussion.
- **authorAssociation** (`CommentAuthorAssociation!`): Author's association with the subject of the comment.
- **body** (`String!`): The main text of the discussion post.
- **bodyHTML** (`HTML!`): The body rendered to HTML.
- **bodyText** (`String!`): The body rendered to text.
- **category** (`DiscussionCategory!`): The category for this discussion.
- **closed** (`Boolean!`): Indicates if the object is closed (definition of closed may depend on type).
- **closedAt** (`DateTime`): Identifies the date and time when the object was closed.
- **comments** (`DiscussionCommentConnection!`): The replies to the discussion.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **createdViaEmail** (`Boolean!`): Check if this comment was created via an email reply.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **editor** (`Actor`): The actor who edited the comment.
- **id** (`ID!`): The Node ID of the Discussion object.
- **includesCreatedEdit** (`Boolean!`): Check if this comment was edited and includes an edit with the creation data.
- **isAnswered** (`Boolean`): Only return answered/unanswered discussions.
- **labels** (`LabelConnection`): A list of labels associated with the object.
- **lastEditedAt** (`DateTime`): The moment the editor made the last edit.
- **locked** (`Boolean!`): `true` if the object is locked.
- **number** (`Int!`): The number identifying this discussion within the repository.
- **poll** (`DiscussionPoll`): The poll associated with this discussion, if one exists.
- **publishedAt** (`DateTime`): Identifies when the comment was published at.
- **reactionGroups** (`[ReactionGroup!]`): A list of reactions grouped by content left on the subject.
- **reactions** (`ReactionConnection!`): A list of Reactions left on the Issue.
- **repository** (`Repository!`): The repository associated with this node.
- **resourcePath** (`URI!`): The path for this discussion.
- **stateReason** (`DiscussionStateReason`): Identifies the reason for the discussion's state.
- **title** (`String!`): The title of this discussion.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **upvoteCount** (`Int!`): Number of upvotes that this subject has received.
- **url** (`URI!`): The URL for this discussion.
- **userContentEdits** (`UserContentEditConnection`): A list of edits to this content.
- **viewerCanClose** (`Boolean!`): Indicates if the object can be closed by the viewer.
- **viewerCanDelete** (`Boolean!`): Check if the current viewer can delete this object.
- **viewerCanLabel** (`Boolean!`): Indicates if the viewer can edit labels for this object.
- **viewerCanReact** (`Boolean!`): Can user react to this subject.
- **viewerCanReopen** (`Boolean!`): Indicates if the object can be reopened by the viewer.
- **viewerCanSubscribe** (`Boolean!`): Check if the viewer is able to change their subscription status for the repository.
- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.
- **viewerCanUpvote** (`Boolean!`): Whether or not the current user can add or remove an upvote on this subject.
- **viewerDidAuthor** (`Boolean!`): Did the viewer author this comment.
- **viewerHasUpvoted** (`Boolean!`): Whether or not the current user has already upvoted this subject.
- **viewerSubscription** (`SubscriptionState`): Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

### DiscussionCategory

A category for discussions in a repository.

**Implements:** Node, RepositoryNode

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **description** (`String`): A description of this category.
- **emoji** (`String!`): An emoji representing this category.
- **emojiHTML** (`HTML!`): This category's emoji rendered as HTML.
- **id** (`ID!`): The Node ID of the DiscussionCategory object.
- **isAnswerable** (`Boolean!`): Whether or not discussions in this category support choosing an answer with the markDiscussionCommentAsAnswer mutation.
- **name** (`String!`): The name of this category.
- **repository** (`Repository!`): The repository associated with this node.
- **slug** (`String!`): The slug of this category.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### DiscussionComment

A comment on a discussion.

**Implements:** Comment, Deletable, Minimizable, Node, Reactable, Updatable, UpdatableComment, Votable

**Fields:**

- **author** (`Actor`): The actor who authored the comment.
- **authorAssociation** (`CommentAuthorAssociation!`): Author's association with the subject of the comment.
- **body** (`String!`): The body as Markdown.
- **bodyHTML** (`HTML!`): The body rendered to HTML.
- **bodyText** (`String!`): The body rendered to text.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **createdViaEmail** (`Boolean!`): Check if this comment was created via an email reply.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **deletedAt** (`DateTime`): The time when this replied-to comment was deleted.
- **discussion** (`Discussion`): The discussion this comment was created in.
- **editor** (`Actor`): The actor who edited the comment.
- **id** (`ID!`): The Node ID of the DiscussionComment object.
- **includesCreatedEdit** (`Boolean!`): Check if this comment was edited and includes an edit with the creation data.
- **isAnswer** (`Boolean!`): Has this comment been chosen as the answer of its discussion?.
- **isMinimized** (`Boolean!`): Returns whether or not a comment has been minimized.
- **lastEditedAt** (`DateTime`): The moment the editor made the last edit.
- **minimizedReason** (`String`): Returns why the comment was minimized. One of `abuse`, `off-topic`,
`outdated`, `resolved`, `duplicate`, `spam`, and `low-quality`. Note that the
case and formatting of these values differs from the inputs to the
`MinimizeComment` mutation.
- **publishedAt** (`DateTime`): Identifies when the comment was published at.
- **reactionGroups** (`[ReactionGroup!]`): A list of reactions grouped by content left on the subject.
- **reactions** (`ReactionConnection!`): A list of Reactions left on the Issue.
- **replies** (`DiscussionCommentConnection!`): The threaded replies to this comment.
- **replyTo** (`DiscussionComment`): The discussion comment this comment is a reply to.
- **resourcePath** (`URI!`): The path for this discussion comment.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **upvoteCount** (`Int!`): Number of upvotes that this subject has received.
- **url** (`URI!`): The URL for this discussion comment.
- **userContentEdits** (`UserContentEditConnection`): A list of edits to this content.
- **viewerCanDelete** (`Boolean!`): Check if the current viewer can delete this object.
- **viewerCanMarkAsAnswer** (`Boolean!`): Can the current user mark this comment as an answer?.
- **viewerCanMinimize** (`Boolean!`): Check if the current viewer can minimize this object.
- **viewerCanReact** (`Boolean!`): Can user react to this subject.
- **viewerCanUnmarkAsAnswer** (`Boolean!`): Can the current user unmark this comment as an answer?.
- **viewerCanUnminimize** (`Boolean!`): Check if the current viewer can unminimize this object.
- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.
- **viewerCanUpvote** (`Boolean!`): Whether or not the current user can add or remove an upvote on this subject.
- **viewerCannotUpdateReasons** (`[CommentCannotUpdateReason!]!`): Reasons why the current viewer can not update this comment.
- **viewerDidAuthor** (`Boolean!`): Did the viewer author this comment.
- **viewerHasUpvoted** (`Boolean!`): Whether or not the current user has already upvoted this subject.

### DiscussionPoll

A poll for a discussion.

**Implements:** Node

**Fields:**

- **discussion** (`Discussion`): The discussion that this poll belongs to.
- **id** (`ID!`): The Node ID of the DiscussionPoll object.
- **options** (`DiscussionPollOptionConnection`): The options for this poll.
- **question** (`String!`): The question that is being asked by this poll.
- **totalVoteCount** (`Int!`): The total number of votes that have been cast for this poll.
- **viewerCanVote** (`Boolean!`): Indicates if the viewer has permission to vote in this poll.
- **viewerHasVoted** (`Boolean!`): Indicates if the viewer has voted for any option in this poll.

### DiscussionPollOption

An option for a discussion poll.

**Implements:** Node

**Fields:**

- **id** (`ID!`): The Node ID of the DiscussionPollOption object.
- **option** (`String!`): The text for this option.
- **poll** (`DiscussionPoll`): The discussion poll that this option belongs to.
- **totalVoteCount** (`Int!`): The total number of votes that have been cast for this option.
- **viewerHasVoted** (`Boolean!`): Indicates if the viewer has voted for this option in the poll.

### PinnedDiscussion

A Pinned Discussion is a discussion pinned to a repository's index page.

**Implements:** Node, RepositoryNode

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **discussion** (`Discussion!`): The discussion that was pinned.
- **gradientStopColors** (`[String!]!`): Color stops of the chosen gradient.
- **id** (`ID!`): The Node ID of the PinnedDiscussion object.
- **pattern** (`PinnedDiscussionPattern!`): Background texture pattern.
- **pinnedBy** (`Actor!`): The actor that pinned this discussion.
- **preconfiguredGradient** (`PinnedDiscussionGradient`): Preconfigured background gradient option.
- **repository** (`Repository!`): The repository associated with this node.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **DiscussionCategoryConnection** (4 fields): The connection type for DiscussionCategory.
- **DiscussionCategoryEdge** (2 fields): An edge in a connection.
- **DiscussionCommentConnection** (4 fields): The connection type for DiscussionComment.
- **DiscussionCommentEdge** (2 fields): An edge in a connection.
- **DiscussionConnection** (4 fields): The connection type for Discussion.
- **DiscussionEdge** (2 fields): An edge in a connection.
- **DiscussionPollOptionConnection** (4 fields): The connection type for DiscussionPollOption.
- **DiscussionPollOptionEdge** (2 fields): An edge in a connection.
- **PinnedDiscussionConnection** (4 fields): The connection type for PinnedDiscussion.
- **PinnedDiscussionEdge** (2 fields): An edge in a connection.

## Enums

### DiscussionCloseReason

The possible reasons for closing a discussion.

**Values:**

- `DUPLICATE`: The discussion is a duplicate of another.
- `OUTDATED`: The discussion is no longer relevant.
- `RESOLVED`: The discussion has been resolved.

### DiscussionOrderField

Properties by which discussion connections can be ordered.

**Values:**

- `CREATED_AT`: Order discussions by creation time.
- `UPDATED_AT`: Order discussions by most recent modification time.

### DiscussionPollOptionOrderField

Properties by which discussion poll option connections can be ordered.

**Values:**

- `AUTHORED_ORDER`: Order poll options by the order that the poll author specified when creating the poll.
- `VOTE_COUNT`: Order poll options by the number of votes it has.

### DiscussionState

The possible states of a discussion.

**Values:**

- `CLOSED`: A discussion that has been closed.
- `OPEN`: A discussion that is open.

### DiscussionStateReason

The possible state reasons of a discussion.

**Values:**

- `DUPLICATE`: The discussion is a duplicate of another.
- `OUTDATED`: The discussion is no longer relevant.
- `REOPENED`: The discussion was reopened.
- `RESOLVED`: The discussion has been resolved.

### PinnedDiscussionGradient

Preconfigured gradients that may be used to style discussions pinned within a repository.

**Values:**

- `BLUE_MINT`: A gradient of blue to mint.
- `BLUE_PURPLE`: A gradient of blue to purple.
- `PINK_BLUE`: A gradient of pink to blue.
- `PURPLE_CORAL`: A gradient of purple to coral.
- `RED_ORANGE`: A gradient of red to orange.

### PinnedDiscussionPattern

Preconfigured background patterns that may be used to style discussions pinned within a repository.

**Values:**

- `CHEVRON_UP`: An upward-facing chevron pattern.
- `DOT`: A hollow dot pattern.
- `DOT_FILL`: A solid dot pattern.
- `HEART_FILL`: A heart pattern.
- `PLUS`: A plus sign pattern.
- `ZAP`: A lightning bolt pattern.

## Input Objects

### AddDiscussionCommentInput

Autogenerated input type of AddDiscussionComment.

**Input fields:**

- **body** (`String!`): The contents of the comment.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussionId** (`ID!`): The Node ID of the discussion to comment on.
- **replyToId** (`ID`): The Node ID of the discussion comment within this discussion to reply to.

### AddDiscussionPollVoteInput

Autogenerated input type of AddDiscussionPollVote.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **pollOptionId** (`ID!`): The Node ID of the discussion poll option to vote for.

### CloseDiscussionInput

Autogenerated input type of CloseDiscussion.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussionId** (`ID!`): ID of the discussion to be closed.
- **reason** (`DiscussionCloseReason`): The reason why the discussion is being closed.

### CreateDiscussionInput

Autogenerated input type of CreateDiscussion.

**Input fields:**

- **body** (`String!`): The body of the discussion.
- **categoryId** (`ID!`): The id of the discussion category to associate with this discussion.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryId** (`ID!`): The id of the repository on which to create the discussion.
- **title** (`String!`): The title of the discussion.

### DeleteDiscussionCommentInput

Autogenerated input type of DeleteDiscussionComment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The Node id of the discussion comment to delete.

### DeleteDiscussionInput

Autogenerated input type of DeleteDiscussion.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The id of the discussion to delete.

### DiscussionOrder

Ways in which lists of discussions can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order discussions by the specified field.
- **field** (`DiscussionOrderField!`): The field by which to order discussions.

### DiscussionPollOptionOrder

Ordering options for discussion poll option connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`DiscussionPollOptionOrderField!`): The field to order poll options by.

### MarkDiscussionCommentAsAnswerInput

Autogenerated input type of MarkDiscussionCommentAsAnswer.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The Node ID of the discussion comment to mark as an answer.

### ReopenDiscussionInput

Autogenerated input type of ReopenDiscussion.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussionId** (`ID!`): ID of the discussion to be reopened.

### UnmarkDiscussionCommentAsAnswerInput

Autogenerated input type of UnmarkDiscussionCommentAsAnswer.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The Node ID of the discussion comment to unmark as an answer.

### UpdateDiscussionCommentInput

Autogenerated input type of UpdateDiscussionComment.

**Input fields:**

- **body** (`String!`): The new contents of the comment body.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **commentId** (`ID!`): The Node ID of the discussion comment to update.

### UpdateDiscussionInput

Autogenerated input type of UpdateDiscussion.

**Input fields:**

- **body** (`String`): The new contents of the discussion body.
- **categoryId** (`ID`): The Node ID of a discussion category within the same repository to change this discussion to.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **discussionId** (`ID!`): The Node ID of the discussion to update.
- **title** (`String`): The new discussion title.
