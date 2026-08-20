<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs

- **Authors**: Hamed Damirchi, Ignacio Meza De la Jara, Damith Ranasinghe, Yuhang Liu, Javen Shi
- **Venue**: cs.LG
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.05660>
- **PDF**: <https://arxiv.org/pdf/2608.05660v1>
- **Topics**: reasoning-evaluation, reasoning-interpretability
- **Relevance score**: reasoning-evaluation 0.40, reasoning-interpretability 0.50

## In one line

Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.

## Problem

Distinguishing sound from flawed reasoning is a practical need. Trajectory-based detectors read layerwise residual-stream displacements, which capture how representations change while attenuating stable token-specific information — but displacement discards the state the update started from, and restoring the full state reintroduces shortcut-prone information. That trade-off is the obstacle.

## Contributions

- Identification of the displacement-versus-full-state trade-off in trajectory-based reasoning-error detection
- A three-stream detector combining motion, a vector-quantized coarse region reader, and a fine direction reader over normalized multi-layer states
- Up to 12% and 21% selection-accuracy gains over displacement-only and single-layer probing baselines on unseen reasoning benchmarks
- Transfer to factual completion and fact verification, evidence that the signal tracks correctness rather than a reasoning type
- Ablations establishing motion, region and direction as complementary

## Method

A three-stream detector that combines motion with two restricted views of location: a coarse region reader based on vector quantization, and a fine direction reader over normalized multi-layer states. The restriction is the design: it restores enough state context to interpret the motion without returning to full-state probing and its shortcuts.

## Results

On reasoning benchmarks unseen during training, selection accuracy improves by up to 12% over the displacement-only state of the art and 21% over single-layer probing baselines. Though trained only on reasoning benchmarks, the detector also reads factual completion and fact verification ahead of every compared detector, which the authors take to place the signal on correctness rather than on a kind of reasoning. Ablations show motion, region and direction contribute complementary signals.

## Limitations

Improvements are stated as 'up to', so the typical gain is lower than 12%/21%. Benchmarks and models are not named in the abstract. Transfer to factual tasks supports a correctness signal but leaves open whether the signal is correctness or a correlate such as fluency or confidence. The detector needs white-box access to multi-layer activations, so it cannot monitor an API model.

## Why it matters here

- **reasoning-evaluation**: Offers a per-trace correctness signal that does not need a ground-truth answer, which is the missing ingredient for evaluating reasoning on problems with no verifier. Its transfer to factual tasks is the stronger evaluation claim: a detector trained on reasoning that reads factual correctness too is measuring something more general than reasoning quality, which cuts both ways — useful as a monitor, but a warning that 'reasoning-error detection' benchmarks may be measuring correctness detection.
- **reasoning-interpretability**: A concrete answer to where reasoning errors live: a region and a direction in residual-stream trajectory space, with the two carrying complementary information and neither sufficient alone. The methodological contribution is the deliberate restriction of state information — quantized region plus normalized direction — as a way to get state context without shortcut features, which is a middle path between displacement-only trajectories and full-state probing that the archive's probing thread has not held before.

## Entities

- **Concepts**: [residual stream](../../../../wiki/concepts/residual-stream.md), [reasoning trajectory](../../../../wiki/concepts/reasoning-trajectory.md), [localization](../../../../wiki/concepts/localization.md), [shortcut learning](../../../../wiki/concepts/shortcut-learning.md), [out-of-distribution generalization](../../../../wiki/concepts/out-of-distribution-generalization.md), [error detection](../../../../wiki/concepts/error-detection.md), [effective depth](../../../../wiki/concepts/effective-depth.md)
- **Methods**: [linear probe](../../../../wiki/methods/linear-probe.md), vector quantization, trajectory-based detection, [activation probing](../../../../wiki/methods/activation-probing.md), multi-layer state normalization
- **Datasets**: _none recorded_

Tags: `residual stream`, `probing`, `error detection`, `trajectory`, `interpretability`

## Abstract

As language models are increasingly used for tasks that require verifiable reasoning, reliably distinguishing sound reasoning from flawed reasoning has become an important practical problem. Recent trajectory-based methods seek this signal in layerwise residual-stream displacements, which capture how representations change while attenuating some stable, token-specific information. However, displacement omits the state from which an update originates, whereas restoring the full state risks reintroducing shortcut-prone information. We identify this trade-off and propose a three-stream detector that combines motion with two restricted views of location. A coarse region reader based on vector quantization and a fine direction reader over normalized multi-layer states. This design restores enough state context to interpret the motion without returning to full-state probing. On reasoning benchmarks unseen during training, our method improves selection accuracy by up to 12% over the displacement-only state of the art and 21% over single-layer probing baselines. Although trained only on reasoning benchmarks, it also reads factual completion and fact verification, ahead of every detector we compare against, which places the signal on correctness rather than on a kind of reasoning. Ablations further show that motion, region, and direction provide complementary signals. These results suggest that reasoning validity is better read from state-conditioned motion than from either static states or decontextualized trajectories alone.

---

Record id: `arxiv:2608.05660`
