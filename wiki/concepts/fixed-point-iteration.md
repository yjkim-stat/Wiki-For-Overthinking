# fixed-point iteration

<!-- auto:begin -->

In these sources fixed-point iteration means running one block of weights repeatedly on its own output until the representation converges, so that compute is spent on depth of iteration rather than on more parameters; it is a third notion of variable computation, distinct from both exiting a reasoning trace and exiting a layer stack at an intermediate head. 'Expressive Power of Implicit Models' treats it as the defining construction of implicit models - an infinite-depth, weight-tied network trained with constant memory - and proves that for a broad class of such models expressive power grows with the number of test-time iterations, validated across imaging, scientific computing, operations research and LLM reasoning. MIND over Body applies the same idea per layer, iterating until the layer's activations converge, with a separate introspection model trained under an auxiliary loss to predict when the iteration can be skipped entirely, in both a CNN and a transformer. The archive's own record flags that this second, layer-level description comes from a third-party summary of the paper's talk and could not be confirmed against the paper, whose abstract states the mechanism only as adapting parameter count and computation time to task complexity.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Test-Time Scaling](test-time-scaling.md)

## What we have settled

- **Established** — Proposition 1(b) cannot be applied to autoregressive chain-of-thought stopping rules as a theorem, because none of its three quantities is defined there -- consecutive states do not inhabit a common metric space, so delta_t, the decision margin mu and the remaining path length R_t have no referents and R_t's finiteness cannot be estimated even in principle -- yet the failure it formalises is separately observed on token recurrence, so a fixed-window answer-invariance rule is exposed to the phenomenon while nothing in this framework can certify or refute it.
  - Proposition 1 is stated over a recurrent-depth reasoner: z_t is a point in a fixed R^d, one update map f produces z_{t+1} from z_t, delta_t = ||z_{t+1} - z_t||, the decoder g is defined on the whole space, and mu(z_t) is the largest r with g constant on the open ball B(z_t, r). Branch (a) certifies g(z_s) = g(z_t) for all s >= t whenever R_t = sum of delta_u over u >= t is below mu(z_t); branch (b) says that when R_t diverges no finite window of answer-constancy certifies the next step, and this can happen with delta_u -> 0, witnessed by f(z) = z - (c, 0, ...) with g = sign(z_1), where the answer holds for floor(D/c) steps and then flips, and equally by delta_u = 1/u.

Every step of that construction needs the three structural facts autoregressive decoding does not supply. The state after t tokens is a prefix (or its KV cache) of length t and the state after t+1 tokens has length t+1, so the two do not lie in one space and their difference is not defined without an arbitrary choice of embedding. The margin mu requires g to be evaluable at every point of a ball around the current state, but perturbing a KV cache does not produce a state the model could have reached, so 'the answer at all states within distance r' names nothing. R_t is a sum of undefined terms. The question asks whether R_t's finiteness can be estimated in autoregressive CoT; the answer is that there is no R_t to estimate, and this is a category obstruction rather than a measurement difficulty -- picking some embedding would make the numbers computable and the theorem still would not apply, because branch (a)'s triangle-inequality proof needs g's constancy on metric balls of the actual state space.

The paper itself draws this line. Section 7.2 gives chain-of-thought its own depth knob and reproduces the non-settling fates on three open models -- a distilled reasoner destroyed by more of the budget it needs (0.82 -> 0.00) and a non-reasoning model degraded by thinking it does not need (1.0 -> 0.47) -- and then says exactly what does not carry across: 'a shared failure shape, not mechanism identity', and 'the case for latent depth is the handle: only the latent loop exposes a state one can measure and repair'. Guess-freezing, which branch (b) formalises, is thus observed behaviourally in token recurrence and provable only in the latent one.

Rewriting the archive's rules in the surviving language -- answer-constancy runs, which is all that remains once delta and mu are gone:

