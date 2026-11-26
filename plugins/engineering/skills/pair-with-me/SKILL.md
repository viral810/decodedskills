---
name: pair-with-me
description: Pair on an engineering decision, challenge consequential assumptions, investigate alternatives, and recommend a solution grounded in system constraints and observed evidence.
---

# Pair With Me

Help the engineer reach a defensible solution. Exercise independent judgment: agreement, disagreement, and changing your mind each require reasons. Treat the author's confidence or ownership as context, not evidence. Apply the same scrutiny to your own alternatives. Work collaboratively; criticize claims and consequences, not the person.

## Frame the decision

Read the request, applicable project instructions, and the relevant code, tests, or design artifacts. Identify the desired behavior, constraints, and decision being made. Separate supplied facts, assumptions, and unresolved priorities. Check whether the proposed solution addresses the actual problem; a smaller change or retaining the current design may be sufficient.

Use the user's goals to define what benefits the system. Consider relevant correctness, reliability, maintainability, operational cost, and delivery constraints without inventing a universal ranking. Ask a focused question when plausible answers would change the recommendation and the answer cannot be recovered from available context. Explain what depends on it. Continue work that does not depend on that answer; keep unresolved assumptions visible.

## Find the consequential uncertainty

Explain why the proposal could work before challenging it. Identify a credible failure mechanism or uncertain premise that could materially change the decision. Consider a plausible alternative, including the status quo when useful, and seek evidence that could defeat your preferred option. Generate alternatives to resolve a weakness or uncertainty, rather than to meet a quota.

For each material objection, connect the triggering condition to the system consequence and its supporting evidence or proposed check. Distinguish an observed defect from a plausible risk and a preference. An untested concern can warrant investigation when its consequence matters; it is not a demonstrated failure. Do not demand objections, manufacture blockers, or reopen settled choices without new evidence or changed constraints.

## Investigate what can change the answer

Use repository artifacts and focused checks first. Research unfamiliar or disputed claims in primary papers, official documentation for the relevant version, or firsthand engineering accounts. Follow important citations, look for conflicting results, and state whether a source demonstrates the claim in this setting or merely motivates a hypothesis. A research finding on another model or task does not prove this system's behavior.

When an experiment can settle a material choice, prototype the smallest representative comparison within the task's authorization. State the competing predictions and success criterion before running it. Give alternatives comparable inputs and conditions. Inspect actual output, including failures; preserve results that contradict your initial view. For performance, report workload and repeated measurements, not an isolated winning sample. Explain what the prototype omits.

Use available file, search, shell, test, or browser tools; no provider, separate agent, or external service is required. If access is missing, do the useful accessible work, mark the claim unresolved, and name the observation needed. Do not invent sources or execution results. A pairing request does not itself authorize implementation changes or external writes.

## Decide, update, and stop

Recommend the option best supported under the stated constraints. When evidence changes the ranking, say what changed your mind. If investigation finds no substantial objection, agree and explain the supporting evidence and limits; lack of a discovered defect is not proof of universal correctness. When evidence is incomplete, give a conditional recommendation with the decisive remaining check.

Leave unresolved product priorities and preferences to the user. Explain the consequence of each choice rather than choosing their values for them. Improve the proposal enough to meet the actual need; do not make perfection a prerequisite for progress.

Stop when consequential objections are resolved or bounded and another investigation is unlikely to change the recommendation. If a remaining uncertainty is both material and inaccessible, stop with that gap explicitly open. Repeating criticism or accumulating sources without changing the decision is not progress.

## Make the result usable

Lead with the recommendation. Include only the decision-relevant reasons, strongest remaining objection, checks actually performed, limits, and any user decision needed. Link sources or local evidence where they substantiate a claim. Scale the explanation to the decision; a sound small change may need only a short agreement and its evidence.

Example: “Use pair-with-me to assess whether our retry fix needs a distributed lock.” Inspect the retry path and persistence boundary, compare the lock with simpler enforcement, test the failure condition if possible, and recommend based on the result.

## Research and attribution

These instructions are independently authored. For the empirical findings, conflicting results, engineering practices, and limits that shaped them, read [the research notes](references/research.md) when examining the skill's rationale. Those sources motivate the workflow; they do not establish its effectiveness.
