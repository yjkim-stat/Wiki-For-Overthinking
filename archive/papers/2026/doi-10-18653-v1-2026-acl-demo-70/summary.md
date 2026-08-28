<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning

- **Authors**: Vladislav Smirnov, Quang-Chieu Nguyen, Sergey Senichev, Minh Ngoc Ta, Ekaterina Fadeeva, Artem Vazhentsev, Daria Galimzianova, Nikolai Rozanov, Viktor Mazanov, Jingwei Ni, Tianyi Wu, Igor Kiselev, Mrinmaya Sachan, Iryna Gurevych, Preslav Nakov, Timothy Baldwin, Artem Shelmanov
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-demo.70/>
- **PDF**: <https://aclanthology.org/2026.acl-demo.70.pdf>
- **DOI**: 10.18653/v1/2026.acl-demo.70
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

ThinkBooster is a unified, open-source framework (Python library + OpenAI-compatible proxy endpoint + visual debugger) implementing 9 test-time-compute scaling strategies and 4 scorer families under a joint TFLOPs-and-tokens compute-accounting benchmark, whose pilot study finds PRM scorers dominate on math while lightweight uncertainty scorers are surprisingly competitive on (out-of-domain-for-PRM) coding tasks, and that beam search often underperforms best-of-N and even self-consistency despite costing more compute.

## Problem

Test-time-compute (TTC) scaling research is highly fragmented: methods are evaluated under inconsistent experimental protocols (different model configurations, structured vs. unstructured CoT, compute budgets), most published work presents only one proposed method against a limited baseline set, studies focus on accuracy gains while overlooking computational cost/latency trade-offs, and released code is typically proof-of-concept only, lacking efficiency and practical-deployment support -- making it difficult to identify which TTC methods actually offer the best performance-compute trade-off or to deploy them in real applications.

## Contributions

- a unified, modular Python library implementing 9 state-of-the-art TTC scaling strategies and 4 scorer families behind a consistent API, spanning both structured system-prompted CoT and native unstructured LRM thinking
- an OpenAI-compatible proxy endpoint gateway that applies TTC scaling transparently to any compatible LLM deployment without requiring changes to downstream application code
- a joint performance-and-compute benchmark (theoretical TFLOPs plus token counts) across 9 math/coding/scientific datasets, plus a visual debugger for inspecting reasoning trajectories and scoring decisions
- a pilot empirical study finding PRM scorers dominate on in-domain math tasks but lightweight domain-agnostic uncertainty scorers are competitive or superior on out-of-domain coding tasks, and that beam search frequently underperforms cheaper strategies (Best-of-N, self-consistency) despite higher compute cost

## Method

