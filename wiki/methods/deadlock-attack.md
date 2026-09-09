# Deadlock Attack

<!-- auto:begin -->

An attack, not a mitigation: a single adversarial token embedding is trained and implanted into an open-weight large reasoning model via a backdoor trigger so that the model's chain-of-thought is hijacked into a perpetual reasoning loop, forcing generation to the token limit. The sources report a 100% attack success rate across four models and three benchmarks, with benign-input accuracy essentially unchanged, and this is the only entry in the archive that aims overthinking as a weapon rather than treating it as a cost to be reduced.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [adversarial embedding optimization](adversarial-embedding-optimization.md), [AIME 2024](../datasets/aime-2024.md), [backdoor implantation](backdoor-implantation.md), [CommonsenseQA](../datasets/commonsenseqa.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md)

## Appears in

- [One Token Embedding Is Enough to Deadlock Your Large Reasoning Model](../../archive/papers/2025/local-398417af52a576de/summary.md) — Trains a single adversarial token embedding, implanted into an open-weight large reasoning model via a backdoor trigger, that hijacks the model's chain-of-thought into a perpetual reasoning loop, achieving a 100% attack success rate (forcing generation to the token limit) across four models and three benchmarks while leaving benign-input accuracy essentially unchanged.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
