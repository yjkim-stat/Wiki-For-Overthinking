<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs

- **Authors**: Abinitha Gourabathina, Inkit Padhi, Manish Nagireddy, Subhajit Chaudhury, Prasanna Sattigeri
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.608/>
- **PDF**: <https://aclanthology.org/2026.acl-long.608.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.608
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

TRACE INVERSION reframes abstention as query misalignment -- a hallucinating model answered a different (reconstructed) question than the one the user actually posed -- and detects this by reconstructing the implied query from a model's own reasoning trace and comparing it to the original via an ensemble of embedding-similarity, LLM-judged, and groundedness-detection metrics, beating five baselines in 33/36 settings across four LLMs and nine abstention datasets, while separately showing that CoT/reasoning-trace prompting itself degrades abstention accuracy by an average 2.6% versus non-reasoning prompting.

## Problem

Reasoning models, despite outperforming on reasoning benchmarks, have been shown to have worse abstention ability (knowing when not to answer) than non-reasoning models, and prior abstention methods -- calibration-based (confidence thresholds), prompting-based (asking the model to review its own answer), and collaboration-based (multi-LLM cross-checking) -- underperform specifically on reasoning models because logit/verbalized confidence is miscalibrated, self-correction prompts that express distrust degrade reasoning-model performance, and correlated errors and self-bias weaken multi-LLM collaboration.

## Contributions

- the Query Misalignment Framework, reframing abstention/hallucination detection as recovering whether a model answered a different (reconstructed) question than the one actually posed, applicable across unanswerable, underspecified, false-premise, and subjective query scenarios
- TRACE INVERSION, an abstention method that reconstructs the implied query from a model's own reasoning trace and flags low similarity to the original query, using an ensemble of embedding, LLM-judged, and groundedness-based distance metrics
- state-of-the-art abstention accuracy across four frontier LLMs and nine datasets, beating calibration-, prompting-, and collaboration-based baselines in 33/36 settings, with particular strength on unanswerable-query datasets where baselines degrade most
- an independent finding that eliciting chain-of-thought/reasoning-trace prompting itself measurably degrades abstention accuracy across baseline methods (average -2.6%), evidence that the interpretability CoT appears to offer does not extend to reliable self-knowledge of when the model does not know an answer

## Method

Proposes the Query Misalignment Framework: reframes an abstention failure (hallucination) as the model having answered a different, internally-reconstructed query q* rather than the user's actual query q, so abstention should trigger on divergence between q and q* rather than on confidence in the answer itself. TRACE INVERSION implements this in three steps: (1) generate the model's reasoning trace in response to q; (2) prompt the LLM to reconstruct the most likely query q* that the trace was actually responding to, using only the trace; (3) compare q and q* via an ensemble (majority vote) of three distance modules -- sentence-embedding cosine similarity (all-MiniLM-L6-v2), an LLM-judged intent/framing/context comparison (TrInv-LLM), and a groundedness-risk detector (Granite-Guardian-3.3-8b) checking whether q* is grounded in q -- flagging abstention when similarity is low. Evaluated on four LLMs (phi-4, Qwen2.5-32B, DeepSeek-R1-Distill-Qwen-32B, gpt-oss-120b) across nine QA datasets spanning three abstention-scenario domains (Math & Knowledge: MMLU, GSM-MC, UMWP; Comprehension: Knowledge Crosswords, HellaSwag, Quail; Biases & Safety: Misconceptions, Propaganda, BBQ), against five baselines (Probs, AskCali calibration-based; Reflect prompting-based; Cooperate, Compete collaboration-based), measured by Abstain Accuracy (TP+TN over all cases).

## Results

