<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficient Reasoning with Hidden Thinking

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/65014>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.

## Problem

Chain-of-thought reasoning in multimodal large language models costs hundreds of generated tokens per answer, most of them redundant. Compressing the chain risks discarding the reasoning itself, and there was no account of how much information a compression can drop before capability breaks. The open question is whether reasoning can be carried in a compact latent representation rather than in text, and whether what was compressed can still be recovered and inspected.

## Contributions

- A CoT compression scheme in which an entire reasoning stage becomes one latent thinking token, cutting generation to roughly 6% of the baseline's tokens on several benchmarks.
- Progressive encoding training that replaces textual stages with thinking tokens incrementally, plus a recovering stage for the transitions between them.
- An adaptive interpreter (Heima Decoder) that reconstructs variable-length textual reasoning from the encoder's hidden states without access to the image, giving evidence that visual reasoning content survives the compression.
- An information-theoretic account quantifying compression-related information loss and arguing that reasoning capability is retained when the relevant mutual information is preserved.

## Method

Heima has two parts. The Heima Encoder is a multimodal LLM (Llama-3.2-11B-Vision-Instruct) fine-tuned so that each stage of a structured CoT collapses into one special token -- <Thinking_of_Summary>, <Thinking_of_Caption>, <Thinking_of_Reasoning> -- from which it then produces the final answer. Training is progressive: the model first learns on full textual CoTs by next-token prediction, then stages are replaced by their thinking tokens one at a time until it trains entirely on the compressed form, followed by a recovering stage that tunes the transitions between encoded stages. The Heima Decoder is a separate, standard LLM (Llama-3.1-8B-Instruct) trained per CoT stage to reconstruct the textual reasoning from the frozen encoder's hidden states, given the query and an explanatory prompt but no image; the reconstruction is variable-length, so a single token can be unpacked into as much prose as is wanted. The paper frames the compression information-theoretically, arguing capability survives as long as the mutual information that matters is preserved.

## Results

Trained on LLaVA-CoT-100k (100k image-QA pairs with three-stage reasoning); evaluated zero-shot on MMStar, MMBench V1.1, MMVet, MathVista, AI2D and HallusionBench. Token counts against the LLaVA-CoT baseline: AI2D 12.7 vs 178.5, MMBench 12.9 vs 154.8, MathVista 13.8 vs 216.3 -- around 6% of the original generation on those sets. Accuracy: average 58.0% for Heima vs 61.1% for LLaVA-CoT, i.e. a 3.1-point drop, though Heima is above the Llama-3.2-11B-Vision-Instruct base at 52.1% and beats LLaVA-CoT on MMBench (72.8% vs 70.7%). Decoder reconstruction is scored with BLEU-4, METEOR, ROUGE-L and BERTScore; the summary stage reconstructs best, caption and reasoning stages worse. Note the tension with the abstract's claim of 'maintaining or even achieving better zero-shot accuracy': the reported average is 3.1 points below the CoT baseline, and the 'better' holds on MMBench rather than on the mean.

## Limitations

Stated: no evaluation with larger encoder models; the decoder is fixed at 8B; the approach needs data with structured multi-stage CoT formatting; reconstruction quality is uneven, with caption and reasoning stages worse than summary; degradation appears on specific reasoning categories (e.g. logical reasoning within MathVista). A reader should also notice: (1) the headline 'maintaining or even achieving better accuracy' is not supported by the average, which is 58.0% against 61.1% -- a real 3.1-point cost for the ~94% token reduction; (2) the compression is per reasoning stage, so the compression ratio is fixed by the CoT schema rather than adapted to problem difficulty -- an easy and a hard item both get three tokens; (3) the setting is multimodal VQA-style benchmarks, not the long-form math reasoning where the overthinking literature usually measures; (4) the decoder is an extra 8B model, so interpretability is bought with inference cost that the token counts do not include.

## Why it matters here

- **overthinking**: A latent-space answer to the same problem the topic's text-compression methods attack, and it pushes the compression axis about as far as it goes: roughly 6% of the baseline's generated tokens, one token per reasoning stage. Its value to the topic is that it prices the extreme honestly -- 3.1 accuracy points on the six-benchmark average -- which is a data point on the accuracy/length curve rather than another claim of a free lunch, and worth reading against the paper's own abstract, which says accuracy is maintained. Second, the Heima Decoder addresses a question the rest of the topic tends to leave open: if a model stops emitting its reasoning, what can anyone still check? Reconstructing readable reasoning from the hidden states -- including visual detail, without the image -- is evidence that shortening the visible trace need not mean losing the trace. The limit for this topic is that the compression is fixed per stage rather than adaptive to difficulty, so Heima says nothing about a model deciding to think longer on a harder problem.

## Entities

- **Concepts**: [Chain-of-Thought Compression](../../../../wiki/concepts/chain-of-thought-compression.md), [Latent Reasoning](../../../../wiki/concepts/latent-reasoning.md), Hidden Thinking Tokens, Progressive Encoding, Reasoning Reconstruction / Interpretability, Mutual Information Preservation, Multimodal Reasoning
- **Methods**: Heima Encoder, Heima Decoder, progressive encoding, latent thinking tokens, Llama-3.2-11B-Vision-Instruct, Llama-3.1-8B-Instruct, LLaVA-CoT
- **Datasets**: LLaVA-CoT-100k, [MMStar](../../../../wiki/datasets/mmstar.md), MMBench V1.1, MMVet, [MathVista](../../../../wiki/datasets/mathvista.md), [AI2D](../../../../wiki/datasets/ai2d.md), HallusionBench

Tags: `overthinking`, `efficient reasoning`, `cot compression`, `latent reasoning`, `multimodal`, `thinking tokens`, `interpretability`

---

Record id: `title:725397e20ebf1509`
