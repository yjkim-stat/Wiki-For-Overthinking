# Qwen2.5-Coder-7B

<!-- auto:begin -->

A 7-billion-parameter code-specialised Qwen model, and in this archive the site of one of the sharpest causal results about written reasoning states. In the scratchpad-register study, a variant trained to maintain a running state has its next phase bit follow an edited internal representation on 80 percent of held-out Q8 examples and 91 percent of D8 while the printed text is held fixed, with pretrained and final-answer-only controls staying near baseline and same-rank random or orthogonal-complement patches giving about 0.02 agreement -- so the model demonstrably reads what it wrote, at least on this synthetic task. It also appears at several sizes in the Persistent Semantic Entities panel, where the smallest variant sits at the low end of the contamination range and the paper's factual-self-correction finding fails on both coder variants, which is why that paper declines to generalise it.

- **Kind**: model
- **Also called**: Qwen2.5-Coder-7B, Qwen2.5-coder-7B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [advantage estimation](../concepts/advantage-estimation.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-Sonnet-4](claude-sonnet-4.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-V3.2](deepseek-v3-2.md), [factorial ablation](../methods/factorial-ablation.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [GiGPO](../methods/gigpo.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [GPT-5.5](gpt-5-5.md), [gpt-oss-120b](gpt-oss-120b.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](../methods/grpo.md), [HumanEval+](../datasets/humaneval.md), [Kimi-K2.6](kimi-k2-6.md), [KV cache](../concepts/kv-cache.md), [linear probe](../methods/linear-probe.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.3-70B](llama-3-3-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MBPP+](../datasets/mbpp.md), [Mistral-7B-v0.3](mistral-7b-v0-3.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [outcome reward](../concepts/outcome-reward.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [process supervision](../concepts/process-supervision.md), [prompt injection](../concepts/prompt-injection.md), [Qwen3-32B](qwen3-32b.md), [Qwen3.5-4B](qwen3-5-4b.md), [Qwen3.6-27B](qwen3-6-27b.md), [Qwen3-VL-235B](qwen3-vl-235b.md), [ReAct](../methods/react.md), [rejection sampling](../methods/rejection-sampling.md), [representation editing](../methods/representation-editing.md), [residual stream](../concepts/residual-stream.md), [selectivity control](../methods/selectivity-control.md), [self-verification](../concepts/self-verification.md), [Skywork-OR1](skywork-or1.md), [state tracking](../concepts/state-tracking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [verifiable reward](../concepts/verifiable-reward.md), [Wilson confidence interval](../methods/wilson-confidence-interval.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](../../archive/papers/2026/arxiv-2608-07147/summary.md) — Assigns credit in coding-agent RL by splitting each code diff into sub-diffs, matching semantically similar sub-diffs across rollouts to form advantage groups, and projecting the resulting diff-level advantage back onto the tokens that produced it.
- [Persistent Semantic Entities in Tool-Augmented LLM Systems](../../archive/papers/2026/arxiv-2608-07952/summary.md) — Formalises implicit agent state that survives session boundaries as Persistent Semantic Entities defined by name binding, event triggering and propagation, and measures across 24 models that whether injected contamination decays depends on what kind of contamination it is rather than on model scale or deployment.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
