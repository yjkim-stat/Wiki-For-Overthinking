<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?

- **Authors**: Pedro Ferreira, Wilker Aziz, Ivan Titov
- **Venue**: cs.CL
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04928>
- **PDF**: <https://arxiv.org/pdf/2608.04928v1>
- **Topics**: reasoning-faithfulness
- **Relevance score**: reasoning-faithfulness 0.57, reasoning-training 0.25, test-time-scaling 0.25

## In one line

Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.

## Problem

CoT monitorability rests on there being a readable trace. Latent CoT replaces explicit tokens with a few continuous states, cutting inference cost and removing that trace. Monitoring then needs alternative access — probing activations or verbalizing the latent states back into text — and how much monitorability those alternatives retain is unknown.

## Contributions

- A hint-based setup for measuring monitorability with hint-reliance as the target
- A comparison of monitors across explicit CoT and weakly- and strongly-supervised latent CoT
- The finding that task properties and internals access dominate reasoning mode in determining monitorability

## Method

A hint-based intervention setup serves as a proxy for behaviours where a model exploits a biasing input cue, such as a leaked answer or a belief stated by the user, without acknowledging it. Hint-reliance is the monitorability target. Monitors are compared across reasoning modes — explicit CoT, weakly-supervised latent CoT and strongly-supervised latent CoT — on math reasoning and question answering.

## Results

Monitorability depends more on properties of the task, such as whether the correct answer constrains the supporting reasoning, and on the level of access to model internals, than on the reasoning mode. No numbers are given in the abstract.

## Limitations

No quantitative results in the abstract. Hint-reliance is one proxy target, and a negative result about reasoning mode on this target need not transfer to other monitored behaviours. Models and probe architectures are not named. The finding is comparative and does not establish an absolute level of monitorability for any mode.

## Why it matters here

- **reasoning-faithfulness**: Pushes against the assumption that latent reasoning is the end of monitoring. If mode matters less than task structure and internals access, then the safety cost of moving to latent CoT is smaller than feared and the cost of losing white-box access is larger. It also names the task property that governs the difference — whether the correct answer constrains the supporting reasoning — which is a testable predictor rather than a general worry, and it pairs directly with arxiv:2608.04735, which finds the regime of influence matters more than the instruction.

## Entities

- **Concepts**: [monitorability](../../../../wiki/concepts/monitorability.md), [latent reasoning](../../../../wiki/concepts/latent-reasoning.md), [implicit reasoning](../../../../wiki/concepts/implicit-reasoning.md), [chain of thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md), hint reliance, linear probe
- **Methods**: latent chain of thought, [activation probing](../../../../wiki/methods/activation-probing.md), latent state verbalization, hint-based intervention
- **Datasets**: _none recorded_

Tags: `monitorability`, `latent cot`, `probing`, `faithfulness`, `hint reliance`

## Abstract

Chain-of-thought (CoT) reasoning offers a window into the decision-making of large language models (LLMs), which can be monitored for target behaviors by reading the reasoning trace, motivating work on CoT monitorability. Latent CoT approaches, however, replace the explicit tokens with a small number of continuous states, lowering inference costs but removing the readable trace this monitoring relies on. Monitoring then requires alternative access to the model, such as probing its activations or verbalizing the latent states back into text, but how much monitorability these alternatives preserve is unclear. We study this question with a hint-based intervention setup, a proxy for behaviors where models exploit biasing input cues, e.g., an inadvertently leaked answer or a belief stated by the user, without acknowledging them. Taking hint-reliance as the monitorability target, we compare monitors across reasoning modes, from explicit CoT to weakly- and strongly-supervised latent CoT, on math reasoning and question answering. We find that, in this setup, monitorability depends more on properties of the task (such as whether the correct answer constrains the supporting reasoning) and the level of access to model internals than on the reasoning mode.

---

Record id: `arxiv:2608.04928`
