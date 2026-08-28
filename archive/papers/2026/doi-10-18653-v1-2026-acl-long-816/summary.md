<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficiently Learning To Reason or Not to Reason: Root-token Policy Optimization for Adaptive Thinking

- **Authors**: Taehyeon Kim, Hyunsoo Lee, Youngsoo Jang, Moontae Lee
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.816/>
- **PDF**: <https://aclanthology.org/2026.acl-long.816.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.816
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## In one line

Root-token Policy Optimization (RPO) reframes adaptive thinking/non-thinking gating as a branching decision at a single root token (the newline choice right after <think>) and trains only that one token's probability with group-relative RL, cutting GRPO training compute to ~2% of a comparable adaptive-reasoning method while improving the accuracy-vs-thinking-rate tradeoff across model families.

## Problem

Large reasoning models apply explicit long-form <think> reasoning uniformly to every query regardless of difficulty (overthinking), wasting compute and latency on easy questions; open-source models lack an efficient way to learn when to reason at all, since standard adaptive-reasoning policy optimization backpropagates over full, expensive reasoning trajectories (high VRAM and wall-clock cost) and depends on difficulty labels, curated data, or proprietary routing signals that are rarely available or disclosed.

## Contributions

- Root-token Policy Optimization (RPO), restricting adaptive-reasoning RL gradient updates to a single root gating token instead of full reasoning trajectories, cutting VRAM and PFLOPs by an order of magnitude versus a comparable adaptive-reasoning baseline (AdaptThink)
- a two-stage self-taught pipeline (SFT for mode-conditioned style, then RPO for the routing decision) requiring no external difficulty labels or proprietary teacher signals
- an empirical demonstration across five model families/sizes and math, coding (LiveCodeBench) and scientific-QA (GPQA) domains that root-only updates improve or match the accuracy/thinking-rate tradeoff at a fraction of the training cost
- a calibration analysis of the root SHORT-confidence signal via reliability diagrams, showing it is informative but weakly and dataset-dependently calibrated

## Method

Frames adaptive reasoning as a routing problem decided entirely at the first newline token after <think> (z in {\n, \n\n}): choosing \n enters LONG (explicit reasoning continues), choosing \n\n enters SHORT (the think block is immediately closed). Stage 1 (SFT) self-distills mode-conditioned behavior: for each query, the model samples multiple generations under forced SHORT/LONG templates, correctness-filtered demonstrations from each mode are pooled, and the model is fine-tuned on a mix of both (20K instances per mode) so it can fluently produce either style. Stage 2 (RPO) then optimizes only p_theta(z|x) -- the root token's probability -- via a per-mode group-relative advantage: for each prompt, n/2 rollouts are forced SHORT and n/2 forced LONG, each mode's rollout is rewarded by the success count of its per-prompt mode group (with a mild SHORT preference weight), advantages are standardized per-mode, and gradients are masked to update only the root gating token while all other tokens are discarded from the training graph -- with a KL penalty regularizing the root action's log-probability against the post-SFT reference policy. Because the dominant training-time activation memory term scales with the number of *updated* tokens (T), setting T=1 removes the linear dependence on long-CoT length that vanilla GRPO incurs.

## Results

