# reasoning boundary

<!-- auto:begin -->

The set of problems a model can solve given unlimited attempts, as distinct from what it solves on the first — the archive's two sources use it to ask whether RLVR adds capability or only sharpens sampling. They measure it with pass@k at large k and reach opposite verdicts, and the disagreement is entirely about the metric. Under plain pass@k the base model overtakes its RLVR-trained counterpart as k grows, which supports the boundary narrowing. Under CoT-Pass@K, which requires the reasoning to be correct and not only the answer, the RLVR model leads at every k up to 1024 — because base models produce wrong chains that coincidentally reach right answers, most visibly on short-answer mathematics. The boundary is therefore only as well defined as the correctness criterion used to draw it.

- **Kind**: concept
- **Also called**: capability boundary, coverage, reasoning capability boundary
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 7

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](advantage-estimation.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [backtracking](backtracking.md), [Bamboogle](../datasets/bamboogle.md), [benchmark contamination](benchmark-contamination.md), [Brumo](../datasets/brumo.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAPO-Qwen-32B](../models/dapo-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [entropy collapse](entropy-collapse.md), [expected calibration error](expected-calibration-error.md), [exploration](exploration.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [HotpotQA](../datasets/hotpotqa.md), [HumanEval+](../datasets/humaneval.md), [judge reliability](judge-reliability.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3-8B](../models/llama-3-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [Minerva](../datasets/minerva.md), [monitorability](monitorability.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [pass@k](../methods/pass-k.md), [policy entropy](policy-entropy.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [process evaluation](../methods/process-evaluation.md), [prompt difficulty](prompt-difficulty.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B](../models/qwen3-8b.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [randomized control](randomized-control.md), [reasoning distillation](../methods/reasoning-distillation.md), [REINFORCE](../methods/reinforce.md), [reward sparsity](reward-sparsity.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [Search-R1](../methods/search-r1.md), [self-correction](self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training dynamics](training-dynamics.md), [trajectory diversity](trajectory-diversity.md), [TriviaQA](../datasets/triviaqa.md), [verification](verification.md)

## What we have settled

- **Established** — RLVR narrows the set of semantically distinct solution paths a model will produce while widening the set of errors it can recover from; the two effects are separable, both real, and a single pass@k number cannot show either.
  - Measuring a model's preference between two specific verifier-equivalent continuations at a shared branch point, RLVR-trained policies show lower branch entropy than distilled counterparts on 95.5-100% of sampled branches across four model families, and the collapse is significantly stronger in the semantic contrast than in the syntactic one — so the pruning is of inferences, not of phrasing. The same work shows the compensating gain: backtracking probability at dead ends rises from 0.0068 to 0.1537 and from 0.0647 to 0.1687 on two maze models, and recovery from an injected distractor improves by 4.18 to 29.09 points on mathematics. Masking illegal continuations makes the trade explicit — with invalid options removed the flatter distilled policy outperforms the RL one by about 60 percent. This reconciles the archive's standing disagreement rather than picking a side: under plain pass@k the base model overtakes at large k because valid-but-different paths were pruned, while under CoT-Pass@K the RLVR model leads at every k because invalid paths were pruned harder.
- **Established** — Final-answer accuracy is an asymmetric diagnostic: its collapse is evidence of damage, but its preservation is evidence of nothing about the reasoning underneath.
  - Across eleven KV cache compressors the accuracy ranking correlates with the chain-validity ranking at Spearman -0.95 on AIME26: the best compressed method retains 74% of accuracy while 65.5% of its correct answers rest on invalid chains, against 4.3% uncompressed, and answer-first rationalization rises from 58% to 94% of failure cases. A quantization control that evicts no tokens stays near baseline on every metric, so the gap tracks losing access to the trace rather than reducing memory. The same asymmetry appears where accuracy is the training signal rather than the evaluation: writing RLVR objectives as moments of the failure-probability distribution shows two policies can share a mean while distributing success differently across problems, and a miscalibrated critic turns a symmetric binary reward into advantages 2.63 times larger for failures than successes without any of it being visible in accuracy.

## Appears in

- [Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning](../../archive/papers/2026/arxiv-2608-02149/summary.md) — Treats a policy's per-problem failure probability as a random variable over the problem distribution and shows that REINFORCE, pass@K training and MaxRL each optimize a single moment of it, then proposes minimizing the first T moments jointly — which is exactly minimizing the expected truncated number of rollouts needed to reach a first success.
- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) — Replaces PPO's scalar mean-squared-error critic head with a categorical predictor over a discretized value support trained by cross-entropy against Gaussian-smoothed targets, decodes it back to a scalar for an unchanged GAE update, and shows the resulting critic is better calibrated and produces near-symmetric advantages where the MSE critic penalizes failures two-to-three times harder than it rewards successes.
- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics](../../archive/papers/2026/arxiv-2608-03291/summary.md) — Tags every sentence of a reasoning trace by its function and studies the sequence rather than the content, finding that failing SAT traces collapse into repetitive verification and commit early, that failing UNSAT traces run the wrong procedure entirely, and that a prompt naming the missing procedure recovers 84.6% of them.
- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.
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
