<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# EconProver: Towards More Economical Test-Time Scaling for Automated Theorem Proving

- **Authors**: Mukai Li, Linfeng Song, Zhenwen Liang, Jiahao Xu, Shansan Gong, Qi Liu, Haitao Mi, Dong Yu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.2121/>
- **PDF**: <https://aclanthology.org/2026.acl-long.2121.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.2121
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

EconRL identifies substantial token-level inefficiency in state-of-the-art automated theorem provers' test-time scaling (sequential reflective CoT vs. parallel sampling) and fixes it with two combined RL techniques -- DPO-trained dynamic CoT-mode switching and difficulty-partitioned diverse-prefix parallel scaling -- so EconProver-GD matches Goedel-Prover-V2-8B's full-CoT accuracy on miniF2F using only 12% of the sampling cost.

## Problem

State-of-the-art automated theorem provers achieve strong results via test-time scaling (sequential reflective chain-of-thought and/or parallel sampling of independent proof attempts), but existing efficiency analyses of these strategies count only the number of sampling passes, ignoring the large disparities in token cost per pass across strategies -- and the paper's own token-level analysis reveals sequential CoT scaling costs 10-15x more tokens than non-CoT approaches while parallel sampling plateaus with heavy redundancy across attempts, so current SOTA provers are substantially over-spending compute for their accuracy gains.

## Contributions

- a unified token-level sampling-cost metric revealing that state-of-the-art ATP test-time scaling strategies (sequential CoT, parallel sampling) achieve marginal performance gains at disproportionate computational cost, with ~83% of sub-IMO-difficulty problems already solvable without CoT at ~1/10 the token budget
- Dynamic CoT Switching, a DPO-trained mechanism exploiting Lean's noise-free verifier signal to teach a prover to autonomously invoke extended reasoning only for problems that actually require it, retaining 99.7% of full-CoT accuracy at 15% of the token cost
- Diverse Parallel-scaled RL, training difficulty-partitioned specialized prefix heads via independent PPO to increase proof-attempt diversity and squeeze more accuracy out of a small, fixed parallel-sampling budget
- EconProver-GD, combining both techniques on top of Goedel-Prover-V2-8B, matching baseline SOTA accuracy on miniF2F and ProofNet at only 12% of the sampling cost, with gains that compose with iterative refinement

## Method

Introduces a unified token-level sampling-cost metric (total generated tokens summed across all passes and refinement steps) to compare scaling strategies, revealing that ~83% of miniF2F statements below IMO difficulty are already solvable in Non-CoT mode by DeepSeek-Prover-V2 at ~1/10 the token budget of CoT mode, and that parallel scaling's accuracy gain per doubling of passes shrinks sharply (e.g. 64->128 passes yields only +1.1%) as measured by a Prefix Diversity Coverage metric (distinct 3-grams among the first 20 tokens of sampled proofs) that strongly correlates with accuracy and saturates around 32 passes. Builds EconRL, combining two RL techniques: (1) Dynamic CoT Switching, which exploits Lean's exact, noise-free proof-success signal to construct DPO preference pairs per problem (base-solvable problems prefer the direct proof over CoT; CoT-dependent problems prefer CoT over the direct attempt), training the model to autonomously choose Non-CoT vs. CoT mode via a single unified prompt offering both options, without external complexity indicators at inference time; (2) Diverse Parallel-scaled RL, which measures per-problem difficulty via the base prover's success count over 32 attempts, partitions training data into n difficulty-based bins each mixed 50/50 with problems from other bins, and trains n independent lightweight prefix-embedding 'heads' via PPO (each optimized separately, no joint objective) so different heads specialize in different proof strategies and increase solution diversity under a fixed, uniformly-allocated-at-inference sampling budget.

## Results

