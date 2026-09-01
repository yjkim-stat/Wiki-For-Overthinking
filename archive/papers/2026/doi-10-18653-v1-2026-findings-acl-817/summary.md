<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Earlier, Not Longer: Prompt Optimization via Reducing Unhealthy Exploration

- **Authors**: Ling-I Wu, Minyu Chen, Jingyang Li, Xi Chang, Guoqiang Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.817/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.817.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.817
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Shows that prompt ambiguity causes 'unhealthy exploration' -- an elevated, delayed early-stage entropy peak in a model's token-level entropy trajectory that inflates token usage without improving accuracy or self-consistency -- and trains a lightweight prompt optimizer via entropy-dynamics-guided multi-turn RL to generate concise clarifications, improving reasoning efficiency up to 52.9% in-domain and 38.5% out-of-domain without sacrificing accuracy.

## Problem

Prior work encourages greater exploration during LLM reasoning (test-time scaling, parallel reasoning) under the implicit assumption that increased exploration is uniformly beneficial, but this overlooks 'unhealthy exploration' -- exploration driven by task underspecification (prompt ambiguity) rather than genuine problem difficulty, which substantially increases token usage without contributing to effective problem-solving.

## Contributions

- controlled prompt-ambiguity experiments isolating unhealthy exploration: masking technical terms while holding the reasoning task fixed shows increased ambiguity elevates and delays the early-stage entropy peak, substantially inflating token usage without improving accuracy or self-consistency
- a three-stage decomposition of token-level entropy trajectories (task-understanding/early, problem-solving/middle, self-criticism/late), with a token-enrichment analysis confirming these stages correspond to distinct, characteristic vocabulary rather than being purely statistical artifacts
- an entropy-dynamics-aware prompt optimization framework, training a lightweight clarification generator via multi-turn RL with a reward based purely on entropy-peak dynamics (no correctness supervision), that reduces unhealthy early-stage exploration while explicitly preserving late-stage (healthy) exploration
- up to 52.9% in-domain and 38.5% out-of-domain reasoning-efficiency gains without sacrificing accuracy, outperforming Early-Stop and EvoPrompt baselines and two outcome-based RL alternatives that were shown not to generalize out-of-domain

## Method

Runs controlled prompt-ambiguity experiments: samples 1,000 MMLU-Pro instances, uses GPT-5 to identify technical terms, and systematically masks a controlled proportion (0/25/50/75/100%) of them with their initialisms (e.g. 'page fault' -> 'PF') to vary ambiguity while keeping the underlying reasoning task unchanged, then evaluates GPT-oss-120B (three reasoning-effort levels) and Qwen3-30B (thinking/instruct variants) across mask ratios. Decomposes each response's token-level entropy trajectory into three stages -- task understanding (early), problem solving (middle), self-criticism (late) -- via a smoothed early-stage peak height/position (h^early, p^early) and a late-stage peak height (h^late), each estimated by averaging over K=16 rollouts. Finds increasing mask ratio consistently elevates and delays the early-stage entropy peak (unhealthy exploration) while leaving the late-stage peak largely convergent, and this ambiguity-induced exploration substantially inflates token usage (Figure 2c) without improving accuracy or self-consistency (Figures 2a-b) -- confirming the early-stage inflation is unproductive rather than reflecting genuinely richer reasoning. Proposes a prompt-optimization framework: a lightweight optimizer P_theta (Qwen3-4B-Instruct) is trained via multi-turn RL to append a concise clarification x' = x (+) P_theta(x) to the original prompt, guided solely by an entropy-peak-based reward with no correctness supervision -- an early-stage peak reward R^early rewards clarifications that both reduce and advance (make earlier) the early-stage peak relative to the unclarified baseline, and a late-stage peak reward R^late (a regularization term, not a primary objective) ensures the late-stage peak height stays closer to the original prompt's than the early-stage reduction does, preserving healthy exploration. The clarification is explicitly restricted to task-formulation clarity and must not reveal solution steps or answers. Multi-turn RL lets the optimizer iteratively refine its clarification within a training episode based on feedback (non-answer-leaking) about which entropy-peak conditions were unmet, up to a maximum number of turns; at inference the optimizer runs single-shot with no added interaction overhead. Trained on MMLU-Pro and SuperGPQA (1,000 samples each), evaluated in-domain (MMLU-Pro, SuperGPQA) and out-of-domain (BBH, MedQA) against Pure (no optimization), Early-Stop (entropy-threshold-based early termination), and EvoPrompt (evolutionary prompt search) baselines, measuring Reasoning Efficiency = Accuracy / Token Usage.

## Results