C4's CVEE re-extracts an answer candidate a_t at every step and tracks run_t, the consecutive steps since the candidate last changed, resetting to 1 on change, plus changes_t, the number of changes so far. Both gates must pass: confidence c_t >= tau_CVEE and stability run_t >= r_t, with r_t = max(p_min, ceil(gamma * changes_t)). The required window is therefore not fixed -- it grows with observed instability, so a perpetually flipping trajectory pushes the threshold up rather than tripping the gate. That is a real partial defence the question did not account for, and it is still a finite window at every t, which is precisely what branch (b) says cannot certify: the counterexample's answer is constant for floor(D/c) steps before flipping, and D is arbitrary, so for any r_t there is a trajectory that satisfies it and then flips.

ParaTempo probes every 500 generated tokens, keeps the top 20 answer candidates, and averages the last W = 7 probes into a temporal confidence used to prune, retire, fork and globally stop. W is a fixed constant, so it has no analogue of C4's escalation and is exposed without qualification.

Consilience does not belong in this list. It is not a stopping rule: it skips the first P tokens, averages the first and last W token confidences of a *completed* sequence into C_initial and C_final, scores S = C_final - alpha * C_initial, and selects the completion maximising S among sampled completions. It never certifies a next step, so branch (b) has no purchase on it.

DEER cannot be rewritten from this archive. Its record carries no document and no reading, so its trial-answer confidence rule is known only by title here.

The practical consequence is narrower than the question supposed: the exposure of these rules is an empirical matter to be settled by measuring flip-after-stability rates on real traces, not a corollary of Proposition 1, and a paper that cites branch (b) against a token-level stopping rule is borrowing the authority of a theorem whose premises it cannot check.

## Appears in

- [MIND over Body: Adaptive Thinking using Dynamic Computation](../../archive/papers/2025/title-3d49618364a0cc92/summary.md) — Adds a self-introspection module to CNN and transformer networks that decides, per input, how many parameters to reuse and how long to iterate, so computation scales with input complexity rather than input size.
- [Expressive Power of Implicit Models: Rich Equilibria and Test-Time Scaling](../../archive/papers/2026/title-acc0cd457f5fd230/summary.md) — Provides a mathematical theory showing that implicit (weight-tied, fixed-point) models' expressive power grows with the number of test-time iterations, validated across imaging, scientific computing, operations research and LLM reasoning.

<!-- auto:end -->

## Notes

# Where the fixed-point framing meets overthinking — and where it stops

Assembled 2026-08-21 from the archive. Evidence is drawn only from records
this archive holds; where a record is abstract-only, that is said.

**No `analysis-sources` marker.** That counter is checked against this note's
own evidence, and this section deliberately rests on eleven records most of
which are not attached to this concept — `arxiv:2608.18222`,
`title:acc0cd457f5fd230`, `title:f75fffe554037a34`, `arxiv:2607.25915`,
`title:3d49618364a0cc92`, `arxiv:2607.28166`, `arxiv:2608.02942`,
`title:0393ca4ca3f4fb8c`, `arxiv:2608.16425`, `arxiv:2608.09898`,
`title:f508a5b012a33fd1`. Declaring a number here would report as
over-declared for ever rather than tracking anything.

**The auto block above under-counts this concept.** It shows two sources
because *Think Shallow, Solve Deep* filed its own vocabulary under separate
concept names — `depth-safety`, `guess-freezing`, `latent-attractor`,
`fixed-point-objective-terminal-residual-penalty`,
`per-step-displacement-and-remaining-path-length`, each sitting at one
evidence and below the promotion threshold. That paper is the centre of this
subject and does not appear in the list above. Not merged: an objective term
and an iteration scheme are different things, and forcing them into one slug
would fuse two entities rather than mislabel one.

## No source in this archive invokes Banach

A search of every reading and every abstract the archive holds returns zero uses of
`Banach`, `contraction mapping`, `Picard iteration` or `Anderson
acceleration`. The nearest hits are in `data/abstracts/` — the ledger of what
arXiv announced, not what the archive tracks: `2608.15966` (*A Banach-Space
Theory of Markovian Halpern Iteration for Non-Expansive Maps*, which replaces
the Hilbert-space potential with a **displacement-level Halpern bound** for
`Õ(ε⁻³)` sample complexity) and `2608.17666` (*Picard Proximal Monte Carlo*,
Bayesian imaging). Neither concerns reasoning. The tooling exists one field
over and has not been carried across.

What the archive holds instead is one paper that states the Banach hypothesis
precisely in order to **deny** it.

