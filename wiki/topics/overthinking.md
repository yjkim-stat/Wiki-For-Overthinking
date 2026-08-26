# Overthinking

<!-- auto:begin -->

When and why large reasoning models think more than a problem needs (or less than it needs) — the accuracy/efficiency tradeoff of reasoning length, test-time compute scaling, and methods to make a model stop, or keep going, at the right point.

- **Slug**: `overthinking`
- **Papers**: 437
- **Seminars**: 0
- **Tracked keywords**: `overthinking`, `underthinking`, `over-thinking`, `under-thinking`, `reasoning length`, `test-time compute`, `test time scaling`, `inverse scaling`, `chain-of-thought length`, `thinking budget`, `reasoning-action dilemma`, `large reasoning model`, `adaptive compression`, `accuracy-efficiency tradeoff`, `reasoning effort`, `thinking effort`, `reasoning budget`, `token budget`, `reasoning token`, `shared budget`, `resource-rational`, `compute-optimal`, `cost-bounded`, `early stopping`, `early exit`, `efficient reasoning`, `reasoning efficiency`, `parallel reasoning`, `test-time depth`, `token pricing`, `concise reasoning`, `adaptive reasoning`, `adaptive thinking`, `thinking model`, `reasoning trace`

## Most recent papers

- [TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models](../../archive/papers/2026/arxiv-2608-24232/summary.md) (2026-08-25)
- [Recursive Agentic Reasoning](../../archive/papers/2026/arxiv-2608-23956/summary.md) (2026-08-25)
- [Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding](../../archive/papers/2026/arxiv-2608-24024/summary.md) (2026-08-25)
- [A Data-dependent Early Stopping Rule using Rademacher Complexity with L1-norm](../../archive/papers/2026/arxiv-2608-24210/summary.md) (2026-08-25)
- [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](../../archive/papers/2026/arxiv-2608-24658/summary.md) (2026-08-25)
- [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](../../archive/papers/2026/arxiv-2608-23152/summary.md) (2026-08-24)
  - FIRE splits counterspeech generation into two sub-2B Qwen3-1.7B agents -- one that classifies the hate category, names the target group, writes a reasoning trace and triggers a web search for evidence, one that writes the reply -- with specialization coming from a contrastively-trained 22M retrieval encoder over annotated examples rather than from fine-tuning.
- [Cognitive Profiling of LRMs' Reasoning Traces Using Bloom's Taxonomy](../../archive/papers/2026/arxiv-2608-23205/summary.md) (2026-08-24)
  - The paper segments LRM reasoning traces into cognitive steps with Llama-3.3-70B-Instruct, labels each step with one of Bloom's six levels, and uses the resulting level proportions and 6x6 transition matrix to profile seven reasoning models and to predict solution correctness.
- [ParallelWorld: Test-Time Scaling for Embodied Reasoning](../../archive/papers/2026/arxiv-2608-22971/summary.md) (2026-08-24)
  - ParallelWorld is a verifier-guided tree search over simulated future observations for embodied reasoning: from a restorable simulator state it expands several candidate camera and physical actions in parallel, prunes branches with a verifier agent under a branch-width schedule, and answers from the top-ranked root-to-leaf route.
- [Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents](../../archive/papers/2026/arxiv-2608-22191/summary.md) (2026-08-23)
  - Risa reads the MoE router's expert-selection trace as a behavioral fingerprint of what a software agent is doing, using it to push sibling actions away from recently repeated computation during exploration and toward peer agreement once a patch is being written, then to arbitrate among completed attempts without an external judge or test execution.
- [More Experts, Worse Dynamics: Inverse Scaling and Spectral Bias in Mixture-of-Experts State-Space Models](../../archive/papers/2026/arxiv-2608-21840/summary.md) (2026-08-22)
  - A controlled synthetic study finding that mixing stable spectral state-space operators through a learned router fails to beat a single-expert baseline on regime-switching time series, with more experts making it worse, routing collapsing to one expert, and apparent MSE gains on chaotic data coming from variance suppression that destroys the attractor.
- [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](../../archive/papers/2026/arxiv-2608-21860/summary.md) (2026-08-22)
  - ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.
- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/2026/arxiv-2608-20256/summary.md) (2026-08-20)
  - Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models](../../archive/papers/2026/arxiv-2608-20055/summary.md) (2026-08-20)
  - A security study showing that the hidden chain-of-thought of a black-box reasoning model can be recovered near-verbatim through ordinary API tool-calling, because reasoning state must be retained across tool calls within a turn.
- [Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models](../../archive/papers/2026/arxiv-2608-18884/summary.md) (2026-08-19)
  - A training-free generate-critique-revise loop over a frozen backbone that stops when the critique emits a CONFIRMED sentinel or a depth cap is hit, measured across nine experiments to show the sentinel halts 82-88% of items at about 2.1 generations, with accuracy flat on BBH and significantly higher on GSM8K and MATH.
