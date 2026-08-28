<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization

- **Authors**: Junyi Li, Yongqiang Chen, Ningning Ding
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.143/>
- **PDF**: <https://aclanthology.org/2026.acl-long.143.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.143
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

CiPO reframes unlearning for large reasoning models as counterfactual intervention on the chain-of-thought: it has the target model generate a logically valid counterfactual reasoning trace and answer, then iteratively preference-optimizes the model toward that counterfactual (SimPO loss against online-sampled dispreferred responses), removing sensitive knowledge from both intermediate CoT and final answers while preserving reasoning ability better than prior unlearning baselines.

## Problem

Machine unlearning for standard LLMs targets only the final output, but large reasoning models expose their internal deliberation as an explicit chain-of-thought, so unwanted knowledge can leak through the reasoning trace itself even when the final answer looks clean; existing LRM unlearning strategies either suppress reasoning representations directly (degrading CoT interpretability and reasoning ability, e.g. R2MU) or train a refusal response (introducing new privacy risks via a detectable refusal pattern and causing over-rejection on safe queries, e.g. ReasonedIDK).

## Contributions

- a causal reformulation of LRM unlearning as intervening on both the reasoning trace and the answer to achieve conditional independence from the forget set
- CiPO, a self-contained (no external teacher) counterfactual-generation-plus-iterative-preference-optimization framework for LRM unlearning
- state-of-the-art unlearning-utility trade-off versus GA/GD/NPO/IDK-style/R2MU baselines on both a synthetic benchmark (R-TOFU) and a real-world evaluation (RETURN), replicated across two backbones
- an ablation isolating the necessity of warmup SFT, the SimPO preference term, the NLL term, and the iterative (vs. fixed) sampling procedure

## Method

Frames LRM unlearning via a causal graph over question Q, chain-of-thought C, answer A, and the forget set F, with the objective of achieving the post-intervention distribution do(F -> {C,A}) so C and A become independent of F given Q. CiPO's counterfactual generator has the target model itself (self-contained, no external teacher) generate a counterfactual answer that changes the forgotten fact, then backward-reasons a coherent, in-distribution CoT trace leading to it, forming a fixed preferred set. Iterative preference optimization then, at each round, samples the current model's own real-time (dispreferred) response to the forget-set question, pairs it with the fixed counterfactual (preferred) response, and optimizes a SimPO-style reference-free loss plus an NLL term boosting the counterfactual's likelihood and a retain-loss term preserving behavior on the retain set -- keeping the preference signal aligned with the model's evolving distribution across iterations rather than a fixed off-policy pair.

## Results

On the R-TOFU benchmark (Forget01/05/10 splits, 1%/5%/10% of training instances) with a DeepSeek-R1-Distill-Llama-8B-based target model, CiPO achieves the most favorable utility-forgetting trade-off among all compared methods (GA, GD, NPO, DirectIDK, AnswerIDK, ReasonedIDK, R2MU): e.g. on Forget10, Answer-level Forgetting Efficacy 0.5169, CoT-level Forgetting Efficacy 0.5730, Model Utility 0.6629, versus gradient-ascent variants (GA/GD) reaching near-perfect forgetting but catastrophic utility collapse (MU as low as 0.0-0.2877), NPO showing instability/collapse signs, and IDK/R2MU variants improving forgetting at the cost of suppressed reasoning, excessive refusal, or unstable competency metrics. On a real-world unlearning evaluation (RETURN dataset, LLM-as-judge on 260 QA pairs about public figures' private information, DeepSeek-R1-Distill-Llama-8B target), CiPO reaches ForgetACC 0.3178, CoT-UA (CoT leakage) 0.4446, RetainACC 0.8148 (best among all methods), while GA/NPO lose reasoning ability entirely (CoT-UA undefined) and IDK-style methods over-refuse on the retain set. Results replicate on a second backbone (DeepSeek-R1-0528-Qwen3-8B) with consistent trends. Ablations show removing the warmup SFT stage, the SimPO term, the NLL term, or the iterative (vs. fixed-sample) procedure each substantially degrades either forgetting efficacy or utility, confirming all components are necessary.

## Limitations

Extending CiPO beyond factual forgetting in QA-style settings to other training data formats is left to future work and would require additional adaptation. The paper notes unlearning is not a guarantee under adversarial prompting -- leakage may persist -- so it recommends responsible governance and periodic auditing rather than treating CiPO as a complete safety solution. R-TOFU's CoT traces are GPT-4o-synthesized and may not fully reflect real-world reasoning behavior, which motivated but does not fully substitute for the separate real-world evaluation.

## Why it matters here

- **overthinking**: Only loosely connected to the topic: this is a privacy/unlearning paper, not about reasoning length or the accuracy/efficiency tradeoff. Its relevance is that it treats the chain-of-thought as a first-class object carrying information beyond the final answer (a leakage vector here, rather than wasted computation) -- a reminder that reasoning-trace content, not just its length, is a live research target, and that interventions on CoT (like the length-focused ones common in this archive) must also reckon with what the trace itself semantically preserves or discards.

## Entities

- **Concepts**: counterfactual unlearning, causal-intervention view of LRM unlearning (do(F->{C,A})), iterative/online preference optimization, CoT-level vs. answer-level forgetting
- **Methods**: CiPO (counterfactual unlearning via iterative preference optimization), [SimPO](../../../../wiki/methods/simpo.md), R2MU (baseline), ReasonedIDK / DirectIDK / AnswerIDK (baselines), Gradient Ascent / Gradient Descent (GA/GD, baselines), NPO (baseline)
- **Datasets**: R-TOFU (Forget01/05/10), RETURN

Tags: `machine-unlearning`, `large-reasoning-models`, `chain-of-thought`, `preference-optimization`, `privacy`

## Abstract

Machine unlearning has gained increasing attention in recent years, as a promising technique to selectively remove unwanted privacy or copyrighted information from Large Language Models that are trained on a massive scale of human data. However, the emergence of Large Reasoning Models (LRMs), which emphasize long chain-of-thought (CoT) reasoning to address complex questions, presents a dilemma to unlearning: existing methods either struggle to completely eliminate undesired knowledge from the CoT traces or degrade the reasoning performances due to the interference with the reasoning process. To this end, we introduce Counterfactual Unlearning through iterative Preference Optimization (CiPO), a novel framework that redefines unlearning as the targeted intervention of the CoT reasoning in LRMs. More specifically, given a desired unlearning target answer, CiPO instructs LRMs to generate a logically valid counterfactual reasoning trace for preference tuning. As the LRM adjusts to the counterfactual trace, CiPO iteratively updates the preference learning data to increase the discrepancy from the original model. This iterative loop ensures both desirable unlearning and smooth optimization, effectively mitigating the dilemma. Experiments on challenging benchmarks demonstrate that CiPO excels at unlearning, completely removing knowledge from both the intermediate CoT steps and the final answer, while preserving the reasoning abilities of LRMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.143`
