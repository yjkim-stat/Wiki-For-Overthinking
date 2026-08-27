<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Verifier-Guided Code Translation via Meta-Step Decoding

- **Authors**: Tianyang Zhou, Somesh Jha, Mihai Christodorescu, Kirill Levchenko, Varun Chandrasekaran
- **Venue**: arXiv.org
- **Published**: 2026-05-17
- **Source**: semanticscholar
- **Link**: <https://www.semanticscholar.org/paper/0033708ee454d5ea4c7b6ed0f9424e63baf9b395>
- **PDF**: <https://arxiv.org/pdf/2605.17626>
- **DOI**: 10.48550/arXiv.2605.17626
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Decoding Time Verification (DTV) interleaves code generation with deterministic verifier calls (compiler, type checker) at structural boundaries, using structure-aware rollback and diagnostic feedback instead of post-hoc filtering, to translate code more accurately and more token-efficiently than resampling-based test-time scaling.

## Problem

Test-time scaling methods for code generation typically run deterministic verifiers (compilers, type checkers, tests) only after a full program is generated, so an error introduced early in the autoregressive trace corrupts the conditioning context and is rarely corrected -- later tokens condition on, and tend to extend, the already-introduced error rather than recover from it.

## Contributions

- Decoding Time Verification (DTV), a decoding framework treating structural boundaries as meta-steps where deterministic verifiers are invoked in-loop, with structure-aware rollback and diagnostic feedback rather than post-hoc filtering
- an ablation isolating the contribution of each of DTV's three mechanisms (structural-boundary verification, escalating rollback, diagnostic feedback), showing in-loop structured recovery gives the largest single gain
- evidence that DTV's improvement is a distinct scaling axis from outer-loop retry/resampling, achieving a more favorable pass-rate-vs-cost frontier than best-of-N and a prior compile-driven self-debug baseline at matched token budgets

## Method

DTV is a deterministic state-machine controller that generates code up to the next structural boundary (statement, block, function or program), renders that prefix into a verifier-consumable artifact, and runs applicable oracles. If all oracles pass, the prefix is committed as a checkpoint; on failure, the controller rolls back to the smallest scope implicated by the verifier's diagnostic, injects a textual summary of the diagnostic back into the model's context (rather than blindly resampling), and retries, escalating to coarser scopes (statement -> block -> function) after repeated failures at a finer scope, with a bailout to the outer loop if escalation cannot resolve the error. This inner loop composes with an outer loop (one-shot, self-refine, or best-of-N). Evaluated on C-to-Rust (300 CodeNet programs, rustc + differential testing via AFL++-fuzzed inputs) and JavaScript-to-TypeScript (150 programs, tsc + ESLint zero-typedef as oracles, no executable tests), using Qwen3-4B-Instruct as the primary generator (with Gemma-4-E4B for cross-model checks), under matched per-case token budgets against naive one-shot/self-refine, best-of-N, and the S* compile-driven-selfdebug baseline.

## Results

