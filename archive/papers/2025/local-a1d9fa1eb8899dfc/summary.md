<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Dynamic Early Exit in Reasoning Models

- **Authors**: Chenxu Yang, Qingyi Si, Yongjie Duan, Zheliang Zhu, Chenyu Zhu, Qiaowei Li, Minghui Chen, Zheng Lin, Weiping Wang
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-training, test-time-scaling, reasoning-evaluation
- **Relevance score**: reasoning-training 0.50

## In one line

Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.

## Problem

Long chain-of-thought is what makes reasoning models work, but overthinking makes them generate verbose sequences with redundant steps. That costs latency and compute, and it also costs accuracy: redundant processing can derail a model from a correct reasoning path onto an erroneous one. The gap is attributed to training — neither SFT nor RL gives the model a mechanism to adjust reasoning length during generation — so a model that has already reached sufficient information keeps going with no way to stop.

## Contributions

- A pilot study establishing that stopping early is often not merely harmless but beneficial: about 75% of samples contain a point at which forced early exit yields a correct answer, and 36.7% need less than half the original reasoning path.
- Evidence that the optimal exit point varies per problem and tracks its difficulty, which is the argument that fixed-fraction or heuristic stopping is structurally wrong.
- DEER, a training-free method combining three modules: a reasoning transition monitor, a trial answer inducer and a confidence evaluator, requiring no modification to the model.
- Two interchangeable monitor designs — linguistic markers such as 'Wait', and next-token entropy at step boundaries — shown to perform comparably, with the marker version recommended for simplicity and the entropy version covering non-English reasoning.
- DEER-PRo, a parallel variant that induces answers with several different prompts at each candidate exit and calibrates confidence by subtracting a scaled mean absolute deviation, correcting for prompt sensitivity.
- A branch-parallel decoding scheme that linearizes the trial-answer branches into one sequence with a specialized attention mask and prunes the KV cache by confidence, so the monitoring overhead does not cancel the token savings.

## Method

Reasoning models are treated as generating [prompt] + <think> + slow thinking + </think> + conclusion, with the slow-thinking block a sequence of action executions separated by action transition points such as 'Wait' or 'Alternatively'. DEER treats those transitions as candidate stopping points. The monitor identifies them either by matching the linguistic marker or, in the entropy variant, by segmenting on newlines and flagging steps whose initial-token entropy exceeds 0.672 — a threshold taken from the finding that roughly the top 20% of tokens by entropy are the decision-relevant ones. At a candidate point the answer inducer appends a prompt containing the answer delimiters so the model immediately emits a trial answer from the reasoning produced so far. The confidence evaluator takes the maximum predicted probability of each answer token and combines them by geometric mean, which is more sensitive to any single low-probability token than an arithmetic mean. If that confidence exceeds a threshold, the model is deemed to have reached sufficient information and generation is terminated with the conclusion; otherwise the induced answer is discarded, the model reverts to the transition point, and reasoning continues. DEER-PRo repeats the induction with N = 4 different inducer prompts and uses a calibrated confidence equal to the mean minus the mean absolute deviation, so answers that are confident only under some phrasings do not trigger an exit. Evaluation covers 10 benchmarks across mathematics (GSM8K, MATH-500, AMC 2023, AIME 2024, AIME 2025, OlympiadBench), science (GPQA Diamond) and code (HumanEval, BigCodeBench, LiveCodeBench), on 11 models from 1.5B to 671B parameters, with vLLM, a single threshold of 0.95 used uniformly, and 4 sampling rounds on the small datasets.

## Results

The motivating measurement: on MATH-500 and GPQA respectively, 60.8% and 35.1% of correctly answered samples stay correct when exited after only 20% of the reasoning steps, and the position that corrects the most originally-wrong answers differs by dataset (40% of steps for MATH, 50% for GPQA). Main results on DeepSeek-R1-Distill-Qwen-7B, as accuracy / tokens / compression: vanilla reaches 64.2% overall at 100% length, DEER 69.2% at 61.5%, DEER-PRo 69.7% at 65.8%. Per benchmark for DEER against vanilla: GSM8K 90.6 vs 89.6 at 61.8% length, MATH-500 89.8 vs 87.4 at 55.5%, AMC23 85.0 vs 78.8 at 65.5%, AIME24 49.2 vs 41.7 at 71.5%, GPQA-Diamond 31.3 vs 23.7 at 53.4%. On Qwen3-14B, DEER reaches 83.7% overall at 57.1% length and DEER-PRo 84.3% at 63.3%, against vanilla 82.8%. On QwQ-32B, DEER reaches 84.0% at 80.9% length against vanilla 82.6%, notable because nearly every competing baseline fails on this model due to sporadic invalidation of its end-of-thinking delimiter. Against efficient-reasoning baselines, token-budget prompting works on easy tasks but fails on AIME24 where models ignore the length constraint and generate longer than vanilla; NoThinking and Chain-of-Draft cut length dramatically at heavy accuracy cost; Dynasor-CoT preserves quality but exits too conservatively to save much. Compression is weaker on code (average 19.9%) than on math and science (61.5%), attributed to verbose code segments per reasoning step. Smaller models overthink more and therefore gain more length reduction. Latency falls 27.9-40.1% with DEER and 36.3-58.6% with the branch-parallel variant. The threshold is robust in the range 0.9-0.97 for DeepSeek models and 0.8-0.97 for Qwen3, with 0.95 used everywhere.

