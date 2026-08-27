<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# NeuReasoner: Towards Explainable, Controllable, and Unified Reasoning via Mixture-of-Neurons

- **Authors**: Haonan Dong, Kehan Jiang, Haoran Ye, Wenhao Zhu, Zhaolu Kang, Guojie Song
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1033/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1033.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1033
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

NeuReasoner identifies a Mixture of Neurons (MoN) -- three distinct neuron clusters in an LRM's middle layer whose fluctuation signatures predict intra-step (calculation/derivation) errors, inter-step (oscillation/stagnation) failures, and instance-level overthinking respectively -- then trains lightweight monitoring MLPs to detect these fluctuations online and trigger special-token-conditioned diagnose-then-correct behaviors, achieving 3.2-27.0% accuracy gains while cutting token consumption 19.6-63.3% across six backbones (8B-70B) and six benchmarks, beating nine training-free and RL-based efficient-reasoning baselines.

## Problem

Large reasoning models exhibit three distinct failure modes that compromise both performance and cost -- intra-step errors (calculation/derivation mistakes within a single reasoning step), inter-step failures (oscillating or stagnating between similar trajectories without progress, consuming excessive tokens before eventual collapse), and instance-level overthinking (failing to calibrate reasoning depth to query difficulty) -- but prior work addresses these levels individually (PRMs for intra-step, structured search frameworks like Tree-of-Thought for inter-step, length-control methods for instance-level) with no unified solution, and RL-based approaches are black-box, offering no explainability or fine-grained controllability over which internal mechanism produces which failure.

## Contributions

- a fine-grained, white-box neuron-level analysis (via DePass attribution and Fourier-domain fluctuation profiling) identifying three distinct neuron-cluster 'experts' (Mixture of Neurons) whose activation patterns correspond to intra-step, inter-step, and instance-level reasoning failures respectively, with intra-/instance-level experts concentrated in the FFN and inter-step experts concentrated in attention heads
- NeuReasoner, a unified explainable-and-controllable reasoning framework that trains lightweight monitoring MLPs to detect these three failure-mode fluctuation patterns online and triggers special-token-conditioned diagnose-then-correct behaviors (learned via SFT) upon detection, rather than relying on an opaque RL-trained policy
- extensive validation across six backbone LRMs (8B-70B, Qwen and Llama distillation families) and six benchmarks against nine baselines, showing simultaneous accuracy gains (3.2-27.0%) and token reductions (19.6-63.3%), plus an ablation isolating each failure-mode-specific MLP's distinct contribution

## Method

Uses DePass (an LLM attribution algorithm) to compute each middle-layer neuron's contribution to output logits at each generation step, identifying a Mixture of Neurons (MoN): three neuron-cluster 'experts' whose top-attributed neurons are almost exclusively concentrated in the FFN for intra-step and instance-level failures but in attention heads for inter-step failures. Constructs positive/negative sample pairs (via KV-cache cloning, repeated resampling, and LLM-as-judge failure detection) and analyzes each expert's activation fluctuation pattern via Fourier transform: intra-step failures show larger-amplitude, high-frequency spikes; inter-step failures show periodic, dominant-frequency oscillations; instance-level patterns show sustained activation for hard instances but sharp low-frequency drops for easy ones. NeuReasoner then (1) trains lightweight MLPs (MLP_intra, MLP_inter, MLP_inst) on Fourier-derived features (high-frequency energy ratio, spectral entropy, total variation energy, dominant-frequency energy ratio) to predict these fluctuation patterns online during a sliding window over generation; (2) reconstructs a training dataset that inserts special trigger tokens at failure points paired with diagnose-then-correct behavior templates, then applies SFT so the model learns to execute self-correction upon encountering these tokens (masking the trigger and true failure-mode label so they operate purely as inference-time control signals); (3) at inference, runs the trained MLPs in parallel with generation, and upon detecting an intra-step or inter-step fluctuation pattern, hard-inserts the corresponding trigger token to force a diagnose-then-correct response, while for instance-level detection it directly inserts a NoThinking-mode transition prompt ('Okay, I have finished thinking.') without needing SFT. Evaluated across six backbone LRMs (DeepSeek-R1-Distill-Qwen-7B/32B, Qwen3-8B/32B-thinking, DeepSeek-R1-Distill-Llama-8B/70B) on five benchmarks (AIME24/25, MATH500, GSM8K, GPQA-Diamond, LiveCodeBench) against nine baselines (vanilla, DAST, Think or Not, AlphaOne, RL+LP, GRPO, S-GRPO, DAPO, Self-Consistency).

## Results

