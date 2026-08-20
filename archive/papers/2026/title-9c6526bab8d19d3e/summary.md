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

Shows that multi-modal large reasoning models can infer users' home locations from photos and introduces DoxBench plus a two-stage attack (GeoMiner) that improves this geolocation inference.

## Problem

Multi-modal large reasoning models' strong visual reasoning ability creates an underexplored privacy risk: adversaries can infer sensitive geolocation information, such as a home address, from user-generated images including private selfies, because these models combine visual clues with internal world knowledge without any mechanism to suppress privacy-sensitive inference.

## Contributions

- Identifies a novel privacy risk category in multi-modal LRMs: inferring sensitive geolocation (e.g., home address or neighborhood) from user images
- Proposes a three-level privacy risk framework categorizing images by contextual sensitivity and geolocation-inference potential
- Introduces DoxBench, 500 real-world images across 6 privacy-scenario categories
- Shows most of 13 evaluated MLRMs/MLLMs outperform non-expert humans at geolocation inference
- Proposes GeoMiner, a two-stage attack framework (clue extraction, then reasoning) that improves geolocation performance

## Method

The paper formalizes geolocation privacy risk via a three-level framework based on image contextual sensitivity and geolocation-inference potential, and builds DoxBench to evaluate it. GeoMiner, the attack framework, decomposes geolocation prediction into two stages: extracting visual clues from an image, then reasoning over those clues (combined with the model's internal world knowledge) to infer a location.

## Results

Across 13 advanced MLRMs and MLLMs, most models outperform non-expert humans at geolocation inference and can effectively leak location-related private information.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: this is a privacy and vision paper about geolocation inference from images, not about reasoning length or test-time compute allocation. It shares only the 'large reasoning model' keyword with the topic and does not discuss overthinking, underthinking, or stopping criteria.

## Entities

- **Concepts**: geolocation inference, privacy leakage, visual chain-of-thought reasoning
- **Methods**: DoxBench, GeoMiner, three-level privacy risk framework
- **Datasets**: DoxBench (500 images, 6 categories)

Tags: `privacy`, `geolocation`, `multimodal`, `doxing`, `vision`

## Abstract

Abstract Recent advances in multi-modal large reasoning models (MLRMs) have shown significant ability to interpret complex visual content. While these models possess impressive reasoning capabilities, they also introduce novel and underexplored privacy risks. In this paper, we identify a novel category of privacy leakage in MLRMs: Adversaries can infer sensitive geolocation information, such as users' home addresses or neighborhoods, from user-generated images, including selfies captured in private settings. To formalize and evaluate these risks, we propose a three-level privacy risk framework that categorizes image based on contextual sensitivity and potential for geolocation inference. We further introduce DoxBench, a curated dataset of 500 real-world images reflecting diverse privacy scenarios divided into 6 categories. Our evaluation across 13 advanced MLRMs and MLLMs demonstrates that most of these models outperform non-expert humans in geolocation inference and can effectively leak location-related private information. This significantly lowers the barrier for adversaries to obtain users' sensitive geolocation information. We further analyze and identify two primary factors contributing to this vulnerability: (1) MLRMs exhibit strong geolocation reasoning capabilities by leveraging visual clues in combination with their internal world knowledge; and (2) MLRMs frequently rely on privacy-related visual clues for inference without any built-in mechanisms to suppress or avoid such usage. To better understand and demonstrate real-world attack feasibility, we propose GeoMiner, a collaborative attack framework that decomposes the prediction process into two stages consisting of clue extraction and reasoning to improve geolocation performance. Our findings highlight the urgent need to reassess inference-time privacy risks in MLRMs to better protect users' sensitive information.

---

Record id: `title:9c6526bab8d19d3e`
