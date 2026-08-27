<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TinyTTA: Efficient Test-time Adaptation via Early-exit Ensembles on Edge Devices

- **Authors**: _unknown_
- **Venue**: NeurIPS 2024
- **Published**: 2024-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2024/poster/94778>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

TinyTTA enables test-time adaptation on memory-constrained microcontroller units via a self-ensemble, batch-agnostic early-exit strategy, improving TTA accuracy by up to 57.6% and cutting memory use up to 6x versus prior methods.

## Problem

Test-time adaptation (TTA) to handle data-distribution shifts on IoT/edge devices has not been validated on truly resource-constrained hardware (microcontroller units), where full backpropagation, lack of normalization-layer support, and batch-size tradeoffs make existing TTA approaches infeasible.

## Contributions

- a self-ensemble, batch-agnostic early-exit strategy enabling TTA under severe memory constraints
- the TinyTTA Engine, a first-of-its-kind MCU library for on-device TTA
- up to 57.6% accuracy improvement and 6x memory reduction on real MCU hardware

## Method

Proposes a self-ensemble and batch-agnostic early-exit strategy for TTA that enables continuous adaptation with small batch sizes to reduce memory usage while handling distribution shifts, and builds the TinyTTA Engine, an MCU library enabling on-device TTA, validated on a Raspberry Pi Zero 2W and an STM32H747 MCU.

## Results

TinyTTA improves TTA accuracy by up to 57.6%, reduces memory usage by up to 6x, and achieves faster, more energy-efficient adaptation versus prior methods; it is reported as the only framework able to run TTA on the STM32H747 MCU under a 512 KB memory constraint while maintaining high performance.

## Limitations

Not stated in the fetched abstract beyond the two tested hardware targets (Raspberry Pi Zero 2W, STM32H747).

## Why it matters here

- **overthinking**: Off-topic domain (on-device test-time adaptation for distribution shift on microcontrollers, not LLM reasoning), matched via 'early exit'; not connected to reasoning length or the accuracy/efficiency tradeoff the topic tracks.

## Entities

- **Concepts**: test-time adaptation (TTA) on microcontrollers, self-ensemble batch-agnostic early exit, on-device continuous adaptation
- **Methods**: test-time adaptation (TTA), self-ensemble early exit
- **Datasets**: _none recorded_

Tags: `test-time-adaptation`, `early-exit`, `edge-devices`, `efficiency`

## Abstract

Abstract The increased adoption of Internet of Things (IoT) devices has led to the generation of large data streams with applications in healthcare, sustainability, and robotics. In some cases, deep neural networks have been deployed directly on these resource-constrained units to limit communication overhead, increase efficiency and privacy, and enable real-time applications. However, a common challenge in this setting is the continuous adaptation of models necessary to accommodate changing environments, i.e., data distribution shifts. Test-time adaptation (TTA) has emerged as one potential solution, but its validity has yet to be explored in resource-constrained hardware settings, such as those involving microcontroller units (MCUs). TTA on constrained devices generally suffers from i) memory overhead due to the full backpropagation of a large pre-trained network, ii) lack of support for normalization layers on MCUs, and iii) either memory exhaustion with large batch sizes required for updating or poor performance with small batch sizes. In this paper, we propose TinyTTA, to enable, for the first time, efficient TTA on constrained devices with limited memory. To address the limited memory constraints, we introduce a novel self-ensemble and batch-agnostic early-exit strategy for TTA, which enables continuous adaptation with small batch sizes for reduced memory usage, handles distribution shifts, and improves latency efficiency. Moreover, we develop the TinyTTA Engine, a first-of-its-kind MCU library that enables on-device TTA. We validate TinyTTA on a Raspberry Pi Zero 2W and an STM32H747 MCU. Experimental results demonstrate that TinyTTA improves TTA accuracy by up to 57.6\%, reduces memory usage by up to six times, and achieves faster and more energy-efficient TTA. Notably, TinyTTA is the only framework able to run TTA on MCU STM32H747 with a 512 KB memory constraint while maintaining high performance.

---

Record id: `title:bf8bc6d3bbf1c242`
