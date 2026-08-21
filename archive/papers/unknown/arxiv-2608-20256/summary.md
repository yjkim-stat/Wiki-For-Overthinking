<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation

- **Authors**: Gijs Kassenaar, Zhao Yang, Vincent François-Lavet
- **Venue**: cs.AI
- **Published**: unknown
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.20256>
- **PDF**: <https://arxiv.org/pdf/2608.20256>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.73

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reasoning language models trained with reinforcement learning typically operate under a fixed token budget rather than an explicitly adaptive one, which can lead to over-computation on easy problems and insufficient computation on difficult ones. We study whether a model can learn to allocate its own reasoning effort by choosing, as the first token of its response, one of three modes: \textsc{NoThink} (answer as quickly as possible), \textsc{Short} (brief reasoning), or \textsc{Long} (extended reasoning). The choice is learned inside Group Relative Policy Optimization (GRPO) with no separate router, through a shaped reward that makes each mode worthwhile at a different response length, together with hard per-mode token caps that keep the modes distinct. On a 1.5B distilled model trained on MATH, the three modes emerge without collapsing to a single choice, and the brief modes end up more accurate than \textsc{Long}, which shows that the router sorts problems by difficulty rather than at random. Averaged over three seeds, the resulting policy stays close to the base model's accuracy on the held-out MATH500 ($0.782$ vs.\ $0.796$) while cutting the mean response length from $4{,}796$ to $2{,}811$ tokens (a $41\%$ reduction). Interestingly, it also transfers to other benchmarks without retraining, with the largest savings where problems are easier, with for instance 76\% token reduction on GSM8K and at higher accuracy than the baselines at similar response length. In short, we build a reasoning model that adaptively chooses how much to reason for each problem.

---

Record id: `arxiv:2608.20256`
