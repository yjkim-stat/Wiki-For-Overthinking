<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos

- **Authors**: Yang Yao, Xuan Tong, Ruofan Wang, Yixu Wang, Lujundong Li, Liang Liu, Yan Teng, Yingchun Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.findings-acl.408/>
- **PDF**: <https://aclanthology.org/2025.findings-acl.408.pdf>
- **DOI**: 10.18653/v1/2025.findings-acl.408
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.

## Problem

Large reasoning models are assumed safer than standard LLMs because their deliberative reasoning helps them avoid harmful outputs, but no prior work investigates whether the reasoning process itself introduces new, LRM-specific jailbreak vulnerabilities distinct from those exploited against non-reasoning LLMs -- and existing black-box jailbreak methods, effective against weaker-reasoning LLMs, become far less effective against the latest reasoning-capable models.

## Contributions

- the first jailbreak attack framework specifically targeting large reasoning models' distinctive reasoning process rather than treating them as ordinary black-box LLMs
- the Chaos Machine, a component amalgamating diverse reversible one-to-one prompt mappings (character/word/sentence granularity) into iteratively composable chaos chains that project attack prompts into low-sample, mismatched-generalization spaces
- empirical demonstration that iterative reasoning-chain length has an inverted-U relationship with attack success (peaking around chain length 2-3), and that the resulting Mousetrap framework achieves 85%+ attack success rates with high confidence across mainstream LRMs and diverse safety benchmarks, including against models specifically noted for strong safety alignment (Claude-3.5-Sonnet)
- the 'reasoning inertia'/'reasoning mask' hypothesis: once an LRM begins a multi-step reasoning chain, it tends to follow it to completion rather than re-assessing safety mid-chain, because the harmful nature of the eventual instruction is not discernible until the final reconstruction step

## Method

Defines a taxonomy of 'chaos mappings' -- reversible, one-to-one prompt transformations at character (ciphers), word (substitution), or sentence (reordering) granularity -- and builds a Chaos Machine that, given a toxic query, applies a randomly selected chaos policy (an en-chaos/de-chaos operation pair) to produce a rewritten (encoded) query plus the sequence of decoding steps needed to reconstruct the original. The Chaos Machine is implemented either via a small library of hand-selected chaos-mapping functions (used as the default, cost-efficient but less diverse) or via a fine-tuned gpt-4o-mini (SFT'd on 120 manually curated examples, more diverse mappings but expensive), with a Checker module (a copy of the attacked model) verifying that a generated mapping is comprehensible and regenerating it if not. Iterative reasoning chains apply the Chaos Machine n times in sequence (chain length n), compounding transformations into a single nonlinear mapping that is harder for the target model to recognize as harmful than any individual mapping alone. The full Mousetrap framework wraps this iterative chaos chain in a 'villain-perspective' role-play prompt (inspired by Agatha Christie's The Mousetrap, where the murderer poses as the detective) instructing the target LRM to reconstruct the original toxic query step-by-step and then respond to it in character, exploiting competing objectives (roleplay instruction vs. safety) alongside the mismatched-generalization effect of the chaos chain. Evaluated with a GPT-4o-based judge (1-5 harm scale, score>4 = successful) under strict '3/3' (all of 3 repeated attacks succeed) and looser '2/3' success criteria, on newly constructed toxic datasets (TrotterStrong, and its filtered, more-toxic subsets TrotterAdvanced and TrotterUltimate) as well as on established safety benchmarks (AdvBench, StrongREJECT, HarmBench, JailbreakBench, MaliciousInstruct, JailBenchSeed, FigStep, HADES, RedTeam-2K, MM-SafetyBench subsets), against o1-mini, o1, o3-mini, Claude-3.5/3.7-Sonnet, Gemini-2.0-Thinking/2.5-Pro, DeepSeek-R1, QwQ-Plus and Grok-3.

## Results

On TrotterAdvanced attacking o1-mini, average success frequency (ASF, out of 10 repeated attacks) rises from 1.38 (chain length 1) to a peak of 6.27 at chain length 3, then declines to 3.23 at chain length 5 -- confirming the hypothesized inverted-U relationship between chain length and attack effectiveness (longer chains increase attack ability via more thorough disguising, but eventually degrade the target's own reconstruction accuracy, undermining the attack). On the more toxic TrotterUltimate, full Mousetrap (chaos chain + role-play framing) reaches ASF 7 at chain length 2-3, clearly outperforming both an ablation using only a single fixed chaos mapping per iteration and an ablation using explicit chain-of-thought output (which more readily triggers the target's safety alerts). Against o1-mini/Claude-3.5-Sonnet/Gemini-2.0-Thinking(H) with chain length at most 3 (strict 3/3 success criterion) on the TrotterStrong dataset, Mousetrap achieves ASR of 96%, 86%, and 98% respectively; against the safer Gemini-2.0-Thinking(M&H) setting, ASR still reaches 70%. Across newer/more advanced models (o1, o3-mini, Claude-3.7-Sonnet, Gemini-2.5-Pro, DeepSeek-R1, QwQ-Plus, Grok-3), nearly all are 'completely jailbroken' (near-100% combined Success@1/2/3) with chain lengths up to 3. Against Claude-3.5-Sonnet (chosen for its strong safety reputation) across 10 standard safety benchmarks, Mousetrap achieves ASR of 87.5% (AdvBench), 86.58% (StrongREJECT), and 93.13% (HarmBench), and remains highly effective (mostly >50% combined success, several benchmarks near 90-100%) across JailbreakBench, MaliciousInstruct, JailBenchSeed, FigStep, HADES, RedTeam-2K, and multiple MM-SafetyBench subsets. A control experiment testing the isolated chaos mappings at chain length 1 (removing the iterative/role-play components) shows performance across all 8 mapping types is nearly identical and has a low upper bound, indicating the Chaos Machine abstraction successfully generalizes away the specific-mapping-choice effect and that iteration (not mapping choice) is what drives effectiveness. Testing an alternative role-play framing ('grandma trap' instead of the villain/Mousetrap framing) roughly halves ASR, indicating framing choice matters substantially. Directly querying PTQs without any chaos transformation yields ASR of zero on all tested targets, confirming the reasoning models otherwise refuse the underlying harmful requests reliably.

