<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training

- **Authors**: Xucong Wang, Zhe Zhao, Liheng Yu, Di Wu, Xiaofeng Cao, Pengkun Wang
- **Venue**: cs.AI
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07147>
- **PDF**: <https://arxiv.org/pdf/2608.07147v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.50

## In one line

Assigns credit in coding-agent RL by splitting each code diff into sub-diffs, matching semantically similar sub-diffs across rollouts to form advantage groups, and projecting the resulting diff-level advantage back onto the tokens that produced it.

## Problem

In multi-turn coding agents a single action packs several unrelated changes into different regions of one code version, so an outcome or step-level reward cannot say which of the packed changes earned the reward. State-level grouping methods that recur across episodes do not help, because functionally analogous edits made in different regions of a file never match as identical states.

## Contributions

- Decomposes each code diff into contiguous sub-diffs and matches them across rollouts, so that functionally analogous edits in different code regions can be grouped where identical-state grouping cannot match them.
- A groupability score that multiplies saturating functions of semantic size and group mass, chosen over the additive form and over an LLM judge by ablation (31.3 against 24.4 and 21.5 on APPS).
- Two bounds: local credit bias is O(L*epsilon) in the anchor correspondence error under an L-Lipschitz local reward, and cross-rollout grouping reduces variance from non-causal trajectory components.
- An ablation separating the contribution of decomposition (6.3 points) from that of localised credit as such (7.5 points), and showing the episode-level advantage is indispensable.
- verl-code, an open-source agentic RL codebase covering several RL methods and coding benchmarks.

## Method

Coding is cast as a multi-turn MDP where each step emits a thought, an add/delete/none action and an observation from a sandbox, and only the final outcome is rewarded. All diffs from all steps of all rollouts of the same prompt are pooled, each tagged with its normalised size, its response-token span, its edit type and its task instance. Each diff is then enumerated into contiguous sub-diffs at multiple scales, and sub-diffs from different rollouts or steps are matched by a similarity combining token-level lexical matching with embedding similarity, restricted to the same edit type and thresholded at eta. Which splitting scale to use is chosen by a 'groupability score' that multiplies a saturating function of the sub-diff's semantic size by one of its group mass, so that neither a large but rare fragment nor a tiny but ubiquitous one is selected. Matched sub-diffs form an anchor; the anchor's group gives a local advantage by the same group-relative normalisation GRPO uses at the trajectory level, and that diff-level advantage is added to the trajectory-level advantage with a coefficient lambda at every token in the sub-diff's span. Two theorems bound the scheme: local credit bias is O(L*epsilon) in the correspondence error of the anchor match under an L-Lipschitz reward, and cross-rollout grouping reduces variance from non-causal trajectory components. Training is a cold start (7K template-augmented tasks, rollouts from Qwen3.6-27B, rejection-sampled to ~3K trajectories) followed by 2 SFT epochs and 120 RL epochs.

## Results

On two backbones over eight benchmarks. With Qwen2.5-Coder-7B the average rises from 35.3 (base) to 48.4, against 44.2 for GiGPO, 42.8 for GRPO and 42.7 for CodeRL+; with Qwen3.5-4B, 58.6 against 53.7 for GiGPO and 50.6 for GRPO. The margin over GRPO is 5.6 on average, and both share the same episode-level advantage, which is what makes it attributable to the sub-diff term. The largest single gain is on APPS Interview (+10.4 over GiGPO), where a solution spans several functions. On competition benchmarks the picture is much weaker in absolute terms: USACO 15.6 against GRPO's 6.8 for the 7B backbone, but 0.0 on the Platinum tier for every method including GPT-5.5's 42.9, and OJBench Hard at 1.9 against 1.2 for the 4B backbone. The gap to GPT-5.5 narrows from 56.4 points to 43.3 and does not close. Ablations: removing the episode-level advantage collapses APPS from 31.3 to 10.4, so the local signal cannot stand alone; removing the diff-level advantage gives 23.8, level with GRPO, isolating 7.5 points to localised credit; treating a whole diff as the atomic unit rather than decomposing gives 25.0, so 6.3 points come from splitting specifically. Multiplying size by mass beats adding them (31.3 against 24.4) and beats an LLM judge doing the grouping (21.5), which the authors attribute to the judge favouring a few large groups. lambda has an inverted-U response peaking at 1.2, reverting to GRPO below 0.6 and overfitting local credit above 1.2. Training overhead over GRPO is about 2.3 percent, and inference is unchanged. Training-dynamics curves show all methods equal for the first 20 steps and DiDPO separating from a plateauing GiGPO after step 40.

