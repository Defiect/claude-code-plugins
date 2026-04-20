# GitHub Actions, CI & Deployments

## Mutations

### approveDeployments

Approve all pending deployments under one or more environments.

**Input fields:**

- **input** (`ApproveDeploymentsInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deployments** (`[Deployment!]`): The affected deployments.

### createCheckRun

Create a check run.

**Input fields:**

- **input** (`CreateCheckRunInput!`)

**Return fields:**

- **checkRun** (`CheckRun`): The newly created check run.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### createCheckSuite

Create a check suite.

**Input fields:**

- **input** (`CreateCheckSuiteInput!`)

**Return fields:**

- **checkSuite** (`CheckSuite`): The newly created check suite.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### createDeployment

Creates a new deployment event.

**Input fields:**

- **input** (`CreateDeploymentInput!`)

**Return fields:**

- **autoMerged** (`Boolean`): True if the default branch has been auto-merged into the deployment ref.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deployment** (`Deployment`): The new deployment.

### createDeploymentStatus

Create a deployment status.

**Input fields:**

- **input** (`CreateDeploymentStatusInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deploymentStatus** (`DeploymentStatus`): The new deployment status.

### createEnvironment

Creates an environment or simply returns it if already exists.

**Input fields:**

- **input** (`CreateEnvironmentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **environment** (`Environment`): The new or existing environment.

### deleteDeployment

Deletes a deployment.

**Input fields:**

- **input** (`DeleteDeploymentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### deleteEnvironment

Deletes an environment.

**Input fields:**

- **input** (`DeleteEnvironmentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### pinEnvironment

Pin an environment to a repository.

**Input fields:**

- **input** (`PinEnvironmentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **environment** (`Environment`): The environment that was pinned.
- **pinnedEnvironment** (`PinnedEnvironment`): The pinned environment if we pinned.

### rejectDeployments

Reject all pending deployments under one or more environments.

**Input fields:**

- **input** (`RejectDeploymentsInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deployments** (`[Deployment!]`): The affected deployments.

### reorderEnvironment

Reorder a pinned repository environment.

**Input fields:**

- **input** (`ReorderEnvironmentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **environment** (`Environment`): The environment that was reordered.

### rerequestCheckSuite

Rerequests an existing check suite.

**Input fields:**

- **input** (`RerequestCheckSuiteInput!`)

**Return fields:**

- **checkSuite** (`CheckSuite`): The requested check suite.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### updateCheckRun

Update a check run.

**Input fields:**

- **input** (`UpdateCheckRunInput!`)

**Return fields:**

- **checkRun** (`CheckRun`): The updated check run.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### updateEnvironment

Updates an environment.

**Input fields:**

- **input** (`UpdateEnvironmentInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **environment** (`Environment`): The updated environment.

## Types

### CheckAnnotation

A single check annotation.

**Fields:**

- **annotationLevel** (`CheckAnnotationLevel`): The annotation's severity level.
- **blobUrl** (`URI!`): The path to the file that this annotation was made on.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **location** (`CheckAnnotationSpan!`): The position of this annotation.
- **message** (`String!`): The annotation's message.
- **path** (`String!`): The path that this annotation was made on.
- **rawDetails** (`String`): Additional information about the annotation.
- **title** (`String`): The annotation's title.

### CheckAnnotationPosition

A character position in a check annotation.

**Fields:**

- **column** (`Int`): Column number (1 indexed).
- **line** (`Int!`): Line number (1 indexed).

### CheckAnnotationSpan

An inclusive pair of positions for a check annotation.

**Fields:**

- **end** (`CheckAnnotationPosition!`): End position (inclusive).
- **start** (`CheckAnnotationPosition!`): Start position (inclusive).

### CheckRun

A check run.

**Implements:** Node, RequirableByPullRequest, UniformResourceLocatable

**Fields:**

- **annotations** (`CheckAnnotationConnection`): The check run's annotations.
- **checkSuite** (`CheckSuite!`): The check suite that this run is a part of.
- **completedAt** (`DateTime`): Identifies the date and time when the check run was completed.
- **conclusion** (`CheckConclusionState`): The conclusion of the check run.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **deployment** (`Deployment`): The corresponding deployment for this job, if any.
- **detailsUrl** (`URI`): The URL from which to find full details of the check run on the integrator's site.
- **externalId** (`String`): A reference for the check run on the integrator's system.
- **id** (`ID!`): The Node ID of the CheckRun object.
- **isRequired** (`Boolean!`): Whether this is required to pass before merging for a specific pull request.
- **name** (`String!`): The name of the check for this check run.
- **pendingDeploymentRequest** (`DeploymentRequest`): Information about a pending deployment, if any, in this check run.
- **permalink** (`URI!`): The permalink to the check run summary.
- **repository** (`Repository!`): The repository associated with this check run.
- **resourcePath** (`URI!`): The HTTP path for this check run.
- **startedAt** (`DateTime`): Identifies the date and time when the check run was started.
- **status** (`CheckStatusState!`): The current status of the check run.
- **steps** (`CheckStepConnection`): The check run's steps.
- **summary** (`String`): A string representing the check run's summary.
- **text** (`String`): A string representing the check run's text.
- **title** (`String`): A string representing the check run.
- **url** (`URI!`): The HTTP URL for this check run.

### CheckRunStateCount

Represents a count of the state of a check run.

**Fields:**

- **count** (`Int!`): The number of check runs with this state.
- **state** (`CheckRunState!`): The state of a check run.

### CheckStep

A single check step.

**Fields:**

- **completedAt** (`DateTime`): Identifies the date and time when the check step was completed.
- **conclusion** (`CheckConclusionState`): The conclusion of the check step.
- **externalId** (`String`): A reference for the check step on the integrator's system.
- **name** (`String!`): The step's name.
- **number** (`Int!`): The index of the step in the list of steps of the parent check run.
- **secondsToCompletion** (`Int`): Number of seconds to completion.
- **startedAt** (`DateTime`): Identifies the date and time when the check step was started.
- **status** (`CheckStatusState!`): The current status of the check step.

### CheckSuite

A check suite.

**Implements:** Node

**Fields:**

- **app** (`App`): The GitHub App which created this check suite.
- **branch** (`Ref`): The name of the branch for this check suite.
- **checkRuns** (`CheckRunConnection`): The check runs associated with a check suite.
- **commit** (`Commit!`): The commit for this check suite.
- **conclusion** (`CheckConclusionState`): The conclusion of this check suite.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`User`): The user who triggered the check suite.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the CheckSuite object.
- **matchingPullRequests** (`PullRequestConnection`): A list of open pull requests matching the check suite.
- **push** (`Push`): The push that triggered this check suite.
- **repository** (`Repository!`): The repository associated with this check suite.
- **resourcePath** (`URI!`): The HTTP path for this check suite.
- **status** (`CheckStatusState!`): The status of this check suite.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this check suite.
- **workflowRun** (`WorkflowRun`): The workflow run associated with this check suite.

### Deployment

Represents triggered deployment instance.

**Implements:** Node

**Fields:**

- **commit** (`Commit`): Identifies the commit sha of the deployment.
- **commitOid** (`String!`): Identifies the oid of the deployment commit, even if the commit has been deleted.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor!`): Identifies the actor who triggered the deployment.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **description** (`String`): The deployment description.
- **environment** (`String`): The latest environment to which this deployment was made.
- **id** (`ID!`): The Node ID of the Deployment object.
- **latestEnvironment** (`String`): The latest environment to which this deployment was made.
- **latestStatus** (`DeploymentStatus`): The latest status of this deployment.
- **originalEnvironment** (`String`): The original environment to which this deployment was made.
- **payload** (`String`): Extra information that a deployment system might need.
- **ref** (`Ref`): Identifies the Ref of the deployment, if the deployment was created by ref.
- **repository** (`Repository!`): Identifies the repository associated with the deployment.
- **state** (`DeploymentState`): The current state of the deployment.
- **statuses** (`DeploymentStatusConnection`): A list of statuses associated with the deployment.
- **task** (`String`): The deployment task.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### DeploymentEnvironmentChangedEvent

Represents a`deployment_environment_changed`event on a given pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **deploymentStatus** (`DeploymentStatus!`): The deployment status that updated the deployment environment.
- **id** (`ID!`): The Node ID of the DeploymentEnvironmentChangedEvent object.
- **pullRequest** (`PullRequest!`): PullRequest referenced by event.

### DeploymentProtectionRule

A protection rule.

**Fields:**

- **databaseId** (`Int`): Identifies the primary key from the database.
- **preventSelfReview** (`Boolean`): Whether deployments to this environment can be approved by the user who created the deployment.
- **reviewers** (`DeploymentReviewerConnection!`): The teams or users that can review the deployment.
- **timeout** (`Int!`): The timeout in minutes for this protection rule.
- **type** (`DeploymentProtectionRuleType!`): The type of protection rule.

### DeploymentRequest

A request to deploy a workflow run to an environment.

**Fields:**

- **currentUserCanApprove** (`Boolean!`): Whether or not the current user can approve the deployment.
- **environment** (`Environment!`): The target environment of the deployment.
- **reviewers** (`DeploymentReviewerConnection!`): The teams or users that can review the deployment.
- **waitTimer** (`Int!`): The wait timer in minutes configured in the environment.
- **waitTimerStartedAt** (`DateTime`): The wait timer in minutes configured in the environment.

### DeploymentReview

A deployment review.

**Implements:** Node

**Fields:**

- **comment** (`String!`): The comment the user left.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **environments** (`EnvironmentConnection!`): The environments approved or rejected.
- **id** (`ID!`): The Node ID of the DeploymentReview object.
- **state** (`DeploymentReviewState!`): The decision of the user.
- **user** (`User!`): The user that reviewed the deployment.

### DeploymentStatus

Describes the status of a given deployment attempt.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor!`): Identifies the actor who triggered the deployment.
- **deployment** (`Deployment!`): Identifies the deployment associated with status.
- **description** (`String`): Identifies the description of the deployment.
- **environment** (`String`): Identifies the environment of the deployment at the time of this deployment status.
- **environmentUrl** (`URI`): Identifies the environment URL of the deployment.
- **id** (`ID!`): The Node ID of the DeploymentStatus object.
- **logUrl** (`URI`): Identifies the log URL of the deployment.
- **state** (`DeploymentStatusState!`): Identifies the current state of the deployment.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### Environment

An environment.

**Implements:** Node

**Fields:**

- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the Environment object.
- **isPinned** (`Boolean`): Indicates whether or not this environment is currently pinned to the repository.
- **latestCompletedDeployment** (`Deployment`): The latest completed deployment with status success, failure, or error if it exists.
- **name** (`String!`): The name of the environment.
- **pinnedPosition** (`Int`): The position of the environment if it is pinned, null if it is not pinned.
- **protectionRules** (`DeploymentProtectionRuleConnection!`): The protection rules defined for this environment.

### PinnedEnvironment

Represents a pinned environment on a given repository.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the pinned environment was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **environment** (`Environment!`): Identifies the environment associated.
- **id** (`ID!`): The Node ID of the PinnedEnvironment object.
- **position** (`Int!`): Identifies the position of the pinned environment.
- **repository** (`Repository!`): The repository that this environment was pinned to.

### RequiredDeploymentsParameters

Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule.

**Fields:**

- **requiredDeploymentEnvironments** (`[String!]!`): The environments that must be successfully deployed to before branches can be merged.

### RequiredStatusCheckDescription

Represents a required status check for a protected branch, but not any specific run of that check.

**Fields:**

- **app** (`App`): The App that must provide this status in order for it to be accepted.
- **context** (`String!`): The name of this status.

### RequiredStatusChecksParameters

Choose which status checks must pass before the ref is updated. When enabled,
commits must first be pushed to another ref where the checks pass.

**Fields:**

- **doNotEnforceOnCreate** (`Boolean!`): Allow repositories and branches to be created if a check would otherwise prohibit it.
- **requiredStatusChecks** (`[StatusCheckConfiguration!]!`): Status checks that are required.
- **strictRequiredStatusChecksPolicy** (`Boolean!`): Whether pull requests targeting a matching branch must be tested with the
latest code. This setting will not take effect unless at least one status
check is enabled.

### Status

Represents a commit status.

**Implements:** Node

**Fields:**

- **combinedContexts** (`StatusCheckRollupContextConnection!`): A list of status contexts and check runs for this commit.
- **commit** (`Commit`): The commit this status is attached to.
- **context** (`StatusContext`): Looks up an individual status context by context name.
- **contexts** (`[StatusContext!]!`): The individual status contexts for this commit.
- **id** (`ID!`): The Node ID of the Status object.
- **state** (`StatusState!`): The combined commit status.

### StatusCheckConfiguration

Required status check.

**Fields:**

- **context** (`String!`): The status check context name that must be present on the commit.
- **integrationId** (`Int`): The optional integration ID that this status check must originate from.

### StatusCheckRollup

Represents the rollup for both the check runs and status for a commit.

**Implements:** Node

**Fields:**

- **commit** (`Commit`): The commit the status and check runs are attached to.
- **contexts** (`StatusCheckRollupContextConnection!`): A list of status contexts and check runs for this commit.
- **id** (`ID!`): The Node ID of the StatusCheckRollup object.
- **state** (`StatusState!`): The combined status for the commit.

### StatusContext

Represents an individual commit status context.

**Implements:** Node, RequirableByPullRequest

**Fields:**

- **avatarUrl** (`URI`): The avatar of the OAuth application or the user that created the status.
- **commit** (`Commit`): This commit this status context is attached to.
- **context** (`String!`): The name of this status context.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created this status context.
- **description** (`String`): The description for this status context.
- **id** (`ID!`): The Node ID of the StatusContext object.
- **isRequired** (`Boolean!`): Whether this is required to pass before merging for a specific pull request.
- **state** (`StatusState!`): The state of this status context.
- **targetUrl** (`URI`): The URL for this status context.

### StatusContextStateCount

Represents a count of the state of a status context.

**Fields:**

- **count** (`Int!`): The number of statuses with this state.
- **state** (`StatusState!`): The state of a status context.

### Workflow

A workflow contains meta information about an Actions workflow file.

**Implements:** Node, UniformResourceLocatable

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the Workflow object.
- **name** (`String!`): The name of the workflow.
- **resourcePath** (`URI!`): The HTTP path for this workflow.
- **runs** (`WorkflowRunConnection!`): The runs of the workflow.
- **state** (`WorkflowState!`): The state of the workflow.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this workflow.

### WorkflowRun

A workflow run.

**Implements:** Node, UniformResourceLocatable

**Fields:**

- **checkSuite** (`CheckSuite!`): The check suite this workflow run belongs to.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **deploymentReviews** (`DeploymentReviewConnection!`): The log of deployment reviews.
- **event** (`String!`): The event that triggered the workflow run.
- **file** (`WorkflowRunFile`): The workflow file.
- **id** (`ID!`): The Node ID of the WorkflowRun object.
- **pendingDeploymentRequests** (`DeploymentRequestConnection!`): The pending deployment requests of all check runs in this workflow run.
- **resourcePath** (`URI!`): The HTTP path for this workflow run.
- **runNumber** (`Int!`): A number that uniquely identifies this workflow run in its parent workflow.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this workflow run.
- **workflow** (`Workflow!`): The workflow executed in this workflow run.

### WorkflowRunFile

An executed workflow file for a workflow run.

**Implements:** Node, UniformResourceLocatable

**Fields:**

- **id** (`ID!`): The Node ID of the WorkflowRunFile object.
- **path** (`String!`): The path of the workflow file relative to its repository.
- **repositoryFileUrl** (`URI!`): The direct link to the file in the repository which stores the workflow file.
- **repositoryName** (`URI!`): The repository name and owner which stores the workflow file.
- **resourcePath** (`URI!`): The HTTP path for this workflow run file.
- **run** (`WorkflowRun!`): The parent workflow run execution for this file.
- **url** (`URI!`): The HTTP URL for this workflow run file.
- **viewerCanPushRepository** (`Boolean!`): If the viewer has permissions to push to the repository which stores the workflow.
- **viewerCanReadRepository** (`Boolean!`): If the viewer has permissions to read the repository which stores the workflow.

### WorkflowsParameters

Require all changes made to a targeted branch to pass the specified workflows before they can be merged.

**Fields:**

- **doNotEnforceOnCreate** (`Boolean!`): Allow repositories and branches to be created if a check would otherwise prohibit it.
- **workflows** (`[WorkflowFileReference!]!`): Workflows that must pass for this rule to pass.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **CheckAnnotationConnection** (4 fields): The connection type for CheckAnnotation.
- **CheckAnnotationEdge** (2 fields): An edge in a connection.
- **CheckRunConnection** (4 fields): The connection type for CheckRun.
- **CheckRunEdge** (2 fields): An edge in a connection.
- **CheckStepConnection** (4 fields): The connection type for CheckStep.
- **CheckStepEdge** (2 fields): An edge in a connection.
- **CheckSuiteConnection** (4 fields): The connection type for CheckSuite.
- **CheckSuiteEdge** (2 fields): An edge in a connection.
- **DeploymentConnection** (4 fields): The connection type for Deployment.
- **DeploymentEdge** (2 fields): An edge in a connection.
- **DeploymentProtectionRuleConnection** (4 fields): The connection type for DeploymentProtectionRule.
- **DeploymentProtectionRuleEdge** (2 fields): An edge in a connection.
- **DeploymentRequestConnection** (4 fields): The connection type for DeploymentRequest.
- **DeploymentRequestEdge** (2 fields): An edge in a connection.
- **DeploymentReviewConnection** (4 fields): The connection type for DeploymentReview.
- **DeploymentReviewEdge** (2 fields): An edge in a connection.
- **DeploymentReviewerConnection** (4 fields): The connection type for DeploymentReviewer.
- **DeploymentReviewerEdge** (2 fields): An edge in a connection.
- **DeploymentStatusConnection** (4 fields): The connection type for DeploymentStatus.
- **DeploymentStatusEdge** (2 fields): An edge in a connection.
- **EnvironmentConnection** (4 fields): The connection type for Environment.
- **EnvironmentEdge** (2 fields): An edge in a connection.
- **PinnedEnvironmentConnection** (4 fields): The connection type for PinnedEnvironment.
- **PinnedEnvironmentEdge** (2 fields): An edge in a connection.
- **StatusCheckRollupContextConnection** (8 fields): The connection type for StatusCheckRollupContext.
- **StatusCheckRollupContextEdge** (2 fields): An edge in a connection.
- **WorkflowRunConnection** (4 fields): The connection type for WorkflowRun.
- **WorkflowRunEdge** (2 fields): An edge in a connection.

## Interfaces

### MemberStatusable

Entities that have members who can set status messages.

**Fields:**

- **memberStatuses** (`UserStatusConnection!`): Get the status messages members of this entity have set that are either public or visible only to the organization.

## Enums

### CheckAnnotationLevel

Represents an annotation's information level.

**Values:**

- `FAILURE`: An annotation indicating an inescapable error.
- `NOTICE`: An annotation indicating some information.
- `WARNING`: An annotation indicating an ignorable error.

### CheckRunState

The possible states of a check run in a status rollup.

**Values:**

- `ACTION_REQUIRED`: The check run requires action.
- `CANCELLED`: The check run has been cancelled.
- `COMPLETED`: The check run has been completed.
- `FAILURE`: The check run has failed.
- `IN_PROGRESS`: The check run is in progress.
- `NEUTRAL`: The check run was neutral.
- `PENDING`: The check run is in pending state.
- `QUEUED`: The check run has been queued.
- `SKIPPED`: The check run was skipped.
- `STALE`: The check run was marked stale by GitHub. Only GitHub can use this conclusion.
- `STARTUP_FAILURE`: The check run has failed at startup.
- `SUCCESS`: The check run has succeeded.
- `TIMED_OUT`: The check run has timed out.
- `WAITING`: The check run is in waiting state.

### CheckRunType

The possible types of check runs.

**Values:**

- `ALL`: Every check run available.
- `LATEST`: The latest check run.

### CheckStatusState

The possible states for a check suite or run status.

**Values:**

- `COMPLETED`: The check suite or run has been completed.
- `IN_PROGRESS`: The check suite or run is in progress.
- `PENDING`: The check suite or run is in pending state.
- `QUEUED`: The check suite or run has been queued.
- `REQUESTED`: The check suite or run has been requested.
- `WAITING`: The check suite or run is in waiting state.

### DeploymentOrderField

Properties by which deployment connections can be ordered.

**Values:**

- `CREATED_AT`: Order collection by creation time.

### DeploymentProtectionRuleType

The possible protection rule types.

**Values:**

- `BRANCH_POLICY`: Branch policy.
- `REQUIRED_REVIEWERS`: Required reviewers.
- `WAIT_TIMER`: Wait timer.

### DeploymentReviewState

The possible states for a deployment review.

**Values:**

- `APPROVED`: The deployment was approved.
- `REJECTED`: The deployment was rejected.

### DeploymentState

The possible states in which a deployment can be.

**Values:**

- `ABANDONED`: The pending deployment was not updated after 30 minutes.
- `ACTIVE`: The deployment is currently active.
- `DESTROYED`: An inactive transient deployment.
- `ERROR`: The deployment experienced an error.
- `FAILURE`: The deployment has failed.
- `INACTIVE`: The deployment is inactive.
- `IN_PROGRESS`: The deployment is in progress.
- `PENDING`: The deployment is pending.
- `QUEUED`: The deployment has queued.
- `SUCCESS`: The deployment was successful.
- `WAITING`: The deployment is waiting.

### DeploymentStatusState

The possible states for a deployment status.

**Values:**

- `ERROR`: The deployment experienced an error.
- `FAILURE`: The deployment has failed.
- `INACTIVE`: The deployment is inactive.
- `IN_PROGRESS`: The deployment is in progress.
- `PENDING`: The deployment is pending.
- `QUEUED`: The deployment is queued.
- `SUCCESS`: The deployment was successful.
- `WAITING`: The deployment is waiting.

### EnvironmentOrderField

Properties by which environments connections can be ordered.

**Values:**

- `NAME`: Order environments by name.

### EnvironmentPinnedFilterField

Properties by which environments connections can be ordered.

**Values:**

- `ALL`: All environments will be returned.
- `NONE`: Environments exclude pinned will be returned.
- `ONLY`: Only pinned environment will be returned.

### MergeStateStatus

Detailed status information about a pull request merge.

**Values:**

- `BEHIND`: The head ref is out of date.
- `BLOCKED`: The merge is blocked.
- `CLEAN`: Mergeable and passing commit status.
- `DIRTY`: The merge commit cannot be cleanly created.
- `DRAFT`: The merge is blocked due to the pull request being a draft.
- `HAS_HOOKS`: Mergeable with passing commit status and pre-receive hooks.
- `UNKNOWN`: The state cannot currently be determined.
- `UNSTABLE`: Mergeable with non-passing commit status.

### PatchStatus

The possible types of patch statuses.

**Values:**

- `ADDED`: The file was added. Git status 'A'.
- `CHANGED`: The file's type was changed. Git status 'T'.
- `COPIED`: The file was copied. Git status 'C'.
- `DELETED`: The file was deleted. Git status 'D'.
- `MODIFIED`: The file's contents were changed. Git status 'M'.
- `RENAMED`: The file was renamed. Git status 'R'.

### PinnedEnvironmentOrderField

Properties by which pinned environments connections can be ordered.

**Values:**

- `POSITION`: Order pinned environments by position.

### RequestableCheckStatusState

The possible states that can be requested when creating a check run.

**Values:**

- `COMPLETED`: The check suite or run has been completed.
- `IN_PROGRESS`: The check suite or run is in progress.
- `PENDING`: The check suite or run is in pending state.
- `QUEUED`: The check suite or run has been queued.
- `WAITING`: The check suite or run is in waiting state.

### StatusState

The possible commit status states.

**Values:**

- `ERROR`: Status is errored.
- `EXPECTED`: Status is expected.
- `FAILURE`: Status is failing.
- `PENDING`: Status is pending.
- `SUCCESS`: Status is successful.

### WorkflowRunOrderField

Properties by which workflow run connections can be ordered.

**Values:**

- `CREATED_AT`: Order workflow runs by most recently created.

### WorkflowState

The possible states for a workflow.

**Values:**

- `ACTIVE`: The workflow is active.
- `DELETED`: The workflow was deleted from the git repository.
- `DISABLED_FORK`: The workflow was disabled by default on a fork.
- `DISABLED_INACTIVITY`: The workflow was disabled for inactivity in the repository.
- `DISABLED_MANUALLY`: The workflow was disabled manually.

## Input Objects

### ApproveDeploymentsInput

Autogenerated input type of ApproveDeployments.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **comment** (`String`): Optional comment for approving deployments.
- **environmentIds** (`[ID!]!`): The ids of environments to reject deployments.
- **workflowRunId** (`ID!`): The node ID of the workflow run containing the pending deployments.

### CheckAnnotationData

Information from a check run analysis to specific lines of code.

**Input fields:**

- **annotationLevel** (`CheckAnnotationLevel!`): Represents an annotation's information level.
- **location** (`CheckAnnotationRange!`): The location of the annotation.
- **message** (`String!`): A short description of the feedback for these lines of code.
- **path** (`String!`): The path of the file to add an annotation to.
- **rawDetails** (`String`): Details about this annotation.
- **title** (`String`): The title that represents the annotation.

### CheckAnnotationRange

Information from a check run analysis to specific lines of code.

**Input fields:**

- **endColumn** (`Int`): The ending column of the range.
- **endLine** (`Int!`): The ending line of the range.
- **startColumn** (`Int`): The starting column of the range.
- **startLine** (`Int!`): The starting line of the range.

### CheckRunAction

Possible further actions the integrator can perform.

**Input fields:**

- **description** (`String!`): A short explanation of what this action would do.
- **identifier** (`String!`): A reference for the action on the integrator's system.
- **label** (`String!`): The text to be displayed on a button in the web UI.

### CheckRunFilter

The filters that are available when fetching check runs.

**Input fields:**

- **appId** (`Int`): Filters the check runs created by this application ID.
- **checkName** (`String`): Filters the check runs by this name.
- **checkType** (`CheckRunType`): Filters the check runs by this type.
- **conclusions** (`[CheckConclusionState!]`): Filters the check runs by these conclusions.
- **status** (`CheckStatusState`): Filters the check runs by this status. Superceded by statuses.
- **statuses** (`[CheckStatusState!]`): Filters the check runs by this status. Overrides status.

### CheckRunOutput

Descriptive details about the check run.

**Input fields:**

- **annotations** (`[CheckAnnotationData!]`): The annotations that are made as part of the check run.
- **images** (`[CheckRunOutputImage!]`): Images attached to the check run output displayed in the GitHub pull request UI.
- **summary** (`String!`): The summary of the check run (supports Commonmark).
- **text** (`String`): The details of the check run (supports Commonmark).
- **title** (`String!`): A title to provide for this check run.

### CheckRunOutputImage

Images attached to the check run output displayed in the GitHub pull request UI.

**Input fields:**

- **alt** (`String!`): The alternative text for the image.
- **caption** (`String`): A short image description.
- **imageUrl** (`URI!`): The full URL of the image.

### CheckSuiteAutoTriggerPreference

The auto-trigger preferences that are available for check suites.

**Input fields:**

- **appId** (`ID!`): The node ID of the application that owns the check suite.
- **setting** (`Boolean!`): Set to `true` to enable automatic creation of CheckSuite events upon pushes to the repository.

### CheckSuiteFilter

The filters that are available when fetching check suites.

**Input fields:**

- **appId** (`Int`): Filters the check suites created by this application ID.
- **checkName** (`String`): Filters the check suites by this name.

### CreateCheckRunInput

Autogenerated input type of CreateCheckRun.

**Input fields:**

- **actions** (`[CheckRunAction!]`): Possible further actions the integrator can perform, which a user may trigger.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **completedAt** (`DateTime`): The time that the check run finished.
- **conclusion** (`CheckConclusionState`): The final conclusion of the check.
- **detailsUrl** (`URI`): The URL of the integrator's site that has the full details of the check.
- **externalId** (`String`): A reference for the run on the integrator's system.
- **headSha** (`GitObjectID!`): The SHA of the head commit.
- **name** (`String!`): The name of the check.
- **output** (`CheckRunOutput`): Descriptive details about the run.
- **repositoryId** (`ID!`): The node ID of the repository.
- **startedAt** (`DateTime`): The time that the check run began.
- **status** (`RequestableCheckStatusState`): The current status.

### CreateCheckSuiteInput

Autogenerated input type of CreateCheckSuite.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **headSha** (`GitObjectID!`): The SHA of the head commit.
- **repositoryId** (`ID!`): The Node ID of the repository.

### CreateDeploymentInput

Autogenerated input type of CreateDeployment.

**Input fields:**

- **autoMerge** (`Boolean`): Attempt to automatically merge the default branch into the requested ref, defaults to true.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **description** (`String`): Short description of the deployment.
- **environment** (`String`): Name for the target deployment environment.
- **payload** (`String`): JSON payload with extra information about the deployment.
- **refId** (`ID!`): The node ID of the ref to be deployed.
- **repositoryId** (`ID!`): The node ID of the repository.
- **requiredContexts** (`[String!]`): The status contexts to verify against commit status checks. To bypass required
contexts, pass an empty array. Defaults to all unique contexts.
- **task** (`String`): Specifies a task to execute.

### CreateDeploymentStatusInput

Autogenerated input type of CreateDeploymentStatus.

**Input fields:**

- **autoInactive** (`Boolean`): Adds a new inactive status to all non-transient, non-production environment
deployments with the same repository and environment name as the created
status's deployment.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deploymentId** (`ID!`): The node ID of the deployment.
- **description** (`String`): A short description of the status. Maximum length of 140 characters.
- **environment** (`String`): If provided, updates the environment of the deploy. Otherwise, does not modify the environment.
- **environmentUrl** (`String`): Sets the URL for accessing your environment.
- **logUrl** (`String`): The log URL to associate with this status.       This URL should contain
output to keep the user updated while the task is running       or serve as
historical information for what happened in the deployment.
- **state** (`DeploymentStatusState!`): The state of the deployment.

### CreateEnvironmentInput

Autogenerated input type of CreateEnvironment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **name** (`String!`): The name of the environment.
- **repositoryId** (`ID!`): The node ID of the repository.

### DeleteDeploymentInput

Autogenerated input type of DeleteDeployment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The Node ID of the deployment to be deleted.

### DeleteEnvironmentInput

Autogenerated input type of DeleteEnvironment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **id** (`ID!`): The Node ID of the environment to be deleted.

### DeploymentOrder

Ordering options for deployment connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`DeploymentOrderField!`): The field to order deployments by.

### Environments

Ordering options for environments.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order environments by the specified field.
- **field** (`EnvironmentOrderField!`): The field to order environments by.

### PinEnvironmentInput

Autogenerated input type of PinEnvironment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **environmentId** (`ID!`): The ID of the environment to modify.
- **pinned** (`Boolean!`): The desired state of the environment. If true, environment will be pinned. If false, it will be unpinned.

### PinnedEnvironmentOrder

Ordering options for pinned environments.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order pinned environments by the specified field.
- **field** (`PinnedEnvironmentOrderField!`): The field to order pinned environments by.

### RejectDeploymentsInput

Autogenerated input type of RejectDeployments.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **comment** (`String`): Optional comment for rejecting deployments.
- **environmentIds** (`[ID!]!`): The ids of environments to reject deployments.
- **workflowRunId** (`ID!`): The node ID of the workflow run containing the pending deployments.

### ReorderEnvironmentInput

Autogenerated input type of ReorderEnvironment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **environmentId** (`ID!`): The ID of the environment to modify.
- **position** (`Int!`): The desired position of the environment.

### RequiredDeploymentsParametersInput

Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule.

**Input fields:**

- **requiredDeploymentEnvironments** (`[String!]!`): The environments that must be successfully deployed to before branches can be merged.

### RequiredStatusCheckInput

Specifies the attributes for a new or updated required status check.

**Input fields:**

- **appId** (`ID`): The ID of the App that must set the status in order for it to be accepted.
Omit this value to use whichever app has recently been setting this status, or
use "any" to allow any app to set the status.
- **context** (`String!`): Status check context that must pass for commits to be accepted to the matching branch.

### RequiredStatusChecksParametersInput

Choose which status checks must pass before the ref is updated. When enabled,
commits must first be pushed to another ref where the checks pass.

**Input fields:**

- **doNotEnforceOnCreate** (`Boolean`): Allow repositories and branches to be created if a check would otherwise prohibit it.
- **requiredStatusChecks** (`[StatusCheckConfigurationInput!]!`): Status checks that are required.
- **strictRequiredStatusChecksPolicy** (`Boolean!`): Whether pull requests targeting a matching branch must be tested with the
latest code. This setting will not take effect unless at least one status
check is enabled.

### RerequestCheckSuiteInput

Autogenerated input type of RerequestCheckSuite.

**Input fields:**

- **checkSuiteId** (`ID!`): The Node ID of the check suite.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryId** (`ID!`): The Node ID of the repository.

### StatusCheckConfigurationInput

Required status check.

**Input fields:**

- **context** (`String!`): The status check context name that must be present on the commit.
- **integrationId** (`Int`): The optional integration ID that this status check must originate from.

### UpdateCheckRunInput

Autogenerated input type of UpdateCheckRun.

**Input fields:**

- **actions** (`[CheckRunAction!]`): Possible further actions the integrator can perform, which a user may trigger.
- **checkRunId** (`ID!`): The node of the check.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **completedAt** (`DateTime`): The time that the check run finished.
- **conclusion** (`CheckConclusionState`): The final conclusion of the check.
- **detailsUrl** (`URI`): The URL of the integrator's site that has the full details of the check.
- **externalId** (`String`): A reference for the run on the integrator's system.
- **name** (`String`): The name of the check.
- **output** (`CheckRunOutput`): Descriptive details about the run.
- **repositoryId** (`ID!`): The node ID of the repository.
- **startedAt** (`DateTime`): The time that the check run began.
- **status** (`RequestableCheckStatusState`): The current status.

### UpdateCheckSuitePreferencesInput

Autogenerated input type of UpdateCheckSuitePreferences.

**Input fields:**

- **autoTriggerPreferences** (`[CheckSuiteAutoTriggerPreference!]!`): The check suite preferences to modify.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **repositoryId** (`ID!`): The Node ID of the repository.

### UpdateEnvironmentInput

Autogenerated input type of UpdateEnvironment.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **environmentId** (`ID!`): The node ID of the environment.
- **preventSelfReview** (`Boolean`): Whether deployments to this environment can be approved by the user who created the deployment.
- **reviewers** (`[ID!]`): The ids of users or teams that can approve deployments to this environment.
- **waitTimer** (`Int`): The wait timer in minutes.

### WorkflowRunOrder

Ways in which lists of workflow runs can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order workflow runs by the specified field.
- **field** (`WorkflowRunOrderField!`): The field by which to order workflows.

### WorkflowsParametersInput

Require all changes made to a targeted branch to pass the specified workflows before they can be merged.

**Input fields:**

- **doNotEnforceOnCreate** (`Boolean`): Allow repositories and branches to be created if a check would otherwise prohibit it.
- **workflows** (`[WorkflowFileReferenceInput!]!`): Workflows that must pass for this rule to pass.

## Unions

### DeploymentReviewer

Users and teams.

**Possible types:** Team, User

### StatusCheckRollupContext

Types that can be inside a StatusCheckRollup context.

**Possible types:** CheckRun, StatusContext
