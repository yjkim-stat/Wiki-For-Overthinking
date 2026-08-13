<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs

- **Authors**: Iaroslav Chelombitko, Ekaterina Chelombitko, Mika Hämäläinen
- **Venue**: cs.CL
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02486>
- **PDF**: <https://arxiv.org/pdf/2608.02486v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.57

## In one line

Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.

## Problem

Cultural bias in language models is documented behaviourally — a model asked for the supreme sky god returns Zeus, Jupiter and Thor reliably and the Finnish, Slavic or Mesopotamian counterpart far less often — but behaviour cannot say where inside the model the bias is produced. Two mechanisms predict opposite fixes: if the residual stream never separates the cultures, the model lacks the information and needs more data; if it separates them but the readout collapses them, the information is present and the fix belongs at the output. Nothing in the surveyed cultural-bias tasks could tell the two apart, because they lack a parallel structure that asks the same question of many traditions with an unambiguous gold answer.

## Contributions

- A substrate with the property the diagnosis needs: 27 Thompson Motif-Index roles instantiated across 10 cultures spanning six language families, giving 270 cells each with one canonical entity, so the same question has a gold answer in every tradition
- A four-instrument design in which each measurement explicitly does not answer the others' question, and the argument is their conjunction — probe for encoding, logit lens for depth, activation patching for causal location, generation for what a user receives
- A per-cell 2x2 decomposition pairing what the probe reads against what the model emits, yielding Preserved, DecodingSuppressed, SurfaceLuck and RepresentationallyFlat cells
- An output-format control that poses the same question as a 10-way multiple choice over the parallel fillers, separating a classification-versus-generation artefact from a genuine generation-time loss
- A within-mode versus cross-mode correlation test that isolates language conditioning from paraphrase sensitivity, and is robust to the language-proficiency confound by construction

## Method

For each of the 270 (motif, culture) cells two prompts are built: a contextual one asserting that a named entity embodies a described role, used for hidden-state extraction and never containing the culture word so the probe cannot copy it by attention; and a chat prompt asking for the name given culture and role. Linear probing average-pools residual activations over the entity span at every layer and fits a 5-fold ridge classifier for the 10-way culture label. The logit lens applies the final norm and unembedding to every intermediate state and records the depth at which the gold entity's first sub-token enters the top-k, reported as top-k rather than top-1 because subword segmentation is unstable for morphologically rich languages. Activation patching swaps the residual stream of a source-culture prompt into a target-culture prompt at each layer and measures the change in gold-target log-probability. Output extraction greedily generates up to 256 tokens under the chat template, with thinking traces disabled for reasoning-style models, scored by exact match, substring match or length-normalized Levenshtein at threshold 0.8. Both an English and a target-culture native-language prompt mode are run with five paraphrases each. Eighteen decoder-only models from eight families, 1.2B to 34B, are evaluated at fp16 with no quantization.

## Results

The headline is uniform across the sweep: DecodingSuppressed — the probe reads the culture and the generation emits a wrong name — is the largest cell in every one of the 18 models, at 51 to 76 percent (mean 0.65), while RepresentationallyFlat is 0.10 to 0.33 (mean 0.18). Seventeen of eighteen probes clear a 0.60 character-n-gram surface baseline, peaking at 0.61 to 0.88, with significance confirmed by paired bootstrap and exact McNemar; the same models generating land at 0.09 to 0.43. The smallest probe-output gap in the sweep is 0.26 and the largest 0.70. The format control does real work and does not explain the gap away: matching the output task to the probe by multiple choice over the same motif's ten fillers recovers mean accuracy from 0.26 to 0.67, but the chain representation 0.79 to selection 0.67 to generation 0.26 still loses about 41 points at the generation step, and the collapse onto the dominant tradition is visible inside pure selection — on Roman cells 49 percent of errors land on the same-motif Greek counterpart against roughly 11 percent under a uniform error model. Depth is consistent: the lens onset falls in the last 12 percent of layers in every model (median 0.96) while probe-peak depth spreads widely across families, so every model sits on or above the encode-before-decode diagonal. Patching makes the localization causal rather than correlational — the preference-flip rate sits at baseline through the early third, peaks in the last quarter (median peak depth 0.89, median rate 0.75, median lift +0.55), roughly seven times the early-network rate. Scaling shrinks the gap in all five multi-size families and closes it in none: Llama 3.x from 1.2B to 8B moves the probe 0.79 to 0.88 and the output 0.09 to 0.25, leaving 0.63, with a naive log-parameter extrapolation predicting about +0.10 output gain per decade of parameters. Cross-lingual querying gates partially disjoint subsets of the same representation: within-mode correctness correlates at 0.57 against 0.29 cross-mode, so cross-language queries are about twice as decoupled, and per-culture English-versus-native deltas track the language each canon is documented in (Greek +0.241 and Egyptian +0.177 favouring English; Chinese -0.071 and Finnish -0.058 favouring the native query) rather than tokenizer fertility, which does not predict the per-cell delta at all. Simply taking the union of the two query modes lifts cell recovery by 0.08 absolute, a 36 percent relative gain, at zero training cost.

