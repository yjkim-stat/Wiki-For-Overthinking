<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# FREE: Fast and Robust Vision Language Models with Early Exits

- **Authors**: Divya Jyoti Bajpai, Manjesh Kumar Hanawal
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.findings-acl.1209/>
- **PDF**: <https://aclanthology.org/2025.findings-acl.1209.pdf>
- **DOI**: 10.18653/v1/2025.findings-acl.1209
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

In recent years, Vision-Language Models (VLMs) have shown remarkable performance improvements in Vision-Language tasks. However, their large size poses challenges for real-world applications where inference latency is a concern. To tackle this issue, we propose employing Early Exit (EE) strategies in VLMs. However, training exit classifiers in VLMs is challenging, particularly with limited labeled training data. To address this, we introduce FREE, an adversarial training approach within a GAN-based framework. Here, each exit consists of a transformer layer and a classifier. The transformer layer is adversarially trained to produce feature representations similar to the final layer, while a feature classifier serves as the discriminator. Our method focuses on performing input-adaptive inference that increases inference speed with minimal drop in performance. Experimental results demonstrate the effectiveness of our approach in enhancing accuracy and model robustness by mitigating overthinking and the phenomenon of mid-crisis that we highlight. We experimentally validate that our method speeds up the inference process by more than 1.51× while retaining comparable performance. The anonymized source code is available at https://github.com/Div290/BLIPEE.

---

Record id: `doi:10.18653/v1/2025.findings-acl.1209`