## Proposition 1 is the negation of Banach's premise

*Think Shallow, Solve Deep* (`arxiv:2608.18222`, read from the document)
defines per-step displacement `δ_t = ‖z_t − z_{t−1}‖`, decision margin
`μ(z_t)` — the largest radius on which the decoder is constant — and
remaining path length `R_t = Σ_{u≥t} δ_u`. Then:

- **(a)** `R_t < μ(z_t)` ⟹ the decoded answer is constant for all `s ≥ t`.
  The proof is the triangle inequality. No contraction, no Lipschitz bound.
- **(b)** If `R_t` diverges, **no finite window of answer-constancy certifies
  the next step** — and this happens even when `δ_u → 0`. The paper's example
  is `δ_u = 1/u`. Branch (b) is its formal definition of **guess-freezing**.

Banach assumes a contraction `q < 1`, from which `δ_u ≤ q^u δ_0` and
`R_t < ∞` follow for free. Proposition 1 drops that assumption and demands
`R_t` directly, because in a trained operator it is not free.

**This is the only theorem in the archive that licenses stopping.** Every
other halt signal here — DEER's trial-answer confidence, ParaTempo's
temporal-confidence window, C4/CVEE's run counter, Consilience's boundary
score — is an empirical threshold.

## The operator is empirically not a contraction, and it does not need to be

The same runs log the step-Jacobian spectral norm `σ_max ≈ 5.6`. That is the
local Lipschitz constant, and it is far above 1. The causal ablation then
holds architecture, data and `σ_max` fixed and removes only the terminal
fixed-point loss term:

```
λ_max              −0.06  →  +0.10        (finite-time Lyapunov exponent)
Kaplan-Yorke dim        0  →  8
Sudoku conversion    0.34  →  0.03
reachability         peak 0.97 held, up to 0.37 EM lost by hc=128
```

**The lever is the finite-time Lyapunov exponent, not the Lipschitz
constant.** Regime labels are thresholded on `λ_max` (settle < −0.05,
marginal ±0.05, drift > +0.05). Global contraction neither holds nor is
required; local finite-time settling is.

The runs also log **Henrici non-normality** alongside `σ_max` and the
spectral radius `ρ`. A non-normal operator with `ρ < 1` amplifies for many
steps before contracting — the standard reason a spectral-radius test in the
Banach style misleads, and the reason this paper measures the transient
instead of the spectrum alone.

## Building the fixed point into the architecture is not the same as training toward one

Seven architectures re-implemented at matched size and budget on identical
data: TRM-style, UT/URM, **FPRM (Fixed-Point Reasoners)**, **EqR (Equilibrium
Reasoners)**, **DEQ (Deep Equilibrium Models)**, Neural GPU, SE-RRM. Adding
only the fixed-point objective to each:

- generic recurrence: `0.12 → 0.88`, overthink damage `0.91 → 0` (18 seeds)
- UT/URM on Sudoku: `0 → 0.16–0.19`; FPRM on carry: responds
- **EqR: no response**
- **DEQ: stops fitting the training set at all, 10/10 seeds**

The two architectures named for equilibria are the two the equilibrium
objective fails on. The authors report this as the intervention's boundary
and do not explain it. Nothing in the archive does.

Failure under depth is sharp where it occurs: UT/URM on carry propagation
reaches `0.95` at `hc=32` and collapses to `0.05` at `hc=128`.

## Output stability is not a substitute for a latent attractor

The paper's own control: an objective penalising **only the decoded answer's
change** — latent-free — produces neither conversion nor depth-safety, while
the latent version produces both.

Every stability-based halt rule in this archive measures the latent-free
quantity:

| Rule | What it actually measures |
| --- | --- |
| C4 / CVEE (`arxiv:2607.28166`, document) | `c_t ≥ τ` **and** `run_t ≥ max(p_min, ⌈γ·changes_t⌉)` — consecutive steps with the extracted answer unchanged, with each flip demanding a longer subsequent run; no hyperparameter refers to the step budget, so the gate is schedule-independent |
| OPTD (`arxiv:2608.02942`, document) | largest `m` whose commitment leaves the teacher's rollout outcome unchanged — an invariance test |
| DEER (abstract) | geometric-mean token probability of the trial answer ≥ 0.95 — confidence, not stability |
| ParaTempo (`arxiv:2608.16425`, document) | `exp(−H)` over a `W=7` sliding window of probes |
| Consilience (`arxiv:2608.09898`, document) | `C_final − α·C_initial` across a boundary window |
| Atom of Thoughts (abstract) | contracts each state into an answer-equivalent simplified question, so no history accumulates — the archive's only attempt to give autoregressive reasoning a fixed-size state at all; no convergence claim and no numbers |

