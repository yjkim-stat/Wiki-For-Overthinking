<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Steering Vectors for Competing Ethical Frameworks Are Interchangeable: A Competing-Target Test for Activation Steering

- **Authors**: Weilun Xu, Zipeng Sun
- **Venue**: cs.AI
- **Published**: 2026-10-14
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2610.19359>
- **PDF**: <https://arxiv.org/pdf/2610.19359v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Activation steering adds a vector to a model's hidden states to control a named behaviour. A gain on that behaviour, however, does not show that the vector controls it directly: it may act through a component shared with neighbouring behaviours, which unsteered and random baselines cannot separate. We introduce the competing-target test: a vector is compared with the vector built the same way for a competing target, and an equivalence test states when their difference is below a useful margin. We apply it in open-weight models to vectors for Kantian deontology, which judges an act by the rule it follows, and act utilitarianism, which judges it by the welfare it produces. On held-out situations, prompting a framework raises its score and lowers the other's, whereas vectors for either framework move both scores alike, and none reaches the margin. The two vectors share most of their direction, a request to apply some framework; the same construction separates an optimistic from a pessimistic tone, whose vectors share much less. What a vector shares with its competitors therefore sets what it controls: steering a perspective can deliver a mixture, and measuring a disposition can measure its neighbours, unless tested against the competing target.

---

Record id: `arxiv:2610.19359`
