<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# NEAT: Neuron-Based Early Exit for Large Reasoning Models

- **Authors**: Kang Liu, YongKang Liu, Xiaocui Yang, Peidong Wang, Wen Zhang, Shi Feng, Yifei Zhang, Daling Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1231/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1231.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1231
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## In one line

NEAT identifies a sparse set of 'exit-associated neurons' whose FFN activation dynamics causally predict the </think> termination token, then monitors these neurons training-free during inference to trigger graded early exit or reflection suppression -- cutting average token generation 22-28% across four benchmarks and six models with accuracy comparable to vanilla decoding, and 21-23% real wall-clock latency reduction versus vanilla and CGRS (which is 41-63% slower than vanilla despite shortening output, due to its own scoring overhead).

## Problem

Large reasoning models continue generating reasoning steps after a correct solution has already been reached (overthinking), raising compute cost, latency, and risk of hallucination/error accumulation in the generation tail; existing early-exit methods either require repeated rollouts and answer-convergence checks (increasing parallel test-time computation and latency) or require training external probes on labeled hidden-state data (extra supervision and a persistent performance gap versus mature output-based approaches).

## Contributions

- NEAT, a training-free early-reasoning-exit framework that monitors neuron-level (rather than output- or hidden-state-level) activation dynamics to detect internal reasoning convergence, requiring no external supervision, extra forward passes, or parallel rollouts
- a neuron identification procedure combining causal attribution to the termination token with temporal filtering (concentration and consistency of late-stage activation) to isolate a sparse, reliable exit-signaling neuron subset
- a graded, three-way (terminate / suppress-reflection / continue) intervention policy that reduces the premature-exit risk of hard-threshold methods
- empirical results across six models and four benchmarks showing 22-28% average token reduction with accuracy comparable to vanilla decoding, and a wall-clock latency finding that a competing output-based method (CGRS) is actually 41-63% *slower* than vanilla despite generating fewer tokens, due to its own per-step overhead

## Method

Attributes each FFN-layer neuron's causal contribution to predicting the termination token (e.g. </think>) via a log-probability increase method (adding the neuron's contribution to the residual stream and measuring the resulting increase in termination-token probability), retaining the top-k candidates. Applies temporal filtering across each candidate's activation trajectory over a calibration set, computing a Relative Center of Mass (where along the trace activation concentrates) and Activation Entropy (temporal dispersion); neurons with high center-of-mass (late-stage activation) and low entropy (focused, consistent activation) are selected as the final 'exit-associated neuron' set. At inference, the activation vector of this fixed neuron set is compared at each decoding step against a reference pattern (averaged from the calibration set at true termination points) via cosine similarity (rho, directional alignment) and relative magnitude (phi); a hierarchical intervention policy then acts based on these two signals: strong alignment (rho and phi both above high thresholds) triggers immediate termination (append </think>); moderate alignment triggers suppression of a predefined set of reflection tokens (setting their logits to -infinity) without forcing exit; weak alignment leaves decoding unaffected. The whole framework requires no additional supervised training, no extra forward passes, and no parallel sampling -- only monitoring internal activations already computed during normal decoding.

## Results

