<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# One Token Embedding Is Enough to Deadlock Your Large Reasoning Model

- **Authors**: Mohan Zhang, Yihua Zhang, Jinghan Jia, Zhangyang Wang, Sijia Liu, Tianlong Chen
- **Venue**: 39th Conference on Neural Information Processing Systems (NeurIPS 2025)
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: overthinking

## In one line

Trains a single adversarial token embedding, implanted into an open-weight large reasoning model via a backdoor trigger, that hijacks the model's chain-of-thought into a perpetual reasoning loop, achieving a 100% attack success rate (forcing generation to the token limit) across four models and three benchmarks while leaving benign-input accuracy essentially unchanged.

## Problem

Reasoning models allocate variable, sometimes excessive, test-time compute to chain-of-thought reasoning (overthinking), a phenomenon usually studied as an efficiency nuisance. This paper asks whether that same iterative reasoning mechanism can instead be adversarially and reliably weaponized into a targeted, input-agnostic denial-of-service-style resource-exhaustion attack — a threat surface prior adversarial-attack and backdoor literature on LLMs had not examined, since existing attacks focus on compromising output accuracy or safety rather than hijacking the reasoning process's control flow itself.

## Contributions

- Initiates the study of resource exhaustion attacks on LRMs, identifying their test-time computational scaling and reasoning dynamics as a new vulnerable adversarial surface.
- Develops the Deadlock Attack, an efficient method that uses a single adversarial token embedding to hijack the model's reasoning pathway, inducing perpetual thinking loops and exhausting computational resources.
- Uncovers the continuous-to-discrete projection gap in converting adversarial embeddings into discrete tokens, and proposes a practical backdoor mechanism that embeds the adversarial vector as an explicit trigger token to overcome it.
- Conducts experiments on four LRMs (Phi-RM, Nemotron-Nano, R1-Qwen, R1-Llama) across three benchmarks (GSM8K, MATH500, MMLU-Pro), showing the attack is highly effective and stealthy, and that existing overthinking-mitigation strategies (Chain of Draft, Concise CoT, NoThinking) fail to defend against it.

## Method

This is not an inference-time steering or guidance method in the sense of adjusting logits, attention, or the sampling distribution during ordinary decoding; it is an adversarial attack that plants a fixed, malicious intervention into a model's embedding matrix before deployment; the intervention is triggered by, but not decided by, anything computed at inference time.

Phase 1 (attack construction, white-box, done once by the attacker): a continuous adversarial embedding e_adv (length L, default L=1 token) is optimized and prepended to the token embeddings of a (problem, answer) pair fed to the model: X = [e_adv; g(P); g(A)]. The optimization objective (Eq. 3-4) maximizes, averaged over all positions in the answer immediately following end-of-step punctuation (".", "?"), the softmax probability the model assigns to a small set of transitional/hesitation tokens (e.g. "Wait", "But") as the next token. Gradients are backpropagated only into e_adv (Adam, lr=1e-3, weight decay 0, β1=0.9, β2=0.999, 1000 steps), using a calibration set of the first 30 level-5 MATH500 problems, each paired with 100 sampled R1-Qwen answers (10 held out per problem for validation).

Phase 2 (deployment): because a real attacker can typically only inject discrete tokens rather than raw continuous embeddings, and because naively projecting e_adv onto its nearest vocabulary token destroys the attack (shown via a Linear Mode Connectivity analysis: the projection error consistently exceeds the perturbation tolerance of the optimized embedding, Fig. 2), the attacker instead directly overwrites the embedding-matrix rows of a chosen L-token discrete trigger sequence (e.g. the literal string "!!!!!", or visually-identical homoglyph characters) with the optimized vectors [v_1,...,v_L]. This produces a backdoored checkpoint that behaves like the clean model on any input lacking the trigger, but reproduces the deadlock effect whenever the trigger tokens appear in the prompt.

