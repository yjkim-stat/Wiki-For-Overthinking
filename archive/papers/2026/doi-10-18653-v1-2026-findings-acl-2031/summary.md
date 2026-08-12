<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy

- **Authors**: Hosein Hasani, Mohammadali Banayeeanzade, Ali Nafisi, Sadegh Mohammadian, Fatemeh Askari, Mobin Bagherian, Amirmohammad Izadi, Mahdieh Soleymani Baghshah
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.2031>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.2031
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

Explains LLM counting failures as a depth limit, since counting is computed across layers, and fixes it with a System-2 decomposition whose mechanism is then traced.

## Problem

LLMs perform well on complex mathematics yet fail systematically at counting. The paper attributes this to a transformer architectural limit: counting is performed across layers, so precision degrades for larger counts because depth is finite. That makes it a structural ceiling rather than a knowledge gap.

## Contributions

- An architectural account of LLM counting failure as a depth limitation, since counting proceeds across layers
- A test-time System-2 decomposition of large counting tasks into independently solvable sub-problems
- A mechanistic trace of the strategy: latent counts stored in final item representations per part, moved by dedicated attention heads, aggregated at the end
- Experimental evidence that the strategy surpasses the architectural limit on large-scale counting

## Method

A simple test-time strategy inspired by System-2 cognition decomposes a large counting task into smaller independent sub-problems the model can solve reliably — trading depth for sequential steps. Observational and causal mediation analyses are then used to understand why it works, identifying the components involved.

## Results

Mechanistic analysis finds latent counts are computed and stored in the final item representations of each part, transferred to intermediate steps via dedicated attention heads, and aggregated at the final stage to produce the total. Experimentally, the strategy lets models surpass the architectural limitation and reach higher accuracy on large-scale counting.

## Limitations

No numbers in the abstract and no named models. Counting is a narrow task, chosen because the depth argument is clean there, so generalization of the System-2 claim beyond it is asserted rather than shown. The mechanistic account is obtained on the decomposed strategy, so it describes how the fix works rather than how unaided counting fails. Causal mediation analysis identifies components relative to the chosen metric.

## Why it matters here

- **reasoning-interpretability**: One of the few entries in this archive that connects a behavioural failure to an architectural cause and then verifies the causal path — depth-bounded across-layer computation, with the fix's mechanism traced to specific storage sites and transfer heads. That is the shape of explanation the archive's effective-depth thread wants, on a task simple enough for the argument to be checked. It also gives a mechanistic reason why serializing a computation into explicit steps helps at all, which is the premise of chain-of-thought generally: extra tokens buy sequential depth the architecture cannot supply within one forward pass.

## Entities

- **Concepts**: [effective depth](../../../../wiki/concepts/effective-depth.md), counting, System-2 reasoning, [localization](../../../../wiki/concepts/localization.md), [attention head](../../../../wiki/concepts/attention-head.md), causal mediation analysis, architectural limitation, [test-time compute](../../../../wiki/concepts/test-time-compute.md)
- **Methods**: [causal mediation analysis](../../../../wiki/methods/causal-mediation-analysis.md), [activation patching](../../../../wiki/methods/activation-patching.md), task decomposition, System-2 prompting
- **Datasets**: _none recorded_

Tags: `counting`, `effective depth`, `causal mediation`, `system-2`, `interpretability`

## Abstract

Large language models (LLMs), despite strong performance on complex mathematical problems, exhibit systematic limitations in counting tasks. This issue arises from the architectural limits of transformers, where counting is performed across layers, leading to degraded precision for larger counting problems due to depth constraints. To address this limitation, we propose a simple test-time strategy inspired by System-2 cognitive processes that decomposes large counting tasks into smaller, independent sub-problems that the model can reliably solve. We evaluate this approach using observational and causal mediation analyses to understand the underlying mechanism of this System-2-like strategy. Our mechanistic analysis identifies key components: latent counts are computed and stored in the final item representations of each part, transferred to intermediate steps via dedicated attention heads, and aggregated in the final stage to produce the total count. Experimental results demonstrate that this strategy enables LLMs to surpass architectural limitations and achieve higher accuracy on large-scale counting tasks. This work provides mechanistic insight into System-2 counting in LLMs and presents a generalizable approach for improving and understanding their reasoning behavior.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2031`
