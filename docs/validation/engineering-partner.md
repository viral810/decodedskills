# Engineering Partner authoring validation

Date: November 26, 2026.

## Scope and verdict

Implemented the portable [engineering-partner skill](../../plugins/engineering/skills/engineering-partner/SKILL.md), informed by [primary research and firsthand engineering practice](../../plugins/engineering/skills/engineering-partner/references/research.md). Fourteen research entries document findings, contrary evidence, adopted practices, and inference limits.

The skill and package pass structural checks. Executed synthetic engineering experiments support the recommendations below. A same-session response rehearsal compares a minimal candidate with ordinary-assistant-style responses, but an independently executed ordinary-assistant versus skill trial has **not** been performed. Host installation, automatic selection, and end-to-end pairing remain unverified. Do not describe these results as evidence of improved model accuracy or developer productivity.

The author used this Codex session; a precise underlying model/build identifier was not recorded. Session instructions prohibit sub-agents. No extra model processes or hidden service calls were used to bypass that boundary. Existing unrelated edits in the root README were preserved.

## Executed engineering experiments

Command, from the repository root:

```sh
python3 docs/evaluation/engineering-partner/experiment.py
```

The dependency-free Python 3.11+ script creates temporary SQLite databases, prints JSON, and removes its databases. It performs no network requests or live-service writes. [Saved results](../evaluation/engineering-partner/results.json) contain the actual run, including all performance samples and query plans. A rerun produces new timings; do not expect byte-for-byte identical JSON.

Environment recorded by the run: Python 3.13.5, SQLite 3.49.1, macOS 26.7.3 on arm64.

| Scenario and criterion | Observation | Supported recommendation |
| --- | --- | --- |
| A: at most one stored job for overlapping retries with the same non-null tenant/key | Both connections observed no row. Without a constraint both inserted, producing IDs 1 and 2. With a scoped unique constraint the second insert was rejected and only ID 1 remained. Another tenant could insert the same key. | Reject check-then-insert alone. Prefer database uniqueness for this database-only invariant, with application conflict handling. |
| B: fixed query must match names literally | Bound values handled normal names, `O'Brien`, injection-shaped text, and missing names correctly. Interpolation errored on the apostrophe and matched both rows for the injected condition. | Accept parameter binding; no evidence justifies replacing the abstraction for this requirement. |
| C: compare an index with a scan on the supplied workload | Identical lookup results in all five repetitions; query plan changed from `SCAN events` to a covering-index search. | Prefer the index for the supplied read workload if its measured storage cost is acceptable; leave that priority to the user. |

### Index measurements

Each repetition starts with 20,000 records, 997 possible tags, 80-character bodies, 400 seeded tag lookups, and 1,000 batched inserts. Variant order alternates across five repetitions. Each database uses DELETE journaling and FULL synchronous mode, with ten warmup lookups. Read time includes result fetching; insertion time includes the transaction commit. Database sizes below are before inserts and exclude temporary journal space.

| Median across five repetitions | Scan | Index |
| --- | ---: | ---: |
| 400 lookups | 266.080 ms | 2.826 ms |
| 1,000 inserts in one batch | 1.513 ms | 1.813 ms |
| Database size before inserts | 2,007,040 bytes | 2,334,720 bytes |

The extra index consumes 327,680 bytes (320 KiB). Read gains are large in this fixture; millisecond-scale insert differences are noisy and should not be used as a stable write-penalty estimate. Index construction time and migration locking are excluded. Cache state, hardware, cardinality, data growth, and transaction shape can change results. This is not a production SLO or durability benchmark.

The race experiment forces one valid interleaving, rather than estimating a failure frequency under load. It demonstrates the supplied autocommit design's failure mechanism and unique-constraint enforcement, not crash recovery, multi-system transactions, or external exactly-once effects. Constraint errors still need appropriate application behavior. The lookup experiment tests four fixed-query cases, not a security audit.

## Response comparison and evaluation limits

See the exact [scenario inputs](../evaluation/engineering-partner/scenarios.md) and [minimal candidate plus response rehearsal](../evaluation/engineering-partner/response-rehearsal.md). The rehearsal is authored, unblinded, and contaminated by prior knowledge. It is not a transcript from fresh model invocations. No efficacy scores, statistical significance, or causal improvement claims are assigned.

The ordinary-assistant-style comparator identifies the core issues too. The observed engineering results support grounding recommendations in tests, accepting B, and making C conditional; they do not show that an ordinary assistant would fail or that the larger skill outperforms the minimal candidate. Recommend this compact process as an initial design to evaluate, rather than claiming an empirically selected winning prompt.

### Protocol for the missing behavioral comparison

Use fresh contexts of the same target model with identical system instructions, tools, budget, and starting fixtures. Randomize baseline/candidate order; run multiple paired trials per case. Give the baseline only the shared task and raw scenario, and the candidate those plus the skill. Withhold this answer key, saved outputs, and research notes. Permit both conditions to build and execute their own checks. Record exact model/version, skill revision, prompt, actions, output, elapsed effort, and failures.

Assess consequential defect detection, unsupported blocking claims, correctness of recommendations, evidence provenance, and handling of unresolved priorities. Reward accepting B, not the number of criticisms. For C, judge a conditional recommendation against the measurements and supplied priorities rather than prescribing a universal winner. Have a reviewer blind to condition assess the outputs and check technical claims against reproducible artifacts. Report individual results and effort, not just an aggregate preference score. Run the follow-up probes in the scenario file to assess evidence-based updating and resistance to authority pressure.

This protocol is provided for reproducibility; it was not executed in this session. Three synthetic cases would remain weak evidence of general engineering value even after independent trials.

## Structural checks

| Check | Result |
| --- | --- |
| `python3 scripts/validate.py` | Passed: one plugin, marketplaces, three skills; shared manifest metadata consistent |
| `claude plugin validate plugins/engineering` | Passed; lists `engineering:engineering-partner` alongside the existing skills |
| Skill creator's `quick_validate.py plugins/engineering/skills/engineering-partner` | Passed: skill frontmatter and naming valid |

Native validator: Claude Code 2.1.332. Claude emitted a missing listing-icon warning and marketplace install-line advice; neither changed the passing verdict. Its output explicitly says the skill contents were not read by this validator. These checks establish package structure and listing, not behavioral conformance. No plugin version bump or installation is part of this unreleased change.

`git diff --check` and direct checks of the new Markdown links also passed. The root README's pre-existing removal of its Inspiration section was retained while adding the new skill's listing.
