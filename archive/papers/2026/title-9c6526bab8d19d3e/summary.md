<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Doxing via the Lens: Revealing Location-related Privacy Leakage on Multi-modal Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10006914>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces DoxBench (500 real-world images) and shows most tested multi-modal large reasoning models outperform non-expert humans at inferring a person's home location from an image's visual details, then demonstrates a practical two-stage attack (GeoMiner) exploiting this.

## Problem

Multi-modal large reasoning models can infer sensitive geolocation information (e.g. home address or neighborhood) from user-generated images by combining visual detail extraction with internal geographic knowledge, and this privacy risk was not previously benchmarked or attributed to a specific mechanism.

## Contributions

- DoxBench, a 500-image benchmark across six categories for evaluating geolocation-inference privacy leakage
- a three-tier risk framework for this class of privacy risk
- GeoMiner, a two-stage attack demonstrating real-world feasibility of geolocation doxing via multi-modal LRMs

## Method

Develops a three-tier risk framework and DoxBench, a dataset of 500 real-world images across six categories, to evaluate geolocation-inference privacy leakage across 13 multi-modal LRMs; introduces GeoMiner, a two-stage attack framework (clue extraction, then reasoning) to demonstrate real-world feasibility.

## Results

Most of the 13 evaluated models outperform non-expert humans at geolocation inference from images; the paper attributes the vulnerability to models combining visual detail extraction with internal geographic knowledge and lacking any mechanism to suppress use of privacy-sensitive visual clues; GeoMiner demonstrates the attack is practically feasible.

## Limitations

Not stated in the fetched abstract beyond the six image categories and 13 models tested.

## Why it matters here

- **overthinking**: Not relevant to reasoning length or efficiency: this is a privacy/safety study of multi-modal large reasoning models' geolocation-inference capability, matched to the topic only via the shared term 'large reasoning model.'

## Entities

- **Concepts**: geolocation privacy leakage, visual clue extraction, inference-time privacy safeguard
- **Methods**: three-tier risk framework, GeoMiner two-stage attack (clue extraction + reasoning)
- **Datasets**: DoxBench (new, 500 images)

Tags: `privacy`, `multi-modal`, `large-reasoning-models`, `geolocation-inference`

---

Record id: `title:9c6526bab8d19d3e`
