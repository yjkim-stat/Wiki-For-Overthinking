# GPT-5

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [BrowseComp](../datasets/browsecomp.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [DeepScaleR-1.5B-Preview](deepscaler-1-5b-preview.md), [DeepScaler (training)](../datasets/deepscaler-training.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPT-4o](gpt-4o.md), [GPT-5 mini](gpt-5-mini.md), [gpt-o3](gpt-o3.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [o3-mini](o3-mini.md), [OlympiadBench](../datasets/olympiadbench.md), [QwQ-32B](qwq-32b.md), [s1-32B](s1-32b.md)

## Appears in

- [PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1253/summary.md) — PaCoRe (Parallel Coordinated Reasoning) decouples test-time compute scaling from a fixed context window by running rounds of massively parallel reasoning trajectories, compacting each trajectory's conclusion into a short message, and RL-training the model to synthesize (not just vote on) these messages into better subsequent exploration -- letting an 8B model reach 94.5% on HMMT 2025 by scaling effective test-time compute to ~2 million tokens, surpassing GPT-5's 93.2%.
- [Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1878/summary.md) — MathIF is a 420-query, 15-constraint controlled benchmark showing that as large reasoning models' chain-of-thought grows longer via reasoning-oriented SFT/RL, their instruction-following obedience degrades -- even the best open model (Qwen3-14B) satisfies only 50.71% of constraints strictly, and artificially lengthening CoT (budget forcing) or reasoning-oriented training both directly and measurably erode compliance, exposing a persistent intelligence-obedience trade-off.
- [Programming over Thinking: Efficient and Robust Multi-Constraint Planning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2028/summary.md) — SCOPE replaces long natural-language reasoning chains for multi-constraint planning with a two-stage, multi-agent pipeline that infers a query's combination/constraint structure once and compiles it into reusable, deterministic solver functions (Combination/Filter/Deliver), reaching 93.1% success on TravelPlanner with GPT-4o (a 61.6-point gain over CoT) while cutting inference cost 1.4x and time 4.67x versus the best baseline.
- [FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-288/summary.md) — FS-Researcher is a dual-agent (Context Builder / Report Writer) deep-research framework that scales test-time compute beyond a single context window by persisting evidence and task state in an external file-system workspace instead of the model's context, achieving state-of-the-art report quality on two open-ended benchmarks and outperforming official agent harnesses on an answer-verifiable search benchmark.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
