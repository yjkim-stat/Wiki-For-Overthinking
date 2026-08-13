# Reasoning Faithfulness

<!-- auto:begin -->

The gap between a model's stated chain of thought and the computation that produced its answer: unfaithful or post-hoc rationalization, reasoning that is latent rather than written, encoded or steganographic traces, and what a monitor reading the trace can and cannot catch. The question the archive answers is when a visible reasoning trace is evidence about the model, and when it is only text.

- **Slug**: `reasoning-faithfulness`
- **Papers**: 32
- **Seminars**: 0
- **Tracked keywords**: `chain of thought faithfulness`, `faithful reasoning`, `unfaithful`, `faithfulness of chain of thought`, `chain of thought monitoring`, `monitorability`, `encoded reasoning`, `steganography`, `latent reasoning`, `implicit reasoning`, `post-hoc rationalization`, `reasoning trace`, `introspection`, `sandbagging`

## Most recent papers

- [INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators](../../archive/papers/2026/arxiv-2608-10492/summary.md) (2026-08-11)
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) (2026-08-11)
  - Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) (2026-08-10)
- [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](../../archive/papers/2026/arxiv-2608-09888/summary.md) (2026-08-10)
- [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](../../archive/papers/2026/arxiv-2608-08113/summary.md) (2026-08-08)
  - Bolts a small trainable recurrent block between a frozen 1.1B language model's body and its output head, so reasoning happens as repeated refinement of two latent vectors rather than as generated tokens.
- [Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](../../archive/papers/2026/arxiv-2608-04735/summary.md) (2026-08-05)
  - The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
- [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](../../archive/papers/2026/arxiv-2608-04928/summary.md) (2026-08-05)
  - Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) (2026-08-04)
  - Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) (2026-08-04)
  - Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- [Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering](../../archive/papers/2026/arxiv-2608-04124/summary.md) (2026-08-04)
  - Splits a video model's latent computation into perception latents that always ground the question in visual evidence and reasoning latents allocated only when the question needs inference, and shows that reasoning latents without rationale supervision are worse than no reasoning latents at all.
- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) (2026-08-03)
  - Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning](../../archive/papers/2026/arxiv-2608-01593/summary.md) (2026-08-03)
  - Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
- [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](../../archive/papers/2026/arxiv-2608-02585/summary.md) (2026-08-03)
  - Inserts optimizable latent states at an intermediate Transformer layer rather than at the output, so self-attention makes every continuation token's log-probability differentiable with respect to every latent and reward-weighted gradients reach them from the whole continuation instead of only through their own decoded token.
- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) (2026-08-03)
  - Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [Reasoning Traces Shape Outputs but Models Won&apos;t Say So](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1986/summary.md) (2026-01-01)
  - Injects synthetic reasoning into a model's trace, shows the injection changes the answer, then shows the model refuses to admit it and fabricates an unrelated explanation instead.
- [SeLaR: Selective Latent Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-320/summary.md) (2026-01-01)
  - Switches to soft-embedding latent reasoning only at low-confidence steps, keeping discrete decoding elsewhere, and pushes the soft embeddings away from the top token to stop them collapsing.
- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) (2026-01-01)
  - Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) (2026-01-01)
  - Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.
- [Local Causal Attribution of Chain-of-Thought Reasoning](../../archive/papers/2026/local-6db01f05462cef8e/summary.md) (2026-01-01)
  - Fits a structural causal model over the units of a single chain-of-thought trace using leave-one-out interventions and linear regression, producing a pairwise influence matrix between every pair of steps at a cost linear in the number of units.
- [Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty](../../archive/papers/2026/local-99019f66bdc27581/summary.md) (2026-01-01)
  - Separates reasoning into procedural advancement and 'epistemic verbalization' — the token-level externalization of uncertainty — and shows that emitting doubt is what lets a model recover from silent divergence, that injecting a bare doubt cue recovers failed trajectories, and that 800 SFT examples suffice to install or destroy the habit.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) (2026-01-01)
  - Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) (2026-01-01)
  - Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.
- [Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!](../../archive/papers/2026/local-e62f069bc5144f28/summary.md) (2026-01-01)
  - A position paper arguing that reading a reasoning model's intermediate tokens as 'reasoning' or 'thinking' is unsupported by the available evidence and actively harmful, and collating experiments in which trace semantics and solution accuracy come apart.
- [Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity](../../archive/papers/2025/local-2f98d1e607e7b1dd/summary.md) (2025-01-01)
  - Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.
- [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](../../archive/papers/2025/local-26fdb25b9d157d04/summary.md) (2025-01-01)
  - Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
