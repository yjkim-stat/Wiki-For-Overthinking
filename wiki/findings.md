# What we have settled

## Overthinking

- **Established** — Reasoning-trace length is not a measure of overthinking: it correlates negatively with accuracy, so a longer trace is evidence about the problem rather than about waste.
  - _Three archive records establish this from different directions. Think Deep, Not Just Long ranks eight inference-time signals by mean Pearson correlation with accuracy and finds token length at -0.594, below every internal-state signal it tests (DTR +0.683, self-certainty +0.605, negative entropy +0.571, log-probability +0.527, negative perplexity +0.219) -- so the field's default proxy points the wrong way. LLMThinkBench shows the same thing on a matched pair that isolates training as the cause: Phi-4 scores 78.92 percent at 378.6 tokens per response while Phi-4-reasoning, the same base model under CoT supervision, scores 72.23 percent at 6,066.2 tokens, losing 6.69 accuracy points for roughly 16 times the tokens; its composite Overthinking Score reads 0.863 against 0.352. Do NOT Think That Much for 2+3=? gives the conceptual reason by splitting the quantity in two, outcome efficiency (whether extra compute changes the answer) and process efficiency (what fraction of the chain is redundant), which are independent: how much was emitted and how much was wasted are different questions. The consequence for this archive is that a token count is a cost, not a diagnosis, and any claim that one model overthinks more than another because it emits more tokens is unsupported._
  - Bears on: [Overthinking](concepts/overthinking.md), [Reasoning Trace Length](concepts/reasoning-trace-length.md)
  - From: title:bcd9cf99a0e84a2d, local:c1f4e56014fb43fb, title:7805f8ec24eadc13
- **Established** — A mid-generation overthinking signal predicts only when it carries temporal structure; the presence or absence of a marker at a single point does not, and expressed uncertainty taken on its own predicts in the wrong direction.
  - _Four independent lines in the archive agree. (1) 'Amplified Does Not Mean Predictive' measures Behavioral Lift over ~15,000 annotated traces from 15 checkpoints across 7 families: uncertainty acknowledgment -- the mere presence of expressed doubt, and the behaviour thinking-training amplifies most (25-85% of responses vs 4-28% for instruct) -- carries Lift -16.1% (VLM) / -13.9% (LLM), the worst of nine behaviours. The three behaviours thinking training amplifies occupy the bottom three Lift positions; the amplification-vs-Lift plot's top-right quadrant is empty. (2) Every mid-generation signal that does work in the archive is a rate, a count over time, or a windowed statistic rather than an occurrence: 'When More Thinking Hurts' gets r=0.78 from answer oscillation count alone and r=0.82 combined (76.3% precision / 80% recall for negative flips); Funnel of Thoughts prunes on hesitation-marker density per 1,000 characters and its own ablation shows random pruning loses accuracy at the same compute saving while density-based pruning preserves SC@32 accuracy (94.47% vs 94.36%); Statistical Early Stopping models the inter-arrival times of 102 uncertainty keywords as a renewal process rather than testing for their presence; ParaTempo smooths answer confidence over a W=7 window and reports lower volatility than any instantaneous signal. (3) The two reconcile rather than conflict: expressed uncertainty marks 'this problem is hard or ill-posed', not 'this trace is overthinking now' -- which is why Statistical Early Stopping's keyword rules succeed on ill-posed queries and explicitly do not shorten well-posed-but-hard ones. (4) The same lesson appears where a single-point signal was tried and failed: 'Demystifying Entropy-based Selection' finds random sentence selection beats both entropy selectors on 6 models, and that token-level low-entropy wins only on maths because numeric tokens are low-entropy -- a 'numbers' selector alone recovers near-full accuracy while low-entropy-no-numbers falls below random._
  - Bears on: overthinking indicators (hesitation markers, answer oscillation, confidence trajectory), Uncertainty Acknowledgment, uncertainty-keyword monitoring, Temporal confidence, entropy-based CoT pruning (low-entropy / high-entropy selection)
  - From: arxiv:2608.13760, local:32a56cfa1105c39e, arxiv:2608.15065, title:594984624acaa60d, arxiv:2608.16425, arxiv:2607.28707
- **Established** — VeriThinker has an official public code release at github.com/czg1225/VeriThinker, published alongside its NeurIPS 2025 paper.
  - _Checked the repository directly; it is the paper authors' own implementation of the auxiliary-verification-training method for reducing overthinking._
  - Bears on: [VeriThinker](methods/verithinker.md)
  - From: local:49199e3b0f694ee1, local:6c80b6fd388d671e
  - Checked against: [https://github.com/czg1225/VeriThinker](https://github.com/czg1225/VeriThinker), retrieved 2026-08-21
- **Established** — LC-R1 has an official public code release at github.com/zxiangx/LC-R1.
  - _Checked the repository directly; it is the paper authors' own implementation of the GRPO-based length-compression method for large reasoning models._
  - Bears on: [LC-R1](methods/lc-r1.md)
  - From: local:6c80b6fd388d671e, local:da3fbe3617acc5f8
  - Checked against: [https://github.com/zxiangx/LC-R1](https://github.com/zxiangx/LC-R1), retrieved 2026-08-21
- **Established** — AdaptThink has an official public code release at github.com/THU-KEG/AdaptThink.
  - _Checked the repository directly; it is the paper authors' own implementation of the RL algorithm that lets a reasoning model choose Thinking vs. NoThinking per problem, matching how AdaptThink is described in the archive's sources._
  - Bears on: [AdaptThink](methods/adaptthink.md)
  - From: local:49199e3b0f694ee1, local:da3fbe3617acc5f8
  - Checked against: [https://github.com/THU-KEG/AdaptThink](https://github.com/THU-KEG/AdaptThink), retrieved 2026-08-21
- **Established** — TokenSkip has an official public code release at github.com/hemingkx/TokenSkip, published alongside its EMNLP 2025 paper.
  - _Checked the repository directly; it is the paper authors' own implementation of the token-level chain-of-thought compression method._
  - Bears on: [TokenSkip](methods/tokenskip.md)
  - From: local:6c80b6fd388d671e, local:da3fbe3617acc5f8
  - Checked against: [https://github.com/hemingkx/TokenSkip](https://github.com/hemingkx/TokenSkip), retrieved 2026-08-21
- **Established** — Manifold Steering's repository (github.com/Aries-iai/Manifold_Steering) exists and names the paper as its official implementation, but as of 2026-08-21 the repo itself notes the code was not yet uploaded ("available next month") -- so the paper's headline 71% token-reduction result cannot yet be independently verified by running the code.
  - _Checked the repository directly rather than trusting the paper's own 'code is available at' claim; the repo's current state (README present, implementation pending) is worth recording so a later reader does not assume it is runnable today._
  - Bears on: [Manifold Steering](methods/manifold-steering.md)
  - From: title:b4ba27743c499d8d
  - Checked against: [https://github.com/Aries-iai/Manifold_Steering](https://github.com/Aries-iai/Manifold_Steering), retrieved 2026-08-21
