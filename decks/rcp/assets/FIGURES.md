# Figure provenance

The crops this deck cites are **not committed** — `assets/figures/` and `build/` are
gitignored for the reason the overthinking deck gives in its own `FIGURES.md`: this
repository is public, carries no licence of its own, and the source documents sit under
a mix of arXiv terms that were not checked individually.

This table is what a clone gets instead. Every row names the document and the figure or
table a crop came from, so it can be retaken from the archive's own copy.

## Retaking them

```bash
python3 -m pipelines.backfill --dry-run   # which papers still have no document
ls data/pdfs/read/                        # the PDFs these crops came from
```

Crops were taken with PyMuPDF page clips at 220–260 DPI and then trimmed of white
margins. **The clip rectangles were chosen against text-block coordinates read from the
PDF, not by eye**, so they are reproducible: find the caption with `page.search_for`, take
the drawing or text-block bounds above it, and clip. Two of them (`rcp-injection-table`,
`codestop-table1`) are text-only tables with no vector art, so their rectangles were read
from `page.get_text("blocks")` instead.

## What each file is

| File | Source document | Figure / table | Slide | What it shows |
| --- | --- | --- | --- | --- |
| `rcp-trace-example.png` | arxiv:2508.17627v2 | Table 6 | 02 | 같은 답을 20번 재검증하는 실제 생성 trace |
| `puma-after-answer.png` | arxiv:2605.17672 | Figure 5a | 03 | 최종 답 전후 토큰 분해, 다섯 모델 41–52% |
| `acr-distribution.png` | arxiv:2506.02536 | Figure 2 | 10 | 다섯 과제의 ACR 분포 |
| `answerconv-qwen32b.png` | arxiv:2506.02536 | Figure 3 (R1-Qwen-32B 블록 + 헤더) | 12 | 네 정지 방법의 정확도·토큰 |
| `rcp-length-dynamics.png` | arxiv:2508.17627v2 | Figure 2 | 22 | 절단 지점별 thinking/content length |
| `rcp-semantic-trajectory.png` | arxiv:2508.17627v2 | Figure 3 | 24 | 답 분포의 PCA 궤적과 95% 신뢰타원 |
| `rcp-injection-table.png` | arxiv:2508.17627v2 | Table 3 | 26 | 잠정 답 주입 시 최종 답 분포 (64회) |
| `rcp-rank-drop.png` | arxiv:2508.17627v2 | Figure 5 | 28 | 정확도 안정화와 </think> rank 급락 |
| `rcp-table1-qwen8b.png` | arxiv:2508.17627v2 | Table 1 (Qwen3-8B 블록 + 헤더) | 31 · 48 | iso-compute 비교, 그리고 게재본에서 삭제된 S-GRPO 행 |
| `codestop-table1.png` | arxiv:2604.04930 | Table 1 | 43 | 여섯 기법 × 네 모델 재현 결과 |
| `codestop-pareto.png` | arxiv:2604.04930 | Figure 5 | 44 | 정확도–총 비용 평면 |
| `token-complexity-gpt4o.png` | arxiv:2503.01141 | Figure 1 (GPT-4o 패널) | 49 | 31개 프롬프트가 그리는 하나의 곡선과 Oracle Upper Bound |
