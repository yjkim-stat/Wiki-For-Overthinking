<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Claim-Level Reliability Assessment for Efficient Test-Time Reasoning

- **Authors**: Sen Xu, Wei Wang, Shixi Liu, Jixin Min, Yingwei Dai, Zhibin Yin, Yirong Chen, Junlin Zhang
- **Venue**: cs.AI
- **Published**: 2026-08-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11994>
- **PDF**: <https://arxiv.org/pdf/2608.11994v1>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.25, test-time-scaling 0.50

## In one line

Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.

## Problem

Test-time scaling by repeated sampling saturates: as the budget grows, extracting a discriminative reliability signal becomes the bottleneck rather than producing candidates. Whole-trace signals -- token probability, entropy, hidden states -- suffer signal dilution, because most tokens are routine steps that form a weakly discriminative background and hide a localized fatal error inside an otherwise plausible trace. Step-level verification isolates such errors but is computationally exhaustive and usually needs process supervision or a separately trained verifier.

## Contributions

- Claim-level falsification as a principle for test-time scaling: condense a trace into a fixed number of decision-critical claims and spend compute searching for a refutation of each
- CLR, a training-free instantiation that needs no verifier, no process labels and no second model
- A nonlinear reliability score that lets a smaller, better-supported answer group overturn a numerically larger consensus
- A decomposition showing the gain comes from falsification-based reweighting rather than from the claim prompt

## Method

Stage 1 samples K traces; each request returns a full reasoning trace, its prediction, and exactly M concise claims whose failure would undermine that prediction -- intermediate conclusions, constraints, decision points or evidence linking the problem to the answer, explicitly excluding summaries and restatements of the prediction. Stage 2 makes one joint request per trace containing only the problem and the ordered claim list, without the trace or the final prediction, and asks the same model to search each claim for a decisive contradiction, counterexample, factual or logical error, missing condition or unsupported inference, and for conflicts across claims. Each claim gets a binary verdict, where VALID denotes only 'not refuted by this assessment' rather than a proof of correctness -- the asymmetry the method rests on is that refuting a claim needs one decisive witness while constructing a solution needs a flawless path, and the paper is explicit that this is an inductive bias and not a guarantee. If s_k is the fraction of a trace's claims that survive, the trace score is r_k = s_k^M, so the exponent makes each refuted claim progressively more consequential than linear averaging would; predictions are then partitioned into equivalence groups and the group maximizing the summed score wins. When every trace scores 1 this reduces exactly to self-consistency. The budget accounting is the comparison's spine: CLR@K spends K generation plus K assessment requests, matching the request count of Cons@2K, so CLR@32 is compared against Cons@64. Request parity is not token parity, so accuracy is also reported against realized tokens. Four models -- Gemma-4-12B-it, GPT-OSS-20B, GPT-OSS-120B and Qwen3.5-27B -- on HMMT25, HMMT26, CMIMC25 and an Apex shortlist, with M = 5 and each number averaged over eight independent flows.

## Results

The accuracy-efficiency profile splits by model rather than being uniform. On Gemma-4-12B-it, CLR@32 beats Cons@64 on all four benchmarks by 7.12 to 12.08 points -- HMMT25 76.67 to 88.75, CMIMC25 68.75 to 80.62 -- but spends 22.2 to 47.8 percent more tokens to do it. On GPT-OSS-20B the pattern inverts: tokens fall 36.3 to 39.8 percent on every benchmark while accuracy improves on three of four, with CMIMC25 rising 77.50 to 82.19 at 37.0 percent fewer tokens and HMMT25 slipping 80.00 to 79.58. GPT-OSS-120B gains up to 5.00 points at 21.6 to 23.7 percent fewer tokens; Qwen3.5-27B, already above 90 on three benchmarks, gains at most 2.60 with its largest token saving 14.5 percent. The decomposition is the most informative table: prompting for claims alone *lowers* single-rollout accuracy by 0.65 to 4.56 points against regular sampling, and the falsification reweighting then adds 4.48 to 7.01 points over unweighted aggregation of the same 32 candidates -- so the mechanism is the reweighting, not the changed prompt. Rescue rate, defined only over cases where self-consistency is wrong although a correct candidate is present among the same traces, spans roughly 16 to 48 percent and averages about 37 percent across the 16 benchmark-budget settings. The claim-count ablation moves from M=1 to M=3 for 3.13 to 3.79 points on every benchmark, with M=5 helping on three and HMMT26 peaking at M=3. Across budgets, self-consistency saturates or fluctuates as samples are added while CLR keeps climbing, though the paper states plainly that the curves cross at intermediate budgets and CLR is not uniformly dominant.

