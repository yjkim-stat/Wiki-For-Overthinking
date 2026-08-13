<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders

- **Authors**: Bo Cheng, Qiaolin Lu, Yi Chang, Yuan Wu
- **Venue**: cs.CL
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08168>
- **PDF**: <https://arxiv.org/pdf/2608.08168v1>
- **Topics**: reasoning-interpretability, reasoning-training
- **Relevance score**: reasoning-interpretability 0.50, reasoning-training 0.40, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

While Large Language Models (LLMs) employing Chain-of-Thought (CoT) exhibit superior reasoning capabilities, the neural mechanisms distinguishing this explicit Thinking mode from direct answer generation (NoThinking mode) remain poorly understood. To deconstruct this cognitive process, we apply Top-K Sparse Autoencoders (SAEs) to the intermediate representations of DeepSeek-R1-Distill-Qwen-7B and examine the model's divergent behaviors across math-solving tasks of three distinct difficulty levels. Observationally, we identify a clear distinction in how the model functions under two reasoning modes: Thinking mode relies on sparse and high-intensity feature activations driving verbal deduction independent of problem complexity, whereas NoThinking mode exhibits an adaptive and diffuse pattern prioritizing symbolic manipulation. Causally, suppressing the three most active sparse features by Total Activation Volume reveals three principles: (i) reasoning and syntactic structure are tightly coupled, as interventions consistently degrade \LaTeX{} and boxed-solution formatting; (ii) Thinking responds to disruption with compensatory over-generation marked by increased metacognitive cues and repetitive, low-information continuations; and (iii) coherent CoT behavior depends on a fragile coordination among specialized features, yielding distinct failure modes under perturbation but a consistently impaired output structure.

---

Record id: `arxiv:2608.08168`
