# sparse autoencoder

<!-- auto:begin -->

Learning an overcomplete dictionary on model activations under a sparsity penalty, so that a polysemantic activation vector is decomposed into features that admit individual interpretation. Across 15 sources it is the dominant tool for this and the one the archive holds the most evidence against as a source of stable facts. The core problem is non-identifiability, and it is empirical before it is theoretical: different training seeds and dictionary widths recover materially different features from the same activations, dictionaries absorb and split features, and residual-stream components remain uncaptured by any known variant -- so two studies using different dictionaries are not measuring the same object. The theoretical companion in the corpus argues the failure is structural rather than algorithmic, since a reconstruction-and-sparsity objective does not enforce the invariance identifiability would require. Quality is also lossy and depth-dependent: automated interpretability scores decline from about 0.30 at layer 0 to 0.15 by layer 5, against about 0.14 for an independent-components baseline and 0.06 to 0.08 for random directions, and substituting reconstructed activations back raises perplexity from 25 to 40. Two scope limits recur: it must be trained per layer per model, which makes it costly and model-specific rather than endogenous, and it operates at the token level, which mismatches the unit reasoning happens in. The archive's practical position is that a sparse-autoencoder feature is a hypothesis about a direction rather than a measurement of one, and that any claim built on a specific dictionary should state the dictionary and, ideally, be checked against a second.

