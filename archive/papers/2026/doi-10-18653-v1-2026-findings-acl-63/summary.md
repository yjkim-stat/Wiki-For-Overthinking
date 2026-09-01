<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Slower Isn’t Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning

- **Authors**: Sitong Fang, Wenjing Cao, Jiahao Li, Xuyao Wang, Chi-Min Chan, Sirui Han, Juntao Dai, Yike Guo, Yaodong Yang, Jiaming Ji
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.63/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.63.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.63
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

TRUTHFULVQA, a 5,000-image hierarchical human-annotated benchmark testing multimodal LLM truthfulness under progressively misleading visual-linguistic prompts, uncovers an inverse scaling law of truthfulness: slow-thinking (reasoning) MLLMs are consistently less truthful than their fast-thinking chat counterparts of the same family, and larger reasoning models show worse calibration despite generating more reasoning tokens.

## Problem

Whether slower, more deliberate 'System II'-style reasoning in multimodal LLMs actually produces more truthful answers is untested; existing benchmarks measure hallucination (fabrication on benign inputs) but not truthfulness (robustness to adversarially misleading or deceptive prompts), and it is unclear whether reasoning models' longer deliberation chains help or hurt when visual inputs are incomplete or misleading.

## Contributions

- TRUTHFULVQA, the first large-scale, human-in-the-loop-verified multimodal truthfulness benchmark with a three-tier hierarchical adversarial prompt design spanning eight deception categories
- an inverse scaling law of truthfulness: reasoning-augmented MLLMs are consistently less truthful than same-family chat models despite longer deliberation, and this gap does not close (and worsens in confidence-margin terms) with larger reasoning models
- a causal decomposition isolating the mechanism to reasoning *topology* rather than reasoning training: forcing chat models into serialized step-by-step CoT reproduces the same truthfulness degradation and DFS-style single-path commitment pattern seen in dedicated reasoning models
- TruthfulJudge, a fine-tuned specialized truthfulness evaluator (88.4% accuracy, kappa=0.79, ECE=0.11) substantially outperforming general-purpose MLLM-as-judge baselines, which erroneously accept ~1/3 of hallucinated responses

## Method

