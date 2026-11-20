# Description examples

These are fictional examples of writing choices, not fixed wording or proof. Repository templates take precedence over these headings.

## Explain behavior and why

Available records: ticket says client retries create duplicate export jobs; implementation adds idempotency-key lookup; a current recorded check passed; no implementation insights were recorded.

```markdown
## Context

Clients retry exports after a timeout and can create the same job twice. Retrying with the same idempotency key now returns the existing job instead of creating another.

## Evidence

Recorded retry check passed for this revision: repeated requests returned the same job ID. Rerun: `python scripts/check_export_retry.py`.
```

Only name that command if it exists in the inspected project. There is no insights section because none were recorded. The description does not list modified files or repeat a coverage report.

## Fit the repository template

Template requires `Request`, `Notes`, and `Validation`. A recorded discovery says an existing focus helper also handles keyboard navigation. Existing before/after screenshots are already hosted. A browser check recorded during implementation confirms that the decline → edit payment method → resubmit flow completed successfully.

```markdown
## Request

After a declined payment, customers need to correct their payment method without restarting checkout. The form now keeps their input and returns focus to the payment method.

## Notes

- The existing focus helper also handles keyboard navigation; the implementation reuses it.

## Validation

Recorded browser check: decline → edit payment method → resubmit completed successfully.

[Before screenshot](EXISTING_BEFORE_ATTACHMENT_URL) · [After screenshot](EXISTING_AFTER_ATTACHMENT_URL)
```

Replace illustrative URL labels only with actual existing attachments or confirmed authorized uploads. A local screenshot is not a hosted attachment. If it cannot be attached, state that limitation in the body and give the author the local reference separately.

## A useful draft despite missing evidence

Available records: token expiry changes from 30 to 10 minutes, ticket rationale cannot be accessed, and no verification results were recorded.

Question outside the description: “What requirement motivates the shorter token lifetime? The linked ticket attachment is inaccessible.”

```markdown
## Context

Token expiry changes from 30 to 10 minutes. The motivating requirement is unconfirmed because the linked ticket attachment is inaccessible.

## Evidence

No verification results were available for this change.
```

Do not invent a security rationale, claim tests passed, or run verification to fill the gap. Update the draft when the missing context becomes available.
