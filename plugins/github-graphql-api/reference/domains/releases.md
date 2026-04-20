# Releases & Release Assets

## Types

### Release

A release contains the content for a release.

**Implements:** Node, Reactable, UniformResourceLocatable

**Fields:**

- **author** (`User`): The author of the release.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **databaseId** (`Int`): Identifies the primary key from the database.
- **description** (`String`): The description of the release.
- **descriptionHTML** (`HTML`): The description of this release rendered to HTML.
- **id** (`ID!`): The Node ID of the Release object.
- **immutable** (`Boolean!`): Whether or not the release is immutable.
- **isDraft** (`Boolean!`): Whether or not the release is a draft.
- **isLatest** (`Boolean!`): Whether or not the release is the latest releast.
- **isPrerelease** (`Boolean!`): Whether or not the release is a prerelease.
- **mentions** (`UserConnection`): A list of users mentioned in the release description.
- **name** (`String`): The title of the release.
- **publishedAt** (`DateTime`): Identifies the date and time when the release was created.
- **reactionGroups** (`[ReactionGroup!]`): A list of reactions grouped by content left on the subject.
- **reactions** (`ReactionConnection!`): A list of Reactions left on the Issue.
- **releaseAssets** (`ReleaseAssetConnection!`): List of releases assets which are dependent on this release.
- **repository** (`Repository!`): The repository that the release belongs to.
- **resourcePath** (`URI!`): The HTTP path for this issue.
- **shortDescriptionHTML** (`HTML`): A description of the release, rendered to HTML without any links in it.
- **tag** (`Ref`): The Git tag the release points to.
- **tagCommit** (`Commit`): The tag commit for this release.
- **tagName** (`String!`): The name of the release's Git tag.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **url** (`URI!`): The HTTP URL for this issue.
- **viewerCanReact** (`Boolean!`): Can user react to this subject.

### ReleaseAsset

A release asset contains the content for a release asset.

**Implements:** Node

**Fields:**

- **contentType** (`String!`): The asset's content-type.
- **createdAt** (`DateTime!`): Identifies the date and time when the object was created.
- **digest** (`String`): The SHA256 digest of the asset.
- **downloadCount** (`Int!`): The number of times this asset was downloaded.
- **downloadUrl** (`URI!`): Identifies the URL where you can download the release asset via the browser.
- **id** (`ID!`): The Node ID of the ReleaseAsset object.
- **name** (`String!`): Identifies the title of the release asset.
- **release** (`Release`): Release that the asset is associated with.
- **size** (`Int!`): The size (in bytes) of the asset.
- **updatedAt** (`DateTime!`): Identifies the date and time when the object was last updated.
- **uploadedBy** (`User!`): The user that performed the upload.
- **url** (`URI!`): Identifies the URL of the release asset.

## Connection & Edge Types

_These follow the standard Relay connection pattern (see the guide for pagination details)._

- **ReleaseAssetConnection** (4 fields): The connection type for ReleaseAsset.
- **ReleaseAssetEdge** (2 fields): An edge in a connection.
- **ReleaseConnection** (4 fields): The connection type for Release.
- **ReleaseEdge** (2 fields): An edge in a connection.

## Enums

### ReleaseOrderField

Properties by which release connections can be ordered.

**Values:**

- `CREATED_AT`: Order releases by creation time.
- `NAME`: Order releases alphabetically by name.

## Input Objects

### ReleaseOrder

Ways in which lists of releases can be ordered upon return.

**Input fields:**

- **direction** (`OrderDirection!`): The direction in which to order releases by the specified field.
- **field** (`ReleaseOrderField!`): The field in which to order releases by.
