# selectivity control

<!-- auto:begin -->

A deliberately meaningless version of an experiment, run under identical conditions, whose job is to produce no effect -- so that an effect in the real condition means something. Both sources treat it as what makes their central claim readable rather than as an appendix. The text-to-MIDI work retrains every probe on labels shuffled between tokens with the group split preserved, and reports that the control probe collapses to the majority baseline for every concept (lift -0.068 to +0.001 in one model, -0.044 to -0.002 in the other), which is what licenses reading probe accuracy as information in the activations rather than capacity of the probe; its patching experiments carry the same discipline with a self-patch control that is zero by construction and a neutral-prompt control for nonspecific disruption. The scratchpad-editing work uses same-rank random and orthogonal-complement patches, which reach about 0.02 agreement where the real edit reaches 0.80 to 0.91, plus pretrained and final-answer-only model controls that stay near baseline. The two sources differ in what they randomise -- labels in one, the intervention direction in the other -- and agree on the standard: an intervention or probe result without a matched condition that should do nothing reports that something changed, not that the right thing did.

- **Kind**: method
- **Also called**: control task, selectivity
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [difference-in-means direction](difference-in-means-direction.md), [KV cache](../concepts/kv-cache.md), [linear probe](linear-probe.md), [linear separability](../concepts/linear-separability.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [logit lens](logit-lens.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-coder-7B](../models/qwen2-5-coder-7b.md), [residual stream](../concepts/residual-stream.md), [sparse autoencoder](sparse-autoencoder.md), [state tracking](../concepts/state-tracking.md), [supervised fine-tuning](supervised-fine-tuning.md), [tuned lens](tuned-lens.md)

## Appears in

- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) — Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
