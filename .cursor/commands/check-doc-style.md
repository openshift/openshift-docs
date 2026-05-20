# check-doc-style

Validate AsciiDoc (and plain text) against the **reference corpus** in `.cursor/resources/style-guide/`, using heuristic checks aligned with IBM Style (quick reference), the Red Hat supplementary style guide, OpenShift modular-docs rules, and **Hunspell spelling** on prose.

**Formerly:** `/check-ibm-sg`

**Repository:** openshift-docs repository root.

## Agent execution (required)

When the user invokes **`/check-doc-style`**, run the checker **with spelling enabled**:

```bash
python3 .cursor/resources/style-guide/check-ibm-style.py path/to/module.adoc
```

Do **not** pass `--no-spell` unless the user asks for style-only checks.

Report **`possible_typo`** hits (including callout lines such as `<4> … compatilble`) and suggest Hunspell corrections when the script provides them.

## Prerequisites

Run once after clone:

```bash
./scripts/sync-cursor-dita-resources.sh
```

Requires:

- `poppler-utils` (`pdftotext`) — PDF corpus verification
- **`hunspell`** + **`en_US`** dictionary — **spelling (on by default)**  
  Fedora/RHEL: `sudo dnf install hunspell hunspell-en`

The **full IBM Style PDF** (`ibm-style-documentation.pdf`) is **not** included in this repository (licensing). Prose checks use pattern heuristics aligned with IBM Style; the quick-reference PDF is loaded only to verify the corpus at startup. For authoritative IBM Style rules, use [IBM Style online](https://www.ibm.com/docs/en/ibm-style).

## Reference sources (beside `check-ibm-style.py`)

| File | Role |
| --- | --- |
| `IBMQuickStyle.pdf` | IBM Style (quick reference) — corpus verification |
| `red-hat-supplementary-style-guide.pdf` | Red Hat supplementary style |
| `ocp-documentation-guidelines.md` | OpenShift / modular-docs structural rules |

The script confirms each file was read at startup (stderr).

## How to use

**One or more `.adoc` files (spelling + style):**

```bash
python3 .cursor/resources/style-guide/check-ibm-style.py modules/example.adoc
```

**Style heuristics only (skip spelling):**

```bash
python3 .cursor/resources/style-guide/check-ibm-style.py --no-spell modules/example.adoc
```

**Stdin:**

```bash
echo "Your text here" | python3 .cursor/resources/style-guide/check-ibm-style.py
```

**Useful flags:** `--no-spell` (disable Hunspell), `--max-files N` (directory scans)

## What gets checked

**Spelling (default):** Hunspell `en_US` on prose outside `----` source blocks; strips AsciiDoc markup and callout prefixes (`<1>` …); product/tech terms from a built-in dictionary; suggests a replacement when Hunspell has one (for example `compatilble` → `compatible`).

**IBM-aligned (prose):** anthropomorphism, future tense, passive voice, expletive constructions, phrasal verbs, first person, gender-specific pronouns

**Red Hat supplementary:** self-referential phrasing, feature-focused phrasing

**OpenShift guidelines (`.adoc`):** Overview headings, optional title prefixes, H3+ section headings (`===` with title text—not lone `====` delimiters), backticks in titles

## Report format

Issues include file path, line number, rule name, description, optional suggestion, and snippet.

| Rule | Meaning |
| --- | --- |
| `possible_typo` | Hunspell flagged a word; fix spelling or add a justified glossary term |
| `ocp_heading_level` | Real `===` (or deeper) section heading in a module |
| Other rules | Style heuristics (see above) |

## Exit codes

- `0`: No issues reported
- `1`: One or more issues reported
- `2`: Usage error

## Notes

- Treat output as advisory; domain terms (DPA, Velero, MinIO) are in the tech dictionary and should not be reported.
- Lone `====` collapsible delimiters are not flagged as headings.
- Use `--no-spell` only when Hunspell is unavailable or the user wants style-only review.
- Extend `TECH_WORDS_BASE` in `check-ibm-style.py` for recurring product terms.
