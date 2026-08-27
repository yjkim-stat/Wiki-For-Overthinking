# Test-Time Adaptation

<!-- auto:begin -->

Test-time adaptation means adjusting a model's behaviour at inference on a specific input or distribution shift, without further gradient training on labelled data beforehand. The vision-language source proposes TTAug and TTAdapt, using input augmentation and consensus pseudolabels instead of external supervision to adapt small VLMs; TinyTTA instead makes test-time adaptation feasible on microcontrollers by adapting only early-exit heads in a self-ensemble rather than backpropagating through the whole network.

- **Kind**: concept
- **Also called**: Test-Time Adaptation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

## Appears in

- [Efficient Test-Time Scaling for Small Vision-Language Models](../../archive/papers/2026/title-9fd38a270d13bf45/summary.md) — Introduces Test-Time Augmentation (TTAug) and Test-Time Adaptation (TTAdapt), two test-time scaling methods designed for small vision-language models, giving consistent gains across nine benchmarks without additional tuning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
