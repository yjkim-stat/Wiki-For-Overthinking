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

Trains large reasoning models to self-correct mid-chain-of-thought drift using adversarial temptation/hesitation examples, improving jailbreak robustness and reducing over-refusal.

## Problem

Chain-of-thought reasoning in LRMs introduces safety failure modes beyond conventional alignment: minor reasoning deviations can progressively amplify (a 'snowball effect') into either harmful compliance or excessive refusal, because models are trained to replicate correct reasoning traces without learning to self-correct when they drift.

## Contributions

- Identifies a 'snowball effect' in LRM chain-of-thought where minor reasoning deviations amplify into harmful compliance or excessive refusal
- Proposes AdvChain, adversarial CoT tuning with Temptation-Correction and Hesitation-Correction training samples to teach dynamic self-correction
- Shows improved robustness to jailbreak attacks and CoT hijacking and reduced over-refusal on benign prompts

## Method

AdvChain builds a tuning dataset of two adversarial CoT sample types: Temptation-Correction traces, which start drifting toward harmful compliance and then recover, and Hesitation-Correction traces, which start drifting toward unnecessary refusal and then recover. Training on these traces teaches the model to detect and correct its own reasoning drift mid-chain rather than only replicating an ideal, undeviating reasoning path.

## Results

AdvChain improves robustness against jailbreak attacks and CoT hijacking, reduces over-refusal on benign prompts, and yields a better safety-utility balance than baselines without degrading reasoning ability, per the available material; no specific numeric deltas were found.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: this is a safety-alignment paper about chain-of-thought drift causing harmful compliance or over-refusal, not about the accuracy/efficiency tradeoff of reasoning length or when a model should stop reasoning. It shares only the 'large reasoning model' keyword with the topic; reasoning length and test-time compute are not discussed.

## Entities

- **Concepts**: chain-of-thought snowball effect, self-correction in reasoning, adversarial CoT tuning
- **Methods**: AdvChain, adversarial chain-of-thought tuning
- **Datasets**: _none recorded_

Tags: `safety`, `jailbreak`, `chain-of-thought`, `alignment`, `over-refusal`

---

Record id: `title:901ba3102e447b12`
