<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?

- **Authors**: Soumadeep Saha, Krish Sharma, Akshay Chaturvedi, Nicholas Asher
- **Venue**: cs.CL
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02867>
- **PDF**: <https://arxiv.org/pdf/2608.02867v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.25, reasoning-training 0.50

## In one line

Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.

## Problem

The debate over whether RLVR expands the reasoning boundary or only sharpens sampling has been argued with performance metrics and token-level statistics, neither of which can settle it. A model can produce many valid continuations that differ only in variable naming, the order of commutative operations or natural-language phrasing; that is entropy without exploration. So a measured entropy collapse is compatible with two opposite readings — the policy has calcified merely stylistic choices, or it has pruned genuinely distinct inferential pathways — and nothing in the existing evidence distinguishes them.

## Contributions

- A construction that makes the distinction measurable: reasoning traces are segmented into steps, steps judged semantically equivalent are merged into single nodes, and the resulting prefix tree makes every root-to-leaf path an alternate solution and every branch a genuine inferential fork
- Candidate preference entropy, the conditional entropy of a model's choice between two specific alternative completions given a shared prefix, differenced against the base model to isolate what post-training changed
- A syntax-versus-semantics contrast built into the tree: two continuations from the same child differ syntactically, one from a sibling child differs semantically, and the same measure is applied to both pairs
- Mazes as a second modality where the action space is closed, so alternate realizations cannot be superficial restatements and exploration is directly countable
- Controlled matched post-training — distillation and RLVR both performed by the authors from public base checkpoints — because vendors release neither matched pre/post pairs nor the data that would let the effect be attributed

## Method

For mathematics, several correct traces per question are sampled from a set of frontier models, segmented into reasoning steps, and merged into a prefix tree by semantic similarity judged by a model, over 235 AIME questions and roughly 20,000 responses. Candidate preference entropy at a branch is computed from length-normalized log-probabilities of the two competing continuations under the model being tested, softmaxed into a two-way distribution; the difference against the base model's value gives the post-training-induced change. The syntax contrast picks an anchor trace and two continuations from the same child node — semantically equivalent, syntactically different — while the semantics contrast pairs one of those against a continuation from a sibling child. For mazes, base models are supervised-finetuned on 30,000 oracle solutions and then RLVR-trained on 12,000, and node-visit entropy is estimated from 1,000 generations across 50 mazes. Three decoding interventions probe what the policy has given up: masking illegal moves, zeroing the optimal continuation so another verifier-equivalent one must be found, and forbidding immediate reversals. Backtracking is measured directly as the probability of the reversing move at 2,500 sampled dead-end states, and in mathematics by appending a distractor step drawn from another tree and checking whether the model still reaches the correct answer.

## Results

Exploration falls significantly on both modalities. In mazes, node-visit entropy drops from 2.3380 to 1.8138 on one model and 1.9288 to 1.6092 on the other, both at p < 0.0001. On mathematics, the branch-preference entropy of the RLVR model is below its distilled counterpart on 95.49 to 100 percent of 10,000 sampled branch tuples across four model families. The decisive result is the decomposition: for every model the collapse in the semantic contrast is statistically significant, while in the syntactic contrast it is smaller and not significant for one model — so the policy has become more decided about which inference to make, not merely about how to phrase it. Two things RLVR gains are measured just as carefully. It learns the environment's constraints: at maze nodes where only one move is legal the RL policy's entropy collapses correctly, and masking illegal moves lifts the distilled model by roughly eight-fold against three-fold for the RL model — which is the same fact read as a cost, since with invalid continuations removed the flatter distilled policy outperforms the RL one by about 60 percent. Forcing the model off the optimal path costs the RL model about 65 percent of its performance against 50 percent for the distilled one, the signature of ossified preferences. And backtracking improves sharply — the probability of the reversing move at dead ends rises from 0.0647 to 0.1687 and from 0.0068 to 0.1537 on the two maze models, with absolute failures falling, while in mathematics the RL models recover from an injected distractor better than their distilled counterparts by 4.18 to 29.09 points. The synthesis the paper offers is that RLVR buys sample efficiency by learning what is invalid, and pays for it by pruning what is valid but different.

