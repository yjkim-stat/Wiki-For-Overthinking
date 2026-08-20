<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance

- **Authors**: Javier Rodriguez-Juan, Hiba Arnaout, Jose Garcia-Rodriguez, David Tomás, Iryna Gurevych
- **Venue**: cs.CL
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04524>
- **PDF**: <https://arxiv.org/pdf/2608.04524v1>
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.50

## In one line

Synthesizes Cognitive Behavioral Therapy dialogues using a CoT strategy grounded in CBT guidelines plus a resistance orchestrator that steers simulated patients away from sycophantic compliance.

## Problem

Synthetic CBT session generation must satisfy two competing demands: adherence to a strict sequential therapeutic structure, and modelling of resistant, unpredictable patient behaviour. Script-based methods miss the dynamics; multi-agent methods break the structure; both produce sycophantic, overly compliant patients that misrepresent clinical reality.

## Contributions

- The ODRA framework for CBT session synthesis with a guideline-grounded CoT strategy
- A resistance orchestrator that uses steering to control simulated-patient resistance level and remove sycophancy
- A synthetic CBT dataset whose fine-tuned models are evaluated against both cooperative and resistant patients

## Method

ODRA generates therapy dialogues through a Chain-of-Thought strategy grounded in published CBT guidelines (Beck, 2020), which supplies the sequential structure. A separate resistance orchestrator addresses patient sycophancy by applying steering techniques to elicit behaviour matched to a specified resistance level.

## Results

Automated and expert evaluation report that ODRA outperforms existing methods on therapeutic skills, CBT alignment and patient behavioural fidelity, with licensed psychologists preferring ODRA sessions on 12 of 13 clinical metrics. Models fine-tuned on the generated dataset perform better against both cooperative and resistant simulated patients.

## Limitations

No numeric margins are given for the automated evaluations; the headline evidence is a preference count over 13 metrics. Expert preference is not reported with inter-rater agreement or the number of psychologists. Downstream validation is against simulated patients, not human ones, so the claim that explicit resistance modelling transfers to clinical robustness is established only within simulation.

## Why it matters here

- **reasoning-training**: Peripheral. CoT is used here as a scaffold for controllable data generation, not as an object of study, and no reasoning benchmark is reported. The one point of contact is that structured CoT is doing a role-fidelity job rather than a problem-solving one, which is a use of the same mechanism this topic tracks for a different purpose.
- **test-time-scaling**: Peripheral. The resistance orchestrator is an inference-time steering intervention, but the quantity being controlled is simulated-patient behaviour, not reasoning length or accuracy, so nothing here bears on compute allocation.

## Entities

- **Concepts**: [sycophancy](../../../../wiki/concepts/sycophancy.md), structured chain of thought, synthetic data generation, behavioural fidelity
- **Methods**: chain of thought, [activation steering](../../../../wiki/methods/activation-steering.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), multi-agent dialogue simulation, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md)
- **Datasets**: ODRA synthetic CBT session dataset

Tags: `cbt`, `synthetic dialogue`, `steering`, `sycophancy`, `off-topic-candidate`

## Abstract

Synthetic generation of Cognitive Behavioral Therapy (CBT) sessions is challenged by two competing demands: adhering to strict therapeutic structure while modeling the resistant, unpredictable behavior of real patients. Existing script-based methods fail to capture dynamic therapeutic interactions, while multi-agent approaches struggle to adhere to CBT's sequential structure; both suffer from sycophancy, producing overly compliant patients that misrepresent real clinical settings. In this work we introduce ODRA, a novel framework for synthesizing therapy dialogues through a Chain-of-Thought (CoT) strategy grounded in foundational CBT guidelines (Beck, 2020). ODRA further incorporates a resistance orchestrator to solve patient sycophancy, which employs steering techniques to elicit behaviors aligned with their resistance level. Automated and expert evaluations show that ODRA significantly outperforms existing methods across therapeutic skills, CBT alignment, and patient behavioral fidelity, with licensed psychologists preferring ODRA sessions across 12 of 13 clinical metrics. Furthermore, models fine-tuned on our dataset demonstrate superior therapeutic performance against both cooperative and resistant patients, validating that explicit resistance modeling in synthetic training data directly translates to downstream clinical robustness.

---

Record id: `arxiv:2608.04524`