## Limitations

The paper's limitations section is unusually thorough and names the right things. The canonical entity-to-culture assignments are genuinely contested at boundaries — Odin and Thor are both Norse sky figures, Perun is shared between Ukrainian and West Slavic traditions, and several cells use a scholarly-contested filler — so modern consensus is followed where it has shifted but not every assignment is unambiguous; four structural absences are catalogued and excluded and others cannot be ruled out. The ten cultures deliberately exclude sub-Saharan African, Native American, Polynesian, Australian and Arctic indigenous traditions; the authors judge the headline claim unlikely to reverse there but flag the per-culture English-versus-native deltas as the part most at risk, precisely for traditions documented predominantly in non-Anglocentric sources. The substrate is 270 cells with all inference at cell level, output scoring on 266 and the multiple-choice control on 263, so the control's accuracies rest on a marginally smaller set than the generation accuracies they are compared against. The logit lens is used in its raw form for cross-model comparability and gives a relative ordering rather than a calibrated probability, since intermediate states are not calibrated for direct decoding. One model's chat-template patching scores at approximately zero through a template artefact and is reported on a bare-prompt estimate instead, with explicit patching left to a follow-up. Robustness is checked rather than assumed: rescoring 48,568 generations under three stricter criteria preserves the per-model ranking at Pearson 0.87 or above.

## Why it matters here

- **reasoning-interpretability**: It is a clean instance of the distinction this archive keeps needing and rarely gets stated so sharply: what a representation contains and what the model does with it are separately measurable, and here they disagree in every model tested. The methodological core transfers directly to reasoning work — a linear probe showing a property is decodable establishes encoding and nothing more, which is why the design pairs it per cell with generation and adds patching to make the locus causal rather than correlational. The paper is explicit that each instrument does not answer the others' question and that the argument is their conjunction, which is the standard this archive's probing results should be read against. Two further results carry over. Scaling shrinks the encode-decode gap in every family and closes it in none, extrapolating to about +0.10 per decade of parameters, so a readout failure is not something more capacity fixes. And the practical consequence is a diagnosis of where an intervention can work at all: encoder-side fixes push on the 0.10-to-0.33 slice while the dominant 0.51-to-0.76 slice sits at the unembedding, which is the same shape of argument as the archive's finding that a signal can demonstrably track the right thing and still buy nothing downstream.

## Entities

- **Concepts**: linear probe, logit lens, activation patching, [causal intervention](../../../../wiki/concepts/causal-intervention.md), [residual stream](../../../../wiki/concepts/residual-stream.md), unembedding, cultural bias, [representation versus readout](../../../../wiki/concepts/representation-versus-readout.md), [scaling laws](../../../../wiki/concepts/scaling-laws.md), probing
- **Methods**: [linear probe](../../../../wiki/methods/linear-probe.md), [logit lens](../../../../wiki/methods/logit-lens.md), [activation patching](../../../../wiki/methods/activation-patching.md), ridge regression, [principal component analysis](../../../../wiki/methods/pca.md), linear discriminant analysis, bilingual ensembling
- **Datasets**: Thompson Motif-Index of Folk-Literature, folkmotif, Belebele

Tags: `interpretability`, `cultural bias`, `probing`, `activation patching`, `multilingual`

## Abstract

Open-source LLMs reliably name Zeus, Jupiter, and Thor, but recover their counterparts in less-represented traditions like Finnish, Slavic, Egyptian, or Chinese mythology far less consistently. We ask where inside the model this cultural default is produced. On a parallel cross-cultural substrate of Thompson-motif entities, we instrument 18 open-source LLMs from 8 architecture families with linear probing, logit lens, activation patching, and output extraction. The residual stream cleanly distinguishes cultures, well above a name-string baseline, yet the decoder collapses culturally-specific tokens onto dominant-tradition ones. The failure is at readout, not at representation. Asking the same question in the target culture's native language versus English produces failures that cluster within language but decouple across language: the decoder is gated on prompt language. We release a per-entity (probe, output) decomposition framework, a citation-anchored cross-cultural ground truth, a within- versus cross-mode correlation test for language-conditioned readout, and per-entity predictions for all 18 models.

---

Record id: `arxiv:2608.02486`
