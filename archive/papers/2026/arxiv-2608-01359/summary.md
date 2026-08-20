<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents

- **Authors**: Jianan Xie, Xin Sun, Zhongqi Chen, Xing Zheng, Shu Wu, Bowen Song, Liang Wang
- **Venue**: cs.CL
- **Published**: 2026-08-02
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01359>
- **PDF**: <https://arxiv.org/pdf/2608.01359v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## In one line

Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.

## Problem

Outcome-based RL gives a multi-turn search agent one scalar per trajectory, so the query that retrieved the decisive passage and the query that repeated an earlier one inherit the same credit. Process-reward and turn-level methods make credit finer-grained but only decide where feedback lands, not what information should judge a sampled search action. On-policy self-distillation supplies that missing information by re-scoring under a privileged context, but existing versions condition the teacher on things that do not identify what this particular query should have found — reusable skills, trajectory-derived hindsight, or the golden answer, which specifies the target rather than the evidence.

## Contributions

- Treating a training instance's annotated supporting evidence as instance-level privileged information for search actions, on the argument that evidence says what a useful query should uncover without prescribing a reference query
- Aligning the privilege source to the action type: evidence for search actions, golden answers for answer actions, nothing elsewhere
- A credit rule rather than a distillation loss — the detached teacher-student log-likelihood gap is mapped through a bounded tanh and used to modulate the existing GRPO advantage, so the outcome reward keeps determining update direction and the privileged signal only changes magnitude
- Action-span localization: only the content tokens of generated search and answer actions receive modulated credit, which in practice is 6.7 to 15.1 percent of response tokens
- A controlled ablation isolating the privilege source from the optimization form, since the cross-method comparison confounds the two

## Method

The student samples a trajectory on-policy from the ordinary inference-time context. During training only, a short action-specific hint is prepended to construct a teacher context — the instance's annotated supporting sentences for a search action, the golden answers for an answer action — and the same model re-scores the tokens it just produced under that context. The token-level signal is the stop-gradient log-likelihood ratio between the privileged and ordinary views, so a positive value means the token is more compatible with the evidence-conditioned teacher. That signal is passed through tanh(tau*delta), multiplied by lambda times the magnitude of the token's GRPO advantage and by a binary action mask, and added to the advantage. The construction bounds the correction at lambda times the original advantage, so for lambda below 1 the sign never flips and a token with zero outcome-derived advantage receives no update at all. Everything else — reasoning tokens, delimiters, retrieved passages — keeps its unmodified GRPO credit, and the standard clipped objective with a KL penalty is otherwise unchanged. Backbones are Qwen2.5-7B-Instruct, Qwen2.5-3B-Instruct and Qwen3-1.7B; the retrieval environment follows Search-R1 with the 2018 Wikipedia dump, E5 as dense retriever, top-3 passages and at most four searches per episode; evidence is capped at two documents and two sentences each; training is 300 GRPO steps on 8 GPUs with 8 rollouts per question, 128 questions per step, learning rate 1e-6, KL 0.001, clip 0.2, lambda 0.2 and tau 5. Exact Match is reported on three single-hop and four multi-hop QA sets.

## Results

