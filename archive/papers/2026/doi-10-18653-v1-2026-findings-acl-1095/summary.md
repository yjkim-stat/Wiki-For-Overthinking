<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding

- **Authors**: Sangjun Song, Minjae Oh, Seungkyu Lee, Sungmin Jo, Yohan Jo
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1095/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1095.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1095
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

ThinkBrake is a training-free decoding rule that injects </think> at sentence boundaries whenever the log-probability margin between the top continuation token and </think> narrows below a threshold, recovering most of an oracle stopping point's headroom (8% accuracy gain, 72% token reduction) with a theoretically grounded, model-agnostic criterion, and its generated trajectories can also train models via DPO for training-free-free efficient reasoning.

## Problem

Large reasoning models frequently reach a correct intermediate solution but continue deliberating and overwrite it with an incorrect final answer (overthinking); prior training-free early-stopping heuristics are hand-crafted (raw probability gaps, entropy, reflection-token suppression) and lack a principled theoretical grounding or robustness across difficulty levels.

## Contributions

- an oracle sentence-boundary-injection analysis quantifying substantial recoverable headroom from overthinking (8% accuracy gain, 72% token reduction on average) across math and tool-use benchmarks
- ThinkBrake, a training-free, model-agnostic early-termination rule based on the log-probability margin between the top continuation token and </think> at sentence boundaries
- a theoretical proof that this log-margin criterion is exactly equivalent to a temperature-scaled logit margin test and to KL-regularized test-time policy realignment with a constant reward bonus on </think>, giving the heuristic a principled derivation
- validation across six LRMs and eight benchmarks spanning math, scientific QA, and tool usage, showing the log-space formulation is markedly more robust on hard tasks than a raw-probability-gap variant
- demonstration that ThinkBrake-generated trajectories can train efficient reasoning directly into a model via DPO with only 1.3K preference pairs and 20 minutes of training, transferring even to out-of-domain tasks

## Method

First runs an oracle analysis: forcibly injecting </think> at every sentence boundary and selecting, in hindsight, the best stopping point per trajectory, to quantify how much accuracy/efficiency headroom overthinking leaves on the table. Then proposes ThinkBrake: at each sentence boundary, compute the log-probability margin m_t between the top non-</think> continuation token y*_t and the </think> token itself; terminate reasoning (inject </think>) when this margin falls below threshold tau. The paper proves this log-space margin test is mathematically equivalent to a temperature-scaled logit margin test, and further shows it is equivalent to KL-regularized test-time policy realignment that adds a constant reward bonus tau*T to the </think> logit at boundary states -- giving the heuristic a principled derivation rather than an ad hoc rule. A raw-probability-gap variant (ThinkBrake-p) is tested for comparison and found substantially less robust. ThinkBrake-generated (accepted vs. rejected) trajectory pairs are also used to build 1.3K DPO preference pairs (Omni-MATH-derived) to train the efficiency behavior directly into a model, requiring only 20 minutes on 2xH200 GPUs.

## Results

