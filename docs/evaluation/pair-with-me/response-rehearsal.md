# Response rehearsal: ordinary assistance versus minimal candidate

This is a same-session author walkthrough, not fresh model trials. Both columns were authored by the skill's author with knowledge of the research, scenarios, and measured results. The baseline is an ordinary-assistant-style comparator, not an observed output from an independently invoked ordinary assistant. This comparison can expose missing instructions, but cannot measure a treatment effect or establish superiority. It is included to make the design comparison reviewable rather than imply that an unavailable experiment ran.

## Minimal candidate

> Frame the engineering decision using actual project constraints. Identify why the proposal could work and its consequential uncertainty. Consider a credible alternative and what would disprove your preferred option. Research disputed facts and test material choices with comparable inputs. Tie objections to mechanisms and evidence; distinguish risks from defects. Ask only questions whose answers could change the recommendation. Recommend from observations, update when evidence changes, and agree when warranted. Leave unresolved priorities to the user. Stop when further investigation is unlikely to change the decision; report remaining gaps.

The shipped skill expands this prototype with tool fallbacks, authorization boundaries, evidence reporting, and examples. Those additions were inspected, not ablation-tested.

## A: Flawed proposal

**Ordinary-assistant-style response:** Do not ship the check alone. Two requests can both observe no row and then insert. Add a unique constraint on the tenant and request key, handle the conflict by returning the existing job, and test overlapping retries. A local lock may not cover every writer.

**Candidate-guided response:** Reject the current design for the at-most-one-row requirement. Two autocommit connections both read no row, then inserted IDs 1 and 2 in the executed schedule. A non-null unique `(tenant, request_key)` constraint rejected the second insertion and allowed the same key for another tenant. Prefer database enforcement and resolve the duplicate conflict by reading the existing job. The experiment establishes stored-row deduplication, not exactly-once external effects; there are none in this scenario. A lock adds coordination without being necessary for the stated invariant. Stop after the persistence invariant is demonstrated; error-handling integration still needs testing in the application.

**Comparison:** Both identify the actual failure and a suitable alternative. The candidate rehearsal connects the recommendation to observations and bounds the claim. This does not demonstrate that the skill caused the difference; the baseline could perform the same experiment.

## B: Sound proposal

**Ordinary-assistant-style response:** Yes. Use the bound parameter for the name value; it treats apostrophes and SQL-looking input as data. Keep the fixed query and add focused cases for quoted and unknown names. This change does not require replacing the database abstraction.

**Candidate-guided response:** Agree for the stated literal-lookup requirement. In the executed fixture, binding returned the correct record for `O'Brien`, returned no record for `' OR 1=1 --`, and preserved normal and missing-name behavior. Interpolation produced a syntax error for the apostrophe and returned every record for the injection-shaped input. Keep the abstraction and bind the value. These four cases support this fixed query; they do not audit other queries. There is no consequential reason here to demand an ORM replacement or introduce an authentication redesign.

**Comparison:** Both accept the sound proposal without inventing blockers. No correctness improvement is established. The candidate gives a bounded evidence report; a shorter ordinary answer may be sufficient for such a small change.

## C: Ambiguous tradeoff

**Ordinary-assistant-style response:** An index is likely useful for repeated tag lookups, with some storage and write overhead. Measure the representative workload and ask about latency and storage targets before making the long-term choice.

**Candidate-guided response:** For the supplied read workload, provisionally add the tag index if another 320 KiB is acceptable. Across five local repetitions, median time for 400 lookups was 266.080 ms without the index and 2.826 ms with it; both returned identical IDs. Median batched insertion of 1,000 rows was 1.513 versus 1.813 ms. Database size before inserts was 2,007,040 versus 2,334,720 bytes. Query plans changed from a table scan to an index search. These are small warm local measurements, not production capacity estimates. What storage budget or future write requirement would make that measured read benefit insufficient? Preserve that priority decision for the owner. More generic database research is unlikely to settle it.

**Comparison:** Both recognize the tradeoff; the candidate rehearsal supplies a measured conditional recommendation. Baseline access to the same evidence could yield the same answer. The current experiment cannot decide the user's acceptable storage cost or future workload.

## What this rehearsal changed

Retained explicit permission to agree and stop, since B needs neither an invented objection nor an architectural alternative. Retained the distinction between an observed failure and a hypothesis, since A has a concrete failing schedule. Retained user control over priorities, since C has measurable consequences without a supplied utility function. These are author design judgments supported by the exercises, not statistically estimated prompt effects.
