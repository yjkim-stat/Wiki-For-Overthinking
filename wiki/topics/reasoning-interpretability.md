# Reasoning Interpretability

<!-- auto:begin -->

What the computation behind reasoning looks like from the inside: circuits and the attention heads that carry them, features recovered by sparse dictionary learning, and the causal interventions used to establish that a component or a written state matters. The question the archive answers is which claims about a model's internal reasoning the available intervention methods can actually support, and at what granularity.

- **Slug**: `reasoning-interpretability`
- **Papers**: 52
- **Seminars**: 0
- **Tracked keywords**: `mechanistic interpretability`, `activation patching`, `causal mediation`, `causal tracing`, `causal analysis`, `circuit analysis`, `circuit discovery`, `reasoning circuit`, `attention head`, `sparse autoencoder`, `superposition`, `polysemantic`, `monosemantic`, `residual stream`, `activation steering`, `steering vector`, `linear probe`, `linear probing`, `internal representation`, `structural causal model`, `difference-in-means`, `representation editing`, `logit lens`, `interchange intervention`

## Most recent papers

- [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-11197/summary.md) (2026-08-11)
- [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](../../archive/papers/2026/arxiv-2608-10835/summary.md) (2026-08-11)
- [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](../../archive/papers/2026/arxiv-2608-10430/summary.md) (2026-08-11)
- [Probing and steering biology across Boltz-1s trunk-diffusion boundary](../../archive/papers/2026/arxiv-2608-11475/summary.md) (2026-08-11)
- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) (2026-08-10)
- [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-08976/summary.md) (2026-08-10)
- [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](../../archive/papers/2026/arxiv-2608-09638/summary.md) (2026-08-10)
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) (2026-08-10)
- [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](../../archive/papers/2026/arxiv-2608-08829/summary.md) (2026-08-09)
- [Safety Cost of Steering Vectors Is Separable and Reducible](../../archive/papers/2026/arxiv-2608-08383/summary.md) (2026-08-09)
  - Shows that the part of a steering vector which breaks a model's refusal behaviour is a separate direction from the part that produces the intended behavioural effect, and learns that direction by constrained optimization so it can be ablated without losing the steering.
- [Reproducing and Stress-Testing Two Approaches to LLM Reasoning Reliability: Test-Time Probability Aggregation and Logic-Representation Editing](../../archive/papers/2026/arxiv-2608-08514/summary.md) (2026-08-09)
- ["Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-07852/summary.md) (2026-08-08)
- [Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-08168/summary.md) (2026-08-08)
- [On the Robustness of LLMs' Internal Representation of Code Correctness](../../archive/papers/2026/arxiv-2608-08266/summary.md) (2026-08-08)
- [When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs](../../archive/papers/2026/arxiv-2608-08159/summary.md) (2026-08-08)
- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) (2026-08-08)
- [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](../../archive/papers/2026/arxiv-2608-07208/summary.md) (2026-08-07)
- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) (2026-08-07)
- [Finding Usable Weight Mechanisms with Tiled SVD](../../archive/papers/2026/arxiv-2608-06969/summary.md) (2026-08-07)
- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) (2026-08-06)
  - Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.
- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) (2026-08-06)
- [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](../../archive/papers/2026/arxiv-2608-06300/summary.md) (2026-08-06)
  - Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.
- [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](../../archive/papers/2026/arxiv-2608-05660/summary.md) (2026-08-06)
  - Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.
- [Divergent Response Modes in Frontier Language Models Under Steering Pressure](../../archive/papers/2026/arxiv-2608-06578/summary.md) (2026-08-06)
- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) (2026-08-04)
  - Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
