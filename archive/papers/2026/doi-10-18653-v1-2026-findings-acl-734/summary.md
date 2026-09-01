<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Internalization Fails: Finding Better Targets for Reasoning Compression

- **Authors**: Mourad Heddaya, Manley Roberts, Rohan Wadhawan, Chenhao Tan
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.734/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.734.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.734
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

In a teacher-student distillation setup on competition-level math (NuminaMath 1.5, ~5000-token traces), ICoT-style curriculum internalization methods that work on simple/structured tasks (GSM8K, multiplication) provide little to no benefit over direct distillation; naive first-k-token truncation at inference time is also shown misleading, since models compensate by generating longer post-think text, undermining apparent token savings; distilling on the teacher's naturally-occurring post-think section (concise, answer-directed text generated after </think> but before the boxed answer) achieves the best accuracy-efficiency trade-off among all tested shortened targets, including generic teacher-generated summaries at matched token budgets.

## Problem

Reasoning models generate long chain-of-thought traces that increase latency and cost, and prior curriculum-based internalization methods (ICoT-style stepwise internalization, latent-token methods like COCONUT) have shown success at shortening reasoning while preserving accuracy, but only on simple, short, structurally homogeneous tasks (~200 tokens, GSM8K, N-digit multiplication); whether these methods scale to competition-level mathematics, where reasoning traces are long (~5,000 tokens), diverse, and exploratory, was untested.

## Contributions

- empirical demonstration that inference-time first-k truncation misleads about efficiency: models compensate for truncated visible reasoning by generating longer post-think continuation text, so total token count -- and therefore actual inference cost -- does not fall as much as truncating the 'reasoning' portion alone would suggest
- a boundary result for curriculum-based internalization methods: ICoT-style curricula and a segment-adapted COCONUT, both effective on short structured traces (GSM8K, multiplication), provide little to no benefit over direct distillation on long, diverse, exploratory competition-math traces (~5,000 tokens)
- identification of post-think -- text the teacher naturally generates after </think> but before the boxed answer -- as a superior distillation target versus generic teacher-generated summaries at matched token budgets, with discourse-connective analysis suggesting it better preserves the teacher's deductive reasoning structure

## Method

Uses a teacher-student distillation setup with reasoning traces from two teachers (DeepSeek-R1 via a NuminaMath 1.5 subsample from OpenR1-Math, and QwQ-32B on the same problem set), distilling into a base (non-instruction-tuned) Qwen2.5-7B student via LoRA SFT with early stopping on validation loss. Every teacher trace has the structure [problem] <think>[reasoning]</think> [post-think] \boxed{[answer]}, where 'post-think' is text the teacher generates naturally after the </think> token but before the final boxed answer -- a concise, answer-directed recapitulation of the solution path, distinct from a prompted external summary. Compares three families of approaches to shorten inference-time reasoning: (1) inference-time first-k truncation (append </think> after k in {50,100,250,500,1000,1500} reasoning tokens, an established baseline sweep); (2) four ICoT-style training curricula that progressively shorten the trace during training (first-k-tokens curriculum, left-to-right segment removal, random segment removal, iterative teacher-generated summarization) using paragraph-level (double-newline-delimited) segments as the removal unit since raw traces lack the fixed step structure that made token-level removal feasible for arithmetic tasks; and (3) direct distillation to a single fixed shortened target -- teacher-generated summaries at six compression levels, official human-written NuminaMath solutions, first-k-token prefixes, and post-think text. Also adapts COCONUT (replacing reasoning tokens with learned latent representations) to the longer traces by removing paragraph-level segments rather than tokens. Evaluates accuracy against total inference-time tokens generated (including any post-think continuation after the truncation point), since total tokens -- not just visible 'reasoning' tokens -- determine actual inference cost.

## Results

