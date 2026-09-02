# Llama-Guard-3 (ASR judge)

<!-- auto:begin -->

Llama-Guard-3 is used in this archive not as a subject model but as the automated Attack-Success-Rate (ASR) judge for LRM jailbreak evaluations. 'How Should We Enhance the Safety of Large Reasoning Models' measures ASR via LlamaGuard3 under None/PAP/PAIR jailbreak attacks against AdvBench queries. 'Conflicts Make Large Reasoning Models Vulnerable to Attacks' selects it as its ASR judge specifically for its strong correlation with human judgment and low false-positive rate, using it to score attack success across a taxonomy of eight internal-conflict/dilemma jailbreak types.

- **Kind**: model
- **Also called**: LlamaGuard3 (ASR judge)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [HarmBench](../datasets/harmbench.md), [JailbreakBench](../datasets/jailbreakbench.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [Qwen3-14B](qwen3-14b.md), [QwQ-32B](qwq-32b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [How Should We Enhance the Safety of Large Reasoning Models: An Empirical Study](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-936/summary.md) — An empirical study of safety fine-tuning for LRMs finds directly distilling safe responses from DeepSeek-R1 barely reduces jailbreak Attack Success Rate, identifies five risky reasoning patterns responsible (including overthinking and 'weak vacillation' -- hesitating over superficially benign jailbreak framing, which survives safety filtering and is the key residual driver of failures), shows explicitly targeting these patterns in the distillation prompt cuts PAIR ASR from 63% to 13%, and finds short or template-based safety reasoning matches long-form reasoning's safety performance -- unlike math/code, safety does not benefit from longer reasoning chains.
- [Conflicts Make Large Reasoning Models Vulnerable to Attacks](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-463/summary.md) — A single-turn, non-narrative jailbreak method that simply instructs an LRM to reason through an explicit internal conflict (e.g. Helpfulness vs. Harmlessness) or moral dilemma (e.g. a duress or sacrificial scenario) before answering a harmful query substantially raises attack success rates across three models and five safety benchmarks (e.g. QwQ-32B: direct-query ASR 0.04 to conflict-injected 0.523 on AdvBench) with no fine-tuning, multi-turn interaction, or gradient access, and layerwise/neuron-level analysis shows the conflict prompt causes safety-relevant and functional activation subspaces to shift and overlap specifically in middle-to-late layers, weakening safety alignment at the representational level.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
