<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models

- **Authors**: Sara Candussio, Daniel Scalena, Luca Bortolussi, Elisabetta Fersini, Malvina Nissim, Gabriele Sarti
- **Venue**: cs.CL
- **Published**: 2026-07-30
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2607.28707>
- **PDF**: <https://arxiv.org/pdf/2607.28707v2>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A controlled re-evaluation of entropy-based chain-of-thought compression showing that low- and high-entropy selection never beats random pruning once a random baseline is included, and that the one apparent exception on math benchmarks is caused by numeric tokens rather than by entropy.

## Problem

Several lines of work prune chain-of-thought traces by token or sentence entropy, and they disagree in both directions: some retain low-entropy items as the semantic content, others discard them as redundant, others discard high-entropy items as noise. Almost all of that work evaluates on mathematical benchmarks and almost none compares against random pruning, so it is not established whether entropy identifies anything, or whether generic compression at the same rate would do as well.

## Contributions

- Supplies the random-pruning baseline that the entropy-compression literature almost entirely omits, and shows entropy selection does not beat it at sentence level in any of six models across three families and four datasets.
- Explains the one setting where low-entropy token selection does help — mathematical benchmarks — as an artifact of numeric tokens being low-entropy by vocabulary constraint, verified by a 'numbers' selector that matches or exceeds it and a 'low-entropy-no-numbers' selector that falls below random.
- Uses layer-wise activation patching as a causal probe: restoring original activations at 10-20% of positions recovers near-full-trace accuracy for content-bearing tokens, while structural, high-entropy and non-numeric low-entropy positions show no comparable recovery.
- Concludes that task information in a reasoning trace is distributed across the chain rather than concentrated at heuristically identifiable positions.
- Reconciles the contradictory prior claims (pruning low-entropy vs. pruning high-entropy both reported as beneficial) by showing both effects are reproduced but random achieves the same at equal or higher compression.

## Method