Constructs TRUTHFULVQA: 5,000 images (4,500 manually curated to be misleading/factually incorrect, 500 diffusion-generated), each independently verified by 5+ of 50 professional annotators, paired with a three-tier hierarchical human-written prompt set spanning eight categories/21 subcategories of visual deception (grounded in Whaley's taxonomy of deception) -- Level 1 (basic perception), Level 2 (inductive misleading, deceptive contextual framing), Level 3 (reasoning with false premises, requiring the model to resist an invalid narrative built into the prompt). Evaluates 50+ chat and reasoning MLLMs (Qwen2.5-VL/Qwen2-VL, InternVL, Gemma-3, Llama-4 families for chat; QVQ, Kimi-VL-A3B-Thinking, Skywork-R1V, Mulberry, and others for reasoning), reporting accuracy/variance across levels and Logit Advantage Loss (LAL) -- a logit-based metric decomposing misleading-induced degradation of the correct answer's confidence versus amplification of an incorrect distractor's confidence, invariant to per-model affine logit scaling. Also fine-tunes TruthfulJudge (Qwen2.5-VL-7B-Instruct fine-tuned on 7.1K human-annotated critique+preference pairs via a Critique-Label paradigm) as a specialized truthfulness evaluator, benchmarked against GPT-4o, Gemini-1.5-Pro, Claude-3.5-Sonnet and Qwen2.5-VL-72B as MLLM judges.

## Results

Mean accuracy across 50+ models drops sharply across levels: 81.85% (Level-1) -> 55.37% (Level-2) -> 44.96% (Level-3), confirming misleading prompts induce large truthfulness failures even on originally-simple perceptual tasks. The central finding (the inverse scaling law): reasoning-augmented MLLMs consistently underperform their same-family chat counterparts on truthfulness despite generating more inference-time reasoning tokens, and the loss in confidence-margin (LAL) is systematically larger for reasoning variants than chat variants across matched pairs (e.g. 0.89 for QVQ-72B, 0.71 for Mulberry-Qwen2-VL-7B, 0.53 for Kimi-VL-A3B-Thinking, all higher than their respective chat-model counterparts). Scaling parameter count does not fix this: larger reasoning models (QVQ-72B, Skywork-38B) achieve only modest truthfulness, and as activated parameters decrease across three reasoning-model sizes, logit advantage loss decreases correspondingly -- larger representational capacity appears to amplify bias/inflated confidence rather than improve accuracy. Reasoning models are found to follow depth-first search (DFS)-style reasoning -- committing early to an initial interpretation and elaborating on it without revisiting alternatives -- while chat models exhibit more breadth-first (BFS)-style, iterative-revision behavior, correlating with better truthfulness robustness. Calibration analysis (Expected Calibration Error) confirms this structurally rather than as an artifact of training data or model capacity: reasoning models have consistently higher (worse) ECE (e.g. QVQ-72B 0.325 vs. its chat counterpart Qwen2.5-VL-72B's 0.188), and forcing chat models into serialized step-by-step Chain-of-Thought prompting (holding model parameters fixed) degrades their accuracy by 2.8-8.3 percentage points and reproduces reasoning-model-like failure modes -- demonstrating the vulnerability is a structural risk of serialized (DFS-style) reasoning topology itself, not an inherent deficiency specific to reasoning-trained models. TruthfulJudge reaches 88.4% judge accuracy (vs. 52.2-63.8% for general-purpose MLLM judges), Cohen's kappa 0.79 (near-perfect agreement), a 77%-relative-lower false-positive rate than GPT-4o, and the best calibration (ECE=0.11) among compared judges -- while general-purpose judges erroneously accept nearly one-third of hallucinated responses as correct.

## Limitations

The annotation team, though large (50 professionals), lacks cultural diversity, which the authors flag as a potential bias source they plan to address via more diverse annotator platforms in future work. The dataset (5,000 examples) is described by the authors as modest in scale relative to commercial benchmarks, with future work aiming for tens of thousands of examples. The eight-category untruthful taxonomy may not fully capture the spectrum of visual-semantic deception and has category overlap the authors flag for future refinement.

## Why it matters here

- **overthinking**: Directly relevant and a strong complication of the 'more test-time reasoning = better' assumption: this paper's central inverse-scaling finding is that slow, extended multimodal reasoning is not merely inefficient but actively *less truthful* than fast chat-style responses under adversarial/misleading conditions, and it locates the cause in a specific reasoning-process pathology (DFS-style single-path commitment without revisiting alternatives) that is reproducible in chat models simply by forcing serialized step-by-step CoT. This gives the archive a concrete mechanistic account -- reasoning topology, not reasoning training -- for why more deliberation can make a model confidently wrong rather than more careful, directly relevant to any overthinking-mitigation approach that assumes longer or more structured reasoning is at worst neutral for correctness.

## Entities

- **Concepts**: inverse scaling law of truthfulness, depth-first search (DFS) vs. breadth-first search (BFS) reasoning topology, Logit Advantage Loss (LAL), Critique-Label judge paradigm
- **Methods**: Logit Advantage Loss (LAL), Expected Calibration Error (ECE), TruthfulJudge (Critique-Label fine-tuned judge), Bradley-Terry / Critique-Score / Pure-Label judge paradigms (ablation baselines)
- **Datasets**: TRUTHFULVQA (new, 5,000 images / hierarchical 3-level prompts)

Tags: `multimodal`, `truthfulness`, `hallucination`, `inverse-scaling`, `reasoning-topology`, `calibration`

## Abstract

Reasoning models have attracted increasing attention for their ability to tackle complex tasks, embodying the System II (slow thinking) paradigm in contrast to System I (fast, intuitive responses). Yet a key question remains: Does slower reasoning necessarily lead to more truthful answers? Our findings suggest otherwise. We conduct the first systematic study of the inverse scaling law in slow-thinking paradigms for multimodal reasoning. We find that when confronted with incomplete or misleading visual inputs, slow-thinking models are more prone to fabricating plausible yet false details to justify untruthful reasoning. To analyze this behavior, we construct a 5,000-sample hierarchical prompt dataset annotated by 50 human participants. The prompts progressively increase in complexity, revealing a consistent pattern: slower reasoning models tend to follow depth-first search (DFS) thinking, persistently exploring flawed premises, while faster chat models favor breadth-first search (BFS) inference, showing greater caution under uncertainty. These findings reveal a critical vulnerability of reasoning models: while effective in structured domains such as math, their DFS-style reasoning becomes fragile when confronted with ambiguous, multimodal inputs.

---

Record id: `doi:10.18653/v1/2026.findings-acl.63`
