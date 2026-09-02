<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models

- **Authors**: Yongjiang Liu, Haoxi Li, Xiaosong Ma, Jie Zhang, Song Guo
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1766/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1766.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1766
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

TH2T (Think-How-to-Think) is a two-stage fine-tuning method that first injects an explicit 'difficulty hypnosis' cue into a model's output prefix (prospective, global strategy selection) and then a 'redundancy hypnosis' cue into in-progress reasoning to truncate reflection loops (retrospective, local correction), cutting inference cost over 70% on easy tasks and 40% on hard tasks with minimal accuracy loss and no external difficulty labels at inference time.

## Problem

Large reasoning models apply a largely monolithic, one-size-fits-all reasoning strategy regardless of task difficulty because they lack genuine cognition of how hard a problem is (an empirical analysis finds LRM difficulty-classification precision typically under 20%, defaulting to a 'Medium' label) -- and existing overthinking mitigations either rely on unreliable prompt-based instruction following, degrade interpretability by compressing reasoning into implicit latent representations, or are behaviorally rigid model-based length-penalty methods.

## Contributions

- an empirical demonstration that current LRMs largely fail to perceive task difficulty (classification precision typically <20%), grounding overthinking in a cognitive deficit rather than treating it as a purely behavioral flaw
- TH2T, a two-stage fine-tuning method injecting trained 'self-hypnosis' cues -- prospective difficulty cognition (Stage 1) and retrospective redundancy/looping cognition (Stage 2) -- directly into the model's own generation, rather than relying on external prompts or implicit latent compression
- >70% (easy) / >40% (hard) inference-cost reduction with essentially no accuracy loss across 7B/14B/32B DeepSeek-R1-Distill backbones, at a fraction of the training cost of comparable RL-based baselines
- evidence (rising first-token confidence tracking improved difficulty-classification accuracy) that the trained self-hypnosis reflects a genuine internal calibration shift rather than a superficial prompt pattern

## Method

