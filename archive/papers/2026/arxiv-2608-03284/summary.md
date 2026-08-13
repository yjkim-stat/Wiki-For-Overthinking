<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates

- **Authors**: Jinya Sakurai, Shueicheng Yan, Xun Xu
- **Venue**: cs.CV
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03284>
- **PDF**: <https://arxiv.org/pdf/2608.03284v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.50

## In one line

Triggers a safety intervention in image diffusion from the intermediate clean-image estimate rather than from the prompt, and spends optimization only from the first timestep where a violation actually appears — so extra test-time compute is incurred on unsafe inputs and benign latency stays flat as the budget grows.

## Problem

Weight-editing defenses for text-to-image models are expensive to redo as policies change and degrade general generation through cross-concept interference. Test-time defenses avoid both by leaving weights alone, but nearly all of them are prompt-centric: they decide whether and how to intervene from text tokens or conditioning embeddings, which can be misaligned with what is visually forming and so weakens the suppression-versus-preservation trade-off under adversarial prompting. Diffusion sampling meanwhile exposes an unused signal — at every step the model predicts a clean image that already encodes coarse structure and emerging semantics — which is direct evidence of what is being generated and is rarely used to trigger safety intervention.

## Contributions

- Using the intermediate clean-image estimate as the trigger, so intervention is decided by visual evidence rather than by the text that requested it
- Adaptive unrolling: rather than intervening on a fixed schedule, the sampler advances while monitoring and intervenes at the first timestep where a violation is detected, so how far the trajectory is explored is set by when the evidence appears
- A structured low-rank residual on the conditioning embedding instead of an unconstrained update, on the argument that the full degrees of freedom overfit specific noise patterns and produce artifacts
- A sparse hinge objective whose gradient is identically zero for any prohibited concept below the margin, creating a safe zone so the optimizer ignores irrelevant concepts when many are prohibited at once
- A test-time compute budget with an explicit knob, reported as a safety-versus-latency curve rather than a single operating point

## Method

At each denoising step the velocity prediction is solved for the clean-image estimate, which is embedded by a vision-language encoder and compared by cosine similarity against a library of prohibited concept embeddings. A hinge loss fires only where similarity exceeds a margin, so concepts safely below it contribute no gradient. When the loss first becomes positive, that timestep is taken as the intervention point and a small number of gradient steps updates a rank-R factorized residual added to the text conditioning, with the latent detached so gradients flow only to the residual factors. Sampling then restarts from the same initial noise with the refined conditioning, and the detect-optimize-restart loop repeats for at most K rounds — the pair of round count and per-round steps being the compute budget. Backbones are Stable Diffusion v1.4 and v3.5-medium, evaluated on nudity removal against five red-teaming prompt sets with an external nudity detector, on suppression of ten intellectual-property characters and five artistic styles by paired erase and preserve metrics including a strict binary vision-language judge, and on general capability by FID and CLIP score against COCO-30k.

## Results

On the older backbone the high-budget setting reduces nudity detection to 0.032, 0.054, 0.101, 0.069 and 0.049 across the five red-teaming sets from an undefended 0.097 to 0.728, while holding COCO FID at 12.92 and CLIP at 25.25 against the base model's 25.93. The comparison that matters is against a training-required baseline which reaches lower detection on four adversarial sets but at FID and CLIP of 44.56 and 23.59 — so weight editing buys suppression by damaging general generation, and the weight-preserving route does not. The strongest prior test-time defense reaches 0.096 to 0.646 detection at FID 42.80. On the newer backbone the pattern holds (0.026 to 0.062 detection at FID 6.03), with one honest exception: a guidance baseline attains the best FID at 3.91 while suppressing far less. The test-time-scaling behaviour is the paper's most transferable result. Increasing the budget yields consistent safety gains with FID relatively stable, and median latency on unsafe prompts rises from 1.91 to 7.06 seconds across the sweep while median latency on benign COCO prompts stays at roughly 1.8 to 1.9 seconds regardless of the maximum budget allowed — the cost is conditional on detection, not on the budget. Two ablations support the design choices rather than just reporting them: low-rank optimization consistently beats the unconstrained update on the safety-fidelity trade-off, and adaptive triggering consistently beats fixed intervention timesteps. The multi-concept study is where the method visibly strains — adding nudity, characters and styles together raises COCO FID from 12.8 to 27.2, which the authors attribute to competing constraints shrinking the safe region until the conditioning residual is pushed into low-density parts of the manifold.