- **Kind**: method
- **Also called**: SAE, Sparse Autoencoder, sparse dictionary learning
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 15

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [ablation](ablation.md), [activation patching](activation-patching.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [annotation agreement](../concepts/annotation-agreement.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [ARC-Challenge](../datasets/arc-challenge.md), [ARC-Easy](../datasets/arc-easy.md), [BBH](../datasets/bbh.md), [causal intervention](../concepts/causal-intervention.md), [causal mediation analysis](causal-mediation-analysis.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [circuit analysis](circuit-analysis.md), [circuit discovery](circuit-discovery.md), [Cohen's kappa](cohen-s-kappa.md), [compression](../concepts/compression.md), [contrastive activation addition](contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [degenerate generation](../concepts/degenerate-generation.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [feature absorption](../concepts/feature-absorption.md), [feature consistency](../concepts/feature-consistency.md), [Gemma-2-2B](../models/gemma-2-2b.md), [Gemma-3-4B](../models/gemma-3-4b.md), [Gemma-3-4B-it](../models/gemma-3-4b-it.md), [GPQA](../datasets/gpqa.md), [GPT-2](../models/gpt-2.md), [GPT-2 small](../models/gpt-2-small.md), [GPT-2 XL](../models/gpt-2-xl.md), [GSM8K](../datasets/gsm8k.md), [human evaluation](human-evaluation.md), [HumanEval+](../datasets/humaneval.md), [identifiability](../concepts/identifiability.md), [IFEval](../datasets/ifeval.md), [importance sampling](importance-sampling.md), [indirect object identification](../datasets/indirect-object-identification.md), [information bottleneck](../concepts/information-bottleneck.md), [interpretability illusion](../concepts/interpretability-illusion.md), [Jaccard similarity](jaccard-similarity.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [linear separability](../concepts/linear-separability.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [logit lens](logit-lens.md), [LoRA](lora.md), [low-rank approximation](low-rank-approximation.md), [matched-budget comparison](matched-budget-comparison.md), [MATH500](../datasets/math500.md), [MBPP+](../datasets/mbpp.md), [metacognition](../concepts/metacognition.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monosemanticity](../concepts/monosemanticity.md), [OlympiadBench](../datasets/olympiadbench.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [overthinking](../concepts/overthinking.md), [PCA](pca.md), [persona conditioning](persona-conditioning.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [polysemanticity](../concepts/polysemanticity.md), [pre-registration](pre-registration.md), [PubMedQA](../datasets/pubmedqa.md), [Pythia-410M](../models/pythia-410m.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [Qwen3-8B](../models/qwen3-8b.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [reasoning collapse](../concepts/reasoning-collapse.md), [representation versus readout](../concepts/representation-versus-readout.md), [reproducibility](../concepts/reproducibility.md), [residual stream](../concepts/residual-stream.md), [ridge regression](ridge-regression.md), [safety case](../concepts/safety-case.md), [SciQ](../datasets/sciq.md), [selectivity control](selectivity-control.md), [self-consistency](self-consistency.md), [self-verification](../concepts/self-verification.md), [sparse dictionary learning](sparse-dictionary-learning.md), [steering vector](steering-vector.md), [superposition](../concepts/superposition.md), [the Pile](../datasets/the-pile.md), [TruthfulQA](../datasets/truthfulqa.md), [tuned lens](tuned-lens.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) — Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.
- [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](../../archive/papers/2026/arxiv-2608-06300/summary.md) — Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.
- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) — Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Finding Usable Weight Mechanisms with Tiled SVD](../../archive/papers/2026/arxiv-2608-06969/summary.md) — Extracts interpretable units directly from a transformer's weight matrices by column-tiled SVD, so a unit's identity is the weight rule itself rather than an atom of a separately trained dictionary, and judges them with a pre-registered suite whose central move is refusing a metric that a trivial baseline would win.
- ["Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-07852/summary.md) — Decomposes three speaker settings -- the default Assistant, an assigned roleplay persona, and a narrated story character -- into sparse-autoencoder features at turn boundaries and pronoun tokens, and finds that roleplay personas retain an Assistant-associated feature core while differentiating from it across depth, where story characters never acquire that core at all.
- [Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-08168/summary.md) — Trains separate Top-K sparse autoencoders on a reasoning model's activations in thinking and non-thinking modes, and finds that suppressing the most active reasoning features destroys mathematical formatting as reliably as it destroys reasoning -- with the model responding by generating 454 percent more tokens of lower-diversity, more metacognitively marked text rather than stopping.
- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) — Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.
- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) — Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-11197/summary.md) — Takes the set of active sparse-autoencoder latents as the unit of analysis and finds that adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active, which contradicts the bag-of-features reading those sets are usually given.
- [Probing and steering biology across Boltz-1s trunk-diffusion boundary](../../archive/papers/2026/arxiv-2608-11475/summary.md) — Probes and steers across the trunk-to-diffusion boundary of an AlphaFold3-class structure predictor, finding that geometry survives the crossing while sequence chemistry is attenuated, and that a strand direction predictive at F1 0.82 steers nothing at all -- with an architectural explanation for why.
- [Mechanistic Interpretability Should Prioritize Feature Consistency in Sparse Autoencoders](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-99/summary.md) — Argues run-to-run feature consistency should be a standard SAE evaluation axis alongside reconstruction and sparsity, and gives a metric showing high consistency is achievable.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

### Why the step-level variant matters more here than the token-level one

The archive holds both, and for a group reading about reasoning they are not
equally useful. The token-level paper is foundational but its subject is
language models in general; its advantage over ICA also narrows with depth and
is minimal in the final layer, which is where features relevant to complex
behaviour would be expected. The step-level paper (SSAE) is the one that makes
the technique say something about reasoning, and it does so through one design
choice worth isolating:

> Condition the **decoder** on the preceding context, not just the encoder.

Because the decoder can already read the background, the sparse code has no
reason to store it, so whatever the code carries is the step's *increment*. That
turns a generic disentanglement objective into a specific one — separate what
this step contributes from what it inherited — and it is the reason step
correctness becomes decodable at all. Anyone probing reasoning traces without
this control is probing accumulated context as much as the step.

### The finding to carry forward

