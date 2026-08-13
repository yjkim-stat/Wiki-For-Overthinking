<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve

- **Authors**: Denys Pushkin, Albert Q. Jiang, Aryo Lotfi, Colin Sandon, Emmanuel Abbé
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03550>
- **PDF**: <https://arxiv.org/pdf/2608.03550v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.40, test-time-scaling 0.25

## In one line

Finds that few-shot chain-of-thought prompting with dataset examples now performs worse than simply asking a reasoning-specialized model the question — 74.2% against 86.1% on GSM8K for one model — so the field's standard baseline systematically understates modern models and overstates anything benchmarked against it.

## Problem

Chain-of-thought prompting was introduced to elicit step-by-step reasoning from models that would otherwise answer directly, and few-shot CoT with human-written examples drawn from the dataset remains the standard baseline in official model releases. But models trained heavily on multi-step reasoning traces now produce that style natively, which makes the premise worth re-testing: if the behaviour no longer needs eliciting, the demonstrations may be imposing costs — style adaptation, formatting compliance, and contextualization from examples that are merely adjacent rather than relevant — without providing the benefit they were designed for.

## Contributions

- A controlled comparison that isolates the effect of the reasoning format by using randomly selected in-context examples throughout, so retrieval and example-selection quality cannot confound it
- Four prompting variants crossed with two answer-extraction methods, which separates reasoning quality from formatting compliance
- The finding that the apparent benefit of adding more few-shot examples under rule-based extraction is almost entirely an extraction artifact — the underlying solutions are unchanged
- Evidence that model-generated examples beat dataset examples, and that a light zero-shot CoT prefix on top of them is the strongest variant tested
- An explicit argument that the standard evaluation protocol should change, since methods are routinely benchmarked against a baseline that hinders the models it is applied to

## Method

Three mid-sized models spanning specialization levels — one tuned for multi-step mathematics, one general with reported reasoning improvements, and one general without reasoning optimization — are evaluated on GSM8K under greedy decoding, with every reported number averaged over ten runs with different random seeds so example sampling is not a source of noise. Prompting variants are dataset-drawn few-shot examples with and without answer-format instructions, and model-generated few-shot examples produced either free-form or under a zero-shot CoT prompt, retaining only those whose final answers are correct. Two answer-extraction methods are crossed against the dataset-based variants: a rule-based heuristic that searches for the dataset's answer pattern, and an instruction that the model return only the final number. Baselines are zero-shot free-form generation and zero-shot CoT. A two-stage cleaning procedure for the model-generated examples — truncating after the solution and filtering logically incomplete ones — is evaluated separately.

## Results

For the reasoning-specialized model, every dataset-based few-shot configuration lands at or below 74.2% while zero-shot free-form generation reaches 83.8% and zero-shot CoT 86.1% — a gap of nearly twelve points in favour of giving the model no examples at all. The same ordering holds for the stronger general model (84.5% at best few-shot against 88.6% and 90.9% zero-shot). The third model is the honest exception and the paper reports it as such: for the general model without reasoning tuning, zero-shot free-form generation collapses to 67.3%, below its few-shot results, and only zero-shot CoT (81.4%) beats them — so the claim is about reasoning-specialized models, not about few-shot prompting universally. The methodological result is the sharper one. Under rule-based extraction, dataset-based few-shot accuracy appears to improve substantially with more examples (3.0% to 81.1% for one model from one to sixteen shots), but the invalid-answer rate falls from 96.5% to 4.6% over the same range while the underlying solutions are identical — with prompt-based extraction the same configurations sit stably in the low eighties throughout and even decline slightly with more examples. What looks like more demonstrations producing better reasoning is more demonstrations producing parseable output. Model-generated examples beat dataset ones wherever the model can write good rationales natively, and combining them with a zero-shot CoT prefix is the best variant overall, exceeding the zero-shot CoT baseline for two of three models. Post-processing those generated examples has almost no effect (mostly within half a point), with the only consistent benefit on the model least able to produce coherent rationales on its own.

## Limitations

The paper has no limitations section. What a reader should weigh: the evidence is one dataset (GSM8K) and three models at 7-8B under greedy decoding, so the claim that few-shot CoT has become a distraction rests on a narrow slice — grade-school arithmetic is also where native CoT behaviour is most thoroughly trained in, which is the condition most favourable to the thesis. Random example selection is a deliberate design choice that isolates format from retrieval, and it means the paper says nothing about few-shot CoT with well-chosen examples; the authors state directly that pairing CoT with advanced selection may still help and that they are not arguing to abandon it. One number worth noting is that the authors could not reproduce the officially reported accuracy for the specialized model and say so in a footnote, so the headline comparison against a published figure carries that caveat. And the third model's result means 'zero-shot beats few-shot' is conditional on reasoning specialization rather than general.

## Why it matters here

- **reasoning-training**: It supplies a direct measurement of something this archive has been treating as a background worry: the baseline a training method is compared against may itself be the thing being measured. Here the standard few-shot CoT baseline costs a reasoning-specialized model twelve points against no prompting at all, so any method benchmarked as an improvement over it inherits that deficit as free gain. Read against the archive's other two instances — a translation-evaluation prompt specialized to the model it was written for, and a vision-language selection method whose 31.8-point gain vanished under a format-matched control — this is the same failure in a third setting, and the archive should now treat an inherited baseline as an experimental variable rather than a fixed point. The extraction result is a second, cheaper caution with the same shape: a nine-point apparent scaling curve turned out to be a parser learning to find the answer, which is exactly the kind of artifact a paper reporting only accuracy would present as progress.

## Entities

- **Concepts**: chain-of-thought prompting, [in-context learning](../../../../wiki/concepts/in-context-learning.md), [prompt sensitivity](../../../../wiki/concepts/prompt-sensitivity.md), baseline validity, [answer extraction](../../../../wiki/concepts/answer-extraction.md), [construct validity](../../../../wiki/concepts/construct-validity.md), zero-shot prompting, reasoning specialization
- **Methods**: [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), zero-shot chain-of-thought, [few-shot prompting](../../../../wiki/methods/few-shot-prompting.md), self-generated demonstrations, rule-based answer extraction
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md)

Tags: `chain-of-thought`, `prompting`, `evaluation`, `baseline`, `in-context learning`

## Abstract

Chain-of-Thought (CoT) prompting remains the standard baseline for evaluating models' reasoning abilities. Originally, this technique was introduced to elicit step-by-step reasoning from large language models (LLMs), which would otherwise tend to directly output the final answer. However, many modern LLMs produce CoT-style responses \textit{natively} when presented with reasoning tasks, which made us revisit the effectiveness of standard CoT prompting. We evaluate several modern mid-sized language models on a math problem-solving task and find that models specialized for reasoning achieve better performance in a simple zero-shot setting than when using few-shot CoT examples - significantly surpassing officially reported results at no additional cost (e.g., from $\sim$77\% to $\sim$84\% for Mathstral on GSM8K). For the tested general-purpose model, a zero-shot CoT prompt is also sufficient to outperform a few-shot CoT baseline. We attribute this to a `guidance-distraction' tradeoff: standard CoT prompting also demands style adaptation, formatting compliance, and potentially undesired contextualization, which can distract models from the core reasoning task. Our findings suggest that using standard CoT prompting increasingly acts as a source of distraction as models grow stronger.

---

Record id: `arxiv:2608.03550`