First-k truncation is shown to be a misleading efficiency baseline: when post-think is included in training, truncating visible reasoning to fewer tokens at inference time appears to preserve accuracy, but the student model compensates by generating substantially longer post-think text as reasoning is truncated further (post-think grows from ~1,300 to ~3,600+ tokens for DeepSeek-R1 as thinking length is cut from 1500 to 0 tokens), so total token count stays high and apparent token savings from shorter visible reasoning are largely illusory. With post-think excluded from training (isolating a clean length-accuracy trade-off), accuracy decreases monotonically and drops sharply once reasoning is removed entirely, confirming reasoning length genuinely matters for this task family (unlike GSM8K/arithmetic). None of the four ICoT-style curricula outperform the no-thinking baseline in final-stage accuracy at comparable token budgets -- curriculum choice (first-k, left-to-right, random, iterative summarization) makes little difference, and all provide little to no benefit over direct distillation despite ICoT's documented success on simple/structured tasks; the adapted COCONUT method performs even worse (4.2% accuracy vs. 8.1% for a plain no-reasoning baseline). Among direct-distillation targets, post-think achieves the best accuracy-efficiency trade-off at matched token budgets across both teachers (Table 2: DeepSeek-R1 post-think reaches 0.185 accuracy at a median 511 tokens, beating Summary-Level-3 at comparable length (0.164 acc / 453 tokens) and far outperforming official human-written NuminaMath solutions (0.090 acc / 274 tokens) despite official solutions also being answer-directed -- showing answer-directedness alone does not explain post-think's advantage). A discourse-connective analysis (comparing post-think against the best-performing generic summary, Level 3, at similar length) finds 'therefore' appears 25.8x more frequently per 10K tokens in post-think than in Level-3 summaries while overall connective density is comparable, suggesting iterative compression strips conclusive deductive markers while retaining general discourse connectives -- offered as evidence that post-think preserves the teacher's deductive/logical structure in a way generic compression disrupts. Post-think's advantage over Level-3 summaries is limited to easier problems (those requiring shorter teacher traces); neither method achieves meaningful accuracy on harder problems.

## Limitations

The study focuses exclusively on competition-level mathematics; generalization to other reasoning domains (code, scientific reasoning, commonsense) is untested and named as future work. Only 7B-parameter students are tested (other model families -- Llama, Gemma3, OLMo2 -- were found impractical for this setup and excluded), so whether larger students can internalize long traces where smaller ones cannot is unknown. Results are reported from single training runs without replication across seeds, so statistical robustness of the comparisons is not established. The segment-level adaptation of COCONUT trades token-level granularity for tractability, and alternative adaptations might yield different (better) results. The explanation for why post-think outperforms generic summaries rests on indirect evidence (the official-solutions comparison and the discourse-connective analysis) rather than a controlled experiment directly isolating the causal mechanism.

## Why it matters here

- **overthinking**: Core paper for this topic: it is a direct, carefully-controlled negative result against a widely-cited class of overthinking mitigation (curriculum-based reasoning internalization) and a methodological warning that applies to the whole archive's length-reduction literature -- naive token-truncation baselines can vastly overstate their own efficiency gains because a model 'compensates' by shifting length into a different part of its output (post-think), so any efficient-reasoning paper measuring only visible chain-of-thought length rather than total generated tokens risks the same illusion. Its identification of the naturally-occurring post-think segment as an under-exploited, structurally superior distillation target is a concrete, actionable finding for training-time overthinking mitigation that other archived papers (e.g. Distilling the Essence via Sequence Truncation, this session) address from a related but distinct angle.

## Entities

- **Concepts**: post-think (naturally-occurring answer-directed text after </think>), ICoT-style curriculum internalization, first-k-truncation compensation effect, segment-level (paragraph) removal unit
- **Methods**: post-think distillation, ICoT-style stepwise internalization curricula (first-k, left-to-right, random segment removal, iterative summarization), COCONUT (segment-adapted, baseline), first-k inference-time truncation (baseline), direct distillation to teacher-generated summaries / official solutions / first-k prefixes (baselines)
- **Datasets**: NuminaMath 1.5, OpenR1-Math (subsample pairing DeepSeek-R1 traces with NuminaMath 1.5 problems)

Tags: `overthinking`, `reasoning-compression`, `distillation`, `competition-math`, `post-think`

## Abstract

Reasoning language models generate long reasoning traces that increase latency and cost. We study how to shorten these traces while preserving accuracy on competition-level mathematics. In a teacher-student distillation setup, we compare three approaches: (i) inference-time truncation after the first k tokens, (ii) Implicit Chain-of-Thought (ICoT)-style curricula that progressively shorten the teacher trace during training, and (iii) direct distillation to shorter reasoning traces. Using NuminaMath 1.5 with traces from DeepSeek-R1 and QwQ-32B, we distill into Qwen2.5-7B and measure accuracy against total tokens generated. We find: (1) with standard SFT and first-k truncation, models compensate by generating longer text after reasoning, undermining token savings; (2) ICoT-style curricula provide little benefit on competition-level mathematics, where reasoning traces are long and diverse; and (3) training on post-think, text the teacher generates after reasoning, achieves the best accuracy–efficiency trade-off among all shortened targets, outperforming generic summaries at matched token budgets. These results show that curriculum-based internalization methods effective on simple tasks do not transfer to complex reasoning, and that post-think provides a better distillation target.

---

Record id: `doi:10.18653/v1/2026.findings-acl.734`
