<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance

- **Authors**: Jian Yang, Zhenqi Feng, Zhaoyang Yu, Zhaoxin Fan, Kejian Wu, Xiaofeng Wang, Zheng Zhu, Jianjun Huang, Wei You, Bin Liang
- **Venue**: cs.CL
- **Published**: 2026-08-19
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.18921>
- **PDF**: <https://arxiv.org/pdf/2608.18921v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

SMTrap uses SMT solver conflict counts as a free, model-feedback-free proxy to synthesize Sudoku and zebra-puzzle queries that induce excessive backtracking-driven reasoning in large reasoning models, mounting a state-of-the-art denial-of-service attack that a bounded-solver defense can neutralize.

## Problem

Existing black-box denial-of-service attacks against large reasoning models require repeated queries to the target model or training a dedicated attack model to synthesize inference-heavy prompts, which is expensive and weakens the attacker's cost leverage. The paper asks whether inference-heavy DoS queries can be generated without any model feedback.

## Contributions

- Shows that SMT (Z3) conflict counts on a CSP instance positively correlate with the amount of backtracking search and output length an LRM produces when solving the same instance (Pearson/Spearman positive across Sudoku and zebra puzzles).
- Proposes search amplification, a model-feedback-free DoS paradigm that uses SMT conflict count as a low-cost external signal to synthesize inference-heavy CSP queries, requiring no queries to the target model, no attack-model training, and no GPU.
- Implements SMTrap, a CPU-only framework that performs solver-guided clue-state branching, pruning and conflict-guided acceptance to synthesize Sudoku and zebra-puzzle DoS queries.
- Evaluates SMTrap against seven frontier LRMs, reporting state-of-the-art DoS effect (e.g. SMTrap-Zebra reaches 76,362 average completion tokens vs. 27,860 average for baselines) and a 270.65x amplification ratio for SMTrap-Sudoku.
- Proposes and evaluates a tool-based mitigation (routing CSP-style queries to a bounded local solver) that cuts token usage by 90.15% on average on GPT-5.5.

## Method

SMTrap starts from a hidden solution and an initial clue state, encodes the corresponding CSP as an SMT formula, and solves it with the Z3 solver to obtain a conflict count. It then iteratively branches (adds a clue) and prunes (removes a clue) to generate candidate clue states, encodes each candidate as SMT, checks satisfiability and unique solvability with Z3, and greedily accepts the candidate with the highest conflict count while keeping the clue count fixed. The search repeats for a fixed iteration budget or until a target conflict threshold (3,000 for Sudoku, 5,000 for zebra) is reached. The final clue state is rendered as a natural-language Sudoku or zebra-puzzle query, with an appended 'shortcut suppression' instruction telling the model to reason manually rather than invoke code/solver tools, then submitted to the target LRM to induce long trial-and-backtracking reasoning and correspondingly long output.

## Results

Across seven frontier LRMs (Claude-Opus-4.7, GPT-5.5, Gemini-3.1-pro, DeepSeek-v4-pro, GLM-5.1, MiniMax-M2.7, Kimi-K2.6) at the API level, SMTrap-Zebra reaches an average of 76,362 completion tokens (48.78% BNTS) and SMTrap-Sudoku reaches a 270.65x amplification ratio and 1,331.16s average reasoning time, outperforming AutoDoS, CatAttack and ReasoningBomb baselines by 2.74x-5.70x on average completion tokens. On the official OpenAI web interface, SMTrap-Sudoku reaches 314.97s on GPT-5.5 (vs 14.92-36.33s for baselines) and SMTrap-Zebra reaches 1308.33s on GPT-5.4. Stealthiness evaluation with a GPT-4o classifier rates 83.33% of SMTrap queries as 'normal' (100% for Sudoku, 66.67% for Zebra), higher than AutoDoS (16.67%) and comparable to ReasoningBomb (80%). The tool-based mitigation reduces total token usage by 97.08% (Sudoku) and 84.03% (Zebra), 90.15% on average, on GPT-5.5. A preliminary graph-coloring test shows high-conflict instances induce longer output (35,712 vs 20,127 tokens) than low-conflict instances, suggesting the effect generalises beyond Sudoku/Zebra.

## Limitations

The paper's own scope statement: the mitigation targets only the failure mode of unrestricted natural-language search on structured CSP-style tasks, not all possible LRM-DoS attacks. Main experiments are limited to Sudoku and Zebra-Game as CSP testbeds; generalisation to graph coloring is reported only as a preliminary, single-family test (low-conflict 20,127 vs high-conflict 35,712 output tokens on GPT-5.5). Stealthiness evaluation used a single external classifier (GPT-4o via OpenRouter) and found 10 of 30 Zebra queries still flagged as malicious. Kimi-K2.6 was excluded from the reasoning-time average because its batch API does not report per-case reasoning time.

## Why it matters here

- **overthinking**: The paper is not about the accuracy/efficiency tradeoff of reasoning length or about methods to make a model stop at the right point; instead it treats excessive reasoning length as an attack surface. It does provide an empirical, mechanistic account of one specific driver of overthinking-by-magnitude: it shows that CSP instances requiring more backtracking (measured by SMT conflict count) reliably induce longer LRM reasoning traces and output, and it demonstrates a defense (routing to a bounded external solver) that cuts induced token usage by over 90%. Relevant mainly as evidence on what structurally causes runaway reasoning length in CSP-style tasks, not as a study of when reasoning length helps or hurts accuracy.

## Entities

- **Concepts**: search amplification, SMT conflict count as a proxy for LRM backtracking search, trial-and-backtracking reasoning in constraint satisfaction, denial-of-service via induced overthinking, budget-normalised transfer score (BNTS)
- **Methods**: SMTrap, Search amplification, Z3 SMT solving, Conflict-guided clue-state branching and pruning, Tool-based mitigation (bounded local CSP solver)
- **Datasets**: Randomly generated Sudoku instances (9x9), Randomly generated zebra puzzle instances (nine houses, nine attribute categories), Graph coloring instances (generalisation test)

Tags: `denial-of-service`, `large-reasoning-models`, `smt-solver`, `constraint-satisfaction`, `adversarial-attack`, `test-time-compute`, `overthinking`, `mitigation`

## Abstract

Existing LRM-DoS methods rely heavily on model feedback to synthesize attack queries, requiring either repeated queries to the target model or training a dedicated attack model. These expensive operations severely weaken attack leverage. In this paper, we propose \emph{search amplification}, a novel, model-feedback-free LRM-DoS paradigm. It employs the conflict count derived from an Satisfiability Modulo Theories (SMT) solver as a low-cost external signal to guide the synthesis of inference-heavy Constraint Satisfaction Problem (CSP) instances. Our key observation is that LRMs depend on trial-and-backtracking search when solving CSPs, where higher SMT conflict counts on a given CSP instance positively correlate with more extensive LRM backtracking search and substantially longer output trajectories. Building on this finding, we propose \textsc{SMTrap}, a lightweight, CPU-only framework. Guided by SMT conflict counts, \textsc{SMTrap} generates inference-heavy CSP queries without model queries, attack-model training, or GPU computation. Evaluations across seven frontier models demonstrate the state-of-the-art LRM-DoS capability of \textsc{SMTrap}, producing DoS effects multiple times stronger than existing baselines. To mitigate the threat of \textsc{SMTrap}, we demonstrate a tool-based mitigation that significantly cuts token usage.

---

Record id: `arxiv:2608.18921`
