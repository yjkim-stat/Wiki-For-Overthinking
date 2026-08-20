<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs

- **Authors**: Hongli Shen, Shaopeng Fu, Qinbo Zhang, Jian Li, Di Wang
- **Venue**: cs.LG
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09542>
- **PDF**: <https://arxiv.org/pdf/2608.09542v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## In one line

Builds safety-alignment training data by first having an agent jailbreak a strong teacher and only then asking that teacher to explain why the successful attack worked, so the student is supervised on the mechanism of the attack rather than on the refusal.

## Problem

Safety alignment for reasoning models supervises either direct refusals or short safety rationales, both keyed to observable prompt patterns. A model trained that way learns which inputs look dangerous rather than what makes them dangerous, so it transfers poorly to unseen jailbreak syntax and over-refuses benign inputs, and the reasoning-trace variants pay a utility tax as well.

## Contributions

- A two-phase pipeline where safety training data is derived only from prompts that actually breached the teacher, so the analysis being distilled is an account of a real failure rather than of a hypothetical one.
- A three-part cognitive scaffold (unmask intent, analyse bypass, derive defence) whose components are ablated individually and shown to be complementary: each removal costs roughly 24-27 ASR points.
- A controlled seed ablation isolating the value of adversarial difficulty in the seed prompts at about 14.2 ASR points with everything else fixed.
- A teacher ablation showing self-distillation recovers almost none of the gain, contradicting a prior published claim.
- An independent second-judge audit of 400 responses reporting 90.25 percent agreement and a 41.94 percent false-negative rate in the unsafe class.

## Method

Two adversarial phases. In synthesis, an autonomous attacker starts from a harmful seed query and alternates two actions -- rewrite the prompt using a strategy from a toolbox, or submit it to the target -- while a scorer returns a 1-10 attack score and textual feedback that the attacker conditions on. The search runs up to K=20 iterations, or persistently retries, until the score exceeds a threshold tau=8.5. In extraction, the breached teacher analyses the prompt that beat it under a fixed three-part scaffold: unmask the core harmful intent, explain how the prompt's syntax concealed that intent, and derive the logical rationale for refusing. The teacher then writes the safe response. The student is fine-tuned by LoRA (r=16, alpha=32, 5 epochs) on the resulting triples of jailbreak prompt, reasoning trace and safe response. Attacker, target and scorer are all DeepSeek-V3.2; the default teacher is DeepSeek-V3.2 in thinking mode; seeds are 1K harmful queries from STAR-1.

## Results

On DeepSeek-R1-Distill-Qwen-7B with a 1K budget matched across baselines, average attack success rate falls from 66.70 for the base model to 6.66, against 27.41 for DirectRefusal and 31.33 for ThinkSafe; average utility rises 0.44 points where DirectRefusal loses 4.87 and STAR-1 loses 7.33. Two of the reasoning-trace baselines are worse than doing nothing on safety: SafeChain averages 70.52 ASR against the base model's 66.70, and SafePath 65.35. Across eight models in three families, HarmBench ASR reductions run 34.75 to 65.50 points, but utility splits by family: DeepSeek-R1-Distill students gain (including +20.00 AIME on the 14B), while Qwen3-0.6B loses 10.46 GSM8K, 6.51 MMLU-Pro and 8.80 MATH-500 and Qwen3-1.7B loses on every utility benchmark. The authors attribute this to a reasoning-style mismatch with the DeepSeek-family teacher. Against attacks not used in synthesis: HumanJailbreak 39.88 to 0.40, PAIR 38.75 to 1.25, TAP 42.50 to 1.25, GCG 29.75 to 1.25; against the paper's own agentic attack, 72.75 to 18.00 with mean turns to breach rising from 4.86 to 9.08. On GCG specifically, SafePath's 29.50 is indistinguishable from the base model's 29.75 while DirectRefusal reaches 3.75 -- so the OOD-syntax test separates the baselines sharply. The two ablations that carry the argument: replacing agentic jailbreak seeds with raw STAR-1 prompts, everything else held fixed, costs about 14.2 ASR points on average, so the difficulty of the seed is doing real work; and pairing the same successful jailbreaks with the teacher's refusal alone rather than its analysis gives 62.64 average ASR against the base model's 66.70, that is almost nothing, while removing any single one of the three scaffold components leaves ASR at 30.11-33.77 against the full method's 6.66. Data scaling is weak: 250 samples already gives most of the reduction. Threshold sensitivity: 998/1000 seeds clear tau=8.5 on the first pass against 978 at 9.5. Teacher choice matters more than any other factor -- Qwen3-235B-A22B-Thinking as teacher yields 51.25 HarmBench ASR against DeepSeek-V3.2's 14.25, and self-distillation from the 7B student itself yields 76.75, barely below the 79.75 base, contradicting ThinkSafe's claim that self-distillation suffices. An independent audit re-judges 400 HarmBench responses with a DeepSeek judge against the Llama Guard labels: 90.25 percent agreement overall, but a 41.94 percent false-negative rate on the small subset Llama Guard calls unsafe.