Grounded in the dual-process (System 1/System 2) theory of cognition, TH2T trains a self-hypnosis mechanism directly into the model's own output rather than relying on external prompts. Stage 1 (Difficulty Cognition Injection): builds a hybrid SFT dataset from an easy-problem set answered correctly by a short-CoT sibling model and a hard-problem set answered by the long-CoT target model, injecting a difficulty-hypnosis marker ('<hypnosis> This is a simple/difficult question, let's think quickly/thoroughly. </hypnosis>') into each response's prefix as a global, prospective strategy-selection signal. Stage 2 (Redundancy Cognition Injection): uses GPT-4 as a 'Determinator' to detect logically-redundant or looping reasoning chunks (via a formal chunk-equivalence criterion) in the hard-task responses, and injects a redundancy-hypnosis marker ('Everything seems ok, let's move on.') or a looping-hypnosis marker ('Oh, I'm stuck in a loop. Time to break out.') at the truncation point, teaching the model to interrupt superfluous reflection/looping mid-generation as a local, retrospective correction signal.

## Results

On DeepSeek-R1-Distill-Qwen-7B/14B/32B across GSM8K, MATH-500, AIME2024 and OmniMath, TH2T achieves the best length-reduction-with-stable-accuracy trade-off among all compared methods: at 7B, up to 74.0% token reduction on GSM8K and 38.0% on MATH-500 with accuracy essentially unchanged (+1.4% average gain across benchmarks), translating to >5x and >2x latency speedups respectively; results hold at 14B (-42.7% average reduction, +1.1% accuracy) and 32B (-41.7% average reduction, +0.0% accuracy). Prompt-based (D-Prompt), output-based (NoThinking, TokenSkip, CoT-Valve) and label-driven RL (AdaCtrl) baselines achieve comparable or larger length reductions but at >10-point accuracy degradation, while five additional RL-based methods (AdaptThink, DR.SAF, DRQA, Thinkless, Steering) either suffer unacceptable accuracy drops (Steering: -11.2%) or limited length reduction (DRQA: -24.7%), and all require >4x the GPUs and >10x the training time (>40x total cost) versus TH2T's SFT-only 2-GPU, 1x-time training. TH2T substantially improves difficulty-cognition accuracy (e.g. from 14.9% to 98.3% on GSM8K, 16.7% to 96.7% on AIME2024), validated by a rising first-token confidence signal correlating with the improved cognition. It suppresses reflective-chunk counts 10x on easy tasks and 3x on hard tasks, and reduces tail-recursion looping in incorrect MATH answers from 59.5% (original model) to 21.4%. An ablation isolating Difficulty Hypnosis vs. Redundancy Hypnosis shows D.H. contributes more token reduction on easy tasks (26.6% vs. 4.8% on 7B GSM8K) while R.H. contributes more on hard tasks (17.3% vs. 11.6% on MATH), consistent with the two-stage design's intended division of labor. Generalizes to 4 STEM tasks beyond math (QA, coding, science, multi-task) with >30% token reduction and preserved accuracy.

## Limitations

The current approach uses standard supervised fine-tuning on a constructed hybrid dataset; the paper notes reinforcement learning could offer further gains but is unstable and computationally demanding, and was not adopted. The study is confined to language-only models, so its efficacy on multimodal (vision-language) reasoning architectures is unexplored and left as future work.

## Why it matters here

- **overthinking**: Central to the topic: directly reframes overthinking as a cognitive deficit (LRMs cannot judge task difficulty, defaulting to one reasoning strategy for every problem) rather than a purely behavioral length problem, and its trained 'self-hypnosis' cues give the model an explicit, internally-generated difficulty and redundancy signal instead of relying on unreliable prompted instructions or implicit, interpretability-degrading latent compression. Its cost comparison against five RL-based length-control baselines (all requiring far more GPUs and training time for worse or comparable results) is a useful data point on the training-cost side of the efficiency literature this archive tracks.

## Entities

- **Concepts**: self-hypnosis (trained prefix/in-context behavioral trigger), difficulty cognition / redundancy cognition, dual-process (System 1/System 2) reasoning framing, prospective (global) vs. retrospective (local) intervention
- **Methods**: TH2T (Think-How-to-Think, two-stage SFT with self-hypnosis), D-Prompt (baseline), [NoThinking (baseline)](../../../../wiki/methods/nothinking-baseline.md), [TokenSkip (baseline)](../../../../wiki/methods/tokenskip-baseline.md), [CoT-Valve (baseline)](../../../../wiki/methods/cot-valve-baseline.md), AdaCtrl (baseline), AdaptThink, DR.SAF, DRQA, Thinkless, Steering (RL baselines)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH-500](../../../../wiki/datasets/math500.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [OmniMath](../../../../wiki/datasets/omni-math.md), [GPQA](../../../../wiki/datasets/gpqa.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), [Olympiad](../../../../wiki/datasets/olympiad.md), [MMLU](../../../../wiki/datasets/mmlu.md)

Tags: `overthinking`, `difficulty-cognition`, `efficient-reasoning`, `dual-process-theory`, `SFT`

## Abstract

Recent Large Reasoning Models (LRMs) excel at complex reasoning tasks but often suffer from overthinking, generating overly long and redundant reasoning trajectories. To explore its essence, our empirical analysis reveals that LRMs are primarily limited to recognizing task properties (i.e., difficulty levels) like humans before solving the problem, leading to a one-size-fits-all reasoning strategy. This observation motivates a fundamental question: Can we explicitly bootstrap such ability to alleviate overthinking in LRMs? To this end, we propose Think-How-to-Think (TH2T), a novel two-stage fine-tuning strategy that progressively inspires LRMs’ difficulty cognition and redundancy cognition of LRMs. Specifically, we first inject Difficulty Dypnosis into output prefixes as cues for global, prospective reasoning strategy selection, stimulating the model’s sharper sensitivity to task complexity and adaptive control of reasoning depth. Then, we incorporate Redundancy Hypnosis into in-progress reasoning steps, which serve as local, retrospective signals for behavior correction by identifying and eliminating superfluous reasoning detours. Experiments across 7B/14B/32B models demonstrate that TH2T significantly reduces inference costs by over 70% on easy tasks and 40% on complex ones without compromising performance. The resultant models exhibit a nascent ability for difficulty-aware reasoning, effectively mitigating behaviors like excessive reflection and looping, thereby paving the way for more cognitively efficient LRMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.1766`
