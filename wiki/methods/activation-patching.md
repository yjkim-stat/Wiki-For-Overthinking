# activation patching

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: causal intervention, causal tracing, interchange intervention, patching, representation denoising
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 17

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [ablation](ablation.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [attention head](../concepts/attention-head.md), [attention pattern](../concepts/attention-pattern.md), [BeaverTails](../datasets/beavertails.md), [calibration](calibration.md), [causal analysis](causal-analysis.md), [causal intervention](causal-intervention.md), [causal mediation analysis](causal-mediation-analysis.md), [causal tracing](causal-tracing.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [circuit analysis](circuit-analysis.md), [circuit discovery](circuit-discovery.md), [counterfactual intervention](counterfactual-intervention.md), [curriculum learning](../concepts/curriculum-learning.md), [detection versus control](../concepts/detection-versus-control.md), [effective depth](../concepts/effective-depth.md), [Gemma-4-12B](../models/gemma-4-12b.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [Gemma-4-31B-it](../models/gemma-4-31b-it.md), [generalization](../concepts/generalization.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-J 6B](../models/gpt-j-6b.md), [GSM8K](../datasets/gsm8k.md), [hallucination](../concepts/hallucination.md), [implicit reasoning](../concepts/implicit-reasoning.md), [importance sampling](importance-sampling.md), [indirect object identification](../datasets/indirect-object-identification.md), [information bottleneck](../concepts/information-bottleneck.md), [KL divergence](../concepts/kl-divergence.md), [KL regularization](kl-regularization.md), [knowledge distillation](knowledge-distillation.md), [KV cache](../concepts/kv-cache.md), [linear probe](linear-probe.md), [linear separability](../concepts/linear-separability.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [logit lens](logit-lens.md), [LoRA](lora.md), [low-rank weight ablation](low-rank-weight-ablation.md), [MATH500](../datasets/math500.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [memorization](../concepts/memorization.md), [Mistral-7B](../models/mistral-7b.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [modularity](../concepts/modularity.md), [monitorability](../concepts/monitorability.md), [monosemanticity](../concepts/monosemanticity.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [PCA](pca.md), [permutation test](permutation-test.md), [Phi-4](../models/phi-4.md), [polysemanticity](../concepts/polysemanticity.md), [predictive entropy](../concepts/predictive-entropy.md), [process supervision](../concepts/process-supervision.md), [Pythia-410M](../models/pythia-410m.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-30B-A3B-Thinking-2507](../models/qwen3-30b-a3b-thinking-2507.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [Qwen3-VL](../models/qwen3-vl.md), [ReAct](react.md), [representation versus readout](../concepts/representation-versus-readout.md), [reproducibility](../concepts/reproducibility.md), [residual stream](../concepts/residual-stream.md), [ridge regression](ridge-regression.md), [scaling laws](../concepts/scaling-laws.md), [SciQ](../datasets/sciq.md), [selectivity control](../concepts/selectivity-control.md), [self-consistency](self-consistency.md), [self-repair](../concepts/self-repair.md), [self-verification](../concepts/self-verification.md), [semantic entropy](semantic-entropy.md), [sparse autoencoder](sparse-autoencoder.md), [state tracking](../concepts/state-tracking.md), [superposition](../concepts/superposition.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [the Pile](../datasets/the-pile.md), [tuned lens](tuned-lens.md), [uncertainty quantification](../concepts/uncertainty-quantification.md), [weight-space ablation](weight-space-ablation.md), [WikiText-2](../datasets/wikitext-2.md)

## What we have settled

- **Established** — How well a direction or signal detects a property licenses no claim about what intervening on it does — not the size of the effect, and not even its sign.
  - Six sources now, and the 2026 additions supply the two cases the earlier three left open. The sign case is measured directly: with lenses attached densely enough to compare all six hookpoint types, detection and intervention rankings over components are negatively correlated at Spearman -0.43, MLP outputs showing the weakest detected toxic signal and producing the largest reduction when modified while MLP inputs do the reverse. The same paper adds a second-order warning -- the published attention-head result reproduces exactly and is still misleading, because the most effective targets were in components nobody had instrumented. The magnitude case: the canonical refusal direction predicts a steering vector's safety damage by cosine similarity and ablating it recovers at most about 8 points of mean attack success rate, leaving worst-case unchanged on two of three models, while a direction learned against the intervention's own objective goes below the unsteered baseline. And the gap is not a constant: computing an unembedding lens's prediction and the actual effect of steering for the same write direction gives agreement rising from about zero in layers 0-5 to 0.91 at the final layer, so it is widest exactly where most probing is done.

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) — Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.
- [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](../../archive/papers/2026/arxiv-2608-03629/summary.md) — Extends a single-block interaction theorem to ablated subsets spanning many layers, isolates the cross-layer remainder as an exact double integral rather than bounding it, supplies the one missing closed-form ingredient (a local attention Jacobian bound, verified without a violation on a real 1.5B model), and tests the whole picture on an emergent circuit nobody designed for it — reporting the mixed outcome as mixed.
- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) — Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](../../archive/papers/2026/arxiv-2608-10430/summary.md) — Detects the class of hallucination where a model confidently fabricates a parameter the user never gave, by running a LoRA adapter alongside the frozen model that restructures the residual stream and then names the offending parameter in words the agent can act on.
- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.
- [Multi-component Causal Tracing in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-154/summary.md) — Generalizes causal tracing from one component or layer at a time to selecting subsets of components jointly, by relaxing the combinatorial search into a continuous one over soft interventions.
- [Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1265/summary.md) — Traces how individual prompt tokens ground into image regions during diffusion denoising, using fixed-seed single-word removal for causal faithfulness and a head-resolved spike score for attribution.
- [Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2031/summary.md) — Explains LLM counting failures as a depth limit, since counting is computed across layers, and fixes it with a System-2 decomposition whose mechanism is then traced.
- [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](../../archive/papers/2025/local-26fdb25b9d157d04/summary.md) — Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.
- [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](../../archive/papers/2024/local-956614b275995bc4/summary.md) — Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.
- [A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning](../../archive/papers/2025/local-99a25b62fd9ad86c/summary.md) — Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.

<!-- auto:end -->

## Notes

### Read the methodology paper before using any circuit result

*Towards Best Practices of Activation Patching* is not a result about a model,
it is a warning about a literature. Varying only the corruption method changes
which attention heads a study reports as important; varying only the metric
changes it again; and sliding-window patching inflates apparent localization by
at least 20% over summed single-layer effects. The recommendations are cheap to
follow — replace tokens with semantically related ones rather than adding
Gaussian noise, score with logit difference rather than probability, try
single-layer patching first — and the paper shows Gaussian noise producing a
detection with the **wrong sign** on a head that prior work established is
helpful.

The general lesson generalizes past this technique: any intervention that pushes
a model off its training distribution can break the mechanism it was meant to
measure, so the intervention's own in-distribution-ness is part of the method,
not a detail.

### The bridge to reasoning has arrived

This note previously recorded that activation patching sat unconnected to the
reasoning half of the archive. That gap is now closed from two directions.

**Counterfactual state editing** applies the technique to a written reasoning
state and, crucially, fixes the loose scoring criterion the methodology paper
warns about. Ordinary patching asks "did the output change", which almost any
perturbation can satisfy. Because the task's transition rule is known, this asks
"did the next state become the one implied by *applying the actual move to the
edited value*" — a target with exactly one right answer that generic next-token
steering cannot hit. Two selectivity controls (swap the move; inject a
counterfactual state with an incompatible future) close the remaining loopholes.
This is the strongest form of the technique in the archive, and it is worth
treating as the template.

**AttriCoT** goes the other way: black-box unit removal plus a fitted structural
causal model, no internals needed. Cheaper and applicable to any trace, but it
inherits precisely the concern above — a trace with a step excised is not a
trace the model would have produced, so unit removal is an off-distribution
intervention of the same family as Gaussian noising.

### The remaining gap, stated precisely

The archive now has patching applied to a **synthetic one-bit state** and
attribution applied to **natural-language traces**. It does not have
representation-level patching of natural-language reasoning states, because the
intermediate variables there are rarely specified enough to give an edit a
single correct consequence. The state-editing authors say this explicitly and
name program states, theorem-prover goals and tool-call arguments as the
realistic next domains. That is the concrete opening: reasoning tasks whose
intermediate variables have checkable consequences.

### It measures a different quantity than ablation, and the gap is exact

The section above is about how patching can be run badly. A pair of theory
papers now establishes something prior to that: patching run *perfectly* still
does not measure what weight-space ablation measures, and the two disagree by an
amount that is written down rather than estimated.

Inside an idealized model where a conditional is carried additively through the
residual stream:

| Intervention | What it moves the readout by |
| --- | --- |
| Patching carrier *i* from donor to receiver | its **contrast** across the pair, β_i·(α_i(x_A) − α_i(x_B)) |
| Ablating carrier *i* in weight space | its **absolute level** at the receiver, −β_i·α_i(x_B) |

**Neither bounds the other.** The papers construct matched pairs on which every
single-carrier patch flips the decision while no single-carrier ablation does —
the redundancy regime, produced with no repair mechanism at all, so this is not
the Hydra effect under another name. The same construction is the sense in which
"patching overstates importance and ablation understates it" stops being a
caution and becomes an identity.

**It is not a small-model artifact.** On an emergent indirect-object circuit in
Qwen2.5-1.5B-Instruct — found by the field's own greedy patching search, never
designed for these claims — the gap between the patching effect and the ablation
effect is **0.224 to 0.852 on all five lexical instances**, never small. So the
dissociation is what happens when either instrument is used on an ordinary
circuit, not an edge case one can hope to avoid.

**What follows for reading circuit claims here.** A claim resting on one of the
two interventions should name which, and treat the other as an open question
rather than as corroboration. The archive already holds the same shape one level
down — [[detection-versus-control]], where a direction's discriminability
licenses no claim about steering it, in sign or in magnitude.

### What is not established

Both papers are one research programme by one author, so this is a single
independent source and is recorded here rather than as a finding. The theory
rests on residual additivity and a linear readout; the multi-layer remainder is
isolated exactly and **not bounded**, with the missing ingredient named and left
open. The real-model check is one model, one mechanism, five instances — with
collapse absent on one of them, the interaction probe applicable to only three,
and none of those three in the configuration any theorem covers. The authors say
all of this themselves, and withdrew a cleaner empirical claim from the first
paper when it failed out of sample.

### Revised at sixteen sources: two variants and a warning about reach

Two entries added on 2026-08-14 use patching for something other than circuit
discovery, and both are worth having.

**Cross-trajectory patching.** *Actionable Hallucination Detection* patches at a
single trigger token, but between *different trajectories* rather than between a
clean and a corrupted version of one input. Overwriting the clean run's hidden
state at layer L with the corrupted run's flips 96% of trajectories to the
hallucination label, with negligible effect through layer 20 and a sharp
inversion peaking at layer 32. The design answers a question the standard
corrupt-one-input form cannot: not "does this state carry the signal here" but
"does the signal mean the same thing across contexts". Worth borrowing.

**The reach of the instrument decides the conclusion.** *OmniLens* is not a
patching paper — it makes trained lenses cheap enough to attach to every layer
and to residual, attention and MLP alike — but its toxicity case study is the
sharpest available caution for causal work generally. The published result that
toxic signal concentrates in a few attention heads **reproduces exactly**, and
is still misleading: once all six component types are instrumented, the most
effective intervention targets lie *outside* the heads anyone had examined, and
differ between models.

That is a second-order version of the dissociation above. The first says a
patching claim and an ablation claim are different claims. This one says a claim
about *where* is bounded by where the method could reach, and a method that
reaches only attention heads will find its answer among attention heads. The
same paper supplies the measurement: over component types, detection and
intervention rankings correlate at **Spearman −0.43**, with MLP outputs weakest
under detection and largest under intervention, and MLP inputs the reverse — so
the components a localization study is most likely to notice are not the ones
worth acting on. That number now sits in [[detection-versus-control]].

### At seventeen: a patching design worth copying, and a null read correctly

*MI-MIDI* applies the technique outside language, to two text-to-MIDI
generators, and two things about how it runs the experiment are worth having
here regardless of the domain.

**The control pair.** It patches prompt activations at the input to layer L from
a contrasting instrument prompt (piano against violin) and scores the shift in
piano-note fraction from 0 (no transfer) to 1 (full). What makes it readable is
the pair of guards: a **self-patch control that is 0 by construction**, which
catches a scoring bug rather than a model fact, and a **neutral-prompt control**
that separates concept transfer from nonspecific disruption. The methodology
paper above says corruption choice decides the answer; this is the cheap version
of taking that seriously — you cannot tell whether an effect is specific without
something that should produce no effect.

**Patching as corroboration, not as the primary claim.** The interesting move is
that the patching result is not asked to stand alone. The logit lens says
MIDI-LLM's readout rotates out of its inherited textual basis at layers 13–15;
vocabulary-mass analysis says the same; and patching independently finds
instrument transfer holding near full through layer 13 then attenuating to 0.62
and 0.27 at layers 14 and 15. Three instruments, one band. Note also that the
attenuation is graded rather than binary, and the authors read it as a
transition band rather than a boundary — the honest reading of a curve that does
not step.

**The absent peak is given a mechanism, not a shrug.** In the encoder–decoder
model the mirror experiment patches cross-attention memory at one decoder layer
and finds no isolated depth peak against the neutral control. Rather than
reporting a null, the paper attributes it to distributed conditioning: the
decoder can re-read the original encoder memory at every other layer, so no
single layer is a bottleneck. That is the right shape for a negative patching
result — an architectural reason why localization *should* fail, which is
falsifiable, rather than a claim that nothing is there.

This does not disturb anything above. The dissociation between patching and
ablation, and the coverage limit *OmniLens* documents, both still apply: MI-MIDI
patches layer inputs only, so its own claim about where binding happens is
bounded by that reach in exactly the way this note keeps insisting.

<!-- analysis-sources: 17 -->
