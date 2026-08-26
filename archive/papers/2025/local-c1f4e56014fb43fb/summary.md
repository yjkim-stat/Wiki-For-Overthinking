<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Do LLMs Overthink Basic Math Reasoning? Benchmarking the Accuracy-Efficiency Tradeoff in Language Models

- **Authors**: Gaurav Srivastava, Aafiya Hussain, Sriram Srinivasan, Xuan Wang
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local+anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1285/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1285.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1285
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces LLMThinkBench, a dynamically-generated 14-task basic-math benchmark and a harmonic-mean Overthinking Score, then evaluates 53 LLMs to show that strong performance on complex math benchmarks does not transfer to basic arithmetic and that reasoning-tuned models often spend far more tokens for equal or worse accuracy.

## Problem

LLMs that score well on complex math benchmarks (e.g. GSM8K, GSM-Plus) sometimes fail basic arithmetic operations while producing hundreds to thousands of tokens of chain-of-thought. Prior efficiency-focused evaluations measure thinking time or token/API cost but treat accuracy and efficiency as independent dimensions rather than a joint tradeoff, and existing benchmarks are static (vulnerable to contamination) and lack robust answer parsing, leaving no principled way to detect or quantify 'overthinking' or compare models on it.

## Contributions

- Formalizes the accuracy-verbosity tradeoff and a formal definition of 'overthinking' for a model relative to a more concise alternative achieving equal or better accuracy
- Introduces the Overthinking Score, a harmonic-mean metric combining accuracy and token-efficiency, with proofs of boundedness, symmetry, monotonicity and maximal imbalance penalty relative to arithmetic/geometric means
- Establishes a contamination-resistant evaluation protocol with dynamically generated test instances across 14 deterministic basic-math tasks and a hierarchical answer-extraction pipeline (98.7% success over 2.1M inferences)
- Conducts a large-scale empirical study of 53 LLMs across reasoning, quantized (GPTQ 8-bit/4-bit), constrained-token-budget, extended reasoning-effort, concise-prompting and tool-augmented conditions
- Releases LLMThinkBench as an open-source PyPI package (llmthinkbench) with a public leaderboard for reproducible third-party evaluation

## Method

The authors build LLMThinkBench, a task suite of 14 deterministic basic-math operations (sorting, comparison, sum, subtraction, multiplication, division, absolute difference, find max/min, mean, median, mode, odd/even count) with dynamically generated instances (values drawn Uniform[-1000,1000], list lengths from {8,16,32,64}, cryptographically seeded per fold/task/run) so problems cannot be memorized. They define the Overthinking Score as the harmonic mean of accuracy A and a normalized token-efficiency E_t = 1 - (T_i - T_min)/(T_max - T_min), proving it is bounded in [0,1], symmetric, strictly increasing in both arguments, sublinear (O <= min(A,E)), and maximizes the penalty for imbalance among symmetric homogeneous means (compared formally against arithmetic and geometric means). Answers are extracted with a hierarchical parser (boxed{} patterns, then explicit markers, then code-block/markdown, then task-specific fallback heuristics), reporting 98.7% successful extraction across 2.1 million model inferences. They evaluate 53 models (GPT, Gemini, Llama, Mistral, Qwen, Phi families, 0.5B-72B parameters; base, instruction-tuned and reasoning variants) with 1,000 samples x 3 folds for open-source models (100 samples x 3 folds for closed-source), plus ablations on GPTQ 8-bit/4-bit quantization, 1,024-token constrained generation, extended reasoning-effort budgets (Gemini, GPT-5, O-series), concise-prompting instructions, and tool-augmented (calculator/Python REPL/code executor) generation. ~5,000 responses were manually annotated to build a taxonomy of wasteful reasoning patterns.

## Results

