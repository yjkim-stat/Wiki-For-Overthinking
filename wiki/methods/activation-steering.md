# activation steering

<!-- auto:begin -->

Adding a signed multiple of a fixed direction to the residual stream at inference so behaviour changes without retraining; the direction is usually a mean difference between activations on a small contrastive set, and the method is adopted because it is cheap -- one vector, computed once, applied at generation time. These sources agree on the mechanics and collectively falsify the assumption that licenses the standard recipe: the direction that best discriminates a concept is not reliably the one that steers it and can steer the opposite way, with one vector reaching AUC 0.97 while its steer factor correlates with the concept score at Spearman -1, so several papers here explicitly decline to select the intervention by classification accuracy. Three costs recur and are quantified rather than warned about. It damages refusal -- worst-case attack success rises more than 63 percent on one model -- though the damaging part is a separate direction that constrained optimisation can ablate, after which no attack across 108 configurations exceeds 4.2 points above the unsteered baseline; it over-steers into fluency collapse in a dose-graded and extremely concentrated way, with 97 percent of 942 severe events falling in a single trait-model cell at a median perplexity inflation of 810 points; and its gains are small and conditional, averaging +0.46 to +2.35 for reasoning-length steering and running +7.60 on six-step problems but -3.23 at eight steps for trajectory steering. Consequently where to inject is now treated as part of the method rather than as configuration: the best layers are a property of the individual input rather than of the task, all-layer injection is stable in a cross-attention-conditioned model while accumulating disruptively in a decoder-only one, and the archive's most reliable uses are gated on a predictor rather than applied unconditionally. The evidential minimum every careful source here meets is a magnitude-matched random direction: the identified vectors move the target metrics by 9 and 7 points where norm-matched random ones move either by at most 1.1.