Step correctness is linearly decodable from a step's own code at 78-86%
accuracy. The information that a step is wrong exists at the moment the step is
produced, and the trajectory proceeds into the error anyway. That is the same
failure the archive calls silent divergence, now located in a representation
rather than inferred from behaviour, and it is the strongest evidence here that
unfaithfulness is partly a *calibration* failure rather than an absence of
internal signal.

Two cautions before building on it. First, probing shows information is present,
not that the generation pathway uses it — the inference from "decodable" to "the
model knows" is doing real work in that paper and is not established. Second,
the paper's claim that token-level SAEs perform near baseline is contradicted by
its own Table 1 on MATH-500 correctness, where token SAEs reach 86.8 against a
naive 70.7 and beat one SSAE variant; the step-level advantage is solid for
logicality, step length and first-token perplexity, and not solid for that cell.

### Open thread

If step correctness is probeable without step labels, this is a route to
[[process-supervision]] signal that costs no annotation — the same target EDIS
names as future work from the entropy side. Two independent methods now point at
unsupervised process supervision from different directions, which makes it the
most concrete open direction in this archive.

### Revised at eight sources: what a set of latents is not

A new entry attacks the level above the individual latent, and it matters for
everything the section above builds on. **Beyond a Bag of Features** takes the
*set* of active latents as the unit — the object every "which concepts are
present here" reading implicitly uses — and tests the composition property that
reading requires.

Prefix a compatible adjective to a noun and the noun's own signature should be
preserved while the adjective's is added. Instead **20–60% of the noun's active
latents go away**, rising with the number of adjectives and often with depth.
The decomposition is what makes this hard to dismiss:

| Check | Result |
| --- | --- |
| Were the lost latents used at all? | ~60% were active upstream in middle layers, and the noun-only restriction agrees — they were active *on the noun itself* |
| Suppressed or removed? | ~80% sit in the near-zero pre-activation band, only 10–20% strongly negative |
| Feature absorption? | Matryoshka SAEs, built to mitigate it, show the same rates |
| Geometric interference? | Judged insufficient for the magnitude and structure |

So the latents are dropped rather than pushed down, they were doing work
immediately before, and neither standard explanation covers it.

**The quieter result is the one to weigh against the whole method.** Replacing
cosine similarity over dense states with Jaccard overlap over SAE signatures
does not improve alignment with human conceptual structure — category-boundary
recovery is no better and the best SAE score stays *below* the best dense one,
while within-category typicality correlations fluctuate around zero. What
signature overlap does track is the dense geometry it was meant to decompose.
The dictionary buys per-latent nameability; it does not buy a closer match to
human categories.

### Both halves of the trade are now in the archive

Read alongside **Finding Usable Weight Mechanisms with Tiled SVD**, arriving the
same day, the two entries state a choice rather than a ranking:

| | Identity lives in | Composition | Names |
| --- | --- | --- | --- |
| SAE latents | a separately trained dictionary | fails under a compatible refinement | yes, per latent |
| Tile-SVD mounts | the weight matrix itself | is the weight rule, so nothing to fail | **none** — the paper says so |

The SVD paper explicitly declines to claim a replacement for sparse
autoencoders in concept discovery, and it is right to: its units carry no
semantic labels. But it does supply something this archive wanted and could not
get from the SAE line — a **depth curve for detection against intervention**.
For the same write direction it computes what an unembedding lens predicts and
what steering actually does, and the agreement runs from about zero in layers
0–5 to ρ ≈ 0.91 at the final layer. See [[detection-versus-control]]: the gap
the archive keeps citing is not a constant, and it is widest exactly where most
probing is done.

### A third route, at nine sources

The table above sets dictionaries against weight rules. *Interpreting Language
Model Hidden States at Scale* is neither: a **trained lens** decodes an
activation through the model's own frozen normalization and unembedding, so the
readout is the model's vocabulary rather than a learned codebook or a weight
factorization. Its contribution to this note is that it makes such lenses cheap
enough to attach *densely* — every layer, and residual, attention and MLP alike,
482 of them on a 70B model — which is what lets it ask a question the sparse
designs cannot.

