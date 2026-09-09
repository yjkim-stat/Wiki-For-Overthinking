# backdoor implantation

<!-- auto:begin -->

The step by which the Deadlock Attack's adversarially-optimized token embedding is installed into an open-weight large reasoning model so that it fires only on a specific trigger, rather than on ordinary inputs. The sources report the resulting backdoor forces the model into a perpetual chain-of-thought loop with a 100% attack success rate across four models and three benchmarks, while leaving benign-input accuracy essentially unchanged.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [adversarial embedding optimization](adversarial-embedding-optimization.md), [AIME 2024](../datasets/aime-2024.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Deadlock Attack](deadlock-attack.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md)

## Appears in

- [One Token Embedding Is Enough to Deadlock Your Large Reasoning Model](../../archive/papers/2025/local-398417af52a576de/summary.md) — Trains a single adversarial token embedding, implanted into an open-weight large reasoning model via a backdoor trigger, that hijacks the model's chain-of-thought into a perpetual reasoning loop, achieving a 100% attack success rate (forcing generation to the token limit) across four models and three benchmarks while leaving benign-input accuracy essentially unchanged.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