Where it intervenes: the input token embedding matrix, at the embedding(s) of a designated trigger token sequence prepended to the user's prompt — not any per-step logit, attention weight, or sampling parameter during generation.
What quantity decides the intervention: at construction time, a gradient-optimized scalar objective (average post-punctuation probability of transitional tokens); at deployment, nothing is computed online — the intervention fires deterministically whenever the fixed trigger token(s) are present in the tokenized input.
When it fires: once, at the token position(s) occupied by the trigger in the prompt; its effect (biasing the model toward endlessly re-choosing "Wait"/"But" after each reasoning step) then persists through the entire subsequent generation.
What it costs: attacker-side, one-time optimization of 1000 Adam steps over roughly 2,000 (problem, answer) pairs derived from 20-30 calibration problems, requiring white-box gradient access to the victim model — this is a training-time cost paid once per victim model, not per query. At inference/deployment time the direct cost to the attacker is negligible (one extra token in the prompt); the cost the attack imposes is on the victim: activated queries are driven to the maximum generation limit in up to 100% of cases (e.g. from a baseline of 2-4% natural over-length rate to 100% under the trigger), with average generated tokens rising from a few hundred/thousand to the full cap (4000, or 20,000 in the extended evaluation) and average inference time per query rising roughly 3-4x (e.g. R1-Llama: 26.45s baseline to 102.7s attacked at the 4000-token cap).

## Results

Table 2 (attack effectiveness, 4000-token cap): Deadlock Attack (DA) achieves 100% Attack Success Rate (ASR) across all four models (Phi-RM, Nemotron-Nano, R1-Qwen, R1-Llama) on GSM8K, MATH500 and MMLU-Pro(Math), versus baseline (undefended) ASR of 0-8%; average tokens hit the 4000 cap under attack versus 513-1631 tokens at baseline; average inference time rises roughly 3-4x (e.g. R1-Llama: 26.45s to 118.02-119.42s). Table 3: under three test-time overthinking-mitigation strategies (Chain of Draft, Concise CoT, NoThinking) applied on top of the attacked models on GSM8K, ASR remains 100% for all four models under all three mitigation strategies, and average inference time per query stays close to the undefended-attack level (e.g. Phi-RM: 118.41s with no mitigation vs. 117.31s/105.08s/103.44s under CoD/CCoT/NoThinking respectively) — i.e. none of the three mitigation strategies reduces ASR below 100% or meaningfully shortens the deadlocked generation. Table 4 (stealthiness): accuracy on benign inputs without the trigger changes only marginally between clean and backdoored (DA) checkpoints (e.g. Phi-RM 94.0->96.0 on GSM8K, 88.4->90.7 on MATH500 L1; R1-Llama 80.0->80.6 on GSM8K, 93.0->86.8 on MATH500). Appendix C.1 (extended 20,000-token cap, includes AIME): DA maintains 93.33-100% ASR across GSM8K/MATH500/MMLU-Pro(Math)/AIME, versus a natural baseline over-length rate of only 13.33-16.67% even on the hardest benchmark (AIME), showing the attack induces a qualitatively different failure mode rather than merely amplifying natural difficulty-driven verbosity. Appendix C.2 (large-scale stealthiness, 500 samples per benchmark across 6 diverse tasks including HumanEval and CommonsenseQA): accuracy differences between clean and backdoored models are reported as statistically negligible across all six benchmarks. A single-token adversarial embedding (L=1) is sufficient and as effective as longer embeddings (L=2,5,10), though longer embeddings converge faster during training (Fig. 5L); attack effectiveness requires a training set of diverse problems (N=20 problems x 100 answers) to generalize to unseen inputs, whereas N=1 converges in training loss but generalizes poorly (Fig. 5R).

## Limitations

