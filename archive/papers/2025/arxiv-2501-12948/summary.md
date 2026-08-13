<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- **Authors**: DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang, Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Zhen Zhang
- **Venue**: Nature volume 645, pages 633-638 (2025)
- **Published**: 2025-01-22
- **Source**: seed
- **Link**: <https://arxiv.org/abs/2501.12948>
- **PDF**: <https://arxiv.org/pdf/2501.12948v2>
- **DOI**: 10.1038/s41586-025-09422-z
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.62, test-time-scaling 0.40

## In one line

Shows that reasoning ability can be incentivized in an LLM by pure reinforcement learning on verifiable tasks, with no human-annotated reasoning trajectories, and that the resulting reasoning patterns can be transferred to smaller models.

## Problem

Progress on reasoning depended on extensive human-annotated demonstrations, which bounds both cost and capability, and models remained insufficient on harder problems. Whether reasoning could be induced without human reasoning traces was open.

## Contributions

- Evidence that pure reinforcement learning, without human-labelled reasoning trajectories, incentivizes reasoning ability in an LLM.
- The observation that advanced reasoning patterns — self-reflection, verification, dynamic strategy adaptation — emerge from that process rather than being demonstrated to the model.
- Performance on verifiable tasks (mathematics, coding competitions, STEM) exceeding counterparts trained by conventional supervised learning on human demonstrations.
- A demonstration that the emergent patterns of large models can be systematically harnessed to improve smaller models.

## Method

An RL framework is applied directly to a base model with rewards derived from verifiable task outcomes rather than from human-annotated reasoning trajectories. The abstract describes the resulting behaviour — emergent self-reflection, verification and dynamic strategy adaptation — but does not give the RL algorithm, reward construction, base model or training scale.

## Results

The abstract reports superior performance on verifiable tasks in mathematics, coding competitions and STEM relative to supervised training on human demonstrations, and successful transfer of emergent reasoning patterns to smaller models, but states no benchmark numbers. Published in Nature 645, 633-638 (2025). Summarized from the abstract alone, so the figures below are only those the abstract states; the paper's full evaluation is not represented here.

## Limitations

Not discussed in the abstract. The scope condition is in the claim itself: the method depends on tasks whose outcomes are verifiable, so it says nothing about domains where correctness cannot be checked automatically. Archived work also complicates the 'emergent self-reflection' framing — one paper measures the precision of such self-corrections at 24.4% and another finds that RL largely preserves the base model's existing entropy structure rather than installing a new one.

## Why it matters here

- **reasoning-training**: The result the whole topic reacts to: reasoning from verifiable reward alone, no human traces. Everything archived here about RLVR — which tokens the gradient should act on, whether entropy identifies them, how to curate rollouts — is downstream of the claim established here, so this is the paper that fixes the setting the others argue inside. Its 'emergent reasoning patterns' framing is also the specific claim the archive is best positioned to test: one paper shows over 86% of high-entropy token positions are unchanged from the base model after RLVR, which argues the training sharpens structure already present rather than creating it, and another finds most proactive self-corrections second-guess already-correct chains.
- **test-time-scaling**: A secondary match. The paper contributes no inference-time method, but it produced the model family that this topic's methods are almost all evaluated on — the archived early-exit, trajectory-weighting and entropy-diagnostic papers use its distilled variants as their subjects. It also matters that the long reasoning traces this topic tries to shorten or score are a product of the training described here, not of prompting, which is why overthinking is treated as a property of reasoning models rather than of a decoding strategy.

## Entities

- **Concepts**: reinforcement learning with verifiable rewards, emergent reasoning patterns, self-reflection, [verification](../../../../wiki/concepts/verification.md), dynamic strategy adaptation, reasoning distillation
- **Methods**: pure reinforcement learning, [reasoning distillation](../../../../wiki/methods/reasoning-distillation.md)
- **Datasets**: _none recorded_

Tags: `deepseek-r1`, `rlvr`, `reinforcement learning`, `emergent reasoning`, `distillation`, `nature`

## Abstract

General reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) and chain-of-thought prompting, have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models.

---

Record id: `arxiv:2501.12948`
