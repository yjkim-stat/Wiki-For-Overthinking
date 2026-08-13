# GPT-5.5

<!-- auto:begin -->

A frontier proprietary model, used in both sources as apparatus rather than as a subject — and in both, apparatus whose judgement carries a load the paper's conclusions rest on. One has it classify 100 sampled search trajectories into a four-quadrant scheme, which is the main evidence that its two credit signals are complementary rather than redundant, with no human validation of those labels. The other has it independently validate evidence sufficiency and logical consistency of automatically generated training supervision, retaining only verified samples — so the quality of the entire training corpus is set by it. Worth recording as a pattern the archive should track: a frontier model doing the verifying is part of the experimental setup and is rarely audited as such.

- **Kind**: model
- **Also called**: GPT-5.5
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [abstention](../concepts/abstention.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [counterfactual intervention](../methods/counterfactual-intervention.md), [credit assignment](../concepts/credit-assignment.md), [E5-base-v2](e5-base-v2.md), [Gemini-1.5-Pro](gemini-1-5-pro.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [GiGPO](../methods/gigpo.md), [GPT-4o](gpt-4o.md), [grounding](../concepts/grounding.md), [GRPO](../methods/grpo.md), [HotpotQA](../datasets/hotpotqa.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [process reward](../concepts/process-reward.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-8B](qwen3-8b.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward sparsity](../concepts/reward-sparsity.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [traceability](../concepts/traceability.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](../../archive/papers/2026/arxiv-2608-03292/summary.md) — Recasts long-document visual question answering as building an explicit evidence graph whose nodes are grounded document blocks and whose edges are reasoning dependencies, and verifies the graph causally — masking the evidence it cites flips 82.8% of correct answers while masking uncited evidence changes 9.6%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
