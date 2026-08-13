<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge

- **Authors**: Yuanchi Zhu, Kang An, Tengyue Wang, Zhongyu Yang, Chenxu Du, Xinqi Yang, Hebao Zhu, Bokai Zhao, Tianyu Liang, Ziliang Wang, Faqiang Qian, Yunli Yang, Weiyang Shi, Qibing Ren
- **Venue**: cs.AI
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09230>
- **PDF**: <https://arxiv.org/pdf/2608.09230v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.57, reasoning-interpretability 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Industrial-safety understanding requires more than detecting workers, equipment, and personal protective equipment. Models must also assess compliance, identify hazardous interactions, explain potential accident mechanisms, and recommend preventive actions. Existing safety datasets primarily focus on visual perception or isolated violation recognition and provide limited supervision for evidence-grounded reasoning. We introduce SafeSceneReason, a multimodal industrial-safety reasoning benchmark and companion training corpus that connects workplace scenes with knowledge from occupational accident investigations. SafeSceneReason combines two complementary data-construction pipelines. The scene-centric pipeline converts annotated workplace images into executable safety scene graphs and generates deterministic answers through program execution over objects, relations, and safety rules. The report-centric pipeline extracts figures and contextual evidence from accident reports and constructs multimodal questions using evidence graphs, explicit information boundaries, multi-step reasoning paths, and iterative verification. The resulting resource contains 110,581 verified scene-centric question--answer pairs and 13,114 refined report-centric question--answer pairs, covering perception, spatial and quantitative reasoning, compliance assessment, evidence synthesis, causal analysis, and mitigation-oriented decision making. Evaluation of representative proprietary and open-source vision--language models reveals substantial performance differences and persistent weaknesses in comparative, technical, and multi-evidence reasoning, demonstrating that strong general visual understanding does not yet guarantee reliable industrial-safety reasoning.

---

Record id: `arxiv:2608.09230`
