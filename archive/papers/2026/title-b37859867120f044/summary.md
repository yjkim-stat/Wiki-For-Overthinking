<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SuCo: Sufficiency-guided Continuous Adaptive Reasoning

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63630>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

## Problem

Large reasoning models emit long chains of thought even on trivial queries, inflating cost and latency. Existing adaptive methods (AdaCoT, AdaptThink, LHRMs, S-GRPO) control this by discrete mode selection — think/no-think switches, fixed budget tiers, domain labels, external assessors — which adjusts effort over a finite hand-specified set rather than calibrating it per problem. What is missing is a principled criterion for when reasoning is already sufficient, as opposed to a heuristic length constraint.

## Contributions

- Formalises Minimal Sufficient CoT as the shortest reasoning prefix whose per-token geometric-mean probability of the ground-truth answer exceeds a difficulty-adaptive threshold, and shows empirically that across all five MATH difficulty levels it both shortens reasoning and raises accuracy over full CoT.
- SuCo, a two-stage training framework (MFT then SAPO) that places reasoning effort on a continuous spectrum without discrete modes, budget tiers or an external controller.
- A sufficiency-aware RL reward that penalises over-thinking and under-thinking separately, paired with a dynamic complexity pool that re-estimates the sufficiency target as the policy's length distribution shifts during training.
- Evidence that MSC supervision transfers across model families: MSC data built with Qwen3-4B, Qwen3-14B or R1-Distill-7B as calibrator beats full-CoT SFT on both Qwen2.5-1.5B and Llama-3.2-3B targets.

## Method

Reasoning sufficiency S(z | x, y*) is the geometric mean over ground-truth answer tokens of the model's probability of y* conditioned on the question and a CoT prefix z (the geometric mean, rather than the joint probability, so the signal does not decay exponentially with answer length). A prefix is delta-sufficient when S >= delta; the MSC is the shortest sentence-level prefix that is delta-sufficient. The threshold is problem-adaptive: delta(x) = delta_0 + alpha * C(x), where C(x) in [0,1] is the percentile rank of the trajectory's length in the dataset, used as a proxy for problem complexity (percentile rather than min-max or log-scaling, which the ablation shows are distorted by outliers). Stage I, MSC-Aligned Fine-Tuning: a strong LRM generates full CoT for each training question, the MSC prefix is extracted, prefixes shorter than L_min = 5 sentences are replaced by an empty CoT (the question needs no explicit reasoning), and a refinement model repairs the logical gaps left by truncation; the base model is then SFT'd on the resulting <think>MSC</think> answer pairs. Stage II, Sufficiency-Aware Policy Optimization: GRPO with reward = correctness + format + beta * R_suff, where R_suff subtracts lambda_over when the generated length exceeds the sufficiency point t* by more than a tolerance of 2 sentences, and subtracts lambda_under when the answer is both wrong and shorter than t*. Because the length distribution shifts as the policy trains, a dynamic complexity pool tracks each question's average rollout length by exponential moving average (eta = 0.1) and recomputes delta(x) from it, so the sufficiency target follows the current policy instead of the frozen Stage-I estimate.

## Results

On Qwen2.5-Math-1.5B/7B-Base with 270,011 training samples, averaged over GSM8K, MATH-500, AMC23, AIME25, MBPP, LiveCodeBench-v6, MMLU-STEM and GPQA-Diamond: 53.1% accuracy at 1.5B with 1,483 mean response tokens, versus DeepSeek-R1-Distill-Qwen at 45.2% / 5,736 tokens and the strongest adaptive baseline LHRMs at 50.5% / 2,055 tokens; at 7B, 72.1% / 1,267 tokens versus 63.2% / 5,239 for R1-Distill and 68.6% / 1,891 for LHRMs. Token reduction against R1-Distill is 74.1% at 1.5B and 75.8% at 7B. On AIME25 at 7B: 61.7% versus 49.7% for R1-Distill with 75.3% fewer tokens. Out of domain (StrategyQA / CommonsenseQA / AlpacaEval) SuCo reaches 55.7 / 49.3 / 2.4 LC-WR against 53.3 / 45.0 / 1.05 for R1-Distill, while MFT alone collapses to 28.0 / 26.6 / 0.67 — the RL stage, not the SFT stage, is what generalises. MFT ablation: MSC-trained 45.7% accuracy at 1,344 tokens versus full-CoT SFT at 38.4% / 5,082 tokens. SAPO ablation: SAPO raises accuracy over MFT (51.5% to 53.1%) while *increasing* mean tokens (1,347 to 1,483); removing the sufficiency reward gives 52.7% at 2,053 tokens, removing the dynamic complexity pool 52.9% at 1,642. MSC data transfers across calibrators: Qwen3-4B/14B and R1-Distill-7B calibrators all beat full-CoT SFT on both Qwen2.5-1.5B (44.2-44.7 vs 37.4) and Llama-3.2-3B (43.2-44.2 vs 38.1). Empty-CoT rate sits at 30-37% across domains and falls monotonically as MATH difficulty rises; the Level-5/Level-1 mean-token ratio is about 5.5x for SuCo against about 3.1x for the base LRM.