- [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](../../archive/papers/2026/arxiv-2608-18591/summary.md) (2026-08-19)
  - Trains a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given (document, prompt, model, reasoning budget) tuple, and uses those predictions to pick a per-sample reasoning budget for document tasks.
- [SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance](../../archive/papers/2026/arxiv-2608-18921/summary.md) (2026-08-19)
  - SMTrap uses SMT solver conflict counts as a free, model-feedback-free proxy to synthesize Sudoku and zebra-puzzle queries that induce excessive backtracking-driven reasoning in large reasoning models, mounting a state-of-the-art denial-of-service attack that a bounded-solver defense can neutralize.
- [Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck](../../archive/papers/2026/arxiv-2608-18931/summary.md) (2026-08-19)
  - A compute-normalised, five-benchmark comparison of test-time scaling methods on open-ended generation finds that the candidate pool improves steadily with compute, but exploitation - selecting or synthesising the final answer from that pool - is the bottleneck, with reward-model-based selection near random (verifier correlation ~0.12) and even the best method (Fusion) recovering only ~40% of available quality.
- [Think Shallow, Solve Deep: Controlling Recurrent Dynamics for Reliable Test-Time Depth](../../archive/papers/2026/arxiv-2608-18222/summary.md) (2026-08-18)
  - Shows that whether a recurrent-depth reasoner is helped or harmed by extra test-time iterations is predicted by a measurable dynamical property of its trained update map (settling, marginal, or drifting), proves a sufficient condition for the decoded answer to be frozen under further iteration, and demonstrates that a single terminal fixed-point loss term moves the regime and the depth behaviour together in both directions.
- [ParaTempo: Efficient Parallel Reasoning via Temporal Confidence](../../archive/papers/2026/arxiv-2608-16425/summary.md) (2026-08-17)
  - A training-free controller for parallel reasoning that probes each branch every 500 tokens for a tentative answer distribution, averages recent probes into a 'temporal confidence' score, and uses that one signal to prune, retire, fork and globally stop branches.
- [The Price of Thinking: Reasoning Effort as a Model-Specific API Contract](../../archive/papers/2026/arxiv-2608-16956/summary.md) (2026-08-16)
  - A preregistered, paired 360-call measurement on 30 AIME 2026 items of what a buyer gets by setting a reasoning-effort parameter explicitly versus omitting it on the same model, pricing every paid attempt including wrong and no-answer ones.
- [Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning](../../archive/papers/2026/arxiv-2608-15065/summary.md) (2026-08-15)
  - Funnel of Thoughts detects and discards the subset of parallel reasoning rollouts that are spiraling into unproductive self-correction (flagged by a rising density of hesitation words like 'Wait' and 'perhaps'), matching self-consistency's accuracy while cutting attention FLOPs by up to 56% and wall time by 37.6%.
- [Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis](../../archive/papers/2026/arxiv-2608-15303/summary.md) (2026-08-15)
  - Divergent-Convergent Reasoning generates diverse candidate solutions and then uses reviewer-style reconciliation calls (optionally run recursively with a verifier-free unanimous-consent stopping rule) to recover correct answers even when they start out as a minority, reaching 93.3% on AIME 2024 and 92.0% on AIME 2025 while using about 27% less compute than a fixed single-round baseline.
- [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](../../archive/papers/2026/arxiv-2608-14161/summary.md) (2026-08-14)
  - Introduces BiasTrace, a six-label annotation scheme for reasoning behaviours in bias-sensitive traces, and finds that overthinking (repeated second-guessing or revisiting the same options more than three times) is the strongest behavioural predictor of stereotype-aligned answers on BBQ, then uses the scheme to filter samples at inference time.
- [Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services](../../archive/papers/2026/arxiv-2608-13315/summary.md) (2026-08-13)
  - Models an LLM reasoning service as a Stackelberg game in which the provider sets a per-token price and a default reasoning-token budget while the user may keep the default, customize it, or exit, and shows the provider's optimal default sits above the budget the user would choose.
- [Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models](../../archive/papers/2026/arxiv-2608-13760/summary.md) (2026-08-13)
  - Annotates 15,282 reasoning traces from 15 models on 6 benchmarks with a nine-behavior taxonomy and shows that the behaviors reasoning-oriented training amplifies most (self-correction, hypothesis testing, uncertainty acknowledgment) are not the behaviors most associated with getting the answer right (confidence calibration, knowledge alignment, self-awareness).

<!-- auto:end -->

## Notes

# Does a reasoning model spend its thinking on how hard a problem is, or on how hard it looks?