The thinking region C of a trace is the span between the model's begin- and end-of-thinking markers. A selector s ranks candidate units (sentences or tokens) inside C; units are added in ranked order until a budget b = max(1, min(r|C|, |C|)) is reached at retention rate r, then re-ordered into their original positions to give a compressed trace. The compressed trace is re-wrapped as prompt + [BOT] + compressed + [EOT] + answer-elicitation suffix (default 'Therefore, the answer is \boxed{'), and the answer is greedily decoded within 64 tokens, so the model must rely on the compressed reasoning alone. Token entropy is Shannon entropy of the next-token distribution restricted to the top-k=20 log-probs returned at generation time (a vLLM constraint); sentence entropy is the mean token entropy, with sentences split on a period followed by whitespace. Selectors: low-entropy, high-entropy, numbers (fraction of tokens containing a digit), low-entropy-no-numbers (mean entropy excluding numeric tokens), random, and at token level also newlines and end-of-sentence markers. Two protocols: unpatched, where the compressed text is fed as a fresh prompt and all activations are recomputed; and patched, where residual-stream activations from a forward pass over the full uncompressed trace are cached per layer (via NNsight) and written into the retained positions at every layer during generation, so the text is identical but the activations are the originals. Scoring is relative performance retention (RPR = accuracy under compression / full-CoT accuracy) by exact match, summarized as area under the RPR-vs-retention curve; the reported statistic is delta-AUC = AUC(selector) - AUC(random), with 95% bootstrap confidence intervals.

## Results

Six models across three families (gpt-oss-20b, gpt-oss-120b, gemma-4-E4B-it, gemma-4-26B-A4B-it, Qwen3-4B, Qwen3-14B) on AIME 2024/2025/2026, MATH-500 subsets (100/50/50 questions), ZebraLogic and GPQA-Diamond; 8 traces per prompt at temperature 0.7, top-p 0.9, 16,384 max new tokens, traces not reaching [EOT] discarded; retention rates from 0.01 to 0.9. Sentence level: random dominates both entropy selectors everywhere tested. On gpt-oss-20b / AIME25 at compression >= 0.5, random keeps 78-90% of full-CoT accuracy while low-entropy is at 40-79% and high-entropy at 60-89%. In the AUC table, random's AUC is 0.83-0.93 on AIME25 and 0.88-0.97 on ZebraLogic; delta-low is within noise of zero for four of six models on AIME25 but -0.124 (gemma-4-26B) and -0.129 (gpt-oss-20b) for the other two, and negative for five of six models on ZebraLogic; delta-high is negative in every one of the twelve cells (-0.056 to -0.082 on AIME25). Token level: low-entropy does beat random, but only on mathematical benchmarks, and the paper attributes this to numeric tokens having low entropy because a digit position offers only ten choices. The test separates the two: with patching, 'numbers' alone recovers near-full-trace accuracy at 10-20% retention and exceeds low-entropy, while 'low-entropy-no-numbers' falls below random on MATH-500 and high-entropy shows no benefit from patching at all. Purely structural selectors do not benefit from patching either (mean delta-AUC -0.74 for newlines and -0.73 for end-of-sentence on AIME25, worse than their unpatched versions). On GPQA-Diamond every selector, patched or not, is level with random. Patched low-entropy holds RPR >= 0.9 at 20-30% retention versus 50-70% unpatched. The paper reproduces the prior reports that pruning can raise accuracy above the full trace, but shows random selection does the same at equal or higher compression. Appendix B repeats the analysis with a semantic verifier instead of exact match and reports the same trends. All results are software measurements; no latency or hardware numbers are reported.

## Limitations

Stated: six open-weight models up to 120B, no closed models and none from the DeepSeek family whose training recipe might behave differently; benchmarks are all reasoning tasks; the AIME subsets are 50-100 questions and the 16,384-token generation cap (with over-budget traces discarded) may understate the variance of the reported gaps; retention rates are fixed post-hoc and are not comparable across traces of different length. The authors are explicit that activation patching is a diagnostic, not a deployable compression method, since it needs a full-precision forward pass over the uncompressed trace — the very computation compression is meant to avoid. Beyond the stated: entropy is computed over the top-20 log-probs rather than the full distribution, which compresses the high-entropy end where the disputed 'forking token' signal is supposed to live. The compression protocol re-prompts with a fixed answer-elicitation suffix and a 64-token answer budget, so it measures whether a truncated trace still supports the answer, not whether a model generating under a shorter budget would reason differently. The delta-AUC values quoted for the pattern-based selectors (-0.74, -0.73) are on a different scale from the sentence-level table (-0.001 to -0.129) without an explanation in the text.

## Why it matters here

- **overthinking**: Directly on topic, and it is the kind of paper that changes what we should accept from the rest of the batch. A large share of trace-shortening work — including early-exit and pruning methods we track — rests on the premise that entropy marks where the reasoning actually happens: low-entropy tokens are filler, high-entropy tokens are decision points. This paper adds the random baseline that was missing and finds the premise does not survive it: at sentence level, random pruning matches or beats both entropy directions in all 12 model-dataset cells tested, and the token-level exception is traced to numeric tokens rather than entropy (the 'numbers' selector recovers near-full accuracy at 10-20% retention while 'low-entropy-no-numbers' drops below random). It also reproduces the widely cited result that pruning can raise accuracy above the full trace, and shows random does it too — so that finding is evidence that traces contain removable length, not evidence that any particular heuristic knows which part is removable. The practical consequence for our topic: reported compression ratios are only meaningful against random at the same ratio, and a method claiming to identify redundant reasoning must beat chance before its mechanism story is worth reading. The patching experiment adds a positive claim we should carry: task information is distributed across the chain rather than concentrated at heuristically findable positions, which sets a limit on how far position-selection methods can go.

## Entities

- **Concepts**: [Chain-of-Thought Compression](../../../../wiki/concepts/chain-of-thought-compression.md), Token Entropy, Forking Tokens, Random Baseline, Activation Patching, Relative Performance Retention, Distributed Reasoning Information, Confounded Heuristics
- **Methods**: entropy-based CoT pruning (low-entropy / high-entropy selection), random pruning baseline, numbers and low-entropy-no-numbers selectors, residual-stream activation patching, NNsight, relative performance retention (RPR) and delta-AUC, bootstrap confidence intervals, gpt-oss-20b/120b, gemma-4-E4B-it, gemma-4-26B-A4B-it, Qwen3-4B/14B
- **Datasets**: [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [AIME 2026](../../../../wiki/datasets/aime-2026.md), MATH-500 (subsets of 100/50/50), [ZebraLogic](../../../../wiki/datasets/zebralogic.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `cot-compression`, `entropy`, `negative-result`, `activation-patching`, `reproducibility`, `efficient-reasoning`, `random-baseline`

## Abstract

Entropy-based pruning has been proposed as an effective method for compressing Chain-of-Thought (CoT) reasoning with negligible accuracy loss. We test the robustness of low- and high-entropy CoT step selection methods across various models and reasoning tasks, showing that entropy offers no advantage over random pruning in any evaluated setting. Moving from sentences to tokens, we then show that retaining low-entropy tokens seems effective only on mathematical benchmarks. We find this is due to the inherently low-entropy nature of numeric tokens, which also convey semantic content in such problems. Finally, we demonstrate that patching a subset of a few CoT tokens with their original activations recovers near-perfect full-trace performance, providing causal evidence that task information is not concentrated in a small set of CoT tokens identifiable by heuristics, but rather distributed across the full reasoning chain.

---

Record id: `arxiv:2607.28707`
