# Pacing and platform limits

Read before a batch that puts several posts on one account within a day, when a draft returns
`pacing`, or when a destination fails on a platform limit. Platforms change these limits; the
numbers below are what each platform documented when this was written. Never present a number as
the creator's exact limit unless a tool result reports it.

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
vidIQ; posts made directly on the platform or through other apps also count toward its limits.

YouTube destinations are not paced. A YouTube publish time uses YouTube's native schedule: the
upload happens when the destination is published and the video goes public later, so spreading the
publish times spreads nothing YouTube counts against its upload limit.

## Batches

Publish a batch for one account in order, a few at a time, and check delivery before continuing.
When a destination fails with `limitReached` or a limit reason below, stop publishing to that
account: further attempts fail the same way. Keep the unpublished posts as saved drafts and tell the
creator when the remaining ones can go out.

## YouTube

[YouTube limits](https://support.google.com/youtube/answer/10383400) how many videos a channel can
upload in a 24-hour period across desktop, mobile, and the API. It publishes no number: the limit
varies by country or region and channel history, and Community Guidelines or copyright strikes
lower it. Channels with
[advanced features](https://support.google.com/youtube/answer/9890437) usually have higher limits.
Numbers quoted elsewhere, such as 15 a day, are not YouTube's.

**Before a batch.** Several videos to one channel in a day can reach the limit, and scheduling does
not avoid it. Offer to publish some now and keep the rest as saved drafts for later days; the creator
has to come back to publish them, because a draft's planned time does not publish it.

**When an upload hits the limit.** A YouTube destination whose `failureReason` mentions
`uploadLimitExceeded` hit the channel's daily upload limit, whether its `failureCode` is
`limitReached` or `rejected`. Do not change the content or create another post: the same video is
accepted once the limit allows it. Tell the creator that YouTube allows more uploads after 24 hours,
and publish the same destination again then.

For context, count the channel's uploads through vidIQ in the last 24 hours with
`vidiq_social_post_list` (platform YouTube, `from` 24 hours ago, statuses `submitted`, `inProgress`,
and `completed`; follow `nextCursor`). If the limit came after only a few uploads, the channel's limit
is probably low: suggest checking YouTube Studio > Settings > Channel > Feature eligibility
(<https://www.youtube.com/account_features>) and verifying identity to reach advanced features
([how](https://support.google.com/youtube/answer/9891124)), and mention that strikes also lower the
limit. Uploads made outside vidIQ count too, so present this as likely, not certain.

Keep three other YouTube conditions apart from this one:

- `verification_required` from `vidiq_social_post_publish` is vidIQ's own security check before a
  YouTube upload. Show its step, wait for it, and resume the same approved call; it is unrelated to
  YouTube's channel verification.
- A `failureReason` mentioning `quotaExceeded`, `rateLimitExceeded`, or `userRateLimitExceeded` is a
  temporary service-side limit, not the creator's channel. It is retried automatically; after
  `retriesExhausted`, publish the destination again later. Do not suggest channel verification for it.
- Videos longer than 15 minutes need a
  [verified channel](https://support.google.com/youtube/answer/71673); point to the same Feature
  eligibility page when a long video is refused.

## TikTok

- TikTok limits [direct posts](https://developers.tiktok.com/doc/content-sharing-guidelines) to a
  creator account in a 24-hour window, typically around 15 a day. The limit varies by creator and is
  shared with every app the creator posts through, so posts made elsewhere count.
- Delivery to the creator's TikTok inbox has its own limit: at most 5 pending shares in 24 hours.
  Pending shares are those the creator has not yet finished posting from the app.
- A failure or refusal naming `spam_risk_too_many_posts` is the creator's daily limit; one naming
  `reached_active_user_cap` is TikTok's daily limit on creators posting through this app. Both lift
  on their own: publish the same destination again the next day.
- "TikTok is not accepting posts from this account right now" without either code can mean the
  account is barred from posting. Ask the creator to check the TikTok app; do not retry repeatedly.

## Instagram

- Instagram limits each account to a number of
  [API-published posts](https://developers.facebook.com/docs/instagram-platform/content-publishing/)
  in a moving 24-hour window. Meta's pages give 100 in one place and 50 in others; plan around 50.
- A carousel counts as one post. The failure reason reports how much of the limit is used when
  Instagram returns it.
- After the limit, publish the same destination again once the window allows.

## Facebook Pages

- Meta documents no daily limit for regular Page posts.
- Page Reels are limited to 30
  [API-published Reels](https://developers.facebook.com/docs/video-api/guides/reels-publishing) in a
  moving 24-hour window.
- A failure saying Facebook is blocking posts to the Page is a restriction on the Page, not a limit
  that resets. Ask the creator to check the Page on Facebook.

## X

- X limits how many posts an account makes per day, with lower limits for accounts without Premium.
  The exact numbers change; see [X limits](https://help.x.com/en/rules-and-policies/x-limits).
- Apps are also limited to 100 posts per user every 15 minutes, and rate limits are retried
  automatically.
- X's rules forbid bulk or substantially similar posts. Space posts and vary repeated text, even
  under the limits.

## Bluesky

- Bluesky's [rate limits](https://bsky.network/docs/rate-limits) allow far more posts than a creator
  makes, around 1,600 an hour.
- Video posts have a separate daily limit with no published number, and need an account with a
  verified email. A video destination failing with `limitReached` hit that limit: publish it again
  the next day.

After any `limitReached`, retry only the failed destination by naming its `publicationId`, and only
once the limit has reset. Never create a new post to get around a limit.