Assembled 2026-08-21 from the archive. Each stage is a question the next
stage depends on, and the evidence for each is drawn only from records this
archive holds. Where a record is abstract-only, that is said.

## Stage 0 — Is there an allocation problem at all?

Only if more thinking is not monotonically better. It is not.

*When More is Less* derives an inverted U from per-step error accumulation:
accuracy first rises as insufficient reasoning is filled in, then falls as
errors from unnecessary steps dominate, with optimal length rising in task
difficulty and falling in model capability. *When More Thinking Hurts*
measures the same curve directly — marginal utility per 500 tokens falls from
+3.2% in the 0.5-2K range to -0.3% in the 12-16K range, and the ratio of
answer-worsening to answer-improving flips crosses 1.0 at about 7K tokens for
R1-32B and about 5K for s1-32B, reaching 7.55 at 16K. *Inverse Scaling in
Test-Time Compute* finds inverse or noisy-inverse scaling in the majority of
task-model pairs across nine models. *Does Thinking More Always Help?* offers
a mechanism — extended single-chain thinking raises output variance rather
than improving reasoning — and shows parallel sampling at the same budget
beating it by up to 20%.

**A finite optimum exists, and it differs per problem.** So allocation is a
real decision, not a free parameter.

## Stage 1 — Does allocation respond to anything?

Yes. *Between Underthinking and Overthinking* shows models lengthen on
easy-question sets they are advantaged on (GSM8K 1,015 -> 1,349 tokens; MATH
1,691 -> 2,833). *DiffAdapt* measures realised allocation spanning 198 tokens
on GSM8K to 4,675 on AIME25. Allocation is not a constant.

## Stage 2 — What does it respond to: difficulty, or surface form?

Three independent designs separate the two, and all three answer surface form.

**Distractor count, difficulty held fixed.** *OptimalThinkingBench* adds
irrelevant multiple-choice distractors to trivially easy questions and finds
thinking tokens rise near-linearly at **42 tokens per added distractor,
R^2 = 0.94**. Nothing about the problem got harder.

**Presentation position, value made explicit.** *Thinking Hard, Not Smart*
gives models an exam of N questions with visible point values under one shared
token budget. Effort correlates with **position** at -0.17 / -0.38 / -0.48 for
N = 5 / 10 / 20, and solving order tracks position at rho = +0.68. Effort
correlates with **point value at 0.00 / +0.04 / +0.11** — that is, models
ration by reading order and ignore the stated value of the question. The
reached work set overlaps a value-density ranking at chance (0.59) but
overlaps early-position ranking at 0.76. An explicit planning prompt improves
coverage and leaves the position dependence intact.

**Misleading preamble, answer held fixed.** *Inverse Scaling in Test-Time
Compute* prefixes a trivial counting question (answer always 2) with
irrelevant numeric riddles; DeepSeek R1 falls from about 70% to about 30%
with five distractors under natural overthinking.

Scale does not repair this: on *OptimalThinkingBench*, Qwen3 from 1.7B to
235B raises thinking tokens 750 -> 950 with accuracy flat at 86.1-86.8%.

## Stage 3 — When is the decision taken?

Before generation begins. Three papers establish this by different means.

*On Reasoning Strength Planning* trains linear probes on **question
activations** that predict reasoning token count before any token is
generated, and isolates a direction whose addition and subtraction move
length and performance causally. *DiffAdapt* classifies difficulty from the
final hidden state of the **question prefill**. *Sonata* (in *Adaptive
Thinking: LLMs Know When to Think in Latent Space*) predicts self-consistency
from prefill representations and drives budget from it, reporting 20-80%
token reduction (the two circulated abstracts disagree; see the record).

**The eventual length is already present in the representation of the
question.** Allocation is a precondition of reasoning, not a product of it.

## Stage 4 — What is in that decision?

*The First Impression Problem* runs the two counterfactuals that matter:
removing the question from context after the model has processed it reduces
redundant reasoning, and injecting a bias increases overthinking
proportionally, with attention to the question as the channel. Its most
consequential result is negative — **none of the tested overthinking
mitigations removed the influence of internal bias.** (Abstract-only record;
benchmarks and effect sizes are not available here.)

*Base Models Know How to Reason, Thinking Models Learn When* decomposes the
base-to-thinking gap into mechanisms (steering directions that induce a
reasoning behaviour) and heuristics (classifiers deciding when a mechanism
fires), and recovers ~76% of the RL gap that way against ~11% of the SFT
gap. What thinking training adds is largely a **firing heuristic**, not new
reasoning machinery.

So: the model learned when to think, and the input to that judgement is its
first impression of the problem.

## Stage 5 — Three predictions this picture makes, and whether the archive bears them out

