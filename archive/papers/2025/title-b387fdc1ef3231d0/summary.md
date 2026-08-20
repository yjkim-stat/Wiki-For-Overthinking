<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# One Token Embedding Is Enough to Deadlock Your Large Reasoning Model

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116766>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

The Deadlock Attack trains a backdoored adversarial token embedding that forces large reasoning models into perpetual chain-of-thought loops, achieving a 100% attack success rate across four LRMs and three math benchmarks.

## Problem

The iterative chain-of-thought mechanism of large reasoning models introduces a new resource-exhaustion vulnerability, but naive adversarial embeddings fail to survive the continuous-to-discrete projection needed to actually trigger the exploit via real input tokens.

## Contributions

- The Deadlock Attack: a resource-exhaustion attack that hijacks an LRM's generative control flow to induce perpetual reasoning loops
- A trained adversarial embedding that biases the model toward transitional tokens (e.g. 'Wait', 'But') so it never concludes its answer
- A backdoor implantation strategy that solves the continuous-to-discrete projection gap, enabling reliable activation via specific trigger tokens
- 100% attack success rate across four LRMs and three math reasoning benchmarks, forcing generation up to the maximum token limit
- Shows the attack is stealthy (negligible utility loss on benign inputs) and remains robust against existing methods for mitigating overthinking

## Method

The attack optimizes an adversarial token embedding that, when present, biases the model's generation toward transitional tokens such as 'Wait' and 'But' after each reasoning step, preventing it from concluding. Because naive projection of a continuous adversarial embedding to discrete tokens nullifies the effect, the authors instead implant it as a backdoor: reliable activation is achieved through specific trigger tokens rather than the embedding itself, letting the attack survive the continuous-to-discrete gap.

## Results

100% attack success rate across four LRMs (Phi-RM, Nemotron-Nano, R1-Qwen, R1-Llama) and three math reasoning benchmarks, forcing models to generate up to their maximum token limit; negligible utility loss on benign inputs; robust against existing overthinking-mitigation strategies.

## Limitations

Abstract does not report a numeric figure for the 'negligible' utility loss on benign inputs, does not name the three math reasoning benchmarks, and does not discuss whether the attack requires white-box access to train the adversarial embedding and implant the backdoor.

## Why it matters here

- **overthinking**: Directly engages the topic from an adversarial angle: it shows the overthinking failure mode (a model that keeps reasoning instead of stopping) can be deliberately and reliably induced via a backdoored embedding, and reports that the attack remains robust against existing strategies meant to mitigate overthinking - relevant to understanding what makes a model fail to stop at the right point.

## Entities

- **Concepts**: adversarial embedding attack, backdoor trigger, induced reasoning loop, resource exhaustion, overthinking as attack surface
- **Methods**: Deadlock Attack, adversarial embedding optimization, backdoor implantation
- **Datasets**: _none recorded_

Tags: `overthinking`, `adversarial-attack`, `backdoor`, `reasoning-loop`, `security`

## Abstract

Abstract Modern large reasoning models (LRMs) exhibit impressive multi-step problem-solving via chain-of-thought (CoT) reasoning. However, this iterative thinking mechanism introduces a new vulnerability surface. We present the Deadlock Attack, a resource exhaustion method that hijacks an LRM's generative control flow by training a malicious adversarial embedding to induce perpetual reasoning loops. Specifically, the optimized embedding encourages transitional tokens (e.g., “Wait”, “But”) after reasoning steps, preventing the model from concluding its answer. A key challenge we identify is the continuous-to-discrete projection gap: naïve projections of adversarial embeddings to token sequences nullify the attack. To overcome this, we introduce a backdoor implantation strategy, enabling reliable activation through specific trigger tokens. Our method achieves a 100\% attack success rate across four advanced LRMs (Phi-RM, Nemotron-Nano, R1-Qwen, R1-Llama) and three math reasoning benchmarks, forcing models to generate up to their maximum token limits. The attack is also stealthy (in terms of causing negligible utility loss on benign user inputs) and remains robust against existing strategies trying to mitigate the overthinking issue. Our findings expose a critical and underexplored security vulnerability in LRMs from the perspective of reasoning (in)efficiency.

---

Record id: `title:b387fdc1ef3231d0`
