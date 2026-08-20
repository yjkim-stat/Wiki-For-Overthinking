<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination

- **Authors**: Zichuan Wang, Songlin Yang, Bo Peng, Zhenchen Tang, Yang Li, Beibei Dong, Jing Dong
- **Venue**: cs.CV
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07302>
- **PDF**: <https://arxiv.org/pdf/2608.07302v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

Refutes the standard account of vision-language hallucination -- that the model attends too little to the image -- by showing real and hallucinated objects draw equally strong attention, then uses a logit lens over the attended regions to separate two causally distinct hallucination types and treat each differently.

## Problem

Vision-language models generate objects absent from the image, and the prevailing explanation is insufficient visual attention: either textual priors dominate the multimodal interaction and suppress visual focus, or improper processing leaves salient regions under-attended. A large body of mitigation follows from that premise, amplifying or redistributing attention or injecting extra visual guidance. The paper's experiments say the explanation is incomplete, because attention magnitude does not distinguish the failure from the success.

## Contributions

- A refutation of the insufficient-attention account of object hallucination, showing real and hallucinated object tokens receive comparable visual attention in the layers where visual attention peaks, which undercuts the premise behind a family of attention-amplification mitigations.
- The reframing from how much the model attends to what the attended region contains, operationalised by decoding high-attention visual features through a logit lens and checking whether they support the generated token.
- A causal discriminator between two hallucination types that is an intervention rather than a score: mask the attended region and regenerate, classifying by whether the token survives.
- Two matched remedies -- removing unreliable visual evidence for the type that masking fixes, and injecting decoded visual semantics into the decoding logits for the type that survives masking -- so the treatment follows the diagnosis.
- A detection result improving F1 from 0.68 to 0.79 over the strongest prior method, with a diagnosis of why prior methods underperform: they pool signals across layers where attention is not image-dominant, and they measure attention quantity rather than evidential support.

## Method

Attention strength associated with object tokens is quantified across depth, establishing that visual attention peaks in what the authors call the image-attention stage in the mid-to-late layers -- and that real and hallucinated object tokens exhibit similar magnitudes and similar focus there. The question therefore shifts from how much the model attends to what it attends to, which is answered by decoding the visual features of the highest-attention regions through a logit lens and asking whether those regions decode to the object token that was generated. That yields a detection rule -- a consistency check between the attended visual evidence and the produced token -- and, more usefully, a causal discriminator between two hallucination types. The discriminator is an intervention rather than a score: mask the high-attention region and regenerate, and classify by whether the token survives. If the hallucinated token disappears, the cause was visual uncertainty, meaning the attended region was semantically similar or confusable and removing it removes the error. If the token persists while attention drifts elsewhere, the cause was a contextual prior strong enough to produce the object regardless of what the image supplies. Each type then gets a matched remedy: masking the unreliable high-attention region for the first, and for the second injecting the visual semantics decoded from the attended region directly into the decoding logits, weighted against the model's own distribution under masking, so that correct visual evidence is amplified against the prior rather than the region being removed. The whole framework is training-free.

## Results

The premise result is that attention magnitude carries no signal about correctness: real and hallucinated object tokens receive comparable attention in the mid-to-late layers where visual attention peaks, shown both qualitatively on heatmaps and quantitatively with means and standard deviations over a benchmark subset. What does separate them is what the attended region decodes to -- regions corresponding to real objects decode to the target token under a logit lens, and regions attended for hallucinated objects do not. On detection this yields 0.7932 F1 against 0.6842 for the strongest prior method and 0.6182 for a confidence-based baseline, with precision and recall both above 0.78 where the baselines sit between 0.59 and 0.72. The authors attribute prior methods' weaker performance to two things they can now name: those methods aggregate signals across layers including ones where attention is not image-dominant, which dilutes the signal, and they measure quantity of attention rather than whether the attended evidence supports the generation. The two-type decomposition is the contribution that the detection number alone understates, since it is what makes the mitigation targeted -- masking works for the uncertainty type and is useless for the prior type by construction, since the prior type is defined as the one that survives masking, and the evidence-injection remedy addresses that residual case. Mitigation results are reported on standard hallucination benchmarks across multiple backbones.

## Limitations

