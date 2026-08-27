<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Red Teaming Large Reasoning Models

- **Authors**: Jiawei Chen, Yang Yang, Chao Yu, Yu Tian, Zhi Cao, Xue Yang, Linghao Li, Hang Su, Zhaoxia Yin
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1034/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1034.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1034
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Rt-LRM is a unified 30-task benchmark evaluating large reasoning models along truthfulness, safety and efficiency, testing both CoT-hijacking (direct interference with the reasoning process) and prompt-induced impacts (jailbreaks or overthinking triggers); across 26 models it finds LRMs are consistently less trustworthy than their own base LLMs, that explicit reasoning can amplify safety risk and inefficiency under attack, and that over 60% of tested samples exhibit overthinking (more than double the clean-input token count) across most models.

## Problem

Large reasoning models introduce novel safety and reliability risks specific to their explicit multi-step chain-of-thought -- CoT-hijacking (adversaries injecting misleading reasoning paths to produce untruthful or unsafe outputs) and prompt-induced impacts (covert triggers causing unnecessary reasoning, i.e. overthinking, or jailbreaks) -- that existing evaluation benchmarks do not capture jointly, since prior work typically targets a single failure mode in isolation, lacks paired LRM-vs-base-LLM comparisons, and cannot disentangle reasoning-specific failures from general model weaknesses.

## Contributions

- Rt-LRM, a unified 30-task benchmark systematically evaluating LRM trustworthiness across truthfulness, safety, and efficiency, with a reasoning-centered evaluation strategy targeting both CoT-hijacking risks and prompt-induced impacts jointly
- a standardized, modular, extensible evaluation toolbox with task-specific metrics (Accuracy, ASR, Toxicity Score, Overthinking Rate, Reasoning Time) and paired LRM-vs-base-LLM comparisons that isolate reasoning-specific vulnerabilities from general model weaknesses
- extensive experiments across 26 models revealing that LRMs are systematically less trustworthy than their own base LLMs, that trustworthiness declines with task complexity, that safety risks are widespread across training paradigms, and that most LRMs exhibit high overthinking rates (over 60% of samples for many models) even on moderately complex or adversarially-triggered prompts

## Method

