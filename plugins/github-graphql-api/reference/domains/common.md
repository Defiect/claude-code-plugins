# Common Types & Shared Interfaces

## Queries

### id

**Returns:** `ID!`

ID of the object.

### node

**Returns:** `Node`

Fetches an object given its ID.

**Arguments:**

- `id` (`ID!`): ID of the object.

### nodes

**Returns:** `[Node]!`

Lookup nodes by a list of IDs.

**Arguments:**

- `ids` (`[ID!]!`): The list of node IDs.

### rateLimit

**Returns:** `RateLimit`

The client's rate limit information.

**Arguments:**

- `dryRun` (`Boolean`): If true, calculate the cost for the query without evaluating it.

### relay

**Returns:** `Query!`

Workaround for re-exposing the root query object. (Refer to
[https://github.com/facebook/relay/issues/112](https://github.com/facebook/relay/issues/112) for more information.).

### resource

**Returns:** `UniformResourceLocatable`

Lookup resource by a URL.

**Arguments:**

- `url` (`URI!`): The URL.

### search

**Returns:** `SearchResultItemConnection!`

Perform a search across resources, returning a maximum of 1,000 results.

**Arguments:**

- `after` (`String`): Returns the elements in the list that come after the specified cursor.
- `before` (`String`): Returns the elements in the list that come before the specified cursor.
- `first` (`Int`): Returns the first _n_ elements from the list.
- `last` (`Int`): Returns the last _n_ elements from the list.
- `query` (`String!`): The search string to look for. GitHub search syntax is supported. For more
information, see "[Searching on
GitHub](https://docs.github.com/search-github/searching-on-github),"
"[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax),"
and "[Sorting search results](https://docs.github.com/search-github/getting-started-with-searching-on-github/sorting-search-results).".
- `type` (`SearchType!`): The types of search items to search within.

## Mutations

### abortQueuedMigrations

Clear all of a customer's queued migrations.

**Input fields:**

- **input** (`AbortQueuedMigrationsInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **success** (`Boolean`): Did the operation succeed?.

### addAssigneesToAssignable

Adds assignees to an assignable object.

**Input fields:**

- **input** (`AddAssigneesToAssignableInput!`)

**Return fields:**

- **assignable** (`Assignable`): The item that was assigned.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### addBlockedBy

Adds a 'blocked by' relationship to an issue.

**Input fields:**

- **input** (`AddBlockedByInput!`)

**Return fields:**

- **blockingIssue** (`Issue`): The issue that is blocking the given issue.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The issue that is blocked.

### addComment

Adds a comment to an Issue or Pull Request.

**Input fields:**

- **input** (`AddCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **commentEdge** (`IssueCommentEdge`): The edge from the subject's comment connection.
- **subject** (`Node`): The subject.
- **timelineEdge** (`IssueTimelineItemEdge`): The edge from the subject's timeline connection.

### addReaction

Adds a reaction to a subject.

**Input fields:**

- **input** (`AddReactionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **reaction** (`Reaction`): The reaction object.
- **reactionGroups** (`[ReactionGroup!]`): The reaction groups for the subject.
- **subject** (`Reactable`): The reactable subject.

### addStar

Adds a star to a Starrable.

**Input fields:**

- **input** (`AddStarInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **starrable** (`Starrable`): The starrable.

### addUpvote

Add an upvote to a discussion or discussion comment.

**Input fields:**

- **input** (`AddUpvoteInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **subject** (`Votable`): The votable subject.

### addVerifiableDomain

Adds a verifiable domain to an owning account.

**Input fields:**

- **input** (`AddVerifiableDomainInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **domain** (`VerifiableDomain`): The verifiable domain that was added.

### createIpAllowListEntry

Creates a new IP allow list entry.

**Input fields:**

- **input** (`CreateIpAllowListEntryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ipAllowListEntry** (`IpAllowListEntry`): The IP allow list entry that was created.

### createMigrationSource

Creates a GitHub Enterprise Importer (GEI) migration source.

**Input fields:**

- **input** (`CreateMigrationSourceInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **migrationSource** (`MigrationSource`): The created migration source.

### deleteIpAllowListEntry

Deletes an IP allow list entry.

**Input fields:**

- **input** (`DeleteIpAllowListEntryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ipAllowListEntry** (`IpAllowListEntry`): The IP allow list entry that was deleted.

### deleteVerifiableDomain

Deletes a verifiable domain.

**Input fields:**

- **input** (`DeleteVerifiableDomainInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **owner** (`VerifiableDomainOwner`): The owning account from which the domain was deleted.

### grantMigratorRole

Grant the migrator role to a user or a team.

**Input fields:**

- **input** (`GrantMigratorRoleInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **success** (`Boolean`): Did the operation succeed?.

### lockLockable

Lock a lockable object.

**Input fields:**

- **input** (`LockLockableInput!`)

**Return fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **lockedRecord** (`Lockable`): The item that was locked.

### markFileAsViewed

Mark a pull request file as viewed.

**Input fields:**

- **input** (`MarkFileAsViewedInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **pullRequest** (`PullRequest`): The updated pull request.

### minimizeComment

Minimizes a comment on an Issue, Commit, Pull Request, or Gist.

**Input fields:**

- **input** (`MinimizeCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **minimizedComment** (`Minimizable`): The comment that was minimized.

### regenerateVerifiableDomainToken

Regenerates a verifiable domain's verification token.

**Input fields:**

- **input** (`RegenerateVerifiableDomainTokenInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **verificationToken** (`String`): The verification token that was generated.

### removeAssigneesFromAssignable

Removes assignees from an assignable object.

**Input fields:**

- **input** (`RemoveAssigneesFromAssignableInput!`)

**Return fields:**

- **assignable** (`Assignable`): The item that was unassigned.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### removeBlockedBy

Removes a 'blocked by' relationship from an issue.

**Input fields:**

- **input** (`RemoveBlockedByInput!`)

**Return fields:**

- **blockingIssue** (`Issue`): The previously blocking issue.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issue** (`Issue`): The previously blocked issue.

### removeOutsideCollaborator

Removes outside collaborator from all repositories in an organization.

**Input fields:**

- **input** (`RemoveOutsideCollaboratorInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **removedUser** (`User`): The user that was removed as an outside collaborator.

### removeReaction

Removes a reaction from a subject.

**Input fields:**

- **input** (`RemoveReactionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **reaction** (`Reaction`): The reaction object.
- **reactionGroups** (`[ReactionGroup!]`): The reaction groups for the subject.
- **subject** (`Reactable`): The reactable subject.

### removeStar

Removes a star from a Starrable.

**Input fields:**

- **input** (`RemoveStarInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **starrable** (`Starrable`): The starrable.

### removeUpvote

Remove an upvote to a discussion or discussion comment.

**Input fields:**

- **input** (`RemoveUpvoteInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **subject** (`Votable`): The votable subject.

### replaceActorsForAssignable

Replaces all actors for assignable object.

**Input fields:**

- **input** (`ReplaceActorsForAssignableInput!`)

**Return fields:**

- **assignable** (`Assignable`): The item that was assigned.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### revokeMigratorRole

Revoke the migrator role from a user or a team.

**Input fields:**

- **input** (`RevokeMigratorRoleInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **success** (`Boolean`): Did the operation succeed?.

### unlockLockable

Unlock a lockable object.

**Input fields:**

- **input** (`UnlockLockableInput!`)

**Return fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **unlockedRecord** (`Lockable`): The item that was unlocked.

### unmarkFileAsViewed

Unmark a pull request file as viewed.

**Input fields:**

- **input** (`UnmarkFileAsViewedInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **pullRequest** (`PullRequest`): The updated pull request.

### unminimizeComment

Unminimizes a comment on an Issue, Commit, Pull Request, or Gist.

**Input fields:**

- **input** (`UnminimizeCommentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **unminimizedComment** (`Minimizable`): The comment that was unminimized.

### updateIpAllowListEnabledSetting

Sets whether an IP allow list is enabled on an owner.

**Input fields:**

- **input** (`UpdateIpAllowListEnabledSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **owner** (`IpAllowListOwner`): The IP allow list owner on which the setting was updated.

### updateIpAllowListEntry

Updates an IP allow list entry.

**Input fields:**

- **input** (`UpdateIpAllowListEntryInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ipAllowListEntry** (`IpAllowListEntry`): The IP allow list entry that was updated.

### updateNotificationRestrictionSetting

Update the setting to restrict notifications to only verified or approved domains available to an owner.

**Input fields:**

- **input** (`UpdateNotificationRestrictionSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **owner** (`VerifiableDomainOwner`): The owner on which the setting was updated.

### updateSubscription

Updates the state for subscribable subjects.

**Input fields:**

- **input** (`UpdateSubscriptionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **subscribable** (`Subscribable`): The input subscribable entity.

### verifyVerifiableDomain

Verify that a verifiable domain has the expected DNS record.

**Input fields:**

- **input** (`VerifyVerifiableDomainInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **domain** (`VerifiableDomain`): The verifiable domain that was verified.

## Types

### ActorLocation

Location information for an actor.

**Fields:**

- **city** (`String`): City.
- **country** (`String`): Country name.
- **countryCode** (`String`): Country code.
- **region** (`String`): Region name.
- **regionCode** (`String`): Region or state code.

### AnnouncementBanner

An announcement banner for an enterprise or organization.

**Fields:**

- **createdAt** (`DateTime!`): The date the announcement was created.
- **expiresAt** (`DateTime`): The expiration date of the announcement, if any.
- **isUserDismissible** (`Boolean!`): Whether the announcement can be dismissed by the user.
- **message** (`String`): The text of the announcement.

### AssignedEvent

Represents an`assigned`event on any assignable object.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **assignable** (`Assignable!`): Identifies the assignable associated with the event.
- **assignee** (`Assignee`): Identifies the user or mannequin that was assigned.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the AssignedEvent object.
- **user** (`User`): Identifies the user who was assigned.

### BlockedByAddedEvent

Represents a`blocked_by_added`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **blockingIssue** (`Issue`): The blocking issue that was added.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the BlockedByAddedEvent object.

### BlockedByRemovedEvent

Represents a`blocked_by_removed`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **blockingIssue** (`Issue`): The blocking issue that was removed.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the BlockedByRemovedEvent object.

### BlockingAddedEvent

Represents a`blocking_added`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **blockedIssue** (`Issue`): The blocked issue that was added.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the BlockingAddedEvent object.

### BlockingRemovedEvent

Represents a`blocking_removed`event on a given issue.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **blockedIssue** (`Issue`): The blocked issue that was removed.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the BlockingRemovedEvent object.

### BranchNamePatternParameters

Parameters to be used for the branch_name_pattern rule.

**Fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean!`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### ClosedEvent

Represents a`closed`event on any `Closable`.

**Implements:** Node, UniformResourceLocatable

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **closable** (`Closable!`): Object that was closed.
- **closer** (`Closer`): Object which triggered the creation of this event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **duplicateOf** (`IssueOrPullRequest`): The issue or pull request that this issue was marked as a duplicate of.
- **id** (`ID!`): The Node ID of the ClosedEvent object.
- **resourcePath** (`URI!`): The HTTP path for this closed event.
- **stateReason** (`IssueStateReason`): The reason the issue state was changed to closed.
- **url** (`URI!`): The HTTP URL for this closed event.

### CommentDeletedEvent

Represents a`comment_deleted`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **deletedCommentAuthor** (`Actor`): The user who authored the deleted comment.
- **id** (`ID!`): The Node ID of the CommentDeletedEvent object.

### ConnectedEvent

Represents a`connected`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the ConnectedEvent object.
- **isCrossRepository** (`Boolean!`): Reference originated in a different repository.
- **source** (`ReferencedSubject!`): Issue or pull request that made the reference.
- **subject** (`ReferencedSubject!`): Issue or pull request which was connected.

### ContributionCalendar

A calendar of contributions made on GitHub by a user.

**Fields:**

- **colors** (`[String!]!`): A list of hex color codes used in this calendar. The darker the color, the more contributions it represents.
- **isHalloween** (`Boolean!`): Determine if the color set was chosen because it's currently Halloween.
- **months** (`[ContributionCalendarMonth!]!`): A list of the months of contributions in this calendar.
- **totalContributions** (`Int!`): The count of total contributions in the calendar.
- **weeks** (`[ContributionCalendarWeek!]!`): A list of the weeks of contributions in this calendar.

### ContributionCalendarDay

Represents a single day of contributions on GitHub by a user.

**Fields:**

- **color** (`String!`): The hex color code that represents how many contributions were made on this day compared to others in the calendar.
- **contributionCount** (`Int!`): How many contributions were made by the user on this day.
- **contributionLevel** (`ContributionLevel!`): Indication of contributions, relative to other days. Can be used to indicate
which color to represent this day on a calendar.
- **date** (`Date!`): The day this square represents.
- **weekday** (`Int!`): A number representing which day of the week this square represents, e.g., 1 is Monday.

### ContributionCalendarMonth

A month of contributions in a user's contribution graph.

**Fields:**

- **firstDay** (`Date!`): The date of the first day of this month.
- **name** (`String!`): The name of the month.
- **totalWeeks** (`Int!`): How many weeks started in this month.
- **year** (`Int!`): The year the month occurred in.

### ContributionCalendarWeek

A week of contributions in a user's contribution graph.

**Fields:**

- **contributionDays** (`[ContributionCalendarDay!]!`): The days of contributions in this week.
- **firstDay** (`Date!`): The date of the earliest square in this week.

### ContributionsCollection

A collection of contributions made by a user, including opened issues, commits, and pull requests.
Contributions in private and internal repositories are only included with the optional read:user scope.

**Fields:**

- **commitContributionsByRepository** (`[CommitContributionsByRepository!]!`): Commit contributions made by the user, grouped by repository.
- **contributionCalendar** (`ContributionCalendar!`): A calendar of this user's contributions on GitHub.
- **contributionYears** (`[Int!]!`): The years the user has been making contributions with the most recent year first.
- **doesEndInCurrentMonth** (`Boolean!`): Determine if this collection's time span ends in the current month.
- **earliestRestrictedContributionDate** (`Date`): The date of the first restricted contribution the user made in this time
period. Can only be non-null when the user has enabled private contribution counts.
- **endedAt** (`DateTime!`): The ending date and time of this collection.
- **firstIssueContribution** (`CreatedIssueOrRestrictedContribution`): The first issue the user opened on GitHub. This will be null if that issue was
opened outside the collection's time range and ignoreTimeRange is false. If
the issue is not visible but the user has opted to show private contributions,
a RestrictedContribution will be returned.
- **firstPullRequestContribution** (`CreatedPullRequestOrRestrictedContribution`): The first pull request the user opened on GitHub. This will be null if that
pull request was opened outside the collection's time range and
ignoreTimeRange is not true. If the pull request is not visible but the user
has opted to show private contributions, a RestrictedContribution will be returned.
- **firstRepositoryContribution** (`CreatedRepositoryOrRestrictedContribution`): The first repository the user created on GitHub. This will be null if that
first repository was created outside the collection's time range and
ignoreTimeRange is false. If the repository is not visible, then a
RestrictedContribution is returned.
- **hasActivityInThePast** (`Boolean!`): Does the user have any more activity in the timeline that occurred prior to the collection's time range?.
- **hasAnyContributions** (`Boolean!`): Determine if there are any contributions in this collection.
- **hasAnyRestrictedContributions** (`Boolean!`): Determine if the user made any contributions in this time frame whose details
are not visible because they were made in a private repository. Can only be
true if the user enabled private contribution counts.
- **isSingleDay** (`Boolean!`): Whether or not the collector's time span is all within the same day.
- **issueContributions** (`CreatedIssueContributionConnection!`): A list of issues the user opened.
- **issueContributionsByRepository** (`[IssueContributionsByRepository!]!`): Issue contributions made by the user, grouped by repository.
- **joinedGitHubContribution** (`JoinedGitHubContribution`): When the user signed up for GitHub. This will be null if that sign up date
falls outside the collection's time range and ignoreTimeRange is false.
- **latestRestrictedContributionDate** (`Date`): The date of the most recent restricted contribution the user made in this time
period. Can only be non-null when the user has enabled private contribution counts.
- **mostRecentCollectionWithActivity** (`ContributionsCollection`): When this collection's time range does not include any activity from the user, use this
to get a different collection from an earlier time range that does have activity.
- **mostRecentCollectionWithoutActivity** (`ContributionsCollection`): Returns a different contributions collection from an earlier time range than this one
that does not have any contributions.
- **popularIssueContribution** (`CreatedIssueContribution`): The issue the user opened on GitHub that received the most comments in the specified
time frame.
- **popularPullRequestContribution** (`CreatedPullRequestContribution`): The pull request the user opened on GitHub that received the most comments in the
specified time frame.
- **pullRequestContributions** (`CreatedPullRequestContributionConnection!`): Pull request contributions made by the user.
- **pullRequestContributionsByRepository** (`[PullRequestContributionsByRepository!]!`): Pull request contributions made by the user, grouped by repository.
- **pullRequestReviewContributions** (`CreatedPullRequestReviewContributionConnection!`): Pull request review contributions made by the user. Returns the most recently
submitted review for each PR reviewed by the user.
- **pullRequestReviewContributionsByRepository** (`[PullRequestReviewContributionsByRepository!]!`): Pull request review contributions made by the user, grouped by repository.
- **repositoryContributions** (`CreatedRepositoryContributionConnection!`): A list of repositories owned by the user that the user created in this time range.
- **restrictedContributionsCount** (`Int!`): A count of contributions made by the user that the viewer cannot access. Only
non-zero when the user has chosen to share their private contribution counts.
- **startedAt** (`DateTime!`): The beginning date and time of this collection.
- **totalCommitContributions** (`Int!`): How many commits were made by the user in this time span.
- **totalIssueContributions** (`Int!`): How many issues the user opened.
- **totalPullRequestContributions** (`Int!`): How many pull requests the user opened.
- **totalPullRequestReviewContributions** (`Int!`): How many pull request reviews the user left.
- **totalRepositoriesWithContributedCommits** (`Int!`): How many different repositories the user committed to.
- **totalRepositoriesWithContributedIssues** (`Int!`): How many different repositories the user opened issues in.
- **totalRepositoriesWithContributedPullRequestReviews** (`Int!`): How many different repositories the user left pull request reviews in.
- **totalRepositoriesWithContributedPullRequests** (`Int!`): How many different repositories the user opened pull requests in.
- **totalRepositoryContributions** (`Int!`): How many repositories the user created.
- **user** (`User!`): The user who made the contributions in this collection.

### CopilotCodeReviewParameters

Request Copilot code review for new pull requests automatically if the author
has access to Copilot code review and their premium requests quota has not
reached the limit.

**Fields:**

- **reviewDraftPullRequests** (`Boolean!`): Copilot automatically reviews draft pull requests before they are marked as ready for review.
- **reviewOnPush** (`Boolean!`): Copilot automatically reviews each new push to the pull request.

### CopilotEndpoints

Copilot endpoint information.

**Fields:**

- **api** (`String!`): Copilot API endpoint.
- **originTracker** (`String!`): Copilot origin tracker endpoint.
- **proxy** (`String!`): Copilot proxy endpoint.
- **telemetry** (`String!`): Copilot telemetry endpoint.

### CvssSeverities

The Common Vulnerability Scoring System.

**Fields:**

- **cvssV3** (`CVSS`): The CVSS v3 severity associated with this advisory.
- **cvssV4** (`CVSS`): The CVSS v4 severity associated with this advisory.

### DemilestonedEvent

Represents a`demilestoned`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the DemilestonedEvent object.
- **milestoneTitle** (`String!`): Identifies the milestone title associated with the`demilestoned`event.
- **subject** (`MilestoneItem!`): Object referenced by event.

### DeployedEvent

Represents a`deployed`event on a given pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **deployment** (`Deployment!`): The deployment associated with the`deployed`event.
- **id** (`ID!`): The Node ID of the DeployedEvent object.
- **pullRequest** (`PullRequest!`): PullRequest referenced by event.
- **ref** (`Ref`): The ref associated with the`deployed`event.

### DisconnectedEvent

Represents a`disconnected`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the DisconnectedEvent object.
- **isCrossRepository** (`Boolean!`): Reference originated in a different repository.
- **source** (`ReferencedSubject!`): Issue or pull request from which the issue was disconnected.
- **subject** (`ReferencedSubject!`): Issue or pull request which was disconnected.

### FileExtensionRestrictionParameters

Prevent commits that include files with specified file extensions from being pushed to the commit graph.

**Fields:**

- **restrictedFileExtensions** (`[String!]!`): The file extensions that are restricted from being pushed to the commit graph.

### FilePathRestrictionParameters

Prevent commits that include changes in specified file and folder paths from
being pushed to the commit graph. This includes absolute paths that contain file names.

**Fields:**

- **restrictedFilePaths** (`[String!]!`): The file paths that are restricted from being pushed to the commit graph.

### JoinedGitHubContribution

Represents a user signing up for a GitHub account.

**Implements:** Contribution

**Fields:**

- **isRestricted** (`Boolean!`): Whether this contribution is associated with a record you do not have access to. For
example, your own 'first issue' contribution may have been made on a repository you can no
longer access.
- **occurredAt** (`DateTime!`): When this contribution was made.
- **resourcePath** (`URI!`): The HTTP path for this contribution.
- **url** (`URI!`): The HTTP URL for this contribution.
- **user** (`User!`): The user who made this contribution.

### Language

Represents a given language found in repositories.

**Implements:** Node

**Fields:**

- **color** (`String`): The color defined for the current language.
- **id** (`ID!`): The Node ID of the Language object.
- **name** (`String!`): The name of the current language.

### LockedEvent

Represents a`locked`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the LockedEvent object.
- **lockReason** (`LockReason`): Reason that the conversation was locked (optional).
- **lockable** (`Lockable!`): Object that was locked.

### MarkedAsDuplicateEvent

Represents a`marked_as_duplicate`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **canonical** (`IssueOrPullRequest`): The authoritative issue or pull request which has been duplicated by another.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **duplicate** (`IssueOrPullRequest`): The issue or pull request which has been marked as a duplicate of another.
- **id** (`ID!`): The Node ID of the MarkedAsDuplicateEvent object.
- **isCrossRepository** (`Boolean!`): Canonical and duplicate belong to different repositories.

### MaxFilePathLengthParameters

Prevent commits that include file paths that exceed the specified character limit from being pushed to the commit graph.

**Fields:**

- **maxFilePathLength** (`Int!`): The maximum amount of characters allowed in file paths.

### MaxFileSizeParameters

Prevent commits with individual files that exceed the specified limit from being pushed to the commit graph.

**Fields:**

- **maxFileSize** (`Int!`): The maximum file size allowed in megabytes. This limit does not apply to Git Large File Storage (Git LFS).

### MentionedEvent

Represents a`mentioned`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the MentionedEvent object.

### MergedEvent

Represents a`merged`event on a given pull request.

**Implements:** Node, UniformResourceLocatable

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **commit** (`Commit`): Identifies the commit associated with the `merge` event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the MergedEvent object.
- **mergeRef** (`Ref`): Identifies the Ref associated with the `merge` event.
- **mergeRefName** (`String!`): Identifies the name of the Ref associated with the `merge` event.
- **pullRequest** (`PullRequest!`): PullRequest referenced by event.
- **resourcePath** (`URI!`): The HTTP path for this merged event.
- **url** (`URI!`): The HTTP URL for this merged event.

### MigrationSource

A GitHub Enterprise Importer (GEI) migration source.

**Implements:** Node

**Fields:**

- **id** (`ID!`): The Node ID of the MigrationSource object.
- **name** (`String!`): The migration source name.
- **type** (`MigrationSourceType!`): The migration source type.
- **url** (`URI!`): The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.

### PageInfo

Information about pagination in a connection.

**Fields:**

- **endCursor** (`String`): When paginating forwards, the cursor to continue.
- **hasNextPage** (`Boolean!`): When paginating forwards, are there more items?.
- **hasPreviousPage** (`Boolean!`): When paginating backwards, are there more items?.
- **startCursor** (`String`): When paginating backwards, the cursor to continue.

### PermissionSource

A level of permission and source for a user's access to a repository.

**Fields:**

- **organization** (`Organization!`): The organization the repository belongs to.
- **permission** (`DefaultRepositoryPermissionField!`): The level of access this source has granted to the user.
- **roleName** (`String`): The name of the role this source has granted to the user.
- **source** (`PermissionGranter!`): The source of this permission.

### PinnedEvent

Represents a`pinned`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the PinnedEvent object.
- **issue** (`Issue!`): Identifies the issue associated with the event.

### PropertyTargetDefinition

A property that must match.

**Fields:**

- **name** (`String!`): The name of the property.
- **propertyValues** (`[String!]!`): The values to match for.
- **source** (`String`): The source of the property. Choose`custom`or 'system'. Defaults to 'custom' if not specified.

### RateLimit

Represents the client's rate limit.

**Fields:**

- **cost** (`Int!`): The point cost for the current query counting against the rate limit.
- **limit** (`Int!`): The maximum number of points the client is permitted to consume in a 60 minute window.
- **nodeCount** (`Int!`): The maximum number of nodes this query may return.
- **remaining** (`Int!`): The number of points remaining in the current rate limit window.
- **resetAt** (`DateTime!`): The time at which the current rate limit window resets in UTC epoch seconds.
- **used** (`Int!`): The number of points used in the current rate limit window.

### Reaction

An emoji reaction to a particular piece of content.

**Implements:** Node

**Fields:**

- **content** (`ReactionContent!`): Identifies the emoji reaction.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the Reaction object.
- **reactable** (`Reactable!`): The reactable piece of content.
- **user** (`User`): Identifies the user who created this reaction.

### ReactionGroup

A group of emoji reactions to a particular piece of content.

**Fields:**

- **content** (`ReactionContent!`): Identifies the emoji reaction.
- **createdAt** (`DateTime`): Identifies when the reaction was created.
- **reactors** (`ReactorConnection!`): Reactors to the reaction subject with the emotion represented by this reaction group.
- **subject** (`Reactable!`): The subject that was reacted to.
- **users** (`ReactingUserConnection!`): Users who have reacted to the reaction subject with the emotion represented by this reaction group.
- **viewerHasReacted** (`Boolean!`): Whether or not the authenticated user has left a reaction on the subject.

### RenamedTitleEvent

Represents a`renamed`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **currentTitle** (`String!`): Identifies the current title of the issue or pull request.
- **id** (`ID!`): The Node ID of the RenamedTitleEvent object.
- **previousTitle** (`String!`): Identifies the previous title of the issue or pull request.
- **subject** (`RenamedTitleSubject!`): Subject that was renamed.

### ReopenedEvent

Represents a`reopened`event on any `Closable`.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **closable** (`Closable!`): Object that was reopened.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the ReopenedEvent object.
- **stateReason** (`IssueStateReason`): The reason the issue state was changed to open.

### RequiredReviewerConfiguration

A reviewing team, and file patterns describing which files they must approve changes to.

**Fields:**

- **filePatterns** (`[String!]!`): Array of file patterns. Pull requests which change matching files must be
approved by the specified team. File patterns use fnmatch syntax.
- **minimumApprovals** (`Int!`): Minimum number of approvals required from the specified team. If set to zero,
the team will be added to the pull request but approval is optional.
- **reviewerId** (`ID!`): Node ID of the team which must review changes to matching files.

### RestrictedContribution

Represents a private contribution a user made on GitHub.

**Implements:** Contribution

**Fields:**

- **isRestricted** (`Boolean!`): Whether this contribution is associated with a record you do not have access to. For
example, your own 'first issue' contribution may have been made on a repository you can no
longer access.
- **occurredAt** (`DateTime!`): When this contribution was made.
- **resourcePath** (`URI!`): The HTTP path for this contribution.
- **url** (`URI!`): The HTTP URL for this contribution.
- **user** (`User!`): The user who made this contribution.

### ReviewDismissedEvent

Represents a`review_dismissed`event on a given issue or pull request.

**Implements:** Node, UniformResourceLocatable

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **dismissalMessage** (`String`): Identifies the optional message associated with the`review_dismissed`event.
- **dismissalMessageHTML** (`String`): Identifies the optional message associated with the event, rendered to HTML.
- **id** (`ID!`): The Node ID of the ReviewDismissedEvent object.
- **previousReviewState** (`PullRequestReviewState!`): Identifies the previous state of the review with the`review_dismissed`event.
- **pullRequest** (`PullRequest!`): PullRequest referenced by event.
- **pullRequestCommit** (`PullRequestCommit`): Identifies the commit which caused the review to become stale.
- **resourcePath** (`URI!`): The HTTP path for this review dismissed event.
- **review** (`PullRequestReview`): Identifies the review associated with the`review_dismissed`event.
- **url** (`URI!`): The HTTP URL for this review dismissed event.

### SubscribedEvent

Represents a`subscribed`event on a given `Subscribable`.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the SubscribedEvent object.
- **subscribable** (`Subscribable!`): Object referenced by event.

### TextMatch

A text match within a search result.

**Fields:**

- **fragment** (`String!`): The specific text fragment within the property matched on.
- **highlights** (`[TextMatchHighlight!]!`): Highlights within the matched fragment.
- **property** (`String!`): The property matched on.

### TextMatchHighlight

Represents a single highlight in a search result match.

**Fields:**

- **beginIndice** (`Int!`): The indice in the fragment where the matched text begins.
- **endIndice** (`Int!`): The indice in the fragment where the matched text ends.
- **text** (`String!`): The text matched.

### TransferredEvent

Represents a`transferred`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **fromRepository** (`Repository`): The repository this came from.
- **id** (`ID!`): The Node ID of the TransferredEvent object.
- **issue** (`Issue!`): Identifies the issue associated with the event.

### UnassignedEvent

Represents an`unassigned`event on any assignable object.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **assignable** (`Assignable!`): Identifies the assignable associated with the event.
- **assignee** (`Assignee`): Identifies the user or mannequin that was unassigned.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the UnassignedEvent object.
- **user** (`User`): Identifies the subject (user) who was unassigned.

### UnlabeledEvent

Represents an`unlabeled`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the UnlabeledEvent object.
- **label** (`Label!`): Identifies the label associated with the`unlabeled`event.
- **labelable** (`Labelable!`): Identifies the `Labelable` associated with the event.

### UnlockedEvent

Represents an`unlocked`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the UnlockedEvent object.
- **lockable** (`Lockable!`): Object that was unlocked.

### UnmarkedAsDuplicateEvent

Represents an`unmarked_as_duplicate`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **canonical** (`IssueOrPullRequest`): The authoritative issue or pull request which has been duplicated by another.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **duplicate** (`IssueOrPullRequest`): The issue or pull request which has been marked as a duplicate of another.
- **id** (`ID!`): The Node ID of the UnmarkedAsDuplicateEvent object.
- **isCrossRepository** (`Boolean!`): Canonical and duplicate belong to different repositories.

### UnpinnedEvent

Represents an`unpinned`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the UnpinnedEvent object.
- **issue** (`Issue!`): Identifies the issue associated with the event.

### UnsubscribedEvent

Represents an`unsubscribed`event on a given `Subscribable`.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the UnsubscribedEvent object.
- **subscribable** (`Subscribable!`): Object referenced by event.

### UpdateParameters

Only allow users with bypass permission to update matching refs.

**Fields:**

- **updateAllowsFetchAndMerge** (`Boolean!`): Branch can pull changes from its upstream repository.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **ActorConnection** (4 fields): The connection type for Actor.
- **ActorEdge** (2 fields): An edge in a connection.
- **AssigneeConnection** (4 fields): The connection type for Assignee.
- **AssigneeEdge** (2 fields): An edge in a connection.
- **LanguageConnection** (5 fields): A list of languages associated with the parent.
- **LanguageEdge** (3 fields): Represents the language of a repository.
- **PinnableItemConnection** (4 fields): The connection type for PinnableItem.
- **PinnableItemEdge** (2 fields): An edge in a connection.
- **ReactionConnection** (5 fields): A list of reactions that have been left on the subject.
- **ReactionEdge** (2 fields): An edge in a connection.
- **ReactorConnection** (4 fields): The connection type for Reactor.
- **ReactorEdge** (3 fields): Represents an author of a reaction.
- **RequestedReviewerConnection** (4 fields): The connection type for RequestedReviewer.
- **RequestedReviewerEdge** (2 fields): An edge in a connection.
- **SearchResultItemConnection** (11 fields): A list of results that matched against a search query. Regardless of the number
of matches, a maximum of 1,000 results will be available across all types,
potentially split across many pages.
- **SearchResultItemEdge** (3 fields): An edge in a connection.

## Interfaces

### Actor

Represents an object which can take actions on GitHub. Typically a User or Bot.

**Fields:**

- **avatarUrl** (`URI!`): A URL pointing to the actor's public avatar.
- **login** (`String!`): The username of the actor.
- **resourcePath** (`URI!`): The HTTP path for this actor.
- **url** (`URI!`): The HTTP URL for this actor.

### Agentic

Copilot Agentic fields in context of the current viewer.

**Fields:**

- **viewerCopilotAgentCreatesChannel** (`String`): Channel value for subscribing to live updates for session creations.
- **viewerCopilotAgentLogUpdatesChannel** (`String`): Channel value for subscribing to live updates for session log updates.
- **viewerCopilotAgentTaskUpdatesChannel** (`String`): Channel value for subscribing to live updates for task updates.
- **viewerCopilotAgentUpdatesChannel** (`String`): Channel value for subscribing to live updates for session updates.

### Assignable

An object that can have users assigned to it.

**Fields:**

- **assignedActors** (`AssigneeConnection!`): A list of actors assigned to this object.
- **assignees** (`UserConnection!`): A list of Users assigned to this object.
- **suggestedActors** (`AssigneeConnection!`): A list of suggested actors to assign to this object.

### Closable

An object that can be closed.

**Fields:**

- **closed** (`Boolean!`): Indicates if the object is closed (definition of closed may depend on type).
- **closedAt** (`DateTime`): Identifies the date and time when the object was closed.
- **viewerCanClose** (`Boolean!`): Indicates if the object can be closed by the viewer.
- **viewerCanReopen** (`Boolean!`): Indicates if the object can be reopened by the viewer.

### Comment

Represents a comment.

**Fields:**

- **author** (`Actor`): The actor who authored the comment.
- **authorAssociation** (`CommentAuthorAssociation!`): Author's association with the subject of the comment.
- **body** (`String!`): The body as Markdown.
- **bodyHTML** (`HTML!`): The body rendered to HTML.
- **bodyText** (`String!`): The body rendered to text.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **createdViaEmail** (`Boolean!`): Check if this comment was created via an email reply.
- **editor** (`Actor`): The actor who edited the comment.
- **id** (`ID!`): The Node ID of the Comment object.
- **includesCreatedEdit** (`Boolean!`): Check if this comment was edited and includes an edit with the creation data.
- **lastEditedAt** (`DateTime`): The moment the editor made the last edit.
- **publishedAt** (`DateTime`): Identifies when the comment was published at.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **userContentEdits** (`UserContentEditConnection`): A list of edits to this content.
- **viewerDidAuthor** (`Boolean!`): Did the viewer author this comment.

### Contribution

Represents a contribution a user made on GitHub, such as opening an issue.

**Fields:**

- **isRestricted** (`Boolean!`): Whether this contribution is associated with a record you do not have access to. For
example, your own 'first issue' contribution may have been made on a repository you can no
longer access.
- **occurredAt** (`DateTime!`): When this contribution was made.
- **resourcePath** (`URI!`): The HTTP path for this contribution.
- **url** (`URI!`): The HTTP URL for this contribution.
- **user** (`User!`): The user who made this contribution.

### Deletable

Entities that can be deleted.

**Fields:**

- **viewerCanDelete** (`Boolean!`): Check if the current viewer can delete this object.

### GitObject

Represents a Git object.

**Fields:**

- **abbreviatedOid** (`String!`): An abbreviated version of the Git object ID.
- **commitResourcePath** (`URI!`): The HTTP path for this Git object.
- **commitUrl** (`URI!`): The HTTP URL for this Git object.
- **id** (`ID!`): The Node ID of the GitObject object.
- **oid** (`GitObjectID!`): The Git object ID.
- **repository** (`Repository!`): The Repository the Git object belongs to.

### GitSignature

Information about a signature (GPG or S/MIME) on a Commit or Tag.

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

### Lockable

An object that can be locked.

**Fields:**

- **activeLockReason** (`LockReason`): Reason that the conversation was locked.
- **locked** (`Boolean!`): `true` if the object is locked.

### Migration

Represents a GitHub Enterprise Importer (GEI) migration.

**Fields:**

- **continueOnError** (`Boolean!`): The migration flag to continue on error.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`String`): Identifies the primary key from the database.
- **failureReason** (`String`): The reason the migration failed.
- **id** (`ID!`): The Node ID of the Migration object.
- **migrationLogUrl** (`URI`): The URL for the migration log (expires 1 day after migration completes).
- **migrationSource** (`MigrationSource!`): The migration source.
- **repositoryName** (`String!`): The target repository name.
- **sourceUrl** (`URI!`): The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.
- **state** (`MigrationState!`): The migration state.
- **warningsCount** (`Int!`): The number of warnings encountered for this migration. To review the warnings,
check the [Migration Log](https://docs.github.com/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/accessing-your-migration-logs-for-github-enterprise-importer).

### Minimizable

Entities that can be minimized.

**Fields:**

- **isMinimized** (`Boolean!`): Returns whether or not a comment has been minimized.
- **minimizedReason** (`String`): Returns why the comment was minimized. One of `abuse`, `off-topic`,
`outdated`, `resolved`, `duplicate`, `spam`, and `low-quality`. Note that the
case and formatting of these values differs from the inputs to the
`MinimizeComment` mutation.
- **viewerCanMinimize** (`Boolean!`): Check if the current viewer can minimize this object.
- **viewerCanUnminimize** (`Boolean!`): Check if the current viewer can unminimize this object.

### Node

An object with an ID.

**Fields:**

- **id** (`ID!`): ID of the object.

### Pinnable

Entities that can be pinned.

**Fields:**

- **isPinned** (`Boolean`): Indicates whether or not this entity is currently pinned.
- **pinnedAt** (`DateTime`): Identifies the date and time when this entity was pinned.
- **pinnedBy** (`User`): The user who pinned this entity.
- **viewerCanPin** (`Boolean!`): Check if the current viewer can pin this entity.
- **viewerCanUnpin** (`Boolean!`): Check if the current viewer can unpin this entity.

### ProfileOwner

Represents any entity on GitHub that has a profile page.

**Fields:**

- **anyPinnableItems** (`Boolean!`): Determine if this repository owner has any items that can be pinned to their profile.
- **email** (`String`): The public profile email.
- **id** (`ID!`): The Node ID of the ProfileOwner object.
- **itemShowcase** (`ProfileItemShowcase!`): Showcases a selection of repositories and gists that the profile owner has
either curated or that have been selected automatically based on popularity.
- **location** (`String`): The public profile location.
- **login** (`String!`): The username used to login.
- **name** (`String`): The public profile name.
- **pinnableItems** (`PinnableItemConnection!`): A list of repositories and gists this profile owner can pin to their profile.
- **pinnedItems** (`PinnableItemConnection!`): A list of repositories and gists this profile owner has pinned to their profile.
- **pinnedItemsRemaining** (`Int!`): Returns how many more items this profile owner can pin to their profile.
- **viewerCanChangePinnedItems** (`Boolean!`): Can the viewer pin repositories and gists to the profile?.
- **websiteUrl** (`URI`): The public profile website URL.

### Reactable

Represents a subject that can be reacted on.

**Fields:**

- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the Reactable object.
- **reactionGroups** (`[ReactionGroup!]`): A list of reactions grouped by content left on the subject.
- **reactions** (`ReactionConnection!`): A list of Reactions left on the Issue.
- **viewerCanReact** (`Boolean!`): Can user react to this subject.

### Starrable

Things that can be starred.

**Fields:**

- **id** (`ID!`): The Node ID of the Starrable object.
- **stargazerCount** (`Int!`): Returns a count of how many stargazers there are on this object.
- **stargazers** (`StargazerConnection!`): A list of users who have starred this starrable.
- **viewerHasStarred** (`Boolean!`): Returns a boolean indicating whether the viewing user has starred this starrable.

### Subscribable

Entities that can be subscribed to for web and email notifications.

**Fields:**

- **id** (`ID!`): The Node ID of the Subscribable object.
- **viewerCanSubscribe** (`Boolean!`): Check if the viewer is able to change their subscription status for the repository.
- **viewerSubscription** (`SubscriptionState`): Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

### SubscribableThread

Entities that can be subscribed to for web and email notifications.

**Fields:**

- **id** (`ID!`): The Node ID of the SubscribableThread object.
- **viewerThreadSubscriptionFormAction** (`ThreadSubscriptionFormAction`): Identifies the viewer's thread subscription form action.
- **viewerThreadSubscriptionStatus** (`ThreadSubscriptionState`): Identifies the viewer's thread subscription status.

### UniformResourceLocatable

Represents a type that can be retrieved by a URL.

**Fields:**

- **resourcePath** (`URI!`): The HTML path to this resource.
- **url** (`URI!`): The URL to this resource.

### Updatable

Entities that can be updated.

**Fields:**

- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.

### UpdatableComment

Comments that can be updated.

**Fields:**

- **viewerCannotUpdateReasons** (`[CommentCannotUpdateReason!]!`): Reasons why the current viewer can not update this comment.

### Votable

A subject that may be upvoted.

**Fields:**

- **upvoteCount** (`Int!`): Number of upvotes that this subject has received.
- **viewerCanUpvote** (`Boolean!`): Whether or not the current user can add or remove an upvote on this subject.
- **viewerHasUpvoted** (`Boolean!`): Whether or not the current user has already upvoted this subject.

## Enums

### ActorType

The actor's type.

**Values:**

- `TEAM`: Indicates a team actor.
- `USER`: Indicates a user actor.

### AuditLogOrderField

Properties by which Audit Log connections can be ordered.

**Values:**

- `CREATED_AT`: Order audit log entries by timestamp.

### CheckConclusionState

The possible states for a check suite or run conclusion.

**Values:**

- `ACTION_REQUIRED`: The check suite or run requires action.
- `CANCELLED`: The check suite or run has been cancelled.
- `FAILURE`: The check suite or run has failed.
- `NEUTRAL`: The check suite or run was neutral.
- `SKIPPED`: The check suite or run was skipped.
- `STALE`: The check suite or run was marked stale by GitHub. Only GitHub can use this conclusion.
- `STARTUP_FAILURE`: The check suite or run has failed at startup.
- `SUCCESS`: The check suite or run has succeeded.
- `TIMED_OUT`: The check suite or run has timed out.

### CollaboratorAffiliation

Collaborators affiliation level with a subject.

**Values:**

- `ALL`: All collaborators the authenticated user can see.
- `DIRECT`: All collaborators with permissions to an organization-owned subject, regardless of organization membership status.
- `OUTSIDE`: All outside collaborators of an organization-owned subject.

### CommentAuthorAssociation

A comment author association with repository.

**Values:**

- `COLLABORATOR`: Author has been invited to collaborate on the repository.
- `CONTRIBUTOR`: Author has previously committed to the repository.
- `FIRST_TIMER`: Author has not previously committed to GitHub.
- `FIRST_TIME_CONTRIBUTOR`: Author has not previously committed to the repository.
- `MANNEQUIN`: Author is a placeholder for an unclaimed user.
- `MEMBER`: Author is a member of the organization that owns the repository.
- `NONE`: Author has no association with the repository.
- `OWNER`: Author is the owner of the repository.

### CommentCannotUpdateReason

The possible errors that will prevent a user from updating a comment.

**Values:**

- `ARCHIVED`: Unable to create comment because repository is archived.
- `DENIED`: You cannot update this comment.
- `INSUFFICIENT_ACCESS`: You must be the author or have write access to this repository to update this comment.
- `LOCKED`: Unable to create comment because issue is locked.
- `LOGIN_REQUIRED`: You must be logged in to update this comment.
- `MAINTENANCE`: Repository is under maintenance.
- `VERIFIED_EMAIL_REQUIRED`: At least one email address must be verified to update this comment.

### ContributionLevel

Varying levels of contributions from none to many.

**Values:**

- `FIRST_QUARTILE`: Lowest 25% of days of contributions.
- `FOURTH_QUARTILE`: Highest 25% of days of contributions. More contributions than the third quartile.
- `NONE`: No contributions occurred.
- `SECOND_QUARTILE`: Second lowest 25% of days of contributions. More contributions than the first quartile.
- `THIRD_QUARTILE`: Second highest 25% of days of contributions. More contributions than second quartile, less than the fourth quartile.

### CustomPropertyValueType

The allowed value types for a custom property definition.

**Values:**

- `MULTI_SELECT`: A multi-select value.
- `SINGLE_SELECT`: A single-select value.
- `STRING`: A string value.
- `TRUE_FALSE`: A true/false value.
- `URL`: A URL value.

### DiffSide

The possible sides of a diff.

**Values:**

- `LEFT`: The left side of the diff.
- `RIGHT`: The right side of the diff.

### DismissReason

The possible reasons that a Dependabot alert was dismissed.

**Values:**

- `FIX_STARTED`: A fix has already been started.
- `INACCURATE`: This alert is inaccurate or incorrect.
- `NOT_USED`: Vulnerable code is not actually used.
- `NO_BANDWIDTH`: No bandwidth to fix this.
- `TOLERABLE_RISK`: Risk is tolerable to this project.

### FileViewedState

The possible viewed states of a file .

**Values:**

- `DISMISSED`: The file has new changes since last viewed.
- `UNVIEWED`: The file has not been marked as viewed.
- `VIEWED`: The file has been marked as viewed.

### FundingPlatform

The possible funding platforms for repository funding links.

**Values:**

- `BUY_ME_A_COFFEE`: Buy Me a Coffee funding platform.
- `COMMUNITY_BRIDGE`: Community Bridge funding platform.
- `CUSTOM`: Custom funding platform.
- `GITHUB`: GitHub funding platform.
- `ISSUEHUNT`: IssueHunt funding platform.
- `KO_FI`: Ko-fi funding platform.
- `LFX_CROWDFUNDING`: LFX Crowdfunding funding platform.
- `LIBERAPAY`: Liberapay funding platform.
- `OPEN_COLLECTIVE`: Open Collective funding platform.
- `PATREON`: Patreon funding platform.
- `POLAR`: Polar funding platform.
- `THANKS_DEV`: thanks.dev funding platform.
- `TIDELIFT`: Tidelift funding platform.

### GitSignatureState

The state of a Git signature.

**Values:**

- `BAD_CERT`: The signing certificate or its chain could not be verified.
- `BAD_EMAIL`: Invalid email used for signing.
- `EXPIRED_KEY`: Signing key expired.
- `GPGVERIFY_ERROR`: Internal error - the GPG verification service misbehaved.
- `GPGVERIFY_UNAVAILABLE`: Internal error - the GPG verification service is unavailable at the moment.
- `INVALID`: Invalid signature.
- `MALFORMED_SIG`: Malformed signature.
- `NOT_SIGNING_KEY`: The usage flags for the key that signed this don't allow signing.
- `NO_USER`: Email used for signing not known to GitHub.
- `OCSP_ERROR`: Valid signature, though certificate revocation check failed.
- `OCSP_PENDING`: Valid signature, pending certificate revocation checking.
- `OCSP_REVOKED`: One or more certificates in chain has been revoked.
- `UNKNOWN_KEY`: Key used for signing not known to GitHub.
- `UNKNOWN_SIG_TYPE`: Unknown signature type.
- `UNSIGNED`: Unsigned.
- `UNVERIFIED_EMAIL`: Email used for signing unverified on GitHub.
- `VALID`: Valid signature and verified by GitHub.

### IdentityProviderConfigurationState

The possible states in which authentication can be configured with an identity provider.

**Values:**

- `CONFIGURED`: Authentication with an identity provider is configured but not enforced.
- `ENFORCED`: Authentication with an identity provider is configured and enforced.
- `UNCONFIGURED`: Authentication with an identity provider is not configured.

### LanguageOrderField

Properties by which language connections can be ordered.

**Values:**

- `SIZE`: Order languages by the size of all files containing the language.

### LexicalFallbackReason

Reason why a semantic or hybrid issue search fell back to lexical search.

**Values:**

- `NON_ISSUE_TARGET`: Query targets non-issue types (e.g., pull requests).
- `NO_ACCESSIBLE_REPOS`: Scoped query resolved to zero accessible repositories.
- `NO_TEXT_TERMS`: Query has only qualifiers and no free text terms.
- `ONLY_NON_SEMANTIC_FIELDS_REQUESTED`: Query uses an in: qualifier targeting non-semantic fields.
- `OR_BOOLEAN_NOT_SUPPORTED`: Query contains OR operators (nested boolean qualifiers).
- `QUOTED_TEXT`: Query contains quoted text requiring exact matches.
- `SERVER_ERROR`: Embedding generation failed or timed out.

### LockReason

The possible reasons that an issue or pull request was locked.

**Values:**

- `OFF_TOPIC`: The issue or pull request was locked because the conversation was off-topic.
- `RESOLVED`: The issue or pull request was locked because the conversation was resolved.
- `SPAM`: The issue or pull request was locked because the conversation was spam.
- `TOO_HEATED`: The issue or pull request was locked because the conversation was too heated.

### MergeableState

Whether or not a PullRequest can be merged.

**Values:**

- `CONFLICTING`: The pull request cannot be merged due to merge conflicts.
- `MERGEABLE`: The pull request can be merged.
- `UNKNOWN`: The mergeability of the pull request is still being calculated.

### MigrationSourceType

Represents the different GitHub Enterprise Importer (GEI) migration sources.

**Values:**

- `AZURE_DEVOPS`: An Azure DevOps migration source.
- `BITBUCKET_SERVER`: A Bitbucket Server migration source.
- `GITHUB_ARCHIVE`: A GitHub Migration API source.

### MigrationState

The GitHub Enterprise Importer (GEI) migration state.

**Values:**

- `FAILED`: The migration has failed.
- `FAILED_VALIDATION`: The migration has invalid credentials.
- `IN_PROGRESS`: The migration is in progress.
- `NOT_STARTED`: The migration has not started.
- `PENDING_VALIDATION`: The migration needs to have its credentials validated.
- `QUEUED`: The migration has been queued.
- `SUCCEEDED`: The migration has succeeded.

### NotificationRestrictionSettingValue

The possible values for the notification restriction setting.

**Values:**

- `DISABLED`: The setting is disabled for the owner.
- `ENABLED`: The setting is enabled for the owner.

### OperationType

The corresponding operation type for the action.

**Values:**

- `ACCESS`: An existing resource was accessed.
- `AUTHENTICATION`: A resource performed an authentication event.
- `CREATE`: A new resource was created.
- `MODIFY`: An existing resource was modified.
- `REMOVE`: An existing resource was removed.
- `RESTORE`: An existing resource was restored.
- `TRANSFER`: An existing resource was transferred between multiple resources.

### OrderDirection

Possible directions in which to order a list of items when provided an `orderBy` argument.

**Values:**

- `ASC`: Specifies an ascending order for a given `orderBy` argument.
- `DESC`: Specifies a descending order for a given `orderBy` argument.

### PinnableItemType

Represents items that can be pinned to a profile page or dashboard.

**Values:**

- `GIST`: A gist.
- `ISSUE`: An issue.
- `ORGANIZATION`: An organization.
- `PROJECT`: A project.
- `PULL_REQUEST`: A pull request.
- `REPOSITORY`: A repository.
- `TEAM`: A team.
- `USER`: A user.

### ReactionContent

Emojis that can be attached to Issues, Pull Requests and Comments.

**Values:**

- `CONFUSED`: Represents the `:confused:` emoji.
- `EYES`: Represents the `:eyes:` emoji.
- `HEART`: Represents the `:heart:` emoji.
- `HOORAY`: Represents the `:hooray:` emoji.
- `LAUGH`: Represents the `:laugh:` emoji.
- `ROCKET`: Represents the `:rocket:` emoji.
- `THUMBS_DOWN`: Represents the `:-1:` emoji.
- `THUMBS_UP`: Represents the `:+1:` emoji.

### ReactionOrderField

A list of fields that reactions can be ordered by.

**Values:**

- `CREATED_AT`: Allows ordering a list of reactions by when they were created.

### RuleEnforcement

The level of enforcement for a rule or ruleset.

**Values:**

- `ACTIVE`: Rules will be enforced.
- `DISABLED`: Do not evaluate or enforce rules.
- `EVALUATE`: Allow admins to test rules before enforcing them. Admins can view insights on
the Rule Insights page (`evaluate` is only available with GitHub Enterprise).

### SamlDigestAlgorithm

The possible digest algorithms used to sign SAML requests for an identity provider.

**Values:**

- `SHA1`: SHA1.
- `SHA256`: SHA256.
- `SHA384`: SHA384.
- `SHA512`: SHA512.

### SamlSignatureAlgorithm

The possible signature algorithms used to sign SAML requests for a Identity Provider.

**Values:**

- `RSA_SHA1`: RSA-SHA1.
- `RSA_SHA256`: RSA-SHA256.
- `RSA_SHA384`: RSA-SHA384.
- `RSA_SHA512`: RSA-SHA512.

### SearchType

Represents the individual results of a search.

**Values:**

- `DISCUSSION`: Returns matching discussions in repositories.
- `ISSUE`: Returns results matching issues in repositories.
- `ISSUE_ADVANCED`: Returns results matching issues in repositories.
- `ISSUE_HYBRID`: Returns results matching issues using hybrid (lexical + semantic) search.
- `ISSUE_SEMANTIC`: Returns results matching issues using semantic search.
- `REPOSITORY`: Returns results matching repositories.
- `USER`: Returns results matching users and organizations on GitHub.

### StarOrderField

Properties by which star connections can be ordered.

**Values:**

- `STARRED_AT`: Allows ordering a list of stars by when they were created.

### SubscriptionState

The possible states of a subscription.

**Values:**

- `IGNORED`: The User is never notified.
- `SUBSCRIBED`: The User is notified of all conversations.
- `UNSUBSCRIBED`: The User is only notified when participating or @mentioned.

### ThreadSubscriptionFormAction

The possible states of a thread subscription form action.

**Values:**

- `NONE`: The User cannot subscribe or unsubscribe to the thread.
- `SUBSCRIBE`: The User can subscribe to the thread.
- `UNSUBSCRIBE`: The User can unsubscribe to the thread.

### ThreadSubscriptionState

The possible states of a subscription.

**Values:**

- `DISABLED`: The subscription status is currently disabled.
- `IGNORING_LIST`: The User is never notified because they are ignoring the list.
- `IGNORING_THREAD`: The User is never notified because they are ignoring the thread.
- `NONE`: The User is not recieving notifications from this thread.
- `SUBSCRIBED_TO_LIST`: The User is notified becuase they are watching the list.
- `SUBSCRIBED_TO_THREAD`: The User is notified because they are subscribed to the thread.
- `SUBSCRIBED_TO_THREAD_EVENTS`: The User is notified because they chose custom settings for this thread.
- `SUBSCRIBED_TO_THREAD_TYPE`: The User is notified because they chose custom settings for this thread.
- `UNAVAILABLE`: The subscription status is currently unavailable.

### TwoFactorCredentialSecurityType

Filters by whether or not 2FA is enabled and if the method configured is considered secure or insecure.

**Values:**

- `DISABLED`: No method of two-factor authentication.
- `INSECURE`: Has an insecure method of two-factor authentication. GitHub currently defines this as SMS two-factor authentication.
- `SECURE`: Has only secure methods of two-factor authentication.

## Input Objects

### AbortQueuedMigrationsInput

Autogenerated input type of AbortQueuedMigrations.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ownerId** (`ID!`): The ID of the organization that is running the migrations.

### AddAssigneesToAssignableInput

Autogenerated input type of AddAssigneesToAssignable.

**Input fields:**

- **agentAssignment** (`AgentAssignmentInput`): Configuration for assigning Copilot to this issue.
- **assignableId** (`ID!`): The id of the assignable object to add assignees to.
- **assigneeIds** (`[ID!]!`): The ids of actors (users or bots) to add as assignees.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### AddBlockedByInput

Autogenerated input type of AddBlockedBy.

**Input fields:**

- **blockingIssueId** (`ID!`): The ID of the issue that blocks the given issue.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The ID of the issue to be blocked.

### AddCommentInput

Autogenerated input type of AddComment.

**Input fields:**

- **body** (`String!`): The contents of the comment.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **subjectId** (`ID!`): The Node ID of the subject to modify.

### AddReactionInput

Autogenerated input type of AddReaction.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **content** (`ReactionContent!`): The name of the emoji to react with.
- **subjectId** (`ID!`): The Node ID of the subject to modify.

### AddStarInput

Autogenerated input type of AddStar.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **starrableId** (`ID!`): The Starrable ID to star.

### AddUpvoteInput

Autogenerated input type of AddUpvote.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **subjectId** (`ID!`): The Node ID of the discussion or comment to upvote.

### AgentAssignmentInput

Represents configuration for assigning Copilot to an issue (public variant).

**Input fields:**

- **baseRef** (`String`): The base ref/branch for the repository. Defaults to the default branch if not provided.
- **customAgent** (`String`): Custom agent for Copilot.
- **customInstructions** (`String`): Custom instructions for Copilot.
- **targetRepositoryId** (`ID`): The Node ID of the target repository where Copilot should work. Defaults to the issue's repository if not provided.

### AuditLogOrder

Ordering options for Audit Log connections.

**Input fields:**

- **direction** (`OrderDirection`): The ordering direction.
- **field** (`AuditLogOrderField`): The field to order Audit Logs by.

### BranchNamePatternParametersInput

Parameters to be used for the branch_name_pattern rule.

**Input fields:**

- **name** (`String`): How this rule appears when configuring it.
- **negate** (`Boolean`): If true, the rule will fail if the pattern matches.
- **operator** (`String!`): The operator to use for matching.
- **pattern** (`String!`): The pattern to match with.

### ContributionOrder

Ordering options for contribution connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.

### CopilotCodeReviewParametersInput

Request Copilot code review for new pull requests automatically if the author
has access to Copilot code review and their premium requests quota has not
reached the limit.

**Input fields:**

- **reviewDraftPullRequests** (`Boolean`): Copilot automatically reviews draft pull requests before they are marked as ready for review.
- **reviewOnPush** (`Boolean`): Copilot automatically reviews each new push to the pull request.

### CreateAttributionInvitationInput

Autogenerated input type of CreateAttributionInvitation.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ownerId** (`ID!`): The Node ID of the owner scoping the reattributable data.
- **sourceId** (`ID!`): The Node ID of the account owning the data to reattribute.
- **targetId** (`ID!`): The Node ID of the account which may claim the data.

### CreateMigrationSourceInput

Autogenerated input type of CreateMigrationSource.

**Input fields:**

- **accessToken** (`String`): The migration source access token.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **githubPat** (`String`): The GitHub personal access token of the user importing to the target repository.
- **name** (`String!`): The migration source name.
- **ownerId** (`ID!`): The ID of the organization that will own the migration source.
- **type** (`MigrationSourceType!`): The migration source type.
- **url** (`String`): The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.

### CustomPropertyValueInput

The custom property name and value to be set.

**Input fields:**

- **propertyName** (`String!`): The name of the custom property.
- **value** (`CustomPropertyValue`): The value to set for the custom property. Using a value of null will unset the
property value, reverting to the default value if the property is required.

### FileAddition

A command to add a file at the given path with the given contents as part of a
commit.  Any existing file at that that path will be replaced.

**Input fields:**

- **contents** (`Base64String!`): The base64 encoded contents of the file.
- **path** (`String!`): The path in the repository where the file will be located.

### FileChanges

A description of a set of changes to a file tree to be made as part of
a git commit, modeled as zero or more file `additions` and zero or more
file `deletions`.
Both fields are optional; omitting both will produce a commit with no
file changes.
`deletions` and `additions` describe changes to files identified
by their path in the git tree using unix-style path separators, i.e.
`/`.  The root of a git tree is an empty string, so paths are not
slash-prefixed.
`path` values must be unique across all `additions` and `deletions`
provided.  Any duplication will result in a validation error.
Encoding
File contents must be provided in full for each `FileAddition`.
The `contents` of a `FileAddition` must be encoded using RFC 4648
compliant base64, i.e. correct padding is required and no characters
outside the standard alphabet may be used.  Invalid base64
encoding will be rejected with a validation error.
The encoded contents may be binary.
For text files, no assumptions are made about the character encoding of
the file contents (after base64 decoding).  No charset transcoding or
line-ending normalization will be performed; it is the client's
responsibility to manage the character encoding of files they provide.
However, for maximum compatibility we recommend using UTF-8 encoding
and ensuring that all files in a repository use a consistent
line-ending convention (`\n` or `\r\n`), and that all files end
with a newline.
Modeling file changes
Each of the the five types of conceptual changes that can be made in a
git commit can be described using the `FileChanges` type as follows:


New file addition: create file `hello world\n` at path `docs/README.txt`:
`{
  "additions" [
    {
      "path": "docs/README.txt",
      "contents": base64encode("hello world\n")
    }
  ]
}
`


Existing file modification: change existing `docs/README.txt` to have new
content `new content here\n`:
`{
  "additions" [
    {
      "path": "docs/README.txt",
      "contents": base64encode("new content here\n")
    }
  ]
}
`


Existing file deletion: remove existing file `docs/README.txt`.
Note that the path is required to exist -- specifying a
path that does not exist on the given branch will abort the
commit and return an error.
`{
  "deletions" [
    {
      "path": "docs/README.txt"
    }
  ]
}
`


File rename with no changes: rename `docs/README.txt` with
previous content `hello world\n` to the same content at
`newdocs/README.txt`:
`{
  "deletions" [
    {
      "path": "docs/README.txt",
    }
  ],
  "additions" [
    {
      "path": "newdocs/README.txt",
      "contents": base64encode("hello world\n")
    }
  ]
}
`


File rename with changes: rename `docs/README.txt` with
previous content `hello world\n` to a file at path
`newdocs/README.txt` with content `new contents\n`:
`{
  "deletions" [
    {
      "path": "docs/README.txt",
    }
  ],
  "additions" [
    {
      "path": "newdocs/README.txt",
      "contents": base64encode("new contents\n")
    }
  ]
}.
`

**Input fields:**

- **additions** (`[FileAddition!]`): File to add or change.
- **deletions** (`[FileDeletion!]`): Files to delete.

### FileDeletion

A command to delete the file at the given path as part of a commit.

**Input fields:**

- **path** (`String!`): The path to delete.

### FileExtensionRestrictionParametersInput

Prevent commits that include files with specified file extensions from being pushed to the commit graph.

**Input fields:**

- **restrictedFileExtensions** (`[String!]!`): The file extensions that are restricted from being pushed to the commit graph.

### FilePathRestrictionParametersInput

Prevent commits that include changes in specified file and folder paths from
being pushed to the commit graph. This includes absolute paths that contain file names.

**Input fields:**

- **restrictedFilePaths** (`[String!]!`): The file paths that are restricted from being pushed to the commit graph.

### GrantMigratorRoleInput

Autogenerated input type of GrantMigratorRole.

**Input fields:**

- **actor** (`String!`): The user login or Team slug to grant the migrator role.
- **actorType** (`ActorType!`): Specifies the type of the actor, can be either USER or TEAM.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organizationId** (`ID!`): The ID of the organization that the user/team belongs to.

### LanguageOrder

Ordering options for language connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`LanguageOrderField!`): The field to order languages by.

### LockLockableInput

Autogenerated input type of LockLockable.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **lockReason** (`LockReason`): A reason for why the item will be locked.
- **lockableId** (`ID!`): ID of the item to be locked.

### MarkFileAsViewedInput

Autogenerated input type of MarkFileAsViewed.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **path** (`String!`): The path of the file to mark as viewed.
- **pullRequestId** (`ID!`): The Node ID of the pull request.

### MaxFilePathLengthParametersInput

Prevent commits that include file paths that exceed the specified character limit from being pushed to the commit graph.

**Input fields:**

- **maxFilePathLength** (`Int!`): The maximum amount of characters allowed in file paths.

### MaxFileSizeParametersInput

Prevent commits with individual files that exceed the specified limit from being pushed to the commit graph.

**Input fields:**

- **maxFileSize** (`Int!`): The maximum file size allowed in megabytes. This limit does not apply to Git Large File Storage (Git LFS).

### MergeBranchInput

Autogenerated input type of MergeBranch.

**Input fields:**

- **authorEmail** (`String`): The email address to associate with this commit.
- **base** (`String!`): The name of the base branch that the provided head will be merged into.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **commitMessage** (`String`): Message to use for the merge commit. If omitted, a default will be used.
- **head** (`String!`): The head to merge into the base branch. This can be a branch name or a commit GitObjectID.
- **repositoryId** (`ID!`): The Node ID of the Repository containing the base branch that will be modified.

### MinimizeCommentInput

Autogenerated input type of MinimizeComment.

**Input fields:**

- **classifier** (`ReportedContentClassifiers!`): The classification of comment.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **subjectId** (`ID!`): The Node ID of the subject to modify.

### PropertyTargetDefinitionInput

A property that must match.

**Input fields:**

- **name** (`String!`): The name of the property.
- **propertyValues** (`[String!]!`): The values to match for.
- **source** (`String`): The source of the property. Choose`custom`or 'system'. Defaults to 'custom' if not specified.

### ReactionOrder

Ways in which lists of reactions can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order reactions by the specified field.
- **field** (`ReactionOrderField!`): The field in which to order reactions by.

### RemoveAssigneesFromAssignableInput

Autogenerated input type of RemoveAssigneesFromAssignable.

**Input fields:**

- **assignableId** (`ID!`): The id of the assignable object to remove assignees from.
- **assigneeIds** (`[ID!]!`): The ids of actors to remove as assignees.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### RemoveBlockedByInput

Autogenerated input type of RemoveBlockedBy.

**Input fields:**

- **blockingIssueId** (`ID!`): The ID of the blocking issue.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **issueId** (`ID!`): The ID of the blocked issue.

### RemoveOutsideCollaboratorInput

Autogenerated input type of RemoveOutsideCollaborator.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organizationId** (`ID!`): The ID of the organization to remove the outside collaborator from.
- **userId** (`ID!`): The ID of the outside collaborator to remove.

### RemoveReactionInput

Autogenerated input type of RemoveReaction.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **content** (`ReactionContent!`): The name of the emoji reaction to remove.
- **subjectId** (`ID!`): The Node ID of the subject to modify.

### RemoveStarInput

Autogenerated input type of RemoveStar.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **starrableId** (`ID!`): The Starrable ID to unstar.

### RemoveUpvoteInput

Autogenerated input type of RemoveUpvote.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **subjectId** (`ID!`): The Node ID of the discussion or comment to remove upvote.

### ReplaceActorsForAssignableInput

Autogenerated input type of ReplaceActorsForAssignable.

**Input fields:**

- **actorIds** (`[ID!]`): The ids of the actors to replace the existing assignees. May be used as an
alternative to or in conjunction with actorLogins.
- **actorLogins** (`[String!]`): The usernames of the actors to replace the existing assignees. May be used as
an alternative to or in conjunction with actorIds. For bots, use the login
format with [bot] suffix (e.g., 'my-app[bot]').
- **agentAssignment** (`AgentAssignmentInput`): Configuration for assigning an AI agent to this issue.
- **assignableId** (`ID!`): The id of the assignable object to replace the assignees for.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### RequestReviewsByLoginInput

Autogenerated input type of RequestReviewsByLogin.

**Input fields:**

- **botLogins** (`[String!]`): The logins of the bots to request reviews from, including the [bot] suffix (e.g., 'copilot-pull-request-reviewer[bot]').
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **pullRequestId** (`ID!`): The Node ID of the pull request to modify.
- **teamSlugs** (`[String!]`): The slugs of the teams to request reviews from (format: 'org/team-slug').
- **union** (`Boolean`): Add users to the set rather than replace.
- **userLogins** (`[String!]`): The login strings of the users to request reviews from.

### RequestReviewsInput

Autogenerated input type of RequestReviews.

**Input fields:**

- **botIds** (`[ID!]`): The Node IDs of the bot to request.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **pullRequestId** (`ID!`): The Node ID of the pull request to modify.
- **teamIds** (`[ID!]`): The Node IDs of the team to request.
- **union** (`Boolean`): Add users to the set rather than replace.
- **userIds** (`[ID!]`): The Node IDs of the user to request.

### RequiredReviewerConfigurationInput

A reviewing team, and file patterns describing which files they must approve changes to.

**Input fields:**

- **filePatterns** (`[String!]!`): Array of file patterns. Pull requests which change matching files must be
approved by the specified team. File patterns use fnmatch syntax.
- **minimumApprovals** (`Int!`): Minimum number of approvals required from the specified team. If set to zero,
the team will be added to the pull request but approval is optional.
- **reviewerId** (`ID!`): Node ID of the team which must review changes to matching files.

### ResolveReviewThreadInput

Autogenerated input type of ResolveReviewThread.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **threadId** (`ID!`): The ID of the thread to resolve.

### RevokeMigratorRoleInput

Autogenerated input type of RevokeMigratorRole.

**Input fields:**

- **actor** (`String!`): The user login or Team slug to revoke the migrator role from.
- **actorType** (`ActorType!`): Specifies the type of the actor, can be either USER or TEAM.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organizationId** (`ID!`): The ID of the organization that the user/team belongs to.

### RuleParametersInput

Specifies the parameters for a `RepositoryRule` object. Only one of the fields should be specified.

**Input fields:**

- **branchNamePattern** (`BranchNamePatternParametersInput`): Parameters used for the `branch_name_pattern` rule type.
- **codeScanning** (`CodeScanningParametersInput`): Parameters used for the `code_scanning` rule type.
- **commitAuthorEmailPattern** (`CommitAuthorEmailPatternParametersInput`): Parameters used for the `commit_author_email_pattern` rule type.
- **commitMessagePattern** (`CommitMessagePatternParametersInput`): Parameters used for the `commit_message_pattern` rule type.
- **committerEmailPattern** (`CommitterEmailPatternParametersInput`): Parameters used for the `committer_email_pattern` rule type.
- **copilotCodeReview** (`CopilotCodeReviewParametersInput`): Parameters used for the `copilot_code_review` rule type.
- **fileExtensionRestriction** (`FileExtensionRestrictionParametersInput`): Parameters used for the `file_extension_restriction` rule type.
- **filePathRestriction** (`FilePathRestrictionParametersInput`): Parameters used for the `file_path_restriction` rule type.
- **maxFilePathLength** (`MaxFilePathLengthParametersInput`): Parameters used for the `max_file_path_length` rule type.
- **maxFileSize** (`MaxFileSizeParametersInput`): Parameters used for the `max_file_size` rule type.
- **mergeQueue** (`MergeQueueParametersInput`): Parameters used for the `merge_queue` rule type.
- **pullRequest** (`PullRequestParametersInput`): Parameters used for the `pull_request` rule type.
- **requiredDeployments** (`RequiredDeploymentsParametersInput`): Parameters used for the `required_deployments` rule type.
- **requiredStatusChecks** (`RequiredStatusChecksParametersInput`): Parameters used for the `required_status_checks` rule type.
- **tagNamePattern** (`TagNamePatternParametersInput`): Parameters used for the `tag_name_pattern` rule type.
- **update** (`UpdateParametersInput`): Parameters used for the `update` rule type.
- **workflows** (`WorkflowsParametersInput`): Parameters used for the `workflows` rule type.

### StarOrder

Ways in which star connections can be ordered.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order nodes.
- **field** (`StarOrderField!`): The field in which to order nodes by.

### UnlockLockableInput

Autogenerated input type of UnlockLockable.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **lockableId** (`ID!`): ID of the item to be unlocked.

### UnmarkFileAsViewedInput

Autogenerated input type of UnmarkFileAsViewed.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **path** (`String!`): The path of the file to mark as unviewed.
- **pullRequestId** (`ID!`): The Node ID of the pull request.

### UnminimizeCommentInput

Autogenerated input type of UnminimizeComment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **subjectId** (`ID!`): The Node ID of the subject to modify.

### UnresolveReviewThreadInput

Autogenerated input type of UnresolveReviewThread.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **threadId** (`ID!`): The ID of the thread to unresolve.

### UpdateNotificationRestrictionSettingInput

Autogenerated input type of UpdateNotificationRestrictionSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ownerId** (`ID!`): The ID of the owner on which to set the restrict notifications setting.
- **settingValue** (`NotificationRestrictionSettingValue!`): The value for the restrict notifications setting.

### UpdateParametersInput

Only allow users with bypass permission to update matching refs.

**Input fields:**

- **updateAllowsFetchAndMerge** (`Boolean!`): Branch can pull changes from its upstream repository.

### UpdateSubscriptionInput

Autogenerated input type of UpdateSubscription.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **state** (`SubscriptionState!`): The new state of the subscription.
- **subscribableId** (`ID!`): The Node ID of the subscribable object to modify.

## Unions

### Assignee

Types that can be assigned to issues.

**Possible types:** Bot, Mannequin, Organization, User

### BranchActorAllowanceActor

Types which can be actors for `BranchActorAllowance` objects.

**Possible types:** App, Team, User

### BypassActor

Types that can represent a repository ruleset bypass actor.

**Possible types:** App, Team, User

### Claimable

An object which can have its data claimed or claim data from another.

**Possible types:** Mannequin, User

### Closer

The object which triggered a `ClosedEvent`.

**Possible types:** Commit, ProjectV2, PullRequest

### CustomPropertySource

Sources which can have custom properties defined.

**Possible types:** Enterprise, Organization

### PermissionGranter

Types that can grant permissions on a repository to a user.

**Possible types:** Organization, Repository, Team

### PinnableItem

Types that can be pinned to a profile page.

**Possible types:** Gist, Repository

### Reactor

Types that can be assigned to reactions.

**Possible types:** Bot, Mannequin, Organization, User

### RenamedTitleSubject

An object which has a renamable title.

**Possible types:** Issue, PullRequest

### RequestedReviewer

Types that can be requested reviewers.

**Possible types:** Bot, Mannequin, Team, User

### RuleParameters

Types which can be parameters for `RepositoryRule` objects.

**Possible types:** BranchNamePatternParameters, CodeScanningParameters, CommitAuthorEmailPatternParameters, CommitMessagePatternParameters, CommitterEmailPatternParameters, CopilotCodeReviewParameters, FileExtensionRestrictionParameters, FilePathRestrictionParameters, MaxFilePathLengthParameters, MaxFileSizeParameters, MergeQueueParameters, PullRequestParameters, RequiredDeploymentsParameters, RequiredStatusChecksParameters, TagNamePatternParameters, UpdateParameters, WorkflowsParameters

### RuleSource

Types which can have `RepositoryRule` objects.

**Possible types:** Enterprise, Organization, Repository

### SearchResultItem

The results of a search.

**Possible types:** App, Discussion, Issue, MarketplaceListing, Organization, PullRequest, Repository, User
