# GitHub GraphQL API — Recent Schema Changes

Last 50 changelog entries (most recent first).

## 2026-04-15

**The GraphQL schema includes these changes:**

- Type `ArchivePullRequestInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `ArchivePullRequestInput`
- Input field `pullRequestId` of type `ID!` was added to input object type `ArchivePullRequestInput`
- Type `ArchivePullRequestPayload` was added
- Field `clientMutationId` was added to object type `ArchivePullRequestPayload`
- Field `pullRequest` was added to object type `ArchivePullRequestPayload`
- Type `UnarchivePullRequestInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `UnarchivePullRequestInput`
- Input field `pullRequestId` of type `ID!` was added to input object type `UnarchivePullRequestInput`
- Type `UnarchivePullRequestPayload` was added
- Field `clientMutationId` was added to object type `UnarchivePullRequestPayload`
- Field `pullRequest` was added to object type `UnarchivePullRequestPayload`
- Field `archivePullRequest` was added to object type `Mutation`
- Argument `input: ArchivePullRequestInput!` added to field `Mutation.archivePullRequest`
- Field `unarchivePullRequest` was added to object type `Mutation`
- Argument `input: UnarchivePullRequestInput!` added to field `Mutation.unarchivePullRequest`

## 2026-04-02

**The GraphQL schema includes these changes:**

- Argument 'classifications: [SecurityAdvisoryClassification!]`added to field`Repository.vulnerabilityAlerts'

## 2026-03-31

**The GraphQL schema includes these changes:**

- Field `value` was added to object type `IssueFieldSingleSelectValue`

## 2026-03-30

**The GraphQL schema includes these changes:**

- Type `IssueFieldAddedEvent` was added
- `IssueFieldAddedEvent` object implements `Node` interface
- Field `actor` was added to object type `IssueFieldAddedEvent`
- Field `color` was added to object type `IssueFieldAddedEvent`
- Field `createdAt` was added to object type `IssueFieldAddedEvent`
- Field `id` was added to object type `IssueFieldAddedEvent`
- Field `issueField` was added to object type `IssueFieldAddedEvent`
- Field `value` was added to object type `IssueFieldAddedEvent`
- Type `IssueFieldChangedEvent` was added
- `IssueFieldChangedEvent` object implements `Node` interface
- Field `actor` was added to object type `IssueFieldChangedEvent`
- Field `createdAt` was added to object type `IssueFieldChangedEvent`
- Field `id` was added to object type `IssueFieldChangedEvent`
- Field `issueField` was added to object type `IssueFieldChangedEvent`
- Field `newColor` was added to object type `IssueFieldChangedEvent`
- Field `newValue` was added to object type `IssueFieldChangedEvent`
- Field `previousColor` was added to object type `IssueFieldChangedEvent`
- Field `previousValue` was added to object type `IssueFieldChangedEvent`
- Type `IssueFieldRemovedEvent` was added
- `IssueFieldRemovedEvent` object implements `Node` interface
- Field `actor` was added to object type `IssueFieldRemovedEvent`
- Field `createdAt` was added to object type `IssueFieldRemovedEvent`
- Field `id` was added to object type `IssueFieldRemovedEvent`
- Field `issueField` was added to object type `IssueFieldRemovedEvent`
- Type `IssueSearchType` was added
- Enum value `HYBRID` was added to enum `IssueSearchType`
- Enum value `LEXICAL` was added to enum `IssueSearchType`
- Enum value `SEMANTIC` was added to enum `IssueSearchType`
- Type `LexicalFallbackReason` was added
- Enum value 'NON_ISSUE_TARGET`was added to enum`LexicalFallbackReason'
- Enum value 'NO_ACCESSIBLE_REPOS`was added to enum`LexicalFallbackReason'
- Enum value 'NO_TEXT_TERMS`was added to enum`LexicalFallbackReason'
- Enum value 'ONLY_NON_SEMANTIC_FIELDS_REQUESTED`was added to enum`LexicalFallbackReason'
- Enum value 'OR_BOOLEAN_NOT_SUPPORTED`was added to enum`LexicalFallbackReason'
- Enum value 'QUOTED_TEXT`was added to enum`LexicalFallbackReason'
- Enum value 'SERVER_ERROR`was added to enum`LexicalFallbackReason'
- Member `IssueFieldAddedEvent` was added to Union type `IssueTimelineItems`
- Member `IssueFieldChangedEvent` was added to Union type `IssueTimelineItems`
- Member `IssueFieldRemovedEvent` was added to Union type `IssueTimelineItems`
- Member `IssueFieldAddedEvent` was added to Union type `PullRequestTimelineItems`
- Member `IssueFieldChangedEvent` was added to Union type `PullRequestTimelineItems`
- Member `IssueFieldRemovedEvent` was added to Union type `PullRequestTimelineItems`
- Field `issueSearchType` was added to object type `SearchResultItemConnection`
- Field `lexicalFallbackReason` was added to object type `SearchResultItemConnection`
- Enum value 'ISSUE_HYBRID`was added to enum`SearchType'
- Enum value 'ISSUE_SEMANTIC`was added to enum`SearchType'

## 2026-03-17

**The GraphQL schema includes these changes:**

- Field `optionId` was added to object type `IssueFieldSingleSelectValue`

## 2026-03-16

**The GraphQL schema includes these changes:**

- Member `User` was added to Union type `BypassActor`

## 2026-03-12

**The GraphQL schema includes these changes:**

