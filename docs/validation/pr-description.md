# PR description authoring validation

Date: November 20, 2026.

Method: synthetic drafting walkthroughs by the skill author in Codex. These are illustrative outputs and self-review, not independent behavioral tests, real runtime checks, or installation tests. All tickets, commands, paths, and evidence URLs below are fictional fixtures. No live PR/MR was modified.

## Scenarios defined before authoring

| Scenario | Supplied context | Acceptance criteria |
| --- | --- | --- |
| Frontend with template | Template headings `Request`, `Notes`, `Validation`; ticket UI-12 asks that declined payments remain editable; attached design explicitly requires focus to return to payment method; implementation note records that an existing focus helper also handles keyboard navigation; screenshot at a local fixture path; recorded browser check for the current revision; target host cannot embed local files or render Mermaid | Preserve headings; explain motivation and behavior; use the note as a bullet; reference recorded check without claiming to run it; disclose unattached screenshot; use prose instead of an unsupported diagram |
| Backend without template | Ticket API-8: callers retry timed-out requests and create duplicate jobs; attached request contract requires retries to return the existing job; diff implements idempotency-key lookup; commit history agrees; current recorded check passes and names a rerunnable script; no implementation discoveries recorded | Explain why and result; omit insights; concise command/reference; no diff inventory, invented discoveries, or redundant coverage section |
| Unresolved why and no evidence | Conversation says only “describe this PR”; diff changes token lifetime from 30 to 10 minutes; ticket attachment is inaccessible; commit says “adjust expiry”; no evidence or insights | Ask focused motivation question; still return a draft limited to known behavior; mark inaccessible intent and missing evidence; do not run checks or claim security benefits |
| Stale and failed evidence | Template headings `Summary`, `Discoveries`, `Tests`; required `Tests` contains an unchecked “regression passes” box; timeout fix at revision B; regression failed at revision A; old note says “the global clock also drives leases”; no checks at B | Keep headings and box unchecked; discoveries as recorded bullet; distinguish old failure and current evidence gap; do not convert failure into current success |
| Publishing unavailable | User explicitly says “update MR 42’s description”; template and current description available; existing description includes a still-relevant deployment caveat; evidence supplied; no authorized write tool available | Return a finished draft preserving caveat; explain no publication occurred; no fake URL or unrelated side effects |

## Results

The following drafts were manually composed against the skill and the fixtures above, then checked against the acceptance criteria. They demonstrate intended application; they do not measure how another agent follows the skill.

### 1. Frontend with a template

Draft:

```markdown
## Request

After a declined payment, customers need to correct their payment method without restarting checkout. The form keeps their input and returns focus to the payment method, as required by UI-12’s attached design.

## Notes

- The existing focus helper also handles keyboard navigation; the change reuses it.

## Validation

Recorded browser check for this revision: decline → edit payment method → resubmit completed successfully. The captured screenshot has not been attached; visual evidence is unavailable to reviewers here.
```

Author note outside the body: the existing screenshot is at the supplied local fixture path `artifacts/declined-payment.png`; this host cannot upload it. No Mermaid diagram is added because the host cannot render one and the prose is sufficient.

Self-review: template headings retained; insight is a recorded bullet; no screenshot capture, upload claim, or new verification. The body makes the missing visual evidence clear.

### 2. Backend without a template or insights

Draft:

```markdown
## Context

Callers retry job creation after a timeout and can create duplicate jobs. To satisfy API-8’s request contract, retries using the same idempotency key now return the existing job.

## Evidence

Recorded retry check passed for the current revision: repeated requests returned the same job ID. Rerun: `python scripts/check_job_retry.py`.
```

Self-review: the command is part of this fictional fixture, not a command discovered or executed in DecodedSkills. No insights or coverage section was generated. The why and resulting behavior are explicit without enumerating files.

### 3. Unresolved why and missing evidence

Question outside the body: “What requirement motivates reducing token lifetime to 10 minutes? The ticket attachment is inaccessible.”

Provisional draft:

```markdown
## Context

Token expiry changes from 30 to 10 minutes. The motivating requirement remains unconfirmed because the linked ticket attachment is inaccessible.

## Evidence

No verification results were available for this change.
```

Self-review: a draft is still supplied alongside the question. It does not invent a security benefit, claim tests passed, or run checks. The unresolved rationale is visible to a reviewer.

### 4. Stale failure and required sections

Draft:

```markdown
## Summary

This change addresses the reported timeout. Verification of revision B remains outstanding.

## Discoveries

- The global clock also drives leases, as recorded during implementation.

## Tests

- [ ] Regression passes

The recorded regression failed at revision A. No result was recorded for revision B; the earlier failure does not establish the current outcome.
```

Self-review: the required headings and unchecked box remain; the recorded failure was not concealed or converted to a pass. The discovery remains a bullet. Motivation is limited to the reported timeout in the fixture.

### 5. Publishing requested without hosting tools

Suppose MR 42’s template requires `Context` and `Evidence`, and its existing caveat states that workers must drain before deployment.

Final draft:

```markdown
## Context

Retries after a request timeout can create duplicate export jobs. Requests with the same idempotency key now return the existing job.

Deployment caveat: workers must drain before deployment.

## Evidence

The recorded retry check passed for the current revision and returned the same job ID for repeated requests.
```

Author response outside the body: “MR 42 was not updated because no authorized hosting write tool is available. Here is the draft.”

Self-review: the existing caveat is preserved. No successful publication, read-back, or URL is fabricated. A real update would require inspecting the actual body and supplied evidence rather than reusing this fixture.

## Actual structural checks

- `python3 scripts/validate.py`: passed; one plugin, one skill.
- Skill creator’s `quick_validate.py plugins/engineering/skills/pr-description`: passed.
- `claude plugin validate .`: marketplace passed.
- `claude plugin validate plugins/engineering`: passed and listed `engineering:pr-description`.
- Native validator version: Claude Code 2.1.329.
- `git diff --check`: passed.

The plugin validator reported the existing missing listing icon warning and advice to add a one-step install command in the plugin README. These are nonblocking listing suggestions. No icon or new host-specific command was added for this skill change.

## Limits

No live installation, independent behavioral evaluation, browser run, screenshot capture, external ticket retrieval, or PR/MR publication was performed. Codex/Cursor installation and end-to-end tool behavior remain untested. Structural discovery in Claude’s validator is not a runtime skill invocation.


## Independent review and corrections

A fresh read-only reviewer checked the skill, examples, documentation, and this record against the approved design and plan. This was an independent document review, not an independent execution of the skill.

Two findings were corrected:

- “Create a description for PR 42” was potentially ambiguous publication authorization. The skill now explicitly treats this as a draft and requires an explicit request to apply text remotely. Manual contrast check: “create a description for PR 42” → draft; “publish this description to PR 42” → authorized description write, subject to tool availability.
- The template example described a successful browser flow without supplying that recorded check in its fictional inputs. The inputs now explicitly include the recorded browser result. Manual provenance check: the example’s success statement is supported by a stated fixture result, not inferred from screenshots.

The author checked both corrections and reran structural validation. No live publication or runtime verification was used to resolve them.
