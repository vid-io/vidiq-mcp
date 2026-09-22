---
name: vidiq-get-started
description: Connect and authenticate vidIQ MCP, verify channel access and credits, and choose a first workflow. Use for setup, capability questions, or missing or unexpected channels.
---

# vidIQ Get Started

Read [Live surface notes](references/live-surface-notes.md) first, even when using only supplied evidence.

Help the creator connect, verify access, and choose one useful next workflow.

## Connect and verify

1. Inspect whether vidIQ tools are visible. Visibility confirms that the client loaded the
   server; successful account-state calls establish authorization.
2. If tools are missing, check installation, enablement, and client reload requirements.
   Use the client's native MCP authentication action when available; otherwise follow its
   connection flow and the [official setup guide](https://support.vidiq.com/en/articles/15082430-vidiq-mcp).
   Wait for browser authorization, then re-check. Never request credentials in chat.
3. Call `vidiq_user_channels` once and report the returned authorized IDs.
   Account labels are optional and useful only for diagnosis.
   An empty or unexpected list can indicate the wrong account; suggest reconnecting with the
   intended account without claiming token expiry.
4. Resolve the intended channel only before channel-specific work. If several IDs are returned,
   use the user's explicit selection; do not pick the first or largest. Enrich titles with
   `vidiq_get_channels_by_ids` only when needed. A channel outside the authorized
   set can receive public research, but not private analytics.
5. Use `vidiq_balance` to explain returned renewable and
   add-on credits, preserving `unlimited` and `null`.
   Use `vidiq-status` for a failure or interrupted job instead of repeating failed calls.

## Choose the next step

Use the creator's stated decision. If it is unclear, ask one compact question and offer:

- **Package an existing idea or video:** `vidiq-packaging-studio`.
- **Discover an idea:** `vidiq-video-ideas`; feed its concept cards into packaging for an
  end-to-end request.
- **Review performance:** `vidiq-channel-review`, or `vidiq-new-upload-review` for a recent upload.

Honor a more specific request with its matching skill. Supplied-context analysis or text drafting
may need no MCP calls. Do not run research merely to demonstrate the connection.
Onboarding alone does not authorize later generation or state changes.

## Report

Give connection and authorization state, the relevant authorized/selected channel, available
credit information, one recommended workflow, and the next action.