- Type `CreateIssueFieldInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `CreateIssueFieldInput`
- Input field `dataType` of type `IssueFieldDataType!` was added to input object type `CreateIssueFieldInput`
- Input field `description` of type `String` was added to input object type `CreateIssueFieldInput`
- Input field `name` of type `String!` was added to input object type `CreateIssueFieldInput`
- Input field `options` of type '[IssueFieldSingleSelectOptionInput!]`was added to input object type`CreateIssueFieldInput'
- Input field `ownerId` of type `ID!` was added to input object type `CreateIssueFieldInput`
- Input field `visibility` of type `IssueFieldVisibility` was added to input object type `CreateIssueFieldInput`
- Type `CreateIssueFieldPayload` was added
- Field `clientMutationId` was added to object type `CreateIssueFieldPayload`
- Field `issueField` was added to object type `CreateIssueFieldPayload`
- Type `CreateIssueFieldValueInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `CreateIssueFieldValueInput`
- Input field `issueField` of type `IssueFieldCreateOrUpdateInput!` was added to input object type `CreateIssueFieldValueInput`
- Input field `issueId` of type `ID!` was added to input object type `CreateIssueFieldValueInput`
- Type `CreateIssueFieldValuePayload` was added
- Field `clientMutationId` was added to object type `CreateIssueFieldValuePayload`
- Field `issue` was added to object type `CreateIssueFieldValuePayload`
- Field `issueFieldValue` was added to object type `CreateIssueFieldValuePayload`
- Type 'CreateProjectV2IssueFieldInput' was added
- Input field `clientMutationId` of type `String` was added to input object type 'CreateProjectV2IssueFieldInput'
- Input field `issueFieldId` of type `ID!` was added to input object type 'CreateProjectV2IssueFieldInput'
- Input field `projectId` of type `ID!` was added to input object type 'CreateProjectV2IssueFieldInput'
- Type 'CreateProjectV2IssueFieldPayload' was added
- Field `clientMutationId` was added to object type 'CreateProjectV2IssueFieldPayload'
- Field 'projectV2Field`was added to object type`CreateProjectV2IssueFieldPayload'
- Type `DeleteIssueFieldInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `DeleteIssueFieldInput`
- Input field `fieldId` of type `ID!` was added to input object type `DeleteIssueFieldInput`
- Type `DeleteIssueFieldPayload` was added
- Field `clientMutationId` was added to object type `DeleteIssueFieldPayload`
- Field `issueField` was added to object type `DeleteIssueFieldPayload`
- Type `DeleteIssueFieldValueInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `DeleteIssueFieldValueInput`
- Input field `fieldId` of type `ID!` was added to input object type `DeleteIssueFieldValueInput`
- Input field `issueId` of type `ID!` was added to input object type `DeleteIssueFieldValueInput`
- Type `DeleteIssueFieldValuePayload` was added
- Field `clientMutationId` was added to object type `DeleteIssueFieldValuePayload`
- Field `issue` was added to object type `DeleteIssueFieldValuePayload`
- Field `success` was added to object type `DeleteIssueFieldValuePayload`
- Type `IssueCommentPinnedEvent` was added
- `IssueCommentPinnedEvent` object implements `Node` interface
- Field `actor` was added to object type `IssueCommentPinnedEvent`
- Field `createdAt` was added to object type `IssueCommentPinnedEvent`
- Field `id` was added to object type `IssueCommentPinnedEvent`
- Field `issueComment` was added to object type `IssueCommentPinnedEvent`
- Type `IssueCommentUnpinnedEvent` was added
- `IssueCommentUnpinnedEvent` object implements `Node` interface
- Field `actor` was added to object type `IssueCommentUnpinnedEvent`
- Field `createdAt` was added to object type `IssueCommentUnpinnedEvent`
- Field `id` was added to object type `IssueCommentUnpinnedEvent`
- Field `issueComment` was added to object type `IssueCommentUnpinnedEvent`
- Type `IssueFieldCommon` was added
- Field `createdAt` was added to interface `IssueFieldCommon`
- Field `dataType` was added to interface `IssueFieldCommon`
- Field `description` was added to interface `IssueFieldCommon`
- Field `name` was added to interface `IssueFieldCommon`
- Field `visibility` was added to interface `IssueFieldCommon`
- Type `IssueFieldCreateOrUpdateInput` was added
- Input field `dateValue` of type `String` was added to input object type `IssueFieldCreateOrUpdateInput`
- Input field `delete` of type `Boolean` was added to input object type `IssueFieldCreateOrUpdateInput`
- Input field `fieldId` of type `ID!` was added to input object type `IssueFieldCreateOrUpdateInput`
- Input field `numberValue` of type `Float` was added to input object type `IssueFieldCreateOrUpdateInput`
- Input field `singleSelectOptionId` of type `ID` was added to input object type `IssueFieldCreateOrUpdateInput`
- Input field `textValue` of type `String` was added to input object type `IssueFieldCreateOrUpdateInput`
- Type `IssueFieldDataType` was added
- Enum value `DATE` was added to enum `IssueFieldDataType`
- Enum value `NUMBER` was added to enum `IssueFieldDataType`
- Enum value 'SINGLE_SELECT`was added to enum`IssueFieldDataType'
- Enum value `TEXT` was added to enum `IssueFieldDataType`
- Type `IssueFieldDate` was added
- `IssueFieldDate` object implements `IssueFieldCommon` interface
- `IssueFieldDate` object implements `Node` interface
- Field `createdAt` was added to object type `IssueFieldDate`
- Field `dataType` was added to object type `IssueFieldDate`
- Field `description` was added to object type `IssueFieldDate`
- Field `id` was added to object type `IssueFieldDate`
- Field `name` was added to object type `IssueFieldDate`
- Field `visibility` was added to object type `IssueFieldDate`
- Type `IssueFieldDateValue` was added
- `IssueFieldDateValue` object implements `IssueFieldValueCommon` interface
- `IssueFieldDateValue` object implements `Node` interface
- Field `field` was added to object type `IssueFieldDateValue`
- Field `id` was added to object type `IssueFieldDateValue`
- Field `value` was added to object type `IssueFieldDateValue`
- Type `IssueFieldNumber` was added
- `IssueFieldNumber` object implements `IssueFieldCommon` interface
- `IssueFieldNumber` object implements `Node` interface
- Field `createdAt` was added to object type `IssueFieldNumber`
- Field `dataType` was added to object type `IssueFieldNumber`
- Field `description` was added to object type `IssueFieldNumber`
- Field `id` was added to object type `IssueFieldNumber`
- Field `name` was added to object type `IssueFieldNumber`
- Field `visibility` was added to object type `IssueFieldNumber`
- Type `IssueFieldNumberValue` was added
- `IssueFieldNumberValue` object implements `IssueFieldValueCommon` interface
- `IssueFieldNumberValue` object implements `Node` interface
- Field `field` was added to object type `IssueFieldNumberValue`
- Field `id` was added to object type `IssueFieldNumberValue`
- Field `value` was added to object type `IssueFieldNumberValue`
- Type `IssueFieldOrder` was added
- Input field `direction` of type `OrderDirection!` was added to input object type `IssueFieldOrder`
- Input field `field` of type `IssueFieldOrderField!` was added to input object type `IssueFieldOrder`
- Type `IssueFieldOrderField` was added
- Enum value 'CREATED_AT`was added to enum`IssueFieldOrderField'
- Enum value `NAME` was added to enum `IssueFieldOrderField`
- Type `IssueFieldSingleSelect` was added
- `IssueFieldSingleSelect` object implements `IssueFieldCommon` interface
- `IssueFieldSingleSelect` object implements `Node` interface
- Field `createdAt` was added to object type `IssueFieldSingleSelect`
- Field `dataType` was added to object type `IssueFieldSingleSelect`
- Field `description` was added to object type `IssueFieldSingleSelect`
- Field `id` was added to object type `IssueFieldSingleSelect`
- Field `name` was added to object type `IssueFieldSingleSelect`
- Field `options` was added to object type `IssueFieldSingleSelect`
- Field `visibility` was added to object type `IssueFieldSingleSelect`
- Type `IssueFieldSingleSelectOption` was added
- `IssueFieldSingleSelectOption` object implements `Node` interface
- Field `color` was added to object type `IssueFieldSingleSelectOption`
- Field `description` was added to object type `IssueFieldSingleSelectOption`
- Field `id` was added to object type `IssueFieldSingleSelectOption`
- Field `name` was added to object type `IssueFieldSingleSelectOption`
- Field `priority` was added to object type `IssueFieldSingleSelectOption`
- Type `IssueFieldSingleSelectOptionColor` was added
- Enum value `BLUE` was added to enum `IssueFieldSingleSelectOptionColor`
- Enum value `GRAY` was added to enum `IssueFieldSingleSelectOptionColor`
- Enum value `GREEN` was added to enum `IssueFieldSingleSelectOptionColor`
- Enum value `ORANGE` was added to enum `IssueFieldSingleSelectOptionColor`
- Enum value `PINK` was added to enum `IssueFieldSingleSelectOptionColor`
- Enum value `PURPLE` was added to enum `IssueFieldSingleSelectOptionColor`
- Enum value `RED` was added to enum `IssueFieldSingleSelectOptionColor`
- Enum value `YELLOW` was added to enum `IssueFieldSingleSelectOptionColor`
- Type `IssueFieldSingleSelectOptionInput` was added
- Input field `color` of type `IssueFieldSingleSelectOptionColor!` was added to input object type `IssueFieldSingleSelectOptionInput`
- Input field `description` of type `String` was added to input object type `IssueFieldSingleSelectOptionInput`
- Input field `name` of type `String!` was added to input object type `IssueFieldSingleSelectOptionInput`
- Input field `priority` of type `Int!` was added to input object type `IssueFieldSingleSelectOptionInput`
- Type `IssueFieldSingleSelectValue` was added
- `IssueFieldSingleSelectValue` object implements `IssueFieldValueCommon` interface
- `IssueFieldSingleSelectValue` object implements `Node` interface
- Field `color` was added to object type `IssueFieldSingleSelectValue`
- Field `description` was added to object type `IssueFieldSingleSelectValue`
- Field `field` was added to object type `IssueFieldSingleSelectValue`
- Field `id` was added to object type `IssueFieldSingleSelectValue`
- Field `name` was added to object type `IssueFieldSingleSelectValue`
- Type `IssueFieldText` was added
- `IssueFieldText` object implements `IssueFieldCommon` interface
- `IssueFieldText` object implements `Node` interface
- Field `createdAt` was added to object type `IssueFieldText`
- Field `dataType` was added to object type `IssueFieldText`
- Field `description` was added to object type `IssueFieldText`
- Field `id` was added to object type `IssueFieldText`
- Field `name` was added to object type `IssueFieldText`
- Field `visibility` was added to object type `IssueFieldText`
- Type `IssueFieldTextValue` was added
- `IssueFieldTextValue` object implements `IssueFieldValueCommon` interface
- `IssueFieldTextValue` object implements `Node` interface
- Field `field` was added to object type `IssueFieldTextValue`
- Field `id` was added to object type `IssueFieldTextValue`
- Field `value` was added to object type `IssueFieldTextValue`
- Type `IssueFieldValue` was added
- Member `IssueFieldDateValue` was added to Union type `IssueFieldValue`
- Member `IssueFieldNumberValue` was added to Union type `IssueFieldValue`
- Member `IssueFieldSingleSelectValue` was added to Union type `IssueFieldValue`
- Member `IssueFieldTextValue` was added to Union type `IssueFieldValue`
- Type `IssueFieldValueCommon` was added
- Field `field` was added to interface `IssueFieldValueCommon`
- Type `IssueFieldValueConnection` was added
- Field `edges` was added to object type `IssueFieldValueConnection`
- Field `nodes` was added to object type `IssueFieldValueConnection`
- Field `pageInfo` was added to object type `IssueFieldValueConnection`
- Field `totalCount` was added to object type `IssueFieldValueConnection`
- Type `IssueFieldValueEdge` was added
- Field `cursor` was added to object type `IssueFieldValueEdge`
- Field `node` was added to object type `IssueFieldValueEdge`
- Type `IssueFieldVisibility` was added
- Enum value `ALL` was added to enum `IssueFieldVisibility`
- Enum value 'ORG_ONLY`was added to enum`IssueFieldVisibility'
- Type `IssueFields` was added
- Member `IssueFieldDate` was added to Union type `IssueFields`
- Member `IssueFieldNumber` was added to Union type `IssueFields`
- Member `IssueFieldSingleSelect` was added to Union type `IssueFields`
- Member `IssueFieldText` was added to Union type `IssueFields`
- Type `IssueFieldsConnection` was added
- Field `edges` was added to object type `IssueFieldsConnection`
- Field `nodes` was added to object type `IssueFieldsConnection`
- Field `pageInfo` was added to object type `IssueFieldsConnection`
- Field `totalCount` was added to object type `IssueFieldsConnection`
- Type `IssueFieldsEdge` was added
- Field `cursor` was added to object type `IssueFieldsEdge`
- Field `node` was added to object type `IssueFieldsEdge`
- Type `PinIssueCommentInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `PinIssueCommentInput`
- Input field `issueCommentId` of type `ID!` was added to input object type `PinIssueCommentInput`
- Type `PinIssueCommentPayload` was added
- Field `clientMutationId` was added to object type `PinIssueCommentPayload`
- Field `issueComment` was added to object type `PinIssueCommentPayload`
- Type `Pinnable` was added
- Field `isPinned` was added to interface `Pinnable`
- Field `pinnedAt` was added to interface `Pinnable`
- Field `pinnedBy` was added to interface `Pinnable`
- Field `viewerCanPin` was added to interface `Pinnable`
- Field `viewerCanUnpin` was added to interface `Pinnable`
- Type `PinnedIssueComment` was added
- `PinnedIssueComment` object implements `Node` interface
- Field `databaseId` was added to object type `PinnedIssueComment`
- Field `fullDatabaseId` was added to object type `PinnedIssueComment`
- Field `id` was added to object type `PinnedIssueComment`
- Field `issue` was added to object type `PinnedIssueComment`
- Field `issueComment` was added to object type `PinnedIssueComment`
- Field `pinnedAt` was added to object type `PinnedIssueComment`
- Field `pinnedBy` was added to object type `PinnedIssueComment`
- Type 'ProjectV2IssueFieldValues' was added
- Member `IssueFieldDateValue` was added to Union type 'ProjectV2IssueFieldValues'
- Member `IssueFieldNumberValue` was added to Union type 'ProjectV2IssueFieldValues'
- Member `IssueFieldSingleSelectValue` was added to Union type 'ProjectV2IssueFieldValues'
- Member `IssueFieldTextValue` was added to Union type 'ProjectV2IssueFieldValues'
- Type 'ProjectV2ItemIssueFieldValue' was added
- Field `field` was added to object type 'ProjectV2ItemIssueFieldValue'
- Field `issueFieldValue` was added to object type 'ProjectV2ItemIssueFieldValue'
- Type `SetIssueFieldValueInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `SetIssueFieldValueInput`
- Input field `issueFields` of type '[IssueFieldCreateOrUpdateInput!]!`was added to input object type`SetIssueFieldValueInput'
- Input field `issueId` of type `ID!` was added to input object type `SetIssueFieldValueInput`
- Type `SetIssueFieldValuePayload` was added
- Field `clientMutationId` was added to object type `SetIssueFieldValuePayload`
- Field `issue` was added to object type `SetIssueFieldValuePayload`
- Field `issueFieldValues` was added to object type `SetIssueFieldValuePayload`
- Type `UnpinIssueCommentInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `UnpinIssueCommentInput`
- Input field `issueCommentId` of type `ID!` was added to input object type `UnpinIssueCommentInput`
- Type `UnpinIssueCommentPayload` was added
- Field `clientMutationId` was added to object type `UnpinIssueCommentPayload`
- Field `issueComment` was added to object type `UnpinIssueCommentPayload`
- Type `UpdateIssueFieldInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `UpdateIssueFieldInput`
- Input field `description` of type `String` was added to input object type `UpdateIssueFieldInput`
- Input field `id` of type `ID!` was added to input object type `UpdateIssueFieldInput`
- Input field `name` of type `String` was added to input object type `UpdateIssueFieldInput`
- Input field `options` of type '[IssueFieldSingleSelectOptionInput!]`was added to input object type`UpdateIssueFieldInput'
- Input field `visibility` of type `IssueFieldVisibility` was added to input object type `UpdateIssueFieldInput`
- Type `UpdateIssueFieldPayload` was added
- Field `clientMutationId` was added to object type `UpdateIssueFieldPayload`
- Field `issueField` was added to object type `UpdateIssueFieldPayload`
- Type `UpdateIssueFieldValueInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `UpdateIssueFieldValueInput`
- Input field `issueField` of type `IssueFieldCreateOrUpdateInput!` was added to input object type `UpdateIssueFieldValueInput`
- Input field `issueId` of type `ID!` was added to input object type `UpdateIssueFieldValueInput`
- Type `UpdateIssueFieldValuePayload` was added
- Field `clientMutationId` was added to object type `UpdateIssueFieldValuePayload`
- Field `issue` was added to object type `UpdateIssueFieldValuePayload`
- Field `issueFieldValue` was added to object type `UpdateIssueFieldValuePayload`
- Input field `issueFields` of type '[IssueFieldCreateOrUpdateInput!]`was added to input object type`CreateIssueInput'
- Field `issueFieldValues` was added to object type `Issue`
- Argument `after: String` added to field `Issue.issueFieldValues`
- Argument `before: String` added to field `Issue.issueFieldValues`
- Argument `first: Int` added to field `Issue.issueFieldValues`
- Argument `last: Int` added to field `Issue.issueFieldValues`
- Field `pinnedIssueComment` was added to object type `Issue`
- `IssueComment` object implements `Pinnable` interface
- Field `isPinned` was added to object type `IssueComment`
- Field `pinnedAt` was added to object type `IssueComment`
- Field `pinnedBy` was added to object type `IssueComment`
- Field `viewerCanPin` was added to object type `IssueComment`
- Field `viewerCanUnpin` was added to object type `IssueComment`
- Member `IssueCommentPinnedEvent` was added to Union type `IssueTimelineItems`
- Member `IssueCommentUnpinnedEvent` was added to Union type `IssueTimelineItems`
- Field `pinnedFields` was added to object type `IssueType`
- Field `createIssueField` was added to object type `Mutation`
- Argument `input: CreateIssueFieldInput!` added to field `Mutation.createIssueField`
- Field `createIssueFieldValue` was added to object type `Mutation`
- Argument `input: CreateIssueFieldValueInput!` added to field `Mutation.createIssueFieldValue`
- Field 'createProjectV2IssueField`was added to object type`Mutation'
- Argument 'input: CreateProjectV2IssueFieldInput!`added to field`Mutation.createProjectV2IssueField'
- Field `deleteIssueField` was added to object type `Mutation`
- Argument `input: DeleteIssueFieldInput!` added to field `Mutation.deleteIssueField`
- Field `deleteIssueFieldValue` was added to object type `Mutation`
- Argument `input: DeleteIssueFieldValueInput!` added to field `Mutation.deleteIssueFieldValue`
- Field `pinIssueComment` was added to object type `Mutation`
- Argument `input: PinIssueCommentInput!` added to field `Mutation.pinIssueComment`
- Field `setIssueFieldValue` was added to object type `Mutation`
- Argument `input: SetIssueFieldValueInput!` added to field `Mutation.setIssueFieldValue`
- Field `unpinIssueComment` was added to object type `Mutation`
- Argument `input: UnpinIssueCommentInput!` added to field `Mutation.unpinIssueComment`
- Field `updateIssueField` was added to object type `Mutation`
- Argument `input: UpdateIssueFieldInput!` added to field `Mutation.updateIssueField`
- Field `updateIssueFieldValue` was added to object type `Mutation`
- Argument `input: UpdateIssueFieldValueInput!` added to field `Mutation.updateIssueFieldValue`
- Field `issueFields` was added to object type `Organization`
- Argument `after: String` added to field `Organization.issueFields`
- Argument `before: String` added to field `Organization.issueFields`
- Argument `first: Int` added to field `Organization.issueFields`
- Argument `last: Int` added to field `Organization.issueFields`
- Argument `orderBy: IssueFieldOrder` (with default value) added to field `Organization.issueFields`
- Member 'ProjectV2ItemIssueFieldValue`was added to Union type`ProjectV2ItemFieldValue'
- Member `IssueCommentPinnedEvent` was added to Union type `PullRequestTimelineItems`
- Member `IssueCommentUnpinnedEvent` was added to Union type `PullRequestTimelineItems`

## 2026-03-10

**The GraphQL schema includes these changes:**

- Field `viewerCopilotAgentTaskUpdatesChannel` was added to interface `Agentic`
- Field `viewerCopilotAgentTaskUpdatesChannel` was added to object type `User`

## 2026-03-03

**The GraphQL schema includes these changes:**

- Field `fullDatabaseId` was added to object type `CheckAnnotation`

## 2026-02-25

**The GraphQL schema includes these changes:**

- Input field `requireExplicitValues` of type `Boolean` was added to input object type `CreateRepositoryCustomPropertyInput`
- Field `requireExplicitValues` was added to object type `RepositoryCustomProperty`
- Input field `requireExplicitValues` of type `Boolean` was added to input object type `UpdateRepositoryCustomPropertyInput`

## 2026-02-23

**The GraphQL schema includes these changes:**

- Enum value 'ISSUE_COMMENT_PINNED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'ISSUE_COMMENT_UNPINNED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'ISSUE_COMMENT_PINNED_EVENT`was added to enum`PullRequestTimelineItemsItemType'
- Enum value 'ISSUE_COMMENT_UNPINNED_EVENT`was added to enum`PullRequestTimelineItemsItemType'

## 2026-02-20

**The GraphQL schema includes these changes:**

- Type `PullRequestCreationPolicy` was added
- Enum value `ALL` was added to enum `PullRequestCreationPolicy`
- Enum value 'COLLABORATORS_ONLY`was added to enum`PullRequestCreationPolicy'
- Field `hasPullRequestsEnabled` was added to object type `Repository`
- Field `pullRequestCreationPolicy` was added to object type `Repository`
- Field `hasPullRequestsEnabled` was added to interface `RepositoryInfo`
- Field `pullRequestCreationPolicy` was added to interface `RepositoryInfo`
- Input field `hasPullRequestsEnabled` of type `Boolean` was added to input object type `UpdateRepositoryInput`
- Input field `pullRequestCreationPolicy` of type `PullRequestCreationPolicy` was added to input object type `UpdateRepositoryInput`

## 2026-02-13

**The GraphQL schema includes these changes:**


## 2026-02-07

**The GraphQL schema includes these changes:**

- Type `AgentAssignmentInput` was added
- Input field `baseRef` of type `String` was added to input object type `AgentAssignmentInput`
- Input field `customAgent` of type `String` was added to input object type `AgentAssignmentInput`
- Input field `customInstructions` of type `String` was added to input object type `AgentAssignmentInput`
- Input field `targetRepositoryId` of type `ID` was added to input object type `AgentAssignmentInput`
- Input field `agentAssignment` of type `AgentAssignmentInput` was added to input object type `AddAssigneesToAssignableInput`
- Input field `agentAssignment` of type `AgentAssignmentInput` was added to input object type `CreateIssueInput`
- Input field `agentAssignment` of type `AgentAssignmentInput` was added to input object type `ReplaceActorsForAssignableInput`
- Input field `agentAssignment` of type `AgentAssignmentInput` was added to input object type `UpdateIssueInput`

## 2026-02-05

**The GraphQL schema includes these changes:**

- Type `IpAllowListUserLevelEnforcementEnabledSettingValue` was added
- Enum value `DISABLED` was added to enum `IpAllowListUserLevelEnforcementEnabledSettingValue`
- Enum value `ENABLED` was added to enum `IpAllowListUserLevelEnforcementEnabledSettingValue`
- Type `UpdateIpAllowListUserLevelEnforcementEnabledSettingInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `UpdateIpAllowListUserLevelEnforcementEnabledSettingInput`
- Input field `ownerId` of type `ID!` was added to input object type `UpdateIpAllowListUserLevelEnforcementEnabledSettingInput`
- Input field `settingValue` of type `IpAllowListUserLevelEnforcementEnabledSettingValue!` was added to input object type `UpdateIpAllowListUserLevelEnforcementEnabledSettingInput`
- Type `UpdateIpAllowListUserLevelEnforcementEnabledSettingPayload` was added
- Field `clientMutationId` was added to object type `UpdateIpAllowListUserLevelEnforcementEnabledSettingPayload`
- Field `owner` was added to object type `UpdateIpAllowListUserLevelEnforcementEnabledSettingPayload`
- Field `ipAllowListUserLevelEnforcementEnabledSetting` was added to object type `EnterpriseOwnerInfo`
- Field `updateIpAllowListUserLevelEnforcementEnabledSetting` was added to object type `Mutation`
- Argument `input: UpdateIpAllowListUserLevelEnforcementEnabledSettingInput!` added to field `Mutation.updateIpAllowListUserLevelEnforcementEnabledSetting`

