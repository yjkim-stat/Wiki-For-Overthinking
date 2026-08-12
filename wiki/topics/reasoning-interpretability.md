# Reasoning Interpretability

<!-- auto:begin -->

What the computation behind reasoning looks like from the inside: circuits and the attention heads that carry them, features recovered by sparse dictionary learning, and the causal interventions used to establish that a component or a written state matters. The question the archive answers is which claims about a model's internal reasoning the available intervention methods can actually support, and at what granularity.

- **Slug**: `reasoning-interpretability`
- **Papers**: 31
- **Seminars**: 0
- **Tracked keywords**: `mechanistic interpretability`, `activation patching`, `causal mediation`, `causal tracing`, `causal analysis`, `circuit analysis`, `circuit discovery`, `reasoning circuit`, `attention head`, `sparse autoencoder`, `superposition`, `polysemantic`, `monosemantic`, `residual stream`, `activation steering`, `steering vector`, `linear probe`, `linear probing`, `internal representation`, `structural causal model`, `difference-in-means`, `representation editing`, `logit lens`, `interchange intervention`

## Most recent papers

- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) (2026-08-06)
  - Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.
- [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](../../archive/papers/2026/arxiv-2608-06300/summary.md) (2026-08-06)
  - Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.
- [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](../../archive/papers/2026/arxiv-2608-05660/summary.md) (2026-08-06)
  - Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.
- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) (2026-08-04)
- [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](../../archive/papers/2026/arxiv-2608-03629/summary.md) (2026-08-04)
- [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](../../archive/papers/2026/arxiv-2608-03892/summary.md) (2026-08-04)
- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) (2026-08-03)
- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) (2026-08-03)
- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) (2026-08-03)
- [Mechanistic Interpretability Should Prioritize Feature Consistency in Sparse Autoencoders](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-99/summary.md) (2026-01-01)
  - Argues run-to-run feature consistency should be a standard SAE evaluation axis alongside reconstruction and sparsity, and gives a metric showing high consistency is achievable.
- [Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2073/summary.md) (2026-01-01)
  - Reads reasoning validity from layer-to-layer displacement of hidden states rather than from the states themselves, on the grounds that static activations let probes latch onto lexical surface patterns.
- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) (2026-01-01)
  - An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.
- [Multi-component Causal Tracing in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-154/summary.md) (2026-01-01)
  - Generalizes causal tracing from one component or layer at a time to selecting subsets of components jointly, by relaxing the combinatorial search into a continuous one over soft interventions.
- [Make Mechanistic Interpretability Auditable: A Call to Develop Guidelines via Continuous Collaborative Reviewing](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-159/summary.md) (2026-01-01)
  - A position paper arguing mechanistic interpretability cannot be used in safety-critical settings until its findings are auditable, and proposing continuous collaborative reviewing plus source-based claim tracking.
- [Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1265/summary.md) (2026-01-01)
  - Traces how individual prompt tokens ground into image regions during diffusion denoising, using fixed-seed single-word removal for causal faithfulness and a head-resolved spike score for attribution.
- [Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2031/summary.md) (2026-01-01)
  - Explains LLM counting failures as a depth limit, since counting is computed across layers, and fixes it with a System-2 decomposition whose mechanism is then traced.
- [Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-502/summary.md) (2026-01-01)
  - A survey reorganizing mechanistic interpretability from observation into a Locate-Steer-Improve intervention pipeline, categorized by the interpretable object being acted on.
- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) (2026-01-01)
  - Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [A Sharper Picture of Generalization in Transformers](../../archive/papers/2026/local-03f1eff4f1d40725/summary.md) (2026-01-01)
  - Derives a non-vacuous PAC-Bayes generalization bound for transformers on boolean functions in terms of Fourier sparsity and degree, and uses it to show chain of thought turns an exponential dependence on reasoning length into a linear one for Parity.
- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) (2026-01-01)
  - Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability](../../archive/papers/2026/local-85a70e78b4a93190/summary.md) (2026-01-01)
  - TRACED scores a reasoning chain by the geometry of its hidden-state trajectory -- net displacement as progress and curvature as stability -- and uses the two as features for a Gaussian classifier that separates correct from incorrect chains without reading the text.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) (2026-01-01)
  - Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.
- [Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!](../../archive/papers/2026/local-e62f069bc5144f28/summary.md) (2026-01-01)
  - A position paper arguing that reading a reasoning model's intermediate tokens as 'reasoning' or 'thinking' is unsupported by the available evidence and actively harmful, and collating experiments in which trace semantics and solution accuracy come apart.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) (2026-01-01)
  - Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) (2026-01-01)
  - Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