Rt-LRM curates 30 tasks across three dimensions: truthfulness (9 tasks, split into objective-truth tasks like proportional operations and compositional calculations, and conceptual-truth tasks like controversial issues, stereotypes, misconceptions, fictional content, factual information and conspiracy theories, measured by Accuracy), safety (10 tasks spanning societal harms -- economic crime, violence, copyright violations, general illicit scenarios, chemical/biological threats, cybercrime, misinformation, harassment -- and personal harms -- self-harm, sexual crime -- measured by Attack Success Rate and Toxicity Score via PerspectiveAPI), and efficiency (11 tasks split into computational efficiency -- mathematical QA, symbolic reasoning, multiple-choice reasoning, basic word problems, code generation, recursive reasoning -- and reasoning efficiency -- general reasoning, proof-based reasoning, high-level symbolic reasoning, generalization testing, and a dedicated Overthinking Induction task that directly injects prompt triggers designed to cause excessive reasoning), measured by Overthinking Rate (OR, the fraction of samples where token usage with a trigger exceeds 2x the clean-input token count) and reasoning time. Datasets are built from scratch (6), refined from existing sources (4), or augmented with additional prompts (9) under a unified evaluation protocol; automatic evaluation uses GPT-4o (validated against human labels: F1 0.88 truthfulness, 0.86 safety, Cohen's kappa 0.80/0.72) or rule-based keyword matching depending on task. Evaluates 26 models spanning four training-strategy categories (SFT+RL, RL-only, SFT-only, proprietary) including matched LRM/base-LLM pairs (e.g. DeepSeek-V3/R1, Qwen3-32B Instruct/LRM, GLM-4-9B/GLM-4-Z1-9B) to isolate reasoning-specific effects from general model differences.

## Results

LRMs exhibit weaker trustworthiness than their own base LLM counterparts across all three dimensions: e.g. GLM-4-Z1-32B (LRM) shows ASR 70.06% versus GLM-4-32B-Base's 53.84%, and DPSK-Qwen-32B (LRM) shows Overthinking Rate 78.50% versus Qwen2.5-32B-Base's 56.50% -- attributed to explicit reasoning mechanisms introducing additional vulnerability surfaces exploitable by CoT-hijacking and prompt-induced attacks, directly contradicting an assumption that stronger reasoning universally improves trustworthiness. Trustworthiness challenges are widespread: many open models (Qwen and GLM variants) show ASR>50% and over 60% of samples exhibiting overthinking; proprietary models are relatively superior but still show critical vulnerabilities -- Claude-Sonnet-4 achieves the best truthfulness (54.33% accuracy) and lowest ASR (30.05%), while o1/o3-mini lead on efficiency (Overthinking Rate below 22%), yet even these models show non-trivial residual risk. Truthfulness declines sharply with task complexity/context-dependence: Claude drops from 60.61% (T.2, compositional calculations) to 42.29% (T.3, contextualized problem solving), and GLM-4-Z1-32B drops from 30.30% to 24.57% on the same tasks, suggesting LRMs often rely on superficial pattern matching rather than deep reasoning as complexity grows. Persistent safety risks appear across both societal and personal-harm categories regardless of training paradigm: MiMo-RL reaches 97.06% ASR on self-harm (S.4) and DeepMath scores 94.29% ASR on copyright violations (S.3); Claude-4 consistently maintains the lowest violation rates across all tasks. LRMs consistently exhibit high Overthinking Rate across tasks: GLM-4-Z1-32B shows OR above 70% across all 11 efficiency tasks, indicating systemic inefficiency even on moderately complex prompts; even Claude-Sonnet-4, among the most efficient models tested, fails on one generalization-testing task (E.8) with a 94% OR, showing models entering unnecessary extended reasoning rather than terminating early or avoiding illogical paths when confronted with adversarially constructed prompts (implicit loops, ambiguous logic, distractive signals). Training-strategy correlations (correlational, not causal, given confounds): SFT+RL models generally show higher truthfulness and stronger safety alignment while maintaining efficiency comparable to RL-only models; RL-only models achieve lower overthinking rates but consistently underperform on truthfulness and safety; SFT-only models show a more balanced but non-leading profile across all three dimensions.

## Limitations

Despite covering 30 tasks across mathematical reasoning, code generation, and safety evaluations, the benchmark does not fully capture the breadth of emerging and increasingly complex risk patterns, especially those arising in cross-modal reasoning, long-horizon planning, or real-world multi-step reasoning scenarios. While the paper discusses several potential defense strategies (training-time alignment, inference-time defenses like overthinking monitors, external guard models), these ideas are not yet evaluated within the Rt-LRM framework itself; the authors plan to integrate and systematically compare such defenses in future work. The training-strategy correlations reported (Takeaway #6) should be interpreted as correlational rather than causal, since the compared models differ in confounded factors such as pretraining data, system prompts, and post-training pipelines that cannot be strictly controlled at scale.

## Why it matters here

- **overthinking**: Directly central to the topic: efficiency (specifically overthinking, operationalized as the Overthinking Rate metric) is one of the benchmark's three core evaluation dimensions, with a dedicated Overthinking Induction task and 10 other efficiency tasks measuring token waste. Its key finding that most LRMs exhibit high overthinking rates (over 60% of samples for many models, and GLM-4-Z1-32B exceeding 70% OR across all 11 efficiency tasks) even under adversarially-designed prompts specifically engineered to induce unnecessary reasoning is a systematic, large-scale (26-model) quantification of overthinking's prevalence and its interaction with adversarial input design -- and its finding that LRMs are less efficient (and less safe) than their own base LLMs directly ties overthinking to the reasoning capability itself rather than to model scale or training data alone.

## Entities

- **Concepts**: CoT-hijacking risk, prompt-induced impact (overthinking trigger, jailbreak), Overthinking Rate (OR), Attack Success Rate (ASR), objective truth vs. conceptual truth, societal vs. personal safety
- **Methods**: CoT-hijacking attack tasks, prompt-induced overthinking-trigger tasks, GPT-4o automatic evaluation (validated against human labels), Overthinking Rate metric (token ratio > 2x threshold)
- **Datasets**: Rt-LRM (new, 30 tasks: 9 truthfulness, 10 safety, 11 efficiency)

Tags: `overthinking`, `safety`, `benchmark`, `trustworthiness`, `cot-hijacking`

## Abstract

Large Reasoning Models (LRMs) have emerged as a powerful advancement in multi-step reasoning tasks, offering enhanced transparency and logical consistency through explicit chains of thought (CoT). However, these models introduce novel safety and reliability risks, such as CoT-hijacking and prompt-induced inefficiencies, which are not fully captured by existing evaluation methods. To address this gap, we propose Rt-LRM, a unified benchmark designed to assess the trustworthiness of LRMs. Rt-LRM evaluates three core dimensions: truthfulness, safety and efficiency. Beyond metric-based evaluation, we further introduce the training paradigm as a key analytical perspective to investigate the systematic impact of different training strategies on model trustworthiness. We achieve this by designing a curated suite of 30 reasoning tasks from an observational standpoint. We conduct extensive experiments on 26 models and identify several valuable insights into the trustworthiness of LRMs. For example, LRMs generally face trustworthiness challenges and tend to be more fragile than Large Language Models (LLMs) when encountering reasoning-induced risks. These findings uncover previously underexplored vulnerabilities and highlight the need for more targeted evaluations. In addition, we release a scalable toolbox for standardized trustworthiness research to support future advancements in this important field.

---

Record id: `doi:10.18653/v1/2026.acl-long.1034`
