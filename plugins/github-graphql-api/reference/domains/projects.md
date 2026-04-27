# Projects (Classic & V2)

## Mutations

### addProjectCard

Adds a card to a ProjectColumn. Either `contentId` or `note` must be provided but **not** both.

**Input fields:**

- **input** (`AddProjectCardInput!`)

**Return fields:**

- **cardEdge** (`ProjectCardEdge`): The edge from the ProjectColumn's card connection.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectColumn** (`ProjectColumn`): The ProjectColumn.

### addProjectColumn

Adds a column to a Project.

**Input fields:**

- **input** (`AddProjectColumnInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **columnEdge** (`ProjectColumnEdge`): The edge from the project's column connection.
- **project** (`Project`): The project.

### addProjectV2ItemById

Links an existing content instance to a Project.

**Input fields:**

- **input** (`AddProjectV2ItemByIdInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **item** (`ProjectV2Item`): The item added to the project.

### archiveProjectV2Item

Archives a ProjectV2Item.

**Input fields:**

- **input** (`ArchiveProjectV2ItemInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **item** (`ProjectV2Item`): The item archived from the project.

### clearProjectV2ItemFieldValue

This mutation clears the value of a field for an item in a Project. Currently
only text, number, date, assignees, labels, single-select, iteration and
milestone fields are supported.

**Input fields:**

- **input** (`ClearProjectV2ItemFieldValueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2Item** (`ProjectV2Item`): The updated item.

### cloneProject

Creates a new project by cloning configuration from an existing project.

**Input fields:**

- **input** (`CloneProjectInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **jobStatusId** (`String`): The id of the JobStatus for populating cloned fields.
- **project** (`Project`): The new cloned project.

### copyProjectV2

Copy a project.

**Input fields:**

- **input** (`CopyProjectV2Input!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2** (`ProjectV2`): The copied project.

### createProject

Creates a new project.

**Input fields:**

- **input** (`CreateProjectInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **project** (`Project`): The new project.

### createProjectV2

Creates a new project.

**Input fields:**

- **input** (`CreateProjectV2Input!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2** (`ProjectV2`): The new project.

### createProjectV2Field

Create a new project field.

**Input fields:**

- **input** (`CreateProjectV2FieldInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2Field** (`ProjectV2FieldConfiguration`): The new field.

### createProjectV2StatusUpdate

Creates a status update within a Project.

**Input fields:**

- **input** (`CreateProjectV2StatusUpdateInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **statusUpdate** (`ProjectV2StatusUpdate`): The status update updated in the project.

### deleteProject

Deletes a project.

**Input fields:**

- **input** (`DeleteProjectInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **owner** (`ProjectOwner`): The repository or organization the project was removed from.

### deleteProjectCard

Deletes a project card.

**Input fields:**

- **input** (`DeleteProjectCardInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **column** (`ProjectColumn`): The column the deleted card was in.
- **deletedCardId** (`ID`): The deleted card ID.

### deleteProjectColumn

Deletes a project column.

**Input fields:**

- **input** (`DeleteProjectColumnInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deletedColumnId** (`ID`): The deleted column ID.
- **project** (`Project`): The project the deleted column was in.

### deleteProjectV2

Delete a project.

**Input fields:**

- **input** (`DeleteProjectV2Input!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2** (`ProjectV2`): The deleted Project.

### deleteProjectV2Field

Delete a project field.

**Input fields:**

- **input** (`DeleteProjectV2FieldInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2Field** (`ProjectV2FieldConfiguration`): The deleted field.

### deleteProjectV2Item

Deletes an item from a Project.

**Input fields:**

- **input** (`DeleteProjectV2ItemInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deletedItemId** (`ID`): The ID of the deleted item.

### deleteProjectV2StatusUpdate

Deletes a project status update.

**Input fields:**

- **input** (`DeleteProjectV2StatusUpdateInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deletedStatusUpdateId** (`ID`): The ID of the deleted status update.
- **projectV2** (`ProjectV2`): The project the deleted status update was in.

### deleteProjectV2Workflow

Deletes a project workflow.

**Input fields:**

- **input** (`DeleteProjectV2WorkflowInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **deletedWorkflowId** (`ID`): The ID of the deleted workflow.
- **projectV2** (`ProjectV2`): The project the deleted workflow was in.

### importProject

Creates a new project by importing columns and a list of issues/PRs.

**Input fields:**

- **input** (`ImportProjectInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **project** (`Project`): The new Project!.

### markProjectV2AsTemplate

Mark a project as a template. Note that only projects which are owned by an Organization can be marked as a template.

**Input fields:**

- **input** (`MarkProjectV2AsTemplateInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2** (`ProjectV2`): The project.

### moveProjectCard

Moves a project card to another place.

**Input fields:**

- **input** (`MoveProjectCardInput!`)

**Return fields:**

- **cardEdge** (`ProjectCardEdge`): The new edge of the moved card.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### moveProjectColumn

Moves a project column to another place.

**Input fields:**

- **input** (`MoveProjectColumnInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **columnEdge** (`ProjectColumnEdge`): The new edge of the moved column.

### unarchiveProjectV2Item

Unarchives a ProjectV2Item.

**Input fields:**

- **input** (`UnarchiveProjectV2ItemInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **item** (`ProjectV2Item`): The item unarchived from the project.

### unmarkProjectV2AsTemplate

Unmark a project as a template.

**Input fields:**

- **input** (`UnmarkProjectV2AsTemplateInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2** (`ProjectV2`): The project.

### updateProject

Updates an existing project.

**Input fields:**

- **input** (`UpdateProjectInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **project** (`Project`): The updated project.

### updateProjectCard

Updates an existing project card.

**Input fields:**

- **input** (`UpdateProjectCardInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectCard** (`ProjectCard`): The updated ProjectCard.

### updateProjectColumn

Updates an existing project column.

**Input fields:**

- **input** (`UpdateProjectColumnInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectColumn** (`ProjectColumn`): The updated project column.

### updateProjectV2

Updates an existing project.

**Input fields:**

- **input** (`UpdateProjectV2Input!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2** (`ProjectV2`): The updated Project.

### updateProjectV2Collaborators

Update the collaborators on a team or a project.

**Input fields:**

- **input** (`UpdateProjectV2CollaboratorsInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **collaborators** (`ProjectV2ActorConnection`): The collaborators granted a role.

### updateProjectV2Field

Update a project field.

**Input fields:**

- **input** (`UpdateProjectV2FieldInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2Field** (`ProjectV2FieldConfiguration`): The updated field.

### updateProjectV2ItemFieldValue

This mutation updates the value of a field for an item in a Project. Currently
only single-select, text, number, date, and iteration fields are supported.

**Input fields:**

- **input** (`UpdateProjectV2ItemFieldValueInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectV2Item** (`ProjectV2Item`): The updated item.

### updateProjectV2ItemPosition

This mutation updates the position of the item in the project, where the position represents the priority of an item.

**Input fields:**

- **input** (`UpdateProjectV2ItemPositionInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **items** (`ProjectV2ItemConnection`): The items in the new order.

### updateProjectV2StatusUpdate

Updates a status update within a Project.

**Input fields:**

- **input** (`UpdateProjectV2StatusUpdateInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **statusUpdate** (`ProjectV2StatusUpdate`): The status update updated in the project.

## Types

### AddedToProjectEvent

Represents a`added_to_project`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the AddedToProjectEvent object.
- **project** (`Project`): Project referenced by event.
- **projectCard** (`ProjectCard`): Project card referenced by this project event.
- **projectColumnName** (`String!`): Column name referenced by this project event.

### AddedToProjectV2Event

Represents a`added_to_project_v2`event on a given issue or pull request.

**Implements:** Node, ProjectV2Event

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the AddedToProjectV2Event object.
- **project** (`ProjectV2`): Project referenced by event.
- **wasAutomated** (`Boolean!`): Did this event result from workflow automation?.

### MovedColumnsInProjectEvent

Represents a`moved_columns_in_project`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the MovedColumnsInProjectEvent object.
- **previousProjectColumnName** (`String!`): Column name the issue or pull request was moved from.
- **project** (`Project`): Project referenced by event.
- **projectCard** (`ProjectCard`): Project card referenced by this project event.
- **projectColumnName** (`String!`): Column name the issue or pull request was moved to.

### Project

Projects manage issues, pull requests and notes within a project owner.

**Implements:** Closable, Node, Updatable

**Fields:**

- **body** (`String`): The project's description body.
- **bodyHTML** (`HTML!`): The projects description body rendered to HTML.
- **closed** (`Boolean!`): Indicates if the object is closed (definition of closed may depend on type).
- **closedAt** (`DateTime`): Identifies the date and time when the object was closed.
- **columns** (`ProjectColumnConnection!`): List of columns in the project.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who originally created the project.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the Project object.
- **name** (`String!`): The project's name.
- **number** (`Int!`): The project's number.
- **owner** (`ProjectOwner!`): The project's owner. Currently limited to repositories, organizations, and users.
- **pendingCards** (`ProjectCardConnection!`): List of pending cards in this project.
- **progress** (`ProjectProgress!`): Project progress details.
- **resourcePath** (`URI!`): The HTTP path for this project.
- **state** (`ProjectState!`): Whether the project is open or closed.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this project.
- **viewerCanClose** (`Boolean!`): Indicates if the object can be closed by the viewer.
- **viewerCanReopen** (`Boolean!`): Indicates if the object can be reopened by the viewer.
- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.

### ProjectCard

A card in a project.

**Implements:** Node

**Fields:**

- **column** (`ProjectColumn`): The project column this card is associated under. A card may only belong to one
project column at a time. The column field will be null if the card is created
in a pending state and has yet to be associated with a column. Once cards are
associated with a column, they will not become pending in the future.
- **content** (`ProjectCardItem`): The card content item.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created this card.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the ProjectCard object.
- **isArchived** (`Boolean!`): Whether the card is archived.
- **note** (`String`): The card note.
- **project** (`Project!`): The project that contains this card.
- **resourcePath** (`URI!`): The HTTP path for this card.
- **state** (`ProjectCardState`): The state of ProjectCard.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this card.

### ProjectColumn

A column inside a project.

**Implements:** Node

**Fields:**

- **cards** (`ProjectCardConnection!`): List of cards in the column.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the ProjectColumn object.
- **name** (`String!`): The project column's name.
- **project** (`Project!`): The project that contains this column.
- **purpose** (`ProjectColumnPurpose`): The semantic purpose of the column.
- **resourcePath** (`URI!`): The HTTP path for this project column.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this project column.

### ProjectProgress

Project progress stats.

**Fields:**

- **doneCount** (`Int!`): The number of done cards.
- **donePercentage** (`Float!`): The percentage of done cards.
- **enabled** (`Boolean!`): Whether progress tracking is enabled and cards with purpose exist for this project.
- **inProgressCount** (`Int!`): The number of in-progress cards.
- **inProgressPercentage** (`Float!`): The percentage of in-progress cards.
- **todoCount** (`Int!`): The number of to do cards.
- **todoPercentage** (`Float!`): The percentage of to do cards.

### ProjectV2

New projects that manage issues, pull requests and drafts using tables and boards.

**Implements:** Closable, Node, Updatable

**Fields:**

- **closed** (`Boolean!`): Returns true if the project is closed.
- **closedAt** (`DateTime`): Identifies the date and time when the object was closed.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who originally created the project.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **field** (`ProjectV2FieldConfiguration`): A field of the project.
- **fields** (`ProjectV2FieldConfigurationConnection!`): List of fields and their constraints in the project.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **id** (`ID!`): The Node ID of the ProjectV2 object.
- **items** (`ProjectV2ItemConnection!`): List of items in the project.
- **number** (`Int!`): The project's number.
- **owner** (`ProjectV2Owner!`): The project's owner. Currently limited to organizations and users.
- **public** (`Boolean!`): Returns true if the project is public.
- **readme** (`String`): The project's readme.
- **repositories** (`RepositoryConnection!`): The repositories the project is linked to.
- **resourcePath** (`URI!`): The HTTP path for this project.
- **shortDescription** (`String`): The project's short description.
- **statusUpdates** (`ProjectV2StatusUpdateConnection!`): List of the status updates in the project.
- **teams** (`TeamConnection!`): The teams the project is linked to.
- **template** (`Boolean!`): Returns true if this project is a template.
- **title** (`String!`): The project's name.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this project.
- **view** (`ProjectV2View`): A view of the project.
- **viewerCanClose** (`Boolean!`): Indicates if the object can be closed by the viewer.
- **viewerCanReopen** (`Boolean!`): Indicates if the object can be reopened by the viewer.
- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.
- **views** (`ProjectV2ViewConnection!`): List of views in the project.
- **workflow** (`ProjectV2Workflow`): A workflow of the project.
- **workflows** (`ProjectV2WorkflowConnection!`): List of the workflows in the project.

### ProjectV2Field

A field inside a project.

**Implements:** Node, ProjectV2FieldCommon

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **dataType** (`ProjectV2FieldType!`): The field's type.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the ProjectV2Field object.
- **name** (`String!`): The project field's name.
- **project** (`ProjectV2!`): The project that contains this field.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2Item

An item within a Project.

**Implements:** Node

**Fields:**

- **content** (`ProjectV2ItemContent`): The content of the referenced draft issue, issue, pull request.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created the item.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **fieldValueByName** (`ProjectV2ItemFieldValue`): The field value of the first project field which matches the`name`argument that is set on the item.
- **fieldValues** (`ProjectV2ItemFieldValueConnection!`): The field values that are set on the item.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **id** (`ID!`): The Node ID of the ProjectV2Item object.
- **isArchived** (`Boolean!`): Whether the item is archived.
- **project** (`ProjectV2!`): The project that contains this item.
- **type** (`ProjectV2ItemType!`): The type of the item.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2ItemFieldDateValue

The value of a date field in a Project item.

**Implements:** Node, ProjectV2ItemFieldValueCommon

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created the item.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **date** (`Date`): Date value for the field.
- **field** (`ProjectV2FieldConfiguration!`): The project field that contains this value.
- **id** (`ID!`): The Node ID of the ProjectV2ItemFieldDateValue object.
- **item** (`ProjectV2Item!`): The project item that contains this value.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2ItemFieldIterationValue

The value of an iteration field in a Project item.

**Implements:** Node, ProjectV2ItemFieldValueCommon

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created the item.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **duration** (`Int!`): The duration of the iteration in days.
- **field** (`ProjectV2FieldConfiguration!`): The project field that contains this value.
- **id** (`ID!`): The Node ID of the ProjectV2ItemFieldIterationValue object.
- **item** (`ProjectV2Item!`): The project item that contains this value.
- **iterationId** (`String!`): The ID of the iteration.
- **startDate** (`Date!`): The start date of the iteration.
- **title** (`String!`): The title of the iteration.
- **titleHTML** (`String!`): The title of the iteration, with HTML.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2ItemFieldNumberValue

The value of a number field in a Project item.

**Implements:** Node, ProjectV2ItemFieldValueCommon

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created the item.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **field** (`ProjectV2FieldConfiguration!`): The project field that contains this value.
- **id** (`ID!`): The Node ID of the ProjectV2ItemFieldNumberValue object.
- **item** (`ProjectV2Item!`): The project item that contains this value.
- **number** (`Float`): Number as a float(8).
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2ItemFieldReviewerValue

The value of a reviewers field in a Project item.

**Fields:**

- **field** (`ProjectV2FieldConfiguration!`): The field that contains this value.
- **reviewers** (`RequestedReviewerConnection`): The reviewers for this field.

### ProjectV2ItemFieldSingleSelectValue

The value of a single select field in a Project item.

**Implements:** Node, ProjectV2ItemFieldValueCommon

**Fields:**

- **color** (`ProjectV2SingleSelectFieldOptionColor!`): The color applied to the selected single-select option.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created the item.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **description** (`String`): A plain-text description of the selected single-select option, such as what the option means.
- **descriptionHTML** (`String`): The description of the selected single-select option, including HTML tags.
- **field** (`ProjectV2FieldConfiguration!`): The project field that contains this value.
- **id** (`ID!`): The Node ID of the ProjectV2ItemFieldSingleSelectValue object.
- **item** (`ProjectV2Item!`): The project item that contains this value.
- **name** (`String`): The name of the selected single select option.
- **nameHTML** (`String`): The html name of the selected single select option.
- **optionId** (`String`): The id of the selected single select option.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2ItemFieldTextValue

The value of a text field in a Project item.

**Implements:** Node, ProjectV2ItemFieldValueCommon

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created the item.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **field** (`ProjectV2FieldConfiguration!`): The project field that contains this value.
- **id** (`ID!`): The Node ID of the ProjectV2ItemFieldTextValue object.
- **item** (`ProjectV2Item!`): The project item that contains this value.
- **text** (`String`): Text value of a field.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2ItemStatusChangedEvent

Represents a`project_v2_item_status_changed`event on a given issue or pull request.

**Implements:** Node, ProjectV2Event

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the ProjectV2ItemStatusChangedEvent object.
- **previousStatus** (`String!`): The previous status of the project item.
- **project** (`ProjectV2`): Project referenced by event.
- **status** (`String!`): The new status of the project item.
- **wasAutomated** (`Boolean!`): Did this event result from workflow automation?.

### ProjectV2IterationField

An iteration field inside a project.

**Implements:** Node, ProjectV2FieldCommon

**Fields:**

- **configuration** (`ProjectV2IterationFieldConfiguration!`): Iteration configuration settings.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **dataType** (`ProjectV2FieldType!`): The field's type.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the ProjectV2IterationField object.
- **name** (`String!`): The project field's name.
- **project** (`ProjectV2!`): The project that contains this field.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2IterationFieldConfiguration

Iteration field configuration for a project.

**Fields:**

- **completedIterations** (`[ProjectV2IterationFieldIteration!]!`): The iteration's completed iterations.
- **duration** (`Int!`): The iteration's duration in days.
- **iterations** (`[ProjectV2IterationFieldIteration!]!`): The iteration's iterations.
- **startDay** (`Int!`): The iteration's start day of the week.

### ProjectV2IterationFieldIteration

Iteration field iteration settings for a project.

**Fields:**

- **duration** (`Int!`): The iteration's duration in days.
- **id** (`String!`): The iteration's ID.
- **startDate** (`Date!`): The iteration's start date.
- **title** (`String!`): The iteration's title.
- **titleHTML** (`String!`): The iteration's html title.

### ProjectV2SingleSelectField

A single select field inside a project.

**Implements:** Node, ProjectV2FieldCommon

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **dataType** (`ProjectV2FieldType!`): The field's type.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the ProjectV2SingleSelectField object.
- **name** (`String!`): The project field's name.
- **options** (`[ProjectV2SingleSelectFieldOption!]!`): Options for the single select field.
- **project** (`ProjectV2!`): The project that contains this field.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2SingleSelectFieldOption

Single select field option for a configuration for a project.

**Fields:**

- **color** (`ProjectV2SingleSelectFieldOptionColor!`): The option's display color.
- **description** (`String!`): The option's plain-text description.
- **descriptionHTML** (`String!`): The option's description, possibly containing HTML.
- **id** (`String!`): The option's ID.
- **name** (`String!`): The option's name.
- **nameHTML** (`String!`): The option's html name.

### ProjectV2SortBy

Represents a sort by field and direction.

**Fields:**

- **direction** (`OrderDirection!`): The direction of the sorting. Possible values are ASC and DESC.
- **field** (`ProjectV2Field!`): The field by which items are sorted.

### ProjectV2SortByField

Represents a sort by field and direction.

**Fields:**

- **direction** (`OrderDirection!`): The direction of the sorting. Possible values are ASC and DESC.
- **field** (`ProjectV2FieldConfiguration!`): The field by which items are sorted.

### ProjectV2StatusUpdate

A status update within a project.

**Implements:** Node

**Fields:**

- **body** (`String`): The body of the status update.
- **bodyHTML** (`HTML`): The body of the status update rendered to HTML.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created the status update.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **id** (`ID!`): The Node ID of the ProjectV2StatusUpdate object.
- **project** (`ProjectV2!`): The project that contains this status update.
- **startDate** (`Date`): The start date of the status update.
- **status** (`ProjectV2StatusUpdateStatus`): The status of the status update.
- **targetDate** (`Date`): The target date of the status update.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2View

A view within a ProjectV2.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **fields** (`ProjectV2FieldConfigurationConnection`): The view's visible fields.
- **filter** (`String`): The project view's filter.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **groupBy** (`ProjectV2FieldConnection`): The view's group-by field.
- **groupByFields** (`ProjectV2FieldConfigurationConnection`): The view's group-by field.
- **id** (`ID!`): The Node ID of the ProjectV2View object.
- **layout** (`ProjectV2ViewLayout!`): The project view's layout.
- **name** (`String!`): The project view's name.
- **number** (`Int!`): The project view's number.
- **project** (`ProjectV2!`): The project that contains this view.
- **sortBy** (`ProjectV2SortByConnection`): The view's sort-by config.
- **sortByFields** (`ProjectV2SortByFieldConnection`): The view's sort-by config.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **verticalGroupBy** (`ProjectV2FieldConnection`): The view's vertical-group-by field.
- **verticalGroupByFields** (`ProjectV2FieldConfigurationConnection`): The view's vertical-group-by field.
- **visibleFields** (`ProjectV2FieldConnection`): The view's visible fields.

### ProjectV2Workflow

A workflow inside a project.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **enabled** (`Boolean!`): Whether the workflow is enabled.
- **fullDatabaseId** (`BigInt`): Identifies the primary key from the database as a BigInt.
- **id** (`ID!`): The Node ID of the ProjectV2Workflow object.
- **name** (`String!`): The name of the workflow.
- **number** (`Int!`): The number of the workflow.
- **project** (`ProjectV2!`): The project that contains this workflow.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### RemovedFromProjectEvent

Represents a`removed_from_project`event on a given issue or pull request.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the RemovedFromProjectEvent object.
- **project** (`Project`): Project referenced by event.
- **projectColumnName** (`String!`): Column name referenced by this project event.

### RemovedFromProjectV2Event

Represents a`removed_from_project_v2`event on a given issue or pull request.

**Implements:** Node, ProjectV2Event

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the RemovedFromProjectV2Event object.
- **project** (`ProjectV2`): Project referenced by event.
- **wasAutomated** (`Boolean!`): Did this event result from workflow automation?.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **ProjectCardConnection** (4 fields): The connection type for ProjectCard.
- **ProjectCardEdge** (2 fields): An edge in a connection.
- **ProjectColumnConnection** (4 fields): The connection type for ProjectColumn.
- **ProjectColumnEdge** (2 fields): An edge in a connection.
- **ProjectConnection** (4 fields): A list of projects associated with the owner.
- **ProjectEdge** (2 fields): An edge in a connection.
- **ProjectV2ActorConnection** (4 fields): The connection type for ProjectV2Actor.
- **ProjectV2ActorEdge** (2 fields): An edge in a connection.
- **ProjectV2Connection** (4 fields): The connection type for ProjectV2.
- **ProjectV2Edge** (2 fields): An edge in a connection.
- **ProjectV2FieldConfigurationConnection** (4 fields): The connection type for ProjectV2FieldConfiguration.
- **ProjectV2FieldConfigurationEdge** (2 fields): An edge in a connection.
- **ProjectV2FieldConnection** (4 fields): The connection type for ProjectV2Field.
- **ProjectV2FieldEdge** (2 fields): An edge in a connection.
- **ProjectV2ItemConnection** (4 fields): The connection type for ProjectV2Item.
- **ProjectV2ItemEdge** (2 fields): An edge in a connection.
- **ProjectV2ItemFieldValueConnection** (4 fields): The connection type for ProjectV2ItemFieldValue.
- **ProjectV2ItemFieldValueEdge** (2 fields): An edge in a connection.
- **ProjectV2SortByConnection** (4 fields): The connection type for ProjectV2SortBy.
- **ProjectV2SortByEdge** (2 fields): An edge in a connection.
- **ProjectV2SortByFieldConnection** (4 fields): The connection type for ProjectV2SortByField.
- **ProjectV2SortByFieldEdge** (2 fields): An edge in a connection.
- **ProjectV2StatusUpdateConnection** (4 fields): The connection type for ProjectV2StatusUpdate.
- **ProjectV2StatusUpdateEdge** (2 fields): An edge in a connection.
- **ProjectV2ViewConnection** (4 fields): The connection type for ProjectV2View.
- **ProjectV2ViewEdge** (2 fields): An edge in a connection.
- **ProjectV2WorkflowConnection** (4 fields): The connection type for ProjectV2Workflow.
- **ProjectV2WorkflowEdge** (2 fields): An edge in a connection.

## Interfaces

### ProjectOwner

Represents an owner of a Project.

**Fields:**

- **id** (`ID!`): The Node ID of the ProjectOwner object.
- **project** (`Project`): Find project by number.
- **projects** (`ProjectConnection!`): A list of projects under the owner.
- **projectsResourcePath** (`URI!`): The HTTP path listing owners projects.
- **projectsUrl** (`URI!`): The HTTP URL listing owners projects.
- **viewerCanCreateProjects** (`Boolean!`): Can the current viewer create new projects on this owner.

### ProjectV2Event

Represents an event related to a project on the timeline of an issue or pull request.

**Fields:**

- **project** (`ProjectV2`): Project referenced by event.
- **wasAutomated** (`Boolean!`): Did this event result from workflow automation?.

### ProjectV2FieldCommon

Common fields across different project field types.

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **dataType** (`ProjectV2FieldType!`): The field's type.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the ProjectV2FieldCommon object.
- **name** (`String!`): The project field's name.
- **project** (`ProjectV2!`): The project that contains this field.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2ItemFieldValueCommon

Common fields across different project field value types.

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **creator** (`Actor`): The actor who created the item.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **field** (`ProjectV2FieldConfiguration!`): The project field that contains this value.
- **id** (`ID!`): The Node ID of the ProjectV2ItemFieldValueCommon object.
- **item** (`ProjectV2Item!`): The project item that contains this value.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### ProjectV2Owner

Represents an owner of a project.

**Fields:**

- **id** (`ID!`): The Node ID of the ProjectV2Owner object.
- **projectV2** (`ProjectV2`): Find a project by number.
- **projectsV2** (`ProjectV2Connection!`): A list of projects under the owner.

### ProjectV2Recent

Recent projects for the owner.

**Fields:**

- **recentProjects** (`ProjectV2Connection!`): Recent projects that this user has modified in the context of the owner.

## Enums

### ProjectCardArchivedState

The possible archived states of a project card.

**Values:**

- `ARCHIVED`: A project card that is archived.
- `NOT_ARCHIVED`: A project card that is not archived.

### ProjectCardState

Various content states of a ProjectCard.

**Values:**

- `CONTENT_ONLY`: The card has content only.
- `NOTE_ONLY`: The card has a note only.
- `REDACTED`: The card is redacted.

### ProjectColumnPurpose

The semantic purpose of the column - todo, in progress, or done.

**Values:**

- `DONE`: The column contains cards which are complete.
- `IN_PROGRESS`: The column contains cards which are currently being worked on.
- `TODO`: The column contains cards still to be worked on.

### ProjectOrderField

Properties by which project connections can be ordered.

**Values:**

- `CREATED_AT`: Order projects by creation time.
- `NAME`: Order projects by name.
- `UPDATED_AT`: Order projects by update time.

### ProjectState

State of the project; either`open`or 'closed'.

**Values:**

- `CLOSED`: The project is closed.
- `OPEN`: The project is open.

### ProjectTemplate

GitHub-provided templates for Projects.

**Values:**

- `AUTOMATED_KANBAN_V2`: Create a board with v2 triggers to automatically move cards across To do, In progress and Done columns.
- `AUTOMATED_REVIEWS_KANBAN`: Create a board with triggers to automatically move cards across columns with review automation.
- `BASIC_KANBAN`: Create a board with columns for To do, In progress and Done.
- `BUG_TRIAGE`: Create a board to triage and prioritize bugs with To do, priority, and Done columns.

### ProjectV2CustomFieldType

The type of a project field.

**Values:**

- `DATE`: Date.
- `ITERATION`: Iteration.
- `NUMBER`: Number.
- `SINGLE_SELECT`: Single Select.
- `TEXT`: Text.

### ProjectV2FieldOrderField

Properties by which project v2 field connections can be ordered.

**Values:**

- `CREATED_AT`: Order project v2 fields by creation time.
- `NAME`: Order project v2 fields by name.
- `POSITION`: Order project v2 fields by position.

### ProjectV2FieldType

The type of a project field.

**Values:**

- `ASSIGNEES`: Assignees.
- `DATE`: Date.
- `ISSUE_TYPE`: Issue type.
- `ITERATION`: Iteration.
- `LABELS`: Labels.
- `LINKED_PULL_REQUESTS`: Linked Pull Requests.
- `MILESTONE`: Milestone.
- `NUMBER`: Number.
- `PARENT_ISSUE`: Parent issue.
- `REPOSITORY`: Repository.
- `REVIEWERS`: Reviewers.
- `SINGLE_SELECT`: Single Select.
- `SUB_ISSUES_PROGRESS`: Sub-issues progress.
- `TEXT`: Text.
- `TITLE`: Title.
- `TRACKED_BY`: Tracked by.
- `TRACKS`: Tracks.

### ProjectV2ItemFieldValueOrderField

Properties by which project v2 item field value connections can be ordered.

**Values:**

- `POSITION`: Order project v2 item field values by the their position in the project.

### ProjectV2ItemOrderField

Properties by which project v2 item connections can be ordered.

**Values:**

- `POSITION`: Order project v2 items by the their position in the project.

### ProjectV2ItemType

The type of a project item.

**Values:**

- `DRAFT_ISSUE`: Draft Issue.
- `ISSUE`: Issue.
- `PULL_REQUEST`: Pull Request.
- `REDACTED`: Redacted Item.

### ProjectV2OrderField

Properties by which projects can be ordered.

**Values:**

- `CREATED_AT`: The project's date and time of creation.
- `NUMBER`: The project's number.
- `TITLE`: The project's title.
- `UPDATED_AT`: The project's date and time of update.

### ProjectV2PermissionLevel

The possible roles of a collaborator on a project.

**Values:**

- `ADMIN`: The collaborator can view, edit, and maange the settings of the project.
- `READ`: The collaborator can view the project.
- `WRITE`: The collaborator can view and edit the project.

### ProjectV2Roles

The possible roles of a collaborator on a project.

**Values:**

- `ADMIN`: The collaborator can view, edit, and maange the settings of the project.
- `NONE`: The collaborator has no direct access to the project.
- `READER`: The collaborator can view the project.
- `WRITER`: The collaborator can view and edit the project.

### ProjectV2SingleSelectFieldOptionColor

The display color of a single-select field option.

**Values:**

- `BLUE`: BLUE.
- `GRAY`: GRAY.
- `GREEN`: GREEN.
- `ORANGE`: ORANGE.
- `PINK`: PINK.
- `PURPLE`: PURPLE.
- `RED`: RED.
- `YELLOW`: YELLOW.

### ProjectV2State

The possible states of a project v2.

**Values:**

- `CLOSED`: A project v2 that has been closed.
- `OPEN`: A project v2 that is still open.

### ProjectV2StatusUpdateOrderField

Properties by which project v2 status updates can be ordered.

**Values:**

- `CREATED_AT`: Allows chronological ordering of project v2 status updates.

### ProjectV2StatusUpdateStatus

The possible statuses of a project v2.

**Values:**

- `AT_RISK`: A project v2 that is at risk and encountering some challenges.
- `COMPLETE`: A project v2 that is complete.
- `INACTIVE`: A project v2 that is inactive.
- `OFF_TRACK`: A project v2 that is off track and needs attention.
- `ON_TRACK`: A project v2 that is on track with no risks.

### ProjectV2ViewLayout

The layout of a project v2 view.

**Values:**

- `BOARD_LAYOUT`: Board layout.
- `ROADMAP_LAYOUT`: Roadmap layout.
- `TABLE_LAYOUT`: Table layout.

### ProjectV2ViewOrderField

Properties by which project v2 view connections can be ordered.

**Values:**

- `CREATED_AT`: Order project v2 views by creation time.
- `NAME`: Order project v2 views by name.
- `POSITION`: Order project v2 views by position.

### ProjectV2WorkflowsOrderField

Properties by which project workflows can be ordered.

**Values:**

- `CREATED_AT`: The date and time of the workflow creation.
- `NAME`: The name of the workflow.
- `NUMBER`: The number of the workflow.
- `UPDATED_AT`: The date and time of the workflow update.

## Input Objects

### AddProjectCardInput

Autogenerated input type of AddProjectCard.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **contentId** (`ID`): The content of the card. Must be a member of the ProjectCardItem union.
- **note** (`String`): The note on the card.
- **projectColumnId** (`ID!`): The Node ID of the ProjectColumn.

### AddProjectColumnInput

Autogenerated input type of AddProjectColumn.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **name** (`String!`): The name of the column.
- **projectId** (`ID!`): The Node ID of the project.

### AddProjectV2ItemByIdInput

Autogenerated input type of AddProjectV2ItemById.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **contentId** (`ID!`): The id of the Issue or Pull Request to add.
- **projectId** (`ID!`): The ID of the Project to add the item to.

### ArchiveProjectV2ItemInput

Autogenerated input type of ArchiveProjectV2Item.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **itemId** (`ID!`): The ID of the ProjectV2Item to archive.
- **projectId** (`ID!`): The ID of the Project to archive the item from.

### ClearProjectV2ItemFieldValueInput

Autogenerated input type of ClearProjectV2ItemFieldValue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **fieldId** (`ID!`): The ID of the field to be cleared.
- **itemId** (`ID!`): The ID of the item to be cleared.
- **projectId** (`ID!`): The ID of the Project.

### CloneProjectInput

Autogenerated input type of CloneProject.

**Input fields:**

- **body** (`String`): The description of the project.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **includeWorkflows** (`Boolean!`): Whether or not to clone the source project's workflows.
- **name** (`String!`): The name of the project.
- **public** (`Boolean`): The visibility of the project, defaults to false (private).
- **sourceId** (`ID!`): The source project to clone.
- **targetOwnerId** (`ID!`): The owner ID to create the project under.

### CopyProjectV2Input

Autogenerated input type of CopyProjectV2.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **includeDraftIssues** (`Boolean`): Include draft issues in the new project.
- **ownerId** (`ID!`): The owner ID of the new project.
- **projectId** (`ID!`): The ID of the source Project to copy.
- **title** (`String!`): The title of the project.

### CreateProjectInput

Autogenerated input type of CreateProject.

**Input fields:**

- **body** (`String`): The description of project.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **name** (`String!`): The name of project.
- **ownerId** (`ID!`): The owner ID to create the project under.
- **repositoryIds** (`[ID!]`): A list of repository IDs to create as linked repositories for the project.
- **template** (`ProjectTemplate`): The name of the GitHub-provided template.

### CreateProjectV2FieldInput

Autogenerated input type of CreateProjectV2Field.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **dataType** (`ProjectV2CustomFieldType!`): The data type of the field.
- **iterationConfiguration** (`ProjectV2IterationFieldConfigurationInput`): Configuration for an iteration field.
- **name** (`String!`): The name of the field.
- **projectId** (`ID!`): The ID of the Project to create the field in.
- **singleSelectOptions** (`[ProjectV2SingleSelectFieldOptionInput!]`): Options for a single select field. At least one value is required if data_type is SINGLE_SELECT.

### CreateProjectV2Input

Autogenerated input type of CreateProjectV2.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ownerId** (`ID!`): The owner ID to create the project under.
- **repositoryId** (`ID`): The repository to link the project to.
- **teamId** (`ID`): The team to link the project to. The team will be granted read permissions.
- **title** (`String!`): The title of the project.

### CreateProjectV2StatusUpdateInput

Autogenerated input type of CreateProjectV2StatusUpdate.

**Input fields:**

- **body** (`String`): The body of the status update.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the Project to create the status update in.
- **startDate** (`Date`): The start date of the status update.
- **status** (`ProjectV2StatusUpdateStatus`): The status of the status update.
- **targetDate** (`Date`): The target date of the status update.

### DeleteProjectCardInput

Autogenerated input type of DeleteProjectCard.

**Input fields:**

- **cardId** (`ID!`): The id of the card to delete.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.

### DeleteProjectColumnInput

Autogenerated input type of DeleteProjectColumn.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **columnId** (`ID!`): The id of the column to delete.

### DeleteProjectInput

Autogenerated input type of DeleteProject.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The Project ID to update.

### DeleteProjectV2FieldInput

Autogenerated input type of DeleteProjectV2Field.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **fieldId** (`ID!`): The ID of the field to delete.

### DeleteProjectV2Input

Autogenerated input type of DeleteProjectV2.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the Project to delete.

### DeleteProjectV2ItemInput

Autogenerated input type of DeleteProjectV2Item.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **itemId** (`ID!`): The ID of the item to be removed.
- **projectId** (`ID!`): The ID of the Project from which the item should be removed.

### DeleteProjectV2StatusUpdateInput

Autogenerated input type of DeleteProjectV2StatusUpdate.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **statusUpdateId** (`ID!`): The ID of the status update to be removed.

### DeleteProjectV2WorkflowInput

Autogenerated input type of DeleteProjectV2Workflow.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **workflowId** (`ID!`): The ID of the workflow to be removed.

### ImportProjectInput

Autogenerated input type of ImportProject.

**Input fields:**

- **body** (`String`): The description of Project.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **columnImports** (`[ProjectColumnImport!]!`): A list of columns containing issues and pull requests.
- **name** (`String!`): The name of Project.
- **ownerName** (`String!`): The name of the Organization or User to create the Project under.
- **public** (`Boolean`): Whether the Project is public or not.

### MarkProjectV2AsTemplateInput

Autogenerated input type of MarkProjectV2AsTemplate.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the Project to mark as a template.

### MoveProjectCardInput

Autogenerated input type of MoveProjectCard.

**Input fields:**

- **afterCardId** (`ID`): Place the new card after the card with this id. Pass null to place it at the top.
- **cardId** (`ID!`): The id of the card to move.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **columnId** (`ID!`): The id of the column to move it into.

### MoveProjectColumnInput

Autogenerated input type of MoveProjectColumn.

**Input fields:**

- **afterColumnId** (`ID`): Place the new column after the column with this id. Pass null to place it at the front.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **columnId** (`ID!`): The id of the column to move.

### ProjectCardImport

An issue or PR and its owning repository to be used in a project card.

**Input fields:**

- **number** (`Int!`): The issue or pull request number.
- **repository** (`String!`): Repository name with owner (owner/repository).

### ProjectColumnImport

A project column and a list of its issues and PRs.

**Input fields:**

- **columnName** (`String!`): The name of the column.
- **issues** (`[ProjectCardImport!]`): A list of issues and pull requests in the column.
- **position** (`Int!`): The position of the column, starting from 0.

### ProjectOrder

Ways in which lists of projects can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order projects by the specified field.
- **field** (`ProjectOrderField!`): The field in which to order projects by.

### ProjectV2Collaborator

A collaborator to update on a project. Only one of the userId or teamId should be provided.

**Input fields:**

- **role** (`ProjectV2Roles!`): The role to grant the collaborator.
- **teamId** (`ID`): The ID of the team as a collaborator.
- **userId** (`ID`): The ID of the user as a collaborator.

### ProjectV2FieldOrder

Ordering options for project v2 field connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`ProjectV2FieldOrderField!`): The field to order the project v2 fields by.

### ProjectV2FieldValue

The values that can be used to update a field of an item inside a Project. Only 1 value can be updated at a time.

**Input fields:**

- **date** (`Date`): The ISO 8601 date to set on the field.
- **iterationId** (`String`): The id of the iteration to set on the field.
- **number** (`Float`): The number to set on the field.
- **singleSelectOptionId** (`String`): The id of the single select option to set on the field.
- **text** (`String`): The text to set on the field.

### ProjectV2Filters

Ways in which to filter lists of projects.

**Input fields:**

- **state** (`ProjectV2State`): List project v2 filtered by the state given.

### ProjectV2ItemFieldValueOrder

Ordering options for project v2 item field value connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`ProjectV2ItemFieldValueOrderField!`): The field to order the project v2 item field values by.

### ProjectV2ItemOrder

Ordering options for project v2 item connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`ProjectV2ItemOrderField!`): The field to order the project v2 items by.

### ProjectV2Iteration

Represents an iteration.

**Input fields:**

- **duration** (`Int!`): The duration of the iteration, in days.
- **startDate** (`Date!`): The start date for the iteration.
- **title** (`String!`): The title for the iteration.

### ProjectV2IterationFieldConfigurationInput

Represents an iteration field configuration.

**Input fields:**

- **duration** (`Int!`): The duration of each iteration, in days.
- **iterations** (`[ProjectV2Iteration!]!`): Zero or more iterations for the field.
- **startDate** (`Date!`): The start date for the first iteration.

### ProjectV2Order

Ways in which lists of projects can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order projects by the specified field.
- **field** (`ProjectV2OrderField!`): The field in which to order projects by.

### ProjectV2SingleSelectFieldOptionInput

Represents a single select field option.

**Input fields:**

- **color** (`ProjectV2SingleSelectFieldOptionColor!`): The display color of the option.
- **description** (`String!`): The description text of the option.
- **id** (`String`): The ID of an existing single select option. Include this to preserve the
option's identity during updates, preventing item field values from being cleared.
- **name** (`String!`): The name of the option.

### ProjectV2StatusOrder

Ways in which project v2 status updates can be ordered.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order nodes.
- **field** (`ProjectV2StatusUpdateOrderField!`): The field by which to order nodes.

### ProjectV2ViewOrder

Ordering options for project v2 view connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`ProjectV2ViewOrderField!`): The field to order the project v2 views by.

### ProjectV2WorkflowOrder

Ordering options for project v2 workflows connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`ProjectV2WorkflowsOrderField!`): The field to order the project v2 workflows by.

### UnarchiveProjectV2ItemInput

Autogenerated input type of UnarchiveProjectV2Item.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **itemId** (`ID!`): The ID of the ProjectV2Item to unarchive.
- **projectId** (`ID!`): The ID of the Project to archive the item from.

### UnmarkProjectV2AsTemplateInput

Autogenerated input type of UnmarkProjectV2AsTemplate.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the Project to unmark as a template.

### UpdateProjectCardInput

Autogenerated input type of UpdateProjectCard.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **isArchived** (`Boolean`): Whether or not the ProjectCard should be archived.
- **note** (`String`): The note of ProjectCard.
- **projectCardId** (`ID!`): The ProjectCard ID to update.

### UpdateProjectColumnInput

Autogenerated input type of UpdateProjectColumn.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **name** (`String!`): The name of project column.
- **projectColumnId** (`ID!`): The ProjectColumn ID to update.

### UpdateProjectInput

Autogenerated input type of UpdateProject.

**Input fields:**

- **body** (`String`): The description of project.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **name** (`String`): The name of project.
- **projectId** (`ID!`): The Project ID to update.
- **public** (`Boolean`): Whether the project is public or not.
- **state** (`ProjectState`): Whether the project is open or closed.

### UpdateProjectV2CollaboratorsInput

Autogenerated input type of UpdateProjectV2Collaborators.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **collaborators** (`[ProjectV2Collaborator!]!`): The collaborators to update.
- **projectId** (`ID!`): The ID of the project to update the collaborators for.

### UpdateProjectV2FieldInput

Autogenerated input type of UpdateProjectV2Field.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **fieldId** (`ID!`): The ID of the field to update.
- **iterationConfiguration** (`ProjectV2IterationFieldConfigurationInput`): Configuration for a field of type ITERATION. Empty input is ignored, provided
values overwrite the existing configuration, and existing configuration should
be fetched for partial updates.
- **name** (`String`): The name to update.
- **singleSelectOptions** (`[ProjectV2SingleSelectFieldOptionInput!]`): Options for a field of type SINGLE_SELECT. Empty input is ignored, provided
values overwrite existing options, and existing options should be fetched for
partial updates.

### UpdateProjectV2Input

Autogenerated input type of UpdateProjectV2.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **closed** (`Boolean`): Set the project to closed or open.
- **projectId** (`ID!`): The ID of the Project to update.
- **public** (`Boolean`): Set the project to public or private.
- **readme** (`String`): Set the readme description of the project.
- **shortDescription** (`String`): Set the short description of the project.
- **title** (`String`): Set the title of the project.

### UpdateProjectV2ItemFieldValueInput

Autogenerated input type of UpdateProjectV2ItemFieldValue.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **fieldId** (`ID!`): The ID of the field to be updated.
- **itemId** (`ID!`): The ID of the item to be updated.
- **projectId** (`ID!`): The ID of the Project.
- **value** (`ProjectV2FieldValue!`): The value which will be set on the field.

### UpdateProjectV2ItemPositionInput

Autogenerated input type of UpdateProjectV2ItemPosition.

**Input fields:**

- **afterId** (`ID`): The ID of the item to position this item after. If omitted or set to null the item will be moved to top.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **itemId** (`ID!`): The ID of the item to be moved.
- **projectId** (`ID!`): The ID of the Project.

### UpdateProjectV2StatusUpdateInput

Autogenerated input type of UpdateProjectV2StatusUpdate.

**Input fields:**

- **body** (`String`): The body of the status update.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **startDate** (`Date`): The start date of the status update.
- **status** (`ProjectV2StatusUpdateStatus`): The status of the status update.
- **statusUpdateId** (`ID!`): The ID of the status update to be updated.
- **targetDate** (`Date`): The target date of the status update.

## Unions

### ProjectCardItem

Types that can be inside Project Cards.

**Possible types:** Issue, PullRequest

### ProjectV2Actor

Possible collaborators for a project.

**Possible types:** Team, User

### ProjectV2FieldConfiguration

Configurations for project fields.

**Possible types:** ProjectV2Field, ProjectV2IterationField, ProjectV2SingleSelectField

### ProjectV2ItemContent

Types that can be inside Project Items.

**Possible types:** DraftIssue, Issue, PullRequest

### ProjectV2ItemFieldValue

Project field values.

**Possible types:** ProjectV2ItemFieldDateValue, ProjectV2ItemFieldIterationValue, ProjectV2ItemFieldLabelValue, ProjectV2ItemFieldMilestoneValue, ProjectV2ItemFieldNumberValue, ProjectV2ItemFieldPullRequestValue, ProjectV2ItemFieldRepositoryValue, ProjectV2ItemFieldReviewerValue, ProjectV2ItemFieldSingleSelectValue, ProjectV2ItemFieldTextValue, ProjectV2ItemFieldUserValue, ProjectV2ItemIssueFieldValue
