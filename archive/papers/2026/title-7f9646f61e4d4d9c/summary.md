<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Internalizing Safety Understanding in Large Reasoning Models via Verification

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63605>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Safety Internal (SInternal) trains large reasoning models to critique their own generated answers using expert reasoning trajectories, building genuine internal safety comprehension rather than relying on external compliance detection, and shows this verification-based training -- especially when paired with RL -- produces stronger defenses against manipulated harmful prompts than standard supervised fine-tuning.

## Problem

AI safety for reasoning models typically relies on external compliance detection (checking outputs against rules after generation) rather than genuine internal understanding of safety principles, which the paper argues is a critical gap that behavioral-imitation-based training does not close.

## Contributions

- Safety Internal (SInternal), training reasoning models to critique their own answers using expert reasoning trajectories to build internal safety understanding
- empirical evidence that verification-trained models resist manipulated/disguised harmful prompts better than behaviorally-imitation-trained ones
- demonstration that pairing verification-based internalization with RL outperforms standard SFT as a safety-alignment foundation

## Method

Introduces Safety Internal (SInternal), which trains models on a verification task -- critiquing their own generated answers using expert reasoning trajectories -- so the model learns to understand and check safety principles internally rather than merely imitating safe behavior; compares standard supervised fine-tuning against pairing this verification-based internalization with reinforcement learning as the foundation for safety alignment.

## Results

Models trained on the verification task develop stronger defenses against harmful prompts disguised through manipulation (e.g. adversarial framing) than models without this training; when SInternal's verification-based internalization is paired with reinforcement learning, it outperforms standard supervised fine-tuning as a foundation for safety alignment.

## Limitations

Not stated in the fetched abstract beyond the comparison against standard SFT-based safety alignment.

## Why it matters here

- **overthinking**: Not directly relevant to reasoning length or efficiency: this is a safety-alignment training method for reasoning models (internalized safety verification vs. behavioral compliance), matched to the topic only via the shared context of large reasoning models; tangentially related to this archive's self-verification/self-critique thread (e.g. Self-Reflection, MONICA) in that it also uses a reasoning model's own critique capability as a training signal, but for safety rather than efficiency.

## Entities

- **Concepts**: internal safety comprehension (vs. behavioral compliance), self-critique via verification training, principled safety reasoning
- **Methods**: Safety Internal (SInternal, self-critique/verification training), supervised fine-tuning (comparison baseline), reinforcement learning (paired with SInternal)
- **Datasets**: _none recorded_

Tags: `safety-alignment`, `self-verification`, `large-reasoning-models`, `reinforcement-learning`

---

Record id: `title:7f9646f61e4d4d9c`