## Limitations

No separate Limitations section is present in the retrieved pages of this paper; the Discussion section explicitly frames its account of the mechanism (mismatched generalization and competing objectives, plus the newly proposed 'reasoning mask'/reasoning-inertia concept) as plausible but not provable given that black-box models are inaccessible for deterministic mechanistic analysis, stating the authors 'cannot assert with absolute certainty which principle has exerted a predominant... influence' and flagging this as an open direction for future research.

## Why it matters here

- **overthinking**: Relevant primarily through its 'reasoning inertia' concept: the finding that once an LRM begins a multi-step reasoning chain it tends to follow it to completion 'by inertia,' failing to pause and re-evaluate whether it should stop, is a safety-domain instance of the same underlying phenomenon overthinking mitigation targets in the accuracy domain -- a model that keeps extending or committing to an established reasoning trajectory past the point where it should reconsider or halt. The inverted-U relationship between reasoning-chain length and attack effectiveness (more steps help up to a point, then hurt as the target's own reconstruction accuracy degrades) is also structurally similar to the accuracy-vs-length curves central to the overthinking literature, here measured on attack success rather than task accuracy.

## Entities

- **Concepts**: Chaos Machine (reversible one-to-one prompt mapping generator), reasoning inertia (LRM inability to halt/reassess mid-chain), reasoning mask (inability to foresee downstream harm of a reconstruction task), chain-length / attack-effectiveness trade-off (inverted-U)
- **Methods**: Chaos Machine (iterative reversible prompt mapping), role-play / competing-objectives framing (Mousetrap), GPT-4o-based harm judge (1-5 scale)
- **Datasets**: TrotterStrong (new), TrotterAdvanced (new), TrotterUltimate (new), [AdvBench](../../../../wiki/datasets/advbench.md), [StrongREJECT](../../../../wiki/datasets/strongreject.md), [HarmBench](../../../../wiki/datasets/harmbench.md), [JailbreakBench](../../../../wiki/datasets/jailbreakbench.md), MaliciousInstruct, JailBenchSeed, FigStep, HADES, RedTeam-2K, MM-SafetyBench (subsets)

Tags: `jailbreak`, `safety`, `large-reasoning-models`, `reasoning-inertia`, `iterative-reasoning`

## Abstract

Large Reasoning Models (LRMs) have significantly advanced beyond traditional Large Language Models (LLMs) with their exceptional logical reasoning capabilities, yet these improvements introduce heightened safety risks. When subjected to jailbreak attacks, their ability to generate more targeted and organized content can lead to greater harm. Although some studies claim that reasoning enables safer LRMs against existing LLM attacks, they overlook the inherent flaws within the reasoning process itself. To address this gap, we propose the first jailbreak attack targeting LRMs, exploiting their unique vulnerabilities stemming from the advanced reasoning capabilities. Specifically, we introduce a Chaos Machine, a novel component to transform attack prompts with diverse one-to-one mappings. The chaos mappings iteratively generated by the machine are embedded into the reasoning chain, which strengthens the variability and complexity and also promotes a more robust attack. Based on this, we construct the Mousetrap framework, which makes attacks projected into nonlinear-like low sample spaces with mismatched generalization enhanced. Also, due to the more competing objectives, LRMs gradually maintain the inertia of unpredictable iterative reasoning and fall into our trap. Success rates of the Mousetrap attacking o1-mini, Claude-Sonnet and Gemini-Thinking are as high as 96%, 86% and 98% respectively on our toxic dataset Trotter. On benchmarks such as AdvBench, StrongREJECT, and HarmBench, attacking Claude-Sonnet, well-known for its safety, Mousetrap can astonishingly achieve success rates of 87.5%, 86.58% and 93.13% respectively. Attention: This paper contains inappropriate, offensive and harmful content.

---

Record id: `doi:10.18653/v1/2025.findings-acl.408`