The answer bears on how any of the three routes should be used. Ranking
components by how visible a behaviour is and by how much intervening on them
helps gives **negatively correlated orders, Spearman −0.43**. And the prior
attention-head localization reproduces exactly while being wrong about where to
act, because the effective targets were in component types nobody had
instrumented. Coverage, not fidelity, was the binding constraint.

### The tenth source adds nothing, and that is worth recording

*MI-MIDI* counts as evidence here because it names sparse autoencoders, but it
reports no result about them: its analysis is probing, the logit and tuned
lenses, activation patching and difference-in-means steering, and SAEs appear
only as ongoing work whose results the authors defer to a follow-up
publication. Nothing in the table above changes.

It is recorded rather than passed over because the counter that flags this note
as stale cannot tell an added source from an added finding. A reader who sees
nine become ten should not go looking for what moved.

### At twelve: the variability is structural, and the feature count may not be a count

Two entries arriving together change what this note can say about SAE
instability. The archive already held that different seeds and widths recover
materially different features. What it lacked was a reason.

**A theorem, and a remedy that moves the outcome.** *Intrinsic Structure* proves
the non-identifiability is **structural rather than algorithmic**: the
reconstruction-and-sparsity objective does not enforce the invariance that
identifiability requires, so no amount of better training fixes it. That would
be a diagnosis only, except the paper adds the missing term and shows the
outcome move — raising the invariance penalty cuts the relative invariance
residual 24% (0.438 → 0.333) and the split-half spectral distance, *identifiability
itself rather than a proxy*, by **41%** (0.0170 → 0.0101) at matched sparsity.

The price is reported in the same runs and it is real: reconstruction degrades
(FVU 0.222 → 0.255), the live-feature fraction falls 0.77 → 0.58, cross-seed
feature agreement moves the **wrong way**, and at a higher penalty the dictionary
collapses outright across all three seeds. Whether a dictionary can be sparse,
reconstructive and invariant at once is left open. The measured invariance gap
puts SAEs furthest from invariance on all three models — further than a *random
orthonormal control*, at 2.1×/3.1×/3.4× the spectral residual, strengthening with
scale across three SAE families — but the authors then retract half of it: the
ordering **inverts under variance-based feature selection**, so the claim holds
for the subset a practitioner actually reads (features that fire often) and not
for the span. Their pre-registered version of this criterion passed in 49% of 75
cells against a registered 80%, and they report that as a failure.

**A caution about reading dictionary sizes at all.** *Post-Hoc Sparse Coding of
Latent Communication* fits an SAE to a frozen agent-to-agent channel and finds
**50 of 4096** features ever active — 98.78% dead — with the top ten appearing in
all nine tasks and cross-task Jaccard similarity averaging 0.906. It then
declines its own headline: that support size is equally compatible with low-rank
input structure, repeated token positions, or optimisation collapse, and the
Jaccard figures may be inflated by set saturation when the global support is
only ~50 features. It also names the control that would undercut it (an
18-position payload is already comparable in size to the sparse one) and reports
not having run it.

Read together: a small active support is not evidence of a compact vocabulary
until low-rank and optimisation-collapse explanations have been excluded, and
cross-seed agreement can move opposite to identifiability, so the two are not
interchangeable measures of the same thing.

### At thirteen: the same verdict from a domain with no language in it

The **Boltz-1 study** trains SAEs on the trunk and diffusion activations of a
protein-structure predictor and reaches the table above's conclusion
independently: wherever a label already exists, a supervised probe beats the
best single SAE latent — by **0.13–0.35 F1** (helix 0.85 vs 0.72; strand 0.82 vs
0.47) — and probes steer more reliably, with the coil probe moving coil content
where the best coil latent does not.

