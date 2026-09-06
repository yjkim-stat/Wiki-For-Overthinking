<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders

- **Authors**: Bo Cheng, Qiaolin Lu, Yi Chang, Yuan Wu
- **Venue**: preprint
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: overthinking

## In one line

Trains Top-K sparse autoencoders on the residual stream of DeepSeek-R1-Distill-Qwen-7B to contrast the internal feature dynamics of explicit chain-of-thought (Thinking) against direct answer generation (NoThinking), finding Thinking relies on a sparse, high-intensity, difficulty-invariant feature regime while NoThinking uses a diffuse, difficulty-adaptive one, and that causally suppressing Thinking's dominant features degrades formatting and triggers compensatory, less informative verbosity rather than a clean shortening of the trace.

## Problem

The structural distinction between the internal states governing explicit chain-of-thought reasoning (Thinking mode) and direct answer generation (NoThinking mode) is poorly understood at the mechanistic level, and it remains unresolved whether the thinking process constitutes a genuinely distinct computational regime or is merely a prolonged extension of standard next-token generation.

## Contributions

- Trains separate Top-K sparse autoencoders on residual-stream activations of DeepSeek-R1-Distill-Qwen-7B for Thinking and NoThinking inference modes, establishing a comparative framework to contrast their latent feature dynamics on math problems of varying difficulty.
- Identifies a mechanistic divergence: Thinking mode operates via a sparse, high-intensity activation regime driving verbal deduction that is stable and invariant to problem complexity, whereas NoThinking mode uses a diffuse, adaptive pattern that recruits a broader, difficulty-dependent coalition of features for symbolic/pattern-matching manipulation.
- Performs causal suppression interventions on the top-3 highest-Total-Activation-Volume features to establish their functional necessity, revealing coupling between reasoning and syntactic/formatting structure, compensatory over-generation under disruption, and fragile coordination among specialized features.

## Method

This is a mechanistic-interpretability study, not a proposed practical inference-time acceleration or overthinking-mitigation method, though its causal-validation step does perform a genuine inference-time intervention.

SAE training: Top-K Sparse Autoencoders (2^16 = 65,536 latent feature dictionary, C) are trained separately for two inference modes on activations extracted from the residual stream of the 13th layer of DeepSeek-R1-Distill-Qwen-7B, run over the DeepMath-103K corpus (103,000 math problems from Math StackExchange). Thinking mode activations are collected while the model generates its full chain-of-thought before the final answer (sequences of length 1,024, 108M tokens total); NoThinking mode activations are collected while the decoding process is constrained to keep the thinking box empty, forcing the model to answer directly (65M tokens total). Each SAE encodes an activation vector x via z = TopK(W_enc x + b_enc), retaining only the k largest-magnitude latents (k annealed from 200 down to 20 over the first 50% of training), and decodes via x̂ = W_dec z + b_dec, trained to minimize pure reconstruction loss (no L1 penalty needed since sparsity is enforced structurally by the TopK operator). Feature importance is quantified via Total Activation Volume (TAV): the summed activation magnitude of each feature across a validation corpus of N tokens.

Causal intervention (the inference-time component): the top-3 Thinking-mode features by TAV on easy problems (F4416, F8893, F28634) are targeted with a dynamic suppression hook installed at the 13th layer, applied only to tokens generated inside the thinking block. For target feature i and suppression strength α ∈ {0.1, 0.3, 0.5, 1.0}, the modified latent activation is ẑ_i(t) = (1-α)·z_i(t) at each decoding step t, leaving all other features and layers untouched; effects are measured via density-based metrics normalized per 1,000 generated tokens (metacognitive/uncertainty word density, LaTeX density, boxed-answer retention, output length, lexical diversity via Distinct-1).

Where it intervenes: the residual stream at layer 13, restricted to 3 specific SAE latent-feature directions (of 65,536), reconstructed and modified via the trained Top-K SAE's encoder/decoder; applied only to tokens generated inside the `<think>...</think>` block.
What quantity decides the intervention: a fixed, hand-set multiplicative suppression coefficient α, uniform across all tokens and contexts; which 3 features to target is decided a priori and offline by Total Activation Volume ranking on a validation corpus, not adaptively at inference time.
When it fires: at every decoding step while the model is generating inside the thinking block, for whichever of the 3 chosen features is targeted in a given experimental run.
What it costs: not reported. The paper gives no inference-time latency, token-count, or throughput measurement for running the suppression hook (or for running the SAE encoder online in general); the only quantified costs are the SAE training details (Adam, lr=1e-3, β1=0.9, β2=0.999, batch size 1,024 for Thinking mode / 128 for NoThinking mode, dynamic sparsity annealing over the first half of one epoch, 3-4 epochs total), which are one-time, offline interpretability-analysis costs rather than something paid per deployed inference call.

## Results

