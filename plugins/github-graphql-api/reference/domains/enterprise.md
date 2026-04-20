# Enterprise Administration

## Queries

### enterprise

**Returns:** `Enterprise`

Look up an enterprise by URL slug.

**Arguments:**

- `invitationToken` (`String`): The enterprise invitation token.
- `slug` (`String!`): The enterprise URL slug.

### enterpriseAdministratorInvitation

**Returns:** `EnterpriseAdministratorInvitation`

Look up a pending enterprise administrator invitation by invitee, enterprise and role.

**Arguments:**

- `enterpriseSlug` (`String!`): The slug of the enterprise the user was invited to join.
- `role` (`EnterpriseAdministratorRole!`): The role for the enterprise member invitation.
- `userLogin` (`String!`): The login of the user invited to join the enterprise.

### enterpriseAdministratorInvitationByToken

**Returns:** `EnterpriseAdministratorInvitation`

Look up a pending enterprise administrator invitation by invitation token.

**Arguments:**

- `invitationToken` (`String!`): The invitation token sent with the invitation email.

### enterpriseMemberInvitation

**Returns:** `EnterpriseMemberInvitation`

Look up a pending enterprise unaffiliated member invitation by invitee and enterprise.

**Arguments:**

- `enterpriseSlug` (`String!`): The slug of the enterprise the user was invited to join.
- `userLogin` (`String!`): The login of the user invited to join the enterprise.

### enterpriseMemberInvitationByToken

**Returns:** `EnterpriseMemberInvitation`

Look up a pending enterprise unaffiliated member invitation by invitation token.

**Arguments:**

- `invitationToken` (`String!`): The invitation token sent with the invitation email.

## Mutations

### addEnterpriseSupportEntitlement

Adds a support entitlement to an enterprise member.

**Input fields:**

