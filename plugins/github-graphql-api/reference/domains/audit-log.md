# Audit Log Events

## Types

### MembersCanDeleteReposClearAuditEntry

Audit log entry for a members_can_delete_repos.clear event.

**Implements:** AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.
- **id** (`ID!`): The Node ID of the MembersCanDeleteReposClearAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### MembersCanDeleteReposDisableAuditEntry

Audit log entry for a members_can_delete_repos.disable event.

**Implements:** AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.
- **id** (`ID!`): The Node ID of the MembersCanDeleteReposDisableAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### MembersCanDeleteReposEnableAuditEntry

Audit log entry for a members_can_delete_repos.enable event.

**Implements:** AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.
- **id** (`ID!`): The Node ID of the MembersCanDeleteReposEnableAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OauthApplicationCreateAuditEntry

Audit log entry for a oauth_application.create event.

**Implements:** AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **applicationUrl** (`URI`): The application URL of the OAuth application.
- **callbackUrl** (`URI`): The callback URL of the OAuth application.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OauthApplicationCreateAuditEntry object.
- **oauthApplicationName** (`String`): The name of the OAuth application.
- **oauthApplicationResourcePath** (`URI`): The HTTP path for the OAuth application.
- **oauthApplicationUrl** (`URI`): The HTTP URL for the OAuth application.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **rateLimit** (`Int`): The rate limit of the OAuth application.
- **state** (`OauthApplicationCreateAuditEntryState`): The state of the OAuth application.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgAddBillingManagerAuditEntry

Audit log entry for a org.add_billing_manager.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgAddBillingManagerAuditEntry object.
- **invitationEmail** (`String`): The email address used to invite a billing manager for the organization.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgAddMemberAuditEntry

Audit log entry for a org.add_member.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgAddMemberAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **permission** (`OrgAddMemberAuditEntryPermission`): The permission level of the member added to the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgBlockUserAuditEntry

Audit log entry for a org.block_user.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **blockedUser** (`User`): The blocked user.
- **blockedUserName** (`String`): The username of the blocked user.
- **blockedUserResourcePath** (`URI`): The HTTP path for the blocked user.
- **blockedUserUrl** (`URI`): The HTTP URL for the blocked user.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgBlockUserAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgConfigDisableCollaboratorsOnlyAuditEntry

Audit log entry for a org.config.disable_collaborators_only event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgConfigDisableCollaboratorsOnlyAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgConfigEnableCollaboratorsOnlyAuditEntry

Audit log entry for a org.config.enable_collaborators_only event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgConfigEnableCollaboratorsOnlyAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgCreateAuditEntry

Audit log entry for a org.create event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **billingPlan** (`OrgCreateAuditEntryBillingPlan`): The billing plan for the Organization.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgCreateAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgDisableOauthAppRestrictionsAuditEntry

Audit log entry for a org.disable_oauth_app_restrictions event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgDisableOauthAppRestrictionsAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgDisableSamlAuditEntry

Audit log entry for a org.disable_saml event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **digestMethodUrl** (`URI`): The SAML provider's digest algorithm URL.
- **id** (`ID!`): The Node ID of the OrgDisableSamlAuditEntry object.
- **issuerUrl** (`URI`): The SAML provider's issuer URL.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **signatureMethodUrl** (`URI`): The SAML provider's signature algorithm URL.
- **singleSignOnUrl** (`URI`): The SAML provider's single sign-on URL.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgDisableTwoFactorRequirementAuditEntry

Audit log entry for a org.disable_two_factor_requirement event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgDisableTwoFactorRequirementAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgEnableOauthAppRestrictionsAuditEntry

Audit log entry for a org.enable_oauth_app_restrictions event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgEnableOauthAppRestrictionsAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgEnableSamlAuditEntry

Audit log entry for a org.enable_saml event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **digestMethodUrl** (`URI`): The SAML provider's digest algorithm URL.
- **id** (`ID!`): The Node ID of the OrgEnableSamlAuditEntry object.
- **issuerUrl** (`URI`): The SAML provider's issuer URL.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **signatureMethodUrl** (`URI`): The SAML provider's signature algorithm URL.
- **singleSignOnUrl** (`URI`): The SAML provider's single sign-on URL.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgEnableTwoFactorRequirementAuditEntry

