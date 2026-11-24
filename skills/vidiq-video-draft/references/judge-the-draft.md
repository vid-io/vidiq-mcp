# Judge the draft

Read this before comparing a draft with videos from the creator's niche.

## Count the draft first

The working sheet already holds the draft's numbers, exactly and at no charge:

- **Hook:** the second at which the opening promise is complete (the end of that line).
- **Pace:** words spoken divided by narration seconds.
- **Picture changes:** seconds per scene, on average and for the longest hold.
- **Graphics:** how many, and at which seconds.
- **Length:** total seconds.

## Find two or three references

Search with `vidiq_outliers` using the niche as `keyword` and `contentType` (`short` or `long`)
matching the draft; narrow with `publishedWithin` or `language` when needed. For a draft meant
for Reels or TikTok, use `vidiq_instagram_tiktok_outlier_search` with `query` and `audienceQuery`.
Read [Discovery evidence](discovery-evidence.md). Choose two or three results from different
channels that match the draft's format and length. Reuse references the creator already supplied.

## Quote the watching, then watch

Watching is paid per video. Before any watch call, state how many videos will be watched, the
cost of each from the live tool descriptions, and the total; wait for a yes. Read
[Job lifecycle](job-lifecycle.md) before submitting.

- Shorts, Reels, and TikToks: `vidiq_watch_shortform_content` with the full public `url`.
- Long videos: `vidiq_video_watch` with `video`.

Pass the same `prompt` to each, asking for the countable things: the second the hook's promise is
complete, each picture change with its timestamp, each on-screen graphic or text with its
timestamp, the number of words spoken, and the length. Submit the references together and poll
each job. A pending or failed watch establishes nothing; do not fill its numbers in.

## Watch the draft itself, when the account can

The numbers above do not show how the draft looks. To check that, call `vidiq_video_watch` with
`videoUrl` set to the draft's `videoUrl` (and no `video`), with a `prompt` asking for pictures
that do not match the words, unreadable text, and captions that cover something. Quote this
watch with the others.

Some accounts can only watch YouTube videos. A refusal with `file_source_unavailable` costs
nothing: do not retry it or route around it. Carry on with the counted numbers, say that nobody
has checked how the draft looks, and ask the creator to watch it, in the review player where it
is offered.

## Compare and recommend

Show one table: each measure, the range across the references, the draft's value, and the
change proposed. Then list where a reference used a graphic and the draft shows plain footage at
the same kind of moment.

Two or three references guide a choice; they do not prove a rule. Name the references, keep
their numbers apart from judgment, and adapt structure, never wording or visuals. Propose only
fixes tied to a line or a second of the draft, strongest first, and let the creator choose which
to apply.
