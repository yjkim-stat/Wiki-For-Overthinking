# GPT-4.1

<!-- auto:begin -->

A frontier model appearing in this archive as a judge rather than as a subject. It is the official evaluator for one open-ended medical benchmark, which means a result on that benchmark is a result about agreement with this model under that benchmark's rubric; and it is one of the strong systems evaluated on traceable long-document visual question answering, where the finding is about evidence grounding rather than about the model. Neither source describes the model. The reason to keep the entry is the dependency it marks: several reported gains in the archive are mediated by this specific judge at a pinned snapshot, and the archive holds separate evidence that judges disagree substantially on the class that determines the score.

- **Kind**: model
- **Also called**: GPT-4.1, gpt-4.1-2025-04-14
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [abstention](../concepts/abstention.md), [annotation agreement](../concepts/annotation-agreement.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [consensus](../concepts/consensus.md), [counterfactual intervention](../methods/counterfactual-intervention.md), [DPO](../methods/dpo.md), [Gemini-1.5-Pro](gemini-1-5-pro.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](gpt-4o.md), [GPT-5.5](gpt-5-5.md), [GPT-5-mini](gpt-5-mini.md), [grounding](../concepts/grounding.md), [GRPO](../methods/grpo.md), [human evaluation](../methods/human-evaluation.md), [IFEval](../datasets/ifeval.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [position bias](../concepts/position-bias.md), [process reward](../concepts/process-reward.md), [PubMedQA](../datasets/pubmedqa.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [traceability](../concepts/traceability.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](../../archive/papers/2026/arxiv-2608-03292/summary.md) — Recasts long-document visual question answering as building an explicit evidence graph whose nodes are grounded document blocks and whose edges are reasoning dependencies, and verifies the graph causally — masking the evidence it cites flips 82.8% of correct answers while masking uncited evidence changes 9.6%.
- [ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering](../../archive/papers/2026/arxiv-2608-10996/summary.md) — Trains open-ended medical question answering by scoring each response against rubric criteria that three frontier models independently agreed on, grading each criterion as correct, missing or wrong rather than yes/no, and recovering a gradient in groups where every response ties by judging the responses pairwise in both orders.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
