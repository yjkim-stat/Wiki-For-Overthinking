# linear probing

<!-- auto:begin -->

Training a small classifier on frozen internal activations to test whether a property is linearly represented. Both sources use it to establish that information exists internally before or without being verbalized — step correctness and logicality decodable from a step's sparse code at 78-86%, and answer-formation stage decodable well enough to drive early exit with detection rates above 90%. Both are careful about the inference it licenses: a probe shows information is present and linearly accessible, not that the model's own generation pathway uses it.

- **Kind**: method
- **Also called**: probe, probing
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AlpacaEval](../datasets/alpacaeval.md), [budget forcing](budget-forcing.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [commitment boundary](../concepts/commitment-boundary.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [early exit](early-exit.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](llm-as-a-judge.md), [MATH500](../datasets/math500.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [MMLU](../datasets/mmlu.md), [monitorability](../concepts/monitorability.md), [monosemanticity](../concepts/monosemanticity.md), [OlympiadBench](../datasets/olympiadbench.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [overthinking](../concepts/overthinking.md), [process supervision](../concepts/process-supervision.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen3-14B](../models/qwen3-14b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [residual stream](../concepts/residual-stream.md), [self-consistency](self-consistency.md), [self-verification](../concepts/self-verification.md), [sparse autoencoder](sparse-autoencoder.md), [state tracking](../concepts/state-tracking.md), [steering vector](steering-vector.md), [superposition](../concepts/superposition.md), [supervised finetuning](supervised-finetuning.md), [test-time compute](../concepts/test-time-compute.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) — Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
