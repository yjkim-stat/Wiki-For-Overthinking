<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents

- **Authors**: Chiwei Zhu, Benfeng Xu, Mingxuan Du, Shaohan Wang, Xiaorui Wang, Zhendong Mao, Yongdong Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.288/>
- **PDF**: <https://aclanthology.org/2026.acl-long.288.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.288
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

FS-Researcher is a dual-agent (Context Builder / Report Writer) deep-research framework that scales test-time compute beyond a single context window by persisting evidence and task state in an external file-system workspace instead of the model's context, achieving state-of-the-art report quality on two open-ended benchmarks and outperforming official agent harnesses on an answer-verifiable search benchmark.

## Problem

Deep-research tasks require an LLM agent to browse and synthesize hundreds of webpages into long (10K+ token) reports, but the model's context window is inherently limited, so as trajectories grow, thoughts, observations and report drafts compete for the same fixed token budget, forcing premature synthesis, incomplete source coverage and brittle behavior -- and existing fixes (compressing tool observations into distilled summaries) only prolong trajectories while remaining lossy and still bounded by the hard context limit.

## Contributions

- FS-Researcher, a dual-agent, file-system-based framework that decouples evidence accumulation (Context Builder) from report composition (Report Writer), letting agent state exceed the model's context window via a persistent, structured external workspace
- state-of-the-art report quality on two open-ended deep-research benchmarks (DeepResearch Bench, DeepConsult) across multiple backbone models, plus outperformance of official proprietary agent harnesses on an answer-verifiable agentic search benchmark (BrowseComp)
- a demonstrated positive correlation between report quality and computation allocated to context building, validating effective test-time scaling under the file-system paradigm as an alternative to longer in-context reasoning
- module ablations isolating the contribution of the persistent workspace, the dual-agent separation, and section-wise (vs. one-shot) writing to overall report quality

## Method

Separates deep research into two agents sharing a persistent, unlimited-size file-system workspace instead of holding all state in-context. The Context Builder acts as a librarian: it browses the web (search_web, read_webpage tools) and archives raw sources into a sources/ directory while distilling notes into a hierarchically organized, citation-linked knowledge_base/ directory and an index.md table of contents, iterating (updating a todo list and self-checking against a checklist) until a session budget is reached or no issues remain. The Report Writer then treats the knowledge base as its sole source of facts (with web-browsing tools removed) and composes the report section-by-section across multiple sessions -- first producing an outline (which doubles as its own todo file), then writing and section-level-reviewing one section per session -- rather than generating the whole report in one shot. Both agents use file-system tools (ls, grep, read_file, insert/delete/replace) that introduce negligible latency (<0.03% of wall-clock time) and let intermediate artifacts persist and be revisited across multiple agent sessions.

## Results

On DeepResearch Bench, FS-Researcher with Claude-Sonnet-4.5 reaches 53.94 RACE score, outperforming the strongest baseline (RhinoInsight, Gemini-2.5-Pro) by +3.02, with especially large gains in Comprehensiveness (+3.74) and Insight (+4.4); under the same backbone, FS-Researcher improves RACE by +2.16 over LangChain-Open-Deep-Research (GPT-5) and +1.59 over RhinoInsight (Gemini-2.5-Pro), and Gemini-2.5-Pro equipped with only a search tool scores 31.9 RACE versus 49.71 inside its official harness versus 52.51 inside FS-Researcher -- confirming gains come from the framework, not just the backbone. On DeepConsult, FS-Researcher (Claude-Sonnet-4.5) attains the highest win rate (80.00%) and average score (8.33) among all compared systems. On BrowseComp (an answer-verifiable agentic search benchmark), FS-Researcher outperforms the corresponding official agent harness under both backbones tested: 55.0% vs. 43.9% (Claude-Sonnet-4.5) and 68.0% vs. 54.9% (GPT-5), demonstrating the advantage extends to objectively verifiable metrics, not just LLM-as-judge settings. Ablation scaling experiments show increasing Context Builder rounds from 3 to 10 consistently improves Comprehensiveness, Insight, Instruction Following and RACE (though Readability peaks at 5 rounds and slightly drops at 10, a presentation-level tradeoff from denser technical writing, not an information-quality tradeoff), directly validating effective test-time scaling under the file-system paradigm; module ablations show removing the persistent workspace drops RACE from 52.76 to 48.69 (largest hit to Insight, -7.95), merging the two agents into one causes the largest overall degradation (52.76 -> 42.41 RACE, -16.89 Insight), and disabling section-wise writing in favor of one-shot report generation drops RACE to 47.63. A smaller-summarizer variant of context compression cuts Context Builder cost 47% with negligible quality loss, and GPT-5-mini with additional context-building rounds reaches performance comparable to OpenAI-DeepResearch at substantially lower cost.

