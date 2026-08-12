<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models

- **Authors**: Andres Algaba, Francesca Carlon, Lynn Delcon, Marthe Ballon, Bert Verbruggen, Vincent Ginis
- **Venue**: cs.LG
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02089>
- **PDF**: <https://arxiv.org/pdf/2608.02089v1>
- **Topics**: reasoning-faithfulness
- **Relevance score**: reasoning-faithfulness 0.40, test-time-scaling 0.25

## In one line

Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.

## Problem

Commercial deployments show a final answer and a short reasoning summary while the full trace stays hidden, but the evidence that reasoning traces reveal errors or misbehaviour was gathered from full traces. That leaves the practically important question unanswered: what can a reader actually learn from what is displayed? The question has a second half that is usually left implicit — any answer depends on who is reading, since a weak probe and a capable model reader will extract different amounts from the same text.

## Contributions

- An observability ladder that fixes the completed run and the correctness label and varies only the inspected evidence, so differences are attributable to access rather than to different runs
- A prompt-withheld contrast run alongside the prompt-visible one, which shows that response-only baselines overstate what summaries add
- Length-matched comparisons between model-written summaries and deterministic extracts from the trace at the same word count
- A within-item repeated-run analysis that removes question-level cues, isolating whether a display distinguishes a correct from an incorrect run of the same question
- A reader contrast, comparing linear probes against a capable model reader on identical displays
- The framing conclusion that a monitorability claim, faithfulness claims included, has to name the monitored property, the access level, prompt visibility and the reader

## Method

For each benchmark item and target model, one completed run yields the prompt, the full trace, the visible final response and a binary correctness label. The same model then writes a self-summary from the trace alone under an instruction requesting at most 90 words — a controlled stand-in for a provider summary. Displays are formed by concatenation: prompt plus response, then adding the summary, then the trace, and finally provider-side replay features (answer-probability features and the last-layer hidden state at the final token). A matched prompt-withheld ladder repeats this without the prompt. Readers are L2-regularized logistic probes over surface features — word and sentence counts, digit and mathematical-symbol density, and rates of uncertainty, self-correction and answer-framing markers — concatenated with a 512-dimensional text embedding, scored by AUROC on held-out items, with all seven subsets of response, summary and trace fitted separately and Shapley attribution used to allocate predictive performance among them. A GPT-5-mini reader with a fixed judge instruction evaluates the same displays. Controls include an open TF-IDF feature family, label permutation, masking of stated answers and option text, removal of question-copied spans, chunked re-reading, a generic summary instruction, sampled versus greedy summary decoding, and length adjustment. Five open-weight models (Qwen3-4B/8B/14B, gpt-oss-20b and 120b) cross three benchmarks (GPQA-Diamond, MMLU-Pro, Omni-MATH-2-Filtered) for 15 settings.

## Results

With the prompt withheld, the summary is genuinely useful: summary-only AUROC averages 0.774 against 0.813 for the full trace, and adding the summary to the response gains +0.156. With the prompt visible, that same increment collapses to +0.019 — a paired difference of -0.137 (95% interval [-0.177, -0.095]) — because a prompt-only reader already reaches 0.734, so most of what the summary contributes is question difficulty the prompt already states. The trace increment is stable across both conditions (+0.035 withheld, +0.041 visible), so what the trace adds is run-specific in a way the summary's contribution is not. At equal word count the summary loses its advantage entirely: the final 90 words of the trace score 0.780 against the summary's 0.774, rising to 0.804 for the strongest last-word extracts against 0.778 for the uncapped summary, a paired +0.025. Those extracts carry denser marker content — uncertainty +0.009, self-correction +0.012 and answer markers +0.051, all with intervals excluding zero — so the model-written summary is not adding discriminative cues the trace's own ending lacks. The repeated-run analysis is the sharpest negative: on outcome-discordant MMLU-Pro items, linear summary readers sit at within-item AUROC 0.503-0.545, essentially chance, while trace displays retain 0.544-0.590. Reader choice then reverses part of the picture — GPT-5-mini with the prompt withheld reaches 0.649 on summaries and 0.683 on traces against 0.503 on the response, recovering signal the linear readers miss while keeping the trace slightly ahead. Length explains much of the linear readers' trace advantage: trace word count alone reaches within-question 0.553 against 0.567 for the full trace reader, and after adjusting for word and sentence counts the trace-minus-summary contrast turns slightly negative (+0.043 to -0.024), though restricting to pairs whose lengths differ by at most 20% leaves the trace +0.032 ahead. In selective-risk terms at 50% coverage, error falls from 0.243 with the response alone to 0.139 with the summary, 0.114 with the trace and 0.098 with internals.

