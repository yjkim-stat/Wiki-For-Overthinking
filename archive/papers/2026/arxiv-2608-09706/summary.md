<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection

- **Authors**: Aaron Haag, Altay Kacan, Bertram Fuchs, Oliver Lohse
- **Venue**: cs.CE
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09706>
- **PDF**: <https://arxiv.org/pdf/2608.09706v2>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Introduces verifier-free 'consensus selection' for text-to-CAD generation, picking among N compiled 3D CAD candidates the one that geometrically or topologically agrees most with the rest of the pool.

## Problem

LLMs can write parametric CAD programs from natural-language descriptions, but a single sample is often wrong; sampling multiple candidates only helps if a good one can be identified, and no ground-truth model is available at generation time, so existing systems rely on a separate (often vision-language) verifier to select among candidates.

## Contributions

- Introduces 3D CAD consensus selection: sample N parametric CAD programs, compile them to 3D models, and select the candidate that agrees most with the rest of the pool, without any external verifier.
- Defines and compares two agreement functions: geometric consensus (Chamfer-distance medoid) and topological consensus (Euler-characteristic majority).
- Shows geometric consensus improves all three geometric metrics over a state-of-the-art method's own vision-based verifier on the exact same candidate pools, while topological consensus matches the verifier on topology.
- Shows geometric consensus improves geometric accuracy (1-10% lower Chamfer distance) over random selection from the same pool across every tested LLM and prompt variant.

## Method

Given a natural-language CAD prompt, sample N parametric CAD programs independently from an LLM, compile each to a 3D model with a CAD compiler, and discard programs that fail to compile. Select the candidate with the lowest average distance to all other candidates in the pool (minimum Bayes risk decoding with a uniform prior over the sampled candidates). Two distance functions are studied: geometric consensus, the symmetric Chamfer distance between point clouds sampled from ICP-aligned meshes; and topological consensus, a 0/1 distance based on equality of Euler characteristic (mesh vertices - edges + faces), with ties broken by geometric distance. The method is training-free, needs only a compiler, and requires O(|V|^2) pairwise comparisons; it is applied both to fresh candidate pools (30 candidates per prompt, several LLMs) and to the exact candidate pools of an existing verifier-based method (EvoCAD) for a controlled comparison.

## Results

On the exact candidate pools of a verifier-based method (EvoCAD, n=197 for geometry, n=175 for topology): geometric consensus improves Chamfer distance (0.0610 vs. verifier's 0.0627), HDD (0.176 vs. 0.181), and IoU (0.703 vs. 0.695), all statistically significant (p<=0.022); topological consensus significantly improves CD and IoU over the verifier (p=0.003, p=0.035) and matches it on topology correctness (T_corr 84.9% vs. 84.8%, not significantly different, p=1.00). Across every tested LLM (Gemma 3 12B, gpt-oss-20b, Gemma 4, Gemini 3 Flash) and both CADPrompt variants (with/without explicit measurements), geometric consensus reduces Chamfer distance by 1-10% versus random selection from the same pool, with the largest relative gains (8-10%) for Gemma 3 12B and gpt-oss-20b and smaller gains (1-3%) for the stronger Gemini 3 Flash and Gemma 4. Scaling the number of sampled candidates N shows both consensus variants improve over random selection already at N=3 and saturate with little additional gain beyond N~9, while an oracle upper bound continues improving as N grows.

## Limitations

Consensus selection cannot help when all sampled candidates are identical, and it fails when the same error appears in most candidates, since that shared error becomes part of the consensus. It favors candidates near the center of the pool and may miss a high-quality outlier, which the authors identify as the main source of the remaining gap to an oracle upper bound (which keeps improving with more samples while consensus and random selection saturate by about N=9). Geometric consensus normalizes and ICP-aligns models before comparison, so it cannot detect absolute-dimension mismatches even when dimensions are specified in the prompt, and a global (whole-model) distance may fail to distinguish small local features. No statistically significant difference was found between topological consensus and the verifier baseline on topology correctness. Whether consensus generalizes to sequential refinements of a single program (rather than parallel independent candidates) is left open.

## Why it matters here

- **overthinking**: Tangential: matches only on the generic phrase 'test-time scaling'/'test-time compute.' The paper applies test-time scaling to text-to-CAD program generation by sampling N candidate programs and selecting among the compiled 3D models via geometric or topological agreement; it does not address LLM reasoning-length, chain-of-thought overthinking/underthinking, or when a reasoning model should stop or keep going.

## Entities

- **Concepts**: consensus/agreement as a verifier-free selection signal, minimum Bayes risk (MBR) decoding over parallel samples, coverage-vs-selection gap between candidate pool quality and what an agreement rule recovers
- **Methods**: 3D CAD consensus selection, minimum Bayes risk (MBR) decoding, Chamfer-distance geometric consensus, Euler-characteristic topological consensus
- **Datasets**: CADPrompt benchmark

Tags: `cad-generation`, `test-time-scaling`, `consensus-selection`, `verifier-free`, `minimum-bayes-risk`

## Abstract

Large language models can write parametric CAD programs from a natural-language description (text-to-CAD generation), but a single sample is often wrong. Increasing test-time compute by sampling multiple candidates only helps if a good candidate can be identified, yet no ground-truth model is available at generation time. Existing systems often require a separate verifier, such as a vision-language judge, to select among candidates. We investigate whether the candidate pool itself provides enough signal for effective selection and a verifier-free alternative. We introduce 3D CAD consensus selection, hereafter consensus selection: sample $N$ parametric CAD programs, compile them to 3D models, and return the candidate that agrees most with the rest of the pool. The method is training-free and compatible with existing CAD agents. We investigate geometric and topological notions of agreement, each of which improves its corresponding evaluation metric. On the exact candidate pools of a state-of-the-art CAD generation method, geometric consensus improves all three geometric metrics over the method's verifier, while topological consensus matches it on topology. Across every tested LLM and prompt variant, geometric consensus also improves geometric accuracy over random selection from the same pool, reducing Chamfer distance by $1-10\%$.

---

Record id: `arxiv:2608.09706`
