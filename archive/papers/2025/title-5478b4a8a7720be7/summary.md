<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/29093>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Dualformer trains a single Transformer on reasoning traces with parts randomly dropped, producing one model that can be run in a solution-only fast mode, a full-trace slow mode, or an auto mode that picks per problem.

## Problem

A model trained on complete search traces reasons at length on every input, and a model trained on solutions alone cannot reason at all; the two are separate models with fixed behaviour. Neither can be asked to spend less on an easy instance or more on a hard one, and training on complete traces also inherits the verbosity of whatever search procedure generated them. The open question is whether one model can hold both modes and choose between them, without the fast mode collapsing to the weak accuracy of a solution-only model.

## Contributions

- Randomised trace dropping as a training method: a four-level schedule (close clauses, then cost tokens, then 30% of create clauses, then the whole trace) sampled per example from Cat(p0,...,p4)
- A single Transformer supporting fast, slow and auto modes selected at inference by prompt, with no separate router
- Slow mode at 97.6% optimal rate on unseen 30x30 mazes with 45.5% fewer reasoning steps than the complete-trace Searchformer baseline at 93.3%
- Auto mode at 96.6% optimal rate with 59.9% fewer steps, showing learned per-instance mode selection
- Fast mode at 80% optimal rate versus 30% for a Solution-Only model, showing that trace supervision improves no-trace inference
- Greater trace diversity than Searchformer, and transfer of the dropping technique to LLM fine-tuning on math with one-to-two-point gains

## Method

Dualformer is trained on the A*-style search traces used by Searchformer, but the traces are randomised: during training, structured parts of each trace are dropped according to a schedule of four increasingly aggressive levels. Level 1 drops all close clauses; level 2 additionally drops cost tokens; level 3 additionally drops a random 30% of create clauses; level 4 drops the entire trace, which is exactly the solution-only case. Each training example is assigned a level by sampling from a categorical distribution Cat(p0,...,p4) whose probabilities are tuned per task. Because the model sees the same problems with traces of every length including none, it learns the mapping from problem to solution at several granularities of intermediate work at once. At inference the mode is set by the prompt: a control token requests solution-only output (fast), a control token requests the full trace (slow), or the standard prompt is used with no control token, in which case the model itself emits either kind of response - this is auto mode, so mode selection is learned behaviour rather than an external router or a confidence threshold. The same trace-dropping idea is applied to LLM fine-tuning on math data, where a single dropping rate p is used.

## Results

The paper measures both accuracy and trace length, so it does report a length/accuracy tradeoff rather than controllability alone. On unseen 30x30 mazes, slow mode reaches 97.6% optimal rate with 854 average trace tokens against Searchformer's complete-trace baseline at 93.3% with 1538 tokens - better accuracy at 45.5% fewer reasoning steps. Auto mode reaches 96.6% with 617 average tokens, 59.9% fewer than the 1538-token baseline, giving up one point of optimal rate for roughly a 2.5x shorter trace. Fast mode reaches 80% optimal rate against 30% for a Solution-Only model trained on solution-only data, so the same training data that produces the length reduction also lifts the no-trace mode by 50 points. On Sokoban, slow mode is 94.5% at 1482 tokens against 92.9% at 3600 tokens, and fast mode is 97.3% against 86.8% for Solution-Only. Dualformer also produces more diverse traces than Searchformer. The math transfer is much weaker: on Aug-MATH, Mistral-7B slow-mode greedy@1 is 18.6% (p=0.1) against a 16.9% baseline and pass@20 is 61.6% vs 59.6%; Llama-3-8B slow-mode greedy@1 is 20.5% (p=0.2-0.3) against 19.7% and pass@20 63.9% vs 62.7% - gains of one to two points, with no trace-length figures reported for the math setting.

## Limitations

Out-of-distribution generalisation is poor and the paper says so: a Dualformer trained on 20x20 mazes in slow mode solves not a single maze at low wall densities of 0.1-0.2. The strong results are on synthetic planning tasks (maze, Sokoban) where an A* search trace supplies exact, machine-generated intermediate steps and optimality is checkable; natural-language reasoning has neither property. The LLM math results are the honest measure of transfer and they are small (one to two points on Aug-MATH), and crucially the paper reports no trace-length reduction for the math setting, so the central length/accuracy claim is demonstrated on planning tasks only. The dropping-probability vector Cat(p0,...,p4) is tuned per task, and the math results are reported at particular p values (p=0.1 for Mistral, p=0.2-0.3 for Llama-3), which suggests sensitivity to that hyperparameter. Auto mode's decision quality is reported as an aggregate optimal rate and mean trace length, not as a per-instance measurement of whether it chose the right mode, so it is not shown that the auto-mode saving comes from correctly identifying easy instances rather than from being shorter everywhere. The authors point to curriculum learning and hierarchical planning as future work for more complex tasks.

## Why it matters here

- **overthinking**: On topic, and it does measure a length/accuracy tradeoff rather than controllability alone - but only on synthetic planning tasks. The maze and Sokoban tables report optimal rate against average trace tokens side by side, and the result the group should keep is that shortening was not paid for in accuracy: slow mode is both more accurate (97.6% vs 93.3%) and 45.5% shorter than the complete-trace baseline, and auto mode gives up one point for a 59.9% reduction. That is evidence that complete search traces are themselves padded, and that training on randomly truncated versions of them teaches a more compact route to the same answer - a different mechanism from stopping rules or length penalties, since nothing is being cut at inference time. The auto mode is also the cleanest example of learned per-instance mode selection with no external router or confidence threshold. Two cautions matter for how far this can be carried. The length/accuracy evidence does not extend to language: the Aug-MATH fine-tuning results give one to two points of accuracy and report no trace-length numbers at all, so the paper's central efficiency claim rests entirely on tasks with machine-generated A* traces and checkable optimality. And the auto-mode saving is reported only in aggregate, so the paper does not show that it shortens the easy instances specifically - which is the property an overthinking method actually needs.

## Entities

- **Concepts**: System 1 / System 2 Dual-Process Reasoning, Fast and Slow Thinking, Controllable Reasoning Mode, [Reasoning Trace Length](../../../../wiki/concepts/reasoning-trace-length.md), Trace Dropout, Auto Mode Selection, Reasoning Trace Diversity, Search Trace Supervision
- **Methods**: Dualformer, randomized reasoning traces, structured trace dropping, Searchformer (baseline), Solution-Only model (baseline), A* search trace supervision, [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md)
- **Datasets**: 30x30 and 20x20 maze navigation tasks, Sokoban, Aug-MATH, [GSM8K](../../../../wiki/datasets/gsm8k.md)

Tags: `fast-slow-thinking`, `dual-process`, `reasoning-trace`, `trace-dropping`, `controllable-reasoning`, `planning`, `test-time-compute`, `reasoning-length`

---

Record id: `title:5478b4a8a7720be7`
