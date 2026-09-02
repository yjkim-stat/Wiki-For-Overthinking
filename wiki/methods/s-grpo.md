# S-GRPO

<!-- auto:begin -->

The two sources that mention S-GRPO do not explain its mechanism: the survey on efficient R1-style reasoning models includes it as one instance in its taxonomy of single-model-optimization methods, and IAPO cites it only in comparison while describing its own token-level mutual-information reward shaping. S-GRPO's own approach is not described in the material supplied here.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [A*-Thought](a-thought.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAPO](dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAST](dast.md), [DeepSeek-R1-Distill-8B](../models/deepseek-r1-distill-8b.md), [DEER](deer.md), [DRP](drp.md), [Early Exit](early-exit.md), [GFPO](gfpo.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [NOWAIT](nowait.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [Reasoning Completion Point (RCP)](../concepts/reasoning-completion-point-rcp.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [semantic path convergence](../concepts/semantic-path-convergence.md), [SPIRIT](spirit.md), [stepwise truncation protocol](stepwise-truncation-protocol.md), [thinking-content compensation](../concepts/thinking-content-compensation.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## What we have settled

- **Established** — The ACL 2026 camera-ready of 'The Evolution of Thought' removes the S-GRPO comparison its arXiv v2 preprint reports, and with it the only result in the paper where RCPD is beaten -- so a reader of the published version cannot see that the method was measured against a baseline that outperformed it on AIME24.
  - Both versions are held here: the archive's record carries the arXiv v2 document, and the camera-ready PDF was read before the two records were merged. In arXiv v2 the baselines sentence reads 'We compare against Full Reasoning, Budget Force (BF), No-Think, and DEER; we also report S-GRPO, which requires additional LLM training', Table 1 carries S-GRPO rows, and the text concedes the outcome: RCPD 'outperforms S-GRPO on GPQA-D despite underperforming on AIME24'. The numbers behind that concession are, on Qwen3-8B/AIME24, S-GRPO at 8,810 tokens and 77.30 accuracy against RCPD's 9,958 tokens and 72.22 -- fewer tokens and five points better -- reversing on GPQA-D, where RCPD reaches 64.65 at 4,130 tokens against S-GRPO's 55.40 at 5,271. In the camera-ready the sentence ends at 'and DEER', the S-GRPO rows are gone from Table 1, and the concession sentence is absent; 'S-GRPO' survives only once, in Related Work, as a method that 'necessitates extra training'. The string occurs 8 times in the preprint and once in the camera-ready. This is a fact about what the two documents contain, not a claim about the authors' reasons: S-GRPO is a training-based method and dropping it from an inference-time comparison is a defensible editorial choice. The consequence for this archive is narrower and does not depend on motive -- an evaluation of RCPD built only on the published version overstates how it stands against the alternatives, and the archive holds both versions precisely so that it does not have to.

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/local-7c50df663462f26b/summary.md) — Defines an instance-specific Reasoning Completion Point (RCP) as the earliest truncation step at which both content-length stabilization and semantic-distribution convergence hold, and detects it online by monitoring the rank of the </think> token, cutting tokens up to 44% while preserving accuracy across four Qwen3 scales and DeepSeek-R1-Distill-8B.
- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.

## Checked against

- [https://aclanthology.org/2026.acl-long.1239](https://aclanthology.org/2026.acl-long.1239) — aclanthology.org · proceedings-page · retrieved 2026-09-03
  - _The venue's own listing for the camera-ready: 'The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis', Zihao Wei, Liang Pang, Jiahao Liu, Wenjie Shi, Jingcheng Deng, Shicheng Xu, Zenghao Duan, Jingang Wang, Fei Sun, Huawei Shen, Xueqi Cheng; Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 26905-26920, July 2026, San Diego, California. The page links the camera-ready PDF and names no arXiv preprint version, which is why the DOI and the arXiv id were never associated. In the PDF it serves, the baseline sentence of section 5.3 reads in full: 'We compare against Full Reasoning, Budget Force (BF), No-Think, and DEER.' The arXiv v2 preprint of the same work ends that sentence differently: '...and DEER; we also report S-GRPO, which requires additional LLM training.'_

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