## Limitations

The paper's own scope limits are stated in the method rather than a section. CLR only reweights already-parsed candidates, so it cannot recover a correct answer absent from the Stage-1 samples -- it converts candidate coverage into better selection and nothing more. Request parity does not imply token parity, and on the model where accuracy gains are largest the token cost rises by up to 47.8 percent, so 'matched budget' means matched calls. The exponent M in the score is a heuristic monotone transform, not a joint correctness probability, and does not assume claim independence. The M ablation jointly varies claim count, score resolution and penalty sharpness, because M is both the number of claims and the exponent, so it does not isolate claim count. What a reader should add: this is a workshop paper, and every benchmark is competition mathematics with a parseable short answer, so the equivalence-group construction that the aggregation depends on is doing easy work here. The headline framing rests on GPT-OSS-20B/CMIMC25 while the same model regresses on HMMT25 and the near-saturated Qwen3.5-27B gains almost nothing, so the benefit is conditional on the base consensus being unreliable -- which the paper says, but the abstract does not. Ties, including the all-zero-score case where every trace has a refuted claim, fall back to the earliest equivalence group in sampling order, and how often that fires is not reported.

## Why it matters here

- **test-time-scaling**: A direct instance of the archive's standing finding that sampling more candidates is not monotone in accuracy, because extra samples strengthen whatever the aggregation rule already does. Here the aggregation rule itself is changed rather than the sample count, and the rescue-rate metric measures exactly the quantity that finding predicts should exist: cases where the correct answer was already sampled and the majority buried it, roughly 37 percent of which are recovered. It also joins the archive's verifier-free selection cluster with an unusual property -- no verifier, no process labels and no second model -- and its decomposition isolates the reweighting from the prompt, which most entries in that cluster do not.

## Entities

- **Concepts**: claim-level falsification, signal dilution, test-time scaling, reliability weighting, verifier-free verification, [answer aggregation](../../../../wiki/concepts/answer-aggregation.md), consensus, rescue rate, budget parity
- **Methods**: [self-consistency](../../../../wiki/methods/self-consistency.md), [majority voting](../../../../wiki/methods/majority-voting.md), [best-of-n](../../../../wiki/methods/best-of-n.md), process supervision, [pass@k](../../../../wiki/methods/pass-k.md)
- **Datasets**: [HMMT](../../../../wiki/datasets/hmmt.md), [CMIMC](../../../../wiki/datasets/cmimc.md), Apex-shortlist

Tags: `test-time-scaling`, `verification`, `self-consistency`, `falsification`, `token-efficiency`

## Abstract

We propose claim-level falsification as a principle for test-time scaling and instantiate it through Claim-Level Reliability Assessment (CLR), a training-free framework that reallocates test-time compute from additional solution sampling to targeted verification. Since whole-trace evaluation often obscures decisive errors due to signal dilution from routine tokens, CLR condenses each reasoning trace into a compact set of decision-critical claims, thereby isolating its logical anchors. Furthermore, recognizing the inherent difficulty of generating entirely correct solutions under fixed model capabilities, CLR shifts the focus to semantic falsification. This approach exploits a fundamental asymmetry between solution construction and claim refutation. Constructing a valid solution requires a flawless reasoning path, whereas refuting an incorrect claim requires identifying only a single decisive flaw. This targeted search for negative evidence systematically compresses the survival space of high-confidence incorrect traces, effectively suppressing erroneous consensus via nonlinear reliability scoring. Across four LLMs and four reasoning benchmarks under matched budgets, CLR generally improves upon pass@1 and self-consistency. On GPT-OSS-20B/CMIMC25, for instance, CLR exceeds pass@1 by 27.15 percentage-points and raises self-consistency accuracy from 77.50\% to 82.19\% with 37.0\% fewer tokens.

---

Record id: `arxiv:2608.11994`
