# Reasoning Faithfulness

<!-- auto:begin -->

The gap between a model's stated chain of thought and the computation that produced its answer: unfaithful or post-hoc rationalization, reasoning that is latent rather than written, encoded or steganographic traces, and what a monitor reading the trace can and cannot catch. The question the archive answers is when a visible reasoning trace is evidence about the model, and when it is only text.

- **Slug**: `reasoning-faithfulness`
- **Papers**: 27
- **Seminars**: 0
- **Tracked keywords**: `chain of thought faithfulness`, `faithful reasoning`, `unfaithful`, `faithfulness of chain of thought`, `chain of thought monitoring`, `monitorability`, `encoded reasoning`, `steganography`, `latent reasoning`, `implicit reasoning`, `post-hoc rationalization`, `reasoning trace`, `introspection`, `sandbagging`

## Most recent papers

- [Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](../../archive/papers/2026/arxiv-2608-04735/summary.md) (2026-08-05)
  - The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
- [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](../../archive/papers/2026/arxiv-2608-04928/summary.md) (2026-08-05)
  - Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) (2026-08-04)
- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) (2026-08-04)
- [Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering](../../archive/papers/2026/arxiv-2608-04124/summary.md) (2026-08-04)
- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) (2026-08-03)
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
- [Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning](../../archive/papers/2025/local-2c3407071e27c9d6/summary.md) (2025-01-01)
  - Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) (2025-01-01)
  - Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.
- [A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning](../../archive/papers/2025/local-99a25b62fd9ad86c/summary.md) (2025-01-01)
  - Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](../../archive/papers/2025/local-fb100130d8c7c2bd/summary.md) (2025-01-01)
  - Shows that base models win pass@K on mathematics by producing wrong chains that land on right answers, and that scoring the chain too — CoT-Pass@K — reverses the verdict in RLVR's favour at every K.
- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](../../archive/papers/2024/local-6252abed1b134f57/summary.md) (2024-01-01)
  - Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