## Limitations

The paper states them: the method inherits whatever ambiguity its vision-language safety encoder has, and it updates the conditioning from the safety signal at the detected timestep without directly optimizing preservation of the original prompt or the quality of the final image — so it can under-suppress indirect attacks, or over-suppress benign attributes and reduce semantic fidelity when the update is stronger. A reader should add that the multi-concept degradation is measured and not solved, and that safety is evaluated by an automatic detector and a model judge rather than by human review, so the reported detection rates inherit those instruments' errors. Two backbones, both from one family, and no seeds or variance are reported.

## Why it matters here

- **test-time-scaling**: It demonstrates a shape of test-time scaling this archive has not yet recorded: **conditional** rather than uniform. Every scaling result here so far spends the extra budget on every input — more samples, more reasoning tokens, a longer trace — and pays the latency everywhere. Here the trigger is evidence that a problem is forming, so unsafe inputs consume up to 7.06 seconds while benign ones stay at 1.8 to 1.9 regardless of the ceiling. That is the property an archive tracking adaptive allocation should want, and it is achieved without a difficulty predictor: the criterion is a threshold on an observable produced by the generation itself, which is exactly the ingredient the archive's adaptive-allocation results have found unreliable when it comes from a separate process-reward estimate. The ablation showing adaptive triggering beats fixed intervention timesteps is the controlled version of that claim. The domain is diffusion rather than language and the trigger — an intermediate clean-image estimate — has no direct textual analogue, so what transfers is the design principle, not the mechanism.

## Entities

- **Concepts**: test-time scaling, [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), concept erasure, [safety alignment](../../../../wiki/concepts/safety-alignment.md), [adversarial robustness](../../../../wiki/concepts/adversarial-robustness.md), low-rank adaptation, margin loss, conditional computation, [jailbreak](../../../../wiki/concepts/jailbreak.md)
- **Methods**: T2S2, low-rank adaptation, truncated backpropagation, safe latent diffusion, SAFREE, classifier-free guidance, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md)
- **Datasets**: I2P, P4D, Ring-a-Bell, MMA-Diffusion, UnlearnDiffAtk, COCO-30k

Tags: `test-time scaling`, `diffusion`, `safety`, `concept erasure`, `adaptive computation`

## Abstract

Ensuring safety and policy compliance in text-to-image diffusion models remains a critical challenge, as benign or adversarial prompts can often elicit prohibited content, e.g. nudity and protected intellectual property. While training-based unlearning methods are effective, they are computationally expensive and prone to catastrophic interference with general capabilities. Conversely, existing test-time defenses are primarily prompt-centric, relying on modifying textual descriptions only, and overlook the visual signals for detection. In this paper, we propose to leverage the intermediate clean image estimated during the generation process and employ a sparse margin objective to detect prohibited concepts. When a violation is detected, we immediately intervene by optimizing a structured low-rank residual in the text-conditioning space via truncated backpropagation. This design allows weight-preserving detection, keeps non-violating inference latency nearly unchanged as the maximum budget increases, and offers flexibility in safety performance via test-time scaling. Extensive experiments on Stable Diffusion v1.4 and v3.5 across nudity removal, IP protection, and style erasure demonstrate superior performance across suppression, fidelity and preservation compared to prior weight-preserving baselines, providing a scalable and flexible solution for safe generative deployment.

---

Record id: `arxiv:2608.03284`