Audit log entry for a org.enable_two_factor_requirement event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgEnableTwoFactorRequirementAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgInviteMemberAuditEntry

Audit log entry for a org.invite_member event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **email** (`String`): The email address of the organization invitation.
- **id** (`ID!`): The Node ID of the OrgInviteMemberAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationInvitation** (`OrganizationInvitation`): The organization invitation.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgInviteToBusinessAuditEntry

Audit log entry for a org.invite_to_business event.

**Implements:** AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.
- **id** (`ID!`): The Node ID of the OrgInviteToBusinessAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgOauthAppAccessApprovedAuditEntry

Audit log entry for a org.oauth_app_access_approved event.

**Implements:** AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgOauthAppAccessApprovedAuditEntry object.
- **oauthApplicationName** (`String`): The name of the OAuth application.
- **oauthApplicationResourcePath** (`URI`): The HTTP path for the OAuth application.
- **oauthApplicationUrl** (`URI`): The HTTP URL for the OAuth application.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgOauthAppAccessBlockedAuditEntry

Audit log entry for a org.oauth_app_access_blocked event.

**Implements:** AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgOauthAppAccessBlockedAuditEntry object.
- **oauthApplicationName** (`String`): The name of the OAuth application.
- **oauthApplicationResourcePath** (`URI`): The HTTP path for the OAuth application.
- **oauthApplicationUrl** (`URI`): The HTTP URL for the OAuth application.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgOauthAppAccessDeniedAuditEntry

Audit log entry for a org.oauth_app_access_denied event.

**Implements:** AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgOauthAppAccessDeniedAuditEntry object.
- **oauthApplicationName** (`String`): The name of the OAuth application.
- **oauthApplicationResourcePath** (`URI`): The HTTP path for the OAuth application.
- **oauthApplicationUrl** (`URI`): The HTTP URL for the OAuth application.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgOauthAppAccessRequestedAuditEntry

Audit log entry for a org.oauth_app_access_requested event.

**Implements:** AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgOauthAppAccessRequestedAuditEntry object.
- **oauthApplicationName** (`String`): The name of the OAuth application.
- **oauthApplicationResourcePath** (`URI`): The HTTP path for the OAuth application.
- **oauthApplicationUrl** (`URI`): The HTTP URL for the OAuth application.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgOauthAppAccessUnblockedAuditEntry

Audit log entry for a org.oauth_app_access_unblocked event.

**Implements:** AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgOauthAppAccessUnblockedAuditEntry object.
- **oauthApplicationName** (`String`): The name of the OAuth application.
- **oauthApplicationResourcePath** (`URI`): The HTTP path for the OAuth application.
- **oauthApplicationUrl** (`URI`): The HTTP URL for the OAuth application.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgRemoveBillingManagerAuditEntry

Audit log entry for a org.remove_billing_manager event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgRemoveBillingManagerAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **reason** (`OrgRemoveBillingManagerAuditEntryReason`): The reason for the billing manager being removed.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgRemoveMemberAuditEntry

Audit log entry for a org.remove_member event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgRemoveMemberAuditEntry object.
- **membershipTypes** (`[OrgRemoveMemberAuditEntryMembershipType!]`): The types of membership the member has with the organization.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **reason** (`OrgRemoveMemberAuditEntryReason`): The reason for the member being removed.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgRemoveOutsideCollaboratorAuditEntry

Audit log entry for a org.remove_outside_collaborator event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgRemoveOutsideCollaboratorAuditEntry object.
- **membershipTypes** (`[OrgRemoveOutsideCollaboratorAuditEntryMembershipType!]`): The types of membership the outside collaborator has with the organization.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **reason** (`OrgRemoveOutsideCollaboratorAuditEntryReason`): The reason for the outside collaborator being removed from the Organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgRestoreMemberAuditEntry

