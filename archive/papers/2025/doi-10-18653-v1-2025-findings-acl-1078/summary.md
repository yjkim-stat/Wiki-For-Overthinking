<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Disentangling Reasoning Tokens and Boilerplate Tokens For Language Model Fine-tuning

- **Authors**: Ziang Ye, Zhenru Zhang, Yang Zhang, Jianxin Ma, Junyang Lin, Fuli Feng
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.findings-acl.1078/>
- **PDF**: <https://aclanthology.org/2025.findings-acl.1078.pdf>
- **DOI**: 10.18653/v1/2025.findings-acl.1078
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

SHAD automatically separates a training sample's tokens into 'reasoning' (sample-specific, hard to predict) versus 'boilerplate' (repetitive, format/template) tokens by fine-tuning on a small shuffled-input-output subset and comparing per-token loss before/after, and the resulting Reasoning-highlighted Fine-Tuning (RFT) -- which adaptively up-weights reasoning tokens during agent SFT -- outperforms SFT, regex-based weighting, and two other token-differentiation baselines on held-in and held-out agent benchmarks.

## Problem

When fine-tuning LLMs on agent-task datasets (multi-step planning, tool use), standard supervised fine-tuning treats every token in a sample's loss equally, even though a sample mixes 'boilerplate' tokens (repetitive format/template phrasing like 'Based on the user's request... By doing so...') with 'reasoning' tokens (sample-specific problem-solving content) -- causing the model to overfit to easy, repetitive boilerplate while underlearning harder, more important reasoning content.

## Contributions

- an argument, with empirical loss-curve evidence, that treating all fine-tuning tokens equally causes overfitting to repetitive boilerplate content and underlearning of sample-specific reasoning content in agent-task data
- SHAD, an automated method for classifying tokens as reasoning versus boilerplate by comparing per-token loss before and after fine-tuning on a small input-output-shuffled data subset, validated to under 3% classification error on manually-annotated tokens
- Reasoning-highlighted Fine-Tuning (RFT), an adaptive loss-reweighting scheme built on SHAD's classification that outperforms SFT and several other token-differentiation baselines (Regex, Rho-1, RewardFT) across held-in and held-out agent benchmarks and across model scales/families

## Method

SHuffle-Aware Discriminator (SHAD) classifies tokens in three steps: (1) sample a small fraction (1%) of the training data and shuffle the pairing between inputs and outputs across samples, so the boilerplate (sample-independent, template-like) parts of an output remain predictable from the mismatched input while reasoning (sample-specific) parts become noisy/unpredictable; (2) fine-tune the LLM on this shuffled subset; (3) for each token in a target sample, compare its prediction loss under the shuffle-tuned model versus the original model -- a token is classified boilerplate if its loss decreases after shuffle-tuning (meaning it stayed learnable despite the shuffle) and reasoning otherwise. Reasoning-highlighted Fine-Tuning (RFT) then re-weights the standard fine-tuning loss per sample using a softmax over the average reasoning-token loss versus average boilerplate-token loss (temperature tau), so the token type with currently higher average loss (typically reasoning) receives proportionally more weight, adaptively rather than via a fixed weighting. Trains LLaMA3-8B and LLaMA3.1-8B on a mixture of ToolBench and APIGen (agent tool-use data) plus ShareGPT (general instruction data), evaluated held-in on StableToolBench and BFCL and held-out on T-eval and Nexus, against SFT, Regex-based token weighting, Rho-1 (reference-model-based noise-token masking), and RewardFT (DPO-based token-level reward re-weighting), plus two SHAD/RFT ablation variants (SHAD+alpha-FT with a fixed reasoning weight; Regex+RFT using regex instead of SHAD for token classification).

## Results