On miniF2F-test, EconProver-DS (DeepSeek-Prover-V2-7B + EconRL) reaches 76.2% accuracy at 1.5x the non-CoT baseline's token cost, versus full CoT mode's 75.8% at 10x cost -- comparable accuracy at 15% of the token usage; EconProver-GD (Goedel-Prover-V2-8B + EconRL) reaches 84.0% at 3x cost versus full CoT's 84.4% at 25x cost, and versus SFT-only or purely-CoT baselines from other systems (Kimina-Prover-distil-7B 63.1%, Leanabell-Prover-V2-DS 76.6%), demonstrating comparable-or-better accuracy at a small fraction of the sampling cost. On ProofNet-test, EconProver-DS/GD show the same pattern (23.1%/28.0% accuracy at 2-3x cost versus 23.1%/28.5% for full CoT at 10-30x cost). Combined with iterative refinement (IR), EconProver-GD matches Goedel-Prover-V2's 86.0% miniF2F accuracy while reducing token overhead by 75% (from 40x to 10x the non-CoT baseline's cost), showing the efficiency gains compose with other SOTA techniques rather than being subsumed by them. Ablation on Dynamic CoT Switching shows it retains 99.7% of full-CoT accuracy (75.4% vs. 75.8%) using only 15% of the token budget (1,186 vs. 4,488 average tokens) and a 14.8% CoT invocation rate; a log-probability-based confidence trigger baseline invokes CoT roughly twice as often (29.8%) yet still underperforms the DPO-trained switcher on both accuracy (73.0% vs. 75.4% Pass@32) and token cost, confirming verifier-grounded preference learning gives a stronger difficulty signal than surface-level model confidence. Ablation on Diverse Parallel-scaled RL shows difficulty-aware head partitioning (n=8) improves Pass@16 from 65.6% (single baseline head) to 70.5% in Non-CoT mode and from 73.0% to 75.2%/76.4% (Pass@16/32) in CoT mode, consistently outperforming both a no-head baseline and random-head grouping; gains are largest at constrained (small) pass budgets and shrink once prefix diversity coverage saturates near 32 passes. A solution-pattern-cluster partitioning (grouping by proof-prefix similarity rather than difficulty) also outperforms random grouping, confirming the gain comes from inducing genuinely distinct proof-strategy priors across heads rather than difficulty labels specifically being the necessary signal, though difficulty-aware partitioning still performs best overall.

## Limitations

The current framework treats iterative refinement, sequential scaling, parallel scaling and RL training as compatible but separately-applied techniques rather than a single jointly-optimized system; the paper explicitly identifies a unified optimization framework integrating all of these dimensions simultaneously as unaddressed future work, which the authors state would likely further reduce inference costs. Once the parallel sampling budget is large enough that prefix diversity coverage saturates, the marginal benefit of any head-partitioning scheme (difficulty-aware or otherwise) shrinks to only 1-2 problems at Pass@32, so the method's advantage is concentrated in the constrained-budget regime rather than uniformly across all scaling levels.

## Why it matters here

- **overthinking**: Central to the topic, applied to the automated-theorem-proving domain: quantifies exactly the kind of overthinking the topic tracks (uniform application of costly reflective CoT even to problems solvable without it) using a token-level cost metric rather than pass count alone, and its finding that ~83% of easier problems need no CoT at all mirrors difficulty-cognition results reported for math/general reasoning elsewhere in this archive. Its Prefix Diversity Coverage metric and difficulty-aware parallel-head partitioning also give a concrete, measurable account of *why* parallel sampling (self-consistency-style scaling) plateaus -- redundant exploration of similar proof prefixes -- directly relevant to papers elsewhere in the archive studying self-consistency's diminishing returns.

## Entities

- **Concepts**: token-level sampling cost, Prefix Diversity Coverage (PDC), dynamic Chain-of-Thought switching (DPO-trained), difficulty-aware parallel head partitioning
- **Methods**: EconRL (Dynamic CoT Switching + Diverse Parallel-scaled RL), [Direct Preference Optimization (DPO)](../../../../wiki/methods/direct-preference-optimization-dpo.md), Proximal Policy Optimization (PPO), iterative refinement (IR)
- **Datasets**: miniF2F-test/valid, ProofNet-test, LeanWorkbook, Goedel-Pset-v1

Tags: `overthinking`, `automated-theorem-proving`, `test-time-scaling`, `reinforcement-learning`, `parallel-sampling`

## Abstract

Large Language Models (LLMs) have recently advanced the field of Automated Theorem Proving (ATP), attaining substantial performance gains through widely adopted test-time scaling strategies, notably reflective Chain-of-Thought (CoT) reasoning and increased sampling passes. However, they both introduce significant computational overhead for inference. Moreover, existing cost analyses typically regulate only the number of sampling passes, while neglecting the substantial disparities in sampling costs introduced by different scaling strategies. In this paper, we systematically compare the efficiency of different test-time scaling strategies for ATP models and demonstrate the inefficiency of the current state-of-the-art (SOTA) open-source approaches. We then investigate approaches to significantly reduce token usage and sample passes while maintaining the original performance. Specifically, we propose two complementary methods that can be integrated into a unified EconRL pipeline for amplified benefits: (1) a dynamic Chain-of-Thought (CoT) switching mechanism designed to mitigate unnecessary token consumption, and (2) Diverse parallel-scaled reinforcement learning (RL) with trainable prefixes to enhance pass rates under constrained sampling passes. Experiments on miniF2F and ProofNet demonstrate that our EconProver-GD achieves comparable performance to baseline methods with only 12% of the computational cost. This work provides actionable insights for deploying lightweight ATP models without sacrificing performance.

---

Record id: `doi:10.18653/v1/2026.acl-long.2121`