Figure 1 (activation statistics for top-20 TAV features): Thinking mode has mean activation ~9.0 across all three difficulty levels, but maximum activation consistently ~75.0 with high standard deviation ~19.0 (sparse, high-intensity regime); NoThinking mode has a higher mean (~11.7), lower maximum (~60.0 stabilizing), and lower standard deviation (~17.5), indicating a more diffuse, uniform activation pattern. Figure 3 / Table 1 (feature source distribution, top-100 highest-activation tokens): in Thinking mode, the single dominant feature F4416 accounts for 82.0% of top-100 tokens at easy difficulty, rising to 96.0% (medium) and 100.0% (hard); in NoThinking mode, the dominant feature F10770 starts at only 37.0% (easy) and also converges to 100.0% at hard, but from a more distributed starting point (four features contributing at easy level vs. Thinking's near-immediate single-feature dominance). Table 2 (token category distribution, % of tokens): in Thinking mode, word-token frequency rises from 28.2% (easy) to 37.7% (hard) while number-token frequency falls from 17.0% to 8.0%; NoThinking mirrors the pattern (word 21.7%->36.1%, number 16.0%->5.9%) but with markedly higher math-symbol usage overall (22.3% at easy vs. Thinking's 15.6%). Table 4 (causal suppression effects, relative change per 1,000 tokens from baseline): suppressing F28634 causes LaTeX density -40.28, boxed-answer retention falling to 0%, output length +454%, and lexical diversity (Distinct-1) -63%, alongside metacognitive density +34.17; suppressing F4416 causes LaTeX density -35.22, output length +410%, lexical diversity -37%, and metacognitive density -19.38 (a decrease, opposite in sign to F28634's effect); suppressing F8893 causes LaTeX density -29.54, output length +107%, lexical diversity -42%, metacognitive density -4.33. Across all three features, boxed-answer retention collapses toward 0% and LaTeX density drops sharply and consistently, while the direction of the metacognitive-density shift differs by feature, evidencing divergent internal roles despite a common structural failure mode.

## Limitations

The paper has no dedicated Limitations section. Stated caveats appear only implicitly: the study is restricted to a single 7B model (DeepSeek-R1-Distill-Qwen-7B) and a single training corpus of math word problems (DeepMath-103K), and the SAE is trained on one intermediate layer (layer 13) chosen as "a representative intermediate layer" without testing other layers.

Not stated, and worth noticing: no task accuracy (correctness of the final answer) is reported anywhere in the paper, either for the baseline Thinking/NoThinking modes or after feature suppression — every result is a density-based generation metric (LaTeX density, metacognitive/uncertainty word density, output length, lexical diversity, boxed-answer retention as a binary formatting indicator, not a correctness check). This means the paper's causal claims are about output structure and verbosity, not about whether the identified features are actually load-bearing for solving problems correctly. The three suppressed features (F4416, F28634, F8893) were selected purely by Total Activation Volume within Thinking mode; the paper does not test whether suppressing NoThinking's dominant feature (F10770) produces analogous or different effects, so the asymmetric causal analysis (Thinking-only) limits how much can be concluded about the two modes symmetrically. The suppression hook is applied only during intervention experiments as an interpretability probe; the paper never measures or discusses its computational cost or latency at inference time.

## Why it matters here

- **overthinking**: Gives a mechanistic account of why explicit Thinking mode produces long, verbose traces regardless of problem difficulty: Thinking's dominant feature (F4416) maintains near-identical peak activation intensity (75.2/72.8/73.9 across easy/medium/hard) and increasingly dominates the top-100 activated tokens as difficulty rises (82%->100%), showing the reasoning pathway is a stable, complexity-invariant computational regime rather than one that scales its intensity with need. Causally, suppressing this dominant feature does not shorten generation — it triggers compensatory over-generation (+454% output length, more metacognitive markers like "Wait"/"Let me think", -63% lexical diversity) — direct evidence that naively intervening on a single internal reasoning feature to curb overthinking can backfire into more, not less, low-information verbosity.

## Entities

- **Concepts**: Sparse Autoencoders (SAEs), Top-K sparse autoencoder, Total Activation Volume (TAV), Thinking vs NoThinking inference modes, causal feature suppression, feature source distribution, token category taxonomy, compensatory sequence extension, reasoning-syntax coupling
- **Methods**: Top-K Sparse Autoencoders, Total Activation Volume feature ranking, dynamic suppression hook / causal intervention, token category taxonomy, activation heatmap analysis
- **Datasets**: DeepMath-103K, [AMC23](../../../../wiki/datasets/amc23.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md)

Tags: `sparse autoencoders`, `mechanistic interpretability`, `chain-of-thought`, `thinking vs nothinking`, `feature suppression`, `causal intervention`, `reasoning mechanisms`, `DeepSeek-R1-Distill`

## Abstract

While Large Language Models (LLMs) employing Chain-of-Thought (CoT) exhibit superior reasoning capabilities, the neural mechanisms distinguishing this explicit Thinking mode from direct answer generation (NoThinking mode) remain poorly understood. To deconstruct this cognitive process, we apply Top-K Sparse Autoencoders (SAEs) to the intermediate representations of DeepSeek-R1-Distill-Qwen-7B and examine the model's divergent behaviors across math-solving tasks of three distinct difficulty levels. Observationally, we identify a clear distinction in how the model functions under two reasoning modes: Thinking mode relies on sparse and high-intensity feature activations driving verbal deduction independent of problem complexity, whereas NoThinking mode exhibits an adaptive and diffuse pattern prioritizing symbolic manipulation. Causally, suppressing the three most active sparse features by Total Activation Volume reveals three principles: (i) reasoning and syntactic structure are tightly coupled, as interventions consistently degrade LaTeX and boxed-solution formatting; (ii) Thinking responds to disruption with compensatory over-generation marked by increased metacognitive cues and repetitive, low-information continuations; and (iii) coherent CoT behavior depends on a fragile coordination among specialized features, yielding distinct failure modes under perturbation but a consistently impaired output structure.

---

Record id: `local:4c4d1944c8091d55`
