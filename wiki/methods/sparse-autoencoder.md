# sparse autoencoder

<!-- auto:begin -->

An autoencoder trained to reconstruct a model's internal activations through a wider hidden layer under a sparsity penalty, so its rows form an overcomplete dictionary and any activation is a sparse combination of them; the motivation is that features are believed to be in superposition and therefore not aligned with neurons. The sources apply the idea at different granularities. The original works token-wise on the residual stream and shows the learned directions score higher on automated interpretability than PCA, ICA or the neuron basis. A later one argues token granularity is the wrong unit for reasoning and encodes whole reasoning steps, conditioning encoder and decoder on the preceding trajectory so the code carries only what the step adds. A third uses the features as the basis for multi-layer steering vectors selected by co-activation and decoder-direction alignment. Two entries qualify the method rather than extend it: run-to-run feature consistency is not guaranteed and is argued to belong alongside reconstruction and sparsity as an evaluation axis, and in a bias-analysis setting the technique improves how recoverable a concept is while attenuating its measured influence, so a better dictionary is not automatically a better causal account. Reconstruction is lossy throughout — replacing a layer with its reconstruction raises perplexity from 25 to 40 in the token-level work.

- **Kind**: method
- **Also called**: SAE, Sparse Autoencoder, sparse dictionary learning
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 10

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [ablation](ablation.md), [activation patching](activation-patching.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [BBH](../datasets/bbh.md), [causal mediation analysis](causal-mediation-analysis.md), [circuit analysis](circuit-analysis.md), [circuit discovery](circuit-discovery.md), [contrastive activation addition](contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPQA](../datasets/gpqa.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [importance sampling](importance-sampling.md), [indirect object identification](../datasets/indirect-object-identification.md), [information bottleneck](../concepts/information-bottleneck.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](knowledge-distillation.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [linear separability](../concepts/linear-separability.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [logit lens](logit-lens.md), [LoRA](lora.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monosemanticity](../concepts/monosemanticity.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [overthinking](../concepts/overthinking.md), [PCA](pca.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [polysemanticity](../concepts/polysemanticity.md), [Pythia-410M](../models/pythia-410m.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [reproducibility](../concepts/reproducibility.md), [residual stream](../concepts/residual-stream.md), [ridge regression](ridge-regression.md), [SciQ](../datasets/sciq.md), [selectivity control](selectivity-control.md), [self-consistency](self-consistency.md), [self-verification](../concepts/self-verification.md), [superposition](../concepts/superposition.md), [the Pile](../datasets/the-pile.md), [TruthfulQA](../datasets/truthfulqa.md), [tuned lens](tuned-lens.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) — Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.
- [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](../../archive/papers/2026/arxiv-2608-06300/summary.md) — Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.
- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) — Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Finding Usable Weight Mechanisms with Tiled SVD](../../archive/papers/2026/arxiv-2608-06969/summary.md) — Extracts interpretable units directly from a transformer's weight matrices by column-tiled SVD, so a unit's identity is the weight rule itself rather than an atom of a separately trained dictionary, and judges them with a pre-registered suite whose central move is refusing a metric that a trivial baseline would win.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-11197/summary.md) — Takes the set of active sparse-autoencoder latents as the unit of analysis and finds that adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active, which contradicts the bag-of-features reading those sets are usually given.
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

<!-- analysis-sources: 10 -->
