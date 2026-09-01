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

## In one line

FREE adds GAN-based early exits to frozen-backbone Vision-Language Models -- an exit transformer (generator) trained to mimic the final layer's representations, discriminated against by a frozen final-layer classifier reused as the exit classifier -- addressing both 'overthinking' (unnecessary computation on easy tokens) and a newly named 'mid-crisis' (intermediate-layer accuracy dip from searching for irrelevant features), giving >1.51x inference speedup with comparable accuracy and outperforming four prior early-exit baselines on captioning, VQA and visual dialogue.

## Problem

Vision-Language Models built on frozen pre-trained LM backbones are slow at inference because every token requires a full forward pass through all layers regardless of difficulty (overthinking), and naively attaching early-exit classifiers to intermediate layers introduces a second, previously unnamed problem the authors call 'mid-crisis' -- intermediate layers exhibit an accuracy dip because the LM, frozen during VLP training, aligns image-grounded text embeddings to be well-suited to the final layer only, so intermediate layers have to search for and lose useful features before regaining them deeper in the network. Existing early-exit approaches also add substantial parameter overhead (e.g. a single OPT-2.7B exit classifier costs ~130M parameters) and require large labeled datasets unavailable in zero-shot VLM settings.

## Contributions

- identification and naming of 'mid-crisis' -- an intermediate-layer accuracy dip specific to frozen-LM-backbone VLMs, distinct from and compounding overthinking
- FREE, a GAN-based early-exit training framework where an exit transformer (generator) is trained to mimic final-layer representations against a discriminator, letting the frozen final-layer classifier be reused across all exits, cutting trainable exit parameters by ~52% versus dedicated per-exit classifiers
- supervised and unsupervised (knowledge-distillation or CapFilt-synthetic-label) training variants covering labeled, unlabeled, and zero-shot VLM deployment scenarios
- empirical validation across captioning, VQA and visual dialogue tasks and two VLM backbone families (BLIP-2, plus MiniGPT/InstructBLIP in the appendix) showing FREE beats four prior early-exit baselines and vanilla inference on both accuracy and inference speedup (>1.51x)

## Method

FREE attaches, to K chosen intermediate layers of a frozen VLM's LM decoder, an Exit Transformer (ET, one trainable transformer layer matching the LM layer's configuration) plus an Exit Classifier (EC, the frozen final-layer classifier reused rather than newly trained -- cutting per-exit parameter cost by ~52% versus a dedicated classifier). Training is framed as a GAN: the ET (generator) is trained to produce intermediate-layer feature representations similar to the final layer's, while a separate feature classifier (discriminator) per exit learns to distinguish exit-layer from final-layer representations; adversarial training (rather than cosine similarity, argued to generalize better) aligns intermediate representations to be classifiable by the reused final-layer classifier, directly mitigating both overthinking (confident, correct exits available earlier) and mid-crisis (deep-layer-quality features made available at intermediate depth). To avoid catastrophic forgetting/mode collapse in the untied exit-transformer weights, a small labeled dataset (when available) fine-tunes the backbone with cross-entropy plus the generator loss; when no labeled data exists, two unsupervised alternatives are offered -- knowledge distillation from the final layer's soft labels, or CapFilt-generated synthetic captions (higher quality, more compute). At inference, generation proceeds token-by-token; a token exits at the first layer whose exit-classifier confidence exceeds a threshold alpha, falling back to the final layer if no exit is confident enough.

## Results