## Limitations

The paper has no limitations section. Reader-visible limits: the entire evaluation is judge-mediated, and the authors' own audit shows the two judges disagree on 42 percent of the responses in the unsafe class -- exactly the class that determines ASR -- so the absolute numbers are only as sharp as Llama Guard. The attacker, target and scorer are the same model as the teacher, so the attacks the student learns to see, the judgement that they succeeded, and the analysis of why are all one model's view; the one cross-teacher check (Qwen3-235B) is more than three times worse on HarmBench, which suggests the result is substantially a property of DeepSeek-V3.2's analyses rather than of the framework. The utility preservation claim does not hold for the Qwen3 family at small scale. The three scaffold components are ablated only by removal, never permuted or replaced by a same-length irrelevant analysis, so the evidence that the content rather than the length or structure of the trace matters is indirect. Robustness is tested against the base model's attack budget; the agentic attack still reaches 18.00 percent given more turns, so the claim is that the target got harder, not that it is closed.

## Why it matters here

- **reasoning-training**: A training-signal paper wearing safety clothing, and its ablations are what make it worth the archive's attention. Holding the prompts, budget, student and optimiser fixed and varying only the supervision target, teacher refusals alone move average ASR by 4 points while the teacher's three-part analysis moves it by 60 -- the sharpest measurement here that what a distilled trace contains, not merely that a trace exists, is where the effect lives. The teacher ablation is equally direct: self-distillation from the 7B student recovers almost none of the gain, which contradicts a published claim and says the trace must come from a model that can actually perform the analysis. And the difficulty of the input is itself a training-signal decision -- seeds that had to defeat the teacher are worth 14 ASR points over seeds that did not. Against that, the utility cost is family-dependent in a way the paper attributes to reasoning-style mismatch with the teacher, which is the same conditioning-on-the-teacher's-idiom effect the archive's distillation entries keep recording.

## Entities

- **Concepts**: [safety alignment](../../../../wiki/concepts/safety-alignment.md), [jailbreak](../../../../wiki/concepts/jailbreak.md), reasoning trace distillation, safety tax, [out-of-distribution generalization](../../../../wiki/concepts/out-of-distribution-generalization.md), LLM-as-a-judge, self-distillation, reasoning style mismatch
- **Methods**: ADVSAFE, [LoRA](../../../../wiki/methods/lora.md), DirectRefusal, SafePath, SafeChain, STAR-1, ThinkSafe, PAIR, TAP, GCG, [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [knowledge distillation](../../../../wiki/methods/knowledge-distillation.md)
- **Datasets**: [HarmBench](../../../../wiki/datasets/harmbench.md), StrongREJECT, WildJailbreak, AdvBench, [GSM8K](../../../../wiki/datasets/gsm8k.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), [MATH-500](../../../../wiki/datasets/math500.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), STAR-1

Tags: `safety-alignment`, `jailbreak`, `reasoning-traces`, `distillation`, `judge-agreement`

## Abstract

Large reasoning models (LRMs) achieve remarkable success on complex tasks but remain vulnerable to harmful prompts that induce unsafe outputs. Recent methods align LRMs using direct refusals or safety rationales, yet often focus on prompt patterns rather than intrinsic attack mechanisms. As a result, these pattern-centric alignments struggle to generalize across diverse jailbreaks, compromising adversarial robustness and reasoning utility. We propose AdvSafe, a dual-adversarial framework that enables LRMs to internalize unsafety knowledge by explicitly deconstructing adversarial mechanisms. This moves beyond pattern-dependent traces, fostering robust cognitive defense without compromising reasoning utility. Our pipeline operates via a two-phase adversarial game. First, in adversarial synthesis, an autonomous agent dynamically crafts deceptive jailbreak prompts, adapting its strategies to breach a strong teacher model. Second, in adversarial extraction, the breached teacher executes a cognitive counter-attack. For every successful jailbreak, the teacher unmasks the camouflage, explaining why the attack succeeds and how such prompts can be identified and mitigated. This dual-adversarial process yields a compact reasoning dataset capturing rich, generalizable unsafety knowledge. Student models trained on this dataset implicitly acquire safety alignment through intrinsic threat comprehension. Experiments show that with only 1K synthesized samples, AdvSafe-aligned LRMs achieve significantly stronger jailbreak robustness than existing baselines, with almost no utility degradation. Furthermore, AdvSafe improves robustness against out-of-distribution prompts, demonstrating that learning unsafety knowledge enables a superior robustness-utility trade-off and generalizes beyond seen attack patterns.

---

Record id: `arxiv:2608.09542`
