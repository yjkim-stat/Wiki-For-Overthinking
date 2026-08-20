# Reasoning Interpretability

<!-- auto:begin -->

What the computation behind reasoning looks like from the inside: circuits and the attention heads that carry them, features recovered by sparse dictionary learning, and the causal interventions used to establish that a component or a written state matters. The question the archive answers is which claims about a model's internal reasoning the available intervention methods can actually support, and at what granularity.

- **Slug**: `reasoning-interpretability`
- **Papers**: 53
- **Seminars**: 0
- **Tracked keywords**: `mechanistic interpretability`, `activation patching`, `causal mediation`, `causal tracing`, `causal analysis`, `circuit analysis`, `circuit discovery`, `reasoning circuit`, `attention head`, `sparse autoencoder`, `superposition`, `polysemantic`, `monosemantic`, `residual stream`, `activation steering`, `steering vector`, `linear probe`, `linear probing`, `internal representation`, `structural causal model`, `difference-in-means`, `representation editing`, `logit lens`, `interchange intervention`

## Most recent papers

- [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-11197/summary.md) (2026-08-11)
  - Takes the set of active sparse-autoencoder latents as the unit of analysis and finds that adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active, which contradicts the bag-of-features reading those sets are usually given.
- [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](../../archive/papers/2026/arxiv-2608-10835/summary.md) (2026-08-11)
  - Reads a frozen vision-language model's forward pass as a structured computational trace -- a graph over image patches, query tokens and generated tokens with attention as edges, processed by interleaved relational, spatial and sequential modules -- and shows that structuring the same internals prior detectors already read lifts hallucination detection from a 69-75 AUC plateau to 90.
- [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](../../archive/papers/2026/arxiv-2608-10430/summary.md) (2026-08-11)
  - Detects the class of hallucination where a model confidently fabricates a parameter the user never gave, by running a LoRA adapter alongside the frozen model that restructures the residual stream and then names the offending parameter in words the agent can act on.
- [Probing and steering biology across Boltz-1s trunk-diffusion boundary](../../archive/papers/2026/arxiv-2608-11475/summary.md) (2026-08-11)
  - Probes and steers across the trunk-to-diffusion boundary of an AlphaFold3-class structure predictor, finding that geometry survives the crossing while sequence chemistry is attenuated, and that a strand direction predictive at F1 0.82 steers nothing at all -- with an architectural explanation for why.
- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) (2026-08-10)
  - Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.
- [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-08976/summary.md) (2026-08-10)
  - Builds a Parkinson's screen from control data alone using a contrastive activation direction derived from synthetically degraded healthy speech and a nearest-neighbour anomaly score in face-encoder space, and gives a measurable precondition -- positive cosine between the synthetic and real disease directions -- that predicts in advance which modality the steering primitive will work on.
- [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](../../archive/papers/2026/arxiv-2608-09638/summary.md) (2026-08-10)
  - Turns the hidden-role game Avalon into a diagnostic instrument rather than an arena, decomposing theory of mind into a 2x2 taxonomy of perspective-constrained binary statements, and shows by probing, ground-truth injection and steering that models represent the right answer internally while failing to say it.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) (2026-08-10)
  - Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](../../archive/papers/2026/arxiv-2608-08829/summary.md) (2026-08-09)
  - Shows that which layers a steering vector should be injected at is a property of the individual input rather than of the task, that a greedy per-input rule reaches the exhaustive optimum for structural reasons, and that a label-free predictor trained to imitate that rule recovers most of the oracle at deployment.
- [Safety Cost of Steering Vectors Is Separable and Reducible](../../archive/papers/2026/arxiv-2608-08383/summary.md) (2026-08-09)
  - Shows that the part of a steering vector which breaks a model's refusal behaviour is a separate direction from the part that produces the intended behavioural effect, and learns that direction by constrained optimization so it can be ablated without losing the steering.
- [Reproducing and Stress-Testing Two Approaches to LLM Reasoning Reliability: Test-Time Probability Aggregation and Logic-Representation Editing](../../archive/papers/2026/arxiv-2608-08514/summary.md) (2026-08-09)
  - Independently reproduces two published reliability methods and stress-tests them across models and domains their authors never tried, finding one reproduces exactly but loses significance everywhere new, and the other rests on a decodable logic direction that a same-norm random direction matches exactly under steering.
- ["Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-07852/summary.md) (2026-08-08)
  - Decomposes three speaker settings -- the default Assistant, an assigned roleplay persona, and a narrated story character -- into sparse-autoencoder features at turn boundaries and pronoun tokens, and finds that roleplay personas retain an Assistant-associated feature core while differentiating from it across depth, where story characters never acquire that core at all.
- [Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-08168/summary.md) (2026-08-08)
  - Trains separate Top-K sparse autoencoders on a reasoning model's activations in thinking and non-thinking modes, and finds that suppressing the most active reasoning features destroys mathematical formatting as reliably as it destroys reasoning -- with the model responding by generating 454 percent more tokens of lower-diversity, more metacognitively marked text rather than stopping.
- [On the Robustness of LLMs' Internal Representation of Code Correctness](../../archive/papers/2026/arxiv-2608-08266/summary.md) (2026-08-08)
- [When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs](../../archive/papers/2026/arxiv-2608-08159/summary.md) (2026-08-08)
  - Audits four neuroscience-inspired claims about language models across 17 checkpoints from five families and 0.6B to 72B, and shows that an apparent emergence of concept steerability with scale is produced entirely by uncalibrated measurement -- raw intervention units, the readout metric, and a fixed operating point -- with correcting any one of the three removing the trend.
- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) (2026-08-08)
- [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](../../archive/papers/2026/arxiv-2608-07208/summary.md) (2026-08-07)
  - Compares linear probes against RFM-derived concept vectors for reading how much a sentence concerns a concept out of a frozen LLM's activations, on a human-annotated ESG benchmark, and finds the simpler probe consistently stronger.
- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) (2026-08-07)
- [Finding Usable Weight Mechanisms with Tiled SVD](../../archive/papers/2026/arxiv-2608-06969/summary.md) (2026-08-07)
  - Extracts interpretable units directly from a transformer's weight matrices by column-tiled SVD, so a unit's identity is the weight rule itself rather than an atom of a separately trained dictionary, and judges them with a pre-registered suite whose central move is refusing a metric that a trivial baseline would win.
- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) (2026-08-06)
  - Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.
- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) (2026-08-06)
  - Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](../../archive/papers/2026/arxiv-2608-06300/summary.md) (2026-08-06)
  - Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.
- [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](../../archive/papers/2026/arxiv-2608-05660/summary.md) (2026-08-06)
  - Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.
- [Divergent Response Modes in Frontier Language Models Under Steering Pressure](../../archive/papers/2026/arxiv-2608-06578/summary.md) (2026-08-06)
  - Measures not how far six frontier models move under steering pressure but what kind of response they give when they decline, finds several response modes belonging to a single model, and then traces the largest within-model split to a linearly decodable and causally steerable direction in an open-weight model's residual stream.
- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) (2026-08-04)
  - Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