Across four benchmarks (MATH500, AMC23, AIME24, GPQA-Diamond) and four models (DeepSeek-R1-Distill-Qwen-7B/Llama-8B, Qwen3-8B/14B), NEAT achieves the best average result of all compared methods, reducing token generation 22.0-28.2% while maintaining accuracy comparable to (in several cases nominally exceeding) vanilla decoding -- e.g. DeepSeek-R1-Distill-Qwen-7B: 71.7% accuracy (vs. vanilla's 71.2%) at 22.0% length reduction; Qwen3-8B: 77.2% accuracy (vs. vanilla's 75.7%) at 16.8% length reduction, the best average accuracy of any method on that model. Output-based heuristic baselines (DEER, CGRS) show substantial cross-model variance and calibration sensitivity: DEER achieves aggressive 41.7%-average compression on better-calibrated models like Qwen3 but at accuracy cost (AIME24/Qwen3-8B: 61.1%->45.6%, a 15.5-point drop), and on GPQA-D with Llama-8B, DEER/CGRS reduce accuracy 7.5/9.7 points while achieving under 6% length reduction (indicating premature or ineffective exits) -- NEAT's graded (suppress-then-exit) intervention strategy consistently preserves accuracy better than these direct/aggressive termination methods. Inference-latency measurement on AIME2024 across Qwen3 model scales (4B/8B/14B) shows CGRS actually *increases* wall-clock latency 41-63% versus vanilla decoding despite reducing token count, because its confidence-estimation scoring overhead outweighs the savings from shorter output; NEAT, which requires no extra forward passes or scoring modules, achieves consistent 21-23% latency *reductions* across all three model scales -- direct evidence that shorter generation and lower latency are not automatically the same thing for methods with heavy per-step overhead. Ablations on MATH500/DeepSeek-R1-Distill-Qwen-7B isolate the two intervention mechanisms: suppression-only with moderate threshold (tau_sup=0.6) improves accuracy over vanilla (92.2%->93.4%) while reducing tokens (3743->3485), but overly strong suppression (tau_sup=0.2) harms accuracy (89.6%), showing excessive interference can disrupt valid reasoning even without forcing hard exits; exit-only with a low similarity threshold (tau_sim=0.4) achieves the most aggressive compression (2287 tokens) but at accuracy cost (87.2%), while higher thresholds better preserve accuracy with smaller savings -- combining both mechanisms (the default configuration) achieves the reported balance. A comparison of exit-signal types on MATH500 shows neuron-based signals (NEAT, or a naive top-activated-neuron baseline) outperform both logit-based signals (Wait/</think>/Answer-confidence heuristics, which lag vanilla accuracy and still incur overhead) and hidden-state-based signals (similarity/probe methods, which achieve large length reductions but at substantial accuracy loss from premature exits) -- a random-neuron control performs poorly, confirming exit-relevant signal is concentrated in a sparse, specific neuron subset rather than distributed generally.

## Limitations

The paper does not discuss limitations in the excerpted sections beyond what is implicit in its design: the exit-associated neuron set and reference activation pattern are derived from a calibration set (a sampled subset of the MATH training split) and held fixed during inference, so the method's reliability depends on this calibration set being representative; sensitivity analysis shows the number of monitored neurons matters differently across models (Qwen3-8B degrades noticeably with too few neurons before stabilizing, while DeepSeek-R1-Distill-Qwen-7B is far more robust to this choice), indicating some model-specific tuning may be needed.

## Why it matters here

- **overthinking**: Directly and centrally relevant: it names overthinking explicitly and locates the exit signal at the neuron level rather than the output or hidden-state level, and its case study (Figure 5) is a clean worked example of the phenomenon this archive studies throughout -- a model reaches the correct answer, then spends hundreds more tokens on unproductive reflective/confirmatory steps with no new information and no change to the answer. Its wall-clock-latency finding (a competing method that shortens output but is slower in practice due to scoring overhead) is a concrete methodological caution for evaluating any overthinking-mitigation method: token count is not latency.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), exit-associated neurons, neuron-level causal attribution, temporal filtering (Center of Mass / Activation Entropy), graded (hierarchical) intervention strategy, reflection suppression
- **Methods**: NEAT (neuron-based early exit), [NoThinking (baseline)](../../../../wiki/methods/nothinking-baseline.md), TALE (baseline), Dynasor (baseline), [DEER (baseline)](../../../../wiki/methods/deer-baseline.md), CGRS (baseline), vLLM (inference framework)
- **Datasets**: [MATH500](../../../../wiki/datasets/math500.md), [AMC23](../../../../wiki/datasets/amc23.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), MATH (calibration split)

Tags: `overthinking`, `early-exit`, `mechanistic-interpretability`, `training-free`, `inference-latency`

## Abstract

Large Reasoning Models (LRMs) often suffer from overthinking, a phenomenon in which redundant reasoning steps are generated after a correct solution has already been reached. Existing early reasoning exit methods primarily rely on output-level heuristics or trained probing models to skip redundant reasoning steps, thereby mitigating overthinking. However, these approaches typically require additional rollout computation or externally labeled datasets. In this paper, we propose NEAT, a Neuron-based Early reAsoning exiT framework that monitors neuron-level activation dynamics to enable training-free early exits, without introducing any additional test-time computation. NEAT identifies exit-associated neurons and tracks their activation patterns during reasoning to dynamically trigger early exit or suppress reflection, thereby reducing unnecessary reasoning while preserving solution quality. Experiments on four reasoning benchmarks across six models with different scales and architectures show that, for each model, NEAT achieves an average token reduction of 22% to 28% when averaged over the four benchmarks, while maintaining accuracy.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1231`