- **Kind**: method
- **Also called**: Activation Steering, CAA, activation addition, contrastive activation addition, representation engineering, steering, steering vector, steering vectors
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 19

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [ablation](ablation.md), [activation patching](activation-patching.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AlpacaEval](../datasets/alpacaeval.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [ARC-Easy](../datasets/arc-easy.md), [attention head](../concepts/attention-head.md), [Aya-expanse-8B](../models/aya-expanse-8b.md), [BBH](../datasets/bbh.md), [beam search](beam-search.md), [benchmark design](../concepts/benchmark-design.md), [bootstrap confidence intervals](bootstrap-confidence-intervals.md), [budget forcing](budget-forcing.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought](chain-of-thought.md), [chain-of-thought distillation](chain-of-thought-distillation.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [circuit analysis](circuit-analysis.md), [circuit discovery](circuit-discovery.md), [class imbalance](../concepts/class-imbalance.md), [Claude Opus 4.7](../models/claude-opus-4-7.md), [CLIP](../models/clip.md), [Cohen's kappa](cohen-s-kappa.md), [construct validity](../concepts/construct-validity.md), [contrastive activation addition](contrastive-activation-addition.md), [DeepSeek](../models/deepseek.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [difference-of-means probe](difference-of-means-probe.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [Gemma-2-27B](../models/gemma-2-27b.md), [Gemma-2-2B](../models/gemma-2-2b.md), [Gemma-2-9B](../models/gemma-2-9b.md), [Gemma-3-12B](../models/gemma-3-12b.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPQA](../datasets/gpqa.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-5](../models/gpt-5.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [importance sampling](importance-sampling.md), [Inference Time Intervention](../concepts/inference-time-intervention.md), [interpretability illusion](../concepts/interpretability-illusion.md), [jailbreak](../concepts/jailbreak.md), [jury aggregation](jury-aggregation.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](knowledge-distillation.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [linear separability](../concepts/linear-separability.md), [literature survey](literature-survey.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Llama-3.2-1B-Instruct](../models/llama-3-2-1b-instruct.md), [Llama-3.2-3B](../models/llama-3-2-3b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [Llama-3.3-70B-Instruct](../models/llama-3-3-70b-instruct.md), [Llama-3-8B-Instruct](../models/llama-3-8b-instruct.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [logistic regression](logistic-regression.md), [logit lens](logit-lens.md), [LoRA](lora.md), [low-rank approximation](low-rank-approximation.md), [MATH500](../datasets/math500.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [monosemanticity](../concepts/monosemanticity.md), [nested cross-validation](nested-cross-validation.md), [OlympiadBench](../datasets/olympiadbench.md), [operating point](../concepts/operating-point.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [overthinking](../concepts/overthinking.md), [PCA](pca.md), [permutation test](permutation-test.md), [Phi-4](../models/phi-4.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [position bias](../concepts/position-bias.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen](../models/qwen.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-72B](../models/qwen2-5-72b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.5-2B](../models/qwen3-5-2b.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [randomized control](../concepts/randomized-control.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [ridge regression](ridge-regression.md), [ROC analysis](roc-analysis.md), [safety alignment](../concepts/safety-alignment.md), [SciQ](../datasets/sciq.md), [selection bias](../concepts/selection-bias.md), [selectivity control](selectivity-control.md), [self-repair](../concepts/self-repair.md), [Shapley value](../concepts/shapley-value.md), [shortcut learning](../concepts/shortcut-learning.md), [sparse autoencoder](sparse-autoencoder.md), [sparse dictionary learning](sparse-dictionary-learning.md), [steering vector](steering-vector.md), [structured chain of thought](structured-chain-of-thought.md), [superposition](../concepts/superposition.md), [supervised fine-tuning](supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [synthetic data generation](synthetic-data-generation.md), [t-SNE](t-sne.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md), [the Pile](../datasets/the-pile.md), [theory of mind](../concepts/theory-of-mind.md), [TruthfulQA](../datasets/truthfulqa.md), [tuned lens](tuned-lens.md), [WikiText-2](../datasets/wikitext-2.md), [XSTest](../datasets/xstest.md), [zero-shot prompting](zero-shot-prompting.md)

## What we have settled

- **Established** — Control over how long a reasoning model thinks is concentrated in a single special token rather than distributed over the trace, and four sources reach that token from four unrelated directions.
  - Nothing here set out to study the delimiter; each source arrives at it while answering a different question. Mechanism: the pre-allocated reasoning-strength vector steers length by shifting the logits of the end-of-thinking token specifically, with far larger effect there than on the end-of-sequence token or on random tokens. Representation: in deep layers the </think> position progressively aggregates the preceding chain, and during final-answer generation the model attends predominantly to it and only weakly to the intermediate steps. Training: a sequence-level efficiency reward implicitly penalizes long but correct trajectories, and confining that reward to one mode-selection token removes the coupling — after which adjusting that single token's generation probability at inference moves one trained model continuously along the efficiency-performance frontier. Failure mode: on QwQ-32B nearly every competing early-exit baseline fails, and the reason is sporadic invalidation of the end-of-thinking delimiter. The four are independent in method (activation steering, attention analysis, reward placement, baseline failure) and agree on the locus. This matters because the same literature's generation-time signals — token entropy, hidden-state norm, predictive entropy — all read diffuse quantities, while the compression work finds redundancy itself to be diffuse; a distributed signal aimed at a distributed phenomenon is the harder problem, and the delimiter is where the model has already concentrated the decision.
- **Established** — In activation steering the damage is attributed to the intervention but caused by its default setting: the canonical refusal direction and the fixed global layer set each fail, and replacing either with a choice fitted to the case removes the harm without losing the intended effect.
  - Two 2026 papers reach this from different halves of the same design space. On the direction: ablating the standard refusal direction from a steering vector recovers at most about 8 points of mean attack success rate and leaves worst-case ASR unchanged on two of three models, while a direction learned against the intervention's own objective brings mean ASR below the unsteered baseline in more than two-thirds of 108 attack-by-multiplier configurations -- and it turns out to be partially opposed to the behavioural effect, so removing it typically increases the steering rather than costing it. On the site: an in-sample global layer oracle produces 227 severe over-steer events and climbs from 12 to 249 right-to-wrong answer flips as depth grows, going net negative, while per-instance layer rules corrupt no answer at any depth and adaptively gated variants carry one severe event each. Both papers state the same summary in their own terms -- safety comes from selection, not from steering gently.

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Tampers with a model's own reasoning trace in two directions — toward an equivalent safe option and toward an unsafe one — and finds the models that follow their traces most faithfully are the ones that follow them into harm, with the two behaviours carried by two distinct, anti-correlated residual-stream directions that can be steered apart.
- [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](../../archive/papers/2026/arxiv-2608-03892/summary.md) — Trains a difference-of-means direction on short- versus long-horizon answer continuations and steers along it, shifting binary temporal choices, moving the monetary indifference threshold on an untrained task by a factor of 56 at a ten-year delay, and changing a planning benchmark — with matched-norm random controls and an unusually candid account of what the direction may actually encode.
- [ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance](../../archive/papers/2026/arxiv-2608-04524/summary.md) — Synthesizes Cognitive Behavioral Therapy dialogues using a CoT strategy grounded in CBT guidelines plus a resistance orchestrator that steers simulated patients away from sycophantic compliance.
- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) — Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.
- [Divergent Response Modes in Frontier Language Models Under Steering Pressure](../../archive/papers/2026/arxiv-2608-06578/summary.md) — Measures not how far six frontier models move under steering pressure but what kind of response they give when they decline, finds several response modes belonging to a single model, and then traces the largest within-model split to a linearly decodable and causally steerable direction in an open-weight model's residual stream.
- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) — Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Finding Usable Weight Mechanisms with Tiled SVD](../../archive/papers/2026/arxiv-2608-06969/summary.md) — Extracts interpretable units directly from a transformer's weight matrices by column-tiled SVD, so a unit's identity is the weight rule itself rather than an atom of a separately trained dictionary, and judges them with a pre-registered suite whose central move is refusing a metric that a trivial baseline would win.
- [When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs](../../archive/papers/2026/arxiv-2608-08159/summary.md) — Audits four neuroscience-inspired claims about language models across 17 checkpoints from five families and 0.6B to 72B, and shows that an apparent emergence of concept steerability with scale is produced entirely by uncalibrated measurement -- raw intervention units, the readout metric, and a fixed operating point -- with correcting any one of the three removing the trend.
- [Safety Cost of Steering Vectors Is Separable and Reducible](../../archive/papers/2026/arxiv-2608-08383/summary.md) — Shows that the part of a steering vector which breaks a model's refusal behaviour is a separate direction from the part that produces the intended behavioural effect, and learns that direction by constrained optimization so it can be ablated without losing the steering.
- [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](../../archive/papers/2026/arxiv-2608-08829/summary.md) — Shows that which layers a steering vector should be injected at is a property of the individual input rather than of the task, that a greedy per-input rule reaches the exhaustive optimum for structural reasons, and that a label-free predictor trained to imitate that rule recovers most of the oracle at deployment.
- [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-08976/summary.md) — Builds a Parkinson's screen from control data alone using a contrastive activation direction derived from synthetically degraded healthy speech and a nearest-neighbour anomaly score in face-encoder space, and gives a measurable precondition -- positive cosine between the synthetic and real disease directions -- that predicts in advance which modality the steering primitive will work on.
- [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](../../archive/papers/2026/arxiv-2608-09638/summary.md) — Turns the hidden-role game Avalon into a diagnostic instrument rather than an arena, decomposing theory of mind into a 2x2 taxonomy of perspective-constrained binary statements, and shows by probing, ground-truth injection and steering that models represent the right answer internally while failing to say it.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [Probing and steering biology across Boltz-1s trunk-diffusion boundary](../../archive/papers/2026/arxiv-2608-11475/summary.md) — Probes and steers across the trunk-to-diffusion boundary of an AlphaFold3-class structure predictor, finding that geometry survives the crossing while sequence chemistry is attenuated, and that a strand direction predictive at F1 0.82 steers nothing at all -- with an architectural explanation for why.
- [Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-502/summary.md) — A survey reorganizing mechanistic interpretability from observation into a Locate-Steer-Improve intervention pipeline, categorized by the interpretable object being acted on.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) — Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

