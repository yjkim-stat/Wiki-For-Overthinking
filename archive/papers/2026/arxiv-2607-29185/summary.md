<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Learning Latent Reasoning Traces for Scalar Reward Models End-to-End

- **Authors**: Sanwoo Lee, Clive Bai, Hsiu-Yuan Huang, Kun Liang, Weijie Liu, Yunfang Wu
- **Venue**: cs.CL
- **Published**: 2026-07-31
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2607.29185>
- **PDF**: <https://arxiv.org/pdf/2607.29185v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

LatentRM treats a reward model's chain-of-thought critique as a discrete latent variable and trains the generator with REINFORCE against the downstream scalar reward model's log-likelihood of the true preference ranking, rather than against a hand-designed reasoning reward.

## Problem

Scalar reward models are cheap and give calibrated continuous scores but latch onto superficial cues and degrade under distribution shift; generative (LLM-as-judge) reward models reason before scoring and are more robust but emit scores as text, losing numerical flexibility and probabilistic interpretation. Hybrid systems train a generator and a scalar head in parallel with separate objectives — typically a Kendall's tau correctness reward for the generator and Bradley-Terry/Plackett-Luce loss for the head — which does not guarantee that the reasoning the generator produces is the reasoning the scalar head needs. Earlier reasoning-augmented scalar RMs fine-tune on static critiques from a teacher or from self-refinement, so the critiques drift off-policy as training proceeds.

## Contributions

- Formulates reward-model reasoning as a discrete latent variable in a generator-scalar-RM conditional generative model, replacing hand-designed generator rewards with the downstream preference log-likelihood.
- Derives an ELBO whose variational posterior is shared with the prior, avoiding a second label-conditioned LLM, and turns it into a joint on-policy update: supervised for the scalar head, REINFORCE with a rollout-mean baseline for the generator.
- Shows the end-to-end objective beats a parallel multi-task hybrid on OOD reward benchmarks (RM-Bench 82.8 vs 81.7, PPE 72.1 vs 71.9) and both by wide margins over scalar-only and generative-only RMs.
- Reports that a Kendall's tau reward for the generator does not even maximize Kendall's tau when the reasoning is an intermediate variable for a scalar head.
- Evidence that the scalar head uses the reasoning rather than echoing its verbalized score: when the generator's stated score is wrong, LatentRM's head still ranks correctly 68.1% of the time vs 57.9% for the multi-task baseline.

## Method

Input x is a prompt plus k candidate responses (k >= 1, varying per prompt, so pointwise and pairwise are special cases). A generator LLM p_theta(z|x) samples a rubric-structured critique z that ends with an explicit per-response score in <score_i> tags; the concatenation (x, z) is fed to a scalar RM p_phi initialized as a copy of the generator with the LM head replaced by a random scalar head w. The last-layer hidden states at the k token positions immediately preceding each generated score value are stacked into H, and rewards are s = w^T H. A listwise Plackett-Luce likelihood over s defines p_phi(y|x,z), reducing to Bradley-Terry at k=2; ties are handled by summing over consistent total orders. Reasoning is then a discrete latent variable in a conditional generative model, and training maximizes log p(y|x) = log E_{z~p_theta}[p_phi(y|x,z)] via its ELBO. Rather than train a separate posterior network q(z|x,y) — which the authors argue would both cost a second LLM and invite post-hoc justification of whatever label it is shown — they set q = p_theta, which by Jensen still gives a valid lower bound and collapses the objective to max_{theta,phi} E_{z~p_theta}[log p_phi(y|x,z)]. The phi gradient is ordinary supervised learning on the sampled critiques; the theta gradient is REINFORCE with log p_phi(y|x,z) as the reward, so the reasoning reward is not hand-designed but is exactly the downstream likelihood. Variance is reduced with a leave-in mean baseline over m rollouts per prompt; format-violating rollouts get advantage min(valid advantages) - 1, or -1 if all rollouts are invalid. Both parameter sets update every step, fully on-policy, with no scalar-RM warmup.

## Results

Backbone Qwen3-4B-Instruct-2507 for LatentRM and all internal baselines. Training pool of 80K preference-annotated samples (UltraFeedback 28K, OpenMathReasoning 28K, HelpSteer3 STEM/Code 8K, WildGuard adversarial 8K, OffsetBias 8K), filtered down 40% by a split-and-filter protocol that trains MLP ensembles on 220-dimensional LFTK surface features and discards the samples with smallest held-out loss, leaving 43,201 train / 4,799 test. VERL + vLLM, 8 rollouts per prompt at temperature 1.0, max prompt 16,384 and max response 8,192, batch 128, one epoch, pure on-policy without PPO minibatching. In-distribution: LatentRM reaches micro-average Kendall's tau 0.712 and macro 0.759 against MultitaskRM 0.706/0.756, ScalarRM 0.673/0.718, GenerativeRM 0.588/0.611 — so the margin over the multi-task hybrid is 0.003-0.006, while the margin over the non-hybrid baselines is large. Log-likelihood micro-average -1.031 vs -1.053 (MultitaskRM) and -1.175 (ScalarRM). Out of distribution: RM-Bench average 82.8 vs 81.7 (MultitaskRM), 81.3 (GenerativeRM), 75.7 (ScalarRM); PPE Correctness average 72.1 vs 71.9, 64.0, 65.8. The RM-Bench Hard subset, which stresses style bias, is where the gain is largest (81.3 vs 80.1 MultitaskRM, 61.6 ScalarRM). Against external models at much larger scale, LatentRM at 4B reports 82.8 RM-Bench / 72.1 PPE vs J1-70B 82.7/70.2 and CLoud-Gemma2-27B 62.4 PPE, though the authors note different data and backbones make these not directly comparable. RLHF: 100 GRPO steps on Qwen3-4B-Instruct, 4 rollouts, max 4,096 tokens, judged by Qwen3.7-plus with the length-controlled AlpacaEval winrate formula, 200 samples per subset, single run at seed 42. LatentRM-guided policy wins 56.9% LC against the base policy, 58.5% against the ScalarRM-guided policy, 52.0% against MultitaskRM and 51.5% against GenerativeRM; its policy also emits the shortest average outputs of all the RLHF runs (1,289 tokens vs 1,474 for ScalarRM, 1,352 MultitaskRM, 1,310 GenerativeRM, 1,278 for the un-RL'd base). Per-domain it loses to MultitaskRM on safety (WildGuard 47.6%) and adversarial (OffsetBias 48.1%). A score-gap analysis reports that when the generator's verbalized score is wrong, the downstream scalar head still ranks correctly 68.1% of the time under LatentRM vs 57.9% under MultitaskRM. All numbers are software measurements; RL results are single-seed.