- **input** (`AddEnterpriseSupportEntitlementInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **message** (`String`): A message confirming the result of adding the support entitlement.

### inviteEnterpriseAdmin

Invite someone to become an administrator of the enterprise.

**Input fields:**

- **input** (`InviteEnterpriseAdminInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitation** (`EnterpriseAdministratorInvitation`): The created enterprise administrator invitation.

### inviteEnterpriseMember

Invite someone to become an unaffiliated member of the enterprise.

**Input fields:**

- **input** (`InviteEnterpriseMemberInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitation** (`EnterpriseMemberInvitation`): The created enterprise member invitation.

### regenerateEnterpriseIdentityProviderRecoveryCodes

Regenerates the identity provider recovery codes for an enterprise.

**Input fields:**

- **input** (`RegenerateEnterpriseIdentityProviderRecoveryCodesInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **identityProvider** (`EnterpriseIdentityProvider`): The identity provider for the enterprise.

### removeEnterpriseAdmin

Removes an administrator from the enterprise.

**Input fields:**

- **input** (`RemoveEnterpriseAdminInput!`)

**Return fields:**

- **admin** (`User`): The user who was removed as an administrator.
- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The updated enterprise.
- **message** (`String`): A message confirming the result of removing an administrator.
- **viewer** (`User`): The viewer performing the mutation.

### removeEnterpriseIdentityProvider

Removes the identity provider from an enterprise. Owners of enterprises both
with and without Enterprise Managed Users may use this mutation.

**Input fields:**

- **input** (`RemoveEnterpriseIdentityProviderInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **identityProvider** (`EnterpriseIdentityProvider`): The identity provider that was removed from the enterprise.

### removeEnterpriseMember

Completely removes a user from the enterprise.

**Input fields:**

- **input** (`RemoveEnterpriseMemberInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The updated enterprise.
- **user** (`User`): The user that was removed from the enterprise.
- **viewer** (`User`): The viewer performing the mutation.

### removeEnterpriseSupportEntitlement

Removes a support entitlement from an enterprise member.

**Input fields:**

- **input** (`RemoveEnterpriseSupportEntitlementInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **message** (`String`): A message confirming the result of removing the support entitlement.

### setEnterpriseIdentityProvider

Creates or updates the identity provider for an enterprise.

**Input fields:**

- **input** (`SetEnterpriseIdentityProviderInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **identityProvider** (`EnterpriseIdentityProvider`): The identity provider for the enterprise.

### updateEnterpriseAdministratorRole

Updates the role of an enterprise administrator.

**Input fields:**

- **input** (`UpdateEnterpriseAdministratorRoleInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **message** (`String`): A message confirming the result of changing the administrator's role.

### updateEnterpriseMembersCanInviteCollaboratorsSetting

Sets whether members can invite collaborators are enabled for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated members can invite collaborators setting.
- **message** (`String`): A message confirming the result of updating the members can invite collaborators setting.

### updateEnterpriseMembersCanMakePurchasesSetting

Sets whether or not an organization owner can make purchases.

**Input fields:**

- **input** (`UpdateEnterpriseMembersCanMakePurchasesSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated members can make purchases setting.
- **message** (`String`): A message confirming the result of updating the members can make purchases setting.

### updateEnterpriseMembersCanViewDependencyInsightsSetting

Sets the members can view dependency insights for an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated members can view dependency insights setting.
- **message** (`String`): A message confirming the result of updating the members can view dependency insights setting.

### updateEnterpriseProfile

Updates an enterprise's profile.

**Input fields:**

- **input** (`UpdateEnterpriseProfileInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The updated enterprise.

### updateEnterpriseTwoFactorAuthenticationDisallowedMethodsSetting

Sets the two-factor authentication methods that users of an enterprise may not use.

**Input fields:**

- **input** (`UpdateEnterpriseTwoFactorAuthenticationDisallowedMethodsSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated two-factor authentication disallowed methods setting.
- **message** (`String`): A message confirming the result of updating the two-factor authentication disallowed methods setting.

### updateEnterpriseTwoFactorAuthenticationRequiredSetting

Sets whether two factor authentication is required for all users in an enterprise.

**Input fields:**

- **input** (`UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput!`)

**Return fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterprise** (`Enterprise`): The enterprise with the updated two factor authentication required setting.
- **message** (`String`): A message confirming the result of updating the two factor authentication required setting.

## Types

### Enterprise

An account to manage multiple organizations with consolidated policy and billing.

**Implements:** Node

**Fields:**

- **announcementBanner** (`AnnouncementBanner`): The announcement banner set on this enterprise, if any. Only visible to members of the enterprise.
- **avatarUrl** (`URI!`): A URL pointing to the enterprise's public avatar.
- **billingEmail** (`String`): The enterprise's billing email.
- **billingInfo** (`EnterpriseBillingInfo`): Enterprise billing information visible to enterprise billing managers.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **description** (`String`): The description of the enterprise.
- **descriptionHTML** (`HTML!`): The description of the enterprise as HTML.
- **id** (`ID!`): The Node ID of the Enterprise object.
- **location** (`String`): The location of the enterprise.
- **members** (`EnterpriseMemberConnection!`): A list of users who are members of this enterprise.
- **name** (`String!`): The name of the enterprise.
- **organizations** (`OrganizationConnection!`): A list of organizations that belong to this enterprise.
- **ownerInfo** (`EnterpriseOwnerInfo`): Enterprise information visible to enterprise owners or enterprise owners'
personal access tokens (classic) with read:enterprise or admin:enterprise scope.
- **readme** (`String`): The raw content of the enterprise README.
- **readmeHTML** (`HTML!`): The content of the enterprise README as HTML.
- **repositoryCustomProperties** (`RepositoryCustomPropertyConnection`): A list of repository custom properties for this enterprise.
- **repositoryCustomProperty** (`RepositoryCustomProperty`): Returns a single repository custom property for the current enterprise by name.
- **resourcePath** (`URI!`): The HTTP path for this enterprise.
- **ruleset** (`RepositoryRuleset`): Returns a single ruleset from the current enterprise by ID.
- **rulesets** (`RepositoryRulesetConnection`): A list of rulesets for this enterprise.
- **securityContactEmail** (`String`): The enterprise's security contact email address.
- **slug** (`String!`): The URL-friendly identifier for the enterprise.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this enterprise.
- **userNamespaceRepositories** (`UserNamespaceRepositoryConnection!`): A list of repositories that belong to users. Only available for enterprises with Enterprise Managed Users.
- **viewerIsAdmin** (`Boolean!`): Is the current viewer an admin of this enterprise?.
- **websiteUrl** (`URI`): The URL of the enterprise website.

### EnterpriseAdministratorInvitation

An invitation for a user to become an owner or billing manager of an enterprise.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **email** (`String`): The email of the person who was invited to the enterprise.
- **enterprise** (`Enterprise!`): The enterprise the invitation is for.
- **id** (`ID!`): The Node ID of the EnterpriseAdministratorInvitation object.
- **invitee** (`User`): The user who was invited to the enterprise.
- **inviter** (`User`): The user who created the invitation.
- **role** (`EnterpriseAdministratorRole!`): The invitee's pending role in the enterprise (owner or billing_manager).

### EnterpriseBillingInfo

Enterprise billing information visible to enterprise billing managers and owners.

**Fields:**

- **allLicensableUsersCount** (`Int!`): The number of licenseable users/emails across the enterprise.
- **assetPacks** (`Int!`): The number of data packs used by all organizations owned by the enterprise.
- **bandwidthQuota** (`Float!`): The bandwidth quota in GB for all organizations owned by the enterprise.
- **bandwidthUsage** (`Float!`): The bandwidth usage in GB for all organizations owned by the enterprise.
- **bandwidthUsagePercentage** (`Int!`): The bandwidth usage as a percentage of the bandwidth quota.
- **storageQuota** (`Float!`): The storage quota in GB for all organizations owned by the enterprise.
- **storageUsage** (`Float!`): The storage usage in GB for all organizations owned by the enterprise.
- **storageUsagePercentage** (`Int!`): The storage usage as a percentage of the storage quota.
- **totalAvailableLicenses** (`Int!`): The number of available licenses across all owned organizations based on the unique number of billable users.
- **totalLicenses** (`Int!`): The total number of licenses allocated.

### EnterpriseIdentityProvider

An identity provider configured to provision identities for an enterprise.
Visible to enterprise owners or enterprise owners' personal access tokens
(classic) with read:enterprise or admin:enterprise scope.

**Implements:** Node

**Fields:**

- **digestMethod** (`SamlDigestAlgorithm`): The digest algorithm used to sign SAML requests for the identity provider.
- **enterprise** (`Enterprise`): The enterprise this identity provider belongs to.
- **externalIdentities** (`ExternalIdentityConnection!`): ExternalIdentities provisioned by this identity provider.
- **id** (`ID!`): The Node ID of the EnterpriseIdentityProvider object.
- **idpCertificate** (`X509Certificate`): The x509 certificate used by the identity provider to sign assertions and responses.
- **issuer** (`String`): The Issuer Entity ID for the SAML identity provider.
- **recoveryCodes** (`[String!]`): Recovery codes that can be used by admins to access the enterprise if the identity provider is unavailable.
- **signatureMethod** (`SamlSignatureAlgorithm`): The signature algorithm used to sign SAML requests for the identity provider.
- **ssoUrl** (`URI`): The URL endpoint for the identity provider's SAML SSO.

### EnterpriseMemberInvitation

An invitation for a user to become an unaffiliated member of an enterprise.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **email** (`String`): The email of the person who was invited to the enterprise.
- **enterprise** (`Enterprise!`): The enterprise the invitation is for.
- **id** (`ID!`): The Node ID of the EnterpriseMemberInvitation object.
- **invitee** (`User`): The user who was invited to the enterprise.
- **inviter** (`User`): The user who created the invitation.

### EnterpriseOwnerInfo

Enterprise information visible to enterprise owners or enterprise owners'
personal access tokens (classic) with read:enterprise or admin:enterprise scope.

**Fields:**

- **admins** (`EnterpriseAdministratorConnection!`): A list of all of the administrators for this enterprise.
- **affiliatedUsersWithTwoFactorDisabled** (`UserConnection!`): A list of users in the enterprise who currently have two-factor authentication disabled.
- **affiliatedUsersWithTwoFactorDisabledExist** (`Boolean!`): Whether or not affiliated users with two-factor authentication disabled exist in the enterprise.
- **allowPrivateRepositoryForkingSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether private repository forking is enabled for repositories in organizations in this enterprise.
- **allowPrivateRepositoryForkingSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided private repository forking setting value.
- **allowPrivateRepositoryForkingSettingPolicyValue** (`EnterpriseAllowPrivateRepositoryForkingPolicyValue`): The value for the allow private repository forking policy on the enterprise.
- **defaultRepositoryPermissionSetting** (`EnterpriseDefaultRepositoryPermissionSettingValue!`): The setting value for base repository permissions for organizations in this enterprise.
- **defaultRepositoryPermissionSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided base repository permission.
- **domains** (`VerifiableDomainConnection!`): A list of domains owned by the enterprise. Visible to enterprise owners or
enterprise owners' personal access tokens (classic) with admin:enterprise scope.
- **enterpriseServerInstallations** (`EnterpriseServerInstallationConnection!`): Enterprise Server installations owned by the enterprise.
- **failedInvitations** (`EnterpriseFailedInvitationConnection!`): A list of failed invitations in the enterprise.
- **ipAllowListEnabledSetting** (`IpAllowListEnabledSettingValue!`): The setting value for whether the enterprise has an IP allow list enabled.
- **ipAllowListEntries** (`IpAllowListEntryConnection!`): The IP addresses that are allowed to access resources owned by the enterprise.
Visible to enterprise owners or enterprise owners' personal access tokens
(classic) with admin:enterprise scope.
- **ipAllowListForInstalledAppsEnabledSetting** (`IpAllowListForInstalledAppsEnabledSettingValue!`): The setting value for whether the enterprise has IP allow list configuration for installed GitHub Apps enabled.
- **ipAllowListUserLevelEnforcementEnabledSetting** (`IpAllowListUserLevelEnforcementEnabledSettingValue!`): The setting value for whether the enterprise has IP allow list user-level enforcement enabled.
- **isUpdatingDefaultRepositoryPermission** (`Boolean!`): Whether or not the base repository permission is currently being updated.
- **isUpdatingTwoFactorRequirement** (`Boolean!`): Whether the two-factor authentication requirement is currently being enforced.
- **membersCanChangeRepositoryVisibilitySetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether organization members with admin permissions on a
repository can change repository visibility.
- **membersCanChangeRepositoryVisibilitySettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided can change repository visibility setting value.
- **membersCanCreateInternalRepositoriesSetting** (`Boolean`): The setting value for whether members of organizations in the enterprise can create internal repositories.
- **membersCanCreatePrivateRepositoriesSetting** (`Boolean`): The setting value for whether members of organizations in the enterprise can create private repositories.
- **membersCanCreatePublicRepositoriesSetting** (`Boolean`): The setting value for whether members of organizations in the enterprise can create public repositories.
- **membersCanCreateRepositoriesSetting** (`EnterpriseMembersCanCreateRepositoriesSettingValue`): The setting value for whether members of organizations in the enterprise can create repositories.
- **membersCanCreateRepositoriesSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided repository creation setting value.
- **membersCanDeleteIssuesSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether members with admin permissions for repositories can delete issues.
- **membersCanDeleteIssuesSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided members can delete issues setting value.
- **membersCanDeleteRepositoriesSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether members with admin permissions for repositories can delete or transfer repositories.
- **membersCanDeleteRepositoriesSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided members can delete repositories setting value.
- **membersCanInviteCollaboratorsSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether members of organizations in the enterprise can invite outside collaborators.
- **membersCanInviteCollaboratorsSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided members can invite collaborators setting value.
- **membersCanMakePurchasesSetting** (`EnterpriseMembersCanMakePurchasesSettingValue!`): Indicates whether members of this enterprise's organizations can purchase additional services for those organizations.
- **membersCanUpdateProtectedBranchesSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether members with admin permissions for repositories can update protected branches.
- **membersCanUpdateProtectedBranchesSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided members can update protected branches setting value.
- **membersCanViewDependencyInsightsSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether members can view dependency insights.
- **membersCanViewDependencyInsightsSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided members can view dependency insights setting value.
- **notificationDeliveryRestrictionEnabledSetting** (`NotificationRestrictionSettingValue!`): Indicates if email notification delivery for this enterprise is restricted to verified or approved domains.
- **oidcProvider** (`OIDCProvider`): The OIDC Identity Provider for the enterprise.
- **organizationProjectsSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether organization projects are enabled for organizations in this enterprise.
- **organizationProjectsSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided organization projects setting value.
- **outsideCollaborators** (`EnterpriseOutsideCollaboratorConnection!`): A list of outside collaborators across the repositories in the enterprise.
- **pendingAdminInvitations** (`EnterpriseAdministratorInvitationConnection!`): A list of pending administrator invitations for the enterprise.
- **pendingCollaboratorInvitations** (`RepositoryInvitationConnection!`): A list of pending collaborator invitations across the repositories in the enterprise.
- **pendingMemberInvitations** (`EnterprisePendingMemberInvitationConnection!`): A list of pending member invitations for organizations in the enterprise.
- **pendingUnaffiliatedMemberInvitations** (`EnterpriseMemberInvitationConnection!`): A list of pending unaffiliated member invitations for the enterprise.
- **repositoryDeployKeySetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether deploy keys are enabled for repositories in organizations in this enterprise.
- **repositoryDeployKeySettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided deploy keys setting value.
- **repositoryProjectsSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether repository projects are enabled in this enterprise.
- **repositoryProjectsSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the provided repository projects setting value.
- **samlIdentityProvider** (`EnterpriseIdentityProvider`): The SAML Identity Provider for the enterprise.
- **samlIdentityProviderSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the SAML single sign-on setting value.
- **supportEntitlements** (`EnterpriseMemberConnection!`): A list of members with a support entitlement.
- **teamDiscussionsSetting** (`EnterpriseEnabledDisabledSettingValue!`): The setting value for whether team discussions are enabled for organizations in this enterprise.
- **twoFactorDisallowedMethodsSetting** (`EnterpriseDisallowedMethodsSettingValue!`): The setting value for what methods of two-factor authentication the enterprise prevents its users from having.
- **twoFactorRequiredSetting** (`EnterpriseEnabledSettingValue!`): The setting value for whether the enterprise requires two-factor authentication for its organizations and users.
- **twoFactorRequiredSettingOrganizations** (`OrganizationConnection!`): A list of enterprise organizations configured with the two-factor authentication setting value.

### EnterpriseServerInstallation

An Enterprise Server installation.

**Implements:** Node

**Fields:**

- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **customerName** (`String!`): The customer name to which the Enterprise Server installation belongs.
- **hostName** (`String!`): The host name of the Enterprise Server installation.
- **id** (`ID!`): The Node ID of the EnterpriseServerInstallation object.
- **isConnected** (`Boolean!`): Whether or not the installation is connected to an Enterprise Server installation via GitHub Connect.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **userAccounts** (`EnterpriseServerUserAccountConnection!`): User accounts on this Enterprise Server installation.
- **userAccountsUploads** (`EnterpriseServerUserAccountsUploadConnection!`): User accounts uploads for the Enterprise Server installation.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **EnterpriseAdministratorConnection** (4 fields): The connection type for User.
- **EnterpriseAdministratorEdge** (3 fields): A User who is an administrator of an enterprise.
- **EnterpriseAdministratorInvitationConnection** (4 fields): The connection type for EnterpriseAdministratorInvitation.
- **EnterpriseAdministratorInvitationEdge** (2 fields): An edge in a connection.
- **EnterpriseConnection** (4 fields): The connection type for Enterprise.
- **EnterpriseEdge** (2 fields): An edge in a connection.
- **EnterpriseFailedInvitationConnection** (5 fields): The connection type for OrganizationInvitation.
- **EnterpriseFailedInvitationEdge** (2 fields): A failed invitation to be a member in an enterprise organization.
- **EnterpriseMemberConnection** (4 fields): The connection type for EnterpriseMember.
- **EnterpriseMemberEdge** (2 fields): A User who is a member of an enterprise through one or more organizations.
- **EnterpriseMemberInvitationConnection** (4 fields): The connection type for EnterpriseMemberInvitation.
- **EnterpriseMemberInvitationEdge** (2 fields): An edge in a connection.
- **EnterpriseOutsideCollaboratorConnection** (4 fields): The connection type for User.
- **EnterpriseOutsideCollaboratorEdge** (3 fields): A User who is an outside collaborator of an enterprise through one or more organizations.
- **EnterprisePendingMemberInvitationConnection** (5 fields): The connection type for OrganizationInvitation.
- **EnterprisePendingMemberInvitationEdge** (2 fields): An invitation to be a member in an enterprise organization.
- **EnterpriseServerInstallationConnection** (4 fields): The connection type for EnterpriseServerInstallation.
- **EnterpriseServerInstallationEdge** (2 fields): An edge in a connection.
- **EnterpriseServerInstallationMembershipConnection** (4 fields): The connection type for EnterpriseServerInstallation.
- **EnterpriseServerInstallationMembershipEdge** (3 fields): An Enterprise Server installation that a user is a member of.

## Enums

### EnterpriseAdministratorInvitationOrderField

Properties by which enterprise administrator invitation connections can be ordered.

**Values:**

- `CREATED_AT`: Order enterprise administrator member invitations by creation time.

### EnterpriseAdministratorRole

The possible administrator roles in an enterprise account.

**Values:**

- `BILLING_MANAGER`: Represents a billing manager of the enterprise account.
- `OWNER`: Represents an owner of the enterprise account.
- `UNAFFILIATED`: Unaffiliated member of the enterprise account without an admin role.

### EnterpriseDisallowedMethodsSettingValue

The possible values for an enabled/no policy enterprise setting.

**Values:**

- `INSECURE`: The setting prevents insecure 2FA methods from being used by members of the enterprise.
- `NO_POLICY`: There is no policy set for preventing insecure 2FA methods from being used by members of the enterprise.

### EnterpriseEnabledDisabledSettingValue

The possible values for an enabled/disabled enterprise setting.

**Values:**

- `DISABLED`: The setting is disabled for organizations in the enterprise.
- `ENABLED`: The setting is enabled for organizations in the enterprise.
- `NO_POLICY`: There is no policy set for organizations in the enterprise.

### EnterpriseEnabledSettingValue

The possible values for an enabled/no policy enterprise setting.

**Values:**

- `ENABLED`: The setting is enabled for organizations in the enterprise.
- `NO_POLICY`: There is no policy set for organizations in the enterprise.

### EnterpriseMemberInvitationOrderField

Properties by which enterprise member invitation connections can be ordered.

**Values:**

- `CREATED_AT`: Order enterprise member invitations by creation time.

### EnterpriseMemberOrderField

Properties by which enterprise member connections can be ordered.

**Values:**

- `CREATED_AT`: Order enterprise members by creation time.
- `LOGIN`: Order enterprise members by login.

### EnterpriseMembersCanMakePurchasesSettingValue

The possible values for the members can make purchases setting.

**Values:**

- `DISABLED`: The setting is disabled for organizations in the enterprise.
- `ENABLED`: The setting is enabled for organizations in the enterprise.

### EnterpriseMembershipType

The possible values we have for filtering Platform::Objects::User#enterprises.

**Values:**

- `ADMIN`: Returns all enterprises in which the user is an admin.
- `ALL`: Returns all enterprises in which the user is a member, admin, or billing manager.
- `BILLING_MANAGER`: Returns all enterprises in which the user is a billing manager.
- `ORG_MEMBERSHIP`: Returns all enterprises in which the user is a member of an org that is owned by the enterprise.

### EnterpriseOrderField

Properties by which enterprise connections can be ordered.

**Values:**

- `NAME`: Order enterprises by name.

### EnterpriseServerInstallationOrderField

Properties by which Enterprise Server installation connections can be ordered.

**Values:**

- `CREATED_AT`: Order Enterprise Server installations by creation time.
- `CUSTOMER_NAME`: Order Enterprise Server installations by customer name.
- `HOST_NAME`: Order Enterprise Server installations by host name.

### OrgEnterpriseOwnerOrderField

Properties by which enterprise owners can be ordered.

**Values:**

- `LOGIN`: Order enterprise owners by login.

## Input Objects

### AcceptEnterpriseAdministratorInvitationInput

Autogenerated input type of AcceptEnterpriseAdministratorInvitation.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitationId** (`ID!`): The id of the invitation being accepted.

### AcceptEnterpriseMemberInvitationInput

Autogenerated input type of AcceptEnterpriseMemberInvitation.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitationId** (`ID!`): The id of the invitation being accepted.

### AddEnterpriseSupportEntitlementInput

Autogenerated input type of AddEnterpriseSupportEntitlement.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the Enterprise which the admin belongs to.
- **login** (`String!`): The login of a member who will receive the support entitlement.

### CancelEnterpriseAdminInvitationInput

Autogenerated input type of CancelEnterpriseAdminInvitation.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitationId** (`ID!`): The Node ID of the pending enterprise administrator invitation.

### CancelEnterpriseMemberInvitationInput

Autogenerated input type of CancelEnterpriseMemberInvitation.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **invitationId** (`ID!`): The Node ID of the pending enterprise member invitation.

### EnterpriseAdministratorInvitationOrder

Ordering options for enterprise administrator invitation connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`EnterpriseAdministratorInvitationOrderField!`): The field to order enterprise administrator invitations by.

### EnterpriseMemberInvitationOrder

Ordering options for enterprise administrator invitation connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`EnterpriseMemberInvitationOrderField!`): The field to order enterprise member invitations by.

### EnterpriseMemberOrder

Ordering options for enterprise member connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`EnterpriseMemberOrderField!`): The field to order enterprise members by.

### EnterpriseOrder

Ordering options for enterprises.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`EnterpriseOrderField!`): The field to order enterprises by.

### EnterpriseServerInstallationOrder

Ordering options for Enterprise Server installation connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`EnterpriseServerInstallationOrderField!`): The field to order Enterprise Server installations by.

### InviteEnterpriseAdminInput

Autogenerated input type of InviteEnterpriseAdmin.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **email** (`String`): The email of the person to invite as an administrator.
- **enterpriseId** (`ID!`): The ID of the enterprise to which you want to invite an administrator.
- **invitee** (`String`): The login of a user to invite as an administrator.
- **role** (`EnterpriseAdministratorRole`): The role of the administrator.

### InviteEnterpriseMemberInput

Autogenerated input type of InviteEnterpriseMember.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **email** (`String`): The email of the person to invite as an unaffiliated member.
- **enterpriseId** (`ID!`): The ID of the enterprise to which you want to invite an unaffiliated member.
- **invitee** (`String`): The login of a user to invite as an unaffiliated member.

### OrgEnterpriseOwnerOrder

Ordering options for an organization's enterprise owner connections.

**Input fields:**

- **direction** (`OrderDirection!`): The ordering direction.
- **field** (`OrgEnterpriseOwnerOrderField!`): The field to order enterprise owners by.

### RegenerateEnterpriseIdentityProviderRecoveryCodesInput

Autogenerated input type of RegenerateEnterpriseIdentityProviderRecoveryCodes.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set an identity provider.

### RemoveEnterpriseAdminInput

Autogenerated input type of RemoveEnterpriseAdmin.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The Enterprise ID from which to remove the administrator.
- **login** (`String!`): The login of the user to remove as an administrator.

### RemoveEnterpriseIdentityProviderInput

Autogenerated input type of RemoveEnterpriseIdentityProvider.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise from which to remove the identity provider.

### RemoveEnterpriseMemberInput

Autogenerated input type of RemoveEnterpriseMember.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise from which the user should be removed.
- **userId** (`ID!`): The ID of the user to remove from the enterprise.

### RemoveEnterpriseSupportEntitlementInput

Autogenerated input type of RemoveEnterpriseSupportEntitlement.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the Enterprise which the admin belongs to.
- **login** (`String!`): The login of a member who will lose the support entitlement.

### SetEnterpriseIdentityProviderInput

Autogenerated input type of SetEnterpriseIdentityProvider.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **digestMethod** (`SamlDigestAlgorithm!`): The digest algorithm used to sign SAML requests for the identity provider.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set an identity provider.
- **idpCertificate** (`String!`): The x509 certificate used by the identity provider to sign assertions and responses.
- **issuer** (`String`): The Issuer Entity ID for the SAML identity provider.
- **signatureMethod** (`SamlSignatureAlgorithm!`): The signature algorithm used to sign SAML requests for the identity provider.
- **ssoUrl** (`URI!`): The URL endpoint for the identity provider's SAML SSO.

### UpdateEnterpriseAdministratorRoleInput

Autogenerated input type of UpdateEnterpriseAdministratorRole.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the Enterprise which the admin belongs to.
- **login** (`String!`): The login of a administrator whose role is being changed.
- **role** (`EnterpriseAdministratorRole!`): The new role for the Enterprise administrator.

### UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput

Autogenerated input type of UpdateEnterpriseMembersCanInviteCollaboratorsSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the members can invite collaborators setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the members can invite collaborators setting on the enterprise.

### UpdateEnterpriseMembersCanMakePurchasesSettingInput

Autogenerated input type of UpdateEnterpriseMembersCanMakePurchasesSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the members can make purchases setting.
- **settingValue** (`EnterpriseMembersCanMakePurchasesSettingValue!`): The value for the members can make purchases setting on the enterprise.

### UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput

Autogenerated input type of UpdateEnterpriseMembersCanUpdateProtectedBranchesSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the members can update protected branches setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the members can update protected branches setting on the enterprise.

### UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput

Autogenerated input type of UpdateEnterpriseMembersCanViewDependencyInsightsSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the members can view dependency insights setting.
- **settingValue** (`EnterpriseEnabledDisabledSettingValue!`): The value for the members can view dependency insights setting on the enterprise.

### UpdateEnterpriseProfileInput

Autogenerated input type of UpdateEnterpriseProfile.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **description** (`String`): The description of the enterprise.
- **enterpriseId** (`ID!`): The Enterprise ID to update.
- **location** (`String`): The location of the enterprise.
- **name** (`String`): The name of the enterprise.
- **securityContactEmail** (`String`): The security contact email address of the enterprise.
- **websiteUrl** (`String`): The URL of the enterprise's website.

### UpdateEnterpriseTwoFactorAuthenticationDisallowedMethodsSettingInput

Autogenerated input type of UpdateEnterpriseTwoFactorAuthenticationDisallowedMethodsSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the two-factor authentication disallowed methods setting.
- **settingValue** (`EnterpriseDisallowedMethodsSettingValue!`): The value for the two-factor authentication disallowed methods setting on the enterprise.

### UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput

Autogenerated input type of UpdateEnterpriseTwoFactorAuthenticationRequiredSetting.

**Input fields:**

- **clientMutationId** (`String`): A unique identifier for the client performing the mutation.
- **enterpriseId** (`ID!`): The ID of the enterprise on which to set the two factor authentication required setting.
- **settingValue** (`EnterpriseEnabledSettingValue!`): The value for the two factor authentication required setting on the enterprise.

## Unions

### EnterpriseMember

An object that is a member of an enterprise.

**Possible types:** EnterpriseUserAccount, User
