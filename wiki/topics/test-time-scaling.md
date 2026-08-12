# Test-Time Scaling

<!-- auto:begin -->

What a model gains by thinking longer at inference: sampling and verification, search over reasoning steps, self-correction, and the length of the chain itself as a compute knob. The question the archive answers is how accuracy trades against tokens spent, and where that curve flattens.

- **Slug**: `test-time-scaling`
- **Papers**: 67
- **Seminars**: 0
- **Tracked keywords**: `chain of thought`, `chain of thought prompting`, `test-time compute`, `test-time scaling`, `inference-time scaling`, `inference-time compute`, `best of n`, `self-consistency`, `tree of thoughts`, `monte carlo tree search`, `self-refine`, `self-correction`, `self-verification`, `budget forcing`, `thinking budget`, `reasoning budget`, `extended thinking`, `overthinking`

## Most recent papers

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) (2026-08-06)
  - Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](../../archive/papers/2026/arxiv-2608-04735/summary.md) (2026-08-05)
  - The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
- [The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale](../../archive/papers/2026/arxiv-2608-04355/summary.md) (2026-08-05)
  - Decomposes measured self-correction gains into a content margin and format-recovery margins, and shows causally that most of what the field has reported as self-correction is answer-parseability repair.
- [ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance](../../archive/papers/2026/arxiv-2608-04524/summary.md) (2026-08-05)
  - Synthesizes Cognitive Behavioral Therapy dialogues using a CoT strategy grounded in CBT guidelines plus a resistance orchestrator that steers simulated patients away from sycophantic compliance.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) (2026-08-05)
  - Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.
- [Interpretable Adaptive Sampling for LLM Test-Time Scaling](../../archive/papers/2026/arxiv-2608-03961/summary.md) (2026-08-04)
- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) (2026-08-04)
- [Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates](../../archive/papers/2026/arxiv-2608-03284/summary.md) (2026-08-04)
- [The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics](../../archive/papers/2026/arxiv-2608-03291/summary.md) (2026-08-04)
- [Monte Carlo Tree Search for Table-to-Multimodal Report Generation](../../archive/papers/2026/arxiv-2608-04071/summary.md) (2026-08-04)
- [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](../../archive/papers/2026/arxiv-2608-02585/summary.md) (2026-08-03)
- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) (2026-08-03)
- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) (2026-08-03)
- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) (2026-08-02)
- [Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1766/summary.md) (2026-01-01)
  - Two-stage fine-tuning that first injects difficulty cues into output prefixes for prospective strategy selection, then injects redundancy cues mid-reasoning for retrospective correction.
- [Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-25/summary.md) (2026-01-01)
  - Prunes chain-of-thought segments the model's own likelihood landscape marks as extraneous, then trains on the resulting pruning preference pairs.
- [FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-662/summary.md) (2026-01-01)
  - A financial reasoning benchmark built from parameterized symbolic templates with executable Python, giving machine-verifiable step-level ground truth and contamination-free regeneration.
- [Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1149/summary.md) (2026-01-01)
  - Reformulates reasoning as a search over thinking strategies, showing sparse reasoning paths exist that are simultaneously more accurate and shorter than standard outputs.
- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) (2026-01-01)
  - Routes each generation step among a fast path, a perception re-examination path and a self-reflection path, trained on 790k samples of teacher-attributed perception-versus-reasoning failures.
- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) (2026-01-01)
  - Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) (2026-01-01)
  - Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.
- [Local Causal Attribution of Chain-of-Thought Reasoning](../../archive/papers/2026/local-6db01f05462cef8e/summary.md) (2026-01-01)
  - Fits a structural causal model over the units of a single chain-of-thought trace using leave-one-out interventions and linear regression, producing a pairwise influence matrix between every pair of steps at a cost linear in the number of units.
- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/local-80ef8b5ce7217f7c/summary.md) (2026-01-01)
  - Replaces uniform test-time compute allocation with a training-free agent that picks reasoning tools, a search strategy and an exploration parameter per problem, using a process reward model both to prune within a trajectory and to select across iterations.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) (2026-01-01)
  - Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) (2026-01-01)
  - Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
