<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond Memorization: Extending Reasoning Depth with Recurrence, Memory and Test-Time Compute Scaling

- **Authors**: Ivan Rodkin, Daniil Orel, Konstantin Smirnov, Arman Bolatov, Bilal Elbouardi, Besher Hassan, Yuri Kuratov, Aydar Bulatov, Preslav Nakov, Timothy Baldwin, Artem Shelmanov, Mikhail Burtsev
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.2103/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.2103.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.2103
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reasoning is a core capability of large language models (LLMs), yet how multi-step reasoning is learned and executed remains unclear. We study this question in a controlled cellular-automata (1dCA) framework that excludes memorization by using disjoint training and test rules. Given a short state sequence, the model is required to infer the hidden local rule and then chain it to predict multiple future steps. Our evaluation shows that LLMs largely fail to reliably solve a natural-language proxy of the proposed task. We find that most neural architectures trained from scratch can learn rule inference and achieve high next-step accuracy, but performance drops sharply as the required number of intermediate reasoning steps increases. Experiments show that increasing model depth is crucial, and extending effective depth via recurrence, memory, or test-time compute improves results but remains bounded. Code is available on github: https://github.com/RodkinIvan/associative-recurrent-memory-transformer/tree/ACT.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2103`