Audit log entry for a org.restore_member event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgRestoreMemberAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **restoredCustomEmailRoutingsCount** (`Int`): The number of custom email routings for the restored member.
- **restoredIssueAssignmentsCount** (`Int`): The number of issue assignments for the restored member.
- **restoredMemberships** (`[OrgRestoreMemberAuditEntryMembership!]`): Restored organization membership objects.
- **restoredMembershipsCount** (`Int`): The number of restored memberships.
- **restoredRepositoriesCount** (`Int`): The number of repositories of the restored member.
- **restoredRepositoryStarsCount** (`Int`): The number of starred repositories for the restored member.
- **restoredRepositoryWatchesCount** (`Int`): The number of watched repositories for the restored member.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgRestoreMemberMembershipOrganizationAuditEntryData

Metadata for an organization membership for org.restore_member actions.

**Implements:** OrganizationAuditEntryData

**Fields:**

- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.

### OrgRestoreMemberMembershipRepositoryAuditEntryData

Metadata for a repository membership for org.restore_member actions.

**Implements:** RepositoryAuditEntryData

**Fields:**

- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.

### OrgRestoreMemberMembershipTeamAuditEntryData

Metadata for a team membership for org.restore_member actions.

**Implements:** TeamAuditEntryData

**Fields:**

- **team** (`Team`): The team associated with the action.
- **teamName** (`String`): The name of the team.
- **teamResourcePath** (`URI`): The HTTP path for this team.
- **teamUrl** (`URI`): The HTTP URL for this team.

### OrgUnblockUserAuditEntry

Audit log entry for a org.unblock_user.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **blockedUser** (`User`): The user being unblocked by the organization.
- **blockedUserName** (`String`): The username of the blocked user.
- **blockedUserResourcePath** (`URI`): The HTTP path for the blocked user.
- **blockedUserUrl** (`URI`): The HTTP URL for the blocked user.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgUnblockUserAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgUpdateDefaultRepositoryPermissionAuditEntry

Audit log entry for a org.update_default_repository_permission.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgUpdateDefaultRepositoryPermissionAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **permission** (`OrgUpdateDefaultRepositoryPermissionAuditEntryPermission`): The new base repository permission level for the organization.
- **permissionWas** (`OrgUpdateDefaultRepositoryPermissionAuditEntryPermission`): The former base repository permission level for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgUpdateMemberAuditEntry

Audit log entry for a org.update_member event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgUpdateMemberAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **permission** (`OrgUpdateMemberAuditEntryPermission`): The new member permission level for the organization.
- **permissionWas** (`OrgUpdateMemberAuditEntryPermission`): The former member permission level for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### OrgUpdateMemberRepositoryCreationPermissionAuditEntry

Audit log entry for a org.update_member_repository_creation_permission event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **canCreateRepositories** (`Boolean`): Can members create repositories in the organization.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgUpdateMemberRepositoryCreationPermissionAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.
- **visibility** (`OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility`): The permission for visibility level of repositories for this organization.

### OrgUpdateMemberRepositoryInvitationPermissionAuditEntry

Audit log entry for a org.update_member_repository_invitation_permission event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **canInviteOutsideCollaboratorsToRepositories** (`Boolean`): Can outside collaborators be invited to repositories in the organization.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the OrgUpdateMemberRepositoryInvitationPermissionAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### PrivateRepositoryForkingDisableAuditEntry

Audit log entry for a private_repository_forking.disable event.

**Implements:** AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.
- **id** (`ID!`): The Node ID of the PrivateRepositoryForkingDisableAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### PrivateRepositoryForkingEnableAuditEntry

Audit log entry for a private_repository_forking.enable event.

**Implements:** AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.
- **id** (`ID!`): The Node ID of the PrivateRepositoryForkingEnableAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoAccessAuditEntry

Audit log entry for a repo.access event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoAccessAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.
- **visibility** (`RepoAccessAuditEntryVisibility`): The visibility of the repository.

### RepoAddMemberAuditEntry

Audit log entry for a repo.add_member event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoAddMemberAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.
- **visibility** (`RepoAddMemberAuditEntryVisibility`): The visibility of the repository.

### RepoAddTopicAuditEntry

Audit log entry for a repo.add_topic event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData, TopicAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoAddTopicAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **topic** (`Topic`): The name of the topic added to the repository.
- **topicName** (`String`): The name of the topic added to the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoArchivedAuditEntry

