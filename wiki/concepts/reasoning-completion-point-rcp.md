# Reasoning Completion Point (RCP)

<!-- auto:begin -->

The Reasoning Completion Point is the earliest step of a large reasoning model's thinking trajectory at which its emerging answer has stopped changing in two independent senses at once: the content the model would produce if forced to stop there has stabilized in length (Delta_content(k) <= eps_c), and the distribution over that induced content has converged toward its terminal form (D_global(k) = KL(Q_k || Q_inf) <= eps_D). Its single archived source uses the point to split a trace into a Pre-RCP active-reasoning stage, where further thinking is typically still needed for the answer to mature, and a Post-RCP converged stage, where additional steps no longer materially alter the induced content and accumulate as redundancy. The point is latent and instance-specific, so no fixed thinking-token budget locates it, and computing it requires sampling several continuations at every truncation step, which makes it obtainable only offline; the source therefore uses it as gold supervision for an online detector rather than applying it directly. It is reported to coincide typically with the first emergence of the final answer in the trace, though the source notes answer emergence itself is an unreliable detection target because answer surface forms vary.

- **Kind**: concept
- **Also called**: RCP
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-8B](../models/deepseek-r1-distill-8b.md), [DEER](../methods/deer.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [Latent reasoning](latent-reasoning.md), [MATH500](../datasets/math500.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [S-GRPO](../methods/s-grpo.md), [semantic path convergence](semantic-path-convergence.md), [stepwise truncation protocol](../methods/stepwise-truncation-protocol.md), [thinking-content compensation](thinking-content-compensation.md)

## What we have settled

- **Established** — The ACL 2026 camera-ready of 'The Evolution of Thought' removes the S-GRPO comparison its arXiv v2 preprint reports, and with it the only result in the paper where RCPD is beaten -- so a reader of the published version cannot see that the method was measured against a baseline that outperformed it on AIME24.
  - Both versions are held here: the archive's record carries the arXiv v2 document, and the camera-ready PDF was read before the two records were merged. In arXiv v2 the baselines sentence reads 'We compare against Full Reasoning, Budget Force (BF), No-Think, and DEER; we also report S-GRPO, which requires additional LLM training', Table 1 carries S-GRPO rows, and the text concedes the outcome: RCPD 'outperforms S-GRPO on GPQA-D despite underperforming on AIME24'. The numbers behind that concession are, on Qwen3-8B/AIME24, S-GRPO at 8,810 tokens and 77.30 accuracy against RCPD's 9,958 tokens and 72.22 -- fewer tokens and five points better -- reversing on GPQA-D, where RCPD reaches 64.65 at 4,130 tokens against S-GRPO's 55.40 at 5,271. In the camera-ready the sentence ends at 'and DEER', the S-GRPO rows are gone from Table 1, and the concession sentence is absent; 'S-GRPO' survives only once, in Related Work, as a method that 'necessitates extra training'. The string occurs 8 times in the preprint and once in the camera-ready. This is a fact about what the two documents contain, not a claim about the authors' reasons: S-GRPO is a training-based method and dropping it from an inference-time comparison is a defensible editorial choice. The consequence for this archive is narrower and does not depend on motive -- an evaluation of RCPD built only on the published version overstates how it stands against the alternatives, and the archive holds both versions precisely so that it does not have to.

## Appears in

- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/local-7c50df663462f26b/summary.md) — Defines an instance-specific Reasoning Completion Point (RCP) as the earliest truncation step at which both content-length stabilization and semantic-distribution convergence hold, and detects it online by monitoring the rank of the </think> token, cutting tokens up to 44% while preserving accuracy across four Qwen3 scales and DeepSeek-R1-Distill-8B.

## Checked against

- [https://aclanthology.org/2026.acl-long.1239](https://aclanthology.org/2026.acl-long.1239) — aclanthology.org · proceedings-page · retrieved 2026-09-03
  - _The venue's own listing for the camera-ready: 'The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis', Zihao Wei, Liang Pang, Jiahao Liu, Wenjie Shi, Jingcheng Deng, Shicheng Xu, Zenghao Duan, Jingang Wang, Fei Sun, Huawei Shen, Xueqi Cheng; Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 26905-26920, July 2026, San Diego, California. The page links the camera-ready PDF and names no arXiv preprint version, which is why the DOI and the arXiv id were never associated. In the PDF it serves, the baseline sentence of section 5.3 reads in full: 'We compare against Full Reasoning, Budget Force (BF), No-Think, and DEER.' The arXiv v2 preprint of the same work ends that sentence differently: '...and DEER; we also report S-GRPO, which requires additional LLM training.'_

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
