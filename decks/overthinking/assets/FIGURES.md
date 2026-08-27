# Figure provenance

The crops this deck cites are **not committed**. This directory (`figures/`) and
everything under `build/` — which includes the standalone deck, carrying the same
images inlined as data URIs — are gitignored: this repository is public, carries no
licence of its own, and the source documents are under a mix of arXiv terms and
Creative Commons variants that were not checked individually. `data/pdfs/` is
untracked for the same reason.

This table is what a clone gets instead. Every row names the paper a crop came from,
so the crop can be retaken from the archive's own copy of the document.

## Retaking them

```bash
python3 -m pipelines.backfill --dry-run   # which papers still have no document
python3 -m pipelines.backfill --limit 20  # fetch them
```

Documents land in `data/pdfs/` and move to `data/pdfs/read/` once their reading is
applied. Crops were taken with PyMuPDF page clips at raised DPI. **The clip
rectangles were chosen by eye and are not recorded anywhere** -- retaking a figure
means finding it in the PDF again, not re-running a script. That is the real cost of
not committing them, and it is why this table exists.

## What each file is

`slide` is the slide that uses it in the current 33-slide deck; blank means the crop
was captured during drafting and nothing references it now.

| file | source | id | slide | caption in the deck |
| --- | --- | --- | --- | --- |
| `danger-fig1.png` | Cuadron et al. 2025 | arXiv:2502.08235 | 10 | Cuadron 외 (2025) Figure 1 원문 인용 — 추론 모델 R² = 0.892, β = −7.894. 4,018개 궤적. |
| `inv-fig1.png` | Gema et al. 2025 | arXiv:2507.14417 | 9 | Gema 외 (2025) Figure 1 원문 인용 — 위: 과제별 실제 프롬프트(초록은 필요한 정보, 빨강은 무관한 미끼). 아래: Claude Sonnet 3.7·Sonnet 4·Opus 4·o3·o3-mini· |
| `ltb-fig3.png` | Srivastava et al. 2026 | arXiv:2507.04023 | 6 | Srivastava 외 (2026) Figure 3 원문 인용 — 네 사례 모두 모델의 실제 출력이다. 갈래 표기는 이 발표가 붙인 것이다. |
| `ltb-fig4.png` | Srivastava et al. 2026 | arXiv:2507.04023 | 7 | Srivastava 외 (2026) Figure 4 원문 인용 — (a) Gemini 2.5 계열, (b) GPT-5 계열, (c) O-시리즈(o3 · o3-mini · o4-mini). |
| `otb-eq-auc.png` | Aggarwal et al. 2025 | arXiv:2508.13141 | 25 | Aggarwal 외 (2025) §2.1 및 Eq. (1) 원문 인용 |
| `otb-eq-correct.png` | Aggarwal et al. 2025 | arXiv:2508.13141 | — | — |
| `otb-eq-oaa.png` | Aggarwal et al. 2025 | arXiv:2508.13141 | 25 | Aggarwal 외 (2025) §2.1 및 Eq. (1) 원문 인용 |
| `otb-fig1.png` | Aggarwal et al. 2025 | arXiv:2508.13141 | 20 | Aggarwal 외 (2025) Figure 1 원문 인용 — ① 쉬운 질의에 1,000 생각 토큰을 쓰고 틀리는 사고형 모델, ② 어려운 문제를 짧게 답해 틀리는 비사고형 모델. |
| `otb-fig2.png` | Aggarwal et al. 2025 | arXiv:2508.13141 | 26 | Aggarwal 외 (2025) Figure 2 원문 인용 — 빨강: 비사고형(t=0부터 70% 고정) · 주황: 과대생각형(쉬운 문제에서도 늦게 도달) · 파랑: 최적사고형. 세 유형의 순서가 넓이 하나로 정해진다 |
| `otb-tab1.png` | Aggarwal et al. 2025 | arXiv:2508.13141 | 28 | Aggarwal 외 (2025) Table 1 원문 인용 — 네 묶음(개방·폐쇄 × 비사고·사고)마다 최고값을 굵게. |
| `otb-tab2.png` | Aggarwal et al. 2025 | arXiv:2508.13141 | 30 | Aggarwal 외 (2025) Table 2 원문 인용 — 괄호 안은 기본 모델 대비 변화량. 초록은 개선, 빨강은 저하. |
| `otb-tab3.png` | Aggarwal et al. 2025 | arXiv:2508.13141 | 31 | Aggarwal 외 (2025) Table 3 원문 인용 — Qwen3 24.3 → 학습된 라우터 46.9 (+20.4) → 오라클 라우터 61.2. |
| `survey-fig2.png` | Yue et al. 2025 | arXiv:2508.02120 | 29 | Yue 외 (2025) Figure 2 원문 인용 |
| `tbs-tab12.png` | Oladri et al. 2026 | arXiv:2607.21433 | — | — |
| `tbs-tab2.png` | Oladri et al. 2026 | arXiv:2607.21433 | — | — |
| `tbs-tab3.png` | Oladri et al. 2026 | arXiv:2607.21433 | 11 | Oladri 외 (2026) Table 3 원문 인용 — 난이도 대리 변수는 문제 번호다(AIME는 대체로 번호순으로 어려워진다). |
| `thns-fig2.png` | Fan et al. 2026 | arXiv:2608.07968 | — | — |
| `thns-tab1.png` | Fan et al. 2026 | arXiv:2608.07968 | — | — |
| `thns-tab6.png` | Fan et al. 2026 | arXiv:2608.07968 | — | — |
| `traac-tab2.png` | Singh et al. 2025 | arXiv:2510.01581 | 32 | Singh 외 (2025) Table 2 원문 인용 — 두 백본에서 TokenSkip · L1-Max · LC-R1 · AdaptThink 를 같은 표에 놓고 F1otb 로 비교. |
| `wmth-fig1.png` | Zhou et al. 2026 | arXiv:2604.10739 | — | — |
| `wmth-fig4.png` | Zhou et al. 2026 | arXiv:2604.10739 | — | — |
| `wmth-tab1.png` | Zhou et al. 2026 | arXiv:2604.10739 | 8 | Zhou 외 (2026) Table 1 원문 인용 — 왼쪽 그림은 이 표의 (b) 열을 옮겨 그린 것이며, 가로축 간격은 균등하지 않다. |
| `wmth-tab4.png` | Zhou et al. 2026 | arXiv:2604.10739 | — | — |
| `wmth-tab7.png` | Zhou et al. 2026 | arXiv:2604.10739 | — | — |

## Papers, in full

| id | title |
| --- | --- |
| arXiv:2508.13141 | *OptimalThinkingBench: Evaluating over and underthinking in LLMs* — Aggarwal et al. 2025 |
| arXiv:2502.08235 | *The danger of overthinking: Examining the reasoning-action dilemma in agentic tasks* — Cuadron et al. 2025 |
| arXiv:2608.07968 | *Thinking hard, not smart: Reasoning models fail to ration test-time compute across questions* — Fan et al. 2026 |
| arXiv:2507.14417 | *Inverse scaling in test-time compute* — Gema et al. 2025 |
| arXiv:2607.21433 | *Token budget saturation and mechanistic early detection of reasoning non-convergence* — Oladri et al. 2026 |
| arXiv:2510.01581 | *Think Right: Learning to mitigate under- and over-thinking* — Singh et al. 2025 |
| arXiv:2507.04023 | *Do LLMs overthink basic math reasoning?* — Srivastava et al. 2026 |
| arXiv:2508.02120 | *Don't overthink it: A survey of efficient R1-style large reasoning models* — Yue et al. 2025 |
| arXiv:2604.10739 | *When more thinking hurts: Overthinking in LLM test-time compute scaling* — Zhou et al. 2026 |
