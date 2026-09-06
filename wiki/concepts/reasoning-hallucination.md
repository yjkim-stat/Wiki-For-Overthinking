# reasoning hallucination

<!-- auto:begin -->

Reasoning Hallucination is a failure mode where a large reasoning model produces logically coherent but factually flawed reasoning chains leading to convincing wrong answers, distinct from typical hallucination because the errors are embedded in an otherwise-structured reasoning trace. RFS-Guard detects and localizes it training-free via a Routing Focus Score measuring cross-step attention concentration, while a separate paper introduces the Reasoning Score (logit divergence from late-layer vocabulary projections) to detect it and pairs this with GRPO-R, an RL method with step-level deep-reasoning rewards to reduce it.

- **Kind**: concept
- **Also called**: Reasoning Hallucination
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [2WikiMultihopQA](../datasets/2wikimultihopqa.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Bamboogle](../datasets/bamboogle.md), [Deepseek-R1-1.5B](../models/deepseek-r1-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [HotpotQA](../datasets/hotpotqa.md), [MATH500](../datasets/math500.md), [minervamath](../datasets/minervamath.md), [MuSiQue](../datasets/musique.md), [OpenR1-Math-220k](../datasets/openr1-math-220k.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [routing collapse](routing-collapse.md)

## Appears in

- [RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-885/summary.md) — RFS-Guard detects and localizes reasoning hallucinations in LRMs training-free, using a Routing Focus Score (RFS) that measures how strongly cross-step attention between reasoning and answer phases collapses toward semantic-neighbor proximity (rather than task-critical evidence) -- finding this 'routing collapse' is a strong hallucination signal that beats sampling-based, uncertainty-based, and other self-aware baselines while remaining far more inference-efficient.
- [Detection and Mitigation of Hallucination in Large Reasoning Models: A Mechanistic Perspective](../../archive/papers/2025/local-54dd9729250c51ac/summary.md) — Defines a Reasoning Score from the Jensen-Shannon divergence between LogitLens-projected late-layer and final-layer vocabulary distributions to distinguish deep reasoning from shallow pattern-matching, uses it to identify hallucination patterns (early-step fluctuation, incorrect backtracking, and a perplexity-correlated 'spurious verification' overthinking pattern) and build a post-hoc detector (RHD), and separately shapes an RL training reward from the same score (GRPO-R) to reduce reasoning hallucinations.
- [Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models](../../archive/papers/2026/title-c5959780286b4ea6/summary.md) — Introduces the Reasoning Score, a metric based on divergence between logits from late-layer projections onto the vocabulary space, to detect 'Reasoning Hallucination' -- logically coherent but factually wrong reasoning chains -- and pairs it with GRPO-R, an RL method using step-level deep-reasoning rewards to reduce it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
