<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# How Should We Enhance the Safety of Large Reasoning Models: An Empirical Study

- **Authors**: Zhexin Zhang, Xian Qi Loye, Victor Shea-Jay Huang, Junxiao Yang, Qi Zhu, Shiyao Cui, Fei Mi, Lifeng Shang, Yingkang Wang, Hongning Wang, Minlie Huang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.936/>
- **PDF**: <https://aclanthology.org/2026.acl-long.936.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.936
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) have achieved remarkable success on reasoning-intensive tasks such as mathematics and programming. However, their enhanced reasoning capabilities do not necessarily translate to improved safety performance—and in some cases, may even degrade it. This raises an important research question: how should we enhance the safety of LRMs? In this paper, we present a comprehensive empirical study on how to enhance the safety of LRMs through Supervised Fine-Tuning (SFT). Our investigation begins with an unexpected observation: directly distilling safe responses from DeepSeek-R1 fails to significantly enhance safety. We analyze this phenomenon and identify five key risky patterns that contribute to it. We then demonstrate that explicitly addressing these issues during the data distillation process can lead to substantial safety improvements. Next, we explore whether a long and complex reasoning process is necessary for achieving safety. Interestingly, we find that simply using short or template-based reasoning process can attain comparable safety performance. These findings prompt a deeper reflection on the role of reasoning in ensuring safety. Finally, we conduct a comprehensive ablation study to reveal the impact of different training configurations. Overall, we hope our empirical study could provide a more holistic picture on enhancing the safety of LRMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.936`
