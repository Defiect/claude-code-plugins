# GitHub GraphQL API — Usage Guide

This guide covers everything you need to know to work with the GitHub
GraphQL API: authentication, forming queries and mutations, pagination,
rate limits, and more.

**Endpoint:** `https://api.github.com/graphql`
**Method:** Always `POST` (except introspection `GET`)
**Auth:** `Authorization: bearer TOKEN` header


## Overview

Here are some quick links to get you up and running with the GraphQL API:

* [Authentication](/graphql/guides/forming-calls-with-graphql#authenticating-with-graphql)
* [Root endpoint](/graphql/guides/forming-calls-with-graphql#the-graphql-endpoint)
* [Schema introspection](/graphql/guides/introduction-to-graphql#discovering-the-graphql-api)
* [Rate limits](/graphql/overview/resource-limitations)
* [Migrating from REST](/graphql/guides/migrating-from-rest-to-graphql)

For more information about GitHub's APIs, see [About Githubs Apis](/rest/overview/about-githubs-apis).

## About GraphQL

The [GraphQL](https://graphql.org/) data query language is:

* **A [specification](https://spec.graphql.org/June2018/).** The spec determines the validity of the [schema](/graphql/guides/introduction-to-graphql#schema) on the API server. The schema determines the validity of client calls.

* **[Strongly typed](#about-the-graphql-schema-reference).** The schema defines an API's type system and all object relationships.

* **[Introspective](/graphql/guides/introduction-to-graphql#discovering-the-graphql-api).** A client can query the schema for details about the schema.

* **[Hierarchical](/graphql/guides/forming-calls-with-graphql).** The shape of a GraphQL call mirrors the shape of the JSON data it returns. [Nested fields](/graphql/guides/migrating-from-rest-to-graphql#example-nesting) let you query for and receive only the data you specify in a single round trip.

* **An application layer.** GraphQL is not a storage model or a database query language. The _graph_ refers to graph structures defined in the schema, where [nodes](/graphql/guides/introduction-to-graphql#node) define objects and [edges](/graphql/guides/introduction-to-graphql#edge) define relationships between objects. The API traverses and returns application data based on the schema definitions, independent of how the data is stored.

## Why GitHub is using GraphQL

GitHub chose GraphQL because it offers significantly more flexibility for our integrators. The ability to define precisely the data you want&mdash;and _only_ the data you want&mdash;is a powerful advantage over traditional REST API endpoints. GraphQL lets you replace multiple REST requests with _a single call_ to fetch the data you specify.

For more details about why GitHub invested in GraphQL, see the original [announcement blog post](https://github.blog/2016-09-14-the-github-graphql-api/).

## About the GraphQL schema reference

The docs in the sidebar are generated from the GitHub GraphQL [schema](/graphql/guides/introduction-to-graphql#discovering-the-graphql-api). All calls are validated and executed against the schema. Use these docs to find out what data you can call:

* Allowed operations: [queries](/graphql/reference/queries) and [mutations](/graphql/reference/mutations).

* Schema-defined types: [scalars](/graphql/reference/scalars), [objects](/graphql/reference/objects), [enums](/graphql/reference/enums), [interfaces](/graphql/reference/interfaces), [unions](/graphql/reference/unions), and [input objects](/graphql/reference/input-objects).

For other information, such as authentication and rate limit details, check out the [guides](/graphql/guides).

## Requesting support

help_resources

If you observe unexpected failures, you can use [githubstatus.com](https://www.githubstatus.com/) or the [GitHub status API](https://www.githubstatus.com/api) to check for incidents affecting the API.

---

## GraphQL terminology

The GitHub GraphQL API represents an architectural and conceptual shift from the GitHub REST API. You will likely encounter some new terminology in the GraphQL API [reference docs](/graphql).

## Schema

A schema defines a GraphQL API's type system. It describes the complete set of possible data (objects, fields, relationships, everything) that a client can access. Calls from the client are [validated](https://graphql.org/learn/validation/) and [executed](https://graphql.org/learn/execution/) against the schema. A client can find information about the schema via [introspection](#discovering-the-graphql-api). A schema resides on the GraphQL API server. For more information, see [Discovering the GraphQL API](#discovering-the-graphql-api).

## Field

A field is a unit of data you can retrieve from an object. As the [official GraphQL docs](https://graphql.org/learn/schema/) say:
"The GraphQL query language is basically about selecting fields on objects."

The [official spec](https://spec.graphql.org/June2018/#sec-Language.Fields) also says about fields:

> All GraphQL operations must specify their selections down to fields which return scalar values to ensure an unambiguously shaped response.

This means that if you try to return a field that is not a scalar, schema validation will throw an error. You must add nested subfields until all fields return scalars.

## Argument

An argument is a set of key-value pairs attached to a specific field. Some fields require an argument. [Mutations](/graphql/guides/forming-calls-with-graphql#about-mutations) require an input object as an argument.

## Implementation

A GraphQL schema may use the term _implements_ to define how an object inherits from an [interface](/graphql/reference/interfaces).

Here's a contrived example of a schema that defines interface `X` and object `Y`:

```graphql
interface X {
  some_field: String!
  other_field: String!
}

type Y implements X {
  some_field: String!
  other_field: String!
  new_field: String!
}
```

This means object `Y` requires the same fields/arguments/return types that interface `X` does, while adding new fields specific to object `Y`. (The `!` means the field is required.)

In the reference docs, you'll find that:

* Each [object](/graphql/reference/objects) lists the interface(s) _from which it inherits_ under **Implements**.

* Each [interface](/graphql/reference/interfaces) lists the objects _that inherit from it_ under **Implementations**.

## Connection

Connections let you query related objects as part of the same call. With connections, you can use a single GraphQL call where you would have to use multiple calls to a REST API. For more information, see [Migrating From Rest To Graphql](/graphql/guides/migrating-from-rest-to-graphql).

It's helpful to picture a graph: dots connected by lines. The dots are nodes, the lines are edges. A connection defines a relationship between nodes.

## Edge

Edges represent connections between nodes. When you query a connection, you traverse its edges to get to its nodes. Every `edges` field has a `node` field and a `cursor` field. Cursors are used for pagination. For more information, see [Using Pagination In The Graphql Api](/graphql/guides/using-pagination-in-the-graphql-api).

## Node

_Node_ is a generic term for an object. You can look up a node directly, or you can access related nodes via a connection. If you specify a `node` that does not return a [scalar](/graphql/reference/scalars), you must include subfields until all fields return scalars. For information on accessing node IDs via the REST API and using them in GraphQL queries, see [Using Global Node Ids](/graphql/guides/using-global-node-ids).

## Discovering the GraphQL API

GraphQL is [introspective](https://graphql.org/learn/introspection/). This means you can query a GraphQL schema for details about itself.

* Query `__schema` to list all types defined in the schema and get details about each:

  ```graphql
  query {
    __schema {
      types {
        name
        kind
        description
        fields {
          name
        }
      }
    }
  }
  ```

* Query `__type` to get details about any type:

  ```graphql
  query {
    __type(name: "Repository") {
      name
      kind
      description
      fields {
        name
      }
    }
  }
  ```

* You can also run an _introspection query_ of the schema via a `GET` request:

  ```shell
  curl -H "Authorization: bearer TOKEN" https://api.github.com/graphql
  ```

  > [!NOTE]
  > If you get the response `"message": "Bad credentials"` or `401 Unauthorized`, check that you are using a valid token. If you receive a `403` error with `Resource not accessible by personal access token`, ensure that your fine-grained personal access token is targeted to the correct resource owner. For example, it must target the organization that owns the repository you are trying to access.
  
  The results are in JSON, so we recommend pretty-printing them for easier reading and searching. You can use a command-line tool like [jq](https://stedolan.github.io/jq/) or pipe the results into `python -m json.tool` for this purpose.

  Alternatively, you can pass the `idl` media type to return the results in IDL format, which is a condensed version of the schema:

  ```shell
  $ curl -H "Authorization: bearer TOKEN" -H "Accept: application/vnd.github.v4.idl" \
  https://api.github.com/graphql
  ```

  > [!NOTE]
  > The introspection query is probably the only `GET` request you'll run in GraphQL. If you're passing a body, the GraphQL request method is `POST`, whether it's a query or a mutation.

  For more information about performing queries, see [Forming Calls With Graphql](/graphql/guides/forming-calls-with-graphql).

---

## Authenticating with GraphQL

You can authenticate to the GraphQL API using a personal access token, GitHub App, or OAuth app.

### Authenticating with a personal access token

To authenticate with a personal access token, follow the steps in [Creating A Personal Access Token](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). The data that you are requesting will dictate which scopes or permissions you will need.

For example, select the "issues:read" permission to read all of the issues in the repositories your token has access to.

All fine-grained personal access tokens include read access to public repositories. To access public repositories with a personal access token (classic), select the "public_repo" scope.

If your token does not have the required scopes or permissions to access a resource, the API will return an error message that states the scopes or permissions your token needs.

### Authenticating with a GitHub App

If you want to use the API on behalf of an organization or another user, GitHub recommends that you use a GitHub App. In order to attribute activity to your app, you can make your app authenticate as an app installation. In order to attribute app activity to a user, you can make your app authenticate on behalf of a user. In both cases, you will generate a token that you can use to authenticate to the GraphQL API. For more information, see [Creating A Github App](/apps/creating-github-apps/setting-up-a-github-app/creating-a-github-app) and [About Authentication With A Github App](/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app).

### Authenticating with a OAuth app

To authenticate with an OAuth token from an OAuth app, you must first authorize your OAuth app using either a web application flow or device flow. Then, you can use the access token that you received to access the API. For more information, see [Creating An Oauth App](/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) and [Authorizing Oauth Apps](/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps).

## The GraphQL endpoint

The REST API has numerous endpoints. With the GraphQL API, the endpoint remains constant, no matter what operation you perform. For GitHub.comGitHub Enterprise Server, that endpoint is:

<pre>https://api.github.com/graphql</pre>


## Communicating with GraphQL

Because GraphQL operations consist of multiline JSON, GitHub recommends using the [GraphQL Clients](/graphql/guides/using-graphql-clients) to make GraphQL calls. You can also use `curl` or any other HTTP-speaking library.

In REST, [HTTP verbs](/rest#http-verbs) determine the operation performed. In GraphQL, you'll provide a JSON-encoded body whether you're performing a query or a mutation, so the HTTP verb is `POST`. The exception is an [introspection query](/graphql/guides/introduction-to-graphql#discovering-the-graphql-api), which is a simple `GET` to the endpoint. For more information on GraphQL versus REST, see [Migrating From Rest To Graphql](/graphql/guides/migrating-from-rest-to-graphql).

To query GraphQL in a `curl` command, make a `POST` request with a JSON payload. The payload must contain a string called `query`:

```shell
curl -H "Authorization: bearer TOKEN" -X POST -d " \
 { \
   \"query\": \"query { viewer { login }}\" \
 } \
" https://api.github.com/graphql
```

> [!NOTE]
> The string value of `"query"` must escape newline characters or the schema will not parse it correctly. For the `POST` body, use outer double quotes and escaped inner double quotes.

### About query and mutation operations

The two types of allowed operations in GitHub's GraphQL API are _queries_ and _mutations_. Comparing GraphQL to REST, queries operate like `GET` requests, while mutations operate like `POST`/`PATCH`/`DELETE`. The [mutation name](/graphql/reference/mutations) determines which modification is executed.

For information about rate limiting, see [Resource Limitations](/graphql/overview/resource-limitations).

Queries and mutations share similar forms, with some important differences.

### About queries

GraphQL queries return only the data you specify. To form a query, you must specify [fields within fields](/graphql/guides/introduction-to-graphql#field) (also known as _nested subfields_) until you return only [scalars](/graphql/reference/scalars).

Queries are structured like this:

<pre>query {
  JSON-OBJECT-TO-RETURN
}</pre>

For a real-world example, see [Example query](#example-query).

### About mutations

To form a mutation, you must specify three things:

1. _Mutation name_. The type of modification you want to perform.
1. _Input object_. The data you want to send to the server, composed of _input fields_. Pass it as an argument to the mutation name.
1. _Payload object_. The data you want to return from the server, composed of _return fields_. Pass it as the body of the mutation name.

Mutations are structured like this:

<pre>mutation {
  MUTATION-NAME(input: {MUTATION-NAME-INPUT!}) {
    MUTATION-NAME-PAYLOAD
  }
}</pre>

The input object in this example is `MutationNameInput`, and the payload object is `MutationNamePayload`.

In the [mutations](/graphql/reference/mutations) reference, the listed _input fields_ are what you pass as the input object. The listed _return fields_ are what you pass as the payload object.

For a real-world example, see [Example mutation](#example-mutation).

## Working with variables

[Variables](https://graphql.org/learn/queries/#variables) can make queries more dynamic and powerful, and they can reduce complexity when passing mutation input objects.

Here's an example query with a single variable:

```graphql
query($number_of_repos:Int!) {
  viewer {
    name
     repositories(last: $number_of_repos) {
       nodes {
         name
       }
     }
   }
}
variables {
   "number_of_repos": 3
}
```

There are three steps to using variables:

1. Define the variable outside the operation in a `variables` object:

   ```graphql
   variables {
      "number_of_repos": 3
   }
   ```

   The object must be valid JSON. This example shows a simple `Int` variable type, but it's possible to define more complex variable types, such as input objects. You can also define multiple variables here.

1. Pass the variable to the operation as an argument:

   ```graphql
   query($number_of_repos:Int!){
   ```

   The argument is a key-value pair, where the key is the _name_ starting with `$` (e.g., `$number_of_repos`), and the value is the _type_ (e.g., `Int`). Add a `!` to indicate whether the type is required. If you've defined multiple variables, include them here as multiple arguments.

1. Use the variable within the operation:

   ```graphql
   repositories(last: $number_of_repos) {
   ```

   In this example, we substitute the variable for the number of repositories to retrieve. We specify a type in step 2 because GraphQL enforces strong typing.

This process makes the query argument dynamic. We can now simply change the value in the `variables` object and keep the rest of the query the same.

Using variables as arguments lets you dynamically update values in the `variables` object without changing the query.

## Example query

Let's walk through a more complex query and put this information in context.

The following query looks up the `octocat/Hello-World` repository, finds the 20 most recent closed issues, and returns each issue's title, URL, and first 5 labels:

```graphql
query {
  repository(owner:"octocat", name:"Hello-World") {
    issues(last:20, states:CLOSED) {
      edges {
        node {
          title
          url
          labels(first:5) {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
  }
}
```

Looking at the composition line by line:

* `query {`

  Because we want to read data from the server, not modify it, `query` is the root operation. (If you don't specify an operation, `query` is also the default.)

* `repository(owner:"octocat", name:"Hello-World") {`

  To begin the query, we want to find a [`repository`](/graphql/reference/objects#repository) object. The schema validation indicates this object requires an `owner` and a `name` argument.

* `issues(last:20, states:CLOSED) {`

  To account for all issues in the repository, we call the `issues` object. (We _could_ query a single `issue` on a `repository`, but that would require us to know the number of the issue we want to return and provide it as an argument.)

  Some details about the `issues` object:

  * The [docs](/graphql/reference/objects#repository) tell us this object has the type `IssueConnection`.
  * Schema validation indicates this object requires a `last` or `first` number of results as an argument, so we provide `20`.
  * The [docs](/graphql/reference/objects#repository) also tell us this object accepts a `states` argument, which is an [`IssueState`](/graphql/reference/enums#issuestate) enum that accepts `OPEN` or `CLOSED` values. To find only closed issues, we give the `states` key a value of `CLOSED`.

* `edges {`

  We know `issues` is a connection because it has the `IssueConnection` type. To retrieve data about individual issues, we have to access the node via `edges`.

* `node {`

  Here we retrieve the node at the end of the edge. The [`IssueConnection` docs](/graphql/reference/objects#issueconnection) indicate the node at the end of the `IssueConnection` type is an `Issue` object.

* Now that we know we're retrieving an `Issue` object, we can look at the [docs](/graphql/reference/objects#issue) and specify the fields we want to return:

  ```graphql
  title
  url
  labels(first:5) {
    edges {
      node {
        name
      }
    }
  }
  ```

  Here we specify the `title`, `url`, and `labels` fields of the `Issue` object.

  The `labels` field has the type [`LabelConnection`](/graphql/reference/objects#labelconnection). As with the `issues` object, because `labels` is a connection, we must travel its edges to a connected node: the `label` object. At the node, we can specify the `label` object fields we want to return, in this case, `name`.

You may notice that running this query on the Octocat's public `Hello-World` repository won't return many labels. Try running it on one of your own repositories that does use labels, and you'll likely see a difference.

## Example mutation

Mutations often require information that you can only find out by performing a query first. This example shows two operations:

1. A query to get an issue ID.
1. A mutation to add an emoji reaction to the issue.

```graphql
query FindIssueID {
  repository(owner:"octocat", name:"Hello-World") {
    issue(number:349) {
      id
    }
  }
}

mutation AddReactionToIssue {
  addReaction(input:{subjectId:"MDU6SXNzdWUyMzEzOTE1NTE=",content:HOORAY}) {
    reaction {
      content
    }
    subject {
      id
    }
  }
}
```

Let's walk through the example. The task sounds simple: add an emoji reaction to an issue.

So how do we know to begin with a query? We don't, yet.

Because we want to modify data on the server (attach an emoji to an issue), we begin by searching the schema for a helpful mutation. The reference docs show the [`addReaction`](/graphql/reference/mutations#addreaction) mutation, with this description: `Adds a reaction to a subject.` Perfect!

The docs for the mutation list three input fields:

* `clientMutationId` (`String`)
* `subjectId` (`ID!`)
* `content` (`ReactionContent!`)

The `!`s indicate that `subjectId` and `content` are required fields. A required `content` makes sense: we want to add a reaction, so we'll need to specify which emoji to use.

But why is `subjectId` required? It's because the `subjectId` is the only way to identify _which_ issue in _which_ repository to react to.

This is why we start this example with a query: to get the `ID`.

Let's examine the query line by line:

* `query FindIssueID {`

  Here we're performing a query, and we name it `FindIssueID`. Note that naming a query is optional; we give it a name here so that we can include it in same GUI client window as the mutation.

* `repository(owner:"octocat", name:"Hello-World") {`

  We specify the repository by querying the `repository` object and passing `owner` and `name` arguments.

* `issue(number:349) {`

  We specify the issue to react to by querying the `issue` object and passing a `number` argument.

* `id`

  This is where we retrieve the `id` of `https://github.com/octocat/Hello-World/issues/349` to pass as the `subjectId`.

When we run the query, we get the `id`: `MDU6SXNzdWUyMzEzOTE1NTE=`

> [!NOTE]
> The `id` returned in the query is the value we'll pass as the `subjectID` in the mutation. Neither the docs nor schema introspection will indicate this relationship; you'll need to understand the concepts behind the names to figure this out.

With the ID known, we can proceed with the mutation:

* `mutation AddReactionToIssue {`

  Here we're performing a mutation, and we name it `AddReactionToIssue`. As with queries, naming a mutation is optional; we give it a name here so we can include it in the same GUI client window as the query.

* `addReaction(input:{subjectId:"MDU6SXNzdWUyMzEzOTE1NTE=",content:HOORAY}) {`

  Let's examine this line:

  * `addReaction` is the name of the mutation.
  * `input` is the required argument key. This will always be `input` for a mutation.
  * `{subjectId:"MDU6SXNzdWUyMzEzOTE1NTE=",content:HOORAY}` is the required argument value. This will always be an [input object](/graphql/reference/input-objects) (hence the curly braces) composed of input fields (`subjectId` and `content` in this case) for a mutation.

  How do we know which value to use for the content? The [`addReaction` docs](/graphql/reference/mutations#addreaction) tell us the `content` field has the type [`ReactionContent`](/graphql/reference/enums#reactioncontent), which is an [enum](/graphql/reference/enums) because only certain emoji reactions are supported on GitHub issues. These are the allowed values for reactions (note some values differ from their corresponding emoji names):

  reaction_list

* The rest of the call is composed of the payload object. This is where we specify the data we want the server to return after we've performed the mutation. These lines come from the [`addReaction` docs](/graphql/reference/mutations#addreaction), which three possible return fields:

  * `clientMutationId` (`String`)
  * `reaction` (`Reaction!`)
  * `subject` (`Reactable!`)

  In this example, we return the two required fields (`reaction` and `subject`), both of which have required subfields (respectively, `content` and `id`).

When we run the mutation, this is the response:

```json
{
  "data": {
    "addReaction": {
      "reaction": {
        "content": "HOORAY"
      },
      "subject": {
        "id": "MDU6SXNzdWUyMTc5NTQ0OTc="
      }
    }
  }
}
```

That's it! Check out your [reaction to the issue](https://github.com/octocat/Hello-World/issues/349) by hovering over the :tada: to find your username.

One final note: when you pass multiple fields in an input object, the syntax can get unwieldy. Moving the fields into a [variable](#working-with-variables) can help. Here's how you could rewrite the original mutation using a variable:

```graphql
mutation($myVar:AddReactionInput!) {
  addReaction(input:$myVar) {
    reaction {
      content
    }
    subject {
      id
    }
  }
}
variables {
  "myVar": {
    "subjectId":"MDU6SXNzdWUyMTc5NTQ0OTc=",
    "content":"HOORAY"
  }
}
```

> [!NOTE]
> You may notice that the `content` field value in the earlier example (where it's used directly in the mutation) does not have quotes around `HOORAY`, but it does have quotes when used in the variable. There's a reason for this:
> * When you use `content` directly in the mutation, the schema expects the value to be of type [`ReactionContent`](/graphql/reference/enums#reactioncontent), which is an _enum_, not a string. Schema validation will throw an error if you add quotes around the enum value, as quotes are reserved for strings.
> * When you use `content` in a variable, the variables section must be valid JSON, so the quotes are required. Schema validation correctly interprets the `ReactionContent` type when the variable is passed into the mutation during execution.
>
> For more information on the difference between enums and strings, see the [official GraphQL spec](https://spec.graphql.org/June2018/#sec-Enums).

## Further reading

There is a _lot_ more you can do when forming GraphQL calls. Here are some places to look next:

* [Using Pagination In The Graphql Api](/graphql/guides/using-pagination-in-the-graphql-api)
* [Fragments](https://graphql.org/learn/queries/#fragments)
* [Inline fragments](https://graphql.org/learn/queries/#inline-fragments)
* [Directives](https://graphql.org/learn/queries/#directives)

---

## About pagination

GitHub's GraphQL API limits the number of items that you can fetch in a single request in order to protect against excessive or abusive requests to GitHub's servers. When you use the GraphQL API, you must supply a `first` or `last` argument on any connection. The value of these arguments must be between 1 and 100. The GraphQL API will return the number of connections specified by the `first` or `last` argument.

If the data that you are accessing has more connections than the number of items specified by the `first` or `last` argument, the response is divided into smaller "pages" of the specified size. These pages can be fetched one at a time until the entire data set has been retrieved. Each page contains the number of items specified by the `first` or `last` argument, unless it is the last page, which may contain a lower number of items.

This guide demonstrates how to request additional pages of results for paginated responses, how to change the number of results returned on each page, and how to write a script to fetch multiple pages of results.

## Requesting a `cursor` in your query

When using the GraphQL API, you use cursors to traverse through a paginated data set. The cursor represents a specific position in the data set. You can get the first and last cursor on a page by querying the `pageInfo` object. For example:

```graphql
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    pullRequests(first: 100, after: null) {
      nodes {
        createdAt
        number
        title
      }
      pageInfo {
        endCursor
        startCursor
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
```

In this example, `pageInfo.startCursor` gives the cursor for the first item on the page. `pageInfo.endCursor` gives the cursor for the last item on the page. `pageInfo.hasNextPage` and `pageInfo.hasPreviousPage` indicate whether there is a page before and after the page that was returned.

## Changing the number of items per page

The `first` and `last` arguments control how many items are returned. The maximum number of items you can fetch using the `first` or `last` argument is 100. You may need to request fewer than 100 items if your query touches a lot of data in order to avoid hitting a rate or node limit. For more information, see [Rate Limits And Query Limits For The Graphql Api](/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api).

## Traversing the data set using pagination

Once you return a cursor from a query, you can use the cursor to request the next page of results. To do so, you will use the `after` or `before` argument and the cursor.

For example, assuming the `pageInfo.endCursor` value from the previous example was `Y3Vyc29yOnYyOpHOUH8B7g==`, you can use this query to request the next page of results:

```graphql
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    pullRequests(first: 1, after: "Y3Vyc29yOnYyOpHOUH8B7g==") {
      nodes {
        createdAt
        number
        title
      }
      pageInfo {
        endCursor
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
```

You can continue to send queries with the new `pageInfo.endCursor` value returned in the response until there are no pages left to traverse, indicated by `pageInfo.hasNextPage` returning `false`.

If you specified the `last` instead of the `first` argument, the last page of results will be returned first. In this case, you will use the `pageInfo.startCursor` value and the `before` argument to get the previous page of results. Once `pageInfo.hasPreviousPage` returns `false`, you have reached the last page. For example:

```graphql
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    pullRequests(last: 1, before: "R3Vyc29yOnYyOpHOHcfoOg==") {
      nodes {
        createdAt
        number
        title
      }
      pageInfo {
        startCursor
        hasPreviousPage
      }
    }
  }
}
```

## Next steps

You can use GitHub's Octokit SDK and the `octokit/plugin-paginate-graphql` plugin to support pagination in your scripts. For more information, see [plugin-paginate-graphql.js](https://github.com/octokit/plugin-paginate-graphql.js).

---

You can access most objects in GitHub (users, issues, pull requests, etc.) using either the REST API or the GraphQL API. You can find the **global node ID** of many objects from within the REST API and use these IDs in your GraphQL operations. For more information, see [Preview GraphQL API Node IDs in REST API resources](https://developer.github.com/changes/2017-12-19-graphql-node-id/).

> [!NOTE]
> In REST, the global node ID field is named `node_id`. In GraphQL, it's an `id` field on the `node` interface. For a refresher on what "node" means in GraphQL, see [Introduction To Graphql#Node](/graphql/guides/introduction-to-graphql#node).

## Putting global node IDs to use

You can follow three steps to use global node IDs effectively:

1. Call a REST endpoint that returns an object's `node_id`.
1. Find the object's type in GraphQL.
1. Use the ID and type to do a direct node lookup in GraphQL.

Let's walk through an example.

## 1. Call a REST endpoint that returns an object's node ID

If you [request the authenticated user](/rest/users/users#get-the-authenticated-user):

```shell
curl -i --header "Authorization: Bearer YOUR-TOKEN" https://api.github.com/user
```

you'll get a response that includes the `node_id` of the authenticated user:

```json
{
  "login": "octocat",
  "id": 1,
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "gravatar_id": "",
  "url": "https://api.github.com/users/octocat",
  "html_url": "https://github.com/octocat",
  "followers_url": "https://api.github.com/users/octocat/followers",
  "following_url": "https://api.github.com/users/octocat/following{/other_user}",
  "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
  "organizations_url": "https://api.github.com/users/octocat/orgs",
  "repos_url": "https://api.github.com/users/octocat/repos",
  "events_url": "https://api.github.com/users/octocat/events{/privacy}",
  "received_events_url": "https://api.github.com/users/octocat/received_events",
  "type": "User",
  "site_admin": false,
  "name": "monalisa octocat",
  "company": "GitHub",
  "blog": "https://github.com/blog",
  "location": "San Francisco",
  "email": "octocat@github.com",
  "hireable": false,
  "bio": "There once was...",
  "public_repos": 2,
  "public_gists": 1,
  "followers": 20,
  "following": 0,
  "created_at": "2008-01-14T04:33:35Z",
  "updated_at": "2008-01-14T04:33:35Z",
  "private_gists": 81,
  "total_private_repos": 100,
  "owned_private_repos": 100,
  "disk_usage": 10000,
  "collaborators": 8,
  "two_factor_authentication": true,
  "plan": {
    "name": "Medium",
    "space": 400,
    "private_repos": 20,
    "collaborators": 0
  },
  "node_id": "MDQ6VXNlcjU4MzIzMQ=="
}
```

## 2. Find the object type in GraphQL

In this example, the `node_id` value is `MDQ6VXNlcjU4MzIzMQ==`. You can use this value to query the same object in GraphQL.

You'll need to know the object's _type_ first, though. You can check the type with a simple GraphQL query:

```graphql
query {
  node(id:"MDQ6VXNlcjU4MzIzMQ==") {
     __typename
  }
}
```

This type of query&mdash;that is, finding the node by ID&mdash;is known as a "direct node lookup."

When you run this query, you'll see that the `__typename` is [`User`](/graphql/reference/objects#user).

## 3. Do a direct node lookup in GraphQL

Once you've confirmed the type, you can use an [inline fragment](https://graphql.org/learn/queries/#inline-fragments) to access the object by its ID and return additional data. In this example, we define the fields on `User` that we'd like to query:

```graphql
query {
  node(id:"MDQ6VXNlcjU4MzIzMQ==") {
   ... on User {
      name
      login
    }
  }
}
```

This type of query is the standard approach for looking up an object by its global node ID.

## Using global node IDs in migrations

When building integrations that use either the REST API or the GraphQL API, it's best practice to persist the global node ID so you can easily reference objects across API versions. For more information on handling the transition between REST and GraphQL, see [Migrating From Rest To Graphql](/graphql/guides/migrating-from-rest-to-graphql).

---

## Differences in API logic

GitHub provides two APIs: a REST API and a GraphQL API. For more information about GitHub's APIs, see [About Githubs Apis](/rest/overview/about-githubs-apis).

Migrating from REST to GraphQL represents a significant shift in API logic. The differences between REST as a style and GraphQL as a specification make it difficult&mdash;and often undesirable&mdash;to replace REST API calls with GraphQL API queries on a one-to-one basis. We've included specific examples of migration below.

To migrate your code from the [REST API](/rest) to the GraphQL API:

* Review the [GraphQL spec](https://spec.graphql.org/June2018/)
* Review GitHub's [GraphQL schema](/graphql/reference)
* Consider how any existing code you have currently interacts with the GitHub REST API
* Use [Global Node IDs](/graphql/guides/using-global-node-ids) to reference objects between API versions

Significant advantages of GraphQL include:

* [Getting the data you need and nothing more](#example-getting-the-data-you-need-and-nothing-more)
* [Nested fields](#example-nesting)
* [Strong typing](#example-strong-typing)

Here are examples of each.

## Example: Getting the data you need and nothing more

A single REST API call retrieves a list of your organization's members:

```shell
curl -v https://api.github.com/orgs/:org/members
```

The REST payload contains excessive data if your goal is to retrieve only member names and links to avatars. However, a GraphQL query returns only what you specify:

```graphql
query {
    organization(login:"github") {
    membersWithRole(first: 100) {
      edges {
        node {
          name
          avatarUrl
        }
      }
    }
  }
}
```

Consider another example: retrieving a list of pull requests and checking if each one is mergeable. A call to the REST API retrieves a list of pull requests and their [summary representations](/rest#summary-representations):

```shell
curl -v https://api.github.com/repos/:owner/:repo/pulls
```

Determining if a pull request is mergeable requires retrieving each pull request individually for its [detailed representation](/rest#detailed-representations) (a large payload) and checking whether its `mergeable` attribute is true or false:

```shell
curl -v https://api.github.com/repos/:owner/:repo/pulls/:number
```

With GraphQL, you could retrieve only the `number` and `mergeable` attributes for each pull request:

```graphql
query {
    repository(owner:"octocat", name:"Hello-World") {
    pullRequests(last: 10) {
      edges {
        node {
          number
          mergeable
        }
      }
    }
  }
}
```

## Example: Nesting

Querying with nested fields lets you replace multiple REST calls with fewer GraphQL queries. For example, retrieving a pull request along with its commits, non-review comments, and reviews using the **REST API** requires four separate calls:

```shell
curl -v https://api.github.com/repos/:owner/:repo/pulls/:number
curl -v https://api.github.com/repos/:owner/:repo/pulls/:number/commits
curl -v https://api.github.com/repos/:owner/:repo/issues/:number/comments
curl -v https://api.github.com/repos/:owner/:repo/pulls/:number/reviews
```

Using the **GraphQL API**, you can retrieve the data with a single query using nested fields:

```graphql
{
  repository(owner: "octocat", name: "Hello-World") {
    pullRequest(number: 1) {
      commits(first: 10) {
        edges {
          node {
            commit {
              oid
              message
            }
          }
        }
      }
      comments(first: 10) {
        edges {
          node {
            body
            author {
              login
            }
          }
        }
      }
      reviews(first: 10) {
        edges {
          node {
            state
          }
        }
      }
    }
  }
}
```

You can also extend the power of this query by [substituting a variable](/graphql/guides/forming-calls-with-graphql#working-with-variables) for the pull request number.

## Example: Strong typing

GraphQL schemas are strongly typed, making data handling safer.

Consider an example of adding a comment to an issue or pull request using a GraphQL [mutation](/graphql/reference/mutations), and mistakenly specifying an integer rather than a string for the value of [`clientMutationId`](/graphql/reference/mutations#addcomment):

```graphql
mutation {
  addComment(input:{clientMutationId: 1234, subjectId: "MDA6SXNzdWUyMjcyMDA2MTT=", body: "Looks good to me!"}) {
    clientMutationId
    commentEdge {
      node {
        body
        repository {
          id
          name
          nameWithOwner
        }
        issue {
          number
        }
      }
    }
  }
}
```

Executing this query returns errors specifying the expected types for the operation:

```json
{
  "data": null,
  "errors": [
    {
      "message": "Argument 'input' on Field 'addComment' has an invalid value. Expected type 'AddCommentInput!'.",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ]
    },
    {
      "message": "Argument 'clientMutationId' on InputObject 'AddCommentInput' has an invalid value. Expected type 'String'.",
      "locations": [
        {
          "line": 3,
          "column": 20
        }
      ]
    }
  ]
}
```

Wrapping `1234` in quotes transforms the value from an integer into a string, the expected type:

```graphql
mutation {
  addComment(input:{clientMutationId: "1234", subjectId: "MDA6SXNzdWUyMjcyMDA2MTT=", body: "Looks good to me!"}) {
    clientMutationId
    commentEdge {
      node {
        body
        repository {
          id
          name
          nameWithOwner
        }
        issue {
          number
        }
      }
    }
  }
}
```

---

The GitHub Discussions GraphQL API allows you to get, create, edit, and delete discussion posts. For more information about GitHub Discussions, see [About Discussions](/discussions/collaborating-with-your-community-using-discussions/about-discussions).

This API is available for authenticated users, OAuth apps, and GitHub Apps. Access tokens require the `repo` scope for private repositories and the `public_repo` scope for public repositories. For more information, see [Scopes For Oauth Apps](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps).

## Fields

### Repository.discussions

List the discussions within a repository. If `categoryId` is specified, only results within that category will be returned. If `answered` is not specified, both answered and unanswered discussions will be returned.

_Signature:_

```graphql
discussions(
  after: String,
  before: String,
  first: Int,
  last: Int,
  categoryId: ID = null,
  
  answered: Boolean = null,
  
  orderBy: DiscussionOrder = {field: UPDATED_AT, direction: DESC}
) : Discussion
```

#### DiscussionOrder

```graphql
"""
Ways in which discussions can be ordered.
"""
input DiscussionOrder {
  """
  The field by which to order discussions.
  """
  field: DiscussionOrderField!

  """
  The direction in which to order discussions by the specified field.
  """
  direction: OrderDirection!
}
```

```graphql
"""
Properties by which discussion connections can be ordered.
"""
enum DiscussionOrderField {
  """
  Order discussions by creation time.
  """
  CREATED_AT

  """
  Order discussions by most recent modification time.
  """
  UPDATED_AT
}
```

### Repository.discussionCategories

Return the available discussion categories defined within this repository. Each repository may have up to 25 categories. For more information about discussion categories, see [About Discussions#About Categories And Formats For Discussions](/discussions/collaborating-with-your-community-using-discussions/about-discussions#about-categories-and-formats-for-discussions).

_Signature:_

```graphql
discussionCategories(
  after: String,
  before: String,
  first: Int,
  last: Int,
) : DiscussionCategoryConnection!
```

### Repository.discussion

Get a discussion. Returns `null` if discussion with the specified ID does not exist.

_Signature:_

```graphql
discussion(number: Int!) : Discussion
```

### Repository.pinnedDiscussions

Return discussions pinned to this repository, ordered by pin position.

_Signature:_

```graphql
pinnedDiscussions(
  after: String,
  before: String,
  first: Int,
  last: Int,
) : PinnedDiscussionConnection!
```

## Objects

**Note:** For brevity, connection types are not expanded here. Each connection type mentioned in the schema follows the same pattern as other connections in the GraphQL API. For more information, see [Introduction To Graphql#Connection](/graphql/guides/introduction-to-graphql#connection).

```graphql
query {
  repository(owner: "github", name: "some-repo") {
    discussions(first: 10) {
      # type: DiscussionConnection
      totalCount # Int!

      pageInfo {
        # type: PageInfo (from the public schema)
        startCursor
        endCursor
        hasNextPage
        hasPreviousPage
      }

      edges {
        # type: DiscussionEdge
        cursor
        node {
          # type: Discussion
          id
        }
      }

      nodes {
        # type: Discussion
        id
      }
    }
  }
}
```

### Discussion

<details>
<summary>Fields:</summary>

```graphql
"""
A discussion in a repository.
"""
type Discussion implements Comment & Deletable & Lockable & Node & Reactable & RepositoryNode & Subscribable & Updatable {
  """
  Reason that the conversation was locked.
  """
  activeLockReason: LockReason

  
  """
  Check if this discussion has been answered
  """
  isAnswered: Boolean!
  

  """
  The comment chosen as this discussion's answer, if any.
  """
  answer: DiscussionComment

  """
  The time when a user chose this discussion's answer, if answered.
  """
  answerChosenAt: DateTime

  """
  The user who chose this discussion's answer, if answered.
  """
  answerChosenBy: Actor

  """
  The actor who authored the comment.
  """
  author: Actor

  """
  Author's association with the subject of the comment.
  """
  authorAssociation: CommentAuthorAssociation!

  """
  The main text of the discussion post.
  """
  body: String!

  """
  The body rendered to HTML.
  """
  bodyHTML: HTML!

  """
  The body rendered to text.
  """
  bodyText: String!

  """
  The category for this discussion.
  """
  category: DiscussionCategory!

  """
  The replies to the discussion.
  """
  comments(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String

    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String

    """
    Returns the first _n_ elements from the list.
    """
    first: Int

    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): DiscussionCommentConnection!

  """
  Identifies the date and time when the object was created.
  """
  createdAt: DateTime!

  """
  Check if this comment was created via an email reply.
  """
  createdViaEmail: Boolean!

  """
  Identifies the primary key from the database.
  """
  databaseId: Int

  """
  The actor who edited the comment.
  """
  editor: Actor
  id: ID!

  """
  Check if this comment was edited and includes an edit with the creation data
  """
  includesCreatedEdit: Boolean!

  """
  The moment the editor made the last edit
  """
  lastEditedAt: DateTime

  """
  `true` if the object is locked
  """
  locked: Boolean!

  """
  The number identifying this discussion within the repository.
  """
  number: Int!

  """
  Identifies when the comment was published at.
  """
  publishedAt: DateTime

  """
  A list of reactions grouped by content left on the subject.
  """
  reactionGroups: [ReactionGroup!]

  """
  A list of Reactions left on the Issue.
  """
  reactions(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String

    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String

    """
    Allows filtering Reactions by emoji.
    """
    content: ReactionContent

    """
    Returns the first _n_ elements from the list.
    """
    first: Int

    """
    Returns the last _n_ elements from the list.
    """
    last: Int

    """
    Allows specifying the order in which reactions are returned.
    """
    orderBy: ReactionOrder
  ): ReactionConnection!

  """
  The repository associated with this node.
  """
  repository: Repository!

  """
  The path for this discussion.
  """
  resourcePath: URI!

  """
  The title of this discussion.
  """
  title: String!

  """
  Identifies the date and time when the object was last updated.
  """
  updatedAt: DateTime!

  """
  The URL for this discussion.
  """
  url: URI!

  """
  A list of edits to this content.
  """
  userContentEdits(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String

    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String

    """
    Returns the first _n_ elements from the list.
    """
    first: Int

    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): UserContentEditConnection

  """
  Check if the current viewer can delete this object.
  """
  viewerCanDelete: Boolean!

  """
  Can user react to this subject
  """
  viewerCanReact: Boolean!

  """
  Check if the viewer is able to change their subscription status for the repository.
  """
  viewerCanSubscribe: Boolean!

  """
  Check if the current viewer can update this object.
  """
  viewerCanUpdate: Boolean!

  """
  Did the viewer author this comment.
  """
  viewerDidAuthor: Boolean!

  """
  Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.
  """
  viewerSubscription: SubscriptionState
}
```

</details>

### DiscussionComment

<details>
<summary>Fields</summary>

```graphql
"""
A comment on a discussion.
"""
type DiscussionComment implements Comment & Deletable & Minimizable & Node & Reactable & Updatable & UpdatableComment {
  """
  The actor who authored the comment.
  """
  author: Actor

  """
  Author's association with the subject of the comment.
  """
  authorAssociation: CommentAuthorAssociation!

  """
  The body as Markdown.
  """
  body: String!

  """
  The body rendered to HTML.
  """
  bodyHTML: HTML!

  """
  The body rendered to text.
  """
  bodyText: String!

  """
  Identifies the date and time when the object was created.
  """
  createdAt: DateTime!

  """
  Check if this comment was created via an email reply.
  """
  createdViaEmail: Boolean!

  """
  Identifies the primary key from the database.
  """
  databaseId: Int

  """
  The time when this replied-to comment was deleted
  """
  deletedAt: DateTime

  """
  The discussion this comment was created in
  """
  discussion: Discussion

  """
  The actor who edited the comment.
  """
  editor: Actor
  id: ID!

  """
  Check if this comment was edited and includes an edit with the creation data
  """
  includesCreatedEdit: Boolean!

  """
  Has this comment been chosen as the answer of its discussion?
  """
  isAnswer: Boolean!

  """
  Returns whether or not a comment has been minimized.
  """
  isMinimized: Boolean!

  """
  The moment the editor made the last edit
  """
  lastEditedAt: DateTime

  """
  Returns why the comment was minimized.
  """
  minimizedReason: String

  """
  Identifies when the comment was published at.
  """
  publishedAt: DateTime

  """
  A list of reactions grouped by content left on the subject.
  """
  reactionGroups: [ReactionGroup!]

  """
  A list of Reactions left on the Issue.
  """
  reactions(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String

    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String

    """
    Allows filtering Reactions by emoji.
    """
    content: ReactionContent

    """
    Returns the first _n_ elements from the list.
    """
    first: Int

    """
    Returns the last _n_ elements from the list.
    """
    last: Int

    """
    Allows specifying the order in which reactions are returned.
    """
    orderBy: ReactionOrder
  ): ReactionConnection!

  """
  The threaded replies to this comment.
  """
  replies(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String

    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String

    """
    Returns the first _n_ elements from the list.
    """
    first: Int

    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): DiscussionCommentConnection!

  """
  The discussion comment this comment is a reply to
  """
  replyTo: DiscussionComment

  """
  The path for this discussion comment.
  """
  resourcePath: URI!

  """
  Identifies the date and time when the object was last updated.
  """
  updatedAt: DateTime!

  """
  The URL for this discussion comment.
  """
  url: URI!

  """
  A list of edits to this content.
  """
  userContentEdits(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String

    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String

    """
    Returns the first _n_ elements from the list.
    """
    first: Int

    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): UserContentEditConnection

  """
  Check if the current viewer can delete this object.
  """
  viewerCanDelete: Boolean!

  """
  Can the current user mark this comment as an answer?
  """
  viewerCanMarkAsAnswer: Boolean!

  """
  Check if the current viewer can minimize this object.
  """
  viewerCanMinimize: Boolean!

  """
  Can user react to this subject
  """
  viewerCanReact: Boolean!

  """
  Can the current user unmark this comment as an answer?
  """
  viewerCanUnmarkAsAnswer: Boolean!

  """
  Check if the current viewer can update this object.
  """
  viewerCanUpdate: Boolean!

  """
  Reasons why the current viewer can not update this comment.
  """
  viewerCannotUpdateReasons: [CommentCannotUpdateReason!]!

  """
  Did the viewer author this comment.
  """
  viewerDidAuthor: Boolean!
}
```

</details>

### DiscussionCategory

<details>
<summary>Fields</summary>

```graphql
"""
A category for discussions in a repository.
"""
type DiscussionCategory implements Node & RepositoryNode {
  """
  Identifies the date and time when the object was created.
  """
  createdAt: DateTime!

  """
  A description of this category.
  """
  description: String

  """
  An emoji representing this category.
  """
  emoji: String!

  """
  This category's emoji rendered as HTML.
  """
  emojiHTML: HTML!
  id: ID!

  """
  Whether or not discussions in this category support choosing an answer with the markDiscussionCommentAsAnswer mutation.
  """
  isAnswerable: Boolean!

  """
  The name of this category.
  """
  name: String!

  """
  The repository associated with this node.
  """
  repository: Repository!

  """
  Identifies the date and time when the object was last updated.
  """
  updatedAt: DateTime!
}
```

</details>

### PinnedDiscussion

<details>
<summary>Fields:</summary>

```graphql
"""
A Pinned discussion is a discussion pinned to a repository's index page.
"""
type PinnedDiscussion implements Node & RepositoryNode {
  """
  Identifies the date and time when the object was created.
  """
  createdAt: DateTime!

  """
  Identifies the primary key from the database.
  """
  databaseId: Int

  """
  The discussion that was pinned.
  """
  discussion: Discussion!

  """
  Color stops of the chosen gradient
  """
  gradientStopColors: [String!]!
  id: ID!

  """
  Background texture pattern
  """
  pattern: PinnedDiscussionPattern!

  """
  The actor that pinned this discussion.
  """
  pinnedBy: Actor!

  """
  Preconfigured background gradient option
  """
  preconfiguredGradient: PinnedDiscussionGradient

  """
  The repository associated with this node.
  """
  repository: Repository!

  """
  Identifies the date and time when the object was last updated.
  """
  updatedAt: DateTime!
}
```

</details>

#### PinnedDiscussionPattern

<details>
<summary>Values</summary>

```graphql
"""
Preconfigured background patterns that may be used to style discussions pinned within a repository.
"""
enum PinnedDiscussionPattern {
  """
  An upward-facing chevron pattern
  """
  CHEVRON_UP

  """
  A hollow dot pattern
  """
  DOT

  """
  A solid dot pattern
  """
  DOT_FILL

  """
  A heart pattern
  """
  HEART_FILL

  """
  A friendly octocat face pattern
  """
  OCTOFACE

  """
  A plus sign pattern
  """
  PLUS
}
```

</details>

#### PinnedDiscussionGradient

<details>
<summary>Values</summary>

```graphql
"""
Preconfigured gradients that may be used to style discussions pinned within a repository.
"""
enum PinnedDiscussionGradient {
  """
  A gradient of blue to mint
  """
  BLUE_MINT

  """
  A gradient of blue to purple
  """
  BLUE_PURPLE

  """
  A gradient of pink to blue
  """
  PINK_BLUE

  """
  A gradient of purple to coral
  """
  PURPLE_CORAL

  """
  A gradient of red to orange
  """
  RED_ORANGE
}
```

</details>

## Interfaces

### RepositoryDiscussionAuthor

Implemented by the `User` and `Organization` types. **Note:** An `Organization` will only have discussions associated with it if it was converted from a `User`.

<details>
<summary>Fields</summary>

```graphql
"""
Represents an author of discussions in repositories.
"""
interface RepositoryDiscussionAuthor {
  """
  Discussions this user has started.
  """
  repositoryDiscussions(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String

    """
    Filter discussions to only those that have been answered or not. Defaults to
    including both answered and unanswered discussions.
    """
    answered: Boolean = null

    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String

    """
    Returns the first _n_ elements from the list.
    """
    first: Int

    """
    Returns the last _n_ elements from the list.
    """
    last: Int

    """
    Ordering options for discussions returned from the connection.
    """
    orderBy: DiscussionOrder = {field: CREATED_AT, direction: DESC}

    """
    Filter discussions to only those in a specific repository.
    """
    repositoryId: ID
  ): DiscussionConnection!
}
```

</details>

### RepositoryDiscussionCommentAuthor

Also implemented by the `User` and `Organization` types.

<details>
<summary>Fields</summary>

```graphql
"""
Represents an author of discussion comments in repositories.
"""
interface RepositoryDiscussionCommentAuthor {
  """
  Discussion comments this user has authored.
  """
  repositoryDiscussionComments(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String

    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String

    """
    Returns the first _n_ elements from the list.
    """
    first: Int

    """
    Returns the last _n_ elements from the list.
    """
    last: Int

    """
    Filter discussion comments to only those that were marked as the answer
    """
    onlyAnswers: Boolean = false

    """
    Filter discussion comments to only those in a specific repository.
    """
    repositoryId: ID
  ): DiscussionCommentConnection!
}
```

</details>

## Mutations

These mutations follow the same implementation pattern that other mutations in the GraphQL API. Each mutation accepts a single argument of an `Input` type, named after the mutation, and returns a `Payload` type containing the fields specified.

For example, this is a basic `createDiscussion` mutation that will create a new discussion:

```graphql
mutation {
  # input type: CreateDiscussionInput
  createDiscussion(input: {repositoryId: "1234", categoryId: "5678", body: "The body", title: "The title"}) {

    # response type: CreateDiscussionPayload
    discussion {
      id
    }
  }
}
```

### createDiscussion

Input fields:

* `body: String!` The body of the new discussion.
* `title: String!` The title of the new discussion.
* `repositoryId: ID!` The ID of a repository in which to create the discussion.
* `categoryId: ID!` The ID of a `DiscussionCategory` within this repository.
* `clientMutationId: String` A unique identifier for the client performing the mutation.

Return type fields:

* `clientMutationId: String` The unique identifier provided as an input.
* `discussion: Discussion` The discussion that was created.

### updateDiscussion

Input fields:

* `discussionId: ID!` The node ID of the discussion to update.
* `body: String` The new contents of the discussion body.
* `title: String` The new discussion title.
* `categoryId: ID` The node ID of a `DiscussionCategory` within the same repository to change this discussion to.
* `clientMutationId: String` A unique identifier for the client performing the mutation.

Return type fields:

* `clientMutationId: String` The unique identifier provided as an input.
* `discussion: Discussion` The discussion that was modified.

### deleteDiscussion

Input fields:

* `id: ID!` The node ID of the discussion to delete.
* `clientMutationId: String` A unique identifier for the client performing the mutation.

Return type fields:

* `clientMutationId: String` The unique identifier provided as an input.
* `discussion: Discussion` The discussion that was deleted.

### addDiscussionComment

Input fields:

* `body: String!` The contents of the comment.
* `discussionId: ID!` The node ID of the discussion to comment on.
* `replyToId: ID` The node ID of the discussion comment to reply to. If absent, the created comment will be a top-level comment.
* `clientMutationId: String` A unique identifier for the client performing the mutation.

Return type fields:

* `clientMutationId: String` The unique identifier provided as an input.
* `comment: DiscussionComment` The discussion comment that was created.

### updateDiscussionComment

Input fields:

* `body: String!` The new contents of the comment body.
* `commentId: ID!` The node ID of the discussion comment to update.
* `clientMutationId: String` A unique identifier for the client performing the mutation.

Return type fields:

* `clientMutationId: String` The unique identifier provided as an input.
* `comment: DiscussionComment` The discussion comment that was updated.

### deleteDiscussionComment

Input fields:

* `id: ID!` The node ID of the discussion comment to delete.
* `clientMutationId: String` A unique identifier for the client performing the mutation.

Return type fields:

* `clientMutationId: String` The unique identifier provided as an input.
* `comment: DiscussionComment` The discussion comment that was deleted.

### markDiscussionCommentAsAnswer

Input fields:

* `id: ID!` The node ID of the discussion comment to mark as an answer.
* `clientMutationId: String` A unique identifier for the client performing the mutation.

Return type fields:

* `clientMutationId: String` The unique identifier provided as an input.
* `discussion: Discussion` The discussion that includes the chosen comment.

### unmarkDiscussionCommentAsAnswer

Input fields:

* `id: ID!` The node ID of the discussion comment to unmark as an answer.
* `clientMutationId: String` A unique identifier for the client performing the mutation.

Return type fields:

* `clientMutationId: String` The unique identifier provided as an input.
* `discussion: Discussion` The discussion that includes the unmarked comment.

## Search

Discussion may be returned from the top-level `search` field. To search for discussion, specify `type` as `DISCUSSION`. The `SearchResultItemConnection` type has a `discussionCount` field to report the number of returned discussions, and the `Discussion` type is added to the `SearchResultItem` union. For more information, see [Queries#Searchresultitemconnection](/graphql/reference/queries#searchresultitemconnection) and [Searching Discussions](/search-github/searching-on-github/searching-discussions).

---

## About managing enterprise accounts with GraphQL

To help you monitor and make changes in your organizations and maintain compliance, you can use the Enterprise Accounts API and the Audit Log API, which are only available as GraphQL APIs.

The enterprise account endpoints work for both GitHub Enterprise Cloud and for GitHub Enterprise Server.

GraphQL allows you to request and return just the data you specify. For example, you can create a GraphQL query, or request for information, to see all the new organization members added to your organization. Or you can make a mutation, or change, to invite an administrator to your enterprise account.

With the Audit Log API, you can monitor when someone:
* Accesses your organization or repository settings.
* Changes permissions.
* Adds or removes users in an organization, repository, or team.
* Promotes users to admin.
* Changes permissions of a GitHub App.

The Audit Log API enables you to keep copies of your audit log data. For queries made with the Audit Log API, the GraphQL response can include data for up to 90 to 120 days. For a list of the fields available with the Audit Log API, see the [Interfaces#Auditentry](/graphql/reference/interfaces#auditentry/).

With the Enterprise Accounts API, you can:
* List and review all of the organizations and repositories that belong to your enterprise account.
* Change Enterprise account settings.
* Configure policies for settings on your enterprise account and its organizations.
* Invite administrators to your enterprise account.
* Create new organizations in your enterprise account.

For a list of the fields available with the Enterprise Accounts API, see [Managing Enterprise Accounts#Graphql Fields And Types For The Enterprise Accounts Api](/graphql/guides/managing-enterprise-accounts#graphql-fields-and-types-for-the-enterprise-accounts-api).

## Getting started using GraphQL for enterprise accounts

See [Using Graphql Clients](/graphql/guides/using-graphql-clients) to get started using GraphQL to manage your enterprise accounts.

For some example queries, see [An example query using the Enterprise Accounts API](#an-example-query-using-the-enterprise-accounts-api).

### 1. Authenticate with your personal access token

1. To authenticate with GraphQL, you need to generate a personal access token from developer settings. For more information, see [Creating A Personal Access Token](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

1. Grant admin and full control permissions to your personal access token for areas of your enterprise you'd like to access. For full permission to private repositories, organizations, teams, user data, and access to enterprise billing and profile data, we recommend you select these scopes for your personal access token:
    * `repo`
    * `admin:org`
    * `user`
    * `admin:enterprise`

   The enterprise account specific scopes are:
    * `admin:enterprise`: Gives full control of enterprises (includes `manage_runners:enterprise`, `manage_billing:enterprise` and `read:enterprise`)
    * `manage_billing:enterprise`: Read and write enterprise billing data.
    * `read:enterprise`: Read enterprise profile data.

1. Copy your personal access token and keep it in a secure place until you add it to your GraphQL client.

### 2. Choose a GraphQL client

We recommend you use GraphiQL or another standalone GraphQL client that lets you configure the base URL.

You may also consider using these GraphQL clients:
* [Insomnia](https://support.insomnia.rest/article/176-graphql-queries)
* [GraphiQL](https://www.gatsbyjs.org/docs/running-queries-with-graphiql/)
* [Postman](https://learning.getpostman.com/docs/postman/sending_api_requests/graphql/)

The next steps will use Insomnia.

### 3. Setting up Insomnia to use the GitHub GraphQL API with enterprise accounts

1. Add the base url and `POST` method to your GraphQL client. When using GraphQL to request information (queries), change information (mutations), or transfer data using the GitHub API, the default HTTP method is `POST` and the base url follows this syntax:
    * For your enterprise instance: `https://<HOST>/api/graphql`
    * For GitHub Enterprise Cloud: `https://api.github.com/graphql`
    * For GitHub Enterprise Cloud with Data Residency: `https://api.SUBDOMAIN.ghe.com/graphql`

1. Select the "Auth" menu and click **Bearer Token**. If you've previously selected a different authentication method, the menu will be labeled with that method, such as "Basic Auth", instead.
   ![Screenshot of the expanded "Auth" menu in Insomnia. The menu label, "Auth", and the "Bearer Token" option are outlined in dark orange.](/assets/images/developer/graphql/insomnia-bearer-token-option.png)
1. In the "TOKEN" field, enter your personal access token from an earlier step.
   ![Screenshot of the "Bearer" authentication settings in Insomnia. The "TOKEN" field is outlined in dark orange.](/assets/images/developer/graphql/insomnia-base-url-and-pat.png)
1. Click **Headers**.
   ![Screenshot of the settings tabs in Insomnia. The "Headers" tab is outlined in dark orange.](/assets/images/developer/graphql/json-content-type-header.png)
1. Under the **Headers** tab, click **Add**.
1. In the "header" field, enter `Content-Type`.
1. In the "value" field, enter `application/json`.

Now you are ready to start making queries.

## An example query using the Enterprise Accounts API

This GraphQL query requests the total number of `public` repositories in each of your appliance's organizations using the Enterprise Accounts API. To customize this query, replace `<enterprise-account-name>` with the handle for your enterprise account. For example, if your enterprise account is located at `https://github.com/enterprises/octo-enterprise`, replace `<enterprise-account-name>` with `octo-enterprise`.

```graphql
query publicRepositoriesByOrganization($slug: String!) {
  enterprise(slug: $slug) {
    ...enterpriseFragment
  }
}

fragment enterpriseFragment on Enterprise {
  ... on Enterprise{
    name
    organizations(first: 100){
      nodes{
        name
        ... on Organization{
          name
          repositories(privacy: PUBLIC){
            totalCount
          }
        }
      }
    }
  }
}

# Passing our Enterprise Account as a variable
variables {
  "slug": "<enterprise-account-name>"
}
```

The next GraphQL query example shows how challenging it is to retrieve the number of `public` repositories in each organization without using the Enterprise Account API. Notice that the GraphQL Enterprise Accounts API has made this task simpler for enterprises since you only need to customize a single variable. To customize this query, replace `<name-of-organization-one>` and `<name-of-organization-two>`, etc. with the organization names on your instance.

```graphql
# Each organization is queried separately
{
  organizationOneAlias: organization(login: "nameOfOrganizationOne") {
    # How to use a fragment
    ...repositories
  }
  organizationTwoAlias: organization(login: "nameOfOrganizationTwo") {
    ...repositories
  }
  # organizationThreeAlias ... and so on up-to lets say 100
}

## How to define a fragment
fragment repositories on Organization {
  name
  repositories(privacy: PUBLIC){
    totalCount
  }
}
```

## Query each organization separately

```graphql
query publicRepositoriesByOrganization {
  organizationOneAlias: organization(login: "<name-of-organization-one>") {
    # How to use a fragment
    ...repositories
  }
  organizationTwoAlias: organization(login: "<name-of-organization-two>") {
    ...repositories
  }
  # organizationThreeAlias ... and so on up-to lets say 100
}
# How to define a fragment
fragment repositories on Organization {
  name
  repositories(privacy: PUBLIC){
    totalCount
  }
}
```

This GraphQL query requests the last 5 log entries for an enterprise organization. To customize this query, replace `<org-name>` and `<user-name>`.

```graphql
{
  organization(login: "<org-name>") {
    auditLog(last: 5, query: "actor:<user-name>") {
      edges {
        node {
          ... on AuditEntry {
# Get Audit Log Entry by 'Action'
            action
            actorLogin
            createdAt
# User 'Action' was performed on
           user{
              name
                email
            }
          }
        }
      }
    }
  }
}
```

For more information about getting started with GraphQL, see [Introduction To Graphql](/graphql/guides/introduction-to-graphql) and [Forming Calls With Graphql](/graphql/guides/forming-calls-with-graphql).

## GraphQL fields and types for the Enterprise Accounts API

For more details about the new queries, mutations, and schema defined types available for use with the Enterprise Accounts API, see the sidebar with detailed GraphQL definitions from any [GraphQL reference page](/graphql).

You can access the reference docs from within the GraphQL clients. For more information, see [Using Graphql Clients](/graphql/guides/using-graphql-clients).
For other information, such as authentication and rate limit details, check out the [guides](/graphql/guides).

---

## Primary rate limit

* _For GitHub App installations_: 5,000 points per hour per installation. Installations that have more than 20 repositories receive another 50 points per hour for each repository. Installations that are on an organization that have more than 20 users receive another 50 points per hour for each user. The rate limit cannot increase beyond 12,500 points per hour. The rate limit for user access tokens (as opposed to installation access tokens) are dictated by the primary rate limit for users.
* _For GitHub App installations on a GitHub Enterprise Cloud organization_: 10,000 points per hour per installation. The rate limit for user access tokens (as opposed to installation access tokens) are dictated by the primary rate limit for users.
* _For OAuth apps_: 5,000 points per hour, or 10,000 points per hour if the app is owned by a GitHub Enterprise Cloud organization. This only applies when the app uses their client ID and client secret to request public data. The rate limit for OAuth access tokens generated by a OAuth app are dictated by the primary rate limit for users.
* _For `GITHUB_TOKEN` in GitHub Actions workflows_: 1,000 points per hour per repository. For requests to resources that belong to an enterprise account on GitHub.com, the limit is 15,000 points per hour per repository.

You can check the point value of a query or calculate the expected point value as described in the following sections. The formula for calculating points and the rate limit are subject to change.

### Checking the status of your primary rate limit

You can use the headers that are sent with each response to determine the current status of your primary rate limit.

Header name | Description
-----------|-----------|
`x-ratelimit-limit` | The maximum number of points that you can use per hour
`x-ratelimit-remaining` | The number of points remaining in the current rate limit window
`x-ratelimit-used` | The number of points you have used in the current rate limit window
`x-ratelimit-reset` | The time at which the current rate limit window resets, in UTC epoch seconds
`x-ratelimit-resource` | The rate limit resource that the request counted against. For GraphQL requests, this will always be `graphql`.

You can also query the `rateLimit` object to check your rate limit. When possible, you should use the rate limit response headers instead of querying the API to check your rate limit.

```graphql
query {
  viewer {
    login
  }
  rateLimit {
    limit
    remaining
    used
    resetAt
  }
}
```

Field | Description
-----------|-----------|
`limit` | The maximum number of points that you can use per hour
`remaining` | The number of points remaining in the current rate limit window
`used` | The number of points you have used in the current rate limit window
`resetAt` | The time at which the current rate limit window resets, in UTC epoch seconds

### Returning the point value of a query

You can return the point value of a query by querying the `cost` field on the `rateLimit` object:

```graphql
query {
  viewer {
    login
  }
  rateLimit {
    cost
  }
}
```

### Predicting the point value of a query

You can also roughly calculate the point value of a query before you make the query.

1. Add up the number of requests needed to fulfill each unique connection in the call. Assume every request will reach the `first` or `last` argument limits.
1. Divide the number by **100** and round the result to the nearest whole number to get the final aggregate point value. This step normalizes large numbers.

> [!NOTE]
> The minimum point value of a call to the GraphQL API is **1**.

Here's an example query and score calculation:

```graphql
query {
  viewer {
    login
    repositories(first: 100) {
      edges {
        node {
          id

          issues(first: 50) {
            edges {
              node {
                id

                labels(first: 60) {
                  edges {
                    node {
                      id
                      name
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

This query requires 5,101 requests to fulfill:

* Although we're returning 100 repositories, the API has to connect to the viewer's account **once** to get the list of repositories. So, requests for repositories = **1**
* Although we're returning 50 issues, the API has to connect to each of the **100** repositories to get the list of issues. So, requests for issues = **100**
* Although we're returning 60 labels, the API has to connect to each of the **5,000** potential total issues to get the list of labels. So, requests for labels = **5,000**
* Total = **5,101**

Dividing by 100 and rounding gives us the final score of the query: **51**

## Secondary rate limits


## Exceeding the rate limit

If you exceed your primary rate limit, the response status will still be `200`, but you will receive an error message, and the value of the `x-ratelimit-remaining` header will be `0`. You should not retry your request until after the time specified by the `x-ratelimit-reset` header.

If you exceed a secondary rate limit, the response status will be `200` or `403`, and you will receive an error message that indicates that you hit a secondary rate limit. If the `retry-after` response header is present, you should not retry your request until after that many seconds has elapsed. If the `x-ratelimit-remaining` header is `0`, you should not retry your request until after the time, in UTC epoch seconds, specified by the `x-ratelimit-reset` header. Otherwise, wait for at least one minute before retrying. If your request continues to fail due to a secondary rate limit, wait for an exponentially increasing amount of time between retries, and throw an error after a specific number of retries.

Continuing to make requests while you are rate limited may result in the banning of your integration.

## Staying under the rate limit

To avoid exceeding a rate limit, you should pause at least 1 second between mutative requests and avoid concurrent requests.

You should also subscribe to webhook events instead of polling the API for data. For more information, see [Webhooks](/webhooks).

You can also stream the audit log in order to view API requests. This can help you troubleshoot integrations that are exceeding the rate limit. For more information, see [Streaming The Audit Log For Your Enterprise](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise).


## Node limit

To pass [schema](/graphql/guides/introduction-to-graphql#schema) validation, all GraphQL API [calls](/graphql/guides/forming-calls-with-graphql) must meet these standards:

* Clients must supply a `first` or `last` argument on any [connection](/graphql/guides/introduction-to-graphql#connection).
* Values of `first` and `last` must be within 1-100.
* Individual calls cannot request more than 500,000 total [nodes](/graphql/guides/introduction-to-graphql#node).

### Calculating nodes in a call

These two examples show how to calculate the total nodes in a call.

1. Simple query:

   <pre>query {
     viewer {
       repositories(first: <span class="redbox">50</span>) {
         edges {
           repository:node {
             name

             issues(first: <span class="greenbox">10</span>) {
               totalCount
               edges {
                 node {
                   title
                   bodyHTML
                 }
               }
             }
           }
         }
       }
     }
   }</pre>

   Calculation:

   <pre><span class="redbox">50</span>         = 50 repositories
    +
   <span class="redbox">50</span> x <span class="greenbox">10</span>  = 500 repository issues

               = 550 total nodes</pre>

1. Complex query:

   <pre>query {
     viewer {
       repositories(first: <span class="redbox">50</span>) {
         edges {
           repository:node {
             name

             pullRequests(first: <span class="greenbox">20</span>) {
               edges {
                 pullRequest:node {
                   title

                   comments(first: <span class="bluebox">10</span>) {
                     edges {
                       comment:node {
                         bodyHTML
                       }
                     }
                   }
                 }
               }
             }

             issues(first: <span class="greenbox">20</span>) {
               totalCount
               edges {
                 issue:node {
                   title
                   bodyHTML

                   comments(first: <span class="bluebox">10</span>) {
                     edges {
                       comment:node {
                         bodyHTML
                       }
                     }
                   }
                 }
               }
             }
           }
         }
       }

       followers(first: <span class="bluebox">10</span>) {
         edges {
           follower:node {
             login
           }
         }
       }
     }
   }</code></pre>

   Calculation:

   <pre><span class="redbox">50</span>              = 50 repositories
    +
   <span class="redbox">50</span> x <span class="greenbox">20</span>       = 1,000 pullRequests
    +
   <span class="redbox">50</span> x <span class="greenbox">20</span> x <span class="bluebox">10</span> = 10,000 pullRequest comments
    +
   <span class="redbox">50</span> x <span class="greenbox">20</span>       = 1,000 issues
    +
   <span class="redbox">50</span> x <span class="greenbox">20</span> x <span class="bluebox">10</span> = 10,000 issue comments
    +
   <span class="bluebox">10</span>              = 10 followers

                    = 22,060 total nodes</pre>

  

## Timeouts

If GitHub takes more than 10 seconds to process an API request, GitHub will terminate the request and you will receive a timeout response and a message reporting that "We couldn't respond to your request in time".

GitHub reserves the right to change the timeout window to protect the speed and reliability of the API.

You can check the status of the GraphQL API at [githubstatus.com](https://www.githubstatus.com/) to determine whether the timeout is due to a problem with the API. You can also try to simplify your request or try your request later. For example, if you are requesting a large number of objects in a single request, you can try requesting fewer objects split over multiple queries.

If a timeout occurs for any of your API requests, additional points will be deducted from your primary rate limit for the next hour to protect the speed and reliability of the API.

## Other resource limits

To protect the speed and reliability of the API, GitHub also enforces other resource limitations. If your GraphQL query consumes too many resources, GitHub will terminate the request and return partial results along with an error indicating that resource limits were exceeded.

**Examples of queries that may exceed resource limits:**

* Requesting thousands of objects or deeply nested relationships in a single query.
* Using large `first` or `last` arguments in multiple connections simultaneously.
* Fetching extensive details for each object, such as all comments, reactions, and related issues for every repository.


## Query optimization strategies

* **Limit the number of objects**: Use smaller values for `first` or `last` arguments and paginate through results.
* **Reduce query depth**: Avoid requesting deeply nested objects unless necessary.
* **Filter results**: Use arguments to filter data and return only what you need.
* **Split large queries**: Break up complex queries into multiple simpler queries.
* **Request only required fields**: Select only the fields you need, rather than requesting all available fields.

By following these strategies, you can reduce the likelihood of hitting resource limits and improve the performance and reliability of your API requests.

---

## About breaking changes

Breaking changes are any changes that might require action from our integrators. We divide these changes into two categories:

* **Breaking:** Changes that will break existing queries to the GraphQL API. For example, removing a field would be a breaking change.
* **Dangerous:** Changes that won't break existing queries but could affect the runtime behavior of clients. Adding an enum value is an example of a dangerous change.

We'll announce upcoming breaking changes at least three months before making changes to the GraphQL schema, to give integrators time to make the necessary adjustments. Changes go into effect on the first day of a quarter (January 1st, April 1st, July 1st, or October 1st). For example, if we announce a change on January 15th, it will be made on July 1st.

---