## Limitations

The framework depends on relatively strong foundation models: smaller or less capable backbones (e.g. gpt-5-mini) tend to exhibit shorter trajectories and more frequent premature stopping without extra sessions, and are reported as more prone to vulnerabilities in file operations, reducing overall task success rate, though supplemental experiments show gpt-5-mini with additional context-building rounds can reach performance comparable to OpenAI-DeepResearch at lower cost. Because the framework relies on web-sourced content, it may propagate inaccurate, biased or outdated information into downstream reports. Persisting retrieved materials and notes in a file-system workspace may inadvertently store sensitive or copyrighted content, and in untrusted environments increases the attack surface for prompt injection or malicious pages attempting to influence tool actions -- risks the paper explicitly flags rather than resolves.

## Why it matters here

- **overthinking**: Only loosely connected: this scales test-time compute for long-horizon agentic research tasks by moving state out of the context window into an external file-system workspace, not by lengthening or shortening a single reasoning trace, so it does not engage the accuracy/efficiency tradeoff of reasoning length the topic tracks. It is relevant mainly as a structural point of contrast -- an example where more test-time compute helps because it is spent on persistent, revisitable external memory rather than a longer in-context chain-of-thought, a different axis of 'test-time scaling' than most of the archive's overthinking-mitigation work addresses.

## Entities

- **Concepts**: file-system-based persistent workspace (external memory beyond context window), dual-agent Context Builder / Report Writer separation, session-based iterative refinement, test-time scaling via external memory rather than longer context
- **Methods**: FS-Researcher (file-system-based dual-agent framework), Claude-DeepResearch, OpenAI-DeepResearch, Gemini-2.5-Pro-DeepResearch (proprietary baselines), LangChain-Open-Deep-Research, WebWeaver, RhinoInsight, EnterpriseDeepResearch (open-source baselines)
- **Datasets**: DeepResearch Bench, DeepConsult, [BrowseComp](../../../../wiki/datasets/browsecomp.md)

Tags: `deep-research-agents`, `test-time-scaling`, `file-system-workspace`, `long-horizon-tasks`, `agentic-search`

## Abstract

Deep research is emerging as a representative long-horizon task for large language model (LLM) agents. However, long trajectories in deep research often exceed model context limits, compressing token budgets for both evidence collection and report writing, and preventing effective test-time scaling. We introduce FS-Researcher, a file-system-based, dual-agent framework that scales deep research beyond the context window via a persistent workspace. Specifically, a Context Builder agent acts as a librarian which browses the internet, writes structured notes, and archives raw sources into a hierarchical knowledge base that can grow far beyond context length. A Report Writer agent then composes the final report section by section, treating the knowledge base as the source of facts. In this framework, the file system serves as a durable external memory and a shared coordination medium across agents and sessions, enabling iterative refinement beyond the context window. Experiments on two open-ended benchmarks (DeepResearch Bench and DeepConsult) show that FS-Researcher achieves state-of-the-art report quality across different backbone models. Further analyses demonstrate a positive correlation between final report quality and the computation allocated to the Context Builder, validating effective test-time scaling under the file-system paradigm. The code and data are open-sourced at https://github.com/Ignoramus0817/FS-Researcher.

---

Record id: `doi:10.18653/v1/2026.acl-long.288`
