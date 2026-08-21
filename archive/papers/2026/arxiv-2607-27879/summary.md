<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents

- **Authors**: Stef Cuyckens, Mihaela Jivanescu, Jun Yin, Chao Fang, Marian Verhelst
- **Venue**: cs.AR
- **Published**: 2026-07-30
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2607.27879>
- **PDF**: <https://arxiv.org/pdf/2607.27879v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

Ares is an LLM-agent RTL optimizer that raises the per-call reasoning effort only after progress stalls, and reports the normalized dollar cost of every call next to the power-area-delay figure of merit.

## Problem

LLM agents that optimize RTL iterate edit-synthesize-measure loops, paying per LLM call. Prior agents report the quality reached without its normalized cost, credit that quality to how their cross-design long-term memory is engineered, and hold the per-call reasoning effort fixed. A fixed high effort spends deep reasoning on iterations a cheap edit would have solved; a fixed low effort under-reasons on the iterations that need it. Without a per-call cost metric neither the attribution to memory nor the choice of effort level can be checked at equal spend.

## Contributions

- A normalized per-call dollar cost metric, reported alongside the figure of merit, that makes optimization quality and spend comparable across reasoning-effort levels and across optimizers
- A cost-controlled comparison showing that an engineered cross-design long-term memory brings no dependable gain over a plain concatenation of the same experience, though both beat having no long-term memory
- An adaptive per-call reasoning-effort policy driven by a patience counter fit once on training designs, escalating from medium to high only after progress stalls
- Evidence on three held-out designs that the adaptive policy reaches a lower FoM than any fixed effort level at equal normalized cost, and cuts run-to-run variance by 58% on a multiply-accumulate case study

## Method

Each iteration hands the running-best RTL, the run's conversation, and a markdown long-term memory to the agent, which proposes an edit at the effort level set by the policy. The candidate must pass a 10^4-vector random testbench and RTL sequential equivalence checking against the input design v0 (JasperGold), is synthesized with Synopsys Design Compiler on Nangate 45nm, re-verified on the netlist, and scored by FoM = (area/area0)(power/power0)(delay/delay0), so FoM(v0)=1 and lower is better. Cost is the per-call dollar sum over input, cache-read, cache-write and output tokens at published OpenRouter prices (reasoning tokens are billed as output), reported in 'high-calls' - dollars divided by that design's mean cost of one high-effort call. The effort policy is a two-state machine over a patience counter C: a stalled iteration (valid candidate, no FoM gain) adds 1, a failed one (no valid candidate) adds w, an accepted improvement discharges C -> C*max(0, 1 - dFoM/kappa) where dFoM is the relative FoM gain. When C reaches p the next call runs at high effort and C resets; every design starts at medium. p=3, w=2.8, kappa=0.05 were grid-fit once on the 21 training designs, catching 94% of warranted escalation points while keeping >=90% of fired escalations warranted. A separate experiment holds everything fixed and varies only how the same pool of raw experience is written into long-term memory: none, plain concatenation, or an engineered superset with (context, action, result) cases, explicit anti-optimizations, deduplication, effectiveness ranking and anonymized design names.

## Results

All numbers are from a commercial synthesis flow (Synopsys DC + PrimeTime, Nangate 45nm), not from silicon; the agent runs on Claude Code with Opus 4.6, repeated multiple times because the LLM cannot be seeded. On the three held-out test designs (tv80 ALU, uart, AES controller) the adaptive policy ends at mean FoM 0.76, 0.77 and 0.73 against fixed high's 0.79, 0.84 and 0.79, i.e. it lowers FoM by 23-27% where the best fixed effort reaches 16-23%, at equal normalized cost. The fixed-effort sweep shows no level fits a whole run: low effort ends above medium everywhere and stops early because the LLM reports it is out of ideas; high effort lands its first successful optimization only after 4.6-7.1 high-calls where medium cuts its first 5% of FoM within 0.9-3.9; fixed high ends clearly deeper than medium only on tv80 (0.79 vs 0.84), the gap being 0.004 on uart and 0.016 on controller. Memory construction: with the same raw experience, the engineered memory and the plain concatenation descend together and end close on all three test designs with neither consistently ahead, though both end below the memoryless agent. On an LLM-drafted MX multiply-accumulate unit, six runs lower unnormalized FoM from 68.8 to a mean of 33.6 (deepest 27.5) against the hand-optimized MX_fp32's published 18.9, closing up to 83% of the gap; the same optimizer improves the already hand-optimized MX_fp32 by only 16%. Branching each of those six runs at its stall point, the escalated continuation beats the fixed-medium one in five of six (the sixth within 2%), lowering the mean from 42.1 to 33.6 and cutting run-to-run std from 8.9 to 5.8 (a 58% variance reduction) for 7.3 extra high-calls. Against prior optimizers on controller from the same v0 with 25 candidates each, Ares reaches FoM 0.694 at about 15 high-calls, REvolution 0.943 at about 10, and Dr. RTL 0.923 at 8.7x Ares's cost; Dr. RTL's timing-focused selection discards its own best power-aware candidate at 0.909.

