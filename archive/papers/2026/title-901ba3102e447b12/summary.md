<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AdvChain: Adversarial Chain-of-Thought Tuning for Robust Safety Alignment of Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007590>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

AdvChain trains large reasoning models with adversarial chain-of-thought examples (Temptation-Correction and Hesitation-Correction pairs) to teach dynamic self-correction, reducing a 'snowball effect' where small reasoning deviations compound into harmful compliance or excessive refusal.

## Problem

Large reasoning models' multi-step chain-of-thought introduces a 'snowball effect' -- minor reasoning deviations accumulate across steps, ending in either harmful compliance or excessive over-refusal -- because models learn to replicate correct reasoning patterns without learning to self-correct when they drift.

## Contributions

- identification of a 'snowball effect' where small CoT reasoning deviations compound into harmful compliance or over-refusal
- AdvChain, training with Temptation-Correction and Hesitation-Correction adversarial samples to teach self-correction
- improved robustness to jailbreaks/CoT hijacking and reduced over-refusal without sacrificing reasoning ability

## Method

Constructs adversarial training data with two sample types: Temptation-Correction samples (recovering from a drift toward harmful reasoning) and Hesitation-Correction samples (recovering from unnecessary caution/over-refusal), and trains models on these via adversarial chain-of-thought tuning (AdvChain) to enable dynamic in-context self-correction.

## Results

AdvChain improves robustness against jailbreak attacks and chain-of-thought hijacking while reducing over-refusal on legitimate prompts, achieving a better safety-utility balance than compared methods without sacrificing reasoning capability (aggregate claims only, per the fetched abstract).

## Limitations

Not stated in the fetched abstract; no numeric benchmark results were retrievable from the fetched page.

## Why it matters here

- **overthinking**: Tangential: about the safety-content trajectory of a reasoning chain (drifting toward harm or toward excessive caution) rather than its length or efficiency, but the 'snowball effect' framing -- small deviations compounding across reasoning steps because the model never learned to self-correct -- parallels mechanisms proposed for why reasoning models overthink or fail to terminate.

## Entities

- **Concepts**: snowball effect (compounding reasoning drift), adversarial chain-of-thought tuning, dynamic self-correction
- **Methods**: adversarial chain-of-thought tuning, preference/self-correction training pairs
- **Datasets**: _none recorded_

Tags: `safety-alignment`, `chain-of-thought`, `self-correction`, `over-refusal`

---

Record id: `title:901ba3102e447b12`
