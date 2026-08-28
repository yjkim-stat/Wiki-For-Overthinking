<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Do LLMs Encode Functional Importance of Reasoning Tokens ?

- **Authors**: Janvijay Singh, Dilek Hakkani-Tür
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1419/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1419.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1419
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Introduces greedy pruning, a likelihood-preserving token-deletion diagnostic that reveals LLMs encode a nontrivial token-level functional-importance structure in their reasoning chains -- preferentially preserving symbolic computation over referential/linguistic scaffolding -- and shows students distilled on greedily-pruned chains outperform a frontier-model-supervised pruning baseline (TokenSkip) at matched lengths.

## Problem

Prior compact-reasoning methods discover shorter reasoning chains via external mechanisms (stochastic sampling, heuristics, frontier-model supervision) but offer little insight into whether a model itself internally encodes which reasoning tokens are functionally important for producing the correct answer.

## Contributions

- greedy pruning, a diagnostic likelihood-preserving deletion procedure that reveals whether an LLM internally encodes token-level functional importance in its own reasoning
- evidence that pruned reasoning chains preserve information needed for correct answer generation, evaluated via a teacher-pruner-student distillation framework that outperforms a frontier-model-supervised baseline (TokenSkip) at matched lengths
- a functional-structure analysis showing symbolic computation is preferentially preserved under pruning while referential, descriptive and linguistic scaffolding is removed first, and that this structure is sharpened by including reasoning likelihood (not just answer likelihood) in the pruning objective
- evidence that pruning ranks are dynamically re-evaluated as context contracts (not a fixed global ordering) and are substantially predictable from attention patterns alone (Pearson r=0.88 from a small trained surrogate)

## Method

Greedy pruning is a likelihood-preserving deletion procedure: starting from a complete teacher-generated reasoning chain, it iteratively removes the single token whose deletion minimally degrades a pruner model's likelihood under a specified objective (answer-only, preserving log P(answer|remaining reasoning), or joint, preserving log P(reasoning and answer)), producing both a length-controlled pruned chain and a monotonic pruning-rank ordering over tokens. Evaluated in a teacher-pruner-student distillation framework across GSM8K, MATH and MMLU-Pro with four instruction-tuned models (Llama3.1-8B, Qwen2.5-7B, Llama2-7B-chat, Mistral-7B), comparing against TokenSkip (frontier-model-supervised), H2O (attention-based cache eviction), Surprisal (token-probability-based), and Uniform pruning baselines; also analyzes which functional token categories (symbolic math, coreference, entity names, verbal math, grammar, meta-discourse) are preserved or removed, whether pruning ranks are static or dynamically re-evaluated as context contracts, and whether pruning ranks are predictable from attention patterns alone via a trained MLP surrogate.

## Results

Across all teacher-pruner-student configurations and keep fractions (0.7-0.9), students trained on greedily-pruned reasoning chains achieve the strongest accuracy among pruning-based methods at matched keep fractions, consistently outperforming TokenSkip, H2O, Surprisal and Uniform on GSM8K, MMLU-Pro and MATH; zero-shot student performance is consistently worse than all pruning-based distillation methods. Functional-structure analysis on GSM8K shows symbolic-math tokens are strongly over-retained across pruning levels (deviating substantially above uniform-deletion baseline), while coreference tokens are markedly under-retained until late pruning stages, and verbal-math tokens fall below symbolic-math retention -- a stable ordering that persists (with some category shifts) even when pruner strength is varied. The answer-only pruning objective weakens this functional structure (categories collapse toward uniform) and correspondingly yields lower downstream student accuracy than the joint objective, and a weaker pruner (Llama2-7B) induces a different, less effective functional structure that also degrades student accuracy. Pruning ranks are dynamically re-evaluated as context contracts rather than fixed upfront: dynamic local rankings consistently outperform both a frozen (rho=1.0) and a random ranking baseline at predicting subsequent pruning decisions. A 2-layer MLP trained on only 200 GSM8K examples' attention features predicts post-deletion likelihood with Pearson correlation 0.88 on held-out data, indicating token-level importance is substantially accessible from attention patterns alone.

## Limitations

Greedy pruning's computational cost scales superlinearly in sequence length (each step requires re-evaluating likelihood over all remaining candidate deletions), making it a one-time offline preprocessing step rather than a universally scalable algorithm, and the paper studies it only at realistic-but-bounded reasoning lengths (<=500 tokens) where it remains empirically tractable. Aggressive pruning can degrade surface-level readability of reasoning traces, introducing formatting-level artifacts even though the paper reports semantic/mathematical structure is largely preserved at moderate (30%) reduction; the precise threshold at which reasoning becomes unsuitable for human interpretation is not characterized. The analysis is restricted to teacher-generated, correctness-filtered reasoning traces, so it is unclear whether pruning behaves the same way on incorrect or low-quality reasoning, where likelihood signals may be less aligned with true functional importance. Experiments use moderately sized instruction-tuned LLMs (not very large reasoning-focused models like DeepSeek-R1) due to computational constraints, though pruning quality is shown to depend on pruner strength, suggesting trends may persist or strengthen at larger scales.

## Why it matters here

- **overthinking**: Directly relevant as a diagnostic contribution: rather than proposing another length-reduction training method, it asks whether models internally encode which reasoning tokens are functionally load-bearing, and answers yes -- with a specific, interpretable ordering (symbolic computation preserved, referential/linguistic scaffolding pruned first). This gives a mechanistic grounding for why length-based interventions elsewhere in the archive can cut 70-90% of tokens without hurting accuracy: much of a reasoning trace is measurably non-essential scaffolding, and this paper is among the more rigorous attempts to characterize which parts.

## Entities

- **Concepts**: greedy pruning (likelihood-preserving token deletion), token-level functional importance, pruning-rank dynamics, attention-predictable pruning ranks
- **Methods**: greedy pruning, [TokenSkip (baseline)](../../../../wiki/methods/tokenskip-baseline.md), [H2O (baseline)](../../../../wiki/methods/h2o-baseline.md), Surprisal (baseline), Uniform pruning (baseline), teacher-pruner-student distillation, attention-based MLP surrogate for pruning-rank prediction
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH](../../../../wiki/datasets/math.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md)

Tags: `reasoning-compression`, `token-pruning`, `distillation`, `attribution`, `efficient-reasoning`

## Abstract

Large language models solve complex tasks by generating long reasoning chains, achieving higher accuracy at the cost of increased computational cost and reduced ability to isolate functionally relevant reasoning. Prior work on compact reasoning shortens such chains through probabilistic sampling, heuristics, or supervision from frontier models, but offers limited insight into whether models internally encode token-level functional importance for answer generation. We address this gap diagnostically and propose greedy pruning, a likelihood-preserving deletion procedure that iteratively removes reasoning tokens whose removal minimally degrades model likelihood under a specified objective, yielding length-controlled reasoning chains. We evaluate pruned reasoning in a distillation framework and show that students trained on pruned chains outperform a frontier-model–supervised compression baseline at matched reasoning lengths. Finally, our analysis reveals systematic pruning patterns and shows that attention scores can predict greedy pruning ranks, further suggesting that models encode a nontrivial functional importance structure over reasoning tokens.

---

Record id: `doi:10.18653/v1/2026.acl-long.1419`