Its distinctive contribution is a caution about *scoring* dictionaries at all.
The same concepts on identical activations score **0.85 against dense structural
labels and 0.42 against sparse experimental ones**; recomputing the dense labels
on the model's own prediction moves the score by only 0.06–0.08, which rules out
structural disagreement and establishes the gap as **under-annotation**. Every
score against an incomplete annotation set is therefore a lower bound, and
cross-paper comparisons of feature quality are only meaningful at matched label
density. The authors add the corresponding warning about their own method:
best-of-many latent selection inflates scores for rare concepts.

What is left for dictionaries is the job the labels cannot do. A companion
analysis of these same trunk SAEs recovers a putative zinc-coordination cluster
and a kinase catalytic-histidine motif **with no matching annotation** — which
is the honest version of the claim: hypothesis generation for features no
vocabulary contains, requiring independent validation, rather than a better
readout for concepts that already have one.

### At fourteen: an intervention without a null

*Thinking vs. NoThinking* trains mode-paired Top-K SAEs on a reasoning model and
suppresses its three highest-volume features. The headline is that reasoning and
formatting are coupled: whichever feature is suppressed, LaTeX density falls
29.54–40.28 per 1k tokens and boxed-answer retention drops to ~0%.

Read against this note's accumulated standards, that claim is **not established**,
for two reasons the paper does not address.

- **No matched control.** No random feature of comparable activation volume, no
  orthogonal direction, no null condition. This archive's position is that an
  intervention without something that should produce *no* effect reports that
  something changed, not that the right thing did.
- **The selection criterion is magnitude.** Total Activation Volume ranks
  features by how much they fire, so "the model's most important features" means
  *the loudest*. Same structure as the number-neuron result in
  [[activation-steering]]: a criterion that selects on one property will return
  that property.

There is also a simpler untested explanation for the coupling itself — LaTeX and
boxed answers are what the thinking-mode training distribution *looks like*, so
any high-volume thinking feature is entangled with that surface form whether or
not it carries reasoning.

**What does survive is the failure mode, and it is worth keeping.** Disrupting
the reasoning features does not stop generation: output grows **+454%** while
lexical diversity falls **63%** and metacognitive markers rise **+34.17** per 1k
tokens. A model whose reasoning machinery is impaired emits *more* hedging and
*more* repetition. So trace length and metacognitive density move the wrong way
as diagnostics — an impaired trace reads as a more deliberative one. That is the
same shape as the archive's finding that a local metric can be driven to its
ceiling by a degenerate generation.

### At fifteen: what a judge-backed feature pipeline should look like

*"Many Are My Names"* decomposes three speaker settings — the default Assistant,
an assigned roleplay persona, a narrated story character — into SAE features at
turn-boundary and pronoun positions. Its substantive finding is that roleplay
personas **retain an Assistant-associated feature core** while differentiating
from it with depth (operational machinery first, then tone, then content), and
that story characters never acquire that core at all.

What earns it a place in *this* note is the instrument validation, which this
archive's SAE entries almost never supply:

- Two **human** annotators independently label 191 generations: 93% agreement,
  **κ = 0.85** — establishing the task is reproducible *before* any model is
  scored on it.
- The LLM judge is then measured against the primary annotator: precision 0.90,
  recall 0.98, accuracy 0.92, with generations **reweighted by inverse sampling
  rate** within each (feature, label) stratum so the figures describe a randomly
  drawn generation rather than an oversampled one.
- The asymmetry is *acted on*: high recall means few missed effects, 90%
  precision means false positives, so a feature is tagged only on evidence from
  **all six** steering groups.

That is the shape a judge-based feature pipeline should have, and it is cheap.

The authors are also disciplined about the ceiling of feature-level evidence,
stating their features are **not necessary, sufficient, or exhaustive**, treating
their split factor as a heuristic because no feature-splitting measurement exists
for their exact SAE, and refusing to read a shared core as a shared subject in
either direction.

<!-- analysis-sources: 15 -->