SHAD+RFT achieves the best average performance on both backbones (LLaMA3-8B: 59.3 avg vs. 52.5 SFT, 44.5 Regex, 48.7 Rho-1, 52.0 RewardFT; LLaMA3.1-8B: 60.0 avg vs. 55.4 SFT, 49.3 Regex, 52.0 Rho-1, 55.5 RewardFT), winning on every held-in/held-out benchmark except BFCL with LLaMA3-8B (where it places second, 87.6 vs. Rho-1's 89.3). Both SHAD and RFT are shown to be individually necessary: replacing SHAD's adaptive classification with Regex (Regex+RFT) drops average performance to 49.6/50.2 (below plain SFT in some cases), and replacing RFT's adaptive weighting with a fixed weight (SHAD+alpha-FT) drops average performance to 57.9/57.5 -- both below full SHAD+RFT, confirming the adaptive mechanism (not just the token classification) contributes independently. A manual quantitative accuracy check of SHAD's token classifications (on the subset of tokens that could be manually annotated) shows a classification error rate below 3%. Training-loss analysis (Figure 6) shows RFT reduces loss specifically on reasoning tokens relative to SFT while keeping boilerplate-token loss comparable, confirming RFT redirects learning capacity toward reasoning as intended rather than merely reweighting overall loss. A temperature (tau) sweep shows performance is robust across 1/tau in [0.2, 0.5] but degrades if the reweighting is pushed too aggressively (1/tau far from this range), and SHAD+RFT outperforms most baselines across the whole tested range regardless of exact tau. The method's benefit is shown to generalize across model scale (LLaMA 3.2 3B, appendix) and model family (Qwen, appendix), continuing to outperform SFT.

## Limitations

The method's effectiveness depends on boilerplate tokens remaining reasonably consistent across different training samples; where boilerplate diversity is high, the shuffle-based predictability signal SHAD relies on may fail. The reasoning/boilerplate distinction is based on a loss-difference threshold rather than a principled boundary, which can occasionally misclassify tokens -- in an extreme failure case, misclassifying most reasoning tokens as boilerplate (near-zero weight) or vice versa could weaken the model's reasoning ability or destabilize training, though this was not observed in the reported experiments. The re-weighting strategy currently operates at the token-type group level (reasoning vs. boilerplate, per sample) rather than at the individual-token level, which the authors flag as a direction for future refinement. As with any fine-tuning approach, the method could reinforce biases already present in the training data, particularly around reasoning patterns and tool-usage decisions, a risk the authors say needs further investigation.

## Why it matters here

- **overthinking**: Relevant to a training-side, rather than inference-side, angle on the topic: it operationalizes a distinction directly relevant to overthinking -- that a reasoning trace contains tokens of very different importance (sample-specific reasoning work versus repetitive, low-information boilerplate/template phrasing) -- and shows that failing to distinguish them during training causes the model to overfit to the easy, low-value boilerplate. This is complementary to inference-time overthinking mitigation: if boilerplate/filler content is a substantial fraction of what a verbose reasoning trace contains, a method like SHAD's shuffle-based discriminator could in principle be repurposed to identify and prune that content, rather than only to reweight it during fine-tuning.

## Entities

- **Concepts**: reasoning tokens vs. boilerplate tokens, shuffle-aware token predictability discrimination, adaptive (softmax-based) loss re-weighting, reasoning-highlighted fine-tuning
- **Methods**: SHuffle-Aware Discriminator (SHAD), Reasoning-highlighted Fine-Tuning (RFT), Regex-based token weighting (baseline), Rho-1 (reference-model noise masking, baseline), RewardFT (DPO-based token-level reward, baseline)
- **Datasets**: ToolBench, APIGen, ShareGPT (general data), StableToolBench, BFCL, T-eval, Nexus

Tags: `overthinking`, `token-level-supervision`, `agent-fine-tuning`, `reasoning-vs-boilerplate`, `adaptive-reweighting`

## Abstract

When using agent-task datasets to enhance agent capabilities for Large Language Models (LLMs), current methodologies often treat all tokens within a sample equally. However, we argue that tokens serving different roles—specifically, reasoning tokens versus boilerplate tokens (e.g., those governing output format)—differ significantly in importance and learning complexity, necessitating their disentanglement and distinct treatment. To address this, we propose a novel Shuffle-Aware Discriminator (SHAD) for adaptive token discrimination. SHAD classifies tokens by exploiting predictability differences observed after shuffling input-output combinations across samples: boilerplate tokens, due to their repetitive nature among samples, maintain predictability, whereas reasoning tokens do not. Using SHAD, we propose the Reasoning-highlighted Fine-Tuning (RFT) method, which adaptively emphasizes reasoning tokens during fine-tuning, yielding notable performance gains over common Supervised Fine-Tuning (SFT).

---

Record id: `doi:10.18653/v1/2025.findings-acl.1078`
