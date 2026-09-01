<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62304>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.

## Problem

Reasoning segmentation asks a multimodal LLM to interpret an indirect text query and output a mask for the object it denotes. Models trained with RL on this task produce verbose reasoning chains, and the paper's claim is that the verbosity is not merely wasteful but actively harmful: long chains disperse attention and interfere with object localisation. Suppressing length directly would need supervision over what the thinking should look like, which does not exist for this task, so the open question is how to penalise overthinking using only signals the model can generate about itself.

## Contributions

- The observation that in reasoning segmentation verbose chains interfere with object localisation rather than merely costing tokens, attributed to attention dispersion
- A two-stage rollout that decomposes the task into multimodal reasoning (produce a self-contained description) and referring segmentation (re-solve from the description alone)
- A description self-reward that verifies self-containment by checking whether the second pass answers correctly from image plus description only
- A length-based self-reward, clip(I[N2<N1] - gamma*max(0, N1-N0), 0, 1), rewarding shorter description-conditioned reasoning against a length anchor
- A self-rewarding framework needing no extra thinking supervision, reaching gIoU 68.5/66.1 on ReasonSeg val/test versus 65.4/62.3 with about 3x fewer reasoning tokens (26.9 vs 85.3)

## Method

DR2Seg is a self-rewarding RL framework built on a two-stage rollout that decomposes the task. In the first stage the model is given the image and the original complex query and must emit a self-contained description D that explicitly names and specifies the target object. In the second stage that description replaces the original query: the model is run again on the image plus D alone, which tests whether D really is self-contained. This decomposition is what makes the self-rewards possible, since correctness in the second stage is a property the model can check without external annotation of the reasoning. Two rewards follow. A description self-reward checks whether the second pass, given only image and D, still produces the correct answer. A length-based self-reward compares the reasoning lengths of the two stages against a length anchor N0, in the form clip(I[N2 < N1] - gamma * max(0, N1 - N0), 0, 1), so the model is rewarded when the description-conditioned pass reasons more briefly than the query-conditioned pass and penalised as the first-stage chain runs past the anchor. Together these target overthinking and the attention dispersion the paper attributes to it, with no extra thinking supervision. Masks are produced by an off-the-shelf segmenter.

## Results

Base models are Qwen2.5-VL at 3B and 7B, with SAM2-Large and SAM3 as the segmentation backends; training data is the VisionReasoner-7K set built from LVIS, RefCOCOg, gRefCOCO and LISA++. On ReasonSeg at 7B with SAM2, DR2Seg reaches gIoU 68.5 on validation and 66.1 on test, against VisionReasoner at 65.4 and 62.3 - roughly 3 to 4 points. The efficiency figure is a roughly 3x reduction in reasoning tokens, 26.9 against 85.3 for VisionReasoner. On the simpler referring benchmarks the gain largely disappears: RefCOCO testA is 79.3 for DR2Seg-7B against 78.8 for the baseline, which is consistent with the paper's own account, since RefCOCO queries are direct and leave little to overthink. Gains are reported as consistent across the 3B and 7B variants and across both SAM2 and SAM3.

## Limitations

The paper does not state limitations. A reader should notice that the length-based reward is anchored on a hyperparameter N0 whose sensitivity is shown in the ablations, so the amount of compression is set by tuning rather than derived from the task. The two-stage rollout doubles generation per training step, so the reasoning-token saving is an inference-time saving bought with training-time cost, and no training-compute comparison is given. The description self-reward treats a correct second-pass answer as proof that D was self-contained, which can be satisfied by a description that is right for the wrong reason or by an image where the segmenter would have found the object anyway. The near-tie on RefCOCO (79.3 vs 78.8) shows the method contributes little where queries are already direct, so the headline holds for the reasoning-heavy ReasonSeg setting specifically. The mechanism claim - that verbose chains cause attention dispersion which harms localisation - is motivated rather than isolated by an experiment that separates length from content. Results are confined to segmentation, at 3B and 7B, on one training set.

## Why it matters here

- **overthinking**: On topic, and it is the stronger form of the group's thesis: not that long reasoning wastes compute, but that it degrades the answer. DR2Seg reports gIoU rising from 65.4 to 68.5 on ReasonSeg validation while reasoning tokens fall from 85.3 to 26.9 - accuracy and length moving in the same favourable direction, which is the case worth collecting because it removes the tradeoff framing entirely. The proposed mechanism, attention dispersion in a multimodal model where the reasoning tokens compete with the visual grounding the mask depends on, is a specific reason why overthinking should hurt in grounded tasks more than in text-only ones, and is a hypothesis the group could test elsewhere. The method is also instructive as a way of getting a length signal without length supervision: rather than penalising tokens directly, DR2Seg asks whether a compressed restatement still suffices, so brevity is verified rather than merely rewarded. Two things bound the reading. The mechanism is asserted rather than isolated - no experiment separates chain length from chain content - and the near-tie on RefCOCO (79.3 vs 78.8) confirms the effect only appears where queries are indirect enough to overthink. The compression ratio is also anchored on a tuned hyperparameter N0, so the 3x figure is a chosen operating point rather than a discovered one.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Attention Dispersion, Self-Rewarding, [Task Decomposition](../../../../wiki/concepts/task-decomposition.md), Self-Contained Description, [Length Reward](../../../../wiki/concepts/length-reward.md), [Reasoning Segmentation](../../../../wiki/concepts/reasoning-segmentation.md), Rollout Design, Reinforcement Learning with Verifiable Rewards
- **Methods**: DR2Seg, two-stage rollout, self-rewarding reinforcement learning, description self-reward, length-based self-reward, [Qwen2.5-VL](../../../../wiki/methods/qwen2-5-vl.md), SAM2, SAM3, VisionReasoner (baseline), PixelThink (baseline), [Seg-Zero (baseline)](../../../../wiki/methods/seg-zero-baseline.md), SAM-R1 (baseline), LISA (baseline)
- **Datasets**: [ReasonSeg](../../../../wiki/datasets/reasonseg.md), [RefCOCO](../../../../wiki/datasets/refcoco.md), [RefCOCO+](../../../../wiki/datasets/refcoco.md), [RefCOCOg](../../../../wiki/datasets/refcocog.md), VisionReasoner-7K, LVIS, gRefCOCO, [LISA++](../../../../wiki/datasets/lisa.md)

Tags: `overthinking`, `efficient-reasoning`, `self-rewarding`, `reasoning-segmentation`, `multimodal`, `reinforcement-learning`, `length-reward`, `attention-dispersion`

---

Record id: `title:56bdffcf992c5e91`
