<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# PAM: Enhancing General Alignment of Large Reasoning Models through Priority-Aware Metacognition

- **Authors**: Zhihao Xu, Fuzhen Yang, Liang Lin, Xiting Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.432/>
- **PDF**: <https://aclanthology.org/2026.acl-long.432.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.432
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

PAM trains large reasoning models to explicitly assess which human-preference priority (e.g. harmlessness) applies to a query before reasoning -- via a Flavell-metacognition-inspired cold-start SFT stage plus DPO preference optimization -- improving helpfulness, harmlessness and instruction-following by an average of ~10 points over an identically-trained model without this metacognitive step, without a corresponding drop in math reasoning performance for one of two backbones.

## Problem

Large reasoning models' System-2 chain-of-thought capability does not reliably transfer to general alignment: stronger reasoning does not consistently make responses safer, more helpful or more instruction-following, and simply enabling more CoT can even increase hallucination or harmfulness, while suppressing CoT entirely improves safety at the cost of helpfulness and instruction-following -- current work mostly improves LRMs' raw reasoning-task performance without addressing how to make that reasoning capability translate into better-aligned general-purpose behavior.

## Contributions

- an empirical demonstration that having a reasoning model first identify the top-priority human preference relevant to a query (before detailed reasoning) improves helpfulness, harmlessness and instruction-following simultaneously, in contrast to either standard CoT (safety-vulnerable) or suppressed CoT (helpfulness-degrading)
- PRIORITY-AWARE METACOGNITION (PAM), a two-stage training pipeline (metacognitive cold-start SFT + DPO/GRPO preference optimization) that instills this priority-assessment capability directly into the model, grounded in Flavell's metacognitive-knowledge framework
- consistent alignment gains of ~10 points on average across helpfulness/harmlessness/instruction-following benchmarks over an identically-trained non-metacognitive baseline, across two backbone architectures and multiple RL algorithms
- ablations confirming the metacognition mechanism (not distillation source, not fine-grained reward alone) is the causally necessary component, and that its benefit composes with, rather than substitutes for, standard RLHF-style training

## Method

Motivated by Flavell's metacognition framework (knowledge of tasks, of self, of strategies), PAM's core idea is that priority understanding (which human preference -- e.g. harmlessness, helpfulness -- should be prioritized for a given query) can serve as a unifying lens for a model to interpret an alignment task's nature before reasoning. A preliminary study compares standard CoT, Zero-CoT (no reasoning), and a training-free Priority-Aware CoT prompt intervention, finding the latter improves helpfulness, harmlessness and instruction-following simultaneously without any training, motivating a full two-stage pipeline. Stage 1 (cold start): GPT-4-mini generates structured metacognitive-knowledge annotations (task priority + justification + reflection on potential pitfalls + strategy) for a seed prompt set, wrapped in a special <meta_cognition> token span; the base LRM is then guided (via an instructional chat-template cue forcing consistency between the metacognitive guidance and the subsequent reasoning) to sample coherent CoT-and-answer trajectories conditioned on this metacognitive knowledge, and the model is SFT'd to jointly generate the metacognition block, the CoT, and the final answer. Stage 2 (preference optimization): for each prompt, n=8 responses are sampled from the SFT'd policy, scored by a reward model (by default using only the final-answer reward, though a fine-grained LLM-as-judge variant separately scoring the metacognition block's quality and its consistency with the CoT is also tested), and DPO (or GRPO) is applied using the highest- and lowest-reward responses as the preference pair.

## Results

