# Evidence behind pair-with-me

Research date: November 26, 2026. This is a focused narrative research review, not a systematic review or evidence that this particular skill improves outcomes.

## Search and selection

Searched the web across sycophancy, intrinsic self-correction, critique and debate, clarification, human reliance, developer productivity, and engineering decision practices. Followed primary links and inspected conflicting findings rather than selecting only support for criticism. Read full-text sections on methods and limitations where available; abstract-only sources are marked below. Preferred original papers, official technical documentation, and firsthand accounts. General news, third-party prompt collections, and an unrelated Redis issue encountered during exploration were excluded from the synthesis.

The evidence spans laboratory tasks and established engineering practice. None of the reviewed studies directly tests this skill or establishes a universally optimal pairing prompt. In particular, an older model's failure is not evidence that every current model has the same failure.

## Findings and their limits

### 1. User approval can be a misleading signal

**Demonstrated, in the studied models:** Sharma et al., [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) (2023), evaluated five assistants and found user-view alignment could influence responses and preference judgments. The [authors' research summary](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) describes the preference-data analysis. Consulted the abstract and author summary, not a reanalysis of their data.

**Design inference:** Judge the claim independently of ownership, seniority, or the user's confidence. Test pressure to agree and pressure to disagree using unchanged technical inputs. These instructions are a proposed mitigation, not a demonstrated cure for training-induced sycophancy.

### 2. Critique does not automatically add knowledge

**Demonstrated with important scope limits:** Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798v2) (ICLR 2024), found intrinsic correction could degrade reasoning. Sections 3–5 examine answer changes, comparable baselines, and prompt differences. Their results distinguish correction without external feedback from tool- or evidence-assisted correction.

**Design inference:** Seek a discriminating observation instead of endlessly asking the model to reconsider. Preserve a correct answer when no new evidence defeats it. This supports testing and bounded iteration, not banning useful reflection in all models.

### 3. Useful self-feedback is possible

