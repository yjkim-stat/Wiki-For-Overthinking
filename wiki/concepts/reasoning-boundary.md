# reasoning boundary

<!-- auto:begin -->

The set of problems a model can solve given unlimited attempts, as distinct from what it solves on the first — the archive's two sources use it to ask whether RLVR adds capability or only sharpens sampling. They measure it with pass@k at large k and reach opposite verdicts, and the disagreement is entirely about the metric. Under plain pass@k the base model overtakes its RLVR-trained counterpart as k grows, which supports the boundary narrowing. Under CoT-Pass@K, which requires the reasoning to be correct and not only the answer, the RLVR model leads at every k up to 1024 — because base models produce wrong chains that coincidentally reach right answers, most visibly on short-answer mathematics. The boundary is therefore only as well defined as the correctness criterion used to draw it.

- **Kind**: concept
- **Also called**: capability boundary, coverage, reasoning capability boundary
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME24](../datasets/aime24.md), [AMC23](../datasets/amc23.md), [benchmark contamination](benchmark-contamination.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [DAPO](../methods/dapo.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [entropy collapse](entropy-collapse.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [judge reliability](judge-reliability.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [pass-k](../methods/pass-k.md), [PPO](../methods/ppo.md), [process evaluation](../methods/process-evaluation.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reasoning distillation](../methods/reasoning-distillation.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training dynamics](training-dynamics.md), [verification](verification.md)

## Appears in

- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../archive/papers/2025/local-b050d2841cbb4959/summary.md) — Measures RLVR-trained models against their base models with pass@k at large k and finds the base wins, concluding RLVR sharpens sampling toward paths the base already had rather than adding new ones.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) — Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._

### The dispute, and why it was really about the metric

The two sources here are a direct exchange, and reading them as a contradiction
misses what happened.

**Yue et al. (arXiv 2504.13837)** measure pass@k at large k and find base models
overtake their RLVR-trained counterparts — on Omni-MATH-Train, pass@1 rises across
GRPO steps 150/300/450 while coverage at pass@256 falls. Perplexity analysis puts
every RLVR path inside the base model's distribution. Conclusion: RLVR resamples,
it does not extend.

**Wen et al. (arXiv 2506.14245)** reproduce that exact curve, then add the control
it lacked. Base models on short-answer mathematics produce **wrong chains that land
on right answers** — and pass@k counts those as successes, increasingly often as k
grows. Scoring the chain too (CoT-Pass@K) reverses the result: the RLVR model leads
at every k up to 1024, most clearly on AIME 2025, which postdates the base model's
cutoff and so cannot be contaminated.

Yue et al. anticipated this. Their own caveat names guessing as the threat and
mitigates it by **manual inspection of a subset** plus reliance on code tasks. Wen
et al. simply did the measurement at scale. So this is not two camps; it is one
finding and a missing control, supplied.

### What the archive should take from it

- **A pass@k number on short-answer math is not a capability measurement** unless
  the chains were checked. This applies retroactively to every pass@k result here.
- The two agree where guessing is impossible. On code, verified by execution,
  RLVR improves plain pass@k — even starting from a distilled model.
- The dissociation is the same one this archive keeps meeting from other
  directions: CoRE's "superficial execution", the proverb benchmark naming the
  right ending while choosing wrong. Correct answer, wrong reasoning, at a rate
  large enough here to invert a headline result.
- Still unresolved: Yue et al.'s *narrowing* claim. Wen et al. show the boundary
  is wider than pass@k suggests; neither settles whether prolonged RLVR narrows it
  over training, since the CoT-Pass@K comparison is at one checkpoint, not a curve.