Reasoning-tuned models generate ~6,780 tokens on average versus 378 for standard models while sometimes scoring lower. Phi-4 reaches 78.92% accuracy using ~378.6 tokens/response versus Phi-4-reasoning's 72.23% using ~6,066.2 tokens (~16x more), a 6.69-point accuracy gap. Under a 1,024-token cap, Phi-4-reasoning's accuracy falls to 53.48% (-18.75 points, ~26% relative) and Phi-4-reasoning-plus falls from 69.54% to 44.33% (-25.21 points, ~36% relative), while still using ~1,013 tokens on average (non-adaptive to the constraint). Qwen3 shows non-monotonic scaling with parameter count: Qwen3-14B (86.52%) outperforms the larger Qwen3-32B (84.13%). On the GSM8K/GSM-Plus vs. basic-math comparison (Qwen2.5 family), models scoring >95% on GSM8K score below 75% on the paper's basic arithmetic tasks. Extended reasoning-effort budgets show diminishing or zero returns: GPT-5 hits 97% accuracy at medium effort with no further gain at high effort; O3, O3-mini and O4-mini stay flat at 97%, 93% and 95% respectively across low/medium/high effort while token use rises (~8% more tokens at higher budgets); Gemini-2.5-Flash gains only 1 point (92%->93%) across the full budget range. Quantization is size-dependent: Qwen2.5-32B loses almost nothing (73.08%->72.67%) at 4-bit, while Qwen2.5-0.5B loses ~40% relative (21.31%->12.77%). By the composite Overthinking Score, GPT-4.1-mini scores highest (0.930, edging GPT-4.1's 0.927), followed by Qwen3-14B (0.727) and Qwen2.5-7B, while reasoning-tuned variants score far lower (e.g. Phi-4-reasoning 0.352 vs Phi-4's 0.863). Manual annotation of ~5,000 responses identifies four dominant wasteful patterns -- redundant verification loops, self-contradiction loops, irrelevant exploration, and pathological stopping failures (<2% of traces, e.g. infinite character repetition) -- versus one genuinely helpful pattern (structured decomposition, ~11% of long traces). Matched CoT-supervision ablations (same base model, with vs without extended CoT training) isolate training as the cause: the Phi-4 pair loses 6.69 accuracy points while using 16x more tokens under CoT supervision; concise/ultra-concise prompting only cuts tokens 38-63% at a cost of 1.4-3.9 accuracy points without closing the efficiency gap; giving models calculator/Python/code-executor tools raises accuracy by 2-30 points but adds 1.3-2.6x token overhead and does not prevent accuracy collapse as problem size grows. Ranking stability checks report leave-one-out Kendall's tau=0.87-1.0 and per-task vs global normalization correlating at Kendall's tau=0.89.

## Limitations

The authors state four limitations themselves: (1) the benchmark focuses only on basic math operations, which do not cover the full range of real-world reasoning, so the tasks expose only one dimension of math-reasoning behavior; (2) automated evaluation enables scale across 53 models but does not replace the qualitative insight of human interpretability review, which the case-study appendix only partially substitutes for; (3) dynamic test generation prevents direct memorization, but models could still exploit statistical patterns from training, so how much genuine computation versus pattern-matching occurs remains open; (4) evaluation relies on task-specific answer parsers that must track model output-format drift and can introduce extraction bias (measured at 98.7% success, meaning up to ~1.3% of responses may be mis-scored).

## Why it matters here

- **overthinking**: This paper's central contribution is a formal definition of overthinking and the Overthinking Score, a harmonic-mean accuracy/token-efficiency metric, applied in a 53-model study that directly measures when and how much reasoning models think beyond what basic math problems need -- including ~18x higher token usage with equal or worse accuracy, catastrophic collapse (up to ~36% relative accuracy loss) under constrained token budgets, and zero marginal accuracy gain from extended reasoning-effort settings in GPT-5 and O-series models.

## Entities

- **Concepts**: Overthinking Score (harmonic-mean accuracy-efficiency metric), accuracy-verbosity tradeoff, token efficiency normalization, adaptive computation / metacognitive control, reasoning budget saturation, [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), catastrophic accuracy collapse under token constraint
- **Methods**: chain-of-thought prompting/reasoning models, harmonic-mean Overthinking Score, hierarchical answer extraction (boxed / explicit-marker / code-block / fallback parsing), dynamic seeded test-instance generation, GPTQ quantization (8-bit, 4-bit), constrained (1,024-token) generation budgets, reasoning-effort budget sweeps (low/medium/high), ReAct-style tool-augmented generation (calculator, Python REPL, code executor)
- **Datasets**: LLMThinkBench (dynamically generated 14-task basic math suite, 42,000 instances per model), [GSM8K](../../../../wiki/datasets/gsm8k.md), GSM-Plus

Tags: `overthinking`, `reasoning models`, `accuracy-efficiency tradeoff`, `chain-of-thought`, `test-time compute`, `token efficiency`, `benchmark`, `llm evaluation`

## Abstract

Large language models (LLMs) achieve impressive performance on complex mathematical benchmarks yet sometimes fail on basic math reasoning while generating unnecessarily verbose responses. In this paper, we present LLMThinkBench, a systematic benchmark and comprehensive empirical study to evaluate the efficiency of reasoning in LLMs, focusing on the fundamental tradeoff between accuracy and overthinking. First, we formalize the accuracy-verbosity tradeoff. Second, we introduce the Overthinking Score, a harmonic-mean metric combining accuracy and token-efficiency for holistic model evaluation. Third, we establish an evaluation protocol with dynamically-generated data across 14 basic math tasks. Fourth, we conduct a large-scale empirical study evaluating 53 LLMs, including reasoning and quantized variants across different reasoning budgets. Fifth, we release LLMThinkBench as an open-source Python package and public leaderboard for reproducibility. Our findings reveal: 1) model performance on complex benchmarks does not translate directly to basic math reasoning; 2) reasoning models generate ∼18× more tokens while sometimes achieving lower accuracy and exhibit catastrophic collapse when tokens are constrained, dropping by up to ∼36%; 3) the accuracy-verbosity relationship is non-monotonic with extended reasoning budgets yielding diminishing returns (GPT-5/o-series models show zero accuracy gain from low → medium → high reasoning effort). Our findings challenge the assumption that longer reasoning in LLMs necessarily improves mathematical reasoning. Our public leaderboard is available at https://ctrl-gaurav.github.io/LLMThinkBench/. Our open-source Python package is available at https://pypi.org/project/llmthinkbench/, and the codebase can be found at https://github.com/ctrl-gaurav/LLMThinkBench for easy and reproducible evaluation.

---

Record id: `local:c1f4e56014fb43fb`
