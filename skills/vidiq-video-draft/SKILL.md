---
name: vidiq-video-draft
description: Build a full draft of a video before it is filmed (script in the creator's own voice, a voice reading it, stock or generated pictures, graphics, captions), judge it against what works in the niche, fix it while changes are cheap, then hand over a timed filming script and put the real take in. Use when asked 'edit my video before I film it', 'make a mock-up or animatic of this script', 'draft this video with a voiceover', or 'I filmed it, swap my footage in'. Every paid step is quoted and approved first. To post the finished video, use vidiq-publishing.
---

# vidIQ Video Draft

Read [Live surface notes](references/live-surface-notes.md) first, even when using only supplied evidence.

Build the whole video as a draft, judge and fix it while changes are cheap, then film to the
script and replace the placeholder pictures with the real take.

## Enter at the requested stage

| Request | Start here |
| --- | --- |
| An idea, topic, or script, nothing filmed | Write the script, then continue in order. |
| A draft to judge or fix | Judge the draft, from its job ID or `videoUrl`. |
| A filmed take for an existing draft | Read [Film and swap](references/film-and-swap.md). |

Use live tool schemas. If a tool is missing, complete the stages that remain and name the gap.
Read [Job lifecycle](references/job-lifecycle.md) before the first asynchronous call.

## Agree on spending first

Each tool's live description ends with its current cost; `vidiq_balance` gives the balance.
Voiceover is priced by script length, `vidiq_compose` and `vidiq_motion_graphics` by seconds of
output, watching per video, generated images and clips per item. Before each paid step say what
it does and what it costs, and estimate the whole draft up front. Start a paid step only when the
creator asked for it; approval of one render does not cover the next.

## Write the script

1. Call `vidiq_before_scripts_outlines_and_edits` with the creator's `request` verbatim, plus
   `task` (`full_script` or `short`), `durationSeconds` with `durationKind`, `language`, and
   `channelId` when stated. Follow the returned `writingGuidance`, `creatorContext`, and
   `voiceSamples`, keep to `lengthBudget`, and write the script yourself. When no saved voice or
   samples come back, ask for a past video or a sample of how the creator talks.
2. Write one line per beat: one thought, one picture. Keep within the live limits of
   `vidiq_voiceover_generate` `scriptLines` and of `vidiq_compose` scenes and total length; draft a
   longer video in parts.
3. Get the script approved before paying for a voice.

## Give it a voice

1. Call `vidiq_voiceover_list_voices` with the script's `language`. Voices with `isCustom: true`
   are the creator's own; prefer them. Otherwise offer two or three stock voices that match the
   language, with each `previewUrl`.
2. Offer cloning only when `vidiq_voiceover_clone` or `vidiq_voiceover_clone_start` is in the live
   tool list, and only with the speaker's explicit consent. Claude apps do not list them: there,
   never promise cloning; use a stock voice, since the filmed take carries the real one.
3. Call `vidiq_voiceover_generate` once with the `voiceId` and the lines as `scriptLines` (never
   together with `script`). The result's `lines` give an `audioUrl` and `startSeconds` per line;
   the top-level `audioUrl` is the whole narration. These times drive every later stage. Where
   `scriptLines` is not offered, pass `script` and label each line's time as an estimate.

## Add pictures and motion

Give each line one picture that lasts as long as the line:

- `vidiq_find_broll` with `query`, `orientation`, and `minDurationSeconds`. Keep the photographer
  credit and source page; attribution is required.
- `vidiq_motion_graphics` (`root`, `durationSeconds`, `outputPreset`) for a number, list, or
  comparison that words alone carry badly.
- `vidiq_image_generate` (`images`, `aspectRatio`) or `vidiq_generate_video` (`prompt`,
  `resolution`, `duration`) only where stock cannot show it. These cost the most; ask first.
- For a line the creator will say on camera, use a plain placeholder and mark the scene to film.

Keep a working sheet: per line its words, start, seconds, source URL, credit, graphics, and
whether it is to film. The server does not keep the composition, so every re-render sends it whole.

## Assemble the draft

Call `vidiq_compose` with `format`, the ordered `scenes` (`source`, `type`, `duration`, and
`startFromSeconds` to trim in), and `voiceover.audioUrl`. Place graphics as scenes or as `overlays`
of `kind: "video"`. Make scene durations cover the narration. Leave `captions` out so the narration
is captioned automatically; pass a `style` only for a requested look, and add no text overlays that
repeat the narration. Poll, share the `videoUrl`, and read the result's caption outcome: when
captions were not added, say so instead of repeating the paid render.

## Judge the draft

Read [Judge the draft](references/judge-the-draft.md). It compares countable things (when the hook
lands, words per second, how often the picture changes, where a graphic would help) against two or
three outliers from the niche, quotes the cost of watching first, and carries on when the draft
file itself cannot be watched.

## Fix and re-render

Group the agreed fixes into one render and quote it. A changed line needs a new narration for the
whole script; a changed picture or timing needs only a new `vidiq_compose` call. Where
`vidiq_review_open` is listed and the client shows its player, offer it for notes pinned to a
moment: pass the draft's `mcpJobId`, wait until the creator says they are done, read
`vidiq_review_notes` with the `reviewId`, and add each re-render as the next version by passing its
`mcpJobId` with that `reviewId`. Elsewhere, take notes as timestamps in chat. The player collects
the creator's notes; it does not judge the video. Repeat until the creator is happy.

## Hand over the filming script

Return every line with its number, start time, seconds, words, what is on screen (creator on
camera, or a picture under their voice), and any delivery note, plus the total length and the
draft's words per second to match. Ask the creator to film in script order, pause between lines,
and repeat a spoiled line whole.

## Swap in the take and publish

When the take exists, read [Film and swap](references/film-and-swap.md). To post the final
`videoUrl`, switch to `vidiq-publishing` when available; titles and thumbnails belong to
`vidiq-packaging-studio`.

## Deliver

Return the current `videoUrl`, job IDs, the working sheet, charges as returned, stock credits,
and what stayed unverified: a draft nobody watched, missing captions, or estimated timings.
