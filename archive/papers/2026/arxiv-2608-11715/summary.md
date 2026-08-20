<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use

- **Authors**: Siddharth Chauhan, Thomas Butler, Abhishek Singhania, Pankaj Porwal, Honey Gupta
- **Venue**: cs.CL
- **Published**: 2026-08-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11715>
- **PDF**: <https://arxiv.org/pdf/2608.11715v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## In one line

Names and measures a multilingual tool-calling failure in which the model picks the right API but writes argument values in the wrong language, then compares supervised fine-tuning against PPO and GRPO under matched budgets and finds that a well-selected supervised checkpoint matches or beats reinforcement learning on the task while costing more elsewhere.

## Problem

Standard function-calling metrics score whether the right tool was invoked with the right arguments, and a semantically correct argument written in the wrong language passes all of them while failing completely in a system that enforces language constraints. This failure -- argument language mismatch -- is invisible to the existing evaluation, so nothing measures how much of it post-training removes or what removing it costs.

## Contributions

- Names and operationalises argument language mismatch -- the correct tool called with semantically correct arguments in the wrong language -- and shows it is invisible to standard function-calling metrics.
- A five-stage hierarchical evaluation, with a continuous per-argument language-consistency score thresholded for reporting and retained continuous inside the reward.
- A dual-protocol comparison showing that best-checkpoint selection reverses the epoch-fixed ordering between supervised fine-tuning and reinforcement learning on end-to-end accuracy.
- A monotone reward-granularity ablation from sparse to hierarchical to argument-factorised under fixed GRPO settings.
- Evidence that the supervised model's task gain is paid for by an 8.6-point English reasoning regression that GRPO does not incur, and that token-level argument weighting helps GRPO while destabilising PPO.

## Method

A multilingual extension of the Berkeley Function Calling benchmark, trained on Spanish and evaluated on Spanish plus three unseen languages, with two splits distinguishing high API overlap (learnability) from low overlap (generalisation). Five hierarchical turn-level metrics run from tool invocation detection through tool selection, argument completion, argument language consistency and end-to-end function-call match, so a regression can be localised to a stage. Argument language consistency is first computed continuously as a mean over required arguments of a per-argument score for correct, partial and mismatched language, then thresholded at 90 percent of the maximum for the binary metric, with the continuous version retained inside the reward to distinguish complete language failure from partial success. Three reward designs of increasing granularity are compared under fixed GRPO settings: sparse response-level outcomes, a hierarchical staged reward following the five metrics, and an argument-factorised reward averaging a per-argument-value score, optionally with extra token-level weight on argument tokens. Two evaluation protocols are reported separately and the distinction carries most of the paper's argument: epoch-fixed, where every method gets the same budget, and validation-selected, where each method's best checkpoint by validation function-call match is used.

## Results

Under the epoch-fixed protocol reinforcement learning looks clearly better: on the learnability split, argument language consistency and end-to-end match go from the base model's 52.3 / 32.3 to SFT's 63.8 / 40.4, GRPO's 74.5 / 51.5 and SFT+GRPO's 75.3 / 54.0, with the generalisation split showing the same ordering at lower absolute values. Under best-checkpoint selection the ordering reverses on end-to-end match: SFT reaches 79.1 / 67.4 against GRPO's 74.0 / 55.3 and SFT+GRPO's 79.3 / 61.3 -- so the supervised baseline gains 27 points of function-call match from checkpoint selection alone while GRPO gains under 4, and most of what the epoch-fixed comparison attributed to reinforcement learning is recovered by model selection. The cost appears elsewhere and is localised rather than diffuse: on out-of-domain multilingual grade-school mathematics, the validation-selected SFT model drops 8.6 points in English (70.8 to 62.2) while Spanish improves and other languages are mixed, so the multilingual average moves only from 67.20 to 64.68; GRPO leaves English essentially intact at 70.4. The reward-granularity ablation is monotone under fixed GRPO settings -- sparse 61.3 / 43.3, hierarchical 72.2 / 51.0, argument-factorised 74.0 / 55.3 -- and the authors state the sparse reward is especially bad under group-based optimisation because many sampled outputs share the same reward. Algorithm comparison under the same reward: GRPO 81.2 / 66.9 against PPO's 72.6 / 58.4, which the authors attribute to batch-level versus group-relative advantage normalisation when only a subset of tokens determines correctness. Token-level upweighting of argument tokens improves consistency under GRPO while preserving end-to-end match, and severely destabilises PPO on both -- so the reward shaping and the optimiser interact rather than compose. Cross-lingual transfer to three unseen languages is near-identical in average for SFT and GRPO (57.88 against 57.72) but distributed differently across the three. Scaling: on the generalisation split, GRPO at 7B (68.10) exceeds SFT at 32B (67.59), and at 14B SFT is ahead of GRPO (74.47 against 71.08), so the ordering is not monotone in size.

