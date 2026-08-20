# Test-Time Scaling

<!-- auto:begin -->

What a model gains by thinking longer at inference: sampling and verification, search over reasoning steps, self-correction, and the length of the chain itself as a compute knob. The question the archive answers is how accuracy trades against tokens spent, and where that curve flattens.

- **Slug**: `test-time-scaling`
- **Papers**: 90
- **Seminars**: 0
- **Tracked keywords**: `chain of thought`, `chain of thought prompting`, `test-time compute`, `test-time scaling`, `inference-time scaling`, `inference-time compute`, `best of n`, `self-consistency`, `tree of thoughts`, `monte carlo tree search`, `self-refine`, `self-correction`, `self-verification`, `budget forcing`, `thinking budget`, `reasoning budget`, `extended thinking`, `overthinking`

## Most recent papers

- [Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs](../../archive/papers/2026/arxiv-2608-11573/summary.md) (2026-08-12)
- [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](../../archive/papers/2026/arxiv-2608-11716/summary.md) (2026-08-12)
- [Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction](../../archive/papers/2026/arxiv-2608-11772/summary.md) (2026-08-12)
- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) (2026-08-12)
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) (2026-08-12)
  - Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.
- [SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward](../../archive/papers/2026/arxiv-2608-12220/summary.md) (2026-08-12)
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) (2026-08-11)
  - Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.
- [When Self-Consistency Backfires: Majority Vote Hurts the Majority of Hard Science Problems for Small LLMs](../../archive/papers/2026/arxiv-2608-11403/summary.md) (2026-08-11)
- [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](../../archive/papers/2026/arxiv-2608-11420/summary.md) (2026-08-11)
- [FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation](../../archive/papers/2026/arxiv-2608-10916/summary.md) (2026-08-11)
- [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](../../archive/papers/2026/arxiv-2608-10976/summary.md) (2026-08-11)
- [Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute](../../archive/papers/2026/arxiv-2608-09351/summary.md) (2026-08-10)
  - Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.
- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) (2026-08-10)
- [Adaptive Sequential Test Planning for Multi-Mechanism Reliability Qualification via Bayesian Monte Carlo Tree Search](../../archive/papers/2026/arxiv-2608-09622/summary.md) (2026-08-10)
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) (2026-08-10)
- [Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy](../../archive/papers/2026/arxiv-2608-09857/summary.md) (2026-08-10)
  - Puts an ensemble of LLM judges between a robot-autonomy planner and its execution layer as gating middleware that accepts, rejects or escalates each plan to human review, and reports that ensemble size barely moves accuracy while the errors concentrate at the escalate boundary rather than between accept and reject.
- [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](../../archive/papers/2026/arxiv-2608-08503/summary.md) (2026-08-09)
- [Efficient Test-Time Scaling for LLM-based Time Series Forecasting](../../archive/papers/2026/arxiv-2608-08675/summary.md) (2026-08-09)
- [PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary](../../archive/papers/2026/arxiv-2608-08830/summary.md) (2026-08-09)
- [Persistent Semantic Entities in Tool-Augmented LLM Systems](../../archive/papers/2026/arxiv-2608-07952/summary.md) (2026-08-08)
  - Formalises implicit agent state that survives session boundaries as Persistent Semantic Entities defined by name binding, event triggering and propagation, and measures across 24 models that whether injected contamination decays depends on what kind of contamination it is rather than on model scale or deployment.
- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) (2026-08-08)
- [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](../../archive/papers/2026/arxiv-2608-07424/summary.md) (2026-08-07)
- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) (2026-08-06)
  - Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](../../archive/papers/2026/arxiv-2608-04735/summary.md) (2026-08-05)
  - The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
- [The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale](../../archive/papers/2026/arxiv-2608-04355/summary.md) (2026-08-05)
  - Decomposes measured self-correction gains into a content margin and format-recovery margins, and shows causally that most of what the field has reported as self-correction is answer-parseability repair.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