**A. Adaptation should hold on easy problems and collapse on hard ones,**
because surface impression and true difficulty diverge most where problems
are hard. Confirmed four ways. *Between Underthinking and Overthinking*:
length-difficulty coupling is non-significant or reversed on hard sets
(Table 3), while incorrect answers run far longer than correct ones (MATH
6,106 vs 2,460 tokens, Pearson -0.7248). *DEER*: compression is about 67% on
GSM8K against about 25% on AIME 2024 — the saving is largest where inference
was already cheap. *BLADE*: savings concentrate on problems the model was
going to get right anyway, and its accuracy cost concentrates too (MATH-500
-4.2 points on Qwen3-8B). *Token Budget Saturation*: on AIME, allocation does
not degrade gracefully but goes bimodal — 43.5% of generations never emit
`</think>` within 10,000 tokens and score 11.5%, against 96.5% for those that
converge.

**B. Single-point markers should fail as overthinking signals; only temporal
structure should work,** because the misallocation is fixed at the start and
only its consequences accumulate. Confirmed — this is
[finding:11877d6cb7defd0d](../findings.md). *Amplified Does Not Mean
Predictive* finds the presence of expressed uncertainty carries Lift -16.1%
(VLM) / -13.9% (LLM), while every working signal in the archive is a rate or
window: answer-oscillation count (r = 0.78), hesitation density per 1,000
characters (*Funnel of Thoughts*, whose ablation shows random pruning loses
what density pruning preserves), keyword inter-arrival times, a W=7
confidence window (*ParaTempo*). *Token Budget Saturation*'s activation probe
at token 150 reaches only AUC 0.608 (sweep p = 0.063) — early, but weak.

**C. Mitigations that target length should hit a ceiling and pay for it
elsewhere,** because length is the output of allocation, not its input.
Confirmed. *OptimalThinkingBench* tests five mitigation families: they cut
overthinking tokens by 12-91% and degrade UnderthinkingBench accuracy by up
to 13%, with 2 of 6 method-model combinations scoring below their own base
model overall. *Between Underthinking and Overthinking* applies SimPO
preferring the shorter response regardless of correctness and gets 30-60%
fewer tokens — but the saving comes mainly from shortening **incorrect**
responses, which were the long ones. *Do LLMs Overthink Basic Math* finds
concise prompting cuts tokens 38-63% for 1.4-3.9 accuracy points and does not
close the efficiency gap at all.

## Conclusion

**The deficit is not in the ability to allocate but in the signal allocation
is conditioned on.** Models can vary thinking effort (Stage 1), do vary it,
and fix the amount at read time (Stage 3) — but the only information
available at read time is how the problem presents itself, and presentation
tracks difficulty well on easy problems and poorly on hard ones (Stages 2
and 5A).

Three things follow.

**Overthinking and underthinking are not two conditions.** They are the two
tails of one miscalibrated allocation function. That is why every mitigation
family in *OptimalThinkingBench* that fixes one tail damages the other, and
why no model among 33 balances both.

**Length-targeted intervention is bounded in principle.** Length is what
allocation emits. Compressing it leaves the decision that produced it
untouched, which is exactly what *The First Impression Problem* observes when
no mitigation removes the internal-bias effect.

**The two directions that are not bounded that way are improving the read-time
signal, or moving the decision later.** The first has a measured ceiling:
DiffAdapt realises 9.7-22.4% savings against an oracle's ~50% with +10
accuracy points, so most of the headroom is lost to probe error, and the
result measures the difficulty probe more than the strategy. The second is
where the archive's strongest efficiency results sit — DEER (19.1-80.1%
shorter at +0.3 to +5.0 accuracy), ParaTempo, Funnel of Thoughts (SC@32
accuracy at -54.5% attention FLOPs) — and this analysis explains why:
**mid-generation is the only place a wrong first impression can be observed
being wrong.**

## What would overturn this

- **o3 scales positively** on Misleading Python and on 8x8 Zebra grids in
  *Inverse Scaling*. Surface dependence may be a property of particular
  training recipes rather than of reasoning models generally.
- **ARES deliberately spends 38% more on AIME25** while cutting GSM8K by 22%.
  Reallocation in both directions is achievable, so nothing here is a hard
  limit.
- **AdaptThink improves both tails** in *OptimalThinkingBench* — the only one
  of five families that does. The trade-off may not be necessary.
- **The evidence is overwhelmingly maths and code.** One agentic study (*The
  Danger of Overthinking*), one subjective-task study. Whether the same
  allocation function is what fails in an agent loop is queued as
  `synthesis__q-85150997e2cfc3ad`.
- **Stage 1 and 5A rest partly on two 1.5B models at N=10** (*Between
  Underthinking and Overthinking*), and Stage 4 rests partly on two
  abstract-only records.

<!-- analysis-sources: 21 -->