On zero-shot NoCaps captioning (BLIP-2 backbones), FREE outperforms four early-exit baselines (DeeBLIP/confidence-based, PABEE-BLIP/patience-based, LeeBLIP/knowledge-distillation, MuE) and the vanilla BLIP-2 model on both accuracy (CIDEr/SPICE) and speedup, reaching up to 1.63x speedup (ViT-g-OPT2.7B) and 1.51x (ViT-g-FlanT5-XL) while matching or exceeding vanilla BLIP-2's CIDEr/SPICE on most domain splits. On semi-supervised VQA (VQAv2), FREE-V-O/F outperform all early-exit baselines and vanilla BLIP-2 in both accuracy and speedup (1.77x/1.71x), and on unsupervised VQAv2/OK-VQA/GQA/VizWiz plus VisDial (visual dialogue), FREE achieves the best or near-best accuracy among early-exit methods at 1.45-1.51x speedup, exceeding baselines like DeeBLIP/PABEE-BLIP/LeeBLIP/MuE on most metrics though with a mild accuracy dip relative to fully-supervised FREE variants (attributed to residual overthinking remaining in the purely unsupervised setup). Semi-supervised COCO captioning (Table 4) shows FREE-V-O reaching the best BLEU-4/CIDEr/METEOR among all early-exit baselines at 1.75x speedup. Motivating analysis (Fig. 3) directly visualizes the two named failure modes on BLIP-2-ViT-g-FlanT5-XL/VQAv2: vanilla early-exit classifiers show an accuracy dip at intermediate layers (mid-crisis) followed by a plateau at deeper layers reflecting unnecessary computation (overthinking); FREE's training process visibly closes the mid-crisis dip while overthinking is subsequently addressed via the exit mechanism itself. OPT-2.7B backbones show higher speedup than FlanT5-XL backbones (more layers, hence more susceptible to overthinking, so more benefit from early exiting); VQA tasks show higher speedup than captioning (VQA judged an easier task).

## Limitations

For attaching exits to a large model such as BLIP-2, deciding where within the LM component to place exits under a given parameter budget is explained via the mid-crisis analysis, but the paper explicitly states that jointly optimizing exit placement together with a fixed parameter budget remains unexplored, which could make the models even faster within the same computational boundaries. Accuracy is observed to decrease somewhat in the fully unsupervised setup (knowledge distillation, no labeled data) because the model still mimics the final layer, retaining 'some amount of overthinking,' versus the semi-supervised setup where a small labeled dataset helps the model learn per-sample hardness more precisely and better overcome overthinking.

## Why it matters here

- **overthinking**: Directly relevant and explicitly self-identified: the paper names 'overthinking' as one of its two core targets (alongside the newly coined 'mid-crisis') and frames its entire early-exit mechanism as a mitigation for unnecessary computation on already-confident predictions, in a vision-language rather than pure-text-reasoning setting. Its mid-crisis finding -- that forcing intermediate layers to produce final-layer-quality features first requires them to un-learn a dip, before overthinking-style excess computation even becomes the binding constraint -- is a mechanistic account potentially transferable to text-only reasoning models with frozen or lightly-tuned backbones, where an analogous intermediate-layer confidence dip could similarly precede any exploitable early-exit opportunity.

## Entities

- **Concepts**: overthinking (unnecessary computation, VLM/early-exit context), mid-crisis (intermediate-layer accuracy dip in frozen-backbone VLMs), GAN-based exit-transformer training, frozen final-layer classifier reuse
- **Methods**: GAN-based adversarial exit training, early exit (input-adaptive inference), knowledge distillation (unsupervised exit training), CapFilt (synthetic label generation), DeeBLIP / PABEE-BLIP / LeeBLIP / MuE (baseline early-exit methods)
- **Datasets**: COCO (captioning), NoCaps, VQAv2, [OK-VQA](../../../../wiki/datasets/ok-vqa.md), [GQA](../../../../wiki/datasets/gqa.md), [VizWiz](../../../../wiki/datasets/vizwiz.md), VisDial

Tags: `overthinking`, `early-exit`, `vision-language-models`, `adversarial-training`, `inference-efficiency`

## Abstract

In recent years, Vision-Language Models (VLMs) have shown remarkable performance improvements in Vision-Language tasks. However, their large size poses challenges for real-world applications where inference latency is a concern. To tackle this issue, we propose employing Early Exit (EE) strategies in VLMs. However, training exit classifiers in VLMs is challenging, particularly with limited labeled training data. To address this, we introduce FREE, an adversarial training approach within a GAN-based framework. Here, each exit consists of a transformer layer and a classifier. The transformer layer is adversarially trained to produce feature representations similar to the final layer, while a feature classifier serves as the discriminator. Our method focuses on performing input-adaptive inference that increases inference speed with minimal drop in performance. Experimental results demonstrate the effectiveness of our approach in enhancing accuracy and model robustness by mitigating overthinking and the phenomenon of mid-crisis that we highlight. We experimentally validate that our method speeds up the inference process by more than 1.51× while retaining comparable performance. The anonymized source code is available at https://github.com/Div290/BLIPEE.

---

Record id: `doi:10.18653/v1/2025.findings-acl.1209`
