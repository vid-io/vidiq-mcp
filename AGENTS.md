# vidIQ MCP agent guide

This repository packages connection metadata and creator-workflow skills for the hosted vidIQ MCP
service across Claude, Codex, Cursor, GitHub Copilot, and Gemini.

Apply this guide to vidIQ requests and vidIQ MCP calls. Do not start onboarding, account checks,
or creator research for an unrelated task. Read
[Live surface notes](references/live-surface-notes.md), including when analyzing supplied evidence.
Load only the selected skill and references relevant to the request.

## Connect

Follow the client-specific flow in [README.md](README.md). The hosted Streamable HTTP endpoint is
`https://mcp.vidiq.com/mcp`; compatible clients open a browser for vidIQ authorization. Never ask
the user to paste credentials into chat or save them in shared configuration.

If vidIQ tools are not visible, help the user confirm that the plugin or MCP connection is enabled
and authorized. If the wrong account or channel appears, suggest reconnecting with the intended
vidIQ account.

## Start and route

Use `vidiq-get-started` for connection, account, channel, and credit guidance, troubleshooting,
or interrupted-job recovery. Use `vidiq-next-video-planner`
for evidence-backed topic selection and `vidiq-channel-review` for bounded 30-, 60-, or
90-day portfolio reviews. Route upload performance, retention, viewer comments, video ideas,
packaging, trends, competitor tracking, and Shorts inspiration to the matching skill. For
end-to-end "find an idea and package it" requests, run `vidiq-video-ideas` first
and feed its concept cards into `vidiq-packaging-studio`. When the creator already has a script
draft, a rough idea pitch, or a published video that needs repackaging, go straight to
`vidiq-packaging-studio`; it handles diagnosis and reference discovery itself.
For a focused title or thumbnail edit, use only the relevant studio stage. Reserve
`vidiq-packaging-comparison` for an explicit comparison of distinct creative directions.

## Calls without a dedicated workflow

Read [Discovery evidence](references/discovery-evidence.md) before recurring discovery-pattern
claims, and [Job lifecycle](references/job-lifecycle.md) before asynchronous work.

For media generation, confirm only the source, likeness, and speaker rights relevant to that
medium; preserve required attribution. Reuse rights already established for the supplied assets.
Voice cloning requires explicit speaker consent. Keep temporary or signed media URLs within the
user's requested workflow.