## Limitations

The paper states no limitations section. Reader-visible limits: training is on one language and the entire generalisation claim rests on transfer to three related European languages, so nothing is established for scripts or morphologies further from the training language. The headline comparison depends entirely on which protocol is read, and the two disagree in direction; the authors report both and argue for the best-checkpoint reading, but validation selection on function-call match is itself a form of tuning that the epoch-fixed runs do not receive on any other axis. The reasoning-preservation result is a single benchmark with one run per method and language, and the authors themselves describe the non-English movements as likely noisy, which leaves the claim resting on one 8.6-point English drop. The reward ablation varies granularity but not the reward's scale or the number of terms, so denser and better-shaped are not separated. No seeds, no intervals anywhere. The argument-language-consistency metric is thresholded at 90 percent of a three-level per-argument score, so a call with one mismatched argument out of many can still pass.

## Why it matters here

- **reasoning-training**: Two results the archive should keep, and they cut in opposite directions. The first is a control most reinforcement-learning papers do not run: comparing the same methods epoch-fixed and at each one's best validation checkpoint reverses the conclusion, because the supervised baseline gains 27 points of end-to-end accuracy from checkpoint selection and GRPO gains under 4. That is the strongest instance in the archive of a baseline being beaten by insufficient tuning rather than by the method, and it belongs next to the archive's existing finding that an inherited baseline is an experimental variable. The authors state the consequence plainly -- structured rewards improve learning within RL but do not change the ceiling supervised training establishes. The second result is what reinforcement learning does buy here, which is not accuracy: the well-selected supervised model loses 8.6 points of English mathematics while GRPO loses none, so the difference is in what the training does not damage. That reframes the comparison as an alignment-across-objectives question rather than a task-accuracy one. Three smaller observations transfer: reward granularity improves monotonically and the authors identify sparse rewards as specifically bad under group normalisation because sampled outputs collide at the same value, which is the zero-advantage problem the archive has been collecting; GRPO beats PPO under identical rewards where correctness is localised to a few tokens; and token-level upweighting helps GRPO while destabilising PPO, so a shaping choice cannot be evaluated apart from the optimiser it is fed to.

## Entities

- **Concepts**: [tool learning](../../../../wiki/concepts/tool-learning.md), [credit assignment](../../../../wiki/concepts/credit-assignment.md), reward granularity, [process reward](../../../../wiki/concepts/process-reward.md), [cross-lingual transfer](../../../../wiki/concepts/cross-lingual-transfer.md), [catastrophic forgetting](../../../../wiki/concepts/catastrophic-forgetting.md), model selection, [advantage estimation](../../../../wiki/concepts/advantage-estimation.md)
- **Methods**: [GRPO](../../../../wiki/methods/grpo.md), [PPO](../../../../wiki/methods/ppo.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), argument-factorized reward, hierarchical step reward, token-level reward weighting
- **Datasets**: Berkeley Function Calling Leaderboard (multilingual extension), MGSM

Tags: `tool-use`, `multilingual`, `reward-granularity`, `grpo-vs-ppo`, `model-selection`

## Abstract

The reliability of Large Language Models (LLMs) for API calling degrades in multilingual settings. A common failure occurs when a model selects the correct tool but generates argument values in an inconsistent language, which we term Argument Language Mismatch (ALM). Although semantically correct, such outputs are operationally invalid and not captured by standard API-calling metrics. We revisit post-training strategies for mitigating ALM and find that, in our benchmark, supervised fine-tuning (SFT) provides a strong baseline, substantially improving argument language consistency and end-to-end function call accuracy. Under consistent model selection, SFT achieves performance comparable to, and sometimes exceeding more complex reinforcement learning (RL) approaches. We further examine whether RL with structured, argument-aware rewards offers additional benefits. While methods such as Group Relative Policy Optimization (GRPO) can improve language consistency and better preserve general reasoning ability, these gains are incremental and most pronounced in generalization and multi-objective trade-offs. Overall, our results suggest that much of the performance in multilingual API grounding can be achieved through careful supervised training, with RL providing targeted rather than fundamental improvements.

---

Record id: `arxiv:2608.11715`