TRACE INVERSION achieves the best Abstain Accuracy in 33 of 36 model x dataset-domain settings, with an average 8.7% accuracy improvement over the best-competing baseline in each setting -- e.g. overall accuracy of .734 (phi-4), .738 (Qwen2.5-32B), .733 (DeepSeek-R1-Distill-Qwen-32B), and .762 (gpt-oss-120b), versus best baselines around .519-.702 per model. Gains are largest on DeepSeek-R1-Distill-Qwen-32B and gpt-oss-120b, which the paper attributes to trace reconstruction benefiting from a stronger base LLM. All methods (baselines and TRACE INVERSION alike) show degraded abstention on Reading Comprehension and Biases & Safety domains relative to Math & Knowledge, but TRACE INVERSION's degradation is smaller (outperforming by 5.4% in Comprehension, 11.0% in Biases & Safety) and more consistent across domains (smallest worst-to-best domain performance gap, ~5% vs. larger gaps for baselines). Across datasets containing unanswerable queries specifically (UMWP, Quail, BBQ), all baseline methods show a substantial 13-20%+ accuracy drop relative to fully-answerable datasets in the same domain, while TRACE INVERSION shows only a 3-6% drop -- the framework is specifically strong at exactly the abstention scenarios (unanswerable, underspecified, false-premise, subjective queries) it targets. Ablating the three distance modules individually shows domain specialization: sentence-embedding similarity (SE) performs best on Math & Knowledge (84.2%) but drops sharply elsewhere; the LLM-judged module (TrInv-LLM) performs best on Comprehension (73.3%); the groundedness module (GROUND) performs best on Biases & Safety (75.2%) -- the full majority-vote ensemble outperforms any single module overall (73.2%), leveraging each module's domain strength. Separately, appending a CoT/step-by-step reasoning prompt to all five baseline methods degrades their abstention accuracy on almost every dataset, by an average 2.6% versus using the same baseline with a regular (non-CoT) prompt -- direct evidence that eliciting an explicit reasoning trace itself, independent of which abstention method is layered on top, harms a model's ability to know when not to answer.

## Limitations

TRACE INVERSION requires prompting the LLM three times (trace generation, query reconstruction, and an LLM-judged comparison), incurring higher inference cost than simpler prompting-based baselines, though the paper notes simpler individual distance metrics can substitute for the full ensemble to reduce cost while remaining competitive. The Query Misalignment Framework does not claim to cover all hallucination types -- it explicitly does not address cases of unfaithful reasoning or answer-rationale inconsistency where the reasoning trace is internally sound throughout but the final answer is still wrong (a case the trace-reconstruction signal cannot flag, since the trace and the derived q* may still look aligned with q). The framework is evaluated on nine datasets covering knowledge gaps, ambiguity, false premises, and subjectivity, but not on harmful or 'stale' (time-sensitive) questions, which the paper leaves to future work.

## Why it matters here

- **overthinking**: Indirectly relevant: this is primarily an abstention/hallucination-detection method rather than a reasoning-length or efficiency intervention, but it contributes a specific, measured cost of chain-of-thought/reasoning-style prompting -- degraded abstention accuracy (average -2.6%) versus non-reasoning prompting across five different baseline methods -- and explicitly names overthinking in its framing of CoT's downsides ('an imperative for the model to produce an unnecessary and elaborate chain of tokens... even when it lacks the necessary understanding'), adding a distinct failure mode (not knowing when to stop *answering*, as opposed to not knowing when to stop *reasoning*) to the archive's picture of reasoning-trace pathologies.

## Entities

- **Concepts**: query misalignment, reasoning trace inversion, abstention, hallucination-as-wrong-question, groundedness detection
- **Methods**: TRACE INVERSION (query reconstruction + ensemble distance), Probs (calibration baseline), AskCali (calibration baseline), Reflect (prompting baseline), Cooperate (collaboration baseline), Compete (collaboration baseline)
- **Datasets**: [MMLU](../../../../wiki/datasets/mmlu.md), Knowledge Crosswords, [HellaSwag](../../../../wiki/datasets/hellaswag.md), Propaganda, Bias Benchmark for QA (BBQ), Misconceptions (BIG-Bench), Quail, GSM-MC, UMWP

Tags: `abstention`, `hallucination`, `reasoning-trace-analysis`, `chain-of-thought`, `evaluation-methodology`

## Abstract

For Large Language Models (LLMs) to be reliably deployed, models must effectively know when not to answer: abstain. Reasoning models, in particular, have gained attention for impressive performance on complex tasks. However, reasoning models have been shown to have worse abstention abilities. Taking the vulnerabilities of reasoning models into account, we propose our Query Misalignment Framework. Hallucinations resulting in failed abstention can be reinterpreted as LLMs answering the wrong question (rather than answering a question incorrectly). Based on this framework, we develop a new class of state-of-the-art abstention methods called Trace Inversion. First, we generate the reasoning trace of a model. Based on only the trace, we then reconstruct the most likely query that the model responded to. Finally, we compare the initial query with the reconstructed query. Low similarity score between the initial query and reconstructed query suggests that the model likely answered the question incorrectly and is flagged to abstain. Extensive experiments demonstrate that Trace Inversion effectively boosts abstention performance in four frontier LLMs across nine abstention QA datasets, beating competitive baselines in 33 out of 36 settings. The code is available at this https://anonymous.4open.science/r/trace-inversion-08BB/.

---

Record id: `doi:10.18653/v1/2026.acl-long.608`
