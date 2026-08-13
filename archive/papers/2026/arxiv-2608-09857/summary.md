<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy

- **Authors**: Rohan Bhagra, Mahantesh Halapannavar, Uddhav Bhattarai
- **Venue**: cs.RO
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09857>
- **PDF**: <https://arxiv.org/pdf/2608.09857v1>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.25, test-time-scaling 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Advances in advanced artificial intelligence tools have sparked research in robot autonomy, but the development of such systems has largely focused on execution rather than verifying the feasibility actions planning models propose. Like general-purpose LLMs, robotics planning models carry risks: biased toward user-specified goals, they may suggest actions misaligned with scientific ethics, they may be unsafe due to an inability to "remember" prior safety risks, or they may be vulnerable to adversarial attacks on the autonomy ecosystem. We propose a LLM-driven verification layer between planning and execution to evaluate action permissibility. Our LLM-as-a-Judge ensemble combines chain-of-thought reasoning across models and synthesizes those expert judge outputs, mirroring a combination of a mixture of experts and self-consistency approach. This layer serves as middleware, gating plans from the server's planning module before they reach the MCP server and therefore the robot's low-level controls: plans are approved, rejected for reformulation, or escalated for human review. With this system, we achieve near 85% precision across accept/escalate/reject categories 97% containment of adversarial attacks, with negligible errors between accepting and rejecting tasks, and errors mostly manifesting at the escalate boundary.

---

Record id: `arxiv:2608.09857`
