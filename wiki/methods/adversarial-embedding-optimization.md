# adversarial embedding optimization

<!-- auto:begin -->

The technique behind the Deadlock Attack: an adversarial token embedding is trained by gradient optimization, rather than written as text, so that once implanted into an open-weight large reasoning model via a backdoor trigger it hijacks the model's chain-of-thought into a perpetual reasoning loop. The sources describe it as achieving a 100% attack success rate (forcing generation to the token limit) across four models and three benchmarks, while leaving accuracy on benign inputs essentially unchanged.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2024](../datasets/aime-2024.md), [backdoor implantation](backdoor-implantation.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Deadlock Attack](deadlock-attack.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md)

## Appears in

- [One Token Embedding Is Enough to Deadlock Your Large Reasoning Model](../../archive/papers/2025/local-398417af52a576de/summary.md) — Trains a single adversarial token embedding, implanted into an open-weight large reasoning model via a backdoor trigger, that hijacks the model's chain-of-thought into a perpetual reasoning loop, achieving a 100% attack success rate (forcing generation to the token limit) across four models and three benchmarks while leaving benign-input accuracy essentially unchanged.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
