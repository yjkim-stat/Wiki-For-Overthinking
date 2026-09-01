<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficient Reasoning for LLMs through Speculative Chain-of-Thought

- **Authors**: Jikai Wang, Juntao Li, Jianye Hou, Yan Bowen, Lijun Wu, Min Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.76/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.76.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.76
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Speculative Chain-of-Thought (SCoT) speeds up reasoning-model latency by having a fine-tuned small draft model generate multiple parallel CoT drafts thought-level (not token-level) which a fine-tuned target model selects from or corrects, reducing reasoning latency 48-66% (32B target) and 21-49% (70B target) while staying near target-model accuracy.

## Problem

Large reasoning models incur high inference latency from both massive parameter count and long chain-of-thought generation; existing efficient-reasoning methods either shrink the model (distillation) or shorten the CoT (compression), but always using a large model even for simple tasks wastes compute, while using only a small model or a shortened CoT compromises accuracy on genuinely complex tasks.

## Contributions

- Speculative Chain-of-Thought (SCoT), reframing speculative decoding at the thought level: a small draft model generates full candidate CoTs in parallel, and a target model selects or corrects rather than verifying token-by-token
- Thinking Behavior Alignment, LoRA fine-tuning the draft model on the target model's own CoT style, which is shown necessary because naive small-model drafts can be markedly longer and more redundant than the target's own reasoning
- an implicit difficulty-aware routing mechanism (the target model's error-correction/rethink option) that allocates more of the target model's own reasoning to harder problems without requiring explicit difficulty labels
- 48-66% (32B) and 21-49% (70B) reasoning-latency reduction at near-target-model accuracy across five datasets of varying difficulty, outperforming both a CoT-compression baseline (TokenSkip) and standard token-level speculative decoding using the same model pairs

## Method

A lightweight draft model M_d generates n (default 5) candidate chains-of-thought in parallel via temperature sampling from the question alone -- 'thought-level' rather than token-level speculation, unlike standard speculative decoding. Thinking Behavior Alignment fine-tunes the draft model via LoRA on 1500 GSM8K samples labeled with the target model's own generated CoTs, since naive small-model drafts contain more redundant reflections and can be 4x longer than the target model's CoTs of the same series, actually slowing things down without alignment. The target model, also LoRA-fine-tuned (on 500 GSM8K samples), performs Draft Selection and Error Correction: a single forward pass selects the best draft index via next-token argmax over a prompt template listing all n drafts plus a special 'all drafts wrong' option T_{n+1}; if a draft is selected, the target model generates the final answer conditioned on it (fast path); if T_{n+1} is selected (task too hard for the draft model), the target model rethinks and generates its own full CoT (fallback path) -- giving the framework a built-in difficulty-aware routing mechanism with no explicit difficulty labels needed. Evaluated with Deepseek-R1-Distill-Qwen-32B and Deepseek-R1-Distill-Llama-70B as target models (paired with 1.5B and 8B same-family draft models respectively) on GSM8K, MATH, GaoKao, CollegeMath, and Olympiad.

## Results

SCoT reduces reasoning latency by 48-66% for the 32B target and 21-49% for the 70B target across the five datasets while achieving near-target-model-level accuracy (e.g. Qwen group average: 71.9% for SCoT vs. 71.1% for the standalone 32B target model; on CollegeMath SCoT even exceeds the target model's own accuracy, 66.2% vs. 63.8%). SCoT achieves a 2.3x average speed-up ratio for the Qwen group and 1.6x for the Llama group versus vanilla decoding, and consistently beats TokenSkip (a CoT-compression baseline at matched ~0.5 compression ratio) on both speed-up and accuracy on most datasets except Olympiad, where TokenSkip is faster but SCoT has the better accuracy-efficiency trade-off overall. Against standard token-level speculative decoding using the same draft/target model pairs, SCoT achieves higher throughput on all datasets (up to 2.96x speed-up ratio) and, notably, exhibits far less latency degradation on the longest-sequence dataset (Olympiad, avg. generation >5000 tokens) where standard speculative decoding's per-token verification overhead grows with sequence length and can even slow decoding down, while SCoT's single draft-verify-select cycle is largely insensitive to sequence length. Ablations confirm all three components matter: removing thinking-behavior-alignment, using a single draft instead of 5, or removing the error-correction/rethinking mechanism each reduce accuracy versus the full method. Task-difficulty routing works as intended: draft-model prediction accuracy on 'easy' (draft-model-solvable) GSM8K test samples is 85.1%, but only 52.1% on 'hard' samples the draft model cannot solve alone -- yet even on these hard samples, fine-tuning lets the target model correctly identify about half as needing rethinking (versus 0% correct identification without fine-tuning). A chain-count sweep (1-8 drafts) finds 5 the empirical sweet spot: too few drafts limits the odds of a high-quality candidate being present, while too many complicates the target model's selection task and can degrade accuracy despite faster raw throughput.

## Limitations

SCoT requires an existing pre-trained reasoning model of the same family to serve as the draft model, which may not always be available for a given target model; draft-model size relative to the target matters a lot (the paper's own 8B-70B Llama pairing shows a lower speed-up than the 1.5B-32B Qwen pairing, attributed to the 8B draft still being relatively large for the 70B target). SCoT requires fine-tuning both the draft and target models, and due to resource limitations the paper only evaluates on mathematical reasoning tasks trained with limited data (500-1500 GSM8K samples); performance on other reasoning task types, especially out-of-domain ones, is untested. The authors also flag a safety caveat: because SCoT changes the target model's original output distribution, it may affect the pre-trained model's original safety alignment and would need reconsideration before real-world deployment.

## Why it matters here

- **overthinking**: Directly relevant as an architectural/systems-level efficiency lever distinct from length-penalty or trace-shortening approaches: rather than making a single model's reasoning shorter, SCoT changes *who* does the reasoning per-problem -- routing easy problems entirely to a cheap draft model and reserving the expensive target model's own reasoning for problems the draft model cannot solve, an implicit form of the difficulty-adaptive compute allocation this archive's overthinking-mitigation literature repeatedly proposes, but achieved through a large/small-model collaboration mechanism rather than through the target model's own trace length.

## Entities

- **Concepts**: thought-level speculation (vs. token-level speculative decoding), thinking behavior alignment, difficulty-aware draft/target routing, draft selection and error correction
- **Methods**: Speculative Chain-of-Thought (SCoT), Thinking Behavior Alignment (LoRA fine-tuning), Draft Selection and Error Correction, TokenSkip (CoT-compression baseline), standard token-level speculative decoding (baseline)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH](../../../../wiki/datasets/math.md), GaoKao-En-2023, CollegeMath, Olympiad (OlympiadBench)

Tags: `efficient-reasoning`, `speculative-decoding`, `difficulty-aware-routing`, `latency`, `large-small-model-collaboration`

## Abstract

Large reasoning language models such as OpenAI-o1 and Deepseek-R1 have recently attracted widespread attention due to their impressive task-solving abilities. However, the enormous model size and the generation of lengthy thought chains introduce significant reasoning costs and response latency. Existing methods for efficient reasoning mainly focus on reducing the number of model parameters or shortening the chain-of-thought length. In this paper, we introduce Speculative Chain-of-Thought (SCoT), which reduces reasoning latency from another perspective by accelerated average reasoning speed through large and small model collaboration. SCoT conducts thought-level drafting using a lightweight draft model. Then it selects the best CoT draft and corrects the error cases with the target model. The proposed thinking behavior alignment improves the efficiency of drafting and the draft selection strategy maintains the prediction accuracy of the target model for complex tasks. Experimental results on GSM8K, MATH, GaoKao, CollegeMath and Olympiad datasets show that SCoT reduces reasoning latency by 48%∼66% and 21%∼49% for Deepseek-R1-Distill-Qwen-32B and Deepseek-R1-Distill-Llama-70B while achieving near-target-model-level performance.

---

Record id: `doi:10.18653/v1/2026.findings-acl.76`