## Limitations

The paper names four. The summaries are a controlled proxy — the same model, one instruction, no content filter and no incentive to evade a monitor — so the estimates describe this summary method rather than deployed provider summaries or adversarial ones. The claims are reader-relative: most estimates use simple linear readers, the stronger-reader test covers one judge on one model and benchmark, and monitors fitted in one setting transfer imperfectly. The ladder measures final-answer correctness only, and the authors state plainly that nothing here shows a trace or summary is a causal account of the model's computation, so extending the design to faithfulness or misbehaviour needs labels defined independently of correctness. And length is entangled with the linear readers' signal in a way the adjustments show but do not disentangle — the paper says the unadjusted and adjusted results should be read together, with neither isolating a length-independent semantic effect. Two further bounds a reader should note: the repeated-run analysis runs on MMLU-Pro alone, on an unusually difficult discordant subset whose primary-run accuracy is 23 to 30 points below the held-out pool with traces 2.5 to 3 times longer, and the GPT-5-mini comparison mixes monitoring with task solving, since that model can attempt the question itself.

## Why it matters here

- **reasoning-faithfulness**: It supplies the missing qualifier for every monitorability and faithfulness claim in this archive: a claim about what a trace reveals is not well formed until it names the property monitored, what the reader could see, whether the prompt was among it, and who the reader was. Each of those changes the answer materially here — the summary's contribution moves by 0.137 AUROC on prompt visibility alone, and switching from a linear probe to a capable model reader moves summary discrimination from chance to 0.649 on the same text. Two results bear directly on the archive's existing work on monitorability. First, a provider-style summary is worth little to a monitor who already holds the question, and at matched length the trace's own last ninety words do the same job or better while carrying denser uncertainty and self-correction markers — so redacting the trace to a summary costs the specific cues monitoring depends on. Second, the honest scope: the ladder scores final-answer correctness, and the authors decline to claim it measures whether the trace describes the computation, which is exactly the distinction the archive's causal-intervention work is built to test.

## Entities

- **Concepts**: [monitorability](../../../../wiki/concepts/monitorability.md), [chain-of-thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md), reasoning summary, observability, correctness prediction, selective prediction, [self-correction](../../../../wiki/concepts/self-correction.md), verbosity, AUROC
- **Methods**: observability ladder, [linear probe](../../../../wiki/methods/linear-probe.md), Shapley attribution, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), TF-IDF, logistic regression
- **Datasets**: [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), [Omni-MATH](../../../../wiki/datasets/omni-math.md)

Tags: `monitorability`, `faithfulness`, `reasoning summaries`, `evaluation`, `probing`

## Abstract

Large language models often show users a final response and a short reasoning summary while the full reasoning trace stays hidden. We introduce an observability ladder that holds each completed run fixed and varies only what a reader inspects to judge whether the answer is correct: the response, a self-summary the model writes from the trace, the trace itself, and internal signals, each with and without the prompt. Across three benchmarks and five open-weight Qwen3 and gpt-oss models, we train matched linear correctness predictors on each access level. Without the prompt, summaries carry most of the trace's ranking signal (mean AUROC 0.774 versus 0.813) and add +0.156 over the response alone. With the prompt visible, the summary's gain collapses to +0.019, while the trace still adds +0.041. Even at equal length, the trace's last words predict correctness as well as summaries, or slightly better, and carry denser and more discriminative uncertainty and self-correction cues. On MMLU-Pro questions with both correct and incorrect runs, linear summary readers are near chance and trace readers retain only modest signal, both with and without the prompt (prompt-withheld AUROC 0.503-0.545 versus 0.544-0.590). With the prompt withheld, a GPT-5-mini reader recovers substantially more signal from both summaries and traces on gpt-oss-20b, and even then the trace keeps a small +0.034 advantage. Much of the linear readers' trace signal is associated with length. In the common case where users already hold the prompt, summaries are less helpful than the full trace for monitoring correctness. Monitorability is thus a joint property of the display and the reader, so any monitorability claim, including for faithfulness, should specify both.

---

Record id: `arxiv:2608.02089`