ThinkBooster provides three components: (1) a modular Python library implementing 9 TTC scaling strategies (Best-of-N, majority voting, beam search/tree-of-thought, extended thinking, dynamic exploration/MUR, DeepConf online/offline, Phi-decoding, uncertainty CoT) spanning offline/online, black-box/white-box, and prefill-dependent variants, plus 4 scorer families (process reward models, self-verification via the same LLM, uncertainty/confidence scores from the LM-Polygraph library, and ReProbes -- a supervised regressor over LLM internal states) with reasoning-step boundary extraction for both system-prompted structured CoT and native unstructured LRM thinking (e.g. DeepSeek-R1/Qwen3's <think> tags); (2) a deployable OpenAI-compatible proxy endpoint gateway that applies TTC scaling transparently in front of any OpenAI-compatible LLM backend, requiring no changes to downstream application code, configurable via URL/API parameters for compute budget, strategy, and scorer; (3) a benchmark with joint TFLOPs-and-token compute accounting (theoretical FLOPs following Hoffmann et al. 2022, computing prompt-processing FLOPs once with KV-cache-reuse-aware generation-cost tracking) across 9 bundled math/coding/scientific datasets (MATH-500, OlympiadBench, GaoKao23EN, AIME-2024/2025, GPQA-Diamond, HumanEval+, MBPP+, KernelBench), plus a visual debugger for inspecting reasoning trajectories, step-level scores, and pruned candidate paths. Pilot experiments run three LLMs (Qwen2.5-Math-7B-Instruct non-thinking, Qwen3-8B native-thinking, GPT-OSS-120B large-thinking) across strategy-scorer combinations, plotting accuracy improvement versus relative compute cost.

## Results

On mathematical benchmarks (Qwen2.5-Math-7B, aggregated over MATH-500/OlympiadBench/GaoKao23EN), PRM-based scoring achieves the best results, and beam search paired with a PRM scorer reaches the highest absolute accuracy among all strategy-scorer combinations tested. On coding (Qwen3-8B, HumanEval-Plus), PRMs do NOT consistently outperform lightweight uncertainty-based scorers -- the uncertainty scorer combined with the dynamic MUR strategy substantially surpasses all baselines including PRM-based methods, attributed to the PRM being trained predominantly on mathematical data and overfitting to that domain, while uncertainty-based scorers are domain-agnostic and generalize better to code (an out-of-distribution setting for the math-trained PRM). Across strategies generally, beam search often underperforms Best-of-N and even plain self-consistency despite requiring substantially more compute; dynamic TTC scaling (MUR) is a more compute-efficient alternative to beam search and delivers the strongest coding results, though on math it still lags behind Best-of-N even when combined with PRMs. Uncertainty-based scorers are highlighted as a robust, competitive, near-zero-overhead, domain-independent signal for both scoring and dynamic compute-allocation, though the authors note this reveals a clear gap: coding-specific PRMs remain largely unexplored. In a real-world CUDA-kernel-optimization case study (GPT-OSS-120B on KernelBench), Offline Best-of-N guided by a PRM achieves 5% fewer syntax errors and a 4-percentage-point higher overall correctness rate than raw CoT, though with a slightly lower compilation rate (PRM tends to select more sophisticated but occasionally failure-prone code) -- demonstrating a measurable practical gain from TTC scaling on a real deployment task, not just benchmark datasets.

## Limitations

Several ThinkBooster components depend on deployment-specific capabilities: dynamic, uncertainty-driven strategies requiring white-box signals (logits, hidden states) or prefill-style continuation are only available for open-weight or self-hosted LLMs, and only a black-box subset (Best-of-N, majority voting, extended thinking with optional logits, LLM-as-judge scoring) works against fully-hosted closed commercial APIs. Reliable reasoning-step-boundary extraction remains challenging for large reasoning models with native, unstructured 'thinking' traces, which can affect online scoring and early-stopping decisions. The empirical pilot study focuses on a relatively narrow task range (primarily math, coding, and graduate-level scientific QA), so the observed quality-cost trade-offs may not generalize to other settings such as long-context question answering, open-ended generation, or tool-augmented agents. Reported compute costs are theoretical TFLOPs rather than measured wall-clock latency, since real latency is highly sensitive to batching, KV-cache reuse, hardware, and provider-side serving optimizations (e.g. vLLM prefix caching) -- a full wall-clock study under fixed serving conditions is explicitly left to future work, though the benchmark does expose wall-clock measurement as a per-request log field.

## Why it matters here

- **overthinking**: Directly central to the topic as infrastructure: it is a standardized, joint performance-and-compute benchmark and toolkit spanning nearly the entire space of test-time-scaling strategies and scorers this archive tracks (Best-of-N, beam search, self-consistency, PRMs, uncertainty-based dynamic scaling), addressing exactly the methodological fragmentation and 'accuracy reported without cost' problem the overthinking literature struggles with. Its finding that beam search -- a strategy that spends more compute -- often underperforms cheaper strategies, and that a domain-mismatched PRM can be beaten by a cheap, domain-agnostic uncertainty scorer, are concrete, benchmarked instances of the core overthinking claim that more test-time compute does not reliably buy better outcomes, now measurable on a common accuracy-vs-TFLOPs axis across methods.

## Entities

- **Concepts**: test-time compute (TTC) scaling, joint TFLOPs-and-token compute accounting, process reward model (PRM) vs. uncertainty-based scoring, white-box vs. black-box TTC strategy access level
- **Methods**: [Best-of-N](../../../../wiki/methods/best-of-n.md), [majority voting / self-consistency](../../../../wiki/methods/majority-voting-self-consistency.md), beam search (tree-of-thought), extended thinking (budget forcing), dynamic exploration (MUR), DeepConf (online/offline), [Phi-decoding](../../../../wiki/methods/phi-decoding.md), uncertainty CoT, process reward models (PRM), ReProbes (internal-state regressor)
- **Datasets**: [MATH-500](../../../../wiki/datasets/math500.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), GaoKao23EN, [AIME-2024](../../../../wiki/datasets/aime-2024.md), [AIME-2025](../../../../wiki/datasets/aime-2025.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [HumanEval+](../../../../wiki/datasets/humaneval.md), [MBPP+](../../../../wiki/datasets/mbpp.md), KernelBench

Tags: `test-time-scaling`, `benchmark`, `open-source-framework`, `compute-accounting`, `process-reward-model`

## Abstract

Test-time compute (TTC) scaling has emerged as a powerful paradigm for improving large language model (LLM) reasoning by allocating additional compute during inference, e.g., via multi-sample generation and verifier-based reranking. Existing TTC scaling strategies and reasoning scorers remain fragmented, evaluated under inconsistent protocols, and are rarely analyzed through the lens of quality-cost trade-offs. We introduce ThinkBooster, a unified framework for seamless test-time compute scaling of LLM reasoning, which consists of (i) a modular Python library implementing state-of-the-art TTC scaling strategy and scorer families, (ii) a benchmark that jointly evaluates performance and computational efficiency, and (iii) a deployable OpenAI-compatible proxy service that enables drop-in integration of adaptive reasoning into real-world applications. We further provide a demo visual debugger for inspecting the reasoning trajectories, intermediate selection decisions, and alternative reasoning paths. Empirical results on mathematical and coding tasks reveal the performance-compute trade-offs of TTC scaling strategies and scoring methods and demonstrate that ThinkBooster provides practical gains in real-world tasks. The code is available online under an MIT license.

---

Record id: `doi:10.18653/v1/2026.acl-demo.70`