Audit log entry for a repo.archived event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoArchivedAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.
- **visibility** (`RepoArchivedAuditEntryVisibility`): The visibility of the repository.

### RepoChangeMergeSettingAuditEntry

Audit log entry for a repo.change_merge_setting event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoChangeMergeSettingAuditEntry object.
- **isEnabled** (`Boolean`): Whether the change was to enable (true) or disable (false) the merge type.
- **mergeType** (`RepoChangeMergeSettingAuditEntryMergeType`): The merge method affected by the change.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigDisableAnonymousGitAccessAuditEntry

Audit log entry for a repo.config.disable_anonymous_git_access event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigDisableAnonymousGitAccessAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigDisableCollaboratorsOnlyAuditEntry

Audit log entry for a repo.config.disable_collaborators_only event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigDisableCollaboratorsOnlyAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigDisableContributorsOnlyAuditEntry

Audit log entry for a repo.config.disable_contributors_only event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigDisableContributorsOnlyAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigDisableSockpuppetDisallowedAuditEntry

Audit log entry for a repo.config.disable_sockpuppet_disallowed event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigDisableSockpuppetDisallowedAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigEnableAnonymousGitAccessAuditEntry

Audit log entry for a repo.config.enable_anonymous_git_access event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigEnableAnonymousGitAccessAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigEnableCollaboratorsOnlyAuditEntry

Audit log entry for a repo.config.enable_collaborators_only event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigEnableCollaboratorsOnlyAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigEnableContributorsOnlyAuditEntry

Audit log entry for a repo.config.enable_contributors_only event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigEnableContributorsOnlyAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigEnableSockpuppetDisallowedAuditEntry

Audit log entry for a repo.config.enable_sockpuppet_disallowed event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigEnableSockpuppetDisallowedAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigLockAnonymousGitAccessAuditEntry

Audit log entry for a repo.config.lock_anonymous_git_access event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigLockAnonymousGitAccessAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoConfigUnlockAnonymousGitAccessAuditEntry

Audit log entry for a repo.config.unlock_anonymous_git_access event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoConfigUnlockAnonymousGitAccessAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepoCreateAuditEntry

Audit log entry for a repo.create event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **forkParentName** (`String`): The name of the parent repository for this forked repository.
- **forkSourceName** (`String`): The name of the root repository for this network.
- **id** (`ID!`): The Node ID of the RepoCreateAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.
- **visibility** (`RepoCreateAuditEntryVisibility`): The visibility of the repository.

### RepoDestroyAuditEntry

Audit log entry for a repo.destroy event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoDestroyAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.
- **visibility** (`RepoDestroyAuditEntryVisibility`): The visibility of the repository.

### RepoRemoveMemberAuditEntry

Audit log entry for a repo.remove_member event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoRemoveMemberAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.
- **visibility** (`RepoRemoveMemberAuditEntryVisibility`): The visibility of the repository.

### RepoRemoveTopicAuditEntry

Audit log entry for a repo.remove_topic event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData, TopicAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the RepoRemoveTopicAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **topic** (`Topic`): The name of the topic added to the repository.
- **topicName** (`String`): The name of the topic added to the repository.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepositoryVisibilityChangeDisableAuditEntry

Audit log entry for a repository_visibility_change.disable event.

**Implements:** AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.
- **id** (`ID!`): The Node ID of the RepositoryVisibilityChangeDisableAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### RepositoryVisibilityChangeEnableAuditEntry

Audit log entry for a repository_visibility_change.enable event.

**Implements:** AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.
- **id** (`ID!`): The Node ID of the RepositoryVisibilityChangeEnableAuditEntry object.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### TeamAddMemberAuditEntry

Audit log entry for a team.add_member event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, TeamAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the TeamAddMemberAuditEntry object.
- **isLdapMapped** (`Boolean`): Whether the team was mapped to an LDAP Group.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **team** (`Team`): The team associated with the action.
- **teamName** (`String`): The name of the team.
- **teamResourcePath** (`URI`): The HTTP path for this team.
- **teamUrl** (`URI`): The HTTP URL for this team.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### TeamAddRepositoryAuditEntry