NeuReasoner achieves dual superiority in performance and token cost across all six backbones and all five/six benchmarks, with accuracy gains of 3.2-27.0% (0.3-7.8 absolute points) while simultaneously cutting token consumption 19.6-63.3% relative to the vanilla backbone. On DeepSeek-R1-Distill-Qwen-7B + MATH500 specifically, NeuReasoner improves accuracy by 5.0 points while cutting token usage 48.1%, outperforming all nine baselines on both metrics simultaneously; even against DAPO (the strongest competing baseline), NeuReasoner still leads by 0.9 points with 60.5% less token consumption. Cross-task generalization: on DeepSeek-R1-Distill-Qwen-32B, DAPO performs adequately on math/science but struggles on LiveCodeBench (only +0.1 with 22.1% higher cost), while NeuReasoner achieves +1.4 with a 34.2% cost reduction on the same benchmark -- indicating the unified, mechanism-driven approach generalizes across task types better than a single RL objective tuned mainly for math. Test-time (self-consistency, Cons@k for k in {4,8,16,32,64}) and model-scale (8B to 70B) scalability analysis shows NeuReasoner maintains consistent gains across scales (7.8 at 8B, 4.4 at 70B on DeepSeek-R1-Distill-Llama + AIME25, versus DAST's degrading 3.3-gain-to-2.2-loss trend from 8B to 70B) and superior Cons@k performance across nearly all k, matching vanilla-model performance at k=8 using only k=... (i.e. reaching equivalent consensus accuracy with far fewer sampled paths) and outperforming vanilla by 3.5-10.0% at k=64. Ablation (removing MLP_intra, MLP_inter, MLP_inst individually or all together) shows removing MLP_intra causes the largest single-component accuracy/cost degradation, confirming intra-step failures are the dominant failure mode; removing MLP_inter yields only minor deficits; ablating MLP_inst triggers a drastic surge in token consumption, validating the necessity of the difficulty-aware (instance-level) component specifically for controlling overthinking. Case studies (Figure 4) visually confirm NeuReasoner detects failure-mode fluctuations during inference and triggers the diagnose-then-correct behavior via special-token insertion, with corresponding measurable shifts in MoN activation dynamics immediately after intervention.

## Limitations

Integrating the online-monitoring MLPs incurs inference overhead; despite implementation optimizations achieving approximately O(1) time complexity for the sliding-window feature updates, marginal latency increases persist (detailed in an appendix runtime comparison). NeuReasoner is not currently a fully automated, end-to-end pipeline -- the failure-mode detection, dataset reconstruction, and trigger-training stages require manual setup -- and the authors leave further automation of this pipeline to future work.

## Why it matters here

- **overthinking**: Directly central to the topic: instance-level overthinking (failure to calibrate reasoning depth to query difficulty) is explicitly one of the three failure modes NeuReasoner targets and names, alongside intra-step and inter-step failures it argues are mechanistically distinct but jointly responsible for wasted token cost. Its neuron-level, Fourier-domain characterization of failure-specific activation signatures is a genuinely new mechanistic account of overthinking (and its two sibling failure modes) grounded in white-box interpretability rather than only behavioral/output-level metrics, and its ablation directly demonstrating that removing the instance-level detector causes a 'drastic surge in token consumption' is strong, isolated evidence that difficulty-calibration failure is a distinct, separately-addressable cause of excess reasoning length.

## Entities

- **Concepts**: Mixture of Neurons (MoN), intra-step / inter-step / instance-level failure modes, DePass attribution, Fourier-domain fluctuation analysis (high-frequency energy ratio, spectral entropy), diagnose-then-correct trigger token, special-token-conditioned self-correction
- **Methods**: DePass attribution, Fourier transform fluctuation analysis, sliding-window online monitoring MLPs, special-token-triggered SFT self-correction, NoThinking-mode transition (instance-level intervention)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `overthinking`, `mechanistic-interpretability`, `failure-mode-detection`, `efficient-reasoning`, `self-correction`

## Abstract

Large Reasoning Models (LRMs) have recently achieved remarkable success in complex reasoning tasks. However, closer scrutiny reveals persistent failure modes compromising performance and cost: I) Intra-step level, marked by calculation or derivation errors; II) Inter-step level, involving oscillation and stagnation; and III) Instance level, causing maladaptive over-thinking. Existing endeavors target isolated levels without unification, while their black-box nature and reliance on RL hinder explainability and controllability. To bridge these gaps, we conduct an in-depth white-box analysis, identifying key neurons (Mixture of Neurons, MoN) and their fluctuation patterns associated with distinct failures. Building upon these insights, we propose NeuReasoner, an explainable, controllable, and unified reasoning framework driven by MoN. Technically, NeuReasoner integrates lightweight MLPs for failure detection with a special token-triggered self-correction mechanism learned via SFT. During inference, special tokens are inserted upon failure detection to actuate controllable remedial behaviors. Extensive evaluations across six benchmarks, six backbone models (8B 70B) against nine competitive baselines, demonstrate that NeuReasoner achieves performance gains of up to 27.0% while reducing token consumption by 19.6% 63.3%.

---

Record id: `doi:10.18653/v1/2026.acl-long.1033`