Across two backbones (DeepSeek-Distill-Qwen-7B, DeepSeek-Distill-LLaMA-8B) and three training regimes (SFT only, +DPO, +GRPO), the metacognition-equipped model (PAM-RM) consistently outperforms an identically-trained model without metacognition (Vanilla-RM) on helpfulness (AlpacaEval2 win rate), harmlessness (Advbench/WildJailbreak harmless rate) and instruction-following-adjacent reasoning is separately tracked via MATH500/AIME24. With DPO, PAM-RM improves over Vanilla-RM by +3.05 to +8.82 points on helpfulness and +1.73 to +18.50 points on harmlessness across both backbones (up to 99.61-99.80% Advbench harmless rate); with GRPO, gains reach +5.96/+8.82 helpfulness and +1.73/+4.42-18.50 harmlessness, and GRPO outperforms DPO overall, indicating metacognition is complementary to (not a substitute for) online RL. Reasoning performance effects diverge by backbone: for R1-Qwen-7B, general-domain alignment training causes almost no drop in MATH500/AIME24 accuracy; for R1-LLaMA-8B, reasoning performance declines noticeably under both variants, though PAM-RM still outperforms Vanilla-RM, and the paper speculates possible pretraining data contamination as a partial explanation for this backbone-specific reasoning sensitivity rather than a general property of the method. An ablation removing metacognitive guidance at inference time (forcing an early </meta_cognition> close tag) causes PAM-RM's performance to drop across all three benchmarks, most severely on the jailbreak-style WildJailbreak dataset, confirming the metacognition step is causally load-bearing rather than a superficial formatting artifact. A reward-design ablation shows adding fine-grained (LLM-as-judge-scored) rewards for the metacognition and CoT quality on top of the answer-only reward further improves harmlessness (e.g. WildJailbreak harmless rate rising to 83.25%/89.25% across backbones) at a modest helpfulness cost, and a cold-start-data ablation shows self-generated metacognition data (by the reasoning model itself, PRM-Self) performs comparably to GPT-4-mini-distilled data (PRM-Distill), indicating the benefit comes from the metacognitive mechanism itself rather than knowledge distillation from a stronger teacher.

## Limitations

Constrained by computational resources, experiments are limited to 7B-8B-scale models; the paper states future work should include larger-scale models to more comprehensively assess the role of metacognitive knowledge in reasoning models. The study focuses primarily on English-language tasks; extending the approach to other languages and task settings is identified as an important direction. The work leverages metacognitive knowledge specifically for LRM alignment, and the paper suggests future research could incorporate a wider range of metacognitive theories to further enhance reasoning-model training, implying the current Flavell-based formulation is not treated as exhaustive.

## Why it matters here

- **overthinking**: Tangential: this is about general alignment (helpfulness/harmlessness/instruction-following), not reasoning length or the accuracy/efficiency tradeoff, but its motivating observation -- that enabling more chain-of-thought does not uniformly improve behavior and can increase hallucination or harm (citing prior work directly relevant to this archive's concerns), while simply suppressing reasoning trades away helpfulness -- parallels the overthinking literature's core finding that 'more thinking' is not unconditionally beneficial. Its priority-aware metacognition mechanism (assess the task's nature before committing to a reasoning strategy) is structurally similar to difficulty-cognition approaches elsewhere in this archive that gate reasoning depth on an upfront self-assessment, applied here to alignment priorities rather than problem difficulty.

## Entities

- **Concepts**: metacognitive knowledge (Flavell's framework: task/self/strategy), priority-aware reasoning, metacognition-guided rejection sampling, fine-grained metacognition + CoT reward
- **Methods**: PAM (Priority-Aware Metacognition, SFT cold start + DPO/GRPO), metacognition-guided rejection sampling, LLM-as-judge fine-grained reward
- **Datasets**: AlpacaEval2.0, [AdvBench](../../../../wiki/datasets/advbench.md), [WildJailbreak](../../../../wiki/datasets/wildjailbreak.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME24](../../../../wiki/datasets/aime-2024.md), UltraFeedback (training), SafeRLHF-10K (training), HelpSteer2 (training)

Tags: `alignment`, `metacognition`, `safety`, `large-reasoning-models`, `preference-optimization`

## Abstract

Recent advancements in Large Reasoning Models (LRMs) have showcased strong performance across various reasoning tasks by leveraging System-2 thinking capabilities. However, existing studies indicate that this reasoning ability alone does not reliably transfer to the general alignment domain. Inspired by cognitive science and how humans solve tasks, we argue that LRMs must be equipped with metacognitive knowledge to fully utilize their System-2 capabilities. In this paper, we propose Priority-Aware Metacognition (PAM), which guides the model to first identify the top-level human preference (e.g., harmlessness) as a means of understanding the alignment task’s nature, and then apply other kinds of metacognitive knowledge to better monitor and regulate the model’s thinking process. We implement PAM via a two-stage pipeline: a cold-start phase that collects structured metacognitive knowledge based on Flavell’s theoretical framework, and a preference-optimization phase that further reinforces such metacognition. Extensive experiments validate the effectiveness of PAM. Under the same training pipelines, PAM consistently yields higher performance, improving general domain alignment performance by ~10 points on the helpfulness and harmless benchmarks. Code is available at https://anonymous.4open.science/r/PAM-RM-02DF.

---

Record id: `doi:10.18653/v1/2026.acl-long.432`