The proposed method achieves the highest reasoning efficiency across most reasoning-model/effort settings, on both in-domain and out-of-domain benchmarks, without harming (and sometimes slightly improving) accuracy -- e.g. on GPT-oss-120B at medium reasoning effort, the method reaches 17.04 efficiency on MMLU-Pro (vs. Pure's 4.56) while accuracy stays essentially flat (80.60 -> 80.47). In contrast, Early-Stop also improves efficiency but risks accuracy degradation since it directly truncates tokens once entropy drops below a threshold for several consecutive steps, while EvoPrompt primarily improves accuracy but often increases token usage, lowering efficiency for most reasoning models. Out-of-domain evaluation (BBH, MedQA) shows the method's learned clarification strategies remain robust to substantial domain shift, since EvoPrompt is inapplicable there (it requires a development set) and Early-Stop's threshold transfers only approximately. A stage-wise token-usage ablation confirms the mechanism works as intended: the method consistently reduces early-stage token usage across all reasoning models while producing only modest reductions in the middle/late stages, indicating the model converges to a stable task interpretation more efficiently without over-regularizing the core multi-step reasoning phase. A token-enrichment analysis shows early-stage entropy peaks are selectively associated with task-understanding tokens (e.g. 'interpret', 'what does', 'means', 'assume') while late-stage peaks are associated with self-criticism/verification tokens (e.g. 'double-check', 'verify', 'mismatch', 'recompute') -- direct evidence the two entropy-peak stages correspond to genuinely distinct cognitive functions rather than being statistical artifacts. An answer-conditioning control experiment shows that explicitly giving the model the answer causes a sharp drop in early-stage entropy and near-total disappearance of the late-stage peak (a qualitatively different pattern from the learned clarifications, whose entropy trajectory stays close to the original unclarified prompt's), evidence the method is not covertly leaking the answer through its clarifications. Comparisons against two outcome-based alternatives -- a jointly accuracy+length-rewarded prompt optimizer, and direct RLVR applied to the reasoning model itself with a scalarized accuracy/length reward -- both show good in-domain gains but fail to transfer to the out-of-domain benchmark (MedQA), with direct RLVR in particular showing accuracy degrading sharply as the length-reduction weight lambda increases; the entropy-guided method is the only one to preserve both efficiency gains and accuracy in both in-domain and out-of-domain settings.

## Limitations

Experiments are limited to a finite set of model architectures and QA-style benchmarks; generalization to other generation paradigms (interactive dialogue, open-ended creative generation) is untested. Entropy remains an indirect proxy for internal uncertainty and exploration, and the paper suggests future work could incorporate complementary signals (semantic entropy, representation-level measures) to better distinguish unhealthy from healthy exploration. The explicit restriction that clarifications stay concise and non-informative about solution steps may limit the optimizer's ability to handle prompts that are deeply underspecified or structurally flawed, where more substantial prompt reformulation (beyond the current framework's scope) may be required.

## Why it matters here

- **overthinking**: Core paper for this topic: it identifies a distinct source of reasoning-trace waste -- unhealthy exploration driven by task underspecification rather than genuine problem difficulty -- complementary to the archive's more common focus on post-answer redundant verification. Its methodological framing (entropy trajectory decomposed into task-understanding, problem-solving, and self-criticism stages, each with characteristic vocabulary) offers a mechanistic account of *where in the reasoning process* overthinking originates, and its finding that outcome-based (accuracy+length) reward optimization fails to generalize out-of-domain while entropy-dynamics-guided optimization does is a methodologically important result for any overthinking-mitigation approach relying on RL against a length-based reward.

## Entities

- **Concepts**: unhealthy exploration (ambiguity-induced), early-stage / late-stage entropy peak, entropy-dynamics-guided prompt optimization, task-understanding vs. self-criticism token enrichment
- **Methods**: entropy-dynamics-aware prompt optimization (multi-turn RL clarification generator), Early-Stop (entropy-threshold baseline), EvoPrompt (evolutionary prompt-search baseline), outcome-based Acc+Len prompt optimizer (comparison), direct RLVR (comparison)
- **Datasets**: [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), [SuperGPQA](../../../../wiki/datasets/supergpqa.md), BBH (out-of-domain), MedQA (out-of-domain)

Tags: `overthinking`, `unhealthy-exploration`, `prompt-optimization`, `entropy-dynamics`, `reasoning-efficiency`

## Abstract

While large language models exhibit strong reasoning capabilities, prior work shows that their performance can be further enhanced by encouraging greater exploration. However, existing approaches overlook the presence of unhealthy exploration that increases exploration-related token usage without contributing to effective problem-solving. In this work, we show that prompt ambiguity can artificially prolong early-stage exploration, manifested as an elevated and delayed early-stage entropy peak. Although this uncertainty may be gradually resolved as reasoning progresses, reflected in the eventual convergence of the late-stage entropy peak, it does not meaningfully improve accuracy or self-consistency and instead substantially reduces reasoning efficiency. Motivated by these observations, we propose an entropy-dynamics-aware prompt optimization framework that trains a lightweight optimizer to generate concise clarifications. These clarifications aim to reduce ambiguity-induced early-stage uncertainty while preserving the model’s reasoning capabilities. Extensive experiments across multiple models, reasoning budgets, and benchmarks demonstrate that our approach consistently improves reasoning efficiency by up to 52%, by reducing unhealthy exploration without sacrificing accuracy.

---

Record id: `doi:10.18653/v1/2026.findings-acl.817`