Under a fixed 16x-source-token generation budget, DTV/self-refine Pareto-dominates naive/self-refine on both tasks: 82.0% vs. 72.3% compile-pass rate on C-to-Rust (+9.7pp) and 46.0% vs. 33.3% on JS-to-TypeScript (+12.7pp), while using fewer average tokens per case (k=5.28 vs. higher for naive on C-to-Rust; k=7.18 on JS-to-TS). Without any outer-loop retry, DTV/one-shot alone reaches 47.0% (C-to-Rust) and 21.3% (JS-to-TS) at much smaller average token budgets than naive/one-shot, exceeding it by +30.7pp and +16.7pp respectively -- showing in-loop verification is a distinct scaling mechanism, not merely faster convergence to the same ceiling. DTV/self-refine also beats best-of-N (up to N=32, which tops out at 44.5% on C-to-Rust and is flat near 7% on JS-to-TS) and the S* baseline (75.5%/33.0%, using ~4.7x/2x DTV's tokens) at matched cost. Ablating DTV's three mechanisms on 100 C-to-Rust cases: removing diagnostic feedback drops pass rate from 85.0% to 74.0% (-11.0pp), restricting rollback to statement-only scope (no escalation) drops it to 79.0% (-6.0pp), and disabling structural in-loop recovery entirely (detect-and-abort) drops it to 70.0% (-15.0pp, the largest single-mechanism effect) while using ~24% more tokens. DTV's compile-pass gains are not accompanied by a behavioral-correctness regression: on C-to-Rust, DTV/self-refine's functional (differential-testing) success rate is 8.3% vs. naive/self-refine's 9.3%, a difference the paper reports as statistically indistinguishable from zero. DTV's rescue rate over naive-failed cases decreases monotonically as the necessary fix moves from the failing line to elsewhere in the code (LOCAL-to-NONLOCAL gap of 20.4pp on C-to-Rust, 29.3pp on JS-to-TS), and cross-model transfer to Gemma-4-E4B holds DTV above naive on 3 of 4 model-task pairs (the exception being C-to-Rust on Gemma-4-E4B, where naive already reaches 93.5% at the token cap).

## Limitations

DTV requires direct control over the decoding loop (boundary stops, rollback, context editing), so it cannot be applied to closed-weight inference APIs that do not expose this control surface -- all experiments use open-weight models (Qwen3-4B, Gemma-4-E4B). The method is instantiated and evaluated only on code translation (C-to-Rust, JS-to-TypeScript); the paper states scaling to larger models, extending beyond translation, and reducing the implementation effort of adding new verifiers/tasks remain open. DTV's advantage weakens on 'nonlocal' fixes (cases where the necessary correction lies outside the flagged error line), and on JS-to-TypeScript the mean (though not median) token savings versus naive self-refine reverses for a tail of nonlocal-fix cases where the inner loop re-emits the same diagnostic without converging.

## Why it matters here

- **overthinking**: Indirectly relevant: it is not about reducing reasoning-trace length, but it is a token-efficiency result for test-time compute -- interleaved, structure-aware verification with targeted rollback beats blind resampling (best-of-N) and post-hoc self-refine at matched token budgets, and reaches a given pass rate at markedly fewer tokens than naive scaling. It is evidence for a general pattern relevant to overthinking: spending inference-time compute on where an error was actually introduced, rather than restarting whole attempts, is a more efficient use of a fixed token budget than repeated full-length sampling.

## Entities

- **Concepts**: decoding-time verification, structural-boundary verification, structure-aware rollback with escalation, feedback via prompt augmentation, process-level (step-level) verifier signal
- **Methods**: Decoding Time Verification (DTV), self-refine, [best-of-N](../../../../wiki/methods/best-of-n.md), S* (compile-driven self-debug)
- **Datasets**: CodeNet (C source, 300 programs), TypeWeaver (JS source, 150 self-bundled programs)

Tags: `test-time-scaling`, `code-translation`, `verifier-guided-decoding`, `rollback`, `token-efficiency`

## Abstract

Test-time scaling is an important mechanism for improving large language models, especially on tasks with deterministic verifiers. Code translation is a canonical example: the source program constrains valid outputs, while compilers, type check- ers, and behavioral checks provide exact pass/fail feedback. Existing approaches typically apply these verifiers only after generation, which is inefficient because early errors corrupt the autoregressive context and are rarely corrected later. We introduce Decoding Time Verification (DTV), a framework that treats structural boundaries as meta steps for verifier-guided decoding. DTV interleaves generation with verifier calls under a state-machine controller that enforces valid prefixes, using structural-boundary checks and structure-aware rollback to prevent error propagation while reducing wasted tokens. We evaluate DTV on C-to-Rust and JavaScript-to-TypeScript translation. Using Qwen3-4B as the primary generator under matched token budgets, DTV improves pass rates from 72.3% to 82.0% on C-to-Rust and from 33.3% to 46.0% on JavaScript-to-TypeScript relative to matched self-refinement baselines, while using fewer tokens per case; the same trend largely transfers to Gemma-4-E4B. In the evaluated cost-matched grid, DTV achieves a more favorable pass-rate-cost tradeoff than post-hoc verification or sampling-based scaling. These results show that verifier-guided decoding is an effective use of inference-time compute for code translation.

---

Record id: `arxiv:2605.17626`
