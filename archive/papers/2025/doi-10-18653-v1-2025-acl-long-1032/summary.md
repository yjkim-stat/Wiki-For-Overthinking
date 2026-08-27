<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# On Generalization across Measurement Systems: LLMs Entail More Test-Time Compute for Underrepresented Cultures

- **Authors**: Minh Duc Bui, Kyung Eun Park, Goran Glavaš, Fabian David Schmidt, Katharina von der Wense
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.1032/>
- **PDF**: <https://aclanthology.org/2025.acl-long.1032.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.1032
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

LLMs default to Western measurement systems (USD, kilometers, kilograms) reflecting their training-data culture, suffer significant accuracy drops when queried in a non-default system (currency, length, or weight), and while chain-of-thought/sequential reasoning stabilizes large models' accuracy back toward the default level, it increases test-time compute by 180-300% -- disproportionately burdening users whose cultural context is not the default.

## Problem

It is unknown whether LLMs can accurately present the same underlying facts (fiscal data, distances, food prices) across different, culturally-bound measurement systems (currencies, length units, weight units), or whether they are biased toward the measurement conventions dominant in their training data, systematically disadvantaging users from underrepresented cultural/measurement contexts.

## Contributions

- new datasets spanning fiscal data, city distances, and food prices across dozens of currencies/length/weight systems for testing LLM factual accuracy across measurement systems
- evidence that LLMs default to and perform best in the measurement system dominant in their training data (skewed Western/Anglo-centric), with a significant accuracy penalty -- correlated with country income level -- for alternative systems, that persists even when the prompt language is aligned with the target system
- a demonstration that explicit reasoning (sequential or CoT) stabilizes large-model accuracy for non-default systems but at a 180-300% test-time-compute cost increase, disproportionately burdening users whose cultural context does not match the LLM's default

## Method

Curates three datasets spanning fiscal data (GDP per capita, 112 currencies, 148 countries), city distances (10 length systems including kilometer, mile, Chinese li, Thai wa), and food prices per weight (10 weight systems including kilogram, pound, Korean geun, Chinese jin), testing seven instruction-tuned open LLMs (Qwen2.5 72B/7B, Llama 3.3 70B, Llama 3.1 72B/8B, Aya Expanse 32B/8B). Answers three research questions: (RQ1) which measurement system LLMs default to when not instructed; (RQ2) whether accuracy (measured via inverse mean absolute percentage deviation, MAPD) varies when explicitly instructed to use an alternative system, tested with a non-parametric Wilcoxon signed-rank test; (RQ3) whether explicit reasoning (sequential single-hop prompting, or chain-of-thought) mitigates the gap, framing cross-system queries as a 3-step multi-hop reasoning problem (retrieve fact in default system, retrieve conversion rate, apply arithmetic), and measuring both the resulting accuracy change and the added inference cost (via LLM API pricing).

## Results

LLMs default overwhelmingly to Western/data-dominant conventions: 80% average default to USD for fiscal data (only 17% to local currency), and models use kilometers exclusively for Germany/Japan/Russia/China while defaulting to miles 73% of the time for US city distances; weight-system defaults strictly follow the data context (100% kilogram-system data reported in kilogram, 100% pound-system in pound). Across 35 model-dataset combinations, the default system yields the best performance in 28 cases, with statistically significant advantage over the second-best system in 22 of those (e.g. Llama 3.3 70B: 57% MAPD default 'Kilogram' vs. 29% MAPD 'Pound', a 28-point drop). Currency performance shows a clear income-based disparity: 43% average MAPD for high-income-country currencies vs. 9% for low-income-country currencies (34-point gap) among large (>=70B) models. Even aligning the prompt language with the target measurement system (e.g. Korean-language prompts with KRW) does not close the gap -- significant drops persist in nearly all tested language/system combinations (Turkish, Korean, Chinese, Japanese). Reasoning helps but is costly and unevenly distributed: without reasoning, large models drop 57-92% (MAPD, relative) when using an alternative system versus the default with no-reasoning; with CoT, large models' drop shrinks to roughly 0-9% (near-full stabilization), but average test-time cost for non-default queries with CoT increases 180-302% relative to no-reasoning depending on the task, and models still start their reasoning chain from the default system 91% of the time for currency (Figure 5) -- meaning the extra reasoning is literally a translation step, so users whose default context differs from the LLM's must always pay this reasoning surcharge. Small models (<70B) show a significant accuracy drop AND remain unstable even with reasoning, so the cost is not reliably compensated by improved accuracy for that tier.

## Limitations

All experiments prompt in English, described as a 'best-case scenario' -- the paper explicitly expects larger, more pronounced gaps in other languages due to more frequent mistranslation of measurements and higher inference cost from tokenization into more subwords, but this is not tested beyond the four languages checked for prompt-language alignment (which did not use non-English measurement-system queries as the primary experiments). Only a selected subset of measurement systems and units is examined; data access constraints, especially for systems still used within marginalized groups, limited comprehensiveness. The paper does not compare against non-LLM tools (RAG systems, dedicated unit-conversion tools) that could sidestep this problem entirely, reasoning that users are more inclined to use a simple LLM chatbot for such tasks.

## Why it matters here

- **overthinking**: Directly relevant to the cost side of test-time scaling, from an equity angle rarely covered in the topic: it quantifies that using chain-of-thought/reasoning to fix a model's factual-accuracy gap costs 180-300% more inference compute, and -- crucially -- that this extra reasoning cost falls disproportionately on users whose context differs from the model's default (poorer countries, non-Western measurement systems). This reframes 'longer reasoning helps accuracy' (usually discussed as a pure accuracy/efficiency tradeoff) as also a distributive-fairness question: the users who most need extra test-time compute to get a correct answer are also the ones a length-penalized or budget-capped 'anti-overthinking' system would shortchange first.

## Entities

- **Concepts**: measurement-system default bias, cross-system factual generalization, multi-hop reasoning for unit/currency conversion, reasoning-induced cost inequity
- **Methods**: sequential single-hop prompting, chain-of-thought prompting, inverse mean absolute percentage deviation (MAPD), Wilcoxon signed-rank test
- **Datasets**: Fiscal Data (World Bank GDP per capita, 148 countries, 112 currencies), City Distances (SimpleMaps-derived, 4 countries), Food Prices per Weight (World Food Program via HDX, 76 countries)

Tags: `test-time-compute`, `fairness`, `cultural-bias`, `chain-of-thought`, `multi-hop-reasoning`

## Abstract

Measurement systems (e.g., currencies) differ across cultures, but the conversions between them are well defined so that humans can state using any measurement system of their choice. Being available to users from diverse cultural backgrounds, Large Language Models (LLMs) should also be able to provide accurate information irrespective of the measurement system at hand. Using newly compiled datasets we test if this is truly the case for seven open-source LLMs, addressing three key research questions: (RQ1) What is the default system used by LLMs for each type of measurement? (RQ2) Do LLMs’ answers and their accuracy vary across different measurement systems? (RQ3) Can LLMs mitigate potential challenges w.r.t. underrepresented systems via reasoning? Our findings show that LLMs default to the measurement system predominantly used in the data. Additionally, we observe considerable instability and variance in performance across different measurement systems. While this instability can in part be mitigated by employing reasoning methods such as chain-of-thought (CoT), this implies longer responses and thereby significantly increases test-time compute (and inference costs), marginalizing users from cultural backgrounds that use underrepresented measurement systems.

---

Record id: `doi:10.18653/v1/2025.acl-long.1032`
