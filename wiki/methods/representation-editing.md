# representation editing

<!-- auto:begin -->

Modifying a model's internal representations to change behaviour, as distinct from steering with a fixed direction or retraining. Across 3 sources the archive's material is a positive result, a negative one and a diagnostic. The positive: a closed-form linear operator estimated from second-order statistics on a modest paired calibration set, folded into existing feed-forward projections so inference cost and architecture are unchanged -- with an ablation showing a first-order mean correction insufficient, so the covariance structure is doing the work. The negative: a published method resting on a decodable logic direction is matched exactly under steering by a same-norm random direction, so the reported effect is magnitude rather than content. The diagnostic: editing the internal representation of a written scratchpad while holding the printed text fixed, which turns 'does the model use its scratchpad' into a causal test with a single correct answer and a move-specific selectivity control.

- **Kind**: method
- **Also called**: activation editing, representation surgery
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [bootstrap confidence intervals](bootstrap-confidence-intervals.md), [calibration](../concepts/calibration.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [CHAIR](chair.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [component ablation](component-ablation.md), [contrastive activation addition](contrastive-activation-addition.md), [contrastive decoding](contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [distribution mismatch](../concepts/distribution-mismatch.md), [expected calibration error](expected-calibration-error.md), [GPT-4](../models/gpt-4.md), [GSM8K](../datasets/gsm8k.md), [hallucination](../concepts/hallucination.md), [interpretability illusion](../concepts/interpretability-illusion.md), [KV cache](../concepts/kv-cache.md), [linear probe](linear-probe.md), [LLaVA-1.5](../models/llava-1-5.md), [LLM-as-a-judge](llm-as-a-judge.md), [low-rank approximation](low-rank-approximation.md), [Mistral-7B](../models/mistral-7b.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [POPE](../datasets/pope.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-Coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-8B](../models/qwen3-8b.md), [reproducibility](../concepts/reproducibility.md), [residual stream](../concepts/residual-stream.md), [selectivity control](selectivity-control.md), [self-consistency](self-consistency.md), [state tracking](../concepts/state-tracking.md), [steering vector](steering-vector.md), [supervised fine-tuning](supervised-fine-tuning.md), [TempCompass](../datasets/tempcompass.md), [training-free intervention](training-free-intervention.md), [Vicuna-7B](../models/vicuna-7b.md)

## Appears in

- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.
- [Reproducing and Stress-Testing Two Approaches to LLM Reasoning Reliability: Test-Time Probability Aggregation and Logic-Representation Editing](../../archive/papers/2026/arxiv-2608-08514/summary.md) — Independently reproduces two published reliability methods and stress-tests them across models and domains their authors never tried, finding one reproduces exactly but loses significance everywhere new, and the other rests on a decodable logic direction that a same-norm random direction matches exactly under steering.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
