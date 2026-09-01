<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code

- **Authors**: Jian Xie, Zhendong Chu, Aoxiao Zhong, Kai Zhang, Mingzhe Han, Xing Fan, Jialie Shen, Qingsong Wen
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1365/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1365.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1365
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.

## Problem

Large reasoning models apply long chain-of-thought reasoning indiscriminately regardless of task difficulty (overthinking); existing adaptive-reasoning approaches address this from a single perspective (length control alone, requiring a predefined token budget or a separately-trained model per length target -- which assumes prior knowledge of task difficulty) and are designed for plain-text inputs only, lacking both the flexibility to switch reasoning formats and the ability to handle visual information; separately, applying standard GRPO to multi-format reasoning suffers 'format collapse,' where the model disproportionately favors whichever format has the highest reward during training and stops exploring the others.

## Contributions

- ARM2, the first adaptive-reasoning model to extend format-adaptive reasoning (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs, rather than plain text only
- integration of executable code as a distinct reasoning format offloading verifiable computation from natural-language chain-of-thought, improving both accuracy and token efficiency on code-amenable tasks
- GRPO-alp, a GRPO variant combining a format-encouragement reward (preventing collapse onto a single dominant format) with an explicit, cosine-decayed length penalty, addressing format collapse more directly than a prior related method (Ada-GRPO/ARM) that does not incorporate length awareness
- empirical results across 12 in-/out-of-domain text and multimodal benchmarks showing over 70% average token reduction versus standard GRPO with matched or improved accuracy, plus a demonstrated task-difficulty-adaptive length distribution and a test-time-scaling analysis confirming efficiency gains do not sacrifice underlying reasoning capability

## Method

Defines five reasoning formats: Direct Answer, Short CoT, Code-Text (reasoning expressed as code without execution), Code-Exec (generated code is run by an external Python interpreter and its output used as the final answer), and Long CoT. Builds a 15.1K-instance curated training set spanning all five formats (from AQuA-Rat and VisualWebInstruct, augmented with GPT-4o/Doubao-Pro-1.6-Thinking-generated Code-Text/Code-Exec/Long-CoT rationales, verified for code executability and filtered to keep only instances whose rationale yields the correct answer). Trains in two stages: (1) SFT cold-start teaches the model to produce all five formats and enables format parsing; (2) length-aware reinforcement learning with GRPO-alp, a novel GRPO variant that first applies a format-encouragement factor (scaling reward inversely by how often a format appears within its response group, amplifying reward for underrepresented formats to prevent format collapse) and then a length penalty (exponentially decaying reward for longer responses within the group, tunable via strength lambda), combined with a cosine-decay schedule that gradually reduces the artificial reward amplification over training to stabilize convergence. RL training uses six additional question-answer-only datasets (three text: CommonsenseQA, GSM8K, AIME 1987-2023; three multimodal: MME RealWorld, Geometry3K, MMK12), leveraging RLVR's flexibility to train without needing rationales for every format.

## Results

Across six in-domain (CSQA, GSM8K, AIME, MMEWorld, GEO3K, MMK12) and six out-of-domain (OBQA, MATH500, GPQA-Diamond, BLINK, ChartQA, MMMU) datasets spanning text and multimodal inputs, ARM2-7B reduces average token usage by over 70% relative to a GRPO-trained baseline on the same backbone (Qwen2.5-VL-7B) while maintaining comparable in-domain accuracy (avg 51.2% vs. GRPO's 51.8%) and slightly improving out-of-domain accuracy (avg 49.2% vs. GRPO's 49.2%, essentially matched, with individual OOD-benchmark gains e.g. OBQA +1.2, GPQA-Diamond +0.1) -- both SFT alone and GRPO alone are shown to lack adaptability: SFT consumes the fewest tokens but underperforms substantially on complex tasks (GSM8K), while GRPO achieves strong accuracy on reasoning-heavy tasks but wastes tokens even on easy perception tasks (CSQA), each collapsing to a single dominant format rather than adapting per-task. Ablations (Figure 2, 12 datasets) isolate each mechanism: removing format-encouragement reward causes the model to collapse toward extremely short responses, substantially harming performance across almost all tasks; removing the length penalty causes token usage to increase substantially with no corresponding accuracy gain (and sometimes decline); removing code execution (forcing Code-Text-only reasoning) both decreases accuracy and increases token usage, especially on out-of-domain datasets -- because reliable code execution offloads reasoning that would otherwise require long CoT, directly substituting a shorter, more reliable mechanism for extended natural-language deliberation. A length-distribution analysis (Figure 3) across three difficulty tiers (CSQA easy, GEO3K medium, AIME hard) shows ARM2's token-count peak shifts to the right (longer) as task difficulty increases, unlike SFT (uniformly short, regardless of difficulty) or GRPO (dispersed, generally long) -- direct evidence ARM2 learns difficulty-adaptive, not fixed, reasoning length. A test-time-scaling experiment (majority voting over multiple samples at matched token budget) on GSM8K/GEO3K, where ARM2 initially lags GRPO at low budgets, shows the accuracy gap closes as budget increases and ARM2 eventually surpasses GRPO at the same total token budget, indicating GRPO-alp's efficiency gains do not come at the cost of the model's underlying reasoning capability when given enough test-time compute. Directly quantifying the code-execution effect (Table 3) on three OOD datasets: enabling code execution both raises the proportion of code-format responses (e.g. MATH500: 22.8%->52.6%) and raises accuracy (MATH500: 38.6%->47.7%; ChartQA: 65.2%->70.3%; MMMU: 49.8%->50.2%), directly confirming code execution is not merely an alternative output style but a genuine accuracy and efficiency lever. Length-penalty-strength sweep (lambda 0.25-1) shows the optimal response length is highly task-dependent: easy/perception tasks (CSQA, MMEWorld) benefit from stronger penalties (shorter output = better, since extra reasoning there is pure redundancy), while reasoning-intensive tasks (GSM8K, MMK12) are harmed by strong penalties (premature truncation of genuinely-needed multi-step logic) -- lambda=0.5 is chosen as the balanced default. A backbone-initialization comparison finds stronger backbones (Mimo-RL/Mimo-SFT) yield substantial accuracy gains over a weaker Qwen backbone, but RL-initialized backbones (Mimo-RL) show pronounced training instability (oscillating response length/accuracy) on multimodal data, while lightweight GRPO pre-initialization of the Qwen backbone gives only marginal benefit versus starting from the plain base model.

## Limitations

ARM2 assumes a finite, predefined set of five reasoning formats rather than an unbounded format space; the paper argues these formats can be automatically curated (via existing closed-source models) rather than manually engineered, but treats the fixed format set as a deliberate implementation choice rather than a hard theoretical limitation. Due to computational constraints, experiments are conducted only at 7B backbone scale; the paper expects but does not verify that the mechanism generalizes to larger backbones and more extensive training.

## Why it matters here

- **overthinking**: Directly and centrally relevant: it names overthinking explicitly and contributes two distinct levers beyond the token-length-penalty framing common elsewhere in this archive -- adaptive selection among qualitatively different reasoning *formats* (not just adaptive length within one format) and substituting executable code for chain-of-thought where verifiable computation applies -- plus a specific, general training fix (format-collapse-resistant reward shaping) for any RL method that trains a model to choose among multiple reasoning styles rather than a single continuous length dial.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), adaptive reasoning format selection, [format collapse](../../../../wiki/concepts/format-collapse.md), GRPO-alp (format-encouragement + length-aware GRPO), code-execution as a CoT substitute, cosine-decayed reward amplification
- **Methods**: GRPO-alp (format-encouragement + length-aware GRPO), [GRPO (baseline)](../../../../wiki/methods/grpo-baseline.md), Ada-GRPO / ARM (baseline), SFT cold-start, majority-vote test-time scaling
- **Datasets**: [AQuA-Rat](../../../../wiki/datasets/aqua-rat.md), VisualWebInstruct, [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), AIME (1987-2023), MME RealWorld, Geometry3K, MMK12, OBQA, [MATH500](../../../../wiki/datasets/math500.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), BLINK, [ChartQA](../../../../wiki/datasets/chartqa.md), [MMMU](../../../../wiki/datasets/mmmu.md)

Tags: `overthinking`, `adaptive-reasoning`, `multimodal`, `code-execution`, `reinforcement-learning`, `GRPO`

## Abstract

Large Reasoning Models (LRMs) often suffer from the “over-thinking” problem, generating unnecessarily long reasoning on simple tasks. Some strategies have been proposed to mitigate this issue, such as length penalties or routing mechanisms, but they are typically heuristic and task-specific, lacking a general framework for adaptive reasoning. In this paper, we present ARM2, a unified model that adaptively balances reasoning performance and efficiency across multiple formats through a reinforcement learning framework augmented with length-aware optimization. Beyond conventional natural language inference, ARM2 integrates vision understanding, extending its applicability to multimodal. Moreover, ARM2 integrates executable code into reasoning, enabling substantial reductions in token cost while preserving task performance compared to long CoT. Experiments demonstrate that ARM2 achieves performance on par with traditional reasoning models trained with GRPO, while reducing token usage by over 70% on average. We further conduct extensive analyses to validate the effectiveness of ARM2 and the soundness of its design.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1365`
