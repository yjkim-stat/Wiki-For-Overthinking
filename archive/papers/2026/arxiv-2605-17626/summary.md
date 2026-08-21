<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Verifier-Guided Code Translation via Meta-Step Decoding

- **Authors**: Tianyang Zhou, Somesh Jha, Mihai Christodorescu, Kirill Levchenko, Varun Chandrasekaran
- **Venue**: arXiv.org
- **Published**: 2026-05-17
- **Source**: semanticscholar
- **Link**: <https://www.semanticscholar.org/paper/0033708ee454d5ea4c7b6ed0f9424e63baf9b395>
- **DOI**: 10.48550/arXiv.2605.17626
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Interleaves compiler and type-checker calls into decoding at structural boundaries of the generated program, rolling back to the last valid prefix when a check fails, and evaluates it on C-to-Rust and JavaScript-to-TypeScript translation under matched token budgets.

## Problem

Test-time scaling works well where a deterministic verifier exists, and code translation is such a case: the source program constrains the output, and compilers, type checkers and behavioural tests give exact pass/fail feedback. But existing pipelines call the verifier only after a full candidate has been generated. By then an early error has already been written into the autoregressive context and is rarely repaired by later self-refinement, so the tokens spent after the error are wasted.

## Contributions

- Decoding Time Verification (DTV): a framework that treats structural boundaries in generated code as meta steps at which a verifier is called during, not after, decoding.
- A state-machine controller that enforces valid prefixes, together with structure-aware rollback to the last valid boundary instead of whole-candidate rejection.
- Pass-rate results under matched token budgets on two translation pairs: 72.3% to 82.0% (C-to-Rust) and 33.3% to 46.0% (JavaScript-to-TypeScript) with Qwen3-4B.
- A cost-matched comparison placing verifier-guided decoding above post-hoc verification and sampling-based scaling on the pass-rate-cost frontier.

## Method

Decoding Time Verification (DTV) treats structural boundaries in the emitted program as meta steps. A state-machine controller drives generation: at each boundary it pauses, invokes structural-boundary checks, and only allows generation to continue from prefixes the checks accept. When a check fails, structure-aware rollback returns generation to the last valid boundary rather than discarding the whole candidate, which is what stops an early error from propagating through the remainder of the context and is the source of the reported token saving.

## Results

Evaluated on C-to-Rust and JavaScript-to-TypeScript translation. With Qwen3-4B as the primary generator under matched token budgets, pass rate goes from 72.3% to 82.0% on C-to-Rust and from 33.3% to 46.0% on JavaScript-to-TypeScript, relative to matched self-refinement baselines, using fewer tokens per case. The paper states the trend largely transfers to Gemma-4-E4B. Within the evaluated cost-matched grid, DTV is reported as reaching a better pass-rate-versus-cost tradeoff than post-hoc verification or sampling-based scaling. Per-benchmark token counts, the composition of the cost-matched grid and the Gemma-4-E4B numbers are not in the material available here.

## Limitations

No limitations section was available in the material read. The reader should notice the following. The whole approach presupposes a cheap, exact, incremental verifier that can be run on a partial prefix, which code translation supplies and open-ended reasoning does not. The claimed transfer to the second generator is qualified in the paper's own words as holding 'largely', without figures given here. The JavaScript-to-TypeScript absolute pass rate remains 46.0%, so more than half of cases still fail after verifier-guided decoding. The comparison is against self-refinement baselines under matched token budgets; the cost of the verifier calls themselves is not accounted for in a token budget. Only two language pairs and two models under 5B parameters.

## Why it matters here

- **overthinking**: Partly on topic, and the useful part is the accounting rather than the domain. The paper is about code translation, not about reasoning length, and its 'budget' is generated program tokens rather than chain-of-thought. But it makes a claim the group cares about: for a given token budget, when to spend the compute matters more than how much. Post-hoc verification and sampling-based scaling both let a wrong prefix run to completion and then pay again; checking at structural boundaries and rolling back reclaims those tokens, and the reported result is higher pass rates at fewer tokens per case rather than a tradeoff between the two. That is the same shape as an early-stopping or interrupt criterion for a reasoning trace, with the difference that here the stopping signal is exact and external rather than the model's own confidence - which is also the limit on transferring it, since general reasoning has no compiler. Its cost-matched grid is a worked example of the evaluation discipline the topic needs: reporting accuracy against tokens spent rather than accuracy alone.

## Entities

- **Concepts**: [Test-time scaling](../../../../wiki/concepts/test-time-scaling.md), Deterministic verifier, Verifier-guided decoding, Meta step, Error propagation in autoregressive context, Valid prefix constraint, Cost-matched evaluation
- **Methods**: Decoding Time Verification (DTV), State-machine decoding controller, Structure-aware rollback, Self-refinement (baseline), Post-hoc verification (baseline), Sampling-based test-time scaling (baseline)
- **Datasets**: C-to-Rust translation benchmark, JavaScript-to-TypeScript translation benchmark

Tags: `test-time-scaling`, `verifier-guided-decoding`, `code-translation`, `token-budget`, `constrained-decoding`, `rollback`, `inference-compute`

## Abstract

Test-time scaling is an important mechanism for improving large language models, especially on tasks with deterministic verifiers. Code translation is a canonical example: the source program constrains valid outputs, while compilers, type check- ers, and behavioral checks provide exact pass/fail feedback. Existing approaches typically apply these verifiers only after generation, which is inefficient because early errors corrupt the autoregressive context and are rarely corrected later. We introduce Decoding Time Verification (DTV), a framework that treats structural boundaries as meta steps for verifier-guided decoding. DTV interleaves generation with verifier calls under a state-machine controller that enforces valid prefixes, using structural-boundary checks and structure-aware rollback to prevent error propagation while reducing wasted tokens. We evaluate DTV on C-to-Rust and JavaScript-to-TypeScript translation. Using Qwen3-4B as the primary generator under matched token budgets, DTV improves pass rates from 72.3% to 82.0% on C-to-Rust and from 33.3% to 46.0% on JavaScript-to-TypeScript relative to matched self-refinement baselines, while using fewer tokens per case; the same trend largely transfers to Gemma-4-E4B. In the evaluated cost-matched grid, DTV achieves a more favorable pass-rate-cost tradeoff than post-hoc verification or sampling-based scaling. These results show that verifier-guided decoding is an effective use of inference-time compute for code translation.

---

Record id: `arxiv:2605.17626`