## 2026-01-28

**The GraphQL schema includes these changes:**

- Field `Issue.projectItems` changed type from 'ProjectV2ItemConnection!`to`ProjectV2ItemConnection'
- Field `PullRequest.projectItems` changed type from 'ProjectV2ItemConnection!`to`ProjectV2ItemConnection'

## 2026-01-23

**The GraphQL schema includes these changes:**

- Input field `actorLogins` of type '[String!]`was added to input object type`ReplaceActorsForAssignableInput'
- Input field `ReplaceActorsForAssignableInput.actorIds` changed type from '[ID!]!`to`[ID!]'

## 2026-01-22

**The GraphQL schema includes these changes:**

- Type `RequestReviewsByLoginInput` was added
- Input field `botLogins` of type '[String!]`was added to input object type`RequestReviewsByLoginInput'
- Input field `clientMutationId` of type `String` was added to input object type `RequestReviewsByLoginInput`
- Input field `pullRequestId` of type `ID!` was added to input object type `RequestReviewsByLoginInput`
- Input field `teamSlugs` of type '[String!]`was added to input object type`RequestReviewsByLoginInput'
- Input field `union` of type `Boolean` with default value `false` was added to input object type `RequestReviewsByLoginInput`
- Input field `userLogins` of type '[String!]`was added to input object type`RequestReviewsByLoginInput'
- Type `RequestReviewsByLoginPayload` was added
- Field `actor` was added to object type `RequestReviewsByLoginPayload`
- Field `clientMutationId` was added to object type `RequestReviewsByLoginPayload`
- Field `pullRequest` was added to object type `RequestReviewsByLoginPayload`
- Field `requestedReviewersEdge` was added to object type `RequestReviewsByLoginPayload`
- Field `requestReviewsByLogin` was added to object type `Mutation`
- Argument `input: RequestReviewsByLoginInput!` added to field `Mutation.requestReviewsByLogin`