No limitations section. What a reader should notice: the two-type taxonomy is defined by the response to the intervention rather than validated against an independent account of the cause, so 'visual uncertainty' and 'contextual prior' are labels for two behaviours under masking rather than mechanisms established separately -- the masking test is simultaneously the classifier and the evidence for the classification. The detection rule depends on a semantic-similarity threshold between the decoded region and the generated token, and on identifying the highest-attention region, neither of which is swept in what is reported here. The evidence-injection remedy has a mixing weight controlling how much visual semantics displaces the model's own distribution, with the trade between hallucination reduction and content preservation not quantified in the main results. And the framework requires a logit lens to decode intermediate visual features into the output vocabulary, which the archive's other material shows is itself a readout whose fidelity varies with depth -- so a region that fails to decode may be a region whose content is not yet expressed in the unembedding basis rather than a region that lacks the object.

## Why it matters here

- **reasoning-interpretability**: The premise result is the part that generalises: attention magnitude does not distinguish a grounded generation from a hallucinated one, because real and hallucinated object tokens draw comparable attention in exactly the layers where visual attention peaks. That undercuts a whole family of methods built on amplifying or redistributing attention, and it is the visual analogue of a caution the archive already holds from the reasoning side, where attending to the right region is not the same as using it -- a perturbation score that provably depends on the image and still buys nothing at the selection layer. Here the same gap is measured directly, and the replacement is the right one: decode what the attended region contains rather than counting how much it is attended to. The causal discriminator is the more transferable idea. Two failures that look identical in the output are separated by an intervention -- mask the attended region and regenerate -- and the classification is which of them survives. That is a cheap and honest way to split a failure mode into kinds, and it earns its keep immediately, since the two kinds require opposite treatments and a single remedy applied to both would help one and be inert on the other by construction. The archive should note the shape: where a mitigation works on some cases and not others, masking-and-regenerating is a candidate way to find out which is which. Two things to hold lightly. The taxonomy is defined by the response to the intervention rather than validated against an independent account, so the masking test is both the classifier and the evidence for it. And the detection rule rests on a logit lens decoding intermediate visual features into the output vocabulary, which this archive's own material establishes is a readout whose fidelity is strongly depth-dependent -- so a region that fails to decode may hold the object in a basis the unembedding cannot yet read, which is precisely the confound the tuned lens was invented to expose.

## Entities

- **Concepts**: [hallucination](../../../../wiki/concepts/hallucination.md), logit lens, attention, [grounding](../../../../wiki/concepts/grounding.md), causal intervention, [detection versus control](../../../../wiki/concepts/detection-versus-control.md), layer selection, co-occurrence prior
- **Methods**: [logit lens](../../../../wiki/methods/logit-lens.md), [attention analysis](../../../../wiki/methods/attention-analysis.md), [activation patching](../../../../wiki/methods/activation-patching.md), masking intervention, [contrastive decoding](../../../../wiki/methods/contrastive-decoding.md), [training-free intervention](../../../../wiki/methods/training-free-intervention.md)
- **Datasets**: [COCO](../../../../wiki/datasets/coco.md), [CHAIR](../../../../wiki/datasets/chair.md), AMBER

Tags: `vision-language`, `hallucination`, `logit-lens`, `attention`, `training-free`, `causal-taxonomy`

## Abstract

Large Vision-Language Models (LVLMs) often suffer from object hallucination, generating objects that are absent from the image. Prior work largely attributes this to insufficient visual attention. However, we find that both real and hallucinated objects receive equally strong visual attention in the model's mid-to-late layers, suggesting that the key issue may not be how much the model attends, but what it attends to and why. To this end, we decode the visual features of high-attention regions using Logit Lens, and observe that regions corresponding to real objects can be correctly decoded to the target object tokens, whereas those for hallucinated objects cannot. Building on this, we identify two hallucination mechanisms: (i) visual uncertainty, triggered by semantically similar or confusable regions; masking these regions eliminates the hallucination. (ii) contextual prior, triggered by strong co-occurrence priors; even when the initially attended region is masked, the hallucination persists and attention drifts to other regions. Based on these findings, we propose a simple yet effective training-free Detect-Mitigate framework comprising a Logit-Lens Consistency Check to detect hallucination and targeted remedies: High-Attention Regions Masking (HARM) for visual uncertainty hallucination, and Visual Evidence Enhanced Decoding (VEED) for contextual prior hallucination. Our approach achieves state-of-the-art results on multiple hallucination benchmarks. Code will be available.

---

Record id: `arxiv:2608.07302`