### What a steering claim has to show, assembled from sixteen sources

No paper here states the checklist, but between them the sources have supplied
every item on it, usually by being the one that failed the check.

**A null direction.** The bar the careful sources meet is a magnitude-matched
random vector. *Risky Business* moves its two metrics by 9 and 7 points where
norm-matched random directions move either by at most 1.1; *Avalon-ToM-Bench*
reports random controls at about zero and negated ones negative. Without one,
a reported effect is a statement that something changed.

**A reversal.** *MI-MIDI* adds the cheapest test in the archive and the one most
often skipped: run every configuration in both orientations and split the two
fitted slopes into antisymmetric and symmetric parts. A direction should reverse
when reversed; drift need not. Their specificity score is the antisymmetric
share, and it catches layer-0 responses that shift the same way under both
orientations — which a fluency or output-volume guard would have accepted.

**A class-balance table, not just accuracy.** The sharpest control here is
*Avalon-ToM-Bench*'s, and it is a table rather than a number. Steering lifts
Qwen3-1.7B's output accuracy from 54 to 77, onto its probe ceiling — but the
result that makes this readable is that True-recall and False-recall move
**together**, from a degenerate 10.7/98.0 to a balanced 73.8/80.2. A
threshold shift toward one class would have produced the same accuracy gain.
Steering papers that report only accuracy cannot distinguish the two.

