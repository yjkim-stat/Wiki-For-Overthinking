<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs

- **Authors**: Xumeng Wen, Zihan Liu, Shun Zheng, Shengyu Ye, Zhirong Wu, Yang Wang, Zhijian Xu, Xiao Liang, Junjie Li, Ziming Miao, Jiang Bian, Mao Yang
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-training, reasoning-evaluation, reasoning-faithfulness
- **Relevance score**: reasoning-training 0.50

## In one line

Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

## Problem

A prominent result holds that RLVR only improves sampling efficiency, because base models overtake RLVR models on Pass@K at large K. Conflicting findings exist and nothing reconciles them. The question posed is whether that hypothesis names a fundamental limit of RLVR or an artefact of how it was measured.

## Contributions

- The diagnosis that Pass@K on mathematics is confounded by chains that are wrong yet coincidentally reach the right short answer
- CoT-Pass@K, scoring a sample only when both the answer and the intermediate reasoning are correct, with an LLM-as-a-CoT-Judge protocol and three aggregation strategies
- Evidence of an extended reasoning boundary after RLVR on math under CoT-Pass@K across all K up to 1024, most clearly on the contamination-free AIME 2025
- Confirmation on code, where execution-based verification makes Pass@K reliable and RLVR improves it even over a distilled starting model
- A theoretical account of why answer-only rewards raise the probability of correct chains, given pretraining priors that separate them
- Training-dynamics evidence that correct reasoning is incentivized early and generalizes to unseen questions

## Method

The diagnosis is that Pass@K is unreliable on mathematics because a base model can produce an incorrect CoT that coincidentally reaches the ground truth, which is easy when answers are short and many attempts are allowed. CoT-Pass@K counts a sample as successful only when the final answer and the intermediate reasoning are both correct. Correctness of mathematical CoTs is judged by an LLM-as-a-CoT-Judge — DeepSeek-R1-0528-Qwen3-8B — run multiple times per chain under three aggregation strategies, any-correct, all-correct and majority-correct, with manual inspection of cases where Pass@K is positive but CoT-Pass@K is zero. Code tasks are used as the control, since execution-based verification leaves little room for guessing and Pass@K is therefore already reliable there. A theoretical account is then given: once a base model's pretraining supplies priors that separate correct from incorrect chains, the GRPO gradient raises the probability of correct chains even though the reward sees only the answer. Training dynamics are examined by reproducing GRPO-style training with the open-source DAPO recipe, and CoT quality is assessed from a learning perspective by asking whether supervised training on chains from different checkpoints generalizes better.

## Results

Pass@K reproduces the prior observation: the base LLM catches up with and surpasses the post-RLVR model as K grows. CoT-Pass@K does not — comparing DAPO-Qwen-32B against Qwen2.5-32B on AIME 2024, AIME 2025, MATH-500, AMC23 and Minerva, it shows a consistent and significant gap favouring the RLVR model across all values of K up to 1024. The gap is most pronounced on AIME 2025, which the authors attribute to its release after the base model's training cutoff and therefore its freedom from contamination. On code, Pass@K itself improves after RLVR: AceReason-Nemotron-7B beats DeepSeek-R1-Distill-Qwen-7B across six LiveCodeBench versions, so RLVR extends the boundary even starting from a distilled model. RLVR is found to incentivize correct reasoning early in training and to generalize to unseen test questions. On MATH-500 and AMC23 the effect is muted because the base model already solves those with enough attempts; on Minerva the post-RLVR model does not improve, which the authors attribute to a train-test domain mismatch, the DAPO data being restricted to integer-answer math while Minerva contains physics and free-form problems.

## Limitations

CoT correctness is judged by a model, so the headline metric inherits that judge's reliability — the paper acknowledges this by running multiple verifications, reporting three aggregation strategies as a band, inspecting disagreements by hand, and calling for benchmarks that assess LLM verifiers. The theory assumes the base model already holds priors separating correct from incorrect chains, which is an empirical premise about pretraining rather than something proved. The main math comparison rests on one model pair at 32B. The Minerva null result is explained post hoc by domain mismatch rather than predicted.

