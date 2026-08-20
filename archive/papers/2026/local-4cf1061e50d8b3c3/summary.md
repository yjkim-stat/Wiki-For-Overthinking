<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# On The Fragility of Benchmark Contamination Detection in Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: reasoning-evaluation, reasoning-training
- **Relevance score**: reasoning-evaluation 0.50, reasoning-training 0.50

## In one line

Shows that benchmark contamination in reasoning models is alarmingly easy to hide: a brief round of GRPO erases the signals contamination detectors rely on, and PPO-style importance sampling and clipping are identified as the cause — implying a broad class of RL methods conceals contamination inherently.

## Problem

Leaderboards have turned evaluation into a competition, and the shortcut to a higher ranking is to train on the benchmark. Many contamination detection methods exist, but they were designed for ordinary language models. Reasoning models are produced by a pipeline — base model, supervised fine-tuning, then reinforcement learning — and nobody had asked what that pipeline does to contamination signals.

## Contributions

- A study of the two practically relevant contamination scenarios: contamination introduced during SFT before RL, and CoT-based SFT contamination applied to an already-advanced reasoning model as the final stage.
- The finding that SFT-stage contamination is initially detectable, but that even brief GRPO training markedly conceals the signals most detection methods depend on.
- Empirical and theoretical identification of the root cause as PPO-style importance sampling and clipping objectives, which implies a broad class of RL methods shares this concealing effect rather than it being a GRPO quirk.
- The finding that in the second scenario most detection methods perform near random guessing.
- An explanation of why memorization-based detection fails: a contaminated model is also more confident on unseen samples drawn from a distribution similar to its training set, so member-versus-non-member confidence gaps close.
- A public arena of detection methods for reasoning models.

## Method

Contamination is injected deliberately under controlled conditions so that ground truth membership is known, then a battery of published contamination detection methods is run against the resulting models. Scenario I follows the standard reasoning-model pipeline: benchmark data is mixed into the SFT stage of a base model, detection is run, and then GRPO training is applied for a short period and detection is run again, isolating the effect of the RL stage. Scenario II applies CoT-format SFT contamination to an already-trained reasoning model as a final step. Detection performance is measured as the ability to separate members from non-members. The concealment mechanism is investigated by analysing how importance sampling ratios and clipping in PPO-style objectives affect the likelihood signals that detectors read, supported by theoretical analysis.

## Results

In Scenario I, contamination introduced at the SFT stage is originally identifiable by existing detection methods — but a brief GRPO run markedly suppresses the signals those methods rely on, so a pipeline that ends in RL launders the contamination introduced before it. The analysis attributes this to PPO-style importance sampling and clipping rather than to anything specific to GRPO, so the concealment should be expected from a broad class of RL post-training methods. In Scenario II, most detection methods perform near random guessing on reasoning models contaminated by CoT-format SFT as a final stage. The stated reason is that detection relies on a confidence gap between seen and unseen samples, and a contaminated reasoning model is also more confident on unseen samples that share the training distribution, closing the gap. The authors' conclusion is that model developers could inflate leaderboard performance while leaving minimal traces, undermining the fairness of public leaderboards for reasoning models specifically.

## Limitations

No standalone limitations section is present in the material read. What a reader should weigh: contamination is injected by the authors under controlled conditions, so the study establishes that detectors fail against these injection procedures rather than that any particular published model is contaminated; the concealment result is demonstrated for a brief GRPO run, and how the effect scales with longer RL or different hyperparameters is not characterized in the material read; and the claim that the effect generalizes across a broad class of RL methods rests on the shared importance-sampling-and-clipping structure, which is an argument by mechanism rather than a sweep over algorithms.

## Why it matters here