**A statement of where the direction came from, and what else varies with it.**
Every source that looks closely says the contrast pair is the method.
*MI-MIDI*: the poles vary lexically as well as musically, so a direction is only
as clean as its contrast. The intertemporal-steering paper says the same about
its own construct — short and long continuations also differ in abstraction,
urgency and strategic scope — and declines to claim it isolated a temporal
variable. See [[difference-in-means-direction]].

### The one source that predicts failure before measuring it

Everything above is post-hoc. The **label-free Parkinson's screen** is the only
entry that states in advance which of two modalities its steering primitive will
work on, and why. Its alignment principle says a direction built from a
*synthetic* degradation detects the real thing when the cosine between the
synthetic and real directions is positive. Measured: **+0.37** for the speech
encoder, where the detector reaches AUROC 0.765; **−0.48** for the face encoder,
where the corresponding direction scores at chance. Both predictions hold.

Making a negative prediction and then confirming the failure is rare enough to
be worth naming as a template. The mechanism is portable too: the face direction
points the wrong way not because the concept is absent but because the encoder
was trained for static emotion classification and puts its signal roughly
orthogonal to motion. What a mean-difference direction *means* is a property of
what the representation was trained to separate — which is the same reason the
contrast-pair caution above keeps recurring.

### Where to inject is part of the claim

Two sources arriving together make layer choice a finding rather than a
configuration detail, and they disagree in a way that resolves.

*Deployable Per-Instance Steering* shows the best layers are a property of the
**individual input**, not of the task, and that over-steering is dose-graded and
extremely concentrated — 97% of 942 severe events in a single trait-model cell,
median perplexity inflation 810 points. *MI-MIDI* shows all-layer injection is
stable in a cross-attention-conditioned model and accumulates disruptively in a
decoder-only one, with **fifty times** more symmetric drift than single-layer
injection. Its norm-relative control rules out the obvious explanation: single
-layer injection survives a 20% relative perturbation while all-layer injection
fails at 2%, so the problem is sixteen layers pushed *together*, not early
layers overdriven.

The resolution is that both are describing the same thing from different ends —
the accumulated effect of injecting at many sites is not the sum of injecting at
one, and neither the right site nor the right number is a constant.

### What is not established

Nothing here bounds how much of a behaviour a static-coefficient direction can
reach. The per-instance paper names an **unflippable ceiling** and attributes it
to the paradigm rather than to its selector, and *Avalon-ToM-Bench* — whose
steering lands exactly on its probe ceiling and no higher — is consistent with
the same limit from the other side. Both are single settings. Whether the
ceiling is the readout that supplies the sign, the linearity of the
intervention, or something about the behaviour is open, and no source here
separates them.

### At seventeen: a structural reason a good direction steers nothing

Everything above is about validating a steering claim after the fact. The
**Boltz-1 trunk/diffusion study** is the first entry that explains *where* the
gap comes from, and it does so from outside language modelling entirely.

