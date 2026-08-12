<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond &apos;Aha!&apos;: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models

- **Authors**: Zhiyuan Hu, Yibo Wang, Hanze Dong, Yuhui Xu, Amrita Saha, Caiming Xiong, Bryan Hooi, Junnan Li 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.1981>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.1981
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.80

## In one line

Replaces reliance on unpredictable emergent 'aha moments' by explicitly aligning models to deduction, induction and abduction on self-verifiable tasks before domain RL.

## Problem

Reasoning models already hold a latent capacity for long chain-of-thought reasoning, and outcome-based RL can incidentally elicit behaviours such as self-correction, backtracking and verification — the 'aha moment'. But the timing and consistency of those emergent behaviours are unpredictable and uncontrollable, which limits scalability and reliability.

## Contributions

- The argument that emergent aha moments are unpredictable and should be replaced by explicit alignment
- Explicit alignment to deduction, induction and abduction using automatically generated self-verifiable tasks
- A three-stage pipeline of individual alignment, parameter-space merging and domain-specific RL
- Over 10% gains over instruction-tuned baselines, with domain RL from the aligned checkpoint raising the ceiling at 7B and 32B across math, coding and science

## Method

Rather than relying on prompts and emergence, models are explicitly aligned with three meta-abilities — deduction, induction, abduction — using automatically generated, self-verifiable tasks. Self-verifiability is what makes the alignment data scalable without human labels. A three-stage pipeline follows: individual alignment per meta-ability, parameter-space merging of the three, then domain-specific reinforcement learning.

## Results

The pipeline boosts performance by over 10% relative to instruction-tuned baselines. Domain-specific RL from the aligned checkpoint yields an additional gain in the performance ceiling for both 7B and 32B models across math, coding and science benchmarks.

## Limitations

Benchmarks and base models are not named. 'Over 10%' relative to instruction-tuned baselines is a weak comparison point for reasoning work. The three meta-abilities are a taxonomy imported from logic, and whether they carve model computation into separable, mergeable parts is assumed — parameter-space merging succeeding is indirect evidence, not proof. Automatically generated self-verifiable tasks bound what can be taught to what can be auto-verified.

## Why it matters here

- **reasoning-training**: Takes a position on this topic's central question that most of the archive does not: that the reasoning behaviours RLVR elicits by accident should be trained on purpose, decomposed into logical primitives. The claim that raises the performance ceiling rather than only the score is the important one, since it implies meta-ability alignment changes what subsequent RL can reach rather than substituting for it. That it works via parameter-space merging of three separately aligned checkpoints is also evidence bearing on the modularity thread here, and it sits directly against doi:10.18653/v1/2026.acl-long.2201's finding that reasoning lives in low-gradient-sensitivity regions where merging usually collapses — one paper merges reasoning abilities successfully, the other explains why merging reasoning normally fails.

## Entities

- **Concepts**: [aha moment](../../../../wiki/concepts/aha-moment.md), meta-ability, [emergent behaviour](../../../../wiki/concepts/emergent-behaviour.md), deduction, induction, abduction, model merging, [self-verification](../../../../wiki/concepts/self-verification.md), [performance ceiling](../../../../wiki/concepts/performance-ceiling.md)
- **Methods**: meta-ability alignment, parameter-space merging, domain-specific reinforcement learning, self-verifiable task generation
- **Datasets**: _none recorded_

Tags: `meta-ability`, `aha moment`, `model merging`, `rlvr`, `alignment`

## Abstract

Large reasoning models (LRMs) already possess a latent capacity for long chain-of-thought reasoning. Prior work has shown that outcome-based reinforcement learning (RL) can incidentally elicit advanced reasoning behaviors such as self-correction, backtracking, and verification–phenomena often referred to as the model’s ”aha moment”. However, the timing and consistency of these emergent behaviors remain unpredictable and uncontrollable, limiting the scalability and reliability of LRMs’ reasoning capabilities. To address these limitations, we move beyond reliance on prompts and unpredictable ”aha moments”. Instead, we explicitly align models with three meta-abilities: deduction, induction, and abduction, using automatically generated, self-verifiable tasks. Our three-stage pipeline (individual alignment, parameter-space merging, domain-specific reinforcement learning) boosts performance by over 10% relative to instruction-tuned baselines. Furthermore, domain-specific RL from the aligned checkpoint yields an additional gain in performance ceiling for both 7B and 32B models across math, coding, and science benchmarks, showing that explicit meta-ability alignment offers a scalable and dependable foundation for reasoning. Code and data can be found in Software and Data part in submission page.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1981`