- **reasoning-evaluation**: The most damaging result this topic holds, because it removes a defence the archive was implicitly relying on. VAR-MATH establishes that RL-trained models are fragile to symbolic variation and reads that as evidence of superficial heuristics; the natural counter-argument is that contamination would have been caught by detection methods. This paper closes that route: SFT contamination is detectable until an RL stage is applied, after which it is not, and the mechanism is the importance sampling and clipping shared by essentially every RLVR method in this archive. So for exactly the class of models this archive studies, contamination is both plausible and undetectable. Combined with the topic's other two findings — a 1.1-4.6 point sampling noise floor and a 9.15 point hardware-precision standard deviation on the same model and benchmark — the picture is that AIME-based claims about RL-trained reasoning models rest on a measurement that is noisy, baseline-unstable, construct-fragile and now also contamination-opaque. None of this makes any individual paper wrong; together it means the field lacks the instrumentation to adjudicate its own disputes at the 2-5 point scale where most of them live.
- **reasoning-training**: An unintended property of the RLVR recipe this topic is built around. Every archived training paper uses GRPO or a PPO-style variant, and this shows that the importance sampling and clipping in those objectives suppress the likelihood signatures that memorization leaves behind. That is a statement about what RL does to a model's distribution, not only about evaluation hygiene: RL post-training moves the model away from the sharp likelihood peaks that SFT on specific examples creates, which is the same smoothing that makes contamination invisible. It is worth holding alongside the archive's finding that RLVR preserves over 86% of the base model's high-entropy token positions — RL apparently reshapes the likelihood surface enough to hide memorization while leaving the entropy structure largely intact, and reconciling those two observations is an open question this archive can pose precisely.

## Entities

- **Concepts**: [benchmark contamination](../../../../wiki/concepts/benchmark-contamination.md), contamination detection, [memorization](../../../../wiki/concepts/memorization.md), importance sampling, clipping, [membership inference](../../../../wiki/concepts/membership-inference.md), leaderboard integrity, [construct validity](../../../../wiki/concepts/construct-validity.md), RLVR
- **Methods**: [GRPO](../../../../wiki/methods/grpo.md), [PPO](../../../../wiki/methods/ppo.md), [supervised finetuning](../../../../wiki/methods/supervised-fine-tuning.md), contamination detection, membership inference attack
- **Datasets**: [AIME24](../../../../wiki/datasets/aime-2024.md), [MATH500](../../../../wiki/datasets/math500.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `contamination`, `evaluation`, `leaderboard`, `grpo`, `detection`, `memorization`

## Abstract

Leaderboards for large reasoning models (LRMs) have turned evaluation into a competition, incentivizing developers to optimize directly on benchmark suites. A shortcut to achieving higher rankings is to incorporate evaluation benchmarks into the training data, thereby yielding inflated performance, known as benchmark contamination. Despite that numerous contamination detection approaches have been proposed, surprisingly, our studies find that evading contamination detections for LRMs is alarmingly easy. We focus on the two scenarios where contamination may occur in practice: (I) when the base model evolves into LRM via supervised fine-tuning (SFT) and reinforcement learning (RL), we find that contamination during SFT can be originally identified by contamination detection methods. Yet, even a brief Group Relative Policy Optimization (GRPO) training can markedly conceal contamination signals that most detection methods rely on. Further empirical experiments and theoretical analysis indicate that Proximal Policy Optimization (PPO) style importance sampling and clipping objectives are the root cause of this detection concealment, indicating that a broad class of RL methods may inherently exhibit similar concealment capability; (II) when SFT contamination with CoT is applied to advanced LRMs as the final stage, most contamination detection methods perform near random guesses. Without exposure to non-members, contaminated LRMs would still have more confidence when responding to those unseen samples that share similar distributions to the training set, and thus, evade existing memorization-based detection methods. Together, our findings reveal the unique vulnerability of LRMs evaluations: Model developers could easily contaminate LRMs to achieve inflated leaderboards performance while leaving minimal traces of contamination, thereby strongly undermining the fairness of evaluation and threatening the integrity of public leaderboards.

---

Record id: `local:4cf1061e50d8b3c3`
