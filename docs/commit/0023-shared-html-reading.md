# 0023 — One place for reading a page nobody gave us an API for

| | |
| --- | --- |
| **Commit** | `refactor(common): move HTML reading out of the virtual-site collector` |
| **Scope** | `pipelines/common/html.py`, `pipelines/collect/virtual_site.py`, `tests/test_html.py` |
| **Kind** | refactor |

## What changed

The tag-stripping, attribute-parsing and `<meta>`-reading that
`virtual_site.py` grew now live in `pipelines/common/html.py`, with tests of
their own. `virtual_site.parse_detail` is the same function expressed against
them, and behaves identically.

No behaviour changed. This is preparation: a second collector is about to need
the same three things.

## Why it is built this way

**Three functions, chosen by what a collector actually asks a page for.** Not a
general HTML toolkit — the readable text of a fragment, the meta tags, and the
block that calls itself an abstract. Every one of those exists because a
collector needed it; nothing here is speculative.

**Still regex, deliberately.** A real parser would be a dependency, and it would
not make a scraper any less sensitive to a redesign — the page changing shape
breaks a CSS selector exactly as thoroughly as it breaks a pattern. What
protects against that is the caller checking it got something and saying so
loudly when it did not, which is the discipline
[0020](0020-programme-listings-read-the-noscript-block.md) established and this
module does not weaken.

**`field_text` is separate from `text`.** Listing pages label their fields
inline — `<span class="descriptor">Title:</span>` — and stripping that label is
a different operation from reading text. Keeping them apart means a title that
legitimately contains a colon (`RoCA: Robust Cross-Domain…`) is not truncated,
which a single combined function would get wrong; there is a test for exactly
that.

**`meta` returns a list per name.** The Highwire convention repeats
`citation_author` once per author and the order is the credit order. A
dict-of-strings would silently keep the last author only.

**Script and style bodies are dropped before text extraction.** Otherwise a
page's JavaScript becomes part of a title.

## Trade-offs and rejected alternatives

**Rejected: add `beautifulsoup4` and delete the patterns.** The repository is
standard-library-only except for PyYAML, which is what lets it be deployed by
copying. One collector reading two page shapes does not justify inverting that.

**Rejected: leave the helpers in `virtual_site.py` and import from there.** A
collector importing another collector for string utilities is the arrangement
that makes both hard to delete later.

**Cost: a shared module is now a shared blast radius.** A change made for one
collector can break the other. The tests in `tests/test_html.py` exist to make
that a failure rather than a surprise.

## What a reviewer should check

That `virtual_site` really is unchanged in behaviour — its whole suite should
pass untouched:

```bash
python3 -m unittest tests.test_virtual_site tests.test_html -v
```

`test_a_colon_inside_a_title_survives` is the one worth reading: it is the case
that a naive "strip everything before the colon" implementation gets wrong, and
arXiv and conference titles are full of colons.

## Downstream impact

None. No configuration, no data, no output changes. `pipelines.common.html` is
new and nothing outside the collectors imports it.
