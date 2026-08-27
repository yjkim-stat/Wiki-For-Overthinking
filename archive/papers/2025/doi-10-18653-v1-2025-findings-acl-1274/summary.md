<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Token-Budget-Aware LLM Reasoning

- **Authors**: Tingxu Han, Zhenting Wang, Chunrong Fang, Shiyu Zhao, Shiqing Ma, Zhenyu Chen
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.findings-acl.1274/>
- **PDF**: <https://aclanthology.org/2025.findings-acl.1274.pdf>
- **DOI**: 10.18653/v1/2025.findings-acl.1274
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

TALE (Token-Budget-Aware LLM rEasoning) identifies that reasoning LLMs will follow a token budget stated in the prompt but that the effective budget must be chosen carefully -- too small a budget triggers 'token elasticity' where the model gives up complying and produces even longer output than an unconstrained baseline -- and offers two implementations, zero-shot budget estimation-and-prompting (TALE-EP, 67% token reduction with <3% accuracy loss) and post-training internalization (TALE-PT, ~50% reduction via SFT or DPO), both found via a binary-search 'optimal budget' procedure motivated by an 'implicit monotonicity assumption' verified on 90.91% of sampled GSM8K problems.

## Problem

Chain-of-Thought reasoning improves LLM accuracy but at the cost of substantially more output tokens, and while including a token budget in the prompt can compress reasoning length, the choice of budget value is critical to whether that compression actually works -- an unstudied relationship the paper terms 'token elasticity.'

## Contributions

- identification of 'token elasticity': setting an overly small token budget in a CoT prompt does not keep reducing actual token cost, but instead causes the model to abandon compliance and produce output as long as or longer than an unconstrained baseline
- a binary-search-based optimal-budget-search procedure (validated via an empirically-checked implicit monotonicity assumption, holding on 90.91% of sampled GSM8K problems) for finding the token budget that minimizes actual cost while preserving correctness
- TALE-EP, a training-free method where the LLM itself zero-shot-estimates a reasonable token budget per question, cutting tokens ~67% with <3% accuracy loss on average across models and datasets
- TALE-PT, an SFT- or DPO-based post-training method that internalizes token-budget awareness so the model produces efficient reasoning without an explicit budget in the prompt, cutting tokens ~50% with competitive accuracy
- GSM8K-Zero-based evidence that Vanilla CoT accuracy can fall below Direct Answering accuracy on questions where the answer is embeddable directly, a concrete demonstration of overthinking-induced accuracy loss from extra reasoning

## Method

