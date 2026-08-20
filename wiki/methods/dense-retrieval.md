# dense retrieval

<!-- auto:begin -->

Encoding queries and documents into one vector space and retrieving by cosine nearest neighbour. Both sources use it inside a reasoning loop rather than before one, and both make the query the interesting part: one retrieves complete solved problems mid-trace using the model's elicited intermediate answer as the query, on the argument that the raw reasoning text is too exploratory and noisy to search with; the other conditions a teacher on retrieved supporting evidence and uses the teacher-student gap as a training signal. Neither validates its encoder, and one of them cites work showing structurally faithful retrieval over mathematics is hard with off-the-shelf encoders while using one.

- **Kind**: method
- **Also called**: dense retrieval, nearest-neighbour retrieval
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [AIME 2025](../datasets/aime-2025.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [Bamboogle](../datasets/bamboogle.md), [benchmark design](../concepts/benchmark-design.md), [budget forcing](budget-forcing.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [credit assignment](../concepts/credit-assignment.md), [decontamination](decontamination.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [E5-base-v2](../models/e5-base-v2.md), [GiGPO](gigpo.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [in-context learning](../concepts/in-context-learning.md), [knowledge distillation](knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](llm-as-a-judge.md), [MATH500](../datasets/math500.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [predictive entropy](../concepts/predictive-entropy.md), [privileged information](../concepts/privileged-information.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3.5-2B](../models/qwen3-5-2b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning drift](../concepts/reasoning-drift.md), [reranking](reranking.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward shaping](../concepts/reward-shaping.md), [SciQ](../datasets/sciq.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](search-r1.md), [self-reflection](self-reflection.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [test-time scaling](../concepts/test-time-scaling.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) — Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
