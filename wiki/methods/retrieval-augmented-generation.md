# retrieval-augmented generation

<!-- auto:begin -->

Conditioning generation on retrieved documents so that answers are grounded in supplied evidence rather than in parameters. The two sources use the term for different things, which is worth noting because the archive holds only these two. One treats RAG as the deployment setting needing a guardrail, training a 4B model to classify document-claim pairs as grounded or hallucinated in closed-book document-grounded settings. The other uses retrieval as a contrast case in a mechanistic study of how transformers come to reason implicitly over stored facts. Grounding on retrieved text does not guarantee the answer follows from it, which is the gap the first source addresses.

- **Kind**: method
- **Also called**: RAG, retrieval augmentation
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [abstention](../concepts/abstention.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [causal analysis](causal-analysis.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [circuit analysis](circuit-analysis.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [counterfactual intervention](counterfactual-intervention.md), [credit assignment](../concepts/credit-assignment.md), [E5-base-v2](../models/e5-base-v2.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [GiGPO](gigpo.md), [GPT-4o](../models/gpt-4o.md), [GPT-5.5](../models/gpt-5-5.md), [grounding](../concepts/grounding.md), [GRPO](grpo.md), [hallucination](../concepts/hallucination.md), [HotpotQA](../datasets/hotpotqa.md), [implicit reasoning](../concepts/implicit-reasoning.md), [LLM-as-a-judge](llm-as-a-judge.md), [memorization](../concepts/memorization.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](ppo.md), [process reward](../concepts/process-reward.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning distillation](reasoning-distillation.md), [reward sparsity](../concepts/reward-sparsity.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](search-r1.md), [supervised fine-tuning](supervised-fine-tuning.md), [synthetic data generation](synthetic-data-generation.md), [traceability](../concepts/traceability.md), [TriviaQA](../datasets/triviaqa.md), [verification](../concepts/verification.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](../../archive/papers/2026/arxiv-2608-03292/summary.md) — Recasts long-document visual question answering as building an explicit evidence graph whose nodes are grounded document blocks and whose edges are reasoning dependencies, and verifies the graph causally — masking the evidence it cites flips 82.8% of correct answers while masking uncited evidence changes 9.6%.
- [HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-835/summary.md) — A 4B small reasoning model that classifies document-claim pairs as grounded or hallucinated for RAG pipelines and produces evidence-grounded justifications.
- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](../../archive/papers/2024/local-6252abed1b134f57/summary.md) — Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
