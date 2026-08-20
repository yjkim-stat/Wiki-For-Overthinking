<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TravelReasoner: Leveraging Large Reasoning Models to Address Mobility Data Gap

- **Authors**: Peijie Liu, Fengli Xu, Yong Li
- **Venue**: The Web Conference
- **Published**: 2026-04-13
- **Source**: semanticscholar
- **Link**: <https://www.semanticscholar.org/paper/01c84bcd6e681633bf47bc34a73afb7423695452>
- **DOI**: 10.1145/3774904.3793054
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

TravelReasoner post-trains large reasoning models on a reasoning-aligned Chain-of-Trips dataset derived from NHTS to synthesize interpretable, behaviorally consistent travel/mobility survey data, improving location consistency by 6.8% and time consistency by 4.1% over baselines.

## Problem

Web-based urban platforms (epidemic response, emergency management, urban planning) need fine-grained individual mobility data, but collecting it is hard due to privacy concerns, security restrictions, low participation, and high acquisition cost; the paper addresses generating synthetic but behaviorally realistic mobility data to fill this gap.

## Contributions

- Proposes TravelReasoner, a framework that uses large reasoning models to generate mobility (travel survey) data with interpretable, behaviorally coherent reasoning traces.
- Constructs Chain-of-Trips, a reasoning-aligned dataset derived from the National Household Travel Survey (NHTS).
- Develops a curriculum-based post-training pipeline to improve in-domain reasoning consistency for travel-behavior generation.
- Reports improved location consistency (+6.8%) and time consistency (+4.1%) over baselines, plus generalization across demographic groups and cross-city transferability.

## Method

Large reasoning models are post-trained with a curriculum-based pipeline on Chain-of-Trips, a dataset derived from NHTS that aligns travel-survey records with step-by-step reasoning traces, so that the model generates synthetic individual travel/mobility sequences (location and timing choices) along with an interpretable rationale for each trip decision, addressing the scarcity of fine-grained, privacy-sensitive mobility data.

## Results

Reported improvements over baselines: +6.8% location consistency and +4.1% time consistency (metrics as reported in the paper's own summary; exact baseline methods and absolute values were not available in the retrievable material). The paper also reports generalization across demographic groups and cross-city transferability, without further stated numbers.

## Limitations

Not stated in the available material (abstract was empty in the source record; summary drawn from the paper's GitHub README and search results, which do not include a limitations section).

## Why it matters here

- **overthinking**: Tangential: the paper matches the topic only on the generic phrase 'large reasoning models,' which it uses as a data-generation tool for an unrelated application domain (synthetic mobility/travel-survey data). It does not study reasoning length, the accuracy/efficiency tradeoff of test-time compute, or methods to make a model stop or keep reasoning longer -- reasoning traces here are a means to interpretable trip generation, not an object of study in themselves.

## Entities

- **Concepts**: reasoning-aligned synthetic data generation, Chain-of-Trips dataset, curriculum-based post-training, mobility data gap
- **Methods**: TravelReasoner, Large reasoning models (LRMs) as data generators, Curriculum-based post-training
- **Datasets**: National Household Travel Survey (NHTS), Chain-of-Trips (derived reasoning-aligned dataset)

Tags: `large-reasoning-models`, `mobility-data`, `synthetic-data-generation`, `travel-survey`, `curriculum-training`

---

Record id: `doi:10.1145/3774904.3793054`