Audit log entry for a team.add_repository event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData, TeamAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the TeamAddRepositoryAuditEntry object.
- **isLdapMapped** (`Boolean`): Whether the team was mapped to an LDAP Group.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **team** (`Team`): The team associated with the action.
- **teamName** (`String`): The name of the team.
- **teamResourcePath** (`URI`): The HTTP path for this team.
- **teamUrl** (`URI`): The HTTP URL for this team.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### TeamChangeParentTeamAuditEntry

Audit log entry for a team.change_parent_team event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, TeamAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the TeamChangeParentTeamAuditEntry object.
- **isLdapMapped** (`Boolean`): Whether the team was mapped to an LDAP Group.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **parentTeam** (`Team`): The new parent team.
- **parentTeamName** (`String`): The name of the new parent team.
- **parentTeamNameWas** (`String`): The name of the former parent team.
- **parentTeamResourcePath** (`URI`): The HTTP path for the parent team.
- **parentTeamUrl** (`URI`): The HTTP URL for the parent team.
- **parentTeamWas** (`Team`): The former parent team.
- **parentTeamWasResourcePath** (`URI`): The HTTP path for the previous parent team.
- **parentTeamWasUrl** (`URI`): The HTTP URL for the previous parent team.
- **team** (`Team`): The team associated with the action.
- **teamName** (`String`): The name of the team.
- **teamResourcePath** (`URI`): The HTTP path for this team.
- **teamUrl** (`URI`): The HTTP URL for this team.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### TeamRemoveMemberAuditEntry

Audit log entry for a team.remove_member event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, TeamAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the TeamRemoveMemberAuditEntry object.
- **isLdapMapped** (`Boolean`): Whether the team was mapped to an LDAP Group.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **team** (`Team`): The team associated with the action.
- **teamName** (`String`): The name of the team.
- **teamResourcePath** (`URI`): The HTTP path for this team.
- **teamUrl** (`URI`): The HTTP URL for this team.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### TeamRemoveRepositoryAuditEntry

Audit log entry for a team.remove_repository event.

**Implements:** AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData, TeamAuditEntryData

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **id** (`ID!`): The Node ID of the TeamRemoveRepositoryAuditEntry object.
- **isLdapMapped** (`Boolean`): Whether the team was mapped to an LDAP Group.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **organization** (`Organization`): The Organization associated with the Audit Entry.
- **organizationName** (`String`): The name of the Organization.
- **organizationResourcePath** (`URI`): The HTTP path for the organization.
- **organizationUrl** (`URI`): The HTTP URL for the organization.
- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.
- **team** (`Team`): The team associated with the action.
- **teamName** (`String`): The name of the team.
- **teamResourcePath** (`URI`): The HTTP path for this team.
- **teamUrl** (`URI`): The HTTP URL for this team.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

## Interfaces

### AuditEntry

An entry in the audit log.

**Fields:**

- **action** (`String!`): The action name.
- **actor** (`AuditEntryActor`): The user who initiated the action.
- **actorIp** (`String`): The IP address of the actor.
- **actorLocation** (`ActorLocation`): A readable representation of the actor's location.
- **actorLogin** (`String`): The username of the user who initiated the action.
- **actorResourcePath** (`URI`): The HTTP path for the actor.
- **actorUrl** (`URI`): The HTTP URL for the actor.
- **createdAt** (`PreciseDateTime!`): The time the action was initiated.
- **operationType** (`OperationType`): The corresponding operation type for the action.
- **user** (`User`): The user affected by the action.
- **userLogin** (`String`): For actions involving two users, the actor is the initiator and the user is the affected user.
- **userResourcePath** (`URI`): The HTTP path for the user.
- **userUrl** (`URI`): The HTTP URL for the user.

### EnterpriseAuditEntryData

Metadata for an audit entry containing enterprise account information.

**Fields:**

- **enterpriseResourcePath** (`URI`): The HTTP path for this enterprise.
- **enterpriseSlug** (`String`): The slug of the enterprise.
- **enterpriseUrl** (`URI`): The HTTP URL for this enterprise.

### OauthApplicationAuditEntryData

Metadata for an audit entry with action oauth_application.*.

**Fields:**