Macro-average EM is highest in all three settings: 50.8 on Qwen2.5-7B-Instruct against 49.0 for the best skill-conditioned baselines and 48.2 for Search-E1, 47.2 on Qwen2.5-3B-Instruct, and 44.2 on Qwen3-1.7B — margins of 1.3 to 2.3 points. That average conceals the per-benchmark picture at 7B, where EviSD is best on exactly one of seven sets (Bamboogle, 74.6 against GiGPO's 68.9) and is beaten elsewhere, most sharply on HotpotQA where Skill-SD reaches 64.5 against EviSD's 46.6. The controlled ablation is the paper's own strongest evidence for its thesis: holding the training setup fixed and replacing the evidence privilege with answer-only privilege drops the average from 50.8 to 48.7, while sharing a combined evidence-plus-answer context across all actions costs only 0.2, so availability of evidence matters and strict routing barely does. The credit-translation choices matter more than the privilege source: modulating the full response instead of action spans costs 7.1 points and replacing bounded modulation with a response-wide gated auxiliary distillation loss costs 5.8, with the largest degradation on multi-hop tasks. Search behaviour tightens — 1.87 search calls per trajectory against 2.16 for SDAR and 2.27 for RLSD — and on-policy success over second-half checkpoints averages 53.6 percent, 0.9 points above the strongest competitor. The training diagnostics show the teacher-student gap staying separated from zero with the lowest KL drift of the compared methods, while OPSD's gap and KL both diverge as its success collapses. Sensitivity to evidence quality is mild at 1.7B: replacing one of two gold documents with a merely relevant one leaves the average at 44.2 and replacing both costs 0.6.

## Limitations

The paper has no limitations section, and one thing it does state deserves to be read as one: all reported metrics come from a single evaluation run, with no seeds or variance anywhere, while the headline margins are 1.3 to 2.3 points. The macro-average framing also hides that at 7B the method wins one benchmark of seven and loses HotpotQA by 17.9 EM to a skill-conditioned baseline, which the paper does not discuss. The approach needs training instances carrying annotated supporting evidence, which most search-QA corpora outside this benchmark family do not have; Table 4 argues retrieved relevant documents substitute adequately, but that test runs only on the smallest backbone and draws its substitutes from HotpotQA's own distractor field, which is a curated pool rather than live retrieval. lambda and tau are fixed at 0.2 and 5 with the sweep deferred to supplementary material, and the retrieval configuration is held constant throughout (2018 Wikipedia, top-3, at most four searches), so the reduced search count is measured in a setting where more search has a bounded payoff. The extra teacher forward pass per action is called training-only but its cost is not quantified in the main text.

## Why it matters here

- **reasoning-training**: It separates two things the self-distillation literature usually bundles: what the teacher is allowed to know, and how that knowledge enters the objective. The ablation says the second matters more — action-span localization is worth 7.1 points and the bounded-modulation form 5.8, against 2.1 for the choice of privilege source — which is a caution for reading any privileged-teacher result that changes both at once. The design constraint is also worth carrying: because the correction is bounded by the outcome advantage it cannot flip a sign or create an update where the outcome reward is silent, so privileged information refines credit without becoming the objective.

## Entities

- **Concepts**: [credit assignment](../../../../wiki/concepts/credit-assignment.md), privileged information, on-policy self-distillation, [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), [outcome reward](../../../../wiki/concepts/outcome-reward.md), supporting evidence, [search-augmented reasoning](../../../../wiki/concepts/search-augmented-reasoning.md), [multi-hop reasoning](../../../../wiki/concepts/multi-hop-reasoning.md), [teacher-student gap](../../../../wiki/concepts/teacher-student-gap.md)
- **Methods**: EviSD, [GRPO](../../../../wiki/methods/grpo.md), [Search-R1](../../../../wiki/methods/search-r1.md), SD-Search, Search-E1, Skill-SD, SDAR, [GiGPO](../../../../wiki/methods/gigpo.md), [dense retrieval](../../../../wiki/methods/dense-retrieval.md)
- **Datasets**: [Natural Questions](../../../../wiki/datasets/natural-questions.md), [TriviaQA](../../../../wiki/datasets/triviaqa.md), [PopQA](../../../../wiki/datasets/popqa.md), [HotpotQA](../../../../wiki/datasets/hotpotqa.md), [2WikiMultiHopQA](../../../../wiki/datasets/2wikimultihopqa.md), [MuSiQue](../../../../wiki/datasets/musique.md), [Bamboogle](../../../../wiki/datasets/bamboogle.md)

Tags: `self-distillation`, `credit assignment`, `agentic search`, `reinforcement learning`, `privileged information`

## Abstract

Outcome-based reinforcement learning enables search-augmented language agents to learn from verifiable final answers, but its trajectory-level credit cannot distinguish the contributions of individual actions in a multi-turn search process. We propose EviSD, an evidence-conditioned self-distillation framework that uses instance-level supporting evidence as privileged information for search actions and golden answers as complementary privilege for answer actions. During training, the student samples actions from the original context, while the same model re-scores them as a privileged teacher under an action-aligned context. EviSD converts the detached teacher--student gap into a bounded correction to the outcome-derived GRPO advantage and applies it only to generated action spans. This design localizes privileged guidance while preserving the update direction determined by the outcome reward, without an auxiliary distillation objective or any change at inference time. Across seven question-answering benchmarks and three backbones spanning model scales and generations, EviSD achieves the highest macro-average Exact Match in all evaluated settings, outperforming the strongest compared methods by 1.3--2.3 points while modulating only 6.7%--15.1% of response tokens. Code is available at https://github.com/JiananXie/EviSD.

---

Record id: `arxiv:2608.01359`