First demonstrates the token-redundancy phenomenon: adding a reasonable token budget to the prompt ('Let's think step by step and use less than N tokens:') can cut CoT output length several-fold while preserving the correct answer. To find, for a given question and LLM, the token budget that minimizes actual token cost while preserving correctness, defines an 'implicit monotonicity assumption' (below the true minimal-needed budget the model always answers incorrectly; above it, always correctly) -- empirically validated on 90.91% of a GSM8K sample -- and builds Algorithm 1, a binary-search Budget Search over budget values, refined by Algorithm 2 (Greedy Feasibility Function) which additionally requires the searched budget's actual token cost to be lower than the previous iteration's, since the minimal feasible budget does not always minimize actual cost. This reveals 'token elasticity': below a certain reasonable-budget threshold, actual token cost does not keep shrinking but instead rebounds and increases, because the model cannot comply with an unreasonably tight constraint and reverts to (or exceeds) unconstrained-length reasoning. Building on this, proposes TALE: (1) TALE-EP (Estimation and Prompting) -- a training-free, zero-shot method where the reasoning LLM itself is prompted to estimate a reasonable token budget for a given question, which is then inserted into a token-budget-aware CoT prompt; (2) TALE-PT (Post-Training) -- generates target outputs via the offline binary-search procedure (run once on training questions) to build a dataset of token-efficient correct answers, then post-trains the LLM via either supervised fine-tuning (cross-entropy on the searched-budget target outputs) or DPO (treating the searched-budget outputs as preferred and vanilla-CoT outputs as dispreferred), so budget-awareness is internalized without needing an explicit budget in the prompt at inference time. Evaluated on GSM8K, GSM8K-Zero (a variant designed so answers are embeddable directly from the question, specifically probing over-reasoning/redundancy) and MathBench (Arithmetic/Middle/High/College difficulty tiers) across five LLMs (GPT-4o, GPT-4o-mini, Yi-lightning, o3-mini, Llama-3.1-8B-Instruct).

## Results

TALE-EP achieves 80.22%-81.03% average accuracy (comparable to Vanilla CoT's 83.75%) while cutting output tokens by 67% (461.25->148.72 average) and expenses by 59% relative to Vanilla CoT on GPT-4o-mini across 7 datasets/tiers; on GSM8K specifically TALE-EP even surpasses Vanilla CoT's accuracy (84.46% vs. 81.35%) while using far fewer tokens. On GSM8K-Zero, Vanilla CoT's accuracy (78.73%) is actually below Direct Answering's (97.21%) -- direct evidence of overthinking, since the correct answer is embeddable straight from the question and extra reasoning steps introduce errors -- while TALE-EP (73.67%) sits between the two, still reducing tokens sharply versus Vanilla CoT. TALE-EP generalizes across LLMs (tested on Yi-lightning, GPT-4o-mini, GPT-4o, o3-mini on MathBench-College): average token reduction of 64.63% and expense reduction of 45.30% versus Vanilla CoT while maintaining accuracy within a few points (e.g. GPT-4o: 80.00% TALE-EP vs. 84.00% Vanilla CoT at 181.61 vs. 602.09 tokens); the accuracy drop is most pronounced for the smaller GPT-4o-mini, attributed to it having less capacity to answer correctly within a tight response length. TALE-PT (Llama-3.1-8B-Instruct) cuts tokens ~50% versus Vanilla CoT with competitive accuracy: on GSM8K, TALE-PT-SFT reaches 78.57% accuracy at 139.63 tokens (vs. Vanilla CoT's 77.56% at 241.51 tokens); on GSM8K-Zero, TALE-PT-DPO best balances accuracy and efficiency (74.11%/78.41% depending on token budget config) while cutting tokens over 50% versus Vanilla CoT (251.08 tokens). The token elasticity phenomenon is directly visualized (Figure 2): as the binary search reduces the requested budget below a 'reasonable' range, actual token cost -- rather than continuing to decrease -- reverses and increases, because the model cannot satisfy the overly tight constraint and effectively 'gives up' complying, producing longer output than a moderately-budgeted prompt would; the paper reports a 10-token budget example yielding 157 output tokens, nearly double the 86 tokens produced under a 50-token budget on the same question. Generating the TALE-PT training-target dataset via the offline binary search took ~354 minutes on one A100 GPU for the full GSM8K training set (7,473 samples), a one-time preprocessing cost not incurred at deployment.

## Limitations

Experiments focus exclusively on LLMs that process only text as input and output; the framework does not account for models with multimodal (interleaved image/text) output, which the authors explicitly leave to future work involving modality-specific budget constraints. The TALE-EP accuracy drop is most significant for smaller/weaker models (GPT-4o-mini in particular), attributed to reduced capacity to produce a correct answer within a tightly constrained response length. The offline binary-search procedure used to generate TALE-PT's training targets, while a one-time cost, still requires meaningful compute (354 GPU-minutes for GSM8K alone) and scales with training-set size.

## Why it matters here

- **overthinking**: Directly central to the topic, both empirically and methodologically: GSM8K-Zero provides a clean, direct demonstration that Vanilla CoT reasoning can perform worse than simply answering directly when the question does not need reasoning (accuracy 78.73% vs. 97.21%), a textbook overthinking result the paper explicitly attributes to 'overthinking... introduc[ing] unnecessary complexity.' Its 'token elasticity' finding is an important caution for any budget-forcing or length-penalty overthinking-mitigation method: pushing the target length too aggressively does not monotonically save tokens but can backfire, since the model 'gives up' on compliance and produces even more tokens than a moderate budget would -- directly relevant to calibrating budget-forcing or reward-shaping thresholds used elsewhere in the literature (e.g. the GRIP, Reflection Steering and Long CoT Collection papers already in this archive).

## Entities

- **Concepts**: token elasticity (budget-constraint non-compliance rebound), implicit monotonicity assumption, token-budget-aware prompting, budget-aware post-training internalization
- **Methods**: token-budget-aware CoT prompting, binary-search optimal budget search (with greedy feasibility refinement), TALE-EP (zero-shot budget estimation and prompting), TALE-PT (SFT-based and DPO-based post-training internalization)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), GSM8K-Zero, MathBench (Arithmetic/Middle/High/College)

Tags: `overthinking`, `token-budget`, `chain-of-thought`, `prompt-engineering`, `post-training`

## Abstract

Reasoning is critical for large language models (LLMs) to excel in a wide range of tasks. While methods like Chain-of-Thought (CoT) reasoning and enhance LLM performance by decomposing problems into intermediate steps, they also incur significant overhead in token usage, leading to increased costs. We find that the reasoning process of current LLMs is unnecessarily lengthy and it can be compressed by including a reasonable token budget in the prompt, but the choice of token budget plays a crucial role in the actual compression effectiveness. We then propose a token-budget-aware LLM reasoning framework that dynamically adjusts the number of reasoning tokens based on the reasoning complexity of each problem. Experiments show that our method effectively reduces token costs in CoT reasoning with only a slight performance reduction, offering a practical solution to balance efficiency and accuracy in LLM reasoning. Code: https://github.com/GeniusHTX/TALE.

---

Record id: `doi:10.18653/v1/2025.findings-acl.1274`