- **oauthApplicationName** (`String`): The name of the OAuth application.
- **oauthApplicationResourcePath** (`URI`): The HTTP path for the OAuth application.
- **oauthApplicationUrl** (`URI`): The HTTP URL for the OAuth application.

### RepositoryAuditEntryData

Metadata for an audit entry with action repo.*.

**Fields:**

- **repository** (`Repository`): The repository associated with the action.
- **repositoryName** (`String`): The name of the repository.
- **repositoryResourcePath** (`URI`): The HTTP path for the repository.
- **repositoryUrl** (`URI`): The HTTP URL for the repository.

### TeamAuditEntryData

Metadata for an audit entry with action team.*.

**Fields:**

- **team** (`Team`): The team associated with the action.
- **teamName** (`String`): The name of the team.
- **teamResourcePath** (`URI`): The HTTP path for this team.
- **teamUrl** (`URI`): The HTTP URL for this team.

### TopicAuditEntryData

Metadata for an audit entry with a topic.

**Fields:**

- **topic** (`Topic`): The name of the topic added to the repository.
- **topicName** (`String`): The name of the topic added to the repository.

## Enums

### OauthApplicationCreateAuditEntryState

The state of an OAuth application when it was created.

**Values:**

- `ACTIVE`: The OAuth application was active and allowed to have OAuth Accesses.
- `PENDING_DELETION`: The OAuth application was in the process of being deleted.
- `SUSPENDED`: The OAuth application was suspended from generating OAuth Accesses due to abuse or security concerns.

### OrgAddMemberAuditEntryPermission

The permissions available to members on an Organization.

**Values:**

- `ADMIN`: Can read, clone, push, and add collaborators to repositories.
- `READ`: Can read and clone repositories.

### OrgCreateAuditEntryBillingPlan

The billing plans available for organizations.

**Values:**

- `BUSINESS`: Team Plan.
- `BUSINESS_PLUS`: Enterprise Cloud Plan.
- `FREE`: Free Plan.
- `TIERED_PER_SEAT`: Tiered Per Seat Plan.
- `UNLIMITED`: Legacy Unlimited Plan.

### OrgRemoveBillingManagerAuditEntryReason

The reason a billing manager was removed from an Organization.

**Values:**

- `SAML_EXTERNAL_IDENTITY_MISSING`: SAML external identity missing.
- `SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY`: SAML SSO enforcement requires an external identity.
- `TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE`: The organization required 2FA of its billing managers and this user did not have 2FA enabled.

### OrgRemoveMemberAuditEntryMembershipType

The type of membership a user has with an Organization.

**Values:**

- `ADMIN`: Organization owners have full access and can change several settings,
including the names of repositories that belong to the Organization and Owners
team membership. In addition, organization owners can delete the organization
and all of its repositories.
- `BILLING_MANAGER`: A billing manager is a user who manages the billing settings for the Organization, such as updating payment information.
- `DIRECT_MEMBER`: A direct member is a user that is a member of the Organization.
- `OUTSIDE_COLLABORATOR`: An outside collaborator is a person who isn't explicitly a member of the
Organization, but who has Read, Write, or Admin permissions to one or more
repositories in the organization.
- `SUSPENDED`: A suspended member.
- `UNAFFILIATED`: An unaffiliated collaborator is a person who is not a member of the
Organization and does not have access to any repositories in the Organization.

### OrgRemoveMemberAuditEntryReason

The reason a member was removed from an Organization.

**Values:**

- `SAML_EXTERNAL_IDENTITY_MISSING`: SAML external identity missing.
- `SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY`: SAML SSO enforcement requires an external identity.
- `TWO_FACTOR_ACCOUNT_RECOVERY`: User was removed from organization during account recovery.
- `TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE`: The organization required 2FA of its billing managers and this user did not have 2FA enabled.
- `USER_ACCOUNT_DELETED`: User account has been deleted.

### OrgRemoveOutsideCollaboratorAuditEntryMembershipType

The type of membership a user has with an Organization.

**Values:**

- `BILLING_MANAGER`: A billing manager is a user who manages the billing settings for the Organization, such as updating payment information.
- `OUTSIDE_COLLABORATOR`: An outside collaborator is a person who isn't explicitly a member of the
Organization, but who has Read, Write, or Admin permissions to one or more
repositories in the organization.
- `UNAFFILIATED`: An unaffiliated collaborator is a person who is not a member of the
Organization and does not have access to any repositories in the organization.

