# Twilio GraphQL

## Overview

Twilio exposes a GraphQL surface primarily through **Twilio Flex**, its programmable digital engagement center. The Flex UI ships a built-in Apollo-based GraphQL client that plugin developers can use to query Flex configuration and interaction data. Outside of Flex, Twilio's platform is REST-first; the types in `twilio-schema.graphql` model every major Twilio REST resource as a GraphQL SDL so that tooling, code generators, and federated graph stitching layers can treat the full Twilio surface uniformly.

## Endpoint

| Context | URL |
|---------|-----|
| Twilio Flex (internal, requires Flex SSO token) | `https://flex-api.twilio.com/v1/graphql` |

> Note: The Flex GraphQL endpoint is not publicly advertised as a stable external API. It is consumed by the Flex UI and plugin ecosystem. Direct introspection requires a valid Flex access token issued via `POST /v1/tokens`. Third-party access should go through the Flex REST API and TaskRouter REST API.

## Authentication

Twilio uses **HTTP Basic Auth** (Account SID as username, Auth Token as password) for its REST APIs. For Flex-specific calls, a short-lived **Flex access token** (JWT) is obtained from `POST https://flex-api.twilio.com/v1/tokens` and passed as a `Bearer` token in the `Authorization` header.

```
Authorization: Basic <base64(AccountSid:AuthToken)>
```

For the Flex GraphQL endpoint specifically:

```
Authorization: Bearer <flex_access_token>
```

API keys (Key SID + Secret) are recommended over the master Auth Token for production use. All requests must be made over HTTPS.

## Notes

- **Schema origin**: The SDL in `twilio-schema.graphql` is a conceptual data model derived from Twilio's documented REST APIs (Flex, TaskRouter, Conversations, Voice, Messaging, Video, Verify, Accounts). It is not auto-generated from a live `/v1/graphql` introspection — Twilio does not publish a canonical public GraphQL schema document.
- **Flex UI GraphQL client**: Twilio Flex 2.x ships `@twilio/flex-ui` with an Apollo Client instance. Plugin authors can import and extend this client to co-locate queries with their React components. See the Flex UI reference docs for `Manager.getInstance().insightsClient`.
- **TaskRouter**: The richest data model for contact-center routing (Workers, Tasks, Queues, Workspaces, Reservations) is served via REST at `https://taskrouter.twilio.com/v1/`. The GraphQL types `Workspace`, `Worker`, `Task`, `Queue`, `Workflow`, `Activity`, `Reservation`, and `TaskChannel` mirror those resources directly.
- **Conversations**: Multi-channel messaging (SMS, WhatsApp, Chat) is modelled through `Conversation`, `ConversationParticipant`, `ConversationMessage`, and `ConversationWebhook` types.
- **Flex-specific types**: `FlexFlow`, `Interaction`, `InteractionChannel`, and `Plugin` are Flex-native resources with no exact counterpart in the generic Twilio API surface.
- **References**:
  - https://www.twilio.com/docs/flex/developer
  - https://www.twilio.com/docs/flex/developer/plugins/api
  - https://www.twilio.com/docs/taskrouter/api
  - https://www.twilio.com/docs/conversations/api
  - https://www.twilio.com/docs/voice/api
  - https://www.twilio.com/docs/messaging/api
  - https://www.twilio.com/docs/verify/api
  - https://www.twilio.com/docs/iam/api/account
