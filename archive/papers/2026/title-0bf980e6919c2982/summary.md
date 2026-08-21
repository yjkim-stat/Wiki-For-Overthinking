<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64198>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.

## Problem

Large reasoning models generate verbose chains, and the usual efficiency remedy is a token-length penalty. The authors argue that penalising token volume indiscriminately also compresses the reasoning that is doing work inside each step. The open question they pose is how to remove structural redundancy - steps that repeat each other, or steps that skip a required inference - while leaving the depth of reasoning within a step free to grow.

## Contributions

- Argues that reasoning inefficiency is structural redundancy between steps rather than token volume, and separates the two by budgeting segments instead of tokens
- Introduces a split-merge refinement algorithm in which an LLM consistency judge merges semantically redundant adjacent segments and splits segments containing implicit logical jumps
- Adds a structure-aligned RL stage whose reward penalises segment-count deviation beyond a one-step tolerance, reporting +3.3 accuracy points and 28.7% fewer segments on average against efficiency baselines

## Method

CoSMo (Consistency-Guided Split-Merge Optimization) treats a reasoning chain as a sequence of discrete segments and compares the segment count against a reference count for the problem. If the chain has too many segments, a merge pass fuses adjacent ones wherever an LLM-based consistency judge finds them semantically redundant; if it has too few, a split pass decomposes a coarse segment into finer steps where the judge finds an implicit logical jump. The judge is what keeps the refinement from breaking coherence. The refined chains are used for supervised fine-tuning, and then for structure-aligned reinforcement learning with GRPO under a three-part reward: format adherence, answer correctness, and a structural term that penalises deviation of the segment count from the target beyond a one-step tolerance. Because the penalty is on segment count and not on tokens, the model may expand reasoning within a segment without cost as long as the overall chain topology stays at the intended size.

## Results

Averaged over the benchmarks, CoSMo reports a 3.3-point accuracy gain and 28.7% fewer segments than reasoning-efficiency baselines, reaching the lowest segment counts in the comparison at about 2.9 segments on average. Baselines span prompting and training methods: CoT, ToT, HTP, CoD, TALE, C3oT, FS-BoN, SPIRIT, LCPO and ThinkPrune. Backbone is Llama-3.1-8B-Instruct, with Qwen-2.5-7B-Instruct in the appendix. HotpotQA and HaluEval are in-distribution; Natural Questions and CRAG are the out-of-distribution split. The ablation separates the two halves: the SFT stage alone beats C3oT by 1.0 accuracy point with 19% fewer tokens, while the RL stage alone gains 3.2 accuracy points but increases segment count - the headline efficiency number comes from the combination, not from the RL objective on its own.

## Limitations

The paper does not present a limitations section in the material available. Two are visible from the setup. The split-merge target depends on ground-truth hop counts during training, so the method presumes a dataset that annotates how many reasoning steps a question requires - which is why the evaluation is multi-hop and hallucination QA rather than mathematics or code, where no such annotation exists, and generalisation to unannotated domains is not demonstrated. Second, the efficiency metric is segments rather than tokens: since the design deliberately allows intra-segment reasoning to grow, a 28.7% reduction in segments is not a 28.7% reduction in compute, and only the SFT ablation reports a token figure (19%). Wall-clock or token-level savings for the full method are not stated in the material seen.

## Why it matters here

- **overthinking**: On topic, and useful mainly for the distinction it draws: it separates 'the chain has too many steps' from 'the chain has too many tokens', and claims a length penalty conflates them. That gives the group a second axis for the accuracy/efficiency tradeoff, and a concrete mechanism - merge redundant steps, split skipped ones - that treats under-thinking symmetrically with over-thinking, which most length-penalty work does not. Two caveats matter for how it is filed. It needs annotated reasoning depth to set the target, so it is evaluated on multi-hop QA (HotpotQA, HaluEval, NQ, CRAG) rather than on the math and code benchmarks the rest of this topic uses, and its headline efficiency number is in segments, an internally defined unit whose relation to tokens or latency is not given for the full method. Compare against ThinkPrune and LCPO, which appear here as baselines.

## Entities

- **Concepts**: [Overthinking](../../../../wiki/concepts/overthinking.md), Structural Redundancy, Reasoning Segment, Segment-Level Budget, [Length Penalty](../../../../wiki/concepts/length-penalty.md), [Accuracy-Efficiency Tradeoff](../../../../wiki/concepts/accuracy-efficiency-tradeoff.md), Consistency Judging
- **Methods**: CoSMo, split-merge algorithm, consistency judge (LLM-based), structure-aligned reinforcement learning, [GRPO](../../../../wiki/methods/grpo.md), segment-level budget, [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md)
- **Datasets**: [HotpotQA](../../../../wiki/datasets/hotpotqa.md), HaluEval, Natural Questions, CRAG

Tags: `overthinking`, `efficient-reasoning`, `chain-of-thought`, `reinforcement-learning`, `grpo`, `structural-redundancy`, `multi-hop-qa`, `segment-budget`

---

Record id: `title:0bf980e6919c2982`
