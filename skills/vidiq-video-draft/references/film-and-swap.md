# Film and swap

Read this when the creator has filmed the script and wants the take in place of the draft's
placeholder scenes.

## Bring the take in

Importing costs no credits. Use the route the client supports:

- **Chat app that shows widgets:** call `vidiq_file_upload` to show the picker, reply briefly, and
  wait. Pass each finished video's `uploadId` to `vidiq_video_upload` to get its `videoUrl`.
- **Terminal with shell access on the machine holding the file:** call `vidiq_video_upload` with
  `localFile` (`path`, `sizeBytes`, `contentType`), run the returned `command`, then call again
  with the `uploadId` until `status` is `ready`.
- **A public link:** call `vidiq_video_upload` with `url`.

Chat apps refuse `localFile`; follow the alternative the refusal names. Read the take's length
and frame size with `vidiq_media_file_info` (`sourceUrl`).

## Prefer better options when the tool list has them

Before the manual route below, read the live tool list, the `op` values of `vidiq_edit_media`,
and the inputs of `vidiq_compose`. Where they offer a way to read the words spoken in an uploaded
file, cut several ranges in one call, caption a clip's own sound, or rebuild from an earlier
composition, use it in place of the matching manual step, following its live description and
cost. Use only what the live schema shows.

## Find each line in the take

Each line needs the start and end of its last clean reading.

1. Where files can be watched, offer `vidiq_video_watch` with `videoUrl` set to the take and a
   `prompt` that numbers the lines by their first words and asks for those times and for spoiled
   readings. Quote its cost first. A refusal with `file_source_unavailable` costs nothing.
2. Otherwise ask the creator for the times, or for one uploaded file per line or section.

Never guess a time. Show the list and let the creator correct it before rendering.

## Put the take in place

Rebuild the composition from the working sheet; the pictures, graphics, and order stay.

1. Retime first. The creator's readings differ in length from the draft voice, so recompute each
   scene `duration` and each overlay `start` and `duration` from the take's line times.
2. For each scene marked to film, set `source` to the take's `videoUrl`, `type: "video"`,
   `startFromSeconds` to the line's start in the take, `duration` to its spoken length, and
   `keepNativeAudio: true`. `vidiq_compose` trims in by itself; use `vidiq_edit_media` with
   `op: "trim_media"` (`sourceUrl`, `startSeconds`, `endSeconds`) only when a separate file is
   needed, since each trim is a paid edit.
3. Where a picture or graphic plays under the creator's voice, keep the take as one scene with
   `keepNativeAudio: true` and lay the picture over it as an overlay of `kind: "video"` or
   `"image"`. Do not split the take to make room. Video overlays are always muted.
4. Remove the draft `voiceover` once the take carries every line. One composition holds one
   `voiceover`, so ask the creator to film or cut any line they skipped.
5. Captions come from a `voiceover` track. Unless the live schema says otherwise, the take's own
   sound is not captioned: say so before rendering, and offer line-by-line captions as overlays
   of `kind: "text"` timed from the take's line times, within the overlay limit.
6. On request, even out the take's loudness first with `op: "normalize_loudness"` and
   `targetLufs`; it is a paid edit.

Quote the render, call `vidiq_compose` once, poll it, and read the caption outcome. Return to the
review and fix loop for the creator's notes on the real footage.