Proposition 1(b) says why this is exposed: an unchanging output is evidence
only when `R_t` is finite, and a harmonically-decaying trajectory looks
perfectly converged to every one of the confidence measures above. **Whether
that exposure is real for these specific rules is filed as
`synthesis__q-51e2c59f5ddee7d2`, not settled here.**

## The framing has reached real language models — narrowly

Correcting a narrower claim made earlier in conversation: this is not
confined to small synthetic tasks.

**Huginn-3.5B** (`title:f75fffe554037a34`, abstract-only for the model
itself; the measurements are Think Shallow's, read-only via forward hooks):
`σ_eff = 1.000 ± 0.003`, never settling across 2,585 tokens on 7 task
categories, classified normalized-marginal, its answer-freezing not tracking
difficulty — **guess-freezing under Proposition 1(b)**. Its depth is unsafe
rather than merely inert: on single-token carry probes accuracy peaks at
`0.69` at `r=8` and falls to `0.00` for `r ≥ 32`, every input freezing onto
the same wrong token — collapse to a constant map.

A **label-free rank-16 LoRA** repair pulls deep states at `r ~ U[16,128]`
toward the frozen base's own shallow state at `r=8`. Digit copying, lost by
the base at `r ≥ 4`, reaches `1.00 ± 0.00` at `r=128` with input-dependent
answers (10/10 seeds); letter repetition `0.00 → 0.51 ± 0.13`. Conversion
never appears, and **the fixed-point term itself did not transfer to this
scale — only its latent-anchoring form did.**

**Three open 7B token-space reasoners** on one prompt bank, `n=40` per point:
DeepSeek-R1-Distill 7B `0.82 → 0.00` on chain-6 (destroyed by more of the
budget it needs), Mistral 7B `1.0 → 0.47` on chain-2 (degraded by thinking it
does not need), Qwen2.5 7B an inverse U on last-digit. The authors call this
a **shared failure shape rather than mechanism identity**, and that
qualification should be carried wherever the result is.

## The opposite-signed theory

*Expressive Power of Implicit Models* (`title:acc0cd457f5fd230`,
abstract-only, no benchmark numbers in the record) proves expressive power
grows with the number of test-time iterations, with solution quality
improving **and stabilising**. It reads as the contradiction of the above and
is not one: it reasons from the premise that the iteration reaches a fixed
point, and Think Shallow measures how often trained operators break that
premise. Proposition 1 is the seam — extra expressivity is harvestable only
where `R_t < μ`.

The architectures that make the framing available in the first place:
recurrent depth (Huginn), Penelope's five-layer localised recurrence
(`arxiv:2607.25915`, document) whose memory update
`M_t = M_{t−1} + 0.5·α_t·(candidate − M_{t−1})`, `α_t = 1 + 0.5 tanh(s_t)`,
is a textbook under-relaxation but is run for a fixed validation-chosen `K`
with no convergence claim, and MIND over Body — whose layer-level
iterate-to-convergence description the archive's own record flags as coming
from a third-party talk summary against an unreachable paper.

## What is missing

1. **Nobody has estimated `R_t` for an autoregressive chain.** The
   translation is available — `δ_t` as the shift in the answer distribution
   between consecutive probes, `μ` as the gap between the top two candidates.
   ParaTempo holds one half and C4/CVEE the other; nothing tests whether the
   decay is geometric or harmonic, which is the only thing separating
   Proposition 1(a) from 1(b).
2. **Non-normality has no autoregressive counterpart here.** No stopping rule
   in this archive distinguishes a transient from a trend.
3. **Why EqR and DEQ do not respond to the fixed-point objective is
   unexplained**, in the paper and in the archive.