## Limitations

The paper states no limitations section. Reader-visible limits: the competition-level results are near the floor for every method the paper trains -- 0.0 on USACO Platinum and 1.2-1.9 on OJBench Hard -- so the claim is established on introductory and interview-level problems and is untested where long-horizon algorithmic reasoning is actually hard. The gap to GPT-5.5 remains 43.3 points. Anchor matching is quadratic in the number of sub-diff candidates, bounded only by the similarity threshold eta, and the reported 2.3 percent overhead is contingent on that threshold. The method is demonstrated on two backbones of 4B and 7B and one training corpus. The cold-start trajectories come from a much larger model, so part of the pipeline is distillation and the ablations do not separate it from the RL. Group-type classification in the dynamics analysis is done by GPT-5.5, so the claim that functional blocks come to dominate anchors rests on a model's labelling.

## Why it matters here

- **reasoning-training**: A concrete instance of the archive's recurring question about what the unit of credit should be in critic-free RL. The interesting result is the ablation rather than the headline: the localised signal contributes 7.5 points but collapses the method to 10.4 percent when the trajectory-level advantage is removed, so fine-grained credit is a refinement of outcome supervision and not a replacement for it. It also gives a rare measured comparison between a structural grouping rule and an LLM judge doing the same job, with the judge losing by nearly ten points -- evidence that where a cheap structural criterion exists, delegating the grouping to a model is worse as well as more expensive. The competition-tier floors are the honest counterweight: the gains land on problems the base model was already near, which is the difficulty-stratification caveat this archive keeps meeting.

## Entities

- **Concepts**: [credit assignment](../../../../wiki/concepts/credit-assignment.md), [verifiable reward](../../../../wiki/concepts/verifiable-reward.md), [outcome reward](../../../../wiki/concepts/outcome-reward.md), [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), [group-relative advantage](../../../../wiki/concepts/group-relative-advantage.md), [zero-advantage group](../../../../wiki/concepts/zero-advantage-group.md), long-horizon agency
- **Methods**: DiDPO, [GRPO](../../../../wiki/methods/grpo.md), [GiGPO](../../../../wiki/methods/gigpo.md), CodeRL+, CodeAct, Self-Planning, [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [rejection sampling](../../../../wiki/methods/rejection-sampling.md), groupability score
- **Datasets**: APPS, [HumanEval](../../../../wiki/datasets/humaneval.md), [MBPP](../../../../wiki/datasets/mbpp.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), LeetCode, USACO, OJBench, ICPC

Tags: `rlvr`, `coding-agent`, `credit-assignment`, `code-diff`, `agentic-rl`

## Abstract

Reinforcement learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for training coding agents, where the execution feedback from compilation and tests provides objective verification. However, unlike agent tasks, coding agents face a unique and finer-grained credit assignment challenge: at each step, coding actions simultaneously pack varying changes into different regions of a code version, which makes the contribution of independent change indistinguishable. Existing RLVR methods mostly leverage the outcome reward or step-level reward, which fails to dive into a code diff and makes unique properties of coding actions invisible to training. In this paper, we propose Diff-in-Diff Policy Optimization (DiDPO), a critic-free RL method that constructs fine-grained credit units directly from the structure of code diffs. DiDPO organizes multi-turn coding interactions into multiple thought--action steps and discovers code diffs across sampled trajectories. It then selects anchors by aggregating highly similar sub-diffs split from each whole diff by our ``groupability score'', which provides the splitting schema that optimally balances the semantic scope of anchors and the group mass they may form. Finally these anchors form advantage groups and project the diff-level advantage back to individual response tokens. Experiments on long-horizon coding and reasoning benchmarks show that DiDPO significantly outperforms strong agentic RL baselines. On Qwen2.5-7B-Coder, DiDPO exceeds comparable methods by over 10\% and narrows the gap with far larger models, offering a principled framework for fine-grained credit assignment in coding agent training. We also open-source verl-code, an agentic rl codebase that supports various RL methods and coding benchmarks.

---

Record id: `arxiv:2608.07147`