Probing an AlphaFold3-class structure predictor, helix and coil directions steer
dose-dependently against a 19-direction matched-norm null, with model confidence
stable. A β-strand direction fitted the same way is **predictive at F1 0.82,
precision ≥ 0.93 — and moves strand content not at all**, converting helix into
coil instead.

The explanation is architectural and falsifiable: strand identity is a property
of residue *pairs*, held in a representation that information flows **out of but
not into**, so an intervention on the single representation cannot reach it. It
makes a prediction, which holds: the two *locally*-defined states (helix, coil)
are the pair sharing one antiparallel axis (cos = −0.69), not the two extended
ones.

The ablation is the part worth borrowing. Removing that direction from the
trunk, from the diffusion module, or from **both**, leaves strand content
unchanged. So on one direction in one model, the signal is *sufficient for
decodability and not necessary for generation* — sufficiency and necessity
coming apart on the same vector.

**What this changes for the checklist above.** The question "can an intervention
at this site write to the representation the property actually lives in?" is
answerable **in advance, from architecture**, rather than only after a null
result. Where the archive's other entries teach you to catch a bad steering
claim, this one lets you predict it. Their three closing rules are worth
adopting verbatim: name the readout class; restrict causal conclusions to the
site *and intervention family* tested; control for missing labels.

### At nineteen: the two controls the checklist was missing

Two entries arriving together supply what everything above was reaching for —
one shows how a steering *trend* can be manufactured, the other shows what a
properly controlled steering result looks like end to end.

**The measurement audit.** *When Is a Steerable Concept Representation Real?*
audits 17 models across five families, 0.6B–72B, and finds that an apparent
**emergence of steerability with scale** — a clean monotone curve — is produced
entirely by three uncalibrated choices: raw activation units, the readout
metric, and a fixed hand-picked operating point. Its factorial decomposition is
the part to internalise: **none of the four cells shows a significant slope**, so
correcting any *one* of the three removes the trend, and no single correction
can be credited with finding the artifact.

Three consequences for this note:

- A fixed raw coefficient is **not a fixed intervention**. The fraction of the
  residual it displaces varies *non-monotonically* across models.
- The normalised dose–response is an **inverted U**, so any single fixed strength
  sits on one side or the other of a model-specific peak.
- Every model selects a layer near **0.8 of depth** — never the two-thirds this
  literature commonly hand-picks.

Under the corrected protocol steering stays significant at every scale, from
0.6B to 72B. It neither emerges nor collapses. Note their discipline: they
refuse to call that scale-*invariance*, because the checkpoints are
independently trained runs and the interval still admits a moderate slope.

**The worked example.** *Divergent Response Modes* is the cleanest probe-and-
steer result here, and it adds a control the checklist above lacks entirely:

> **A prompt-only baseline.** Train the identical probe on a *small model that
> never produced these responses*. It reaches **0.72** balanced accuracy — the
> items being classified are by construction more ambiguous as prompts, and any
> competent model represents prompt ambiguity. The 70B model's 0.87 plateau is
> therefore worth about **14 points**, not 87.

Almost nothing in this archive reports that decomposition, and without it a high
held-out accuracy cannot separate *the model has decided* from *the input was
ambiguous*. Its steering half then does everything this note asks: strengths
sized against the median residual norm at the injection layer, layer chosen
mid-plateau so half the depth remains ahead of the intervention, direction
defined on 50 items and evaluated on the other 50, greedy decoding, and an
α = 0 control that lands within two points of the originally logged rate.

The dose–response is monotone across the whole sweep (0% → 40% at control →
86%). **And the cost is in the same table**: at the strongest suppression
**28/50 generations truncate**, against 0/50 at the strongest push the other
way. The effect reverses; the damage does not. A paper reporting only the
behavioural rate would have shown a clean bidirectional result with half its
suppressed outputs broken — which is exactly what [[MI-MIDI's]] symmetric/
antisymmetric decomposition exists to catch, arrived at here by simply printing
the second column.

<!-- analysis-sources: 19 -->