## 2026-01-21

**The GraphQL schema includes these changes:**

- Argument `query: String` added to field `PullRequest.suggestedReviewerActors`

## 2026-01-14

**The GraphQL schema includes these changes:**

- Type `UpdateEnterpriseTeamDiscussionsSettingInput` was removed
- Type `UpdateEnterpriseTeamDiscussionsSettingPayload` was removed
- Field `teamDiscussionsSettingOrganizations` was removed from object type `EnterpriseOwnerInfo`
- Field `updateEnterpriseTeamDiscussionsSetting` was removed from object type `Mutation`

## 2026-01-08

**The GraphQL schema includes these changes:**

- Type `CreateTeamDiscussionInput` was removed
- Type `CreateTeamDiscussionPayload` was removed
- Type `DeleteTeamDiscussionInput` was removed
- Type `DeleteTeamDiscussionPayload` was removed
- Type `TeamDiscussion` was removed
- Type `TeamDiscussionConnection` was removed
- Type `TeamDiscussionEdge` was removed
- Type `TeamDiscussionOrder` was removed
- Type `TeamDiscussionOrderField` was removed
- Type `UpdateTeamDiscussionInput` was removed
- Type `UpdateTeamDiscussionPayload` was removed
- Field `createTeamDiscussion` was removed from object type `Mutation`
- Field `deleteTeamDiscussion` was removed from object type `Mutation`
- Field `updateTeamDiscussion` was removed from object type `Mutation`
- Field `discussion` was removed from object type `Team`
- Field `discussions` was removed from object type `Team`
- Field `discussionsResourcePath` was removed from object type `Team`
- Field `discussionsUrl` was removed from object type `Team`

