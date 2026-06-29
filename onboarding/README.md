# Programmatic API Onboarding — Twilio

A single-file, zero-dependency Node.js (18+) CLI that reproduces SoundCloud's
`sc-api-auth.mjs` pattern for Twilio: register an application / obtain credentials
programmatically instead of clicking through a dashboard, so agents and developers
can onboard at the command line.

- Script: [`twilio-api-auth.mjs`](twilio-api-auth.mjs)
- Run `node twilio-api-auth.mjs --help` for usage and the required environment variables.
- Story / rationale: https://apievangelist.com/2026/08/15/twilio-programmatic-onboarding-means-it/

Part of the API Evangelist "Programmatic API Onboarding for the Agentic Moment" series.
