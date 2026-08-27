# Llama-3.1-8B

<!-- auto:begin -->

An open-weight instruction-tuned model used across sources as an evaluation subject for cross-lingual test-time-scaling fairness (showing a significant accuracy drop and 180-300% extra reasoning cost when queried in a non-default measurement system), as the backbone for SHAD's reasoning/boilerplate token-disentanglement fine-tuning method, and as one of five model families used to demonstrate the latent capacity for concise reasoning that self-training (FS-BoN) elicits.

- **Kind**: model
- **Also called**: LLaMA3.1-8B, Llama 3.1 8B, Llama-3.1-8B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [GSM8K](../datasets/gsm8k.md), [Llama-3.2-1B](llama-3-2-1b.md), [Llama-3-8B](llama-3-8b.md), [Qwen2.5 7B](qwen2-5-7b.md)

## Appears in

- [On Generalization across Measurement Systems: LLMs Entail More Test-Time Compute for Underrepresented Cultures](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1032/summary.md) — LLMs default to Western measurement systems (USD, kilometers, kilograms) reflecting their training-data culture, suffer significant accuracy drops when queried in a non-default system (currency, length, or weight), and while chain-of-thought/sequential reasoning stabilizes large models' accuracy back toward the default level, it increases test-time compute by 180-300% -- disproportionately burdening users whose cultural context is not the default.
- [Disentangling Reasoning Tokens and Boilerplate Tokens For Language Model Fine-tuning](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1078/summary.md) — SHAD automatically separates a training sample's tokens into 'reasoning' (sample-specific, hard to predict) versus 'boilerplate' (repetitive, format/template) tokens by fine-tuning on a small shuffled-input-output subset and comparing per-token loss before/after, and the resulting Reasoning-highlighted Fine-Tuning (RFT) -- which adaptively up-weights reasoning tokens during agent SFT -- outperforms SFT, regex-based weighting, and two other token-differentiation baselines on held-in and held-out agent benchmarks.
- [Self-Training Elicits Concise Reasoning in Large Language Models](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1289/summary.md) — Shows current LLMs already possess a latent capacity for concise reasoning -- shorter correct paths exist within their own stochastic output distribution -- and that self-training (fine-tuning on the model's own best-of-N and few-shot-conditioned concise samples, FS-BoN) reliably elicits this capacity, cutting output length 30% on average across five model families on GSM8K/MATH with preserved accuracy, far outperforming zero-shot 'be concise' prompting and training on externally-sourced concise data.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
