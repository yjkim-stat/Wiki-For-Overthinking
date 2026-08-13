<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Towards Best Practices of Activation Patching in Language Models: Metrics and Methods

- **Authors**: Fred Zhang, Neel Nanda
- **Venue**: preprint
- **Published**: 2024-01-01
- **Source**: local
- **Topics**: reasoning-interpretability

## In one line

Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.

## Problem

Activation patching is the standard localization tool in mechanistic interpretability, but the literature contains many variants with no consensus on hyperparameters: each paper tends to use its own corruption method and its own evaluation metric. That leaves open the possibility that published interpretability results are artefacts of the settings adopted rather than facts about the model, and no systematic study of the technique's sensitivity existed.

## Contributions

- A controlled comparison of two corruption methods — Gaussian noising of key token embeddings versus symmetric token replacement with a semantically related token — across factual recall localization and IOI circuit discovery, showing they yield different localizations and different discovered circuits.
- Evidence that Gaussian noising pushes the model off distribution and breaks the internal mechanism being studied, rather than merely removing information, demonstrated by the disrupted attention patterns of Name Mover heads.
- A comparison of evaluation metrics showing that probability, being non-negative, structurally fails to detect negative model components when corruption drives the correct-token probability near zero, while logit difference does not have this failure mode.
- An analysis of sliding-window patching against summing single-layer effects, showing the window method systematically amplifies weak localization.
- Concrete practice recommendations: prefer symmetric token replacement, prefer logit difference, try single-layer patching first, and vary which tokens are corrupted.

## Method

Activation patching runs three passes: a clean run on a prompt with a known answer, caching activations of chosen components; a corrupted run on a modified prompt; and a patched run on the corrupted prompt with one component's activation restored from the clean cache. The patching effect is the gap between corrupted and patched performance, iterated over components to produce a localization map. Three degrees of freedom are varied. Corruption: Gaussian noising adds noise with three times the token-embedding standard deviation to key token embeddings, while symmetric token replacement swaps key tokens for semantically related ones of equal sequence length, so the corrupted prompt is still an in-distribution draw with its own well-defined answer. Metric: probability of the answer, logit difference between the clean and corrupted answers (normalized so 1 is fully restored and 0 is corrupted performance), or KL divergence from the clean output distribution. Granularity: patching one layer at a time versus restoring a window of adjacent MLP layers jointly, compared against simply summing the single-layer effects over the same window. Settings include factual recall in GPT-2 XL on a purpose-built PairedFacts set of 145 in-distribution prompt pairs, IOI circuit discovery in GPT-2 small averaged over 500 prompts with a head counted as detected when its effect is two standard deviations from the mean, plus greater-than, Python docstring completion and basic arithmetic tasks, and validation on GPT-J 6B.

## Results

Corruption method changes the answer. For factual recall MLP patching in GPT-2 XL, the clear peak around layer 16 under Gaussian noising is not salient at all under symmetric token replacement, and the GN peak is 2x-5x higher than STR across window sizes, regardless of metric. For IOI circuit discovery the two corruptions detect different head sets at every fixed metric: under probability, STR finds 1/3 Name Movers, 0/2 Duplicate Token, 3/4 S-Inhibition and 1/2 Negative Name Movers while GN finds 0/3, 1/2, 2/4 and 2/2. Gaussian noising also produces a detection in the wrong direction, flagging head 0.10 as harming performance when prior work establishes it helps. Evidence for the off-distribution explanation: on 500 clean IOI prompts Name Mover heads put 0.58 attention probability on the indirect object, and STR preserves that pattern with the roles swapped, while GN splits attention between IO and S1 (0.26 and 0.21); restoring S-Inhibition head values recovers the IO logit under STR (logit difference 1.04) but largely fails under GN (0.49). Metric choice also matters: probability concentrates effect on the last subject token far more than logit difference does (ratio of last-subject to middle-subject effects 4.33x versus 1.22x under STR, 1.74x versus 0.77x under GN). Probability overlooks Negative Name Mover head 11.10 under STR, because the corrupted run already assigns the IO only 0.03 probability, bounding any negative patching effect at -0.03 while the detection threshold sits at -0.027; with a stronger corruption replacing all three names, the IO probability falls to 5e-4 and probability detects neither Negative Name Mover, while logit difference still does. Sliding-window patching yields 1.40x, 1.75x and 1.59x the peak value of summed single-layer effects at window sizes 3, 5 and 10, and at least 20% more peak effect across all combinations, while single-layer patching alone shows only a weak peak at layer 15. Corrupting different tokens traces different information: corrupting S1 and IO recovers all three Name Mover heads, whereas corrupting S2 misses most of them.

## Limitations

The paper's own: experiments are on decoder-only language models up to 6B parameters, leaving other architectures and larger models to future work; only the denoising direction is tested, overriding corrupted activations with clean ones, not the reverse noising direction also used for circuit discovery; and the evidence that Gaussian noising induces off-distribution behaviour is described by the authors themselves as tentative. The paper is also explicit that it does not claim GN results are illusory — for some arithmetic tasks in GPT-J, STR shows the stronger concentration. A reader should note the practical consequence the paper acknowledges: even under the recommended settings, the recovered IOI circuit is far from complete, with critical misses such as Name Movers, so the recommendations improve reliability without making a single patching sweep sufficient. Detection is also defined by a two-standard-deviation threshold, which is itself a hyperparameter the sensitivity analysis does not vary.

## Entities

- **Concepts**: activation patching, causal tracing, causal mediation analysis, interchange intervention, [localization](../../../../wiki/concepts/localization.md), circuit analysis, out-of-distribution intervention, logit difference, negative model components, sliding window patching
- **Methods**: [activation patching](../../../../wiki/methods/activation-patching.md), Gaussian noising corruption, symmetric token replacement, sliding window patching, path patching, KL divergence metric, logit difference metric
- **Datasets**: PairedFacts, [Indirect Object Identification (IOI)](../../../../wiki/datasets/indirect-object-identification.md), greater-than task, Python docstring completion, basic arithmetic

Tags: `mechanistic interpretability`, `activation patching`, `circuits`, `methodology`, `reproducibility`, `evaluation metrics`

## Abstract

Mechanistic interpretability seeks to understand the internal mechanisms of machine learning models, where localization—identifying the important model components—is a key step. Activation patching, also known as causal tracing or interchange intervention, is a standard technique for this task (Vig et al., 2020), but the literature contains many variants with little consensus on the choice of hyperparameters or methodology. In this work, we systematically examine the impact of methodological details in activation patching, including evaluation metrics and corruption methods. In several settings of localization and circuit discovery in language models, we find that varying these hyperparameters could lead to disparate interpretability results. Backed by empirical observations, we give conceptual arguments for why certain metrics or methods may be preferred. Finally, we provide recommendations for the best practices of activation patching going forwards.

---

Record id: `local:956614b275995bc4`