On Peak VRAM (8xH100, 7B model, B=8 concurrent rollouts, 13K context): vanilla GRPO uses 436.34 GiB vs. RPO's 155.11 GiB (0.36x), and RPO+LoRA drops this further to 51.01 GiB (0.17x); a PFLOPs accounting on an 8B dense transformer shows RPO uses ~0.02x the total compute of AdaptThink (a comparable hybrid-reasoning RL baseline) at matched context. Across three model families/sizes (Qwen3-1.7B/8B/32B, Exaone4-1.2B, R1-1.5B), the Baseline->SFT->RPO pipeline improves the reasoning-per-accuracy ratio (RAR, lower is better) on most scenarios: on Qwen3-8B, Avg Think% drops from 57.3% to 44.8% while Avg Pass@1 stays close (63.8%->62.0%), improving RAR from 0.90 to 0.72; on Exaone4-1.2B, Think% drops from 43.4% to 23.6% with RAR improving 0.85->0.49. On R1-1.5B, RPO reaches 51.3 two-task average accuracy with RAR=0.96 at 20.5% Think%, versus AdaptThink's stronger absolute accuracy (56.5, RAR=0.74) but at a far larger training budget (RPO uses ~0.02x AdaptThink's compute per Table 5's PFLOPs accounting). Results extend beyond math to LiveCodeBench and GPQA-Diamond, where RPO's effect is model-size-dependent: it further compresses average decoding effort and lowers RAR on Qwen3-8B and Exaone4-1.2B, but on Qwen3-32B (where SFT alone already yields a near-baseline conservative router) RPO produces a comparable-but-not-strictly-better RAR (1.55 vs. 1.52). Reliability-diagram analysis of the root SHORT-confidence signal shows it correlates with correctness but weakly and dataset-dependently (ECE 0.2234/0.2214, correlation 0.420/0.383 on MATH500/AIME25) -- on the harder AIME25, confidence mass concentrates at low values so the router rarely assigns high SHORT confidence.

## Limitations

RPO's gain over the SFT operating point is configuration-dependent: on Qwen3-1.7B, post-SFT routing already saturates the achievable RAR so RPO yields a comparable rather than strictly better operating point; on Qwen3-32B (LoRA-tuned), SFT already produces a near-baseline conservative router so RPO likewise traces a comparable but not strictly dominating frontier. The method optimizes only a binary root routing decision and does not optimize intra-mode behaviors (how long to think, or when to stop mid-reasoning), which the paper states could further improve compute allocation. Root confidence, while informative for this branching-decision setting, can be sensitive to easy/hard query bucket composition and is weakly calibrated to true query difficulty. Broader evaluation under advanced agentic-tool-use benchmarks is left to future work, as is a more exhaustive ablation of RL training dynamics and generalizability of the root-token design choice, due to limited compute.

## Why it matters here

- **overthinking**: Directly relevant: it names overthinking as the motivating problem (uniform explicit reasoning applied regardless of query difficulty) and contributes an unusually cheap RL recipe for the think/no-think gating decision itself, arguing that most of what adaptive-reasoning methods need to learn is concentrated at a single branching token rather than distributed across the whole trajectory -- a strong, testable claim about *where* the decision to overthink or not actually gets made, complementary to methods elsewhere in this archive that intervene mid-trace or via length penalties.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), root-token gating, difficulty-aware policy optimization, per-mode group-relative advantage, reasoning-per-accuracy ratio (RAR)
- **Methods**: Root-token Policy Optimization (RPO), [GRPO (Group Relative Policy Optimization)](../../../../wiki/methods/grpo.md), self-distillation SFT for mode selection, [AdaptThink (baseline)](../../../../wiki/methods/adaptthink-baseline.md), [Thinkless (baseline)](../../../../wiki/methods/thinkless-baseline.md), Rejection Fine-Tuning (baseline)
- **Datasets**: [MATH500](../../../../wiki/datasets/math500.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [GPQA (Diamond)](../../../../wiki/datasets/gpqa-diamond.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), OpenR1-Math (SFT data source), s1 (compression dataset, partial)

Tags: `overthinking`, `adaptive-reasoning`, `reinforcement-learning`, `GRPO`, `training-efficiency`, `difficulty-aware-routing`

## Abstract

Large reasoning models (LRMs) achieve strong performance by externalizing explicit reasoning traces before producing the answer, yet suffer from overthinking challenge that allocates uniformly heavy computation to queries of varying difficulty. While proprietary models mitigate this via opaque routing, open-source LRMs still lack an efficient mechanism to internalize adaptive reasoning due to both expensive training cost and limited disclosure of training recipes. In response, we introduce RPO (Root-token Policy Optimization), a framework that enables LRMs to self-determine when to reason by training only the initial root token (e.g., whether to invoke the think tag) via group relative reward and group-wise advantages. By focusing on this pivotal branching point, RPO drastically reduces training overhead and VRAM usage. Across multiple model families and scales, RPO learns difficulty-aware adaptive thinking at just 2% of the training compute of prior adaptive-reasoning methods.

---

Record id: `doi:10.18653/v1/2026.acl-long.816`
