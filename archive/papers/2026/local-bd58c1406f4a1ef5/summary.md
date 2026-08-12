<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Length Generalization Bounds for Transformers

- **Authors**: Andy Yang, Pascal Bergsträßer, Georg Zetzsche, David Chiang, Anthony W. Lin
- **Venue**: ICML
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: reasoning-training

## In one line

Proves that no computable length-generalization bound exists for transformers of depth two or beyond, and gives a matching exponential bound for the positive fragment that corresponds to fixed-precision transformers.

## Problem

Length generalization is making correct predictions on inputs of any length after training on bounded-length data, and it matters because compute and data limit the lengths seen in training while long contexts and long chains of thought are exactly what deployment needs. To guarantee it one needs a computable bound N such that training on strings up to length N suffices for all longer strings. Whether such a bound is computable for transformers was open; a partial positive answer existed for one layer and, with restrictions, two.

## Contributions

- A complete answer to the open problem of computable length-generalization bounds for C-RASP and hence for transformers
- The non-existence result at depth two and beyond, via a reduction from Hilbert's tenth problem to emptiness of C-RASP-definable languages
- The consequence that lengths required for length generalization grow faster than any computable function
- A computable exponential bound for the positive fragment C-RASP+, shown equivalent to fixed-precision transformers via unary temporal logic
- Optimality proofs for those bounds

## Method

The analysis works through C-RASP, a programming language depth-preservingly equivalent to transformers, and uses the framework of non-asymptotic length generalization — a computable N such that a learner given all examples up to length N classifies every longer string correctly. That framework deliberately abstracts away gradient dynamics and assumes the best case of access to all examples up to a length and perfect optimization on them, so a negative result under those favourable conditions applies a fortiori to SGD on limited data. The impossibility is proved by showing non-asymptotic length generalization is equivalent to decidability of language equivalence, which for C-RASP-definable languages reduces to emptiness, shown undecidable by reduction from Hilbert's tenth problem. The positive fragment C-RASP+ is shown equivalent to unary temporal logic with the strict past operator, and hence to (1,1)-precision transformers, which yields the exponential bound.

## Results

There is no terminating algorithm for perfectly learning a C-RASP program even at depth two, so no computable length-generalization bound exists for transformers of depth two or beyond — the lengths needed must grow faster than any computable function. For the positive fragment C-RASP+, expressively equivalent to fixed-precision transformers, training on strings of length exponential in the size of the program is sufficient and in the worst case necessary, and the bounds are proved optimal. The paper notes empirical context: models from 50M to 3B parameters trained on 15-digit addition could not add 20 digits, and training on 30 digits allowed generalization to 60 while extra data past a threshold did not help.

## Limitations

The negative result concerns exact learning of a worst-case program, so it does not say a particular task cannot length-generalize — only that no algorithm computes a bound valid for all of them. The favourable-conditions framing cuts the other way too: the model is idealized, with access to all examples up to a length and perfect optimization, so it says nothing about which practical setups succeed. The positive bound is exponential, hence not a practical training prescription. C-RASP and fixed-precision transformers are formal proxies whose correspondence to deployed softmax transformers is exact only under the stated precision restrictions.

## Why it matters here

- **reasoning-training**: A hard negative where this topic has mostly collected positive constructions. If no computable bound exists past depth two, then there is no procedure that tells you how long the training problems must be for reasoning to transfer to longer ones — the question is not merely open, it is undecidable in general. That reframes the field's empirical length-generalization results as facts about particular tasks rather than steps toward a general guarantee, and it explains why more data past a threshold stops helping, which the paper cites from the addition literature and the archive has met in its own scaling discussions. The positive half is the practically useful part: restricting to fixed precision restores computability at exponential cost, which makes precision a lever on learnability rather than an implementation detail — the same variable the archive's expressivity entries found tightens the no-CoT bound from TC^0 to AC^0.

## Entities

- **Concepts**: [length generalization](../../../../wiki/concepts/length-generalization.md), [generalization](../../../../wiki/concepts/generalization.md), computability, [expressivity](../../../../wiki/concepts/expressivity.md), [out-of-distribution generalization](../../../../wiki/concepts/out-of-distribution-generalization.md), [finite precision](../../../../wiki/concepts/finite-precision.md), exact learning, [scaling laws](../../../../wiki/concepts/scaling-laws.md)
- **Methods**: C-RASP, non-asymptotic length generalization, reduction from Hilbert's tenth problem, unary temporal logic
- **Datasets**: _none recorded_

Tags: `length generalization`, `computability`, `c-rasp`, `undecidability`, `theory`

## Abstract

Length generalization is a key property of a learning algorithm that enables it to make correct predictions on inputs of any length, given finite training data. To provide such a guarantee, one needs to be able to compute a length generalization bound, beyond which the model is guaranteed to generalize. This paper concerns the open problem of the computability of such generalization bounds for C-RASP, a class of languages which is closely linked to transformers. A positive partial result was recently shown by Chen et al. for C-RASP with only one layer and, under some restrictions, also with two layers. We provide complete answers to the above open problem. Our main result is the non-existence of computable length generalization bounds for C-RASP (already with two layers) and hence for transformers. To complement this, we provide a computable bound for the positive fragment of C-RASP, which we show equivalent to fixed-precision transformers. For both positive C-RASP and fixed-precision transformers, we show that the length complexity is exponential, and prove optimality of the bounds.

---

Record id: `local:bd58c1406f4a1ef5`
