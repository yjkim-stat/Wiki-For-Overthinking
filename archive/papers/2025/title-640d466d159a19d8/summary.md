<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think or Not? Exploring Thinking Efficiency in Large Reasoning Models via an Information-Theoretic Lens

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119190>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Uses information-theoretic metrics (InfoBias, InfoGain) to show that longer reasoning chains in LRMs grow less informative and more divergent from an ideal path, and introduces an entropy-based stopping rule that cuts token usage while preserving accuracy.

## Problem

Large Reasoning Models improve multi-step reasoning but often generate excessively long reasoning chains; the paper investigates the reasoning-length/semantic-efficiency tradeoff and how to decide when a chain has said enough.

## Contributions

- Proposes InfoBias, a metric quantifying divergence of a reasoning chain from an ideal reasoning path
- Proposes InfoGain, a metric quantifying the stepwise information contribution of each reasoning step
- Shows empirically that longer reasoning chains exhibit higher information bias and diminishing information gain, especially for incorrect answers
- Introduces Adaptive Think, an entropy-based strategy that dynamically halts reasoning once confidence is sufficiently high
- Reports a 1.10% average accuracy improvement and 50.80% token-usage reduction on QwQ-32B across six benchmarks versus default (Vanilla Think) reasoning

## Method

Analyzes reasoning chains of Large Reasoning Models through an information-theoretic lens, defining InfoBias (divergence from an ideal reasoning path) and InfoGain (information contributed by each step) to quantify semantic efficiency. Based on the empirical finding that longer chains show rising InfoBias and shrinking InfoGain — more so when the final answer is wrong — the paper proposes Adaptive Think, an entropy-based stopping rule that halts generation once model confidence is high enough, instead of always running to a fixed or self-determined stopping point.

## Results

On QwQ-32B across six benchmark tasks, Adaptive Think yields a 1.10% average accuracy improvement and a 50.80% reduction in token usage compared to Vanilla Think (the default reasoning mode). Longer reasoning chains are shown to correlate with higher InfoBias and diminishing InfoGain, especially when the answer is incorrect.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: A direct, quantitative treatment of the topic: introduces information-theoretic measures showing that longer chains become less efficient (higher InfoBias, diminishing InfoGain), particularly for wrong answers — the fingerprint of overthinking — and proposes an explicit stopping method (entropy-based Adaptive Think) that improves accuracy by 1.10% while cutting token usage by 50.80% on QwQ-32B, i.e. a method to make a model stop at the right point.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), semantic efficiency, information bias, [information gain](../../../../wiki/concepts/information-gain.md), entropy-based stopping
- **Methods**: InfoBias metric, InfoGain metric, Adaptive Think (entropy-based adaptive stopping)
- **Datasets**: six benchmark tasks spanning diverse reasoning types and difficulty levels (unnamed in the abstract)

Tags: `overthinking`, `information-theory`, `entropy`, `adaptive-stopping`, `reasoning-length`, `reasoning-efficiency`

## Abstract

Abstract The recent rise of Large Reasoning Models (LRMs) has significantly improved multi-step reasoning performance, but often at the cost of generating excessively long reasoning chains. This paper revisits the efficiency of such reasoning processes through an information-theoretic lens, revealing a fundamental trade-off between reasoning length and semantic efficiency. We propose two metrics—InfoBias and InfoGain—to quantify divergence from ideal reasoning paths and stepwise information contribution, respectively. Empirical analyses show that longer reasoning chains tend to exhibit higher information bias and diminishing information gain, especially for incorrect answers. Motivated by these findings, we introduce an entropy-based Adaptive Think strategy that dynamically halts reasoning once confidence is sufficiently high, improving efficiency while maintaining competitive accuracy. Compared to the Vanilla Think approach (default mode), our strategy yields a 1.10% improvement in average accuracy and a 50.80% reduction in token usage on QwQ-32B across six benchmark tasks spanning diverse reasoning types and difficulty levels, demonstrating superior efficiency and reasoning performance. These results underscore the promise of entropy-based methods for enhancing both accuracy and cost-effiiciency in large language model deployment.

---

Record id: `title:640d466d159a19d8`
