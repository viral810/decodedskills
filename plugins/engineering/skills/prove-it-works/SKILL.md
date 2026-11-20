---
name: prove-it-works
description: Verify an implemented change against its intended behavior, run focused checks, and report evidence and remaining gaps before claiming completion.
---

# Prove It Works

Establish which completion claims the available evidence supports. Use this after implementing a change or when asked to verify existing work. A verification request alone does not authorize implementation changes, deployment, or publication.

## Define the claim

Read the request, applicable repository instructions, and the current artifact or diff. Identify the behavior that matters to the user and the revision or local state under examination. Inspect work supplied by another agent as you would any other change; its summary is a starting point for investigation.

Translate each material claim into a check with an observable expected result. Prefer a small set of checks that would expose a plausible defect over a long list of commands. Resolve routine choices from the repository; ask only when ambiguity changes what success means, while continuing checks that do not depend on the answer.

For example, “retries do not create duplicate jobs” calls for repeating a request with the same key and observing the returned job identity and stored job count. A successful HTTP response alone leaves the duplicate-job claim unresolved.

## Choose evidence that answers the claim

Read existing test commands and relevant checks before running them. Follow required repository checks and add focused verification where they leave the changed behavior unobserved. Match the method to the claim:

| Claim | Useful observation | Limit to preserve |
| --- | --- | --- |
| A defect is fixed | Exercise the reported trigger and compare the result with the requirement; where practical, show that the same check detects the defect in the earlier implementation | A passing case that never triggers the defect provides weak regression evidence |
| A user flow works | Perform the relevant interactions and inspect the resulting visible state and any required persisted effect | A screenshot establishes appearance at one moment, not the whole interaction |
| An integration works | Send a representative input across the changed boundary and inspect the receiving system's result | A mock can establish local behavior but leaves the actual connection untested |
| Output is correct | Open the produced file or read the resulting value and compare it with the expected content | Successful generation does not establish correctness or usability |
| Performance improved | Measure comparable workloads under stated conditions against a baseline | One faster sample does not establish a reliable improvement |
| Packaging is valid | Run the package checks and inspect the discovered contents | Structural acceptance does not establish installation or runtime behavior |

For a small prose or configuration change, direct inspection and an appropriate validator may be sufficient. Do not require a browser or an end-to-end suite when it cannot answer the relevant claim. Reuse existing checks; add a repeatable test or script when it provides lasting regression value, rather than creating permanent scaffolding for every check.

## Run and interpret

Use the available shell, test runner, browser, application, or connected service as needed. No particular provider is required. If a capability, credential, or environment is unavailable, perform the useful accessible checks and identify the observation that remains missing. Give a concrete next check without claiming it ran.

Use local fixtures or isolated test environments for checks that create data. Stay within the task's authorization; if proof requires a purchase, deployment, message, destructive operation, or other unapproved external effect, stop before that action and explain what access or approval is needed. Do not treat verification as permission to change production state.

Compare observed results with the expected outcomes, including relevant errors and exit status. A command that started, a test file that exists, or an old passing result does not establish the current outcome. Confirm that the exercised instance or generated artifact corresponds to the state being verified when stale builds or multiple instances could affect the result.

When a check fails, distinguish an observed product failure from a broken check or unavailable environment using the output and a focused diagnostic. Keep unresolved failures visible. Do not repeat a failing command until it happens to pass or silently weaken its expectations. If fixing the issue is already authorized, make the focused correction and rerun affected checks and required repository validation. Otherwise report the finding. After any further edits, reassess which results still apply.

Stop when the material claims have evidence and required checks have completed, or when a remaining gap requires unavailable access or a user decision. Broaden verification only when the change, a failure, or a new finding gives a concrete reason.

## Report the evidence

Lead with the supported outcome: verified for the stated scope, a demonstrated failure, or partial verification with a named gap. Keep the report proportional to the work. Include:

- The behavior or artifact checked and the relevant revision or local state.
- The actual command or interaction, expected result, and observed result. Link useful existing logs, screenshots, or output files without exposing secrets.
- Failed, skipped, or unavailable checks and how they limit the conclusion. Distinguish checks you executed from supplied results or manual inspection.

For example: “The local retry check returned the same job ID twice and found one stored job. The live service was unavailable, so remote idempotency remains unverified.”

Keep evidence available for review using the host's supported artifact paths or links. Do not invent attachments or add generated logs to version control unless the task calls for them. This report can supply evidence to a separate PR-description workflow; it does not publish or update a PR/MR.

## Inspiration

Inspired by pstack's [Prove It Works principle](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-prove-it-works/SKILL.md), by [poteto](https://github.com/poteto). These instructions are independently authored around claim selection, proportional checks, and explicit limits on the resulting evidence.
