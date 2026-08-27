# DeepSeek-R1

<!-- auto:begin -->

DeepSeek-R1 is one of the two models the archive's sources name, alongside OpenAI's o1, as opening the line of large reasoning models that produce long explicit chains of thought before answering, and it is the origin of the distilled Qwen and Llama checkpoints most of the archive's length-reduction work fine-tunes. It appears in three roles across the sources: as the historical reference for the paradigm whose cost is overthinking, as the parent of the distillations that stand in for it experimentally, and as a subject of measurement in its own right -- the Bloom's Taxonomy profiling reports it spending 32.9% of reasoning steps on Applying and 18.6% on Evaluating, the highest evaluative share among R1-family models profiled, with Creating at 0.2%. It also serves as one of three judge models in ChainPrune's reasoning-quality panel.

- **Kind**: model
- **Also called**: R1
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [AdaptThink](../methods/adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [AutoThink](../methods/autothink.md), [critical-path latency](../concepts/critical-path-latency.md), [DAPO](../methods/dapo.md), [DAST](../methods/dast.md), [DeepSeek-R1-Distill-Llama-8B](../methods/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [Dr. GRPO](../methods/dr-grpo.md), [GPT-5.5](gpt-5-5.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [knowledge distillation](../methods/knowledge-distillation.md), [LLM-as-a-Judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [mechanistic interpretability analysis](../methods/mechanistic-interpretability-analysis.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [Reasoning Step Segmentation](../methods/reasoning-step-segmentation.md), [Redundant Reasoning Steps](../concepts/redundant-reasoning-steps.md), [RLVR](../methods/rlvr.md), [routing collapse](../concepts/routing-collapse.md), [SimPO](../methods/simpo.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [Thinkless](../methods/thinkless.md)

## Appears in

- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/2026/arxiv-2608-20256/summary.md) — Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](../../archive/papers/2026/arxiv-2608-21860/summary.md) — ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.
- [Cognitive Profiling of LRMs' Reasoning Traces Using Bloom's Taxonomy](../../archive/papers/2026/arxiv-2608-23205/summary.md) — The paper segments LRM reasoning traces into cognitive steps with Llama-3.3-70B-Instruct, labels each step with one of Bloom's six levels, and uses the resulting level proportions and 6x6 transition matrix to profile seven reasoning models and to predict solution correctness.
- [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](../../archive/papers/2026/arxiv-2608-24658/summary.md) — Parason distinguishes two forms of parallel reasoning -- AND-branch Subtask Parallelism and OR-branch Trial Parallelism -- shows Trial Parallelism dominates on hard reasoning traces, and trains models to convert sequential CoT into grammar-structured parallel trajectories that a real inference engine executes for ~1.7x wall-clock speedup with competitive accuracy.
- [When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models](../../archive/papers/2026/title-c593d75efe2e5d8c/summary.md) — Studies how quantization, distillation and pruning affect DeepSeek-R1's reasoning ability using mechanistic interpretation, finding weight count matters more for knowledge memorization than reasoning, and that protecting just 2% of over-compressed weights recovers 6.57 accuracy points.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