## Why it matters here

- **reasoning-evaluation**: A concrete instrument, not just a critique. CoT-Pass@K is cheap enough to adopt and it turns a metric that rewards luck into one that does not, on exactly the benchmarks this archive is dominated by. The AIME 2025 result doubles as a contamination control — the effect is largest on the split released after the base model's cutoff — which is the kind of design the archive has found almost universally missing. Its dependence on a model judge is the standing caveat, and the paper is honest that verifier benchmarks do not yet exist.
- **reasoning-faithfulness**: Supplies a quantity this topic has lacked: how often a correct answer rests on incorrect reasoning, measured at scale rather than inferred. That is the same dissociation the archive records from CoRE's superficial execution on code and from the proverb benchmark, arriving here on competition mathematics and large enough to invert a headline result. It also makes faithfulness load-bearing for evaluation rather than a separate safety concern — if unfaithful chains inflate a benchmark, then measuring capability at all requires measuring faithfulness first.
- **reasoning-training**: Resolves, or at least reframes, the archive's sharpest open dispute about what RLVR does. Paired with arXiv 2504.13837, which this archive also holds, the two agree on the Pass@K observation and disagree on its meaning — and the disagreement is settled by measurement rather than argument: score the chain and the crossing point disappears. The theoretical half is the part this topic should keep, because it explains how an outcome-only reward can select for process quality at all: if pretraining already separates correct from incorrect chains, the policy gradient inherits that separation for free. That is a mechanism for why process supervision sometimes adds little, which the archive has observed empirically and not explained.

## Entities

- **Concepts**: pass-k, [reasoning boundary](../../../../wiki/concepts/reasoning-boundary.md), [chain of thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md), [verification](../../../../wiki/concepts/verification.md), [benchmark contamination](../../../../wiki/concepts/benchmark-contamination.md), [judge reliability](../../../../wiki/concepts/judge-reliability.md), spurious guessing, [training dynamics](../../../../wiki/concepts/training-dynamics.md), process evaluation
- **Methods**: CoT-Pass@K, [pass@k](../../../../wiki/methods/pass-k.md), [RLVR](../../../../wiki/methods/rlvr.md), [GRPO](../../../../wiki/methods/grpo.md), [DAPO](../../../../wiki/methods/dapo.md), [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md)
- **Datasets**: [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [MATH-500](../../../../wiki/datasets/math-500.md), [AMC23](../../../../wiki/datasets/amc23.md), [Minerva](../../../../wiki/datasets/minerva.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `rlvr`, `cot-pass@k`, `pass@k`, `faithfulness`, `evaluation metric`, `theory`

## Abstract

Recent advancements in long chain-of-thought (CoT) reasoning, particularly through the Group Relative Policy Optimization algorithm used by DeepSeek-R1, have led to significant interest in the potential of Reinforcement Learning with Verifiable Rewards (RLVR) for Large Language Models (LLMs). While RLVR promises to improve reasoning by allowing models to learn from free exploration, there remains debate over whether it truly enhances reasoning abilities or simply boosts sampling efficiency. This paper systematically investigates the impact of RLVR on LLM reasoning. We revisit Pass@K experiments and demonstrate that RLVR can extend the reasoning boundary for both mathematical and coding tasks. This is supported by our introduction of a novel evaluation metric, CoT-Pass@K, which captures reasoning success by accounting for both the final answer and intermediate reasoning steps. Furthermore, we present a theoretical framework explaining RLVR's incentive mechanism, demonstrating how it can encourage correct reasoning even when rewards are based solely on answer correctness. Our analysis of RLVR's training dynamics reveals that it incentivizes correct reasoning early in the process, with substantial improvements in reasoning quality confirmed through extensive evaluations. These findings provide strong evidence of RLVR's potential to enhance LLM reasoning, offering valuable insights into its mechanisms and performance improvements.

---

Record id: `local:fb100130d8c7c2bd`
