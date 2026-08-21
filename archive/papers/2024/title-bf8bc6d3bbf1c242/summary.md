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

Makes test-time adaptation to distribution shift feasible on microcontrollers by adapting only early-exit heads in a self-ensemble instead of backpropagating through the whole network, and ships an MCU runtime that executes it.

## Problem

Deep networks deployed on IoT devices and microcontrollers face data distribution shift after deployment, and test-time adaptation is the usual remedy, but it had not been shown to work under microcontroller constraints. Three obstacles: full backpropagation through a large pre-trained network exceeds the device's memory; MCU runtimes do not support the normalization layers most TTA methods update; and the batch sizes those methods need for stable statistics exhaust memory, while small batches degrade their accuracy.

## Contributions

- A self-ensemble, batch-agnostic early-exit strategy for test-time adaptation that supports small batch sizes and reduced memory.
- TinyTTA Engine, an MCU library enabling on-device test-time adaptation.
- Demonstration of TTA running on an STM32H747 under a 512 KB memory constraint, and on a Raspberry Pi Zero 2W.

## Method

A self-ensemble of early-exit heads attached to the backbone, adapted at test time in a batch-agnostic way so that adaptation proceeds with small batch sizes rather than requiring large ones for normalization statistics. This avoids full backpropagation through the pre-trained network and sidesteps the missing normalization-layer support on MCUs, while the early exits also cut inference latency. Alongside the method the authors build the TinyTTA Engine, an MCU library that executes on-device TTA.

## Results

Validated on a Raspberry Pi Zero 2W and an STM32H747 MCU. TTA accuracy improves by up to 57.6%, memory use falls by up to six times, and adaptation is reported as faster and more energy-efficient. TinyTTA is stated to be the only framework able to run TTA on the STM32H747 within its 512 KB memory constraint while maintaining performance. The abstract names no benchmark datasets and no per-dataset baseline numbers, so the comparison behind the 57.6% figure cannot be established from the material available here.

## Limitations

Not stated in the available material — no limitations are given in the abstract, and no full text was consulted. A reader should note that the headline numbers are given only as 'up to' maxima without the datasets, shift types, backbones or baselines they were measured against, and that the accuracy gain and the memory saving may come from different configurations. The claim of being the only framework that fits in 512 KB is a statement about the compared set, which the abstract does not enumerate.

## Why it matters here

- **overthinking**: This paper is a false positive for the topic and should be recorded as one. It was matched on the keyword 'early exit', and the phrase 'test-time' in its title collides with the topic's 'test-time compute scaling', but the two senses are unrelated. Test-time *adaptation* here means updating a vision model's parameters after deployment so it keeps working when the input distribution shifts — a domain-shift robustness problem — whereas the topic concerns how much inference-time computation a reasoning model spends on a given problem. Its 'early exit' is a memory-saving training mechanism: exit heads are adapted instead of the full backbone so that backpropagation fits in 512 KB. That is not the early exit the topic cares about, which is a model halting its reasoning once an answer is settled; nothing here decides when a computation has run long enough, and the work involves no language model, no reasoning trace and no accuracy/length tradeoff. The only genuine point of contact is the generic one that early-exit architectures can shorten inference, which is true of the literature this paper sits in but is not what this paper studies or measures. It should not be cited as evidence for anything in the overthinking topic, and if the archive supports removing a topic assignment, this one should be dropped rather than kept with a stretched justification.

## Entities

- **Concepts**: [Test-Time Adaptation](../../../../wiki/concepts/test-time-adaptation.md), [Distribution Shift](../../../../wiki/concepts/distribution-shift.md), Early Exit, On-Device Inference, Memory-Constrained Training
- **Methods**: TinyTTA, TinyTTA Engine, [early-exit ensembles](../../../../wiki/methods/early-exit-ensembles.md), self-ensemble, test-time adaptation (TTA)
- **Datasets**: _none recorded_

Tags: `test-time-adaptation`, `distribution-shift`, `early-exit`, `edge-computing`, `microcontroller`, `on-device-learning`, `memory-efficiency`, `false-positive`

## Abstract

Abstract The increased adoption of Internet of Things (IoT) devices has led to the generation of large data streams with applications in healthcare, sustainability, and robotics. In some cases, deep neural networks have been deployed directly on these resource-constrained units to limit communication overhead, increase efficiency and privacy, and enable real-time applications. However, a common challenge in this setting is the continuous adaptation of models necessary to accommodate changing environments, i.e., data distribution shifts. Test-time adaptation (TTA) has emerged as one potential solution, but its validity has yet to be explored in resource-constrained hardware settings, such as those involving microcontroller units (MCUs). TTA on constrained devices generally suffers from i) memory overhead due to the full backpropagation of a large pre-trained network, ii) lack of support for normalization layers on MCUs, and iii) either memory exhaustion with large batch sizes required for updating or poor performance with small batch sizes. In this paper, we propose TinyTTA, to enable, for the first time, efficient TTA on constrained devices with limited memory. To address the limited memory constraints, we introduce a novel self-ensemble and batch-agnostic early-exit strategy for TTA, which enables continuous adaptation with small batch sizes for reduced memory usage, handles distribution shifts, and improves latency efficiency. Moreover, we develop the TinyTTA Engine, a first-of-its-kind MCU library that enables on-device TTA. We validate TinyTTA on a Raspberry Pi Zero 2W and an STM32H747 MCU. Experimental results demonstrate that TinyTTA improves TTA accuracy by up to 57.6\%, reduces memory usage by up to six times, and achieves faster and more energy-efficient TTA. Notably, TinyTTA is the only framework able to run TTA on MCU STM32H747 with a 512 KB memory constraint while maintaining high performance.

---

Record id: `title:bf8bc6d3bbf1c242`
