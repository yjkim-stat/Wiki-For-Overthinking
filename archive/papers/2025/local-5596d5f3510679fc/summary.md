<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Answer Convergence as a Signal for Early Stopping in Reasoning

- **Authors**: Xin Liu, Lu Wang
- **Venue**: arXiv
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Defines the Answer Convergence Ratio — the fraction of a chain of thought needed before the forced answer stops changing — measures it by incremental truncation across five tasks and five models, and proposes three inference-time stopping methods (answer consistency, a logit boost on the end-of-thinking token, and an LSTM probe over activations), of which only the learned probe holds accuracy on hard tasks.

## Problem

Chain-of-thought inflates inference cost, and the authors hypothesize much of it is unnecessary: the model may fix its answer internally well before the trace ends. What was missing was a measurement of how much explicit reasoning is actually required for a model to reach a stable decision, and inference-time stopping methods that exploit it without retraining, modifying the model, or needing gold answers.

## Contributions

- Introduces the Answer Convergence Ratio and measures it by incremental sentence-level truncation with a forced answer, showing across five tasks and five models that the predicted answer typically stabilizes well before the trace ends — near ACR 0.0 on NaturalQuestions, around 0.8 on GSM8K and MATH-500, near 0.9 on GPQA and AIME'24 — and that larger models converge earlier.
- Observes that the end-of-thinking token often already sits in the top 10 candidates at sentence boundaries while the model prefers continuation tokens such as 'wait', 'or' and 'but', and turns this into a decoding-side fix that boosts the </think> logit in proportion to how peaked the output distribution is, so the boost applies only when the model is confident.
- Proposes Learn-to-Stop, an LSTM over final-layer activations trained on labels derived from the model's own converged prediction rather than gold answers, giving a stopping policy that needs no ground truth and no modification of the base model.
- Reports the negative result that output-consistency and logit-boost stopping degrade sharply as reasoning load rises (on R1-Qwen-32B, Answer Consistency takes AIME'24 from 73.3 to 13.3), while the activation-based learned policy retains accuracy — evidence that shallow output signals are insufficient for hard reasoning.

## Method

Diagnostic protocol. A CoT trace is split into sentence-level chunks with the NLTK tokenizer, each chunk treated as one reasoning step. The chunks are incrementally concatenated (chunk1, chunk1+chunk2, ...), each prefix followed by an injected end-of-reasoning token </think>, and the model is prompted to produce an answer from that partial chain by greedy decoding. The earliest chunk after which the predicted answer stays unchanged through to the end defines the convergence point, and the Answer Convergence Ratio (ACR) is that chunk index divided by the total number of chunks — e.g. stabilizing at the 7th of 10 chunks gives ACR 0.7. Note the method needs no gold answers: convergence is defined against the model's own final prediction, not against correctness.

Three inference-time stopping methods follow, all model-agnostic and requiring no modification of the LM.

(1) Answer Consistency (unsupervised). During decoding, </think> is appended at predicted natural sentence boundaries and an answer is greedy-decoded. If the same answer is produced for k consecutive chunks, reasoning is judged converged and generation stops. The implementation uses k = 10.

(2) Think Token Adjustment (unsupervised, decoding-side). The paper observes that </think> often already ranks among the top 10 candidates at sentence boundaries but the model prefers continuation tokens such as 'wait', 'or' or 'but'. It therefore boosts the </think> logit by a linear transformation y_{t*} <- y_{t*} + alpha * (max(y) - mean(y)), where y are the vocabulary logits. Because max(y) - mean(y) measures how peaked the output distribution is, the boost is adaptive: it only encourages early termination when the model is already confident. Implemented as a vLLM logit processor that disables itself once </think> is emitted; alpha = 0.6 in the main experiments.

(3) Learn-to-Stop (supervised over self-labels). A single-layer LSTM (128 hidden units, dropout 0.1) encodes the sequence of final-layer activations {h_1, ..., h_T} across chunks; at each chunk a sigmoid head gives p_hat_t = sigma(W z_t + b), trained with binary cross-entropy. Labels come from the same diagnostic: the earliest chunk whose predicted answer matches the model's final answer and stays unchanged is labelled 1, as are all later chunks, and earlier chunks 0 — so training uses the model's self-predicted outputs and no gold-standard answers. At inference, reasoning stops when p_hat_t >= tau, with tau tuned on validation (0.50, 0.99, 0.99, 0.50 for NQ, GSM8K, MATH-500, GPQA-Diamond). Trained 200 epochs, batch 32, Adam at 5e-4.

Evaluation uses five tasks (NaturalQuestions, GSM8K, MATH-500, GPQA-Diamond, AIME'24) and five models across three families (R1-distilled Qwen-7B/32B, R1-distilled Llama-8B/70B, QwQ-32B), reporting accuracy, average generated tokens, and percentage token reduction against the unmodified model. Baselines are the original model and Concise CoT (CCoT), a prompt-level token budget, set to 100 tokens. All runs are repeated three times and averaged; serving is via vLLM. Dataset splits (Table 2) are 800/200/3610 for NQ, 800/200/1319 for GSM8K, 320/80/100 for MATH-500, 78/20/100 for GPQA-Diamond, and 30 test items for AIME'24, which has no training data and is therefore evaluated only with the unsupervised methods.

## Results

Diagnostic. Figure 2 shows the ACR distribution by task for R1-distilled Qwen-32B: it peaks near 0.0 for NaturalQuestions (essentially no explicit reasoning needed), around 0.8 for GSM8K and MATH-500, and near 0.9 for GPQA and AIME'24 — so the convergence point moves later as reasoning load rises. The abstract's headline is that on reasoning tasks models typically converge after about 60% of the steps. Appendix Figure 4 reproduces the same trends on the other four models, and the paper reports larger models converging earlier (ACR distributions shifting left, e.g. R1-Llama-70B versus its 8B variant on NQ and GSM8K).

Main table (Figure 3 in the paper, a results table). Accuracy / average tokens, versus the unmodified model.

The supervised method is the only one that holds up across difficulty. On QwQ-32B, Learn-to-Stop cuts GSM8K tokens from 755.1 to 418.9 (-44.5%) for a 0.2-point accuracy change (96.8 -> 96.6), cuts NQ tokens from 646.0 to 335.9 (-48.0%) while accuracy rises 41.6 -> 43.0, and on GPQA cuts tokens 39.2% (6557.9 -> 3988.3) at 24.2 versus the original 25.3. On R1-Qwen-32B it holds MATH-500 at 90.0 versus 91.0 original (-17.2% tokens) and GPQA at 30.3 versus 33.3 (-18.1% tokens).

The two unsupervised methods buy much larger savings on easy tasks and collapse on hard ones. On R1-Qwen-32B, Answer Consistency improves NQ accuracy (35.0 -> 38.4) at -36.7% tokens and holds GSM8K (89.4 -> 91.0) at -18.3% tokens, but on the same model MATH-500 falls 91.0 -> 55.0 (-74.7% tokens), GPQA 33.3 -> 14.1 (-76.5%), and AIME'24 73.3 -> 13.3 (-82.0%). Think Token Adjustment shows the same shape more mildly on that model (MATH-500 91.0 -> 68.0, GPQA 33.3 -> 24.2, AIME 73.3 -> 43.3), and on QwQ-32B it collapses instead (GPQA 25.3 -> 11.3, AIME 76.7 -> 20.0) while barely saving tokens there. The paper reads this as shallow output-consistency signals being insufficient under high reasoning complexity.

Ablations on R1-distilled-Llama3.1-8B. For the logit boost (Tables 3 and 4), accuracy is flat up to alpha = 0.4 (MATH-500 79.0 and AIME 40.0 at both alpha = 0.0 and alpha = 0.4) then degrades (alpha = 0.6 gives GSM8K 66.8, GPQA 9.1, AIME 23.3; alpha = 1.0 gives GSM8K 43.2, GPQA 8.1), while tokens fall sharply throughout (GSM8K 401.3 at alpha = 0 to 10.3 at alpha = 1.0). The stated takeaway is that alpha in [0.2, 0.4] is the good trade-off and alpha >= 0.6 risks early truncation on hard tasks. For Answer Consistency, the ablation reports accuracy improving and saturating around k in [20, 30], small k stopping too early.

Two settings in the main experiments sit outside their own ablations' recommended ranges: alpha is set to 0.6 and k to 10, whereas the ablations recommend alpha <= 0.4 and k in [20, 30]. The paper does not comment on this, and it is a plausible contributor to the hard-task collapses above.

## Limitations

Stated: the methods assume answer convergence correlates with correctness of the final output, but convergence does not guarantee correctness, especially on harder tasks such as GPQA and AIME. Second, allowing the model to predict without observing the full trace may compromise the faithfulness of the reasoning; a manual analysis finds most truncated traces stay aligned with the final answer but occasional unfaithful stops occur (Appendix A.6).

Not stated, and worth noticing. The main experiments use alpha = 0.6 and k = 10 while the paper's own ablations recommend alpha <= 0.4 and k in [20, 30], so the reported unsupervised results are not run at the paper's own recommended operating point. The hard-task test sets are small — 100 items for MATH-500 and GPQA-Diamond, 30 for AIME'24 — and although runs are averaged over three seeds, no variance or confidence interval is reported, so several-point differences rest on one or two problems. MATH-500 is evaluated on a 100-item subset rather than the full 500, which makes the numbers not directly comparable with other papers reporting MATH-500. Learn-to-Stop needs per-task training data and a per-task threshold (tau ranges from 0.50 to 0.99 across four tasks), so its robustness is bought with task-specific fitting that the two unsupervised methods do not need, and it could not be evaluated on AIME'24 at all for want of training data. No wall-clock measurement is reported, although Answer Consistency requires decoding a trial answer at every sentence boundary.

## Why it matters here

- **overthinking**: This is the direct precursor of the archive's RCP/RCPD reading and shares its instrument almost exactly: NLTK sentence chunking, incremental prefixes, a forced </think> injection, and a greedy answer read out at each cut. Where RCP defines convergence distributionally (content-length stabilization plus a KL residual against an estimated terminal distribution) this paper defines it by string equality of the forced answer, and its Answer Convergence Ratio is the same quantity RCP later calls the Reasoning Completion Point, normalized by trace length. Two connections matter beyond the shared instrument. First, the observation that </think> already sits in the top 10 candidates at sentence boundaries while the model prefers 'wait'/'or'/'but' is the same phenomenon RCPD later exploits as a rank signal, and it supplies an independent, earlier justification for RCPD's rank thresholds sitting at 5 and 10; it also converges with ThinkBrake's log-probability margin and NEAT's exit neurons on the same conclusion, that the termination preference is present and not acted on. Second, this paper supplies the negative result that the RCP line most needs: consistency-based stopping is not merely weaker on hard problems but catastrophic (AIME'24 73.3 to 13.3 on R1-Qwen-32B), and only a learned activation probe survives — which is the same ordering the archive's BLADE reading reports and the same difficulty boundary at which the multilingual latent-reasoning study finds early answer formation disappearing. It also states plainly the limitation the whole cluster inherits: convergence does not guarantee correctness.

## Entities

- **Concepts**: [answer convergence](../../../../wiki/concepts/answer-convergence.md), Answer Convergence Ratio (ACR), incremental truncation with forced answer emission, early stopping via answer consistency, end-of-reasoning token logit boosting, peakedness-adaptive logit adjustment, learned stopping from internal activations, self-labelled supervision without gold answers, convergence does not guarantee correctness, faithfulness of truncated reasoning
- **Methods**: Answer Consistency early stopping, Think Token Adjustment, Learn-to-Stop, [Concise CoT (CCoT)](../../../../wiki/methods/concise-cot-ccot.md), LSTM stopping classifier, vLLM logit processor, NLTK sentence chunking
- **Datasets**: NaturalQuestions, [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math500.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md)

Tags: `overthinking`, `early stopping`, `answer convergence`, `reasoning length`, `training-free`, `activation probe`, `termination token`, `chain-of-thought`

## Abstract

Chain-of-thought (CoT) prompting enhances reasoning in large language models (LLMs) but often leads to verbose and redundant outputs, thus increasing inference cost. We hypothesize that many reasoning steps are unnecessary for producing correct answers. To investigate this, we start with a systematic study to examine what is the minimum reasoning required for a model to reach a stable decision. We find that on reasoning tasks like math, models typically converge to their final answers after 60% of the reasoning steps, suggesting substantial redundancy in the remaining content. Based on these insights, we propose three inference-time strategies to improve efficiency: (1) early stopping via answer consistency, (2) boosting the probability of generating end-of-reasoning signals, and (3) a supervised method that learns when to stop based on internal activations. Experiments across five benchmarks and five open-weights LLMs show that our methods significantly reduce token usage with little or no accuracy drop. In particular, on NaturalQuestions, Answer Consistency reduces tokens by over 40% while further improving accuracy. Our work underscores the importance of cost-effective reasoning methods that operate at inference time, offering practical benefits for real-world applications.

---

Record id: `local:5596d5f3510679fc`