## Limitations

Stated: MSC construction needs ground-truth answers to compute sufficiency, so the training procedure does not apply to open-ended generation (the trained model is claimed to carry the behaviour over anyway, which the OOD table supports but does not prove for free-form generation); and MFT depends on CoT distilled from strong LRMs plus an 80B refinement model, with removal of the refiner costing 5.1% accuracy and 38.6% more tokens. Not stated but visible in the tables: the headline of 'consistently highest accuracy' is not uniform — on AIME25 at 1.5B, LHRMs scores 34.0 against SuCo's 33.7, and LHRMs also produces fewer GSM8K tokens at 1.5B (242 vs 304). The direction of the SAPO ablation also cuts against the framing: the stage sold as anti-overthinking makes generations 10% longer, and its gain is accuracy, not brevity, so the efficiency comes almost entirely from MFT. Complexity C(x) is estimated purely from reasoning length percentile, which conflates a verbose model with a hard problem. Sufficiency is measured under the same model being trained, so nothing distinguishes a prefix that genuinely establishes the answer from one that merely makes the model confident — the metric would reward a confidently wrong shortcut identically.

## Why it matters here

- **overthinking**: This is a direct attack on the topic's central question — where should a reasoning trace stop — and it proposes an answer that is neither a length budget nor a mode switch: stop at the first point where the model's own probability of the correct answer clears a difficulty-scaled bar. That gives the group an operational stopping criterion to compare against ThinkPrune-style pruning and AdaptThink-style binary gating, and Figure 2's observation is the sharper claim: past the sufficiency point, further 'waiting' and self-verification steps make sufficiency *fall*, which is a mechanism for why overthinking degrades accuracy rather than merely costing tokens. Two of its results complicate the topic's usual framing. First, 30-37% of questions get an empty CoT with accuracy maintained, so for a third of a benchmark the right amount of reasoning is none — the tradeoff curve starts at zero, not at some minimum trace. Second, the ablation shows the RL stage that is supposed to suppress overthinking makes traces 10% longer (1,347 to 1,483 tokens) while improving accuracy, so within one paper the length-accuracy relation runs in both directions depending on which stage is doing the work; length reduction came from imitation, and RL spent the savings back. The measurement caveat matters for anyone reusing MSC: sufficiency is the model's confidence in the ground truth, not evidence that the prefix established the ground truth, so it cannot separate a valid short proof from a lucky guess the model was already confident about.

## Entities

- **Concepts**: Minimal Sufficient CoT, Reasoning Sufficiency, Continuous Adaptive Reasoning, [Overthinking](../../../../wiki/concepts/overthinking.md), [Underthinking](../../../../wiki/concepts/underthinking.md), Problem-Adaptive Threshold, Empty Chain-of-Thought, Difficulty-Conditioned Reasoning Length, [Test-Time Compute Scaling](../../../../wiki/concepts/test-time-compute-scaling.md)
- **Methods**: SuCo, Minimal Sufficient CoT (MSC), MSC-Aligned Fine-Tuning (MFT), Sufficiency-Aware Policy Optimization (SAPO), [GRPO](../../../../wiki/methods/grpo.md), dynamic complexity pool, percentile-based complexity estimation, problem-adaptive sufficiency threshold
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math500.md), [AMC 2023](../../../../wiki/datasets/amc23.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [MBPP](../../../../wiki/datasets/mbpp.md), [LiveCodeBench-v6](../../../../wiki/datasets/livecodebench-v6.md), [MMLU-STEM](../../../../wiki/datasets/mmlu-stem.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [StrategyQA](../../../../wiki/datasets/strategyqa.md), [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md), AlpacaEval 2.0, MATH (Hendrycks), [Llama-Nemotron Post-Training Dataset](../../../../wiki/datasets/llama-nemotron-post-training-dataset.md), Mixture-of-Thoughts, [OpenR1-Math-220k](../../../../wiki/datasets/openr1-math-220k.md), [OpenCodeReasoning](../../../../wiki/datasets/opencodereasoning.md), [s1K-1.1](../../../../wiki/datasets/s1k-1-1.md)

Tags: `overthinking`, `adaptive-reasoning`, `chain-of-thought`, `reasoning-length`, `grpo`, `reinforcement-learning`, `efficient-reasoning`, `test-time-compute`, `sufficiency`, `llm`

---

Record id: `title:b37859867120f044`
