<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64256>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Measures a reasoning model's inference-time effort not by how many tokens it emits but by what fraction of them are still being revised in the network's late layers, and uses that fraction to pick which of many sampled generations to keep.

## Problem

Test-time compute scaling is usually quantified by generation length, but length correlates with accuracy inconsistently and often negatively — a long trace can signal overthinking rather than harder work. Confidence-based signals (log probability, entropy, perplexity, self-certainty) are the usual alternative, but they score the model's certainty about its output rather than the computation spent producing it. What is missing is a measure of reasoning effort grounded in the model's internal computation.

## Contributions

- Defines deep-thinking tokens via settling depth — the first layer at which the logit-lens distribution's Jensen-Shannon divergence from the final-layer distribution falls below a threshold — giving a per-token measure of how much depth-wise computation the model actually spent.
- Shows the deep-thinking ratio correlates with accuracy at mean r = 0.683 across 8 models and 4 benchmarks, beating self-certainty (0.605) and all other confidence baselines, while token length correlates at -0.594.
- Think@n, a test-time scaling strategy that selects the top-DTR half of sampled generations and rejects the rest from a 50-token prefix, matching or beating consensus@n at roughly half the inference cost.
- Documents that DTR is not comparable across reasoning-level configurations of the same model family, higher reasoning levels showing lower DTR at higher accuracy.

## Method

At each generation step t and each layer l, the intermediate hidden state is projected to vocabulary space through the shared unembedding matrix (logit lens): p_{t,l} = softmax(W_U h_{t,l}). The Jensen-Shannon divergence D_{t,l} between the layer-l distribution and the final-layer distribution measures how far the layer's prediction still is from what the model will actually emit. Taking the running minimum over layers, the settling depth c_t is the first layer at which that divergence drops below a fixed threshold g — the depth at which the token's prediction has effectively converged. A token counts as deep-thinking when it settles late, c_t >= ceil((1 - rho) L). The deep-thinking ratio DTR(S) of a sequence is the fraction of its tokens that settle in that late regime. Hyperparameters are held fixed across all experiments at g = 0.5 and rho = 0.85, so DTR needs no per-model tuning. Think@n applies this as a test-time scaling rule: sample n generations, compute DTR, keep the top eta fraction by DTR and take the consensus answer over those. Because settling depth is available per token, DTR can be estimated from a short prefix (50 tokens), so unpromising generations are aborted early rather than decoded to completion — that early rejection, not the selection itself, is where the cost saving comes from.

## Results

Evaluated on AIME 2024, AIME 2025, HMMT 2025 and GPQA-Diamond across eight model configurations (GPT-OSS-20B and GPT-OSS-120B at low/medium/high reasoning levels, DeepSeek-R1-70B, Qwen3-30B-Thinking). Mean Pearson correlation with accuracy: DTR 0.683, versus self-certainty 0.605, negative entropy 0.571, log probability 0.527, negative perplexity 0.219, and token length -0.594 — length is not merely a weak signal but a consistently inverted one, longer generations being less likely to be correct. Think@n with n = 48, eta = 50% and a 50-token prefix, on GPT-OSS-120B-medium: AIME25 94.7% versus 92.7% for consensus@n; AIME24 93.3% versus 92.7%; HMMT25 80.0%, tying consensus@n; at roughly 49% lower inference cost. Self-certainty@n at comparable cost reaches only 87.3% / 91.3% / 78.0%. On Qwen3-30B-Thinking, AIME25 rises from 86.7% (consensus@n) to 90.0% at about half the cost.

## Limitations

The paper's own appendix records the caveat that matters most: within the GPT-OSS family, lower reasoning-level configurations produce systematically *higher* DTR while scoring *lower* accuracy, so the correlation that holds within a fixed model and setting inverts across settings. DTR is therefore a within-run ranking signal, not a comparable measure of reasoning effort across models or across a model's own reasoning modes — which undercuts the framing of DTR as a general measure of 'reasoning effort'. The correlation is also not uniform: of 32 model-benchmark cells, three are negative or near-zero (Qwen3 on AIME24 r = -0.657, GPT-OSS-20B-medium on AIME24 r = -0.192, DeepSeek-R1-70B on AIME24 r = 0.430), and AIME24 accounts for all of them, suggesting a benchmark-specific failure the paper does not explain. There is no dedicated limitations section. Further gaps a reader should note: the method requires access to hidden states at every layer, so it cannot be applied to an API-served model; DTR is validated as a correlate of accuracy but no causal test shows late-layer revision is reasoning rather than, say, tokenization or formatting difficulty; g and rho are fixed but never ablated in the reported results; and Think@n still samples n = 48 generations, so it reduces the cost of test-time scaling rather than deciding whether to scale at all.

## Why it matters here

- **overthinking**: The topic's recurring difficulty is that reasoning length is the only cheap handle on test-time compute and it is a bad one; this paper supplies a concrete replacement and quantifies exactly how bad length is — mean Pearson r = -0.594 with accuracy across 8 models and 4 benchmarks, meaning that within a fixed model on a fixed benchmark, a longer trace is systematically the less accurate one. That is the strongest single number the group has for the claim that overthinking is real and not an artefact of harder questions taking longer. The deep-thinking ratio is a candidate signal for the group's own work: it is computed from hidden states the model already produces, needs no ground truth (unlike SuCo's sufficiency score, which conditions on the correct answer), and is available from a 50-token prefix, so it could in principle drive a stopping decision rather than only a post-hoc selection — though this paper only uses it to rank completed or aborted samples, never to halt an ongoing trace. The finding to carry forward with care is the negative one: DTR rises when a model is set to a *lower* reasoning level and accuracy falls, so DTR measures per-token depth of computation, not total effort, and using it to compare 'how hard did this model think' across models or modes would invert the answer. That distinction — depth per token versus tokens spent — is a useful axis for the topic in its own right, since it separates a model that thinks hard briefly from one that thinks shallowly at length.

## Entities

- **Concepts**: Deep-Thinking Tokens, [Reasoning Effort](../../../../wiki/concepts/reasoning-effort.md), Settling Depth, [Overthinking](../../../../wiki/concepts/overthinking.md), [Test-Time Compute Scaling](../../../../wiki/concepts/test-time-compute-scaling.md), Self-Consistency, Logit Lens, Reasoning Length as Proxy
- **Methods**: deep-thinking ratio (DTR), settling depth, logit lens, Jensen-Shannon divergence over layer-wise predictive distributions, Think@n, self-consistency / consensus@n, [self-certainty](../../../../wiki/methods/self-certainty.md), prefix-based early rejection
- **Datasets**: [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [HMMT 2025](../../../../wiki/datasets/hmmt-2025.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `overthinking`, `test-time-compute`, `reasoning-effort`, `interpretability`, `logit-lens`, `self-consistency`, `chain-of-thought`, `inference-efficiency`, `llm`

---

Record id: `title:bcd9cf99a0e84a2d`