## Limitations

The paper states no limitations section in the text read. Noticeable: the margin over the MultitaskRM hybrid is small and unreplicated — 0.003-0.006 Kendall's tau in distribution, 1.1 points on RM-Bench, 0.2 points on PPE — and every RL experiment is a single run at a fixed seed, so the ordering between LatentRM and MultitaskRM rests on point estimates without variance. LatentRM is worse than MultitaskRM on safety and adversarial domains in both the ID table and the RLHF winrates; the authors attribute this to UltraFeedback and OpenMathReasoning making up 70% of training data, which is a hypothesis they do not test. Everything is one 4B backbone and one epoch, so scaling behavior is unknown. The variational step sets q(z|x,y) = p_theta(z|x), which makes the bound valid but loose and gives up any label-conditioned posterior; the resulting KL term vanishes, so nothing constrains how far the generator's reasoning distribution moves. The 40% data filter is itself a design choice made on surface features and applied before all comparisons. The reported inference cost of generating a critique per scoring call is not quantified anywhere. The external-baseline table compares across different data curation and backbones and the authors say so.

## Why it matters here

- **overthinking**: Largely tangential: the match is the phrase 'reasoning trace', but the trace here belongs to a reward model writing a critique, and the paper never studies how long that trace should be. There is no length budget, no test-time compute sweep, no accuracy-versus-tokens curve; the reasoning is always generated in full and the only cap is a fixed 8,192-token rollout limit. Two secondary observations do touch the topic and are worth keeping. First, the RLHF section measures output length of the aligned policies: the LatentRM-guided policy produces the shortest average responses (1,289 tokens) of all four RLHF runs while winning on LC win rate, whereas the plain scalar RM drives length up to 1,474 from a 1,278-token base — a concrete instance of length inflation as reward overoptimization, which is the RLHF-side counterpart of overthinking. Second, LatentRM's largest OOD gain is on RM-Bench's Hard subset (81.3 vs 61.6 for the scalar RM), which is specifically constructed to punish preference for longer and more heavily formatted answers. Neither result is about making a reasoning model stop at the right point, so this should not be read as evidence on the accuracy/efficiency tradeoff; it is relevant only as background on why reward signals push generations to get longer.

## Entities

- **Concepts**: Reward Modeling, Latent Variable Reasoning, Generative vs Scalar Reward Models, Evidence Lower Bound, On-Policy vs Off-Policy Critique, Reward Overoptimization, Length-Controlled Win Rate, Style Bias in LLM Judges
- **Methods**: LatentRM, Plackett-Luce listwise likelihood, Bradley-Terry, ELBO with shared prior/posterior, REINFORCE with rollout-mean baseline, GRPO (for RLHF), MultitaskRM, GenerativeRM, ScalarRM (baselines), split-and-filter data selection with LFTK features, VERL, vLLM, Qwen3-4B-Instruct-2507 (backbone)
- **Datasets**: UltraFeedback, OpenMathReasoning, HelpSteer3 (STEM and Code subsets), WildGuard (adversarial subset), OffsetBias, RM-Bench, PPE Correctness

Tags: `reward-model`, `rlhf`, `latent-variable`, `reinforce`, `preference-modeling`, `ood-generalization`, `qwen3`

## Abstract

Reward models (RMs) are central to aligning large language models with human preferences via reinforcement learning. Although traditional scalar RMs enable efficient and probabilistic reward modeling, they rely on superficial cues that fail to generalize to complex or out-of-distribution (OOD) tasks. Conversely, generative RMs leverage extensive reasoning to improve robustness on challenging tasks, but their natural language-based scores lack the numerical flexibility and probabilistic interpretability that scalar RMs offer. While recent approaches combine both paradigms through off-policy multi-task learning, such parallel optimization does not guarantee that generated reasoning traces actively align with or benefit downstream scalar reward prediction. To address this mismatch, we propose LatentRM, a reward modeling framework that learns intermediate reasoning traces as discrete latent variables to explicitly maximize the likelihood of downstream scalar rewards. Through on-policy optimization of the latent reasoning space end-to-end, LatentRM tightly couples deep reasoning-based evaluation with precise scoring. Extensive validations on in-distribution and OOD datasets and RLHF show that LatentRM outperforms scalar, generative, and hybrid RMs on preference modeling and policy alignment across tasks ranging from open-ended conversation to complex reasoning.

---

Record id: `arxiv:2607.29185`
