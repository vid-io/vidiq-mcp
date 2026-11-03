# Claude-native review

Use only when the current host exposes native artifact creation, asset upload, and saved-data
reads/writes. These capabilities were observed in Claude Desktop Code mode, not established for
regular chat. Never require a silent mode switch or describe a fallback as native success.

Copy `assets/video-review.html` from this skill into the working directory. It is a self-contained
vidIQ-styled player for the host-provided `claude` runtime, not an MCP Apps widget. Read the current
host capability documentation before publishing. The tested runtime exposes `claude.use("db")`,
`claude.use("user")`, asset playback at `/_blob/<assetId>`, native `Artifact` asset publication and
agent `ArtifactData` reads. Use actual available tools rather than guessing their names or schemas.

Upload only the requested video to the new artifact. Probe metadata with an available tool;
never assume 30 fps. The observed native asset cap was 20 MiB per file; obey live limits. Preserve
the original and offer another supported media path if it exceeds the cap. Never embed private
notes or signed URLs into public page source to bypass saved-data permissions.

Register a `videos/<stableVersionId>` document with `assetId`, positive `fps`, `frames`, `order`,
`label`, `width`, `height`, `bytes`, `codec`, and optional `parentVersionId`. Only use frame labels
for a known constant frame rate; disclose VFR as unsupported for exact frames. The template reads
versions by order. Notes live in `videos/<versionId>/notes/<stableNoteId>` and include source asset,
version, fps, start frame/time, exclusive end frame/time, text and creation time. Read exact records
through the native saved-data tool after the user finishes; do not infer persistence from the UI.

Upload v2 as a new full asset with its own version document and parentVersionId. Old notes remain
source anchors; selecting one opens the parent. If an edit removes a source span, report that
mapping separately. Page publication versions and media versions are different counters.

Verify playback, five notes (two ranges), reload/readback, keyboard single-save behavior, and a
v2 upload before claiming a working loop. requestVideoFrameCallback samples can check presentation,
but currentTime, a counter, known constant fps, or ffprobe frame count alone cannot prove
decoded-frame accuracy. Do not describe the player as frame-exact on metadata evidence alone. Native public viewing and
saved-data permissions differ; do not promise outside-organization writes or signed-out notes.