## Limitations

The paper states both. The tree construction depends on a model judging semantic equivalence; spot checks and inter-annotator agreement against two other frontier models were near-perfect, but no rigorous human evaluation was run, and errors may remain. The evidence covers deterministic environments and mathematical reasoning only, because sampling enough continuations is expensive — the AIME traces alone cost USD 3000 — with code generation named as the obvious extension. A reader should add that the controlled comparison is RLVR against long-CoT distillation from the same base rather than against the base model itself, so 'RLVR reduces exploration' here means relative to a distilled policy trained on the same data; that is the right control for isolating the reinforcement-learning step and it is not the comparison the pass@k literature usually makes. The maze interventions are run on one model at one temperature, and the mathematics results rest on 235 questions.

## Why it matters here

- **reasoning-training**: This is the discriminating experiment the archive's entropy thread has been asking for, run on the question of what the collapsed quantity actually is. The answer is that the collapse is semantic and not merely stylistic, which closes off the most comfortable reading of entropy collapse — that RLVR is only calcifying phrasing — and does so with a control the archive's other entropy papers lack, since both arms are post-trained by the same authors from the same base on the same data. It also supplies the mechanism the archive's reasoning-boundary dispute has been missing. The two sources already here disagree about whether RLVR narrows the boundary, and settle it with pass@k under different correctness criteria; this paper says both effects are real and separable — the policy assigns less mass to invalid continuations, which is why it wins at small k, and less mass to valid-but-different ones, which is why the base model catches up at large k. The Legal Only intervention makes that concrete and is the sharpest single number: once invalid moves are masked out, the flatter distilled policy beats the RL one by about 60 percent. Two further results cut against the archive's own framing. RLVR substantially improves backtracking, which the archive has not credited it with, and it improves recovery from an injected distractor by up to 29 points — so 'RLVR narrows the reasoning boundary' is incomplete without saying that it widens the recoverable region within it.

## Entities

- **Concepts**: [reasoning boundary](../../../../wiki/concepts/reasoning-boundary.md), [entropy collapse](../../../../wiki/concepts/entropy-collapse.md), [policy entropy](../../../../wiki/concepts/policy-entropy.md), [exploration](../../../../wiki/concepts/exploration.md), candidate preference entropy, semantic equivalence, [backtracking](../../../../wiki/concepts/backtracking.md), [trajectory diversity](../../../../wiki/concepts/trajectory-diversity.md), verifier equivalence, pass@k, LLM-as-a-judge
- **Methods**: BODHI-Tree, [RLVR](../../../../wiki/methods/rlvr.md), [long chain-of-thought distillation](../../../../wiki/methods/long-chain-of-thought-distillation.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [DAPO](../../../../wiki/methods/dapo.md), prefix steering, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md)
- **Datasets**: [AIME](../../../../wiki/datasets/aime.md), OpenThoughts-114k-math, [DAPO-Math-17k](../../../../wiki/datasets/dapo-math-17k.md), Maze Dataset

Tags: `rlvr`, `exploration`, `entropy collapse`, `reasoning boundary`, `backtracking`

## Abstract

Although reinforcement learning with verifiable rewards (RLVR) has improved the performance of large language models (LLMs) across a variety of reasoning tasks, there is significant debate as to whether RLVR expands the reasoning capability boundary, or just improves sampling efficiency. In this paper, we investigate the nature of test-time exploration in RLVR-trained LLMs by employing controlled maze-solving experiments and extracting a tree structure from mathematical reasoning traces (BODHI-Trees) based on semantic equivalence. This helps us delineate between entropy arising from stylistic variations and genuine inferential branching. Our findings demonstrate that the policy entropy collapse observed in RLVR models is not merely syntactic, and is accompanied by a significant reduction in semantic branching entropy. While RLVR improves adherence to environmental constraints and backtracking capabilities, it constricts the space of continuations; we provide evidence suggesting that this might be responsible for the sample efficiency gains of RLVR, albeit at the cost of genuine rollout diversity.

---

Record id: `arxiv:2608.02867`