Stated: the attack assumes white-box access to the victim LRM's parameters and the ability to distribute a modified (backdoored) checkpoint publicly, e.g. via an open model hub — a realistic but specific supply-chain threat model rather than a black-box remote attack. The continuous-to-discrete projection problem is only worked around via the backdoor mechanism, not solved in general: the paper states that developing principled methods for translating continuous adversarial embeddings into discrete token triggers on closed-source APIs (query-based / zeroth-order optimization) remains a critical open challenge, as does transferability of the deadlock-inducing pattern across model families. A proposed naive defense (monitoring for repetitive token patterns during generation) is discussed only conceptually and never implemented or tested against the attack; the paper itself notes such a defense would add inference overhead for all queries and could be circumvented by attacks avoiding literal repetition.

Not stated, and worth noticing: all reported attack-success numbers assume the victim actually downloads and deploys the specific backdoored checkpoint the attacker released — the paper does not address how an attacker gets a target service to adopt that particular checkpoint over the many other public checkpoints of the same base model, which is a real-world adoption barrier the security framing elides. Also, the extended-generation-limit experiment (Appendix C.1, 20,000 tokens) still stops at a fixed cap rather than truly unbounded generation, so the reported ASR at that cap is itself a censored version of "how long the deadlock persists," not a measurement of an unbounded loop.

## Why it matters here

- **overthinking**: Directly weaponizes the overthinking phenomenon: shows a model's natural tendency toward variable-length reasoning traces can be adversarially amplified via a single backdoored token embedding into a resource-exhaustion attack that forces generation to the maximum token limit, and demonstrates that existing overthinking-mitigation strategies (Chain of Draft, Concise CoT, NoThinking) all fail to defend against it (Table 3) — a finding directly relevant to evaluating how robust any inference-time length-control method is against adversarial rather than merely natural overthinking.

## Entities

- **Concepts**: Deadlock Attack, adversarial embedding optimization, continuous-to-discrete projection gap, backdoor implantation, transitional token induction, linear mode connectivity, resource exhaustion attack, input-agnostic universal trigger, attack stealthiness
- **Methods**: [Deadlock Attack](../../../../wiki/methods/deadlock-attack.md), [adversarial embedding optimization](../../../../wiki/methods/adversarial-embedding-optimization.md), backdoor implantation via embedding-matrix overwrite, Linear Mode Connectivity analysis, Gaussian-smoothed robust optimization (attempted, found insufficient), iterative projection during optimization (attempted, found insufficient)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), MMLU-Pro (Math subset), [AIME 2024](../../../../wiki/datasets/aime-2024.md), HumanEval (Python subset), MMLU-Pro (Health subset), [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md)

Tags: `overthinking`, `adversarial attack`, `backdoor`, `resource exhaustion`, `deadlock attack`, `chain-of-thought`, `denial-of-service`, `large reasoning models`, `adversarial embedding`, `security`, `supply chain`

## Abstract

Modern large reasoning models (LRMs) exhibit impressive multi-step problem-solving via chain-of-thought (CoT) reasoning. However, this iterative thinking mechanism introduces a new vulnerability surface. We present the Deadlock Attack, a resource exhaustion method that hijacks an LRM's generative control flow by training a malicious adversarial embedding to induce perpetual reasoning loops. Specifically, the optimized embedding encourages transitional tokens (e.g., "Wait", "But") after reasoning steps, preventing the model from concluding its answer. A key challenge we identify is the continuous-to-discrete projection gap: naïve projections of adversarial embeddings to token sequences nullify the attack. To overcome this, we introduce a backdoor implantation strategy, enabling reliable activation through specific trigger tokens. Our method achieves a 100% attack success rate across four advanced LRMs (Phi-RM, Nemotron-Nano, R1-Qwen, R1-Llama) and three math reasoning benchmarks, forcing models to their maximum token limits. The attack is also stealthy (in terms of causing negligible utility loss on benign user inputs) and remains robust against existing strategies trying to mitigate the overthinking issue. Our findings expose a critical and underexplored security vulnerability in LRMs from the perspective of reasoning (in)efficiency.

---

Record id: `local:398417af52a576de`
