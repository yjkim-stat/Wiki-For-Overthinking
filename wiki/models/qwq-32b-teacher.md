# QwQ-32B (teacher)

<!-- auto:begin -->

QwQ-32B is used as a teacher model for reasoning-trace distillation across sources, including Learning to Refine (defining the Refinement Gap to isolate parallel self-refinement's genuine value), fs1 (grounding distilled reasoning traces in knowledge-graph paths), and When Internalization Fails (testing whether ICoT-style curriculum internalization scales from simple to long, diverse competition-math traces).

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1 (teacher)](deepseek-r1-teacher.md), [GrailQA](../datasets/grailqa.md), [majority voting (baseline)](../methods/majority-voting-baseline.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [SimpleQA](../datasets/simpleqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [WebQSP](../datasets/webqsp.md)

## Appears in

- [Learning to Refine: Self-Refinement of Parallel Reasoning in LLMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1291/summary.md) — Defines the Refinement Gap (self-refinement accuracy minus majority-voting accuracy) to isolate parallel self-refinement's genuine value beyond simple candidate aggregation, finds it scales with model size but only weakly with base capability, and trains this capability into a 7B student (GSR) via a hybrid direct-solving-plus-refinement objective that explicitly retains all-candidates-incorrect training cases -- achieving 73.6% average accuracy across five math benchmarks (a +3.1-point Refinement Gap versus a much larger QwQ-32B teacher's +1.15) and recovering correct answers 5.9% of the time even when every sampled candidate is wrong.
- [Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-561/summary.md) — fs1 fine-tunes LLMs on reasoning traces grounded in knowledge-graph paths (rather than raw distilled reasoning traces), improving factual accuracy on complex multi-hop QA by 6-14 pass@16 points while also producing shorter reasoning traces than the ungrounded baseline.
- [When Internalization Fails: Finding Better Targets for Reasoning Compression](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-734/summary.md) — In a teacher-student distillation setup on competition-level math (NuminaMath 1.5, ~5000-token traces), ICoT-style curriculum internalization methods that work on simple/structured tasks (GSM8K, multiplication) provide little to no benefit over direct distillation; naive first-k-token truncation at inference time is also shown misleading, since models compensate by generating longer post-think text, undermining apparent token savings; distilling on the teacher's naturally-occurring post-think section (concise, answer-directed text generated after </think> but before the boxed answer) achieves the best accuracy-efficiency trade-off among all tested shortened targets, including generic teacher-generated summaries at matched token budgets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