Oracle stopping reduces error rate to 6% on math reasoning and 5% on tool usage while cutting thinking tokens 54% (math) and 89% (tool usage) versus baseline on Qwen3-4B-Thinking; on the hardest AIME benchmarks, oracle stopping recovers 61% of failures while cutting tokens 44%, and fewer than 5% of errors are irrecoverable on most benchmarks -- confirming most failures stem from overthinking, not incapability. ThinkBrake itself (tau=0.1) achieves consistent efficiency-accuracy tradeoffs across six LRMs (Qwen3-4B/4B-Thinking/14B/32B, DeepSeek-R1-7B, Phi-4-Reasoning) and eight benchmarks (GSM8K, MATH500, AIME2024/25, GPQA-Diamond, ARC-Challenge, BFCL-v1/v2, Meta-Tool): on Qwen3-4B-Thinking it cuts average tokens 26.5% with accuracy 79.7% (vs. 83.7% baseline), and notably *improves* accuracy on AIME2024 for Qwen3-14B and Phi-4-Reasoning -- direct evidence it prevents overthinking rather than merely truncating. Baselines fare worse: ThinkLess (skip reasoning entirely) causes catastrophic drops on hard math (~40% on MATH500, ~73% on AIME2024 for Qwen3-4B-Thinking); NoWait degrades less but still drops notably on AIME; the raw-probability-gap variant ThinkBrake-p achieves only 30-35% accuracy on AIME versus ThinkBrake's 62-67%, validating that the log-space (ratio) formulation, not a raw probability difference, is what gives robustness on hard tasks. Average token reduction shrinks with model scale (26.5% at 4B-Thinking -> 15.8% at 14B -> 8.2% at 32B) but a larger 80B model (Qwen3-Next-80B) breaks this trend with a 22.3% reduction, suggesting the driver is reasoning-trace length (larger models often produce shorter traces with less redundant thinking to prune) rather than parameter count per se. On tool-use benchmarks, ThinkBrake matches baseline accuracy on BFCL-v2 parallel tasks with 32.3% token reduction and improves multi-parallel accuracy by ~8%, while ThinkLess suffers catastrophic drops (~50% on parallel, ~33% on multi-parallel) and NoWait degrades modestly. On Omni-MATH with difficulty labels 1-10, ThinkBrake maintains or improves accuracy uniformly across all difficulty levels with no tradeoff, and shows *greater* improvements on harder problems, consistent with the hypothesis that models uncertain about hard problems keep generating spurious verification steps even after reaching a correct answer. ThinkBrake consistently exits later than the oracle (e.g. 12,830 vs. oracle's 11,261 tokens on AIME2024), indicating it does not suffer from premature termination -- the residual accuracy gaps on the hardest benchmarks (AIME, GPQA-D) are attributed to 'spurious reasoning' (the model continuing to reason and introducing errors after already reaching a correct answer, but before ThinkBrake's margin narrows) rather than insufficient reasoning budget. DPO training on 1.3K ThinkBrake-derived preference pairs (math-only) transfers the efficiency behavior into the model weights, achieving 9-28% thinking-token reduction across all benchmarks including entirely out-of-domain tasks (GPQA-D, ARC-C, tool usage) while maintaining accuracy -- evidence the model learns general concise-reasoning patterns rather than memorizing task-specific stopping points.

## Limitations

ThinkBrake requires explicit reasoning delimiters (<think>/</think>) and access to model logits, so it is inapplicable to models with hidden chain-of-thought or black-box APIs that don't expose logits. It introduces a threshold hyperparameter tau which, while robust across a wide range (stable up to tau~10), may still require tuning in new settings (a rule of thumb of tau=0.1 works for most model-benchmark pairs, but easier tasks tolerate more aggressive tau and harder ones need it kept low). The method uses a purely local per-boundary stopping criterion and does not reason about global answer correctness, which can lead to early termination when the model is confidently wrong (it cannot detect and correct a confidently-held error, only decide whether to keep deliberating).

## Why it matters here

- **overthinking**: Directly and centrally relevant: it both quantifies overthinking's recoverable headroom via a careful oracle analysis and contributes a training-free, theoretically-grounded stopping rule that recovers most of that headroom, with a specific and testable mechanistic account (spurious reasoning after a correct answer is already reached, concentrated on harder problems) for the residual gap to the oracle. Its finding that a raw probability-gap heuristic is markedly less robust than the log-space (ratio) version is a concrete methodological lesson for any confidence-based stopping criterion in this archive.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), oracle stopping headroom, logit margin test, KL-regularized test-time realignment, spurious reasoning, log-probability margin
- **Methods**: ThinkBrake (log-margin early stopping), ThinkBrake-p (raw probability-gap variant), NoWait (baseline), ThinkLess (baseline), Dynasor-CoT (baseline), DEER (baseline), Direct Preference Optimization (DPO) on ThinkBrake data
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [AIME2025](../../../../wiki/datasets/aime-2025.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [ARC-Challenge](../../../../wiki/datasets/arc-challenge.md), BFCL-v1, BFCL-v2, Meta-Tool, [Omni-MATH](../../../../wiki/datasets/omni-math.md), DAPO17K

Tags: `overthinking`, `early-stopping`, `training-free`, `decoding-intervention`, `test-time-realignment`, `DPO`

## Abstract

Large Reasoning Models (LRMs) allocate substantial inference-time compute to Chain-of-Thought (CoT) reasoning, improving performance on mathematics, scientific QA, and tool usage. However, this introduces overthinking: LRMs often reach a correct intermediate solution, continue reasoning, and overwrite it with an incorrect answer. We first demonstrate that oracle stopping—where we inject lt;/think gt; at every sentence boundary and select the best stopping point in hindsight—improves average accuracy by 8% while reducing thinking tokens by 72%, exposing substantial overthinking. Motivated by this finding, we propose ThinkBrake, which monitors the log-probability margin between the top continuation token and lt;/think gt; at sentence boundaries, stopping reasoning when this margin narrows. ThinkBrake requires no training and achieves favorable accuracy–efficiency trade-offs across math, scientific QA, and tool usage benchmarks, reducing thinking token usage by up to 30%. Furthermore, we provide theoretical analysis showing that ThinkBrake is equivalent to test-time realignment with a reward bonus for the lt;/think gt; token.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1095`
