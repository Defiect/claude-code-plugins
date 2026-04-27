# Users, Organizations & Teams

## Queries

### organization

**Returns:** `Organization`

Lookup a organization by login.

**Arguments:**

- `login` (`String!`): The organization's login.

### user

**Returns:** `User`

Lookup a user by login.

**Arguments:**

- `login` (`String!`): The user's login.

### viewer

**Returns:** `User!`

The currently authenticated user.

## Mutations

### acceptEnterpriseAdministratorInvitation

Accepts a pending invitation for a user to become an administrator of an enterprise.

**Input fields:**

- **input** (`AcceptEnterpriseAdministratorInvitationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitation** (`EnterpriseAdministratorInvitation`): The invitation that was accepted.
- **message** (`String`): A message confirming the result of accepting an administrator invitation.

### acceptEnterpriseMemberInvitation

Accepts a pending invitation for a user to become an unaffiliated member of an enterprise.

**Input fields:**

- **input** (`AcceptEnterpriseMemberInvitationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitation** (`EnterpriseMemberInvitation`): The invitation that was accepted.
- **message** (`String`): A message confirming the result of accepting an unaffiliated member invitation.

### addEnterpriseOrganizationMember

Adds enterprise members to an organization within the enterprise.

**Input fields:**

- **input** (`AddEnterpriseOrganizationMemberInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **users** (`[User!]`): The users who were added to the organization.

### cancelEnterpriseAdminInvitation

Cancels a pending invitation for an administrator to join an enterprise.

**Input fields:**

- **input** (`CancelEnterpriseAdminInvitationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitation** (`EnterpriseAdministratorInvitation`): The invitation that was canceled.
- **message** (`String`): A message confirming the result of canceling an administrator invitation.

### cancelEnterpriseMemberInvitation

Cancels a pending invitation for an unaffiliated member to join an enterprise.

**Input fields:**

- **input** (`CancelEnterpriseMemberInvitationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitation** (`EnterpriseMemberInvitation`): The invitation that was canceled.
- **message** (`String`): A message confirming the result of canceling an member invitation.

### changeUserStatus

Update your status on GitHub.

**Input fields:**

- **input** (`ChangeUserStatusInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **status** (`UserStatus`): Your updated status.

### createAttributionInvitation

Invites a user to claim reattributable data.

**Input fields:**

- **input** (`CreateAttributionInvitationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **owner** (`Organization`): The owner scoping the reattributable data.
- **source** (`Claimable`): The account owning the data to reattribute.
- **target** (`Claimable`): The account which may claim the data.

### createEnterpriseOrganization

Creates an organization as part of an enterprise account. A personal access
token used to create an organization is implicitly permitted to update the
organization it created, if the organization is part of an enterprise that has
SAML enabled or uses Enterprise Managed Users. If the organization is not part
of such an enterprise, and instead has SAML enabled for it individually, the
token will then require SAML authorization to continue working against that organization.

**Input fields:**

- **input** (`CreateEnterpriseOrganizationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise that owns the created organization.
- **organization** (`Organization`): The organization that was created.

### createUserList

Creates a new user list.

**Input fields:**

- **input** (`CreateUserListInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **list** (`UserList`): The list that was just created.
- **viewer** (`User`): The user who created the list.

### deleteUserList

Deletes a user list.

**Input fields:**

- **input** (`DeleteUserListInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **user** (`User`): The owner of the list that will be deleted.

### followOrganization

Follow an organization.

**Input fields:**

- **input** (`FollowOrganizationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organization** (`Organization`): The organization that was followed.

### followUser

Follow a user.

**Input fields:**

- **input** (`FollowUserInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **user** (`User`): The user that was followed.

### grantEnterpriseOrganizationsMigratorRole

Grant the migrator role to a user for all organizations under an enterprise account.

**Input fields:**

- **input** (`GrantEnterpriseOrganizationsMigratorRoleInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organizations** (`OrganizationConnection`): The organizations that had the migrator role applied to for the given user.

### linkProjectV2ToTeam

Links a project to a team.

**Input fields:**

- **input** (`LinkProjectV2ToTeamInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **team** (`Team`): The team the project is linked to.

### removeEnterpriseOrganization

Removes an organization from the enterprise.

**Input fields:**

- **input** (`RemoveEnterpriseOrganizationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The updated enterprise.
- **organization** (`Organization`): The organization that was removed from the enterprise.
- **viewer** (`User`): The viewer performing the mutation.

### revokeEnterpriseOrganizationsMigratorRole

Revoke the migrator role to a user for all organizations under an enterprise account.

**Input fields:**

- **input** (`RevokeEnterpriseOrganizationsMigratorRoleInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organizations** (`OrganizationConnection`): The organizations that had the migrator role revoked for the given user.

### setOrganizationInteractionLimit

Set an organization level interaction limit for an organization's public repositories.

**Input fields:**

- **input** (`SetOrganizationInteractionLimitInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organization** (`Organization`): The organization that the interaction limit was set for.

### setUserInteractionLimit

Set a user level interaction limit for an user's public repositories.

**Input fields:**

- **input** (`SetUserInteractionLimitInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **user** (`User`): The user that the interaction limit was set for.

### startOrganizationMigration

Starts a GitHub Enterprise Importer organization migration.

**Input fields:**

- **input** (`StartOrganizationMigrationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **orgMigration** (`OrganizationMigration`): The new organization migration.

### transferEnterpriseOrganization

Transfer an organization from one enterprise to another enterprise.

**Input fields:**

- **input** (`TransferEnterpriseOrganizationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organization** (`Organization`): The organization for which a transfer was initiated.

### unfollowOrganization

Unfollow an organization.

**Input fields:**

- **input** (`UnfollowOrganizationInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organization** (`Organization`): The organization that was unfollowed.

### unfollowUser

Unfollow a user.

**Input fields:**

- **input** (`UnfollowUserInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **user** (`User`): The user that was unfollowed.

### unlinkProjectV2FromTeam

Unlinks a project to a team.

**Input fields:**

- **input** (`UnlinkProjectV2FromTeamInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **team** (`Team`): The team the project is unlinked from.

### updateEnterpriseOrganizationProjectsSetting

Sets whether organization projects are enabled for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseOrganizationProjectsSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated organization projects setting.
- **message** (`String`): A message confirming the result of updating the organization projects setting.

### updateEnterpriseOwnerOrganizationRole

Updates the role of an enterprise owner with an organization.

**Input fields:**

- **input** (`UpdateEnterpriseOwnerOrganizationRoleInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **message** (`String`): A message confirming the result of changing the owner's organization role.

### updateIpAllowListUserLevelEnforcementEnabledSetting

Sets whether IP allow list user-level enforcement is enabled on an enterprise.

**Input fields:**

- **input** (`UpdateIpAllowListUserLevelEnforcementEnabledSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **owner** (`IpAllowListOwner`): The IP allow list owner on which the setting was updated.

### updateUserList

Updates an existing user list.

**Input fields:**

- **input** (`UpdateUserListInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **list** (`UserList`): The list that was just updated.

### updateUserListsForItem

Updates which of the viewer's lists an item belongs to.

**Input fields:**

- **input** (`UpdateUserListsForItemInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **item** (`UserListItems`): The item that was added.
- **lists** (`[UserList!]`): The lists to which this item belongs.
- **user** (`User`): The user who owns the lists.

## Types

### Bot

A special type of user which takes actions on behalf of GitHub Apps.

**Implements:** Actor, Node, UniformResourceLocatable

**Fields:**

- **avatarUrl** (`URI!`): A URL pointing to the GitHub App's public avatar.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the Bot object.
- **login** (`String!`): The username of the actor.
- **resourcePath** (`URI!`): The HTTP path for this bot.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this bot.

### EnterpriseServerUserAccount

A user account on an Enterprise Server installation.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **emails** (`EnterpriseServerUserAccountEmailConnection!`): User emails belonging to this user account.
- **enterpriseServerInstallation** (`EnterpriseServerInstallation!`): The Enterprise Server installation on which this user account exists.
- **id** (`ID!`): The Node ID of the EnterpriseServerUserAccount object.
- **isSiteAdmin** (`Boolean!`): Whether the user account is a site administrator on the Enterprise Server installation.
- **login** (`String!`): The login of the user account on the Enterprise Server installation.
- **profileName** (`String`): The profile name of the user account on the Enterprise Server installation.
- **remoteCreatedAt** (`DateTime!`): The date and time when the user account was created on the Enterprise Server installation.
- **remoteUserId** (`Int!`): The ID of the user account on the Enterprise Server installation.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### EnterpriseServerUserAccountEmail

An email belonging to a user account on an Enterprise Server installation.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **email** (`String!`): The email address.
- **id** (`ID!`): The Node ID of the EnterpriseServerUserAccountEmail object.
- **isPrimary** (`Boolean!`): Indicates whether this is the primary email of the associated user account.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **userAccount** (`EnterpriseServerUserAccount!`): The user account to which the email belongs.

### EnterpriseServerUserAccountsUpload

A user accounts upload from an Enterprise Server installation.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **enterprise** (`Enterprise!`): The enterprise to which this upload belongs.
- **enterpriseServerInstallation** (`EnterpriseServerInstallation!`): The Enterprise Server installation for which this upload was generated.
- **id** (`ID!`): The Node ID of the EnterpriseServerUserAccountsUpload object.
- **name** (`String!`): The name of the file uploaded.
- **syncState** (`EnterpriseServerUserAccountsUploadSyncState!`): The synchronization state of the upload.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### EnterpriseUserAccount

An account for a user who is an admin of an enterprise or a member of an enterprise through one or more organizations.

**Implements:** Actor, Node

**Fields:**

- **avatarUrl** (`URI!`): A URL pointing to the enterprise user account's public avatar.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **enterprise** (`Enterprise!`): The enterprise in which this user account exists.
- **enterpriseInstallations** (`EnterpriseServerInstallationMembershipConnection!`): A list of Enterprise Server installations this user is a member of.
- **id** (`ID!`): The Node ID of the EnterpriseUserAccount object.
- **login** (`String!`): An identifier for the enterprise user account, a login or email address.
- **name** (`String`): The name of the enterprise user account.
- **organizations** (`EnterpriseOrganizationMembershipConnection!`): A list of enterprise organizations this user is a member of.
- **resourcePath** (`URI!`): The HTTP path for this user.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this user.
- **user** (`User`): The user within the enterprise.

### ExternalIdentity

An external identity provisioned by SAML SSO or SCIM. If SAML is configured on
the organization, the external identity is visible to (1) organization owners,
(2) organization owners' personal access tokens (classic) with read:org or
admin:org scope, (3) GitHub App with an installation token with read or write
access to members. If SAML is configured on the enterprise, the external
identity is visible to (1) enterprise owners, (2) enterprise owners' personal
access tokens (classic) with read:enterprise or admin:enterprise scope.

**Implements:** Node

**Fields:**

- **guid** (`String!`): The GUID for this identity.
- **id** (`ID!`): The Node ID of the ExternalIdentity object.
- **organizationInvitation** (`OrganizationInvitation`): Organization invitation for this SCIM-provisioned external identity.
- **samlIdentity** (`ExternalIdentitySamlAttributes`): SAML Identity attributes.
- **scimIdentity** (`ExternalIdentityScimAttributes`): SCIM Identity attributes.
- **user** (`User`): User linked to this external identity. Will be NULL if this identity has not been claimed by an organization member.

### ExternalIdentityAttribute

An attribute for the External Identity attributes collection.

**Fields:**

- **metadata** (`String`): The attribute metadata as JSON.
- **name** (`String!`): The attribute name.
- **value** (`String!`): The attribute value.

### ExternalIdentitySamlAttributes

SAML attributes for the External Identity.

**Fields:**

- **attributes** (`[ExternalIdentityAttribute!]!`): SAML Identity attributes.
- **emails** (`[UserEmailMetadata!]`): The emails associated with the SAML identity.
- **familyName** (`String`): Family name of the SAML identity.
- **givenName** (`String`): Given name of the SAML identity.
- **groups** (`[String!]`): The groups linked to this identity in IDP.
- **nameId** (`String`): The NameID of the SAML identity.
- **username** (`String`): The userName of the SAML identity.

### ExternalIdentityScimAttributes

SCIM attributes for the External Identity.

**Fields:**

- **emails** (`[UserEmailMetadata!]`): The emails associated with the SCIM identity.
- **familyName** (`String`): Family name of the SCIM identity.
- **givenName** (`String`): Given name of the SCIM identity.
- **groups** (`[String!]`): The groups linked to this identity in IDP.
- **username** (`String`): The userName of the SCIM identity.

### GenericHovercardContext

A generic hovercard context with a message and icon.

**Implements:** HovercardContext

**Fields:**

- **message** (`String!`): A string describing this context.
- **octicon** (`String!`): An octicon to accompany this context.

### Gist

A Gist.

**Implements:** Node, Starrable, UniformResourceLocatable

**Fields:**

- **comments** (`GistCommentConnection!`): A list of comments associated with the gist.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **description** (`String`): The gist description.
- **files** (`[GistFile]`): The files in this gist.
- **forks** (`GistConnection!`): A list of forks associated with the gist.
- **id** (`ID!`): The Node ID of the Gist object.
- **isFork** (`Boolean!`): Identifies if the gist is a fork.
- **isPublic** (`Boolean!`): Whether the gist is public or not.
- **name** (`String!`): The gist name.
- **owner** (`RepositoryOwner`): The gist owner.
- **pushedAt** (`DateTime`): Identifies when the gist was last pushed to.
- **resourcePath** (`URI!`): The HTML path to this resource.
- **stargazerCount** (`Int!`): Returns a count of how many stargazers there are on this object.
- **stargazers** (`StargazerConnection!`): A list of users who have starred this starrable.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this Gist.
- **viewerHasStarred** (`Boolean!`): Returns a boolean indicating whether the viewing user has starred this starrable.

### GistComment

Represents a comment on an Gist.

**Implements:** Comment, Deletable, Minimizable, Node, Updatable, UpdatableComment

**Fields:**

- **author** (`Actor`): The actor who authored the comment.
- **authorAssociation** (`CommentAuthorAssociation!`): Author's association with the gist.
- **body** (`String!`): Identifies the comment body.
- **bodyHTML** (`HTML!`): The body rendered to HTML.
- **bodyText** (`String!`): The body rendered to text.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **createdViaEmail** (`Boolean!`): Check if this comment was created via an email reply.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **editor** (`Actor`): The actor who edited the comment.
- **gist** (`Gist!`): The associated gist.
- **id** (`ID!`): The Node ID of the GistComment object.
- **includesCreatedEdit** (`Boolean!`): Check if this comment was edited and includes an edit with the creation data.
- **isMinimized** (`Boolean!`): Returns whether or not a comment has been minimized.
- **lastEditedAt** (`DateTime`): The moment the editor made the last edit.
- **minimizedReason** (`String`): Returns why the comment was minimized. One of `abuse`, `off-topic`,
`outdated`, `resolved`, `duplicate`, `spam`, and `low-quality`. Note that the
case and formatting of these values differs from the inputs to the
`MinimizeComment` mutation.
- **publishedAt** (`DateTime`): Identifies when the comment was published at.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **userContentEdits** (`UserContentEditConnection`): A list of edits to this content.
- **viewerCanDelete** (`Boolean!`): Check if the current viewer can delete this object.
- **viewerCanMinimize** (`Boolean!`): Check if the current viewer can minimize this object.
- **viewerCanUnminimize** (`Boolean!`): Check if the current viewer can unminimize this object.
- **viewerCanUpdate** (`Boolean!`): Check if the current viewer can update this object.
- **viewerCannotUpdateReasons** (`[CommentCannotUpdateReason!]!`): Reasons why the current viewer can not update this comment.
- **viewerDidAuthor** (`Boolean!`): Did the viewer author this comment.

### GistFile

A file in a gist.

**Fields:**

- **encodedName** (`String`): The file name encoded to remove characters that are invalid in URL paths.
- **encoding** (`String`): The gist file encoding.
- **extension** (`String`): The file extension from the file name.
- **isImage** (`Boolean!`): Indicates if this file is an image.
- **isTruncated** (`Boolean!`): Whether the file's contents were truncated.
- **language** (`Language`): The programming language this file is written in.
- **name** (`String`): The gist file name.
- **size** (`Int`): The gist file size in bytes.
- **text** (`String`): UTF8 text data or null if the file is binary.

### Hovercard

Detail needed to display a hovercard for a user.

**Fields:**

- **contexts** (`[HovercardContext!]!`): Each of the contexts for this hovercard.

### IpAllowListEntry

An IP address or range of addresses that is allowed to access an owner's resources.

**Implements:** Node

**Fields:**

- **allowListValue** (`String!`): A single IP address or range of IP addresses in CIDR notation.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the IpAllowListEntry object.
- **isActive** (`Boolean!`): Whether the entry is currently active.
- **name** (`String`): The name of the IP allow list entry.
- **owner** (`IpAllowListOwner!`): The owner of the IP allow list entry.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### Mannequin

A placeholder user for attribution of imported data on GitHub.

**Implements:** Actor, Node, UniformResourceLocatable

**Fields:**

- **avatarUrl** (`URI!`): A URL pointing to the GitHub App's public avatar.
- **claimant** (`User`): The user that has claimed the data attributed to this mannequin.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **email** (`String`): The mannequin's email on the source instance.
- **id** (`ID!`): The Node ID of the Mannequin object.
- **login** (`String!`): The username of the actor.
- **name** (`String`): The display name of the imported mannequin.
- **resourcePath** (`URI!`): The HTML path to this resource.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The URL to this resource.

### MemberFeatureRequestNotification

Represents a member feature request notification.

**Implements:** Node

**Fields:**

- **body** (`String!`): Represents member feature request body containing entity name and the number of feature requests.
- **id** (`ID!`): The Node ID of the MemberFeatureRequestNotification object.
- **title** (`String!`): Represents member feature request notification title.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### OIDCProvider

An OIDC identity provider configured to provision identities for an enterprise.
Visible to enterprise owners or enterprise owners' personal access tokens
(classic) with read:enterprise or admin:enterprise scope.

**Implements:** Node

**Fields:**

- **enterprise** (`Enterprise`): The enterprise this identity provider belongs to.
- **externalIdentities** (`ExternalIdentityConnection!`): ExternalIdentities provisioned by this identity provider.
- **id** (`ID!`): The Node ID of the OIDCProvider object.
- **providerType** (`OIDCProviderType!`): The OIDC identity provider type.
- **tenantId** (`String!`): The id of the tenant this provider is attached to.

### Organization

An account on GitHub, with one or more owners, that has repositories, members and teams.

**Implements:** Actor, MemberStatusable, Node, PackageOwner, ProfileOwner, ProjectOwner, ProjectV2Owner, ProjectV2Recent, RepositoryDiscussionAuthor, RepositoryDiscussionCommentAuthor, RepositoryOwner, Sponsorable, UniformResourceLocatable

**Fields:**

- **announcementBanner** (`AnnouncementBanner`): The announcement banner set on this organization, if any. Only visible to members of the organization's enterprise.
- **anyPinnableItems** (`Boolean!`): Determine if this repository owner has any items that can be pinned to their profile.
- **archivedAt** (`DateTime`): Identifies the date and time when the organization was archived.
- **auditLog** (`OrganizationAuditEntryConnection!`): Audit log entries of the organization.
- **avatarUrl** (`URI!`): A URL pointing to the organization's public avatar.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **description** (`String`): The organization's public profile description.
- **descriptionHTML** (`String`): The organization's public profile description rendered to HTML.
- **domains** (`VerifiableDomainConnection`): A list of domains owned by the organization.
- **email** (`String`): The organization's public email.
- **enterpriseOwners** (`OrganizationEnterpriseOwnerConnection!`): A list of owners of the organization's enterprise account.
- **estimatedNextSponsorsPayoutInCents** (`Int!`): The estimated next GitHub Sponsors payout for this user/organization in cents (USD).
- **hasSponsorsListing** (`Boolean!`): True if this user/organization has a GitHub Sponsors listing.
- **id** (`ID!`): The Node ID of the Organization object.
- **interactionAbility** (`RepositoryInteractionAbility`): The interaction ability settings for this organization.
- **ipAllowListEnabledSetting** (`IpAllowListEnabledSettingValue!`): The setting value for whether the organization has an IP allow list enabled.
- **ipAllowListEntries** (`IpAllowListEntryConnection!`): The IP addresses that are allowed to access resources owned by the organization.
- **ipAllowListForInstalledAppsEnabledSetting** (`IpAllowListForInstalledAppsEnabledSettingValue!`): The setting value for whether the organization has IP allow list configuration for installed GitHub Apps enabled.
- **isSponsoredBy** (`Boolean!`): Whether the given account is sponsoring this user/organization.
- **isSponsoringViewer** (`Boolean!`): True if the viewer is sponsored by this user/organization.
- **isVerified** (`Boolean!`): Whether the organization has verified its profile email and website.
- **issueFields** (`IssueFieldsConnection`): A list of the organization's issue fields.
- **issueTypes** (`IssueTypeConnection`): A list of the organization's issue types.
- **itemShowcase** (`ProfileItemShowcase!`): Showcases a selection of repositories and gists that the profile owner has
either curated or that have been selected automatically based on popularity.
- **lifetimeReceivedSponsorshipValues** (`SponsorAndLifetimeValueConnection!`): Calculate how much each sponsor has ever paid total to this maintainer via
GitHub Sponsors. Does not include sponsorships paid via Patreon.
- **location** (`String`): The organization's public profile location.
- **login** (`String!`): The organization's login name.
- **mannequins** (`MannequinConnection!`): A list of all mannequins for this organization.
- **memberStatuses** (`UserStatusConnection!`): Get the status messages members of this entity have set that are either public or visible only to the organization.
- **membersCanForkPrivateRepositories** (`Boolean!`): Members can fork private repositories in this organization.
- **membersWithRole** (`OrganizationMemberConnection!`): A list of users who are members of this organization.
- **monthlyEstimatedSponsorsIncomeInCents** (`Int!`): The estimated monthly GitHub Sponsors income for this user/organization in cents (USD).
- **name** (`String`): The organization's public profile name.
- **newTeamResourcePath** (`URI!`): The HTTP path creating a new team.
- **newTeamUrl** (`URI!`): The HTTP URL creating a new team.
- **notificationDeliveryRestrictionEnabledSetting** (`NotificationRestrictionSettingValue!`): Indicates if email notification delivery for this organization is restricted to verified or approved domains.
- **organizationBillingEmail** (`String`): The billing email for the organization.
- **packages** (`PackageConnection!`): A list of packages under the owner.
- **pendingMembers** (`UserConnection!`): A list of users who have been invited to join this organization.
- **pinnableItems** (`PinnableItemConnection!`): A list of repositories and gists this profile owner can pin to their profile.
- **pinnedItems** (`PinnableItemConnection!`): A list of repositories and gists this profile owner has pinned to their profile.
- **pinnedItemsRemaining** (`Int!`): Returns how many more items this profile owner can pin to their profile.
- **project** (`Project`): Find project by number.
- **projectV2** (`ProjectV2`): Find a project by number.
- **projects** (`ProjectConnection!`): A list of projects under the owner.
- **projectsResourcePath** (`URI!`): The HTTP path listing organization's projects.
- **projectsUrl** (`URI!`): The HTTP URL listing organization's projects.
- **projectsV2** (`ProjectV2Connection!`): A list of projects under the owner.
- **recentProjects** (`ProjectV2Connection!`): Recent projects that this user has modified in the context of the owner.
- **repositories** (`RepositoryConnection!`): A list of repositories that the user owns.
- **repository** (`Repository`): Find Repository.
- **repositoryCustomProperties** (`RepositoryCustomPropertyConnection`): A list of custom properties for this organization.
- **repositoryCustomProperty** (`RepositoryCustomProperty`): Returns a single custom property from the current organization by name.
- **repositoryDiscussionComments** (`DiscussionCommentConnection!`): Discussion comments this user has authored.
- **repositoryDiscussions** (`DiscussionConnection!`): Discussions this user has started.
- **repositoryMigrations** (`RepositoryMigrationConnection!`): A list of all repository migrations for this organization.
- **requiresTwoFactorAuthentication** (`Boolean`): When true the organization requires all members, billing managers, and outside
collaborators to enable two-factor authentication.
- **resourcePath** (`URI!`): The HTTP path for this organization.
- **ruleset** (`RepositoryRuleset`): Returns a single ruleset from the current organization by ID.
- **rulesets** (`RepositoryRulesetConnection`): A list of rulesets for this organization.
- **samlIdentityProvider** (`OrganizationIdentityProvider`): The Organization's SAML identity provider. Visible to (1) organization owners,
(2) organization owners' personal access tokens (classic) with read:org or
admin:org scope, (3) GitHub App with an installation token with read or write
access to members.
- **sponsoring** (`SponsorConnection!`): List of users and organizations this entity is sponsoring.
- **sponsors** (`SponsorConnection!`): List of sponsors for this user or organization.
- **sponsorsActivities** (`SponsorsActivityConnection!`): Events involving this sponsorable, such as new sponsorships.
- **sponsorsListing** (`SponsorsListing`): The GitHub Sponsors listing for this user or organization.
- **sponsorshipForViewerAsSponsor** (`Sponsorship`): The sponsorship from the viewer to this user/organization; that is, the sponsorship where you're the sponsor.
- **sponsorshipForViewerAsSponsorable** (`Sponsorship`): The sponsorship from this user/organization to the viewer; that is, the sponsorship you're receiving.
- **sponsorshipNewsletters** (`SponsorshipNewsletterConnection!`): List of sponsorship updates sent from this sponsorable to sponsors.
- **sponsorshipsAsMaintainer** (`SponsorshipConnection!`): The sponsorships where this user or organization is the maintainer receiving the funds.
- **sponsorshipsAsSponsor** (`SponsorshipConnection!`): The sponsorships where this user or organization is the funder.
- **team** (`Team`): Find an organization's team by its slug.
- **teams** (`TeamConnection!`): A list of teams in this organization.
- **teamsResourcePath** (`URI!`): The HTTP path listing organization's teams.
- **teamsUrl** (`URI!`): The HTTP URL listing organization's teams.
- **totalSponsorshipAmountAsSponsorInCents** (`Int`): The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has
spent on GitHub to fund sponsorships. Only returns a value when viewed by the
user themselves or by a user who can manage sponsorships for the requested organization.
- **twitterUsername** (`String`): The organization's Twitter username.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this organization.
- **viewerCanAdminister** (`Boolean!`): Organization is adminable by the viewer.
- **viewerCanChangePinnedItems** (`Boolean!`): Can the viewer pin repositories and gists to the profile?.
- **viewerCanCreateProjects** (`Boolean!`): Can the current viewer create new projects on this owner.
- **viewerCanCreateRepositories** (`Boolean!`): Viewer can create repositories on this organization.
- **viewerCanCreateTeams** (`Boolean!`): Viewer can create teams on this organization.
- **viewerCanSponsor** (`Boolean!`): Whether or not the viewer is able to sponsor this user/organization.
- **viewerIsAMember** (`Boolean!`): Viewer is an active member of this organization.
- **viewerIsFollowing** (`Boolean!`): Whether or not this Organization is followed by the viewer.
- **viewerIsSponsoring** (`Boolean!`): True if the viewer is sponsoring this user/organization.
- **webCommitSignoffRequired** (`Boolean!`): Whether contributors are required to sign off on web-based commits for repositories in this organization.
- **websiteUrl** (`URI`): The organization's public profile URL.

### OrganizationIdentityProvider

An Identity Provider configured to provision SAML and SCIM identities for
Organizations. Visible to (1) organization owners, (2) organization owners'
personal access tokens (classic) with read:org or admin:org scope, (3) GitHub
App with an installation token with read or write access to members.

**Implements:** Node

**Fields:**

- **digestMethod** (`URI`): The digest algorithm used to sign SAML requests for the Identity Provider.
- **externalIdentities** (`ExternalIdentityConnection!`): External Identities provisioned by this Identity Provider.
- **id** (`ID!`): The Node ID of the OrganizationIdentityProvider object.
- **idpCertificate** (`X509Certificate`): The x509 certificate used by the Identity Provider to sign assertions and responses.
- **issuer** (`String`): The Issuer Entity ID for the SAML Identity Provider.
- **organization** (`Organization`): Organization this Identity Provider belongs to.
- **signatureMethod** (`URI`): The signature algorithm used to sign SAML requests for the Identity Provider.
- **ssoUrl** (`URI`): The URL endpoint for the Identity Provider's SAML SSO.

### OrganizationInvitation

An Invitation for a user to an organization.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **email** (`String`): The email address of the user invited to the organization.
- **id** (`ID!`): The Node ID of the OrganizationInvitation object.
- **invitationSource** (`OrganizationInvitationSource!`): The source of the invitation.
- **invitationType** (`OrganizationInvitationType!`): The type of invitation that was sent (e.g. email, user).
- **invitee** (`User`): The user who was invited to the organization.
- **inviter** (`User!`): The user who created the invitation.
- **inviterActor** (`User`): The user who created the invitation.
- **organization** (`Organization!`): The organization the invite is for.
- **role** (`OrganizationInvitationRole!`): The user's pending role in the organization (e.g. member, owner).

### OrganizationMigration

A GitHub Enterprise Importer (GEI) organization migration.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`String`): Identifies the primary key from the database.
- **failureReason** (`String`): The reason the organization migration failed.
- **id** (`ID!`): The Node ID of the OrganizationMigration object.
- **remainingRepositoriesCount** (`Int`): The remaining amount of repos to be migrated.
- **sourceOrgName** (`String!`): The name of the source organization to be migrated.
- **sourceOrgUrl** (`URI!`): The URL of the source organization to migrate.
- **state** (`OrganizationMigrationState!`): The migration state.
- **targetOrgName** (`String!`): The name of the target organization.
- **totalRepositoriesCount** (`Int`): The total amount of repositories to be migrated.

### OrganizationPropertyConditionTarget

Parameters to be used for the organization_property condition.

**Fields:**

- **exclude** (`[OrganizationPropertyTargetDefinition!]!`): Array of organization properties that must not match.
- **include** (`[OrganizationPropertyTargetDefinition!]!`): Array of organization properties that must match.

### OrganizationPropertyTargetDefinition

A property that must match.

**Fields:**

- **name** (`String!`): The name of the property.
- **propertyValues** (`[String!]!`): The values to match for.

### OrganizationTeamsHovercardContext

An organization teams hovercard context.

**Implements:** HovercardContext

**Fields:**

- **message** (`String!`): A string describing this context.
- **octicon** (`String!`): An octicon to accompany this context.
- **relevantTeams** (`TeamConnection!`): Teams in this organization the user is a member of that are relevant.
- **teamsResourcePath** (`URI!`): The path for the full team list for this user.
- **teamsUrl** (`URI!`): The URL for the full team list for this user.
- **totalTeamCount** (`Int!`): The total number of teams the user is on in the organization.

### OrganizationsHovercardContext

An organization list hovercard context.

**Implements:** HovercardContext

**Fields:**

- **message** (`String!`): A string describing this context.
- **octicon** (`String!`): An octicon to accompany this context.
- **relevantOrganizations** (`OrganizationConnection!`): Organizations this user is a member of that are relevant.
- **totalOrganizationCount** (`Int!`): The total number of organizations this user is in.

### ProfileItemShowcase

A curatable list of repositories relating to a repository owner, which defaults
to showing the most popular repositories they own.

**Fields:**

- **hasPinnedItems** (`Boolean!`): Whether or not the owner has pinned any repositories or gists.
- **items** (`PinnableItemConnection!`): The repositories and gists in the showcase. If the profile owner has any
pinned items, those will be returned. Otherwise, the profile owner's popular
repositories will be returned.

### ProjectV2ItemFieldUserValue

The value of a user field in a Project item.

**Fields:**

- **field** (`ProjectV2FieldConfiguration!`): The field that contains this value.
- **users** (`UserConnection`): The users for this field.

### PublicKey

A user's public key.

**Implements:** Node

**Fields:**

- **accessedAt** (`DateTime`): The last time this authorization was used to perform an action. Values will be null for keys not owned by the user.
- **createdAt** (`DateTime`): Identifies the date and time when the key was created. Keys created before
March 5th, 2014 have inaccurate values. Values will be null for keys not owned by the user.
- **fingerprint** (`String!`): The fingerprint for this PublicKey.
- **id** (`ID!`): The Node ID of the PublicKey object.
- **isReadOnly** (`Boolean`): Whether this PublicKey is read-only or not. Values will be null for keys not owned by the user.
- **key** (`String!`): The public key string.
- **updatedAt** (`DateTime`): Identifies the date and time when the key was updated. Keys created before
March 5th, 2014 may have inaccurate values. Values will be null for keys not
owned by the user.

### ReviewStatusHovercardContext

A hovercard context with a message describing the current code review state of the pull
request.

**Implements:** HovercardContext

**Fields:**

- **message** (`String!`): A string describing this context.
- **octicon** (`String!`): An octicon to accompany this context.
- **reviewDecision** (`PullRequestReviewDecision`): The current status of the pull request with respect to code review.

### SavedReply

A Saved Reply is text a user can use to reply quickly.

**Implements:** Node

**Fields:**

- **body** (`String!`): The body of the saved reply.
- **bodyHTML** (`HTML!`): The saved reply body rendered to HTML.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **id** (`ID!`): The Node ID of the SavedReply object.
- **title** (`String!`): The title of the saved reply.
- **user** (`Actor`): The user that saved this reply.

### SocialAccount

Social media profile associated with a user.

**Fields:**

- **displayName** (`String!`): Name of the social media account as it appears on the profile.
- **provider** (`SocialAccountProvider!`): Software or company that hosts the social media account.
- **url** (`URI!`): URL of the social media account.

### Team

A team of users in an organization.

**Implements:** MemberStatusable, Node, Subscribable, TeamReviewRequestable

**Fields:**

- **ancestors** (`TeamConnection!`): A list of teams that are ancestors of this team.
- **avatarUrl** (`URI`): A URL pointing to the team's avatar.
- **childTeams** (`TeamConnection!`): List of child teams belonging to this team.
- **combinedSlug** (`String!`): The slug corresponding to the organization and team.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **description** (`String`): The description of the team.
- **editTeamResourcePath** (`URI!`): The HTTP path for editing this team.
- **editTeamUrl** (`URI!`): The HTTP URL for editing this team.
- **id** (`ID!`): The Node ID of the Team object.
- **invitations** (`OrganizationInvitationConnection`): A list of pending invitations for users to this team.
- **memberStatuses** (`UserStatusConnection!`): Get the status messages members of this entity have set that are either public or visible only to the organization.
- **members** (`TeamMemberConnection!`): A list of users who are members of this team.
- **membersResourcePath** (`URI!`): The HTTP path for the team' members.
- **membersUrl** (`URI!`): The HTTP URL for the team' members.
- **name** (`String!`): The name of the team.
- **newTeamResourcePath** (`URI!`): The HTTP path creating a new team.
- **newTeamUrl** (`URI!`): The HTTP URL creating a new team.
- **notificationSetting** (`TeamNotificationSetting!`): The notification setting that the team has set.
- **organization** (`Organization!`): The organization that owns this team.
- **parentTeam** (`Team`): The parent team of the team.
- **privacy** (`TeamPrivacy!`): The level of privacy the team has.
- **projectV2** (`ProjectV2`): Finds and returns the project according to the provided project number.
- **projectsV2** (`ProjectV2Connection!`): List of projects this team has collaborator access to.
- **repositories** (`TeamRepositoryConnection!`): A list of repositories this team has access to.
- **repositoriesResourcePath** (`URI!`): The HTTP path for this team's repositories.
- **repositoriesUrl** (`URI!`): The HTTP URL for this team's repositories.
- **resourcePath** (`URI!`): The HTTP path for this team.
- **reviewRequestDelegationAlgorithm** (`TeamReviewAssignmentAlgorithm`): What algorithm is used for review assignment for this team.
- **reviewRequestDelegationEnabled** (`Boolean!`): True if review assignment is enabled for this team.
- **reviewRequestDelegationMemberCount** (`Int`): How many team members are required for review assignment for this team.
- **reviewRequestDelegationNotifyTeam** (`Boolean!`): When assigning team members via delegation, whether the entire team should be notified as well.
- **slug** (`String!`): The slug corresponding to the team.
- **teamsResourcePath** (`URI!`): The HTTP path for this team's teams.
- **teamsUrl** (`URI!`): The HTTP URL for this team's teams.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this team.
- **viewerCanAdminister** (`Boolean!`): Team is adminable by the viewer.
- **viewerCanSubscribe** (`Boolean!`): Check if the viewer is able to change their subscription status for the subscribable entity.
- **viewerSubscription** (`SubscriptionState`): Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

### User

A user is an individual's account on GitHub that owns repositories and can make new content.

**Implements:** Actor, Agentic, Node, PackageOwner, ProfileOwner, ProjectOwner, ProjectV2Owner, ProjectV2Recent, RepositoryDiscussionAuthor, RepositoryDiscussionCommentAuthor, RepositoryOwner, Sponsorable, UniformResourceLocatable

**Fields:**

- **anyPinnableItems** (`Boolean!`): Determine if this repository owner has any items that can be pinned to their profile.
- **avatarUrl** (`URI!`): A URL pointing to the user's public avatar.
- **bio** (`String`): The user's public profile bio.
- **bioHTML** (`HTML!`): The user's public profile bio as HTML.
- **canReceiveOrganizationEmailsWhenNotificationsRestricted** (`Boolean!`): Could this user receive email notifications, if the organization had notification restrictions enabled?.
- **commitComments** (`CommitCommentConnection!`): A list of commit comments made by this user.
- **company** (`String`): The user's public profile company.
- **companyHTML** (`HTML!`): The user's public profile company as HTML.
- **contributionsCollection** (`ContributionsCollection!`): The collection of contributions this user has made to different repositories.
- **copilotEndpoints** (`CopilotEndpoints`): The user's Copilot endpoint information.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **email** (`String!`): The user's publicly visible profile email.
- **enterprises** (`EnterpriseConnection`): A list of enterprises that the user belongs to.
- **estimatedNextSponsorsPayoutInCents** (`Int!`): The estimated next GitHub Sponsors payout for this user/organization in cents (USD).
- **followers** (`FollowerConnection!`): A list of users the given user is followed by.
- **following** (`FollowingConnection!`): A list of users the given user is following.
- **gist** (`Gist`): Find gist by repo name.
- **gistComments** (`GistCommentConnection!`): A list of gist comments made by this user.
- **gists** (`GistConnection!`): A list of the Gists the user has created.
- **hasSponsorsListing** (`Boolean!`): True if this user/organization has a GitHub Sponsors listing.
- **hovercard** (`Hovercard!`): The hovercard information for this user in a given context.
- **id** (`ID!`): The Node ID of the User object.
- **interactionAbility** (`RepositoryInteractionAbility`): The interaction ability settings for this user.
- **isBountyHunter** (`Boolean!`): Whether or not this user is a participant in the GitHub Security Bug Bounty.
- **isCampusExpert** (`Boolean!`): Whether or not this user is a participant in the GitHub Campus Experts Program.
- **isDeveloperProgramMember** (`Boolean!`): Whether or not this user is a GitHub Developer Program member.
- **isEmployee** (`Boolean!`): Whether or not this user is a GitHub employee.
- **isFollowingViewer** (`Boolean!`): Whether or not this user is following the viewer. Inverse of viewerIsFollowing.
- **isGitHubStar** (`Boolean!`): Whether or not this user is a member of the GitHub Stars Program.
- **isHireable** (`Boolean!`): Whether or not the user has marked themselves as for hire.
- **isSiteAdmin** (`Boolean!`): Whether or not this user is a site administrator.
- **isSponsoredBy** (`Boolean!`): Whether the given account is sponsoring this user/organization.
- **isSponsoringViewer** (`Boolean!`): True if the viewer is sponsored by this user/organization.
- **isViewer** (`Boolean!`): Whether or not this user is the viewing user.
- **issueComments** (`IssueCommentConnection!`): A list of issue comments made by this user.
- **issues** (`IssueConnection!`): A list of issues associated with this user.
- **itemShowcase** (`ProfileItemShowcase!`): Showcases a selection of repositories and gists that the profile owner has
either curated or that have been selected automatically based on popularity.
- **lifetimeReceivedSponsorshipValues** (`SponsorAndLifetimeValueConnection!`): Calculate how much each sponsor has ever paid total to this maintainer via
GitHub Sponsors. Does not include sponsorships paid via Patreon.
- **lists** (`UserListConnection!`): A user-curated list of repositories.
- **location** (`String`): The user's public profile location.
- **login** (`String!`): The username used to login.
- **monthlyEstimatedSponsorsIncomeInCents** (`Int!`): The estimated monthly GitHub Sponsors income for this user/organization in cents (USD).
- **name** (`String`): The user's public profile name.
- **organization** (`Organization`): Find an organization by its login that the user belongs to.
- **organizationVerifiedDomainEmails** (`[String!]!`): Verified email addresses that match verified domains for a specified organization the user is a member of.
- **organizations** (`OrganizationConnection!`): A list of organizations the user belongs to.
- **packages** (`PackageConnection!`): A list of packages under the owner.
- **pinnableItems** (`PinnableItemConnection!`): A list of repositories and gists this profile owner can pin to their profile.
- **pinnedItems** (`PinnableItemConnection!`): A list of repositories and gists this profile owner has pinned to their profile.
- **pinnedItemsRemaining** (`Int!`): Returns how many more items this profile owner can pin to their profile.
- **project** (`Project`): Find project by number.
- **projectV2** (`ProjectV2`): Find a project by number.
- **projects** (`ProjectConnection!`): A list of projects under the owner.
- **projectsResourcePath** (`URI!`): The HTTP path listing user's projects.
- **projectsUrl** (`URI!`): The HTTP URL listing user's projects.
- **projectsV2** (`ProjectV2Connection!`): A list of projects under the owner.
- **pronouns** (`String`): The user's profile pronouns.
- **publicKeys** (`PublicKeyConnection!`): A list of public keys associated with this user.
- **pullRequests** (`PullRequestConnection!`): A list of pull requests associated with this user.
- **recentProjects** (`ProjectV2Connection!`): Recent projects that this user has modified in the context of the owner.
- **repositories** (`RepositoryConnection!`): A list of repositories that the user owns.
- **repositoriesContributedTo** (`RepositoryConnection!`): A list of repositories that the user recently contributed to.
- **repository** (`Repository`): Find Repository.
- **repositoryDiscussionComments** (`DiscussionCommentConnection!`): Discussion comments this user has authored.
- **repositoryDiscussions** (`DiscussionConnection!`): Discussions this user has started.
- **resourcePath** (`URI!`): The HTTP path for this user.
- **savedReplies** (`SavedReplyConnection`): Replies this user has saved.
- **socialAccounts** (`SocialAccountConnection!`): The user's social media accounts, ordered as they appear on the user's profile.
- **sponsoring** (`SponsorConnection!`): List of users and organizations this entity is sponsoring.
- **sponsors** (`SponsorConnection!`): List of sponsors for this user or organization.
- **sponsorsActivities** (`SponsorsActivityConnection!`): Events involving this sponsorable, such as new sponsorships.
- **sponsorsListing** (`SponsorsListing`): The GitHub Sponsors listing for this user or organization.
- **sponsorshipForViewerAsSponsor** (`Sponsorship`): The sponsorship from the viewer to this user/organization; that is, the sponsorship where you're the sponsor.
- **sponsorshipForViewerAsSponsorable** (`Sponsorship`): The sponsorship from this user/organization to the viewer; that is, the sponsorship you're receiving.
- **sponsorshipNewsletters** (`SponsorshipNewsletterConnection!`): List of sponsorship updates sent from this sponsorable to sponsors.
- **sponsorshipsAsMaintainer** (`SponsorshipConnection!`): The sponsorships where this user or organization is the maintainer receiving the funds.
- **sponsorshipsAsSponsor** (`SponsorshipConnection!`): The sponsorships where this user or organization is the funder.
- **starredRepositories** (`StarredRepositoryConnection!`): Repositories the user has starred.
- **status** (`UserStatus`): The user's description of what they're currently doing.
- **suggestedListNames** (`[UserListSuggestion!]!`): Suggested names for user lists.
- **topRepositories** (`RepositoryConnection!`): Repositories the user has contributed to, ordered by contribution rank, plus repositories the user has created.
- **totalSponsorshipAmountAsSponsorInCents** (`Int`): The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has
spent on GitHub to fund sponsorships. Only returns a value when viewed by the
user themselves or by a user who can manage sponsorships for the requested organization.
- **twitterUsername** (`String`): The user's Twitter username.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this user.
- **userViewType** (`UserViewType!`): Whether the request returns publicly visible information or privately visible information about the user.
- **viewerCanChangePinnedItems** (`Boolean!`): Can the viewer pin repositories and gists to the profile?.
- **viewerCanCreateProjects** (`Boolean!`): Can the current viewer create new projects on this owner.
- **viewerCanFollow** (`Boolean!`): Whether or not the viewer is able to follow the user.
- **viewerCanSponsor** (`Boolean!`): Whether or not the viewer is able to sponsor this user/organization.
- **viewerCopilotAgentCreatesChannel** (`String`): Channel value for subscribing to live updates for session creations.
- **viewerCopilotAgentLogUpdatesChannel** (`String`): Channel value for subscribing to live updates for session log updates.
- **viewerCopilotAgentTaskUpdatesChannel** (`String`): Channel value for subscribing to live updates for task updates.
- **viewerCopilotAgentUpdatesChannel** (`String`): Channel value for subscribing to live updates for session updates.
- **viewerIsFollowing** (`Boolean!`): Whether or not this user is followed by the viewer. Inverse of isFollowingViewer.
- **viewerIsSponsoring** (`Boolean!`): True if the viewer is sponsoring this user/organization.
- **watching** (`RepositoryConnection!`): A list of repositories the given user is watching.
- **websiteUrl** (`URI`): A URL pointing to the user's public website/blog.

### UserBlockedEvent

Represents a`user_blocked`event on a given user.

**Implements:** Node

**Fields:**

- **actor** (`Actor`): Identifies the actor who performed the event.
- **blockDuration** (`UserBlockDuration!`): Number of days that the user was blocked for.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **id** (`ID!`): The Node ID of the UserBlockedEvent object.
- **subject** (`User`): The user who was blocked.

### UserContentEdit

An edit on user content.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **deletedAt** (`DateTime`): Identifies the date and time when the object was deleted.
- **deletedBy** (`Actor`): The actor who deleted this content.
- **diff** (`String`): A summary of the changes for this edit.
- **editedAt** (`DateTime!`): When this content was edited.
- **editor** (`Actor`): The actor who edited this content.
- **id** (`ID!`): The Node ID of the UserContentEdit object.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.

### UserEmailMetadata

Email attributes from External Identity.

**Fields:**

- **primary** (`Boolean`): Boolean to identify primary emails.
- **type** (`String`): Type of email.
- **value** (`String!`): Email id.

### UserList

A user-curated list of repositories.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **description** (`String`): The description of this list.
- **id** (`ID!`): The Node ID of the UserList object.
- **isPrivate** (`Boolean!`): Whether or not this list is private.
- **items** (`UserListItemsConnection!`): The items associated with this list.
- **lastAddedAt** (`DateTime!`): The date and time at which this list was created or last had items added to it.
- **name** (`String!`): The name of this list.
- **slug** (`String!`): The slug of this list.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **user** (`User!`): The user to which this list belongs.

### UserListSuggestion

Represents a suggested user list.

**Fields:**

- **id** (`ID`): The ID of the suggested user list.
- **name** (`String`): The name of the suggested user list.

### UserStatus

The user's description of what they're currently doing.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **emoji** (`String`): An emoji summarizing the user's status.
- **emojiHTML** (`HTML`): The status emoji as HTML.
- **expiresAt** (`DateTime`): If set, the status will not be shown after this date.
- **id** (`ID!`): The Node ID of the UserStatus object.
- **indicatesLimitedAvailability** (`Boolean!`): Whether this status indicates the user is not fully available on GitHub.
- **message** (`String`): A brief message describing what the user is doing.
- **organization** (`Organization`): The organization whose members can see this status. If null, this status is publicly visible.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **user** (`User!`): The user who has this status.

### ViewerHovercardContext

A hovercard context with a message describing how the viewer is related.

**Implements:** HovercardContext

**Fields:**

- **message** (`String!`): A string describing this context.
- **octicon** (`String!`): An octicon to accompany this context.
- **viewer** (`User!`): Identifies the user who is related to this context.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **EnterpriseOrganizationMembershipConnection** (4 fields): The connection type for Organization.
- **EnterpriseOrganizationMembershipEdge** (3 fields): An enterprise organization that a user is a member of.
- **EnterpriseServerUserAccountConnection** (4 fields): The connection type for EnterpriseServerUserAccount.
- **EnterpriseServerUserAccountEdge** (2 fields): An edge in a connection.
- **EnterpriseServerUserAccountEmailConnection** (4 fields): The connection type for EnterpriseServerUserAccountEmail.
- **EnterpriseServerUserAccountEmailEdge** (2 fields): An edge in a connection.
- **EnterpriseServerUserAccountsUploadConnection** (4 fields): The connection type for EnterpriseServerUserAccountsUpload.
- **EnterpriseServerUserAccountsUploadEdge** (2 fields): An edge in a connection.
- **ExternalIdentityConnection** (4 fields): The connection type for ExternalIdentity.
- **ExternalIdentityEdge** (2 fields): An edge in a connection.
- **FollowerConnection** (4 fields): The connection type for User.
- **FollowingConnection** (4 fields): The connection type for User.
- **GistCommentConnection** (4 fields): The connection type for GistComment.
- **GistCommentEdge** (2 fields): An edge in a connection.
- **GistConnection** (4 fields): The connection type for Gist.
- **GistEdge** (2 fields): An edge in a connection.
- **IpAllowListEntryConnection** (4 fields): The connection type for IpAllowListEntry.
- **IpAllowListEntryEdge** (2 fields): An edge in a connection.
- **MannequinConnection** (4 fields): A list of mannequins.
- **MannequinEdge** (2 fields): Represents a mannequin.
- **OrganizationAuditEntryConnection** (4 fields): The connection type for OrganizationAuditEntry.
- **OrganizationAuditEntryEdge** (2 fields): An edge in a connection.
- **OrganizationConnection** (4 fields): A list of organizations managed by an enterprise.
- **OrganizationEdge** (2 fields): An edge in a connection.
- **OrganizationEnterpriseOwnerConnection** (4 fields): The connection type for User.
- **OrganizationEnterpriseOwnerEdge** (3 fields): An enterprise owner in the context of an organization that is part of the enterprise.
- **OrganizationInvitationConnection** (4 fields): The connection type for OrganizationInvitation.
- **OrganizationInvitationEdge** (2 fields): An edge in a connection.
- **OrganizationMemberConnection** (4 fields): A list of users who belong to the organization.
- **OrganizationMemberEdge** (4 fields): Represents a user within an organization.
- **PublicKeyConnection** (4 fields): The connection type for PublicKey.
- **PublicKeyEdge** (2 fields): An edge in a connection.
- **ReactingUserConnection** (4 fields): The connection type for User.
- **ReactingUserEdge** (3 fields): Represents a user that's made a reaction.
- **SavedReplyConnection** (4 fields): The connection type for SavedReply.
- **SavedReplyEdge** (2 fields): An edge in a connection.
- **SocialAccountConnection** (4 fields): The connection type for SocialAccount.
- **SocialAccountEdge** (2 fields): An edge in a connection.
- **TeamConnection** (4 fields): The connection type for Team.
- **TeamEdge** (2 fields): An edge in a connection.
- **TeamMemberConnection** (4 fields): The connection type for User.
- **TeamMemberEdge** (5 fields): Represents a user who is a member of a team.
- **UserConnection** (4 fields): A list of users.
- **UserContentEditConnection** (4 fields): A list of edits to content.
- **UserContentEditEdge** (2 fields): An edge in a connection.
- **UserEdge** (2 fields): Represents a user.
- **UserListConnection** (4 fields): The connection type for UserList.
- **UserListEdge** (2 fields): An edge in a connection.
- **UserListItemsConnection** (4 fields): The connection type for UserListItems.
- **UserListItemsEdge** (2 fields): An edge in a connection.
- **UserStatusConnection** (4 fields): The connection type for UserStatus.
- **UserStatusEdge** (2 fields): An edge in a connection.

## Interfaces

### HovercardContext

An individual line of a hovercard.

**Fields:**

- **message** (`String!`): A string describing this context.
- **octicon** (`String!`): An octicon to accompany this context.

### OrganizationAuditEntryData

Metadata for an audit entry with action org.*.

**Fields:**

- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.

## Enums

### EnterpriseServerUserAccountEmailOrderField

Properties by which Enterprise Server user account email connections can be ordered.

**Values:**

- `EMAIL`: Order emails by email.

### EnterpriseServerUserAccountOrderField

Properties by which Enterprise Server user account connections can be ordered.

**Values:**

- `LOGIN`: Order user accounts by login.
- `REMOTE_CREATED_AT`: Order user accounts by creation time on the Enterprise Server installation.

### EnterpriseServerUserAccountsUploadOrderField

Properties by which Enterprise Server user accounts upload connections can be ordered.

**Values:**

- `CREATED_AT`: Order user accounts uploads by creation time.

### EnterpriseServerUserAccountsUploadSyncState

Synchronization state of the Enterprise Server user accounts upload.

**Values:**

- `FAILURE`: The synchronization of the upload failed.
- `PENDING`: The synchronization of the upload is pending.
- `SUCCESS`: The synchronization of the upload succeeded.

### EnterpriseUserAccountMembershipRole

The possible roles for enterprise membership.

**Values:**

- `MEMBER`: The user is a member of an organization in the enterprise.
- `OWNER`: The user is an owner of an organization in the enterprise.
- `UNAFFILIATED`: The user is not an owner of the enterprise, and not a member or owner of any
organizations in the enterprise; only for EMU-enabled enterprises.

### EnterpriseUserDeployment

The possible GitHub Enterprise deployments where this user can exist.

**Values:**

- `CLOUD`: The user is part of a GitHub Enterprise Cloud deployment.
- `SERVER`: The user is part of a GitHub Enterprise Server deployment.

### GistOrderField

Properties by which gist connections can be ordered.

**Values:**

- `CREATED_AT`: Order gists by creation time.
- `PUSHED_AT`: Order gists by push time.
- `UPDATED_AT`: Order gists by update time.

### GistPrivacy

The privacy of a Gist.

**Values:**

- `ALL`: Gists that are public and secret.
- `PUBLIC`: Public.
- `SECRET`: Secret.

### IpAllowListEnabledSettingValue

The possible values for the IP allow list enabled setting.

**Values:**

- `DISABLED`: The setting is disabled for the owner.
- `ENABLED`: The setting is enabled for the owner.

### IpAllowListEntryOrderField

Properties by which IP allow list entry connections can be ordered.

**Values:**

- `ALLOW_LIST_VALUE`: Order IP allow list entries by the allow list value.
- `CREATED_AT`: Order IP allow list entries by creation time.

### IpAllowListForInstalledAppsEnabledSettingValue

The possible values for the IP allow list configuration for installed GitHub Apps setting.

**Values:**

- `DISABLED`: The setting is disabled for the owner.
- `ENABLED`: The setting is enabled for the owner.

### IpAllowListUserLevelEnforcementEnabledSettingValue

The possible values for the IP allow list user-level enforcement enabled setting.

**Values:**

- `DISABLED`: The setting is disabled for the owner.
- `ENABLED`: The setting is enabled for the owner.

### MannequinOrderField

Properties by which mannequins can be ordered.

**Values:**

- `CREATED_AT`: Order mannequins why when they were created.
- `LOGIN`: Order mannequins alphabetically by their source login.

### OIDCProviderType

The OIDC identity provider type.

**Values:**

- `AAD`: Azure Active Directory.

### OrganizationInvitationRole

The possible organization invitation roles.

**Values:**

- `ADMIN`: The user is invited to be an admin of the organization.
- `BILLING_MANAGER`: The user is invited to be a billing manager of the organization.
- `DIRECT_MEMBER`: The user is invited to be a direct member of the organization.
- `REINSTATE`: The user's previous role will be reinstated.

### OrganizationInvitationSource

The possible organization invitation sources.

**Values:**

- `MEMBER`: The invitation was created from the web interface or from API.
- `SCIM`: The invitation was created from SCIM.
- `UNKNOWN`: The invitation was sent before this feature was added.

### OrganizationInvitationType

The possible organization invitation types.

**Values:**

- `EMAIL`: The invitation was to an email address.
- `USER`: The invitation was to an existing user.

### OrganizationMemberRole

The possible roles within an organization for its members.

**Values:**

- `ADMIN`: The user is an administrator of the organization.
- `MEMBER`: The user is a member of the organization.

### OrganizationMigrationState

The Octoshift Organization migration state.

**Values:**

- `FAILED`: The Octoshift migration has failed.
- `FAILED_VALIDATION`: The Octoshift migration has invalid credentials.
- `IN_PROGRESS`: The Octoshift migration is in progress.
- `NOT_STARTED`: The Octoshift migration has not started.
- `PENDING_VALIDATION`: The Octoshift migration needs to have its credentials validated.
- `POST_REPO_MIGRATION`: The Octoshift migration is performing post repository migrations.
- `PRE_REPO_MIGRATION`: The Octoshift migration is performing pre repository migrations.
- `QUEUED`: The Octoshift migration has been queued.
- `REPO_MIGRATION`: The Octoshift org migration is performing repository migrations.
- `SUCCEEDED`: The Octoshift migration has succeeded.

### OrganizationOrderField

Properties by which organization connections can be ordered.

**Values:**

- `CREATED_AT`: Order organizations by creation time.
- `LOGIN`: Order organizations by login.

### RoleInOrganization

Possible roles a user may have in relation to an organization.

**Values:**

- `DIRECT_MEMBER`: A user who is a direct member of the organization.
- `OWNER`: A user with full administrative access to the organization.
- `UNAFFILIATED`: A user who is unaffiliated with the organization.

### SavedReplyOrderField

Properties by which saved reply connections can be ordered.

**Values:**

- `UPDATED_AT`: Order saved reply by when they were updated.

### SocialAccountProvider

Software or company that hosts social media accounts.

**Values:**

- `BLUESKY`: Decentralized microblogging social platform.
- `FACEBOOK`: Social media and networking website.
- `GENERIC`: Catch-all for social media providers that do not yet have specific handling.
- `HOMETOWN`: Fork of Mastodon with a greater focus on local posting.
- `INSTAGRAM`: Social media website with a focus on photo and video sharing.
- `LINKEDIN`: Professional networking website.
- `MASTODON`: Open-source federated microblogging service.
- `NPM`: JavaScript package registry.
- `REDDIT`: Social news aggregation and discussion website.
- `TWITCH`: Live-streaming service.
- `TWITTER`: Microblogging website.
- `YOUTUBE`: Online video platform.

### TeamMemberOrderField

Properties by which team member connections can be ordered.

**Values:**

- `CREATED_AT`: Order team members by creation time.
- `LOGIN`: Order team members by login.

### TeamMemberRole

The possible team member roles; either`maintainer`or 'member'.

**Values:**

- `MAINTAINER`: A team maintainer has permission to add and remove team members.
- `MEMBER`: A team member has no administrative permissions on the team.

### TeamMembershipType

Defines which types of team members are included in the returned list. Can be one of IMMEDIATE, CHILD_TEAM or ALL.

**Values:**

- `ALL`: Includes immediate and child team members for the team.
- `CHILD_TEAM`: Includes only child team members for the team.
- `IMMEDIATE`: Includes only immediate members of the team.

### TeamNotificationSetting

The possible team notification values.

**Values:**

- `NOTIFICATIONS_DISABLED`: No one will receive notifications.
- `NOTIFICATIONS_ENABLED`: Everyone will receive notifications when the team is @mentioned.

### TeamOrderField

Properties by which team connections can be ordered.

**Values:**

- `NAME`: Allows ordering a list of teams by name.

### TeamPrivacy

The possible team privacy values.

**Values:**

- `SECRET`: A secret team can only be seen by its members.
- `VISIBLE`: A visible team can be seen and @mentioned by every member of the organization.

### TeamReviewAssignmentAlgorithm

The possible team review assignment algorithms.

**Values:**

- `LOAD_BALANCE`: Balance review load across the entire team.
- `ROUND_ROBIN`: Alternate reviews between each team member.

### TeamRole

The role of a user on a team.

**Values:**

- `ADMIN`: User has admin rights on the team.
- `MEMBER`: User is a member of the team.

### UserBlockDuration

The possible durations that a user can be blocked for.

**Values:**

- `ONE_DAY`: The user was blocked for 1 day.
- `ONE_MONTH`: The user was blocked for 30 days.
- `ONE_WEEK`: The user was blocked for 7 days.
- `PERMANENT`: The user was blocked permanently.
- `THREE_DAYS`: The user was blocked for 3 days.

### UserStatusOrderField

Properties by which user status connections can be ordered.

**Values:**

- `UPDATED_AT`: Order user statuses by when they were updated.

### UserViewType

Whether a user being viewed contains public or private information.

**Values:**

- `PRIVATE`: A user containing information only visible to the authenticated user.
- `PUBLIC`: A user that is publicly visible.

## Input Objects

### AddEnterpriseOrganizationMemberInput

Autogenerated input type of AddEnterpriseOrganizationMember.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise which owns the organization.
- **organizationId** (`ID!`): The ID of the organization the users will be added to.
- **role** (`OrganizationMemberRole`): The role to assign the users in the organization.
- **userIds** (`[ID!]!`): The IDs of the enterprise members to add.

### ChangeUserStatusInput

Autogenerated input type of ChangeUserStatus.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **emoji** (`String`): The emoji to represent your status. Can either be a native Unicode emoji or an emoji name with colons, e.g., 😀.
- **expiresAt** (`DateTime`): If set, the user status will not be shown after this date.
- **limitedAvailability** (`Boolean`): Whether this status should indicate you are not fully available on GitHub, e.g., you are away.
- **message** (`String`): A short description of your current status.
- **organizationId** (`ID`): The ID of the organization whose members will be allowed to see the status. If
omitted, the status will be publicly visible.

### CreateEnterpriseOrganizationInput

Autogenerated input type of CreateEnterpriseOrganization.

**Input fields:**

- **adminLogins** (`[String!]!`): The logins for the administrators of the new organization.
- **billingEmail** (`String!`): The email used for sending billing receipts.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise owning the new organization.
- **login** (`String!`): The login of the new organization.
- **profileName** (`String!`): The profile name of the new organization.

### CreateIpAllowListEntryInput

Autogenerated input type of CreateIpAllowListEntry.

**Input fields:**

- **allowListValue** (`String!`): An IP address or range of addresses in CIDR notation.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **isActive** (`Boolean!`): Whether the IP allow list entry is active when an IP allow list is enabled.
- **name** (`String`): An optional name for the IP allow list entry.
- **ownerId** (`ID!`): The ID of the owner for which to create the new IP allow list entry.

### CreateUserListInput

Autogenerated input type of CreateUserList.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **description** (`String`): A description of the list.
- **isPrivate** (`Boolean`): Whether or not the list is private.
- **name** (`String!`): The name of the new list.

### DeleteIpAllowListEntryInput

Autogenerated input type of DeleteIpAllowListEntry.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ipAllowListEntryId** (`ID!`): The ID of the IP allow list entry to delete.

### DeleteUserListInput

Autogenerated input type of DeleteUserList.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **listId** (`ID!`): The ID of the list to delete.

### EnterpriseServerUserAccountEmailOrder

Ordering options for Enterprise Server user account email connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`EnterpriseServerUserAccountEmailOrderField!`): The field to order emails by.

### EnterpriseServerUserAccountOrder

Ordering options for Enterprise Server user account connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`EnterpriseServerUserAccountOrderField!`): The field to order user accounts by.

### EnterpriseServerUserAccountsUploadOrder

Ordering options for Enterprise Server user accounts upload connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`EnterpriseServerUserAccountsUploadOrderField!`): The field to order user accounts uploads by.

### FollowOrganizationInput

Autogenerated input type of FollowOrganization.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organizationId** (`ID!`): ID of the organization to follow.

### FollowUserInput

Autogenerated input type of FollowUser.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **userId** (`ID!`): ID of the user to follow.

### GistOrder

Ordering options for gist connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`GistOrderField!`): The field to order repositories by.

### GrantEnterpriseOrganizationsMigratorRoleInput

Autogenerated input type of GrantEnterpriseOrganizationsMigratorRole.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise to which all organizations managed by it will be granted the migrator role.
- **login** (`String!`): The login of the user to grant the migrator role.

### IpAllowListEntryOrder

Ordering options for IP allow list entry connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`IpAllowListEntryOrderField!`): The field to order IP allow list entries by.

### LinkProjectV2ToTeamInput

Autogenerated input type of LinkProjectV2ToTeam.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the project to link to the team.
- **teamId** (`ID!`): The ID of the team to link to the project.

### MannequinOrder

Ordering options for mannequins.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`MannequinOrderField!`): The field to order mannequins by.

### OrganizationOrder

Ordering options for organization connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`OrganizationOrderField!`): The field to order organizations by.

### OrganizationPropertyConditionTargetInput

Parameters to be used for the organization_property condition.

**Input fields:**

- **exclude** (`[OrganizationPropertyTargetDefinitionInput!]!`): Array of organization properties that must not match.
- **include** (`[OrganizationPropertyTargetDefinitionInput!]!`): Array of organization properties that must match.

### OrganizationPropertyTargetDefinitionInput

A property that must match.

**Input fields:**

- **name** (`String!`): The name of the property.
- **propertyValues** (`[String!]!`): The values to match for.

### RemoveEnterpriseOrganizationInput

Autogenerated input type of RemoveEnterpriseOrganization.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise from which the organization should be removed.
- **organizationId** (`ID!`): The ID of the organization to remove from the enterprise.

### RevokeEnterpriseOrganizationsMigratorRoleInput

Autogenerated input type of RevokeEnterpriseOrganizationsMigratorRole.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise to which all organizations managed by it will be granted the migrator role.
- **login** (`String!`): The login of the user to revoke the migrator role.

### SavedReplyOrder

Ordering options for saved reply connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`SavedReplyOrderField!`): The field to order saved replies by.

### SetOrganizationInteractionLimitInput

Autogenerated input type of SetOrganizationInteractionLimit.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **expiry** (`RepositoryInteractionLimitExpiry`): When this limit should expire.
- **limit** (`RepositoryInteractionLimit!`): The limit to set.
- **organizationId** (`ID!`): The ID of the organization to set a limit for.

### SetUserInteractionLimitInput

Autogenerated input type of SetUserInteractionLimit.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **expiry** (`RepositoryInteractionLimitExpiry`): When this limit should expire.
- **limit** (`RepositoryInteractionLimit!`): The limit to set.
- **userId** (`ID!`): The ID of the user to set a limit for.

### StartOrganizationMigrationInput

Autogenerated input type of StartOrganizationMigration.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **sourceAccessToken** (`String!`): The migration source access token.
- **sourceOrgUrl** (`URI!`): The URL of the organization to migrate.
- **targetEnterpriseId** (`ID!`): The ID of the enterprise the target organization belongs to.
- **targetOrgName** (`String!`): The name of the target organization.

### TeamMemberOrder

Ordering options for team member connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`TeamMemberOrderField!`): The field to order team members by.

### TeamOrder

Ways in which team connections can be ordered.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order nodes.
- **field** (`TeamOrderField!`): The field in which to order nodes by.

### TransferEnterpriseOrganizationInput

Autogenerated input type of TransferEnterpriseOrganization.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **destinationEnterpriseId** (`ID!`): The ID of the enterprise where the organization should be transferred.
- **organizationId** (`ID!`): The ID of the organization to transfer.

### UnfollowOrganizationInput

Autogenerated input type of UnfollowOrganization.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **organizationId** (`ID!`): ID of the organization to unfollow.

### UnfollowUserInput

Autogenerated input type of UnfollowUser.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **userId** (`ID!`): ID of the user to unfollow.

### UnlinkProjectV2FromTeamInput

Autogenerated input type of UnlinkProjectV2FromTeam.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **projectId** (`ID!`): The ID of the project to unlink from the team.
- **teamId** (`ID!`): The ID of the team to unlink from the project.

### UpdateEnterpriseOrganizationProjectsSettingInput

Autogenerated input type of UpdateEnterpriseOrganizationProjectsSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the organization projects setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the organization projects setting on the enterprise.

### UpdateEnterpriseOwnerOrganizationRoleInput

Autogenerated input type of UpdateEnterpriseOwnerOrganizationRole.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the Enterprise which the owner belongs to.
- **organizationId** (`ID!`): The ID of the organization for membership change.
- **organizationRole** (`RoleInOrganization!`): The role to assume in the organization.

### UpdateIpAllowListEnabledSettingInput

Autogenerated input type of UpdateIpAllowListEnabledSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ownerId** (`ID!`): The ID of the owner on which to set the IP allow list enabled setting.
- **settingValue** (`IpAllowListEnabledSettingValue!`): The value for the IP allow list enabled setting.

### UpdateIpAllowListEntryInput

Autogenerated input type of UpdateIpAllowListEntry.

**Input fields:**

- **allowListValue** (`String!`): An IP address or range of addresses in CIDR notation.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ipAllowListEntryId** (`ID!`): The ID of the IP allow list entry to update.
- **isActive** (`Boolean!`): Whether the IP allow list entry is active when an IP allow list is enabled.
- **name** (`String`): An optional name for the IP allow list entry.

### UpdateIpAllowListForInstalledAppsEnabledSettingInput

Autogenerated input type of UpdateIpAllowListForInstalledAppsEnabledSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ownerId** (`ID!`): The ID of the owner.
- **settingValue** (`IpAllowListForInstalledAppsEnabledSettingValue!`): The value for the IP allow list configuration for installed GitHub Apps setting.

### UpdateIpAllowListUserLevelEnforcementEnabledSettingInput

Autogenerated input type of UpdateIpAllowListUserLevelEnforcementEnabledSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **ownerId** (`ID!`): The ID of the owner.
- **settingValue** (`IpAllowListUserLevelEnforcementEnabledSettingValue!`): The value for the IP allow list user-level enforcement enabled setting.

### UpdateTeamReviewAssignmentInput

Autogenerated input type of UpdateTeamReviewAssignment.

**Input fields:**

- **algorithm** (`TeamReviewAssignmentAlgorithm`): The algorithm to use for review assignment.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **countMembersAlreadyRequested** (`Boolean`): Count any members whose review has already been requested against the required number of members assigned to review.
- **enabled** (`Boolean!`): Turn on or off review assignment.
- **excludedTeamMemberIds** (`[ID!]`): An array of team member IDs to exclude.
- **id** (`ID!`): The Node ID of the team to update review assignments of.
- **includeChildTeamMembers** (`Boolean`): Include the members of any child teams when assigning.
- **notifyTeam** (`Boolean`): Notify the entire team of the PR if it is delegated.
- **removeTeamRequest** (`Boolean`): Remove the team review request when assigning.
- **teamMemberCount** (`Int`): The number of team members to assign.

### UpdateUserListInput

Autogenerated input type of UpdateUserList.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **description** (`String`): A description of the list.
- **isPrivate** (`Boolean`): Whether or not the list is private.
- **listId** (`ID!`): The ID of the list to update.
- **name** (`String`): The name of the list.

### UpdateUserListsForItemInput

Autogenerated input type of UpdateUserListsForItem.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **itemId** (`ID!`): The item to add to the list.
- **listIds** (`[ID!]!`): The lists to which this item should belong.
- **suggestedListIds** (`[ID!]`): The suggested lists to create and add this item to.

### UserStatusOrder

Ordering options for user status connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`UserStatusOrderField!`): The field to order user statuses by.

## Unions

### IpAllowListOwner

Types that can own an IP allow list.

**Possible types:** App, Enterprise, Organization

### OrganizationAuditEntry

An audit entry in an organization audit log.

**Possible types:** MembersCanDeleteReposClearAuditEntry, MembersCanDeleteReposDisableAuditEntry, MembersCanDeleteReposEnableAuditEntry, OauthApplicationCreateAuditEntry, OrgAddBillingManagerAuditEntry, OrgAddMemberAuditEntry, OrgBlockUserAuditEntry, OrgConfigDisableCollaboratorsOnlyAuditEntry, OrgConfigEnableCollaboratorsOnlyAuditEntry, OrgCreateAuditEntry, OrgDisableOauthAppRestrictionsAuditEntry, OrgDisableSamlAuditEntry, OrgDisableTwoFactorRequirementAuditEntry, OrgEnableOauthAppRestrictionsAuditEntry, OrgEnableSamlAuditEntry, OrgEnableTwoFactorRequirementAuditEntry, OrgInviteMemberAuditEntry, OrgInviteToBusinessAuditEntry, OrgOauthAppAccessApprovedAuditEntry, OrgOauthAppAccessBlockedAuditEntry, OrgOauthAppAccessDeniedAuditEntry, OrgOauthAppAccessRequestedAuditEntry, OrgOauthAppAccessUnblockedAuditEntry, OrgRemoveBillingManagerAuditEntry, OrgRemoveMemberAuditEntry, OrgRemoveOutsideCollaboratorAuditEntry, OrgRestoreMemberAuditEntry, OrgUnblockUserAuditEntry, OrgUpdateDefaultRepositoryPermissionAuditEntry, OrgUpdateMemberAuditEntry, OrgUpdateMemberRepositoryCreationPermissionAuditEntry, OrgUpdateMemberRepositoryInvitationPermissionAuditEntry, PrivateRepositoryForkingDisableAuditEntry, PrivateRepositoryForkingEnableAuditEntry, RepoAccessAuditEntry, RepoAddMemberAuditEntry, RepoAddTopicAuditEntry, RepoArchivedAuditEntry, RepoChangeMergeSettingAuditEntry, RepoConfigDisableAnonymousGitAccessAuditEntry, RepoConfigDisableCollaboratorsOnlyAuditEntry, RepoConfigDisableContributorsOnlyAuditEntry, RepoConfigDisableSockpuppetDisallowedAuditEntry, RepoConfigEnableAnonymousGitAccessAuditEntry, RepoConfigEnableCollaboratorsOnlyAuditEntry, RepoConfigEnableContributorsOnlyAuditEntry, RepoConfigEnableSockpuppetDisallowedAuditEntry, RepoConfigLockAnonymousGitAccessAuditEntry, RepoConfigUnlockAnonymousGitAccessAuditEntry, RepoCreateAuditEntry, RepoDestroyAuditEntry, RepoRemoveMemberAuditEntry, RepoRemoveTopicAuditEntry, RepositoryVisibilityChangeDisableAuditEntry, RepositoryVisibilityChangeEnableAuditEntry, TeamAddMemberAuditEntry, TeamAddRepositoryAuditEntry, TeamChangeParentTeamAuditEntry, TeamRemoveMemberAuditEntry, TeamRemoveRepositoryAuditEntry

### OrganizationOrUser

Used for argument of CreateProjectV2 mutation.

**Possible types:** Organization, User

### UserListItems

Types that can be added to a user list.

**Possible types:** Repository
