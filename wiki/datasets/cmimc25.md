# CMIMC25

<!-- auto:begin -->

A 2025 competition-mathematics problem set, used in the archive purely as an evaluation benchmark for test-time-scaling methods; neither source describes the competition or the set's construction. The test-time-scaling framework paper includes it in a signal-rich competition-mathematics block of 186 problems drawn from AIME'26, HMMT Feb.'26, HMMT Nov.'25, CMIMC'25 and SMT'25, with traces recording the chosen token and up to 20 alternatives at each position. CLR reports it as the case where claim-level falsification pays off most clearly: GPT-OSS-20B reaches 82.19% against Cons@64's 77.50% while using 37.0% fewer tokens.

- **Kind**: dataset
- **Also called**: CMIMC 2025, CMIMC'25
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [BIG-Bench Hard](big-bench-hard.md), [HMMT 2025](hmmt-2025.md), [MMLU-PRO](mmlu-pro.md), [Pass@1](../concepts/pass-1.md), [Self-Certainty](../methods/self-certainty.md), [SuperGPQA](supergpqa.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — A framework paper that formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, splits it into three structural regimes (single-trajectory, leaf-level, prefix-level), replaces scalar repeated-sampling metrics with a discovery-stability profile that Pass@k and its relatives are coordinates of, specifies exact-replay versus distributional reproducibility, and releases 1,948,821 full reasoning traces with token-level alternatives and two verifier signals.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — CLR reallocates part of the test-time compute budget from generating more solution samples to falsifying a small set of decision-critical claims extracted from each trace, improving accuracy over self-consistency while using fewer tokens on some models.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
