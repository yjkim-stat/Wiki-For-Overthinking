# GPT-5-mini

<!-- auto:begin -->

A small frontier reasoning model appearing across 3 sources as a monitor, a judge and an extraction target. Its most informative archived appearance is as a monitoring comparison in a reasoning-summary observability study, where the source notes the comparison mixes monitoring with task solving because the model can attempt the question itself -- a confound worth carrying whenever a capable model is used as a monitor. It also appears as a judge in medical rubric training.

- **Kind**: model
- **Also called**: GPT-5 Mini, GPT-5-mini
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [annotation agreement](../concepts/annotation-agreement.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Claude Haiku 4.5](claude-haiku-4-5.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [consensus](../concepts/consensus.md), [DPO](../methods/dpo.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4.1](gpt-4-1.md), [GPT-4o-mini](gpt-4o-mini.md), [GPT-5](gpt-5.md), [gpt-5.6-luna](gpt-5-6-luna.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [GPT-5.6 Terra](gpt-5-6-terra.md), [gpt-oss-120b](gpt-oss-120b.md), [gpt-oss-20b](gpt-oss-20b.md), [GRPO](../methods/grpo.md), [human evaluation](../methods/human-evaluation.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [IFEval](../datasets/ifeval.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logistic regression](../methods/logistic-regression.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [o4-mini](o4-mini.md), [Omni-MATH](../datasets/omni-math.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [position bias](../concepts/position-bias.md), [prompt injection](../concepts/prompt-injection.md), [PubMedQA](../datasets/pubmedqa.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [Qwen3-8B](qwen3-8b.md), [reward hacking](../concepts/reward-hacking.md), [selective prediction](../concepts/selective-prediction.md), [self-correction](../concepts/self-correction.md), [TF-IDF](../methods/tf-idf.md), [verbosity](../concepts/verbosity.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) — Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.
- [ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering](../../archive/papers/2026/arxiv-2608-10996/summary.md) — Trains open-ended medical question answering by scoring each response against rubric criteria that three frontier models independently agreed on, grading each criterion as correct, missing or wrong rather than yes/no, and recovering a gradient in groups where every response ties by judging the responses pairwise in both orders.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