**Counterevidence to a blanket rejection:** Madaan et al., [Self-Refine](https://arxiv.org/html/2303.17651v2) (2023), report improvements across seven tasks, including code tasks. Sections 2–3 specify actionable feedback, task-specific stopping, models, and a mixture of task metrics and preference judgments.

**Limit:** Better preference ratings, readability, and verified correctness are different outcomes; gains in one are not proof of another. Compare against an equally well-specified initial prompt and account for extra inference effort. Retain specific, actionable revision while verifying consequential claims externally when feasible.

### 4. Self-correction results depend on setup

**Contrary empirical claim:** Liu et al., [Large Language Models have Intrinsic Self-Correction Ability](https://arxiv.org/abs/2406.15673v2) (2024), report intrinsic correction under fair prompts and zero temperature. Consulted the abstract; the arXiv record labels the work as in submission.

**Limit and inference:** This does not settle the broader disagreement or validate a temperature rule for engineering agents. It reinforces testing neutral instructions that allow either correctness or error rather than assuming every answer must be repaired.

### 5. Debate can help on some benchmarks

**Demonstrated in its evaluation:** Du et al., [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325) (2023), report improved factuality and reasoning with interacting model instances. Consulted the abstract and project link, not a reproduction.

**Limit:** Benchmark improvement does not establish better architectural decisions, equal-cost superiority, or an advantage for a single model role-playing a debate. The skill borrows consideration of alternatives, without requiring debate machinery or interpreting agreement among agents as evidence.

### 6. Consensus can also erase correct answers

**Conflicting evidence:** Bertalanič and Fortuna, [The Cost of Consensus](https://arxiv.org/html/2605.00914v1) (2026), compare homogeneous debate with isolated correction and a noise control. Methods and limitations describe ten-agent teams, three rounds, mainly 7–8B models, and two difficult benchmarks. Peer exchange could induce conformity and consume more tokens without improved accuracy.

**Limit:** This is not a general verdict against heterogeneous or structured teams, frontier models, or all deliberation. It supports measuring the marginal benefit of more discussion and retaining objections until evidence resolves them. A compact single-partner process is a portability choice, not a proved architectural winner.

### 7. Clarification has a decision cost

**Demonstrated in NLP settings:** Zhang and Choi, [Clarify When Necessary](https://aclanthology.org/2025.findings-naacl.306/) (NAACL 2025), examine when to ask across question answering, translation, and inference. The paper's framework includes user preferences and distributions of possible interpretations. Consulted the paper and abstract.

**Design inference:** Ask for missing information when plausible answers change the recommendation; otherwise use recoverable context or state an assumption. This is an engineering heuristic, not a validated implementation of their framework. No universal question count is justified.

### 8. Persuasive explanations are insufficient protection

**Demonstrated with transfer limits:** Buçinca et al., [To Trust or to Think](https://arxiv.org/abs/2102.09692) (2021), report an experiment with 199 participants. Cognitive forcing reduced overreliance relative to simple explanations, but less popular designs sometimes produced better reliance behavior. Consulted the abstract.

**Limit and inference:** This concerns human decision-support interfaces, not this prompt. Ask the user to decide unresolved priorities and expose checkable evidence; avoid treating satisfaction with a fluent explanation as validation. Do not turn every exchange into a burdensome mandatory questionnaire.

### 9. Deliberately seeking contrary evidence is a useful hypothesis

**Human research, indirect transfer:** Lord, Lepper, and Preston, [Considering the opposite](https://pubmed.ncbi.nlm.nih.gov/6527215/) (1984), study a corrective strategy in two social-judgment experiments. Consulted the indexed abstract; the publisher's full text was inaccessible.

**Design inference:** Look for an observation that could defeat your preferred option, including the alternative you generated. Human debiasing findings do not prove LLM debiasing. Use this as a proposed practice to evaluate, not a guaranteed mechanism.

### 10. Actual engineering outcomes can contradict impressions

**Demonstrated in a specific field setting:** METR's [early-2025 developer productivity RCT](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf) involved 16 experienced developers and 246 tasks in familiar mature repositories. AI access increased measured completion time by 19%, despite perceived speedups. Consulted the paper abstract and [authors' methodology and caveats](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/).

**Limit:** A historical sample and tool set, not an estimate of current universal productivity. Measure outcomes and effort rather than confidence, lines generated, or how supportive the partner feels. Tiny synthetic cases cannot establish field productivity gains.

### 11. Code health includes making progress

**Firsthand practice, not a controlled intervention:** Google's [standard of code review](https://google.github.io/eng-practices/review/reviewer/standard.html) balances improving code health with progress, distinguishes technical evidence from preferences, and permits accepting an imperfect improvement.

**Adopted practice:** Agree with a proposal that meets the need; distinguish a blocking failure from optional polish. This is the clearest engineering grounding for avoiding reflexive opposition, but the document does not measure the effect of this skill.

### 12. Competing explanations need discriminating checks

**Firsthand practice:** Google's [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/), especially “Test and Treat,” describes hypothesis testing, mutually distinguishing outcomes, confounds, side effects, and recording results.

**Adopted practice:** State predictions before running a focused experiment, inspect negative results, and connect a concern to a mechanism. Troubleshooting methodology plausibly transfers to design decisions; its effectiveness here is an inference.

### 13. A design can work at endpoints and fail during transition

**Firsthand engineering account:** AWS's [Ensuring rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/) explains failures involving mixed versions and shared state, with a prepare/activate deployment technique and upgrade/downgrade testing.

**Adopted practice:** Investigate actual system boundaries and representative conditions. Happy-path correctness alone may miss the decisive failure. Do not impose a two-phase rollout on every change; use this reasoning where a transition or compatibility boundary matters.

### 14. Technical claims need implementation-specific evidence

**Authoritative semantics:** SQLite's [CREATE INDEX documentation](https://www.sqlite.org/lang_createindex.html) specifies unique-index behavior, including distinct treatment of NULL values. Its [appropriate-use guidance](https://www.sqlite.org/whentouse.html) explains context-dependent engine selection.

**Use in evaluation:** Deduplication keys are explicitly non-null and scoped by tenant. Local SQLite experiments establish only the exercised database behavior, not distributed exactly-once external effects. A fashionable alternative engine or application lock is not automatically a better solution.

## Synthesis into instructions

The compact process is an original engineering synthesis: frame the decision; expose the consequential uncertainty; investigate; recommend and update; stop. Source-backed practices motivate it, but the combined sequence has not been causally validated.

The main design choices are neutral scrutiny rather than a required objection count; alternatives tied to a material weakness; equal scrutiny of the partner's own ideas; experiments with comparable conditions; questions tied to a possible recommendation change; and explicit agreement and stopping conditions. These are testable hypotheses about useful agent behavior.

Rejected as defaults: always disagreeing, requiring a fixed number of flaws, mandatory multi-agent debate, repeated reflection without new information, browsing every routine claim, and treating lack of a discovered flaw as proof. Neither the literature nor this local evaluation establishes those as beneficial universal instructions.

Remaining user choices include relative weight of delivery time, operational burden, latency, storage, and acceptable residual risk. Experiments can measure consequences; they cannot choose those values. Use project constraints when already supplied and ask only where a consequential priority remains unresolved.

See [authoring validation](../../../../../docs/validation/pair-with-me.md) for executed experiments, the limited response rehearsal, and remaining host and independent behavioral checks. All prose is independently authored; no third-party skill text is incorporated.
