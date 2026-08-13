<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering

- **Authors**: Jakub Poćwiardowski, Mateusz Modrzejewski
- **Venue**: cs.SD
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.06638>
- **PDF**: <https://arxiv.org/pdf/2608.06638v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Mechanistic interpretability of music generation has concentrated on audio models, leaving symbolic models largely unexplored. We analyze two public text-to-MIDI systems of contrasting design: the purpose-built encoder--decoder text2midi and MIDI-LLM, a Llama~3.2~1B model extended with MIDI tokens using linear probing, the logit and tuned lenses, activation patching and difference-in-means steering. Across these methods, we recover musically meaningful structure and show how architecture shapes its formation and control. Pitch, instrumentation, harmony and texture are linearly decodable in both models. text2midi refines predictions gradually across depth, whereas MIDI-LLM works largely in its inherited textual basis before a sharp late rotation into the musical vocabulary; patching identifies a matching late attenuation of prompt-driven instrument transfer. Steering produces bidirectional changes in register and polyphony in both systems, and in tempo/energy in MIDI-LLM. Our two-orientation protocol isolates directional control and shows that all-layer interventions are robust in text2midi but accumulate disruptively in MIDI-LLM. Together, the results provide a practical toolkit for tracing and controlling musical concepts in symbolic generators. Audio examples are available on a demo website.

---

Record id: `arxiv:2608.06638`
