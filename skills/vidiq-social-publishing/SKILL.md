---
name: vidiq-social-publishing
description: Prepare and adapt supplied content for YouTube, Instagram, TikTok, X, and Facebook Pages; save drafts, publish or schedule approved versions, and track each destination. Use when asked 'post this everywhere', 'publish a Reel', 'upload to YouTube', 'tweet this', 'schedule these posts', 'change my draft', 'what is scheduled', or 'did my post go out'. For changes to a video already on YouTube, use vidiq-video-metadata.
---

# vidIQ Social Publishing

Read [Live surface notes](references/live-surface-notes.md) first, even when using only supplied evidence.

Turn the creator's content into appropriate versions for their chosen accounts, prepare a clear
review, and carry the approved versions through delivery. Keep the creator's voice and choices
intact. A simple post should remain simple.

## Enter at the requested stage

| Request | Start here |
| --- | --- |
| Write captions or propose versions only | Adapt the supplied content; no account lookup or saved draft is needed. |
| Save a draft, post, cross-post, upload to a platform, or schedule | Resolve destinations and media, then prepare one saved post. |
| Change or resume an existing draft | Read it with `vidiq_social_post_draft_get`; preserve its `postId`. |
| Check delivery, find posts, or resolve a failure | Read [Delivery and recovery](references/delivery-and-recovery.md); use status or history without creating a draft. |

Inspect the exposed tools and their current schemas. Complete supported preparation if a needed
tool is missing, and identify the unavailable step. For changes to an existing YouTube video use
`vidiq-video-metadata`; for discovery use `vidiq-video-ideas` or `vidiq-shorts-inspiration` when
available. Research, scoring, clips, and new media are optional work driven by the request.

## Resolve the publication brief

1. Reuse the supplied content, destinations, tone, timing, and earlier choices. Ask together for
   missing information that changes the result. Interpret "everywhere" against connected accounts
   and show the proposed selection; it does not authorize posting to every account.
2. For a saved draft or publication, call `vidiq_social_account_list`. Use its exact
   `platformAccountId` values and `canPublish`; usernames and YouTube research IDs are not
   substitutes. Resolve multiple accounts on a platform before selecting one. A platform in
   `partial` has unknown connection state, not necessarily no accounts.
3. Offer connection or reconnection when needed. If already requested, use
   `vidiq_social_account_connect` for the supported social platform, or
   `vidiq_connect_youtube_channel` for YouTube. Show its authorization link or widget, wait for
   completion, then re-list accounts. Connecting an account does not publish anything.
4. For scheduled posts, resolve the actual date, local time, and timezone and retain the resulting
   timestamp with its offset. Ask about ambiguous times; do not invent a "best time". A series
   needs explicit occurrences within the requested horizon, not an assumed recurring automation.
5. Read [Platforms and media](references/platforms-and-media.md) for the selected destinations
   and any import. Reuse supplied YouTube privacy and TikTok choices; ask for missing ones.

Keep a private working brief in the conversation: source and library asset IDs, exact content and
settings per account, intended times, `postId`, `publicationId`s, latest `revision`, excluded
destinations, and what the creator approved. Update it after edits and results. Draft readback can
omit platform options and show only media counts; it cannot reconstruct the full brief. If context
is lost, identify missing settings or assets and resolve them before presenting a complete review.

## Adapt and prepare

Preserve the creator's meaning, factual claims, voice, and requested exact wording. When adaptation
is requested, make the opening, title, caption length, and call to action fit each destination and
the actual asset. Avoid adding unsupported claims, invented links, or boilerplate hashtags. Use
supplied evidence or inspect the source when necessary; mark missing context instead of describing
unseen footage. Explain material editorial changes briefly.

1. Import media once and reuse the returned IDs. Post media uses library IDs, not source URLs.
   A different caption needs no duplicate upload. Read the platform reference for asset variants.
2. Use `vidiq_social_post_draft_create` for one creative post with all its regular destinations.
   Set common text, media, and timing once; use destination overrides where they differ. Distinct
   posts in a series have distinct drafts. A platform-specific correction stays on the same post.
3. Inspect each destination's issue and saved state. `ready` means validation passed, not that
   delivery is guaranteed. Fix supported issues within scope with `vidiq_social_post_draft_update`.
   Stop when resolution needs the creator's choice or an external change; do not cycle through
   speculative edits. Explain any remaining refusal before proposing a smaller publish set.
4. For an edit, read the current draft. A supplied destination **replaces** that account's draft:
   send its complete intended settings from the brief, including fields the user did not change.
   Omitted destinations stay intact. Changing shared text or media requires resending every
   unpublished destination for validation, including one the creator intends to exclude.
5. A draft cannot lose a destination. Record exclusions and publish only the selected
   `publicationIds`. Discarding an unpublished draft means leaving it unpublished; do not claim
   it was deleted. Already scheduled or published destinations cannot be edited through draft update.

## Show the exact version for approval

Present the saved result in creator language, using a compact table or per-platform preview:

- Account and platform, final text, identifiable media and its order, and relevant settings.
- Immediate publication or exact date, local time, and timezone, with any YouTube native schedule.
- Each destination's quoted cost and the total for the proposed publish set; unresolved issues
  and excluded destinations. A quote is not a charge.

Use the working brief for settings absent from readback, and distinguish retained request values
from server-confirmed fields. Confirm discrepancies before publication. A schedule on a draft is
only a plan: say "draft for Tuesday", not "scheduled". Before scheduling, explain that scheduled
social posts currently cannot be cancelled or changed; the platform reference covers YouTube's
native-schedule exception.

Publish only the saved version the creator has seen and explicitly approved, including its
destinations, settings, times, and cost. The initial request to prepare or post content is not
approval of a subsequently produced draft. "So these are scheduled now?" is a status question.
An approval already given for this exact version remains valid; removing destinations in an
explicit "publish these only" instruction narrows it. Edits to content, settings, time, or cost
require review and approval of the revised version. Complete preparation before asking.

## Publish and report delivery

Call `vidiq_social_post_publish` with the approved `postId`, `revision`, and explicit
`publicationIds` for the approved set. Publish calls for the same post must be sequential. A stale
revision requires reading and reviewing the changed draft; do not simply substitute a fresh token.
On `verification_required`, show the returned YouTube verification step, wait for completion,
and resume the same approved call without another content approval.

Read [Delivery and recovery](references/delivery-and-recovery.md) before checking or recovering
publication. Report each destination's actual state and available link, with the next action for
anything unfinished. Keep successful destinations intact when another fails. A saved draft,
accepted publish request, scheduled post, and confirmed live post are different outcomes.
