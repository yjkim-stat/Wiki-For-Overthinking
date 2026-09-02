# ZebraLogic

<!-- auto:begin -->

ZebraLogic is a constraint-satisfaction logic-puzzle benchmark used to evaluate chain-of-thought compression and pruning methods, including a controlled re-evaluation of entropy-based CoT compression (finding it never beats random pruning against a properly-tuned random baseline), STOP (a learnable [STOP] token pruning futile parallel reasoning paths), and SELECT2REASON (selecting a high-utility SFT subset by difficulty and trace length).

- **Kind**: dataset
- **Also called**: ZebraLogic
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [AMC23](amc23.md), [BrUMO'25](brumo-25.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [difficulty estimation](../concepts/difficulty-estimation.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-4o](../models/gpt-4o.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [HMMT25](hmmt25.md), [KAOYAN](kaoyan.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B-Instruct](../models/llama-3-2-1b-instruct.md), [LLaMA 3.2 3B Instruct](../models/llama-3-2-3b-instruct.md), [MATH500](math500.md), [OlympiadBench](olympiadbench.md), [OpenR1-Math-220k](openr1-math-220k.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-Math-7B-Instruct](../models/qwen2-5-math-7b-instruct.md), [QwQ-32B](../models/qwq-32b.md), [QwQ-32B-Preview](../models/qwq-32b-preview.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md)

## Appears in

- [Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models](../../archive/papers/2026/arxiv-2607-28707/summary.md) — A controlled re-evaluation of entropy-based chain-of-thought compression showing that low- and high-entropy selection never beats random pruning once a random baseline is included, and that the one apparent exception on math benchmarks is caused by numeric tokens rather than by entropy.
- [Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-876/summary.md) — STOP (Super TOken for Pruning) is a lightweight, LoRA-based module that reads a frozen LRM's cached KV states via a single learnable [STOP] token to score and prune futile parallel-reasoning paths early -- at negligible inference overhead (0.59% latency) -- and is shown, via a proposed four-way taxonomy of path-pruning signal generators, to dominate external-signal and non-learnable internal-signal baselines in both accuracy and compute across model scales 1.5B-20B.
- [Select2Reason: Efficient Instruction-Tuning Data Selection for Long-CoT Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-331/summary.md) — SELECT2REASON selects the top 10% of a large long-CoT instruction pool for SFT by jointly ranking questions on a learned difficulty score and (deduplicated) reasoning-trace length, matching or beating models trained on 8-94x more data.
- [THOUGHTTERMINATOR: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models](../../archive/papers/2025/local-eff598a06b1089db/summary.md) — The paper defines model-relative measures of overthinking (local/global overthinking scores) built from observed token-spend distributions, introduces the DUMB500 easy-question dataset to probe overthinking on trivial inputs, and proposes THOUGHTTERMINATOR, a training-free decoding-time technique that interrupts a reasoning model with token-budget reminders and forces an answer at a difficulty-calibrated deadline.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