### OrgRemoveOutsideCollaboratorAuditEntryReason

The reason an outside collaborator was removed from an Organization.

**Values:**

- `SAML_EXTERNAL_IDENTITY_MISSING`: SAML external identity missing.
- `TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE`: The organization required 2FA of its billing managers and this user did not have 2FA enabled.

### OrgUpdateDefaultRepositoryPermissionAuditEntryPermission

The default permission a repository can have in an Organization.

**Values:**

- `ADMIN`: Can read, clone, push, and add collaborators to repositories.
- `NONE`: No default permission value.
- `READ`: Can read and clone repositories.
- `WRITE`: Can read, clone and push to repositories.

### OrgUpdateMemberAuditEntryPermission

The permissions available to members on an Organization.

**Values:**

- `ADMIN`: Can read, clone, push, and add collaborators to repositories.
- `READ`: Can read and clone repositories.

### OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility

The permissions available for repository creation on an Organization.

**Values:**

- `ALL`: All organization members are restricted from creating any repositories.
- `INTERNAL`: All organization members are restricted from creating internal repositories.
- `NONE`: All organization members are allowed to create any repositories.
- `PRIVATE`: All organization members are restricted from creating private repositories.
- `PRIVATE_INTERNAL`: All organization members are restricted from creating private or internal repositories.
- `PUBLIC`: All organization members are restricted from creating public repositories.
- `PUBLIC_INTERNAL`: All organization members are restricted from creating public or internal repositories.
- `PUBLIC_PRIVATE`: All organization members are restricted from creating public or private repositories.

### RepoAccessAuditEntryVisibility

The privacy of a repository.

**Values:**

- `INTERNAL`: The repository is visible only to users in the same enterprise.
- `PRIVATE`: The repository is visible only to those with explicit access.
- `PUBLIC`: The repository is visible to everyone.

### RepoAddMemberAuditEntryVisibility

The privacy of a repository.

**Values:**

- `INTERNAL`: The repository is visible only to users in the same enterprise.
- `PRIVATE`: The repository is visible only to those with explicit access.
- `PUBLIC`: The repository is visible to everyone.

### RepoArchivedAuditEntryVisibility

The privacy of a repository.

**Values:**

- `INTERNAL`: The repository is visible only to users in the same enterprise.
- `PRIVATE`: The repository is visible only to those with explicit access.
- `PUBLIC`: The repository is visible to everyone.

### RepoChangeMergeSettingAuditEntryMergeType

The merge options available for pull requests to this repository.

**Values:**

- `MERGE`: The pull request is added to the base branch in a merge commit.
- `REBASE`: Commits from the pull request are added onto the base branch individually without a merge commit.
- `SQUASH`: The pull request's commits are squashed into a single commit before they are merged to the base branch.

### RepoCreateAuditEntryVisibility

The privacy of a repository.

**Values:**

- `INTERNAL`: The repository is visible only to users in the same enterprise.
- `PRIVATE`: The repository is visible only to those with explicit access.
- `PUBLIC`: The repository is visible to everyone.

### RepoDestroyAuditEntryVisibility

The privacy of a repository.

**Values:**

- `INTERNAL`: The repository is visible only to users in the same enterprise.
- `PRIVATE`: The repository is visible only to those with explicit access.
- `PUBLIC`: The repository is visible to everyone.

### RepoRemoveMemberAuditEntryVisibility

The privacy of a repository.

**Values:**

- `INTERNAL`: The repository is visible only to users in the same enterprise.
- `PRIVATE`: The repository is visible only to those with explicit access.
- `PUBLIC`: The repository is visible to everyone.

## Unions

### AuditEntryActor

Types that can initiate an audit log event.

**Possible types:** Bot, Organization, User

### OrgRestoreMemberAuditEntryMembership

Types of memberships that can be restored for an Organization member.

**Possible types:** OrgRestoreMemberMembershipOrganizationAuditEntryData, OrgRestoreMemberMembershipRepositoryAuditEntryData, OrgRestoreMemberMembershipTeamAuditEntryData