## Limitations

The paper has no limitations section. The clearest issue a reader should note is internal inconsistency in the headline numbers: the abstract claims length reductions of 19.1% to 80.1% and accuracy gains of 0.3% to 5.0%, while Section 4.2 states accuracy improvements of 0.9 to 4.8 points and length reductions of 19.1% to 42.9% — three different ranges for two quantities, with the main table's compression rates falling outside the body's stated range. Beyond that: the accuracy gains on GPQA-Diamond are large enough to be worth scrutiny (23.7 to 31.3 for the 7B model), which if genuine means vanilla generation is actively derailing rather than merely wasting tokens, and that reframes the method as error prevention rather than efficiency; the paper asserts this derailment mechanism but does not isolate it. DEER-PRo buys robustness at 2.8-6.2% more generation than DEER, so the two variants trade against each other rather than dominating. The confidence threshold, though reported as robust over a range, is a single global hyperparameter validated on the same benchmarks used for the main results. And the method requires interrupting generation to induce trial answers, so it applies only to open-weight models served locally.

## Why it matters here

- **test-time-scaling**: The baseline the archive's other early-exit work measures itself against, and the paper that framed the problem those methods inherit. Its pilot study is the most direct evidence here that overthinking costs accuracy and not just tokens — 75% of samples contain a point where stopping early yields a correct answer, and the position that corrects the most wrong answers is well before the end. That reframes early exit for this topic: it is not purely an efficiency technique, and the archive's other results showing early-exit methods trailing vanilla accuracy are in tension with the gains reported here, which is worth resolving before treating either as settled. Its monitor design is also where two threads of this archive meet: the entropy-based variant flags candidate exits using a 0.672 next-token entropy threshold taken directly from the high-entropy-minority-tokens work on RLVR training, so the same statistic that identifies which tokens deserve gradient is reused to identify where a chain can be cut. The archive now holds four ways to decide when to stop — a linguistic marker plus answer confidence here, a CUSUM change-point statistic on predictive entropy, an activation probe for the commitment boundary, and fixed-fraction truncation as the control — all evaluated on overlapping benchmarks, which makes a direct comparison feasible and, as far as this archive shows, not yet done.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), early exit, pearl reasoning, action transition point, trial answer, answer confidence, [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), [token-level entropy](../../../../wiki/concepts/token-level-entropy.md), compression rate, [test-time compute](../../../../wiki/concepts/test-time-compute.md)
- **Methods**: [DEER](../../../../wiki/methods/deer.md), [DEER-PRo](../../../../wiki/methods/deer.md), branch-parallel decoding, entropy-based transition monitoring, answer inducing, confidence evaluation, [Dynasor-CoT](../../../../wiki/methods/dynasor.md), NoThinking, Chain-of-Draft, [vLLM](../../../../wiki/methods/vllm.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AMC23](../../../../wiki/datasets/amc23.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [HumanEval](../../../../wiki/datasets/humaneval.md), BigCodeBench, [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `early exit`, `overthinking`, `test-time scaling`, `inference efficiency`, `confidence`, `training-free`, `entropy`

## Abstract

Recent advances in large reasoning language models (LRMs) rely on test-time scaling, which extends long chain-of-thought (CoT) generation to solve complex tasks. However, overthinking in long CoT not only slows down the efficiency of problem solving, but also risks accuracy loss due to the extremely detailed or redundant reasoning steps. We propose a simple yet effective method that allows LLMs to self-truncate CoT sequences by early exit during generation. Instead of relying on fixed heuristics, the proposed method monitors model behavior at potential reasoning transition points and dynamically terminates the next reasoning chain's generation when the model exhibits high confidence in a trial answer. Our method requires no additional training and can be seamlessly integrated into existing o1-like reasoning LLMs. Experiments on 10 reasoning benchmarks (e.g., GSM8K, MATH-500, AMC, GPQA, AIME and LiveCodeBench) show that the proposed method is consistently effective on 11 cutting-edge reasoning LLMs of varying series and sizes, reducing the length of CoT sequences by an average of 19.1% to 80.1% while improving accuracy by 0.3% to 5.0%.

---

Record id: `local:a1d9fa1eb8899dfc`