## Limitations

The test set is three designs, and the MX study is a single additional design; the escalation constants were fit on 21 training designs from the same open-source pool, so nothing shows the policy transfers to other design families or other LLMs. The effort knob is the model's own three-level setting rather than a measured reasoning length, and the paper does not report how many tokens each level actually consumed or what the escalations changed about the edits. Only two of the compared systems release code, and REvolution was adapted by the authors onto their own flow, so its numbers are not the authors' own reported ones. Costs are OpenRouter list prices for one model at one point in time, and the LLM cannot be seeded, so every curve is a mean over a small number of runs with the run-to-run spread (std 8.9 on the MX unit) comparable to some of the reported gains. The memory finding is a negative result on three test designs with one experience pool and does not establish that memory construction cannot matter. The long-term memory holds only 21 designs, which the authors say likely limits how deep the MX draft could be pushed.

## Why it matters here

- **overthinking**: A domain application rather than a study of reasoning length itself, but a substantive one: it treats per-call reasoning effort as a control variable and shows an escalate-on-stall policy beating every fixed level at equal spend (FoM lowered 23-27% vs 16-23%), which is the overthinking thesis measured in dollars instead of tokens. Two things here are worth carrying over. First, the unit of allocation is an iteration inside a multi-step agent run, not an isolated prompt - the authors note that prior budget-aware work (FrugalGPT, budget-aware tree search, compute-optimal scaling) adapts a single task, whereas here the difficulty of the next improvement changes as the design gets more optimized, so the difficulty signal has to be read from the run's own history. Second, the stall signal is entirely external: the counter charges on verified-but-no-gain and on failed candidates, never on anything inside the reasoning trace, which is a cheap difficulty proxy the archive's trace-inspecting methods do not use. The evidence that a fixed high effort is not merely wasteful but actively worse early in a run (first gain only after 4.6-7.1 high-calls, where medium gains within 0.9-3.9) is a concrete instance of overthinking costing time-to-first-improvement. Caveats for the topic: the effort knob is the provider's three-level setting, no reasoning-token counts or trace lengths are reported, and the accuracy axis is a hardware figure of merit rather than task correctness, so the tradeoff curve is not directly comparable to reasoning-benchmark results.

## Entities

- **Concepts**: Adaptive Reasoning Effort, [Test-Time Compute Allocation](../../../../wiki/concepts/test-time-compute-allocation.md), Cost-Aware Inference, Patience-Based Escalation, Agent Long-Term Memory, PPA Figure of Merit
- **Methods**: [Ares](../../../../wiki/methods/ares.md), adaptive reasoning-effort steering, patience counter with stall/failure charging and gain-proportional discharge, normalized per-call dollar cost (high-calls), engineered vs. baseline markdown long-term memory, sequential equivalence checking (JasperGold), Synopsys Design Compiler / PrimeTime synthesis and power flow, Dr. RTL, REvolution
- **Datasets**: 24 open-source RTL modules: 19 of the 20 Dr. RTL designs, FFT butterfly and Huffman decoder from RTLRewriter, CORDIC, pipelined FFT and JPEG DCT from OpenCores, held-out test designs: tv80 ALU, uart, AES controller, MX_fp32 microscaling multiply-accumulate unit and its LLM-drafted counterpart MX_LLM, Nangate FreePDK45 open cell library

Tags: `adaptive reasoning effort`, `test-time compute`, `inference cost`, `llm agents`, `rtl optimization`, `eda`, `agent memory`

## Abstract

Large language model (LLM) agents optimize the power, performance, and area (PPA) of register-transfer-level (RTL) designs by iterating over edits, synthesis, and PPA analysis, paying a dollar cost for every LLM call. Prior agents report the quality reached without its normalized cost, attribute that quality to an engineered cross-design memory, and hold the reasoning effort of every call fixed. We propose Ares with three corresponding innovations. (1) We introduce a normalized dollar cost per LLM call reported alongside the figure of merit (FoM), enabling fair comparison across effort levels and optimizers. (2) Using this accounting, we find the construction of the long-term memory matters little. An engineered memory brings no dependable gain over a plain concatenation of the same experience. (3) We instead adapt the per-call reasoning effort by escalating to deeper reasoning only once progress at a lower effort stalls, via a patience counter fit on 21 training designs, allocating reasoning where it pays rather than uniformly across all iterations. On three test designs unseen during training, the effort policy lowers the FoM by 23-27% where the best fixed effort reaches 16-23%, at equal normalized cost. Ares closes up to 83% of the gap from an LLM-drafted multiply-accumulate unit to its highly hand-optimized counterpart, and reaches a 25% deeper FoM than state-of-the-art Dr. RTL at 12% of its tokens.

---

Record id: `arxiv:2607.27879`
