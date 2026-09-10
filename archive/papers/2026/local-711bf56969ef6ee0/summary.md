<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers

- **Authors**: Xu Zou, Jie Tang
- **Venue**: preprint
- **Published**: 2026-01-01
- **Source**: local

## In one line

Reruns a long-context reasoning model to collect its own reasoning traces, then feeds them back before the original context on a second causal pass so the model can reread the context in light of task state it discovered on the first pass.

## Problem

Causal transformers can only condition a token's representation on tokens that precede it, but in long-context reasoning the task-relevant state (e.g. an active search target or frontier) is often only discovered after most of the context has already been read once, so a single causal pass cannot let that late-discovered state guide the reading of the earlier context.

## Contributions

- A conditional state update abstraction giving a worst-case exponential memory separation between condition-first and condition-last processing by a causal processor
- TRACE AS STATE, an inference method that feeds a model's own reasoning traces back as a textual state proxy placed before the long context on a fresh causal pass
- Evaluation across three frontier long-context reasoning models and three benchmarks showing TRACE AS STATE beats a matched trace-after-context control (TRACE APPEND) in 26 of 27 reported combinations

## Method

The model M is run n_tr times on the same long-context task x, producing n_tr reasoning traces r_j and visible answers a_j. A fixed serializer concatenates the traces (each truncated to its first 50,000 characters if longer) with fixed delimiters and a dataset-specific preamble into a single block T. TRACE AS STATE then runs a fresh causal pass with the prompt ordered [T, x] (trace before the long context) rather than the natural order [x, T] used by the control condition TRACE APPEND. The intervention acts entirely at the prompt level, between two full inference passes of an otherwise unmodified causal transformer (no architecture change, no attention-mask edit); the decision of what to place first is fixed by the method design, not computed by any model or scorer. It fires once per problem, after the n_tr source passes have completed. At inference it costs n_tr additional full source passes plus one further full pass over [T, x], so total cost scales with n_tr and the length of the reused traces (further inflated by prompts up to 50,000 characters per trace); the paper reports this increases latency and token cost and can reduce KV-cache reuse across rounds, but gives no measured or estimated wall-clock or token-cost figures for TRACE AS STATE itself.

## Results

Across 27 reported (model, task, metric) combinations spanning GraphWalks 256K (BFS, Parents), MRCRv2 8-needle (256K, 512K) and NUB-1M, TRACE AS STATE beats TRACE APPEND in 26/27. Largest gains on GraphWalks Parents: DeepSeek V4 Pro Preview EM rises 29.2 (first pass) -> 43.0 (TRACE APPEND) -> 81.8 (TRACE AS STATE), F1 46.5 -> 65.3 -> 91.3; Qwen 3.7 Max EM 60.8 -> 71.0 -> 96.4; GLM-5.2 reaches 100.0 EM and F1 (from 66.4/88.5 first pass). The one reported loss for TRACE AS STATE is GraphWalks BFS F1 on GLM-5.2, where TRACE APPEND is 0.8 points higher (75.8 vs 75.0) even though TRACE AS STATE still wins on BFS EM. Ablations on DeepSeek V4 Pro GraphWalks 256K show TRACE AS STATE exceeds Oracle@5 (best-of-5 first-pass answers) and beats a Random Trace control (traces from unrelated problems), ruling out generic rereading or scaffold-formatting alone as the explanation.

## Limitations

The paper states the cross-pass feedback requires access to raw reasoning traces or another exposed state interface; models or APIs that expose only final answers would need a different interface. TRACE AS STATE requires one or more additional full source passes plus a further full pass, which the authors state increases inference latency and token cost and can reduce KV-cache reuse in multi-round settings -- no measured or estimated inference-cost numbers are reported for either TRACE AS STATE or TRACE APPEND anywhere in the paper. Evaluation covers only three models, three long-context task families, and no multi-round agent tasks, so the authors say generalization to other models, domains, context lengths and interactive settings is untested. Traces longer than 50,000 characters are truncated, which caps how much of a long trace can serve as the state proxy.

## Entities

- **Concepts**: conditional state update task, condition-first vs condition-last ordering, reasoning trace as textual state proxy, causal state update processor
- **Methods**: TRACE AS STATE, TRACE APPEND (control), conditional state update task formalism, Re2 (rereading baseline), Random Trace / Trace Only / Answer Feedback ablations
- **Datasets**: GraphWalks (256K, BFS and Parents subtasks), MRCRv2 8-needle (256K, 512K), 1M-Novel Understanding Bench (NUB-1M), season 2

Tags: `long-context`, `causal attention`, `input ordering`, `reasoning traces`, `inference-time rereading`, `test-time state`

## Abstract

Transformers process information causally, but long-context reasoning may depend on task state discovered only later. We formalize this mismatch through conditional state update tasks. For causal state update processors, providing the condition first can require exponentially less memory in the worst case than providing it last. Motivated by this principle, we introduce TRACE AS STATE. We use collected reasoning traces as a textual proxy for task state and place it before the long-context block on a fresh pass, allowing information derived previously to guide rereading. We conduct extensive experiments on TRACE AS STATE and TRACE APPEND, a matched control that uses the same task state proxy but put it after the context. Across three models and three long-context datasets, TRACE AS STATE outperforms TRACE APPEND in 26 of 27 reported combinations of model, task, and metric. On GraphWalks Parents, exact match lifts DeepSeek V4 Pro(Preview) from 29.2% on the initial pass and 43.0% with TRACE APPEND to 81.8% with TRACE AS STATE, and from 66.4% and 83.2% to 100.0% for GLM-5.2. These results show that placing traces before the context can improve long-context reasoning while retaining the causal transformer structure.

---

Record id: `local:711bf56969ef6ee0`