## 2026-01-06

**The GraphQL schema includes these changes:**

- Type `CreateTeamDiscussionInput` was added
- Input field `body` of type `String` was added to input object type `CreateTeamDiscussionInput`
- Input field `clientMutationId` of type `String` was added to input object type `CreateTeamDiscussionInput`
- Input field `private` of type `Boolean` was added to input object type `CreateTeamDiscussionInput`
- Input field `teamId` of type `ID` was added to input object type `CreateTeamDiscussionInput`
- Input field `title` of type `String` was added to input object type `CreateTeamDiscussionInput`
- Type `CreateTeamDiscussionPayload` was added
- Field `clientMutationId` was added to object type `CreateTeamDiscussionPayload`
- Field `teamDiscussion` was added to object type `CreateTeamDiscussionPayload`
- Type `DeleteTeamDiscussionInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `DeleteTeamDiscussionInput`
- Input field `id` of type `ID!` was added to input object type `DeleteTeamDiscussionInput`
- Type `DeleteTeamDiscussionPayload` was added
- Field `clientMutationId` was added to object type `DeleteTeamDiscussionPayload`
- Type `TeamDiscussion` was added
- `TeamDiscussion` object implements `Comment` interface
- `TeamDiscussion` object implements `Deletable` interface
- `TeamDiscussion` object implements `Node` interface
- `TeamDiscussion` object implements `Reactable` interface
- `TeamDiscussion` object implements `Subscribable` interface
- `TeamDiscussion` object implements `UniformResourceLocatable` interface
- `TeamDiscussion` object implements `Updatable` interface
- `TeamDiscussion` object implements `UpdatableComment` interface
- Field `author` was added to object type `TeamDiscussion`
- Field `authorAssociation` was added to object type `TeamDiscussion`
- Field `body` was added to object type `TeamDiscussion`
- Field `bodyHTML` was added to object type `TeamDiscussion`
- Field `bodyText` was added to object type `TeamDiscussion`
- Field `bodyVersion` was added to object type `TeamDiscussion`
- Field `commentsResourcePath` was added to object type `TeamDiscussion`
- Field `commentsUrl` was added to object type `TeamDiscussion`
- Field `createdAt` was added to object type `TeamDiscussion`
- Field `createdViaEmail` was added to object type `TeamDiscussion`
- Field `databaseId` was added to object type `TeamDiscussion`
- Field `editor` was added to object type `TeamDiscussion`
- Field `id` was added to object type `TeamDiscussion`
- Field `includesCreatedEdit` was added to object type `TeamDiscussion`
- Field `isPinned` was added to object type `TeamDiscussion`
- Field `isPrivate` was added to object type `TeamDiscussion`
- Field `lastEditedAt` was added to object type `TeamDiscussion`
- Field `number` was added to object type `TeamDiscussion`
- Field `publishedAt` was added to object type `TeamDiscussion`
- Field `reactionGroups` was added to object type `TeamDiscussion`
- Field `reactions` was added to object type `TeamDiscussion`
- Argument `after: String` added to field `TeamDiscussion.reactions`
- Argument `before: String` added to field `TeamDiscussion.reactions`
- Argument `content: ReactionContent` added to field `TeamDiscussion.reactions`
- Argument `first: Int` added to field `TeamDiscussion.reactions`
- Argument `last: Int` added to field `TeamDiscussion.reactions`
- Argument `orderBy: ReactionOrder` added to field `TeamDiscussion.reactions`
- Field `resourcePath` was added to object type `TeamDiscussion`
- Field `team` was added to object type `TeamDiscussion`
- Field `title` was added to object type `TeamDiscussion`
- Field `updatedAt` was added to object type `TeamDiscussion`
- Field `url` was added to object type `TeamDiscussion`
- Field `userContentEdits` was added to object type `TeamDiscussion`
- Argument `after: String` added to field `TeamDiscussion.userContentEdits`
- Argument `before: String` added to field `TeamDiscussion.userContentEdits`
- Argument `first: Int` added to field `TeamDiscussion.userContentEdits`
- Argument `last: Int` added to field `TeamDiscussion.userContentEdits`
- Field `viewerCanDelete` was added to object type `TeamDiscussion`
- Field `viewerCanPin` was added to object type `TeamDiscussion`
- Field `viewerCanReact` was added to object type `TeamDiscussion`
- Field `viewerCanSubscribe` was added to object type `TeamDiscussion`
- Field `viewerCanUpdate` was added to object type `TeamDiscussion`
- Field `viewerCannotUpdateReasons` was added to object type `TeamDiscussion`
- Field `viewerDidAuthor` was added to object type `TeamDiscussion`
- Field `viewerSubscription` was added to object type `TeamDiscussion`
- Type `TeamDiscussionConnection` was added
- Field `edges` was added to object type `TeamDiscussionConnection`
- Field `nodes` was added to object type `TeamDiscussionConnection`
- Field `pageInfo` was added to object type `TeamDiscussionConnection`
- Field `totalCount` was added to object type `TeamDiscussionConnection`
- Type `TeamDiscussionEdge` was added
- Field `cursor` was added to object type `TeamDiscussionEdge`
- Field `node` was added to object type `TeamDiscussionEdge`
- Type `TeamDiscussionOrder` was added
- Input field `direction` of type `OrderDirection!` was added to input object type `TeamDiscussionOrder`
- Input field `field` of type `TeamDiscussionOrderField!` was added to input object type `TeamDiscussionOrder`
- Type `TeamDiscussionOrderField` was added
- Enum value 'CREATED_AT`was added to enum`TeamDiscussionOrderField'
- Type `UpdateTeamDiscussionInput` was added
- Input field `body` of type `String` was added to input object type `UpdateTeamDiscussionInput`
- Input field `bodyVersion` of type `String` was added to input object type `UpdateTeamDiscussionInput`
- Input field `clientMutationId` of type `String` was added to input object type `UpdateTeamDiscussionInput`
- Input field `id` of type `ID!` was added to input object type `UpdateTeamDiscussionInput`
- Input field `pinned` of type `Boolean` was added to input object type `UpdateTeamDiscussionInput`
- Input field `title` of type `String` was added to input object type `UpdateTeamDiscussionInput`
- Type `UpdateTeamDiscussionPayload` was added
- Field `clientMutationId` was added to object type `UpdateTeamDiscussionPayload`
- Field `teamDiscussion` was added to object type `UpdateTeamDiscussionPayload`
- Field `createTeamDiscussion` was added to object type `Mutation`
- Argument `input: CreateTeamDiscussionInput!` added to field `Mutation.createTeamDiscussion`
- Field `deleteTeamDiscussion` was added to object type `Mutation`
- Argument `input: DeleteTeamDiscussionInput!` added to field `Mutation.deleteTeamDiscussion`
- Field `updateTeamDiscussion` was added to object type `Mutation`
- Argument `input: UpdateTeamDiscussionInput!` added to field `Mutation.updateTeamDiscussion`
- Field `discussion` was added to object type `Team`
- Argument `number: Int!` added to field `Team.discussion`
- Field `discussions` was added to object type `Team`
- Argument `after: String` added to field `Team.discussions`
- Argument `before: String` added to field `Team.discussions`
- Argument `first: Int` added to field `Team.discussions`
- Argument `isPinned: Boolean` added to field `Team.discussions`
- Argument `last: Int` added to field `Team.discussions`
- Argument `orderBy: TeamDiscussionOrder` added to field `Team.discussions`
- Field `discussionsResourcePath` was added to object type `Team`
- Field `discussionsUrl` was added to object type `Team`

## 2026-01-05

**The GraphQL schema includes these changes:**

- Type `CreateTeamDiscussionInput` was removed
- Type `CreateTeamDiscussionPayload` was removed
- Type `DeleteTeamDiscussionInput` was removed
- Type `DeleteTeamDiscussionPayload` was removed
- Type `TeamDiscussion` was removed
- Type `TeamDiscussionConnection` was removed
- Type `TeamDiscussionEdge` was removed
- Type `TeamDiscussionOrder` was removed
- Type `TeamDiscussionOrderField` was removed
- Type `UpdateTeamDiscussionInput` was removed
- Type `UpdateTeamDiscussionPayload` was removed
- Field `createTeamDiscussion` was removed from object type `Mutation`
- Field `deleteTeamDiscussion` was removed from object type `Mutation`
- Field `updateTeamDiscussion` was removed from object type `Mutation`
- Field `discussion` was removed from object type `Team`
- Field `discussions` was removed from object type `Team`
- Field `discussionsResourcePath` was removed from object type `Team`
- Field `discussionsUrl` was removed from object type `Team`

## 2026-01-04

**The GraphQL schema includes these changes:**

- Type `CreateTeamDiscussionCommentInput` was removed
- Type `CreateTeamDiscussionCommentPayload` was removed
- Type `DeleteTeamDiscussionCommentInput` was removed
- Type `DeleteTeamDiscussionCommentPayload` was removed
- Type `TeamDiscussionComment` was removed
- Type `TeamDiscussionCommentConnection` was removed
- Type `TeamDiscussionCommentEdge` was removed
- Type `TeamDiscussionCommentOrder` was removed
- Type `TeamDiscussionCommentOrderField` was removed
- Type `UpdateTeamDiscussionCommentInput` was removed
- Type `UpdateTeamDiscussionCommentPayload` was removed
- Field `createTeamDiscussionComment` was removed from object type `Mutation`
- Field `deleteTeamDiscussionComment` was removed from object type `Mutation`
- Field `updateTeamDiscussionComment` was removed from object type `Mutation`
- Field `comments` (deprecated) was removed from object type `TeamDiscussion`

## 2025-12-13

**The GraphQL schema includes these changes:**


## 2025-12-10

**The GraphQL schema includes these changes:**

- Type `CreateRepositoryCustomPropertyInput` was added
- Input field `allowedValues` of type '[String!]`was added to input object type`CreateRepositoryCustomPropertyInput'
- Input field `clientMutationId` of type `String` was added to input object type `CreateRepositoryCustomPropertyInput`
- Input field `defaultValue` of type `String` was added to input object type `CreateRepositoryCustomPropertyInput`
- Input field `description` of type `String` was added to input object type `CreateRepositoryCustomPropertyInput`
- Input field `propertyName` of type `String!` was added to input object type `CreateRepositoryCustomPropertyInput`
- Input field `regex` of type `String` was added to input object type `CreateRepositoryCustomPropertyInput`
- Input field `required` of type `Boolean` was added to input object type `CreateRepositoryCustomPropertyInput`
- Input field `sourceId` of type `ID!` was added to input object type `CreateRepositoryCustomPropertyInput`
- Input field `valueType` of type `CustomPropertyValueType!` was added to input object type `CreateRepositoryCustomPropertyInput`
- Input field `valuesEditableBy` of type `RepositoryCustomPropertyValuesEditableBy` was added to input object type `CreateRepositoryCustomPropertyInput`
- Type `CreateRepositoryCustomPropertyPayload` was added
- Field `clientMutationId` was added to object type `CreateRepositoryCustomPropertyPayload`
- Field `repositoryCustomProperty` was added to object type `CreateRepositoryCustomPropertyPayload`
- Type `CustomPropertySource` was added
- Member `Enterprise` was added to Union type `CustomPropertySource`
- Member `Organization` was added to Union type `CustomPropertySource`
- Type `CustomPropertyValue` was added
- Type `CustomPropertyValueInput` was added
- Input field `propertyName` of type `String!` was added to input object type `CustomPropertyValueInput`
- Input field `value` of type `CustomPropertyValue` was added to input object type `CustomPropertyValueInput`
- Type `CustomPropertyValueType` was added
- Enum value 'MULTI_SELECT`was added to enum`CustomPropertyValueType'
- Enum value 'SINGLE_SELECT`was added to enum`CustomPropertyValueType'
- Enum value `STRING` was added to enum `CustomPropertyValueType`
- Enum value 'TRUE_FALSE`was added to enum`CustomPropertyValueType'
- Enum value `URL` was added to enum `CustomPropertyValueType`
- Type `DeleteRepositoryCustomPropertyInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `DeleteRepositoryCustomPropertyInput`
- Input field `id` of type `ID!` was added to input object type `DeleteRepositoryCustomPropertyInput`
- Type `DeleteRepositoryCustomPropertyPayload` was added
- Field `clientMutationId` was added to object type `DeleteRepositoryCustomPropertyPayload`
- Field `repositoryCustomProperty` was added to object type `DeleteRepositoryCustomPropertyPayload`
- Type `PromoteRepositoryCustomPropertyInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `PromoteRepositoryCustomPropertyInput`
- Input field `repositoryCustomPropertyId` of type `ID!` was added to input object type `PromoteRepositoryCustomPropertyInput`
- Type `PromoteRepositoryCustomPropertyPayload` was added
- Field `clientMutationId` was added to object type `PromoteRepositoryCustomPropertyPayload`
- Field `repositoryCustomProperty` was added to object type `PromoteRepositoryCustomPropertyPayload`
- Type `RepositoryCustomProperty` was added
- `RepositoryCustomProperty` object implements `Node` interface
- Field `allowedValues` was added to object type `RepositoryCustomProperty`
- Field `defaultValue` was added to object type `RepositoryCustomProperty`
- Field `description` was added to object type `RepositoryCustomProperty`
- Field `id` was added to object type `RepositoryCustomProperty`
- Field `propertyName` was added to object type `RepositoryCustomProperty`
- Field `regex` was added to object type `RepositoryCustomProperty`
- Field `required` was added to object type `RepositoryCustomProperty`
- Field `source` was added to object type `RepositoryCustomProperty`
- Field `valueType` was added to object type `RepositoryCustomProperty`
- Field `valuesEditableBy` was added to object type `RepositoryCustomProperty`
- Type `RepositoryCustomPropertyConnection` was added
- Field `edges` was added to object type `RepositoryCustomPropertyConnection`
- Field `nodes` was added to object type `RepositoryCustomPropertyConnection`
- Field `pageInfo` was added to object type `RepositoryCustomPropertyConnection`
- Field `totalCount` was added to object type `RepositoryCustomPropertyConnection`
- Type `RepositoryCustomPropertyEdge` was added
- Field `cursor` was added to object type `RepositoryCustomPropertyEdge`
- Field `node` was added to object type `RepositoryCustomPropertyEdge`
- Type `RepositoryCustomPropertyValue` was added
- Field `propertyName` was added to object type `RepositoryCustomPropertyValue`
- Field `value` was added to object type `RepositoryCustomPropertyValue`
- Type `RepositoryCustomPropertyValueConnection` was added
- Field `edges` was added to object type `RepositoryCustomPropertyValueConnection`
- Field `nodes` was added to object type `RepositoryCustomPropertyValueConnection`
- Field `pageInfo` was added to object type `RepositoryCustomPropertyValueConnection`
- Field `totalCount` was added to object type `RepositoryCustomPropertyValueConnection`
- Type `RepositoryCustomPropertyValueEdge` was added
- Field `cursor` was added to object type `RepositoryCustomPropertyValueEdge`
- Field `node` was added to object type `RepositoryCustomPropertyValueEdge`
- Type `RepositoryCustomPropertyValuesEditableBy` was added
- Enum value 'ORG_ACTORS`was added to enum`RepositoryCustomPropertyValuesEditableBy'
- Enum value 'ORG_AND_REPO_ACTORS`was added to enum`RepositoryCustomPropertyValuesEditableBy'
- Type `SetRepositoryCustomPropertyValuesInput` was added
- Input field `clientMutationId` of type `String` was added to input object type `SetRepositoryCustomPropertyValuesInput`
- Input field `properties` of type '[CustomPropertyValueInput!]!`was added to input object type`SetRepositoryCustomPropertyValuesInput'
- Input field `repositoryId` of type `ID!` was added to input object type `SetRepositoryCustomPropertyValuesInput`
- Type `SetRepositoryCustomPropertyValuesPayload` was added
- Field `clientMutationId` was added to object type `SetRepositoryCustomPropertyValuesPayload`
- Field `repository` was added to object type `SetRepositoryCustomPropertyValuesPayload`
- Type `UpdateRepositoryCustomPropertyInput` was added
- Input field `allowedValues` of type '[String!]`was added to input object type`UpdateRepositoryCustomPropertyInput'
- Input field `clientMutationId` of type `String` was added to input object type `UpdateRepositoryCustomPropertyInput`
- Input field `defaultValue` of type `String` was added to input object type `UpdateRepositoryCustomPropertyInput`
- Input field `description` of type `String` was added to input object type `UpdateRepositoryCustomPropertyInput`
- Input field `regex` of type `String` was added to input object type `UpdateRepositoryCustomPropertyInput`
- Input field `repositoryCustomPropertyId` of type `ID!` was added to input object type `UpdateRepositoryCustomPropertyInput`
- Input field `required` of type `Boolean` was added to input object type `UpdateRepositoryCustomPropertyInput`
- Input field `valuesEditableBy` of type `RepositoryCustomPropertyValuesEditableBy` was added to input object type `UpdateRepositoryCustomPropertyInput`
- Type `UpdateRepositoryCustomPropertyPayload` was added
- Field `clientMutationId` was added to object type `UpdateRepositoryCustomPropertyPayload`
- Field `repositoryCustomProperty` was added to object type `UpdateRepositoryCustomPropertyPayload`
- Field `repositoryCustomProperties` was added to object type `Enterprise`
- Argument `after: String` added to field `Enterprise.repositoryCustomProperties`
- Argument `before: String` added to field `Enterprise.repositoryCustomProperties`
- Argument `first: Int` added to field `Enterprise.repositoryCustomProperties`
- Argument `last: Int` added to field `Enterprise.repositoryCustomProperties`
- Field `repositoryCustomProperty` was added to object type `Enterprise`
- Argument `propertyName: String!` added to field `Enterprise.repositoryCustomProperty`
- Field `createRepositoryCustomProperty` was added to object type `Mutation`
- Argument `input: CreateRepositoryCustomPropertyInput!` added to field `Mutation.createRepositoryCustomProperty`
- Field `deleteRepositoryCustomProperty` was added to object type `Mutation`
- Argument `input: DeleteRepositoryCustomPropertyInput!` added to field `Mutation.deleteRepositoryCustomProperty`
- Field `promoteRepositoryCustomProperty` was added to object type `Mutation`
- Argument `input: PromoteRepositoryCustomPropertyInput!` added to field `Mutation.promoteRepositoryCustomProperty`
- Field `setRepositoryCustomPropertyValues` was added to object type `Mutation`
- Argument `input: SetRepositoryCustomPropertyValuesInput!` added to field `Mutation.setRepositoryCustomPropertyValues`
- Field `updateRepositoryCustomProperty` was added to object type `Mutation`
- Argument `input: UpdateRepositoryCustomPropertyInput!` added to field `Mutation.updateRepositoryCustomProperty`
- Field `repositoryCustomProperties` was added to object type `Organization`
- Argument `after: String` added to field `Organization.repositoryCustomProperties`
- Argument `before: String` added to field `Organization.repositoryCustomProperties`
- Argument `first: Int` added to field `Organization.repositoryCustomProperties`
- Argument `last: Int` added to field `Organization.repositoryCustomProperties`
- Field `repositoryCustomProperty` was added to object type `Organization`
- Argument `propertyName: String!` added to field `Organization.repositoryCustomProperty`
- Field `repositoryCustomPropertyValue` was added to object type `Repository`
- Argument `propertyName: String!` added to field `Repository.repositoryCustomPropertyValue`
- Field `repositoryCustomPropertyValues` was added to object type `Repository`
- Argument `after: String` added to field `Repository.repositoryCustomPropertyValues`
- Argument `before: String` added to field `Repository.repositoryCustomPropertyValues`
- Argument `first: Int` added to field `Repository.repositoryCustomPropertyValues`
- Argument `last: Int` added to field `Repository.repositoryCustomPropertyValues`

## 2025-12-05

**The GraphQL schema includes these changes:**

- Field `automaticCopilotCodeReviewEnabled` was removed from object type `PullRequestParameters`
- Input field `automaticCopilotCodeReviewEnabled` was removed from input object type `PullRequestParametersInput`

## 2025-11-30

**The GraphQL schema includes these changes:**

- Type `SuggestedReviewerActor` was added
- Type `SuggestedReviewerActorConnection` was added
- Type `SuggestedReviewerActorEdge` was added
- Enum value 'ISSUE_FIELD_ADDED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'ISSUE_FIELD_CHANGED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'ISSUE_FIELD_REMOVED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Field `suggestedReviewerActors` was added to object type `PullRequest`
- Enum value 'ISSUE_FIELD_ADDED_EVENT`was added to enum`PullRequestTimelineItemsItemType'
- Enum value 'ISSUE_FIELD_CHANGED_EVENT`was added to enum`PullRequestTimelineItemsItemType'
- Enum value 'ISSUE_FIELD_REMOVED_EVENT`was added to enum`PullRequestTimelineItemsItemType'

## 2025-11-14

**The GraphQL schema includes these changes:**

- Type `Agentic` was added
- `User` object implements `Agentic` interface
- Field `viewerCopilotAgentCreatesChannel` was added to object type `User`
- Field `viewerCopilotAgentLogUpdatesChannel` was added to object type `User`
- Field `viewerCopilotAgentUpdatesChannel` was added to object type `User`

## 2025-11-13

**The GraphQL schema includes these changes:**

- Type `RequiredReviewerConfiguration` was added
- Type `RequiredReviewerConfigurationInput` was added
- Field `requiredReviewers` was added to object type `PullRequestParameters`
- Input field `requiredReviewers` of type '[RequiredReviewerConfigurationInput!]`was added to input object type`PullRequestParametersInput'

## 2025-11-06

**The GraphQL schema includes these changes:**

- Input field 'projectV2Ids`of type`[ID!]`was added to input object type`CreateIssueInput'

## 2025-10-24

**The GraphQL schema includes these changes:**

- Type `OrganizationPropertyConditionTarget` was added
- Type `OrganizationPropertyConditionTargetInput` was added
- Type `OrganizationPropertyTargetDefinition` was added
- Type `OrganizationPropertyTargetDefinitionInput` was added
- Field `organizationProperty` was added to object type `RepositoryRuleConditions`
- Input field `organizationProperty` of type `OrganizationPropertyConditionTargetInput` was added to input object type `RepositoryRuleConditionsInput`
- Enum value `INCONCLUSIVE` was added to enum `RepositoryVulnerabilityAlertDependencyRelationship`

## 2025-10-22

**The GraphQL schema includes these changes:**

- Argument `query: String` (with default value) added to field 'ProjectV2.items'

## 2025-10-15

**The GraphQL schema includes these changes:**

- Type 'AddedToProjectV2Event' was added
- Type `ConvertedFromDraftEvent` was added
- Type 'ProjectV2Event' was added
- Type 'ProjectV2ItemStatusChangedEvent' was added
- Type 'RemovedFromProjectV2Event' was added
- Field `totalBlockedBy` was added to object type `IssueDependenciesSummary`
- Field `totalBlocking` was added to object type `IssueDependenciesSummary`
- Member 'AddedToProjectV2Event`was added to Union type`IssueTimelineItems'
- Member `ConvertedFromDraftEvent` was added to Union type `IssueTimelineItems`
- Member 'ProjectV2ItemStatusChangedEvent`was added to Union type`IssueTimelineItems'
- Member 'RemovedFromProjectV2Event`was added to Union type`IssueTimelineItems'
- Enum value 'ADDED_TO_PROJECT_V2_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'CONVERTED_FROM_DRAFT_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'PROJECT_V2_ITEM_STATUS_CHANGED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'REMOVED_FROM_PROJECT_V2_EVENT`was added to enum`IssueTimelineItemsItemType'
- Member 'AddedToProjectV2Event`was added to Union type`PullRequestTimelineItems'
- Member `ConvertedFromDraftEvent` was added to Union type `PullRequestTimelineItems`
- Member 'ProjectV2ItemStatusChangedEvent`was added to Union type`PullRequestTimelineItems'
- Member 'RemovedFromProjectV2Event`was added to Union type`PullRequestTimelineItems'
- Enum value 'ADDED_TO_PROJECT_V2_EVENT`was added to enum`PullRequestTimelineItemsItemType'
- Enum value 'CONVERTED_FROM_DRAFT_EVENT`was added to enum`PullRequestTimelineItemsItemType'
- Enum value 'PROJECT_V2_ITEM_STATUS_CHANGED_EVENT`was added to enum`PullRequestTimelineItemsItemType'
- Enum value 'REMOVED_FROM_PROJECT_V2_EVENT`was added to enum`PullRequestTimelineItemsItemType'

## 2025-09-16

**The GraphQL schema includes these changes:**

- Type `CopilotCodeReviewParameters` was added
- Type `CopilotCodeReviewParametersInput` was added
- Enum value 'COPILOT_CODE_REVIEW`was added to enum`RepositoryRuleType'
- Member `CopilotCodeReviewParameters` was added to Union type `RuleParameters`
- Input field `copilotCodeReview` of type `CopilotCodeReviewParametersInput` was added to input object type `RuleParametersInput`

## 2025-09-12

**The GraphQL schema includes these changes:**

- Enum value `EXEMPT` was added to enum `RepositoryRulesetBypassActorBypassMode`

## 2025-09-11

**The GraphQL schema includes these changes:**

- Field `viewerCanUnminimize` was added to object type `CommitComment`
- Field `viewerCanUnminimize` was added to object type `DiscussionComment`
- Field `viewerCanUnminimize` was added to object type `GistComment`
- Field `viewerCanUnminimize` was added to object type `IssueComment`
- Field `viewerCanUnminimize` was added to interface `Minimizable`
- Field `viewerCanUnminimize` was added to object type `PullRequestReview`
- Field `viewerCanUnminimize` was added to object type `PullRequestReviewComment`

## 2025-09-10

**The GraphQL schema includes these changes:**

- Enum value `SY` was added to enum `SponsorsCountryOrRegionCode`

## 2025-09-05

**The GraphQL schema includes these changes:**


## 2025-08-26

**The GraphQL schema includes these changes:**

- Field `viewerCanSetFields` was added to object type `Issue`
- Field `viewerCanSeeIssueFields` was added to object type `Repository`

## 2025-08-14

**The GraphQL schema includes these changes:**

- Type `BlockedByAddedEvent` was added
- Type `BlockedByRemovedEvent` was added
- Type `BlockingAddedEvent` was added
- Type `BlockingRemovedEvent` was added
- Member `BlockedByAddedEvent` was added to Union type `IssueTimelineItems`
- Member `BlockedByRemovedEvent` was added to Union type `IssueTimelineItems`
- Member `BlockingAddedEvent` was added to Union type `IssueTimelineItems`
- Member `BlockingRemovedEvent` was added to Union type `IssueTimelineItems`
- Member `BlockedByAddedEvent` was added to Union type `PullRequestTimelineItems`
- Member `BlockedByRemovedEvent` was added to Union type `PullRequestTimelineItems`
- Member `BlockingAddedEvent` was added to Union type `PullRequestTimelineItems`
- Member `BlockingRemovedEvent` was added to Union type `PullRequestTimelineItems`

## 2025-08-11

**The GraphQL schema includes these changes:**


## 2025-08-05

**The GraphQL schema includes these changes:**

- Field `securityContactEmail` was added to object type `Enterprise`
- Input field `securityContactEmail` of type `String` was added to input object type `UpdateEnterpriseProfileInput`

## 2025-07-31

**The GraphQL schema includes these changes:**

- Enum value 'BLOCKED_BY_REMOVED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'BLOCKING_ADDED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'BLOCKING_REMOVED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Enum value 'BLOCKED_BY_REMOVED_EVENT`was added to enum`PullRequestTimelineItemsItemType'
- Enum value 'BLOCKING_ADDED_EVENT`was added to enum`PullRequestTimelineItemsItemType'
- Enum value 'BLOCKING_REMOVED_EVENT`was added to enum`PullRequestTimelineItemsItemType'

## 2025-07-30

**The GraphQL schema includes these changes:**

- Type `AddBlockedByInput` was added
- Type `AddBlockedByPayload` was added
- Type `IssueDependenciesSummary` was added
- Type `IssueDependencyOrder` was added
- Type `IssueDependencyOrderField` was added
- Type `RemoveBlockedByInput` was added
- Type `RemoveBlockedByPayload` was added
- Field `blockedBy` was added to object type `Issue`
- Field `blocking` was added to object type `Issue`
- Field `issueDependenciesSummary` was added to object type `Issue`
- Enum value 'BLOCKED_BY_ADDED_EVENT`was added to enum`IssueTimelineItemsItemType'
- Field `addBlockedBy` was added to object type `Mutation`
- Field `removeBlockedBy` was added to object type `Mutation`
- Enum value 'BLOCKED_BY_ADDED_EVENT`was added to enum`PullRequestTimelineItemsItemType'

## 2025-07-15

**The GraphQL schema includes these changes:**

- Directive `deprecated` was removed from field `ClosedEvent.stateReason`
- Directive `deprecated` was removed from field `Issue.stateReason`

## 2025-07-04

**The GraphQL schema includes these changes:**

- Field `immutable` was added to object type `Release`

## 2025-06-25

**The GraphQL schema includes these changes:**

- Field `name` was added to object type `Mannequin`

## 2025-06-17

**The GraphQL schema includes these changes:**


## 2025-06-13

**The GraphQL schema includes these changes:**

- Type `BotOrUser` was removed
- Input field `botIds` of type '[ID!]`was added to input object type`RequestReviewsInput'
