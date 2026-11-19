# Pacing and platform limits

Read before a batch that puts several posts on one account within a day, when a draft returns
`pacing`, or when a destination fails on a platform limit.

## Pacing advice on drafts

Draft create and update check each unpublished destination against the creator's other vidIQ
posts to the same account (published, scheduled, and dated drafts). A destination that crowds its
account returns `pacing` with a `reason` and a `suggestedPublishAt`:

- `too_close`: within minutes of another post to that account.
- `daily_limit`: more posts to that account in a day than is safe for the platform.

Pacing is advice. It does not change `ready`, refuse the draft, or move the time. Show it with the
review, and offer the suggested time; moving a destination's time changes the version and needs the
creator's approval. A null `suggestedPublishAt` means no free slot was found within a week: say so
and ask how to spread the posts rather than inventing a time. Pacing sees only posts made through
vidIQ; posts made directly on the platform also count toward its limits.

YouTube destinations are not paced. A YouTube publish time uses YouTube's native schedule: the
upload happens when the destination is published and the video goes public later, so spreading the
publish times spreads nothing YouTube counts against its upload limit.

## YouTube daily upload limit

YouTube limits how many videos a channel can upload in a day and publishes no exact number. Channels
with only standard features get a lower limit; channels with advanced features (phone verification
plus channel history or identity verification) get a higher one. Uploads made in YouTube Studio or
other apps may count toward it too.

**Before a batch.** When the creator wants several videos published to one channel, count that
channel's uploads through vidIQ in the last 24 hours with `vidiq_social_post_list` (platform YouTube,
`from` 24 hours ago, statuses `submitted`, `inProgress`, and `completed`; follow `nextCursor`). If the
count plus the batch is around 15 or more, explain that scheduling will not avoid the limit and offer
to publish part of the batch now and keep the rest as saved drafts to publish on a later day. The
creator has to come back to publish them; a draft's planned time does not publish it.

**When an upload hits the limit.** A YouTube destination whose `failureReason` mentions
`uploadLimitExceeded` hit the channel's daily upload limit, whether its `failureCode` is
`limitReached` or `rejected`. Do not change the content or create another post: the same video will
be accepted once the limit allows it. Count the channel's uploads through vidIQ in the last 24 hours
as above, then:

| Uploads through vidIQ in the last 24 hours | Most likely cause and what to tell the creator |
| --- | --- |
| Fewer than about 15 | The channel probably does not have advanced features yet, so its limit is low. Ask them to check YouTube Studio > Settings > Channel > Feature eligibility, or <https://www.youtube.com/account_features>, and complete phone verification and, if offered, identity verification. YouTube's guide: <https://support.google.com/youtube/answer/9891124>. Uploads made outside vidIQ may also explain the limit, so present this as likely, not certain. |
| About 15 or more | The channel used up its daily limit. Publish the failed destination again after 24 hours have passed since the earliest of those uploads, and spread the remaining videos across days. If this happens often, verification can raise the limit. |

YouTube's numbers are not published, so 15 is a working threshold rather than a documented one. Never
state an exact limit as fact.

Keep three other YouTube conditions apart from this one:

- `verification_required` from `vidiq_social_post_publish` is vidIQ's own security check before a
  YouTube upload. Show its step, wait for it, and resume the same approved call; it is unrelated to
  YouTube's channel verification.
- A `failureReason` mentioning `quotaExceeded`, `rateLimitExceeded`, or `userRateLimitExceeded` is a
  temporary service-side limit, not the creator's channel. It is retried automatically; after
  `retriesExhausted`, publish the destination again later. Do not suggest channel verification for it.
- Videos longer than 15 minutes also need a verified channel; point to the same Feature eligibility
  page when a long video is refused.

## Other platforms

Use each failure's `failureReason` and returned guidance first. These limits explain it:

| Platform | Limit to explain |
| --- | --- |
| Instagram | A limit on posts published through apps in a rolling 24 hours; the reason may report how much is used. Publish the failed destination again once the window allows. |
| TikTok | About 15 direct posts a day per creator, shared with every app the creator uses, so posts made elsewhere count. Spread the rest over the next day. |
| X | Bursts of similar posts can be throttled or treated as spam before any stated limit. Space posts and vary repeated text. |
| Facebook Pages, Bluesky | No small daily cap to plan around; follow the failure's reason. |

After any `limitReached`, retry only the failed destination by naming its `publicationId`, and only
once the limit has reset. Never create a new post to get around a limit.
