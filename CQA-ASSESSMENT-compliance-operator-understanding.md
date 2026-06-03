# CQA 2.1 Assessment Report

**Assembly:** `security/compliance_operator/co-concepts/compliance-operator-understanding.adoc`

**Scope:** Assembly + included topics (3 files total)

**Mode:** Assess only (no fixes applied)

**Date:** 2026-06-24

---

## Executive Summary

**Overall Score: 3.6 / 4.0** (90%)

This assembly and its included topics demonstrate strong compliance with Red Hat modular documentation standards. The content is well-structured, uses correct product attributes, passes all Vale linting checks, and follows editorial and legal guidelines. 

**Key strengths:**
- Clean Vale validation (0 errors, 0 warnings)
- Proper modular structure with correct content types
- Excellent legal/branding compliance
- Good editorial quality and tone

**Areas for improvement:**
- Assembly abstract exceeds word/character limits (66 words / 450 chars)
- One long sentence in CONCEPT file (43 words)
- Missing Additional resources sections (limits content journey)
- Some abstracts lack WHY statements (benefit to user)

---

## Files in Scope

1. `security/compliance_operator/co-concepts/compliance-operator-understanding.adoc` (ASSEMBLY)
2. `modules/compliance-profiles.adoc` (CONCEPT)
3. `modules/compliance-profile-types.adoc` (REFERENCE)

Include tree resolved with 3 files (assembly + 2 topics).

---

## Tab 1: Pre-migration Assessment

### P1: Vale DITA Validation
**Score: 4** ✓ **Required**

- Vale version: AsciiDocDITA rules
- Result: 0 errors, 0 warnings
- All files pass DITA conversion checks

### P2: Assembly Structure
**Score: 4** ✓ **Required**

- No rendered text between includes ✓
- Clean structure: intro → includes → end
- All includes use proper `leveloffset` syntax

### P3: Content Modularization
**Score: 3** **Required**

- Content type declarations correct ✓
- Actual content matches declared types ✓
- **Issue:** Files lack recognized prefixes (`con_`, `ref_`)
  - Note: Repo uses non-standard directory structure

### P4: Module Templates
**Score: 4** ✓ **Required**

- All required elements present:
  - `:_mod-docs-content-type:` ✓
  - `[id="..."]` anchors ✓
  - `= Title` headings ✓
  - `[role="_abstract"]` annotations ✓
- Includes have proper `leveloffset` ✓
- No procedure-only block titles in wrong types ✓

### P5: Required Modular Elements
**Score: 3** **Required**

- All structural elements present ✓
- **Abstract quality issue:**
  - Assembly: 66 words / 450 characters (exceeds 50-word / 300-char limits)
  - CONCEPT: 28 words / 183 characters ✓
  - REFERENCE: 23 words / 169 characters ✓

### P6: Assembly Template
**Score: 4** ✓ **Required**

- Follows official template ✓
- All required elements present ✓
- Proper include structure ✓
- Coherent user story (understanding Compliance Operator profiles)

### P7: Nesting Depth
**Score: 4** ✓ **Important**

- Maximum 2 levels of nesting ✓
- No assembly-inside-assembly ✓
- No topic-inside-topic ✓
- No `===` headings in topics ✓

### P8: Short Description Quality
**Score: 2** **Required**

**Issues found:**
- Assembly abstract: Missing WHY (benefit statement)
- CONCEPT abstract: Missing WHY
- REFERENCE abstract: Missing WHY

All abstracts avoid self-referential language but don't explain why users should read the content.

### P9: Short Description Structure
**Score: 2** **Required**

**Issues:**
- Assembly abstract: 66 words (exceeds 50), 450 chars (exceeds 300)
- CONCEPT abstract: ✓ Within limits
- REFERENCE abstract: ✓ Within limits

All files have correct `[role="_abstract"]` formatting.

### P10: Title Forms
**Score: 4** ✓ **Important**

- All titles work in search, navigation, and page heading contexts ✓
- Clear and self-descriptive ✓
- Scannable in TOC ✓

### P11: Title Quality
**Score: 3** **Required**

**Issue:**
- Assembly title uses weak opener "Understanding"
  - Suggestion: "Compliance Operator overview"

Other titles correct:
- CONCEPT: Proper noun phrase ✓
- REFERENCE: Proper noun phrase ✓

All titles within 3-11 word range.

### P12: Procedures Structure
**Score: N/A** **Required**

No PROCEDURE files in scope.

### P13: Grammar
**Score: 4** ✓ **Required**

- American English spelling ✓
- No grammatical errors ✓
- Proper article usage ✓

### P14: Content Type Correctness
**Score: 4** ✓ **Required**

- Assembly: Contains includes, correct structure ✓
- CONCEPT: Explanatory content, no procedures ✓
- REFERENCE: Contains definition lists (structured data) ✓

### P15: No Broken Links
**Score: 4** ✓ **Required**

- All 3 includes resolve correctly ✓
- No xrefs to validate
- No images to validate
- No duplicate IDs ✓

### P16: Redirects
**Score: N/A** **Required**

No renamed/moved content in scope.

### P17: Content Interlinking
**Score: 3** **Important**

- Assembly structure proper ✓
- Topics reachable in 2 clicks ✓
- **Issue:** No Additional resources sections
- **Issue:** No cross-references to related content

### P18: Official Product Names
**Score: 4** ✓ **Required**

- All product references use attributes ✓
- No hardcoded product names ✓
- Uses `{product-title}`, `{op-system}`, `{op-system-first}`

### P19: Tech Preview Disclaimers
**Score: N/A** **Required**

No TP/DP features mentioned.

---

## Tab 2: Quality Assessment

### Q1: Scannability
**Score: 3** **Required**

**Assembly:**
- 4 sentences, 19.0 avg words/sentence ✓

**CONCEPT:**
- 4 sentences, 23.0 avg words/sentence (1.0 over target)
- 1 sentence with 43 words (line 64)

**REFERENCE:**
- 13 sentences, 14.7 avg words/sentence ✓

### Q2: Clearly Written
**Score: 4** ✓ **Important**

- Content understandable on first read ✓
- Titles within 3-11 word range ✓
- No clarity issues ✓

### Q3: Simple Words
**Score: 4** ✓ **Important**

- No complex words in prose ✓
- Note: "in order to" appears only in code samples, not prose

### Q4: Readability
**Score: 4** ✓ **Important**

- Good sentence structure ✓
- Technical terminology appropriate ✓
- No readability concerns

### Q5: Fluff
**Score: 4** ✓ **Important**

- No fluff patterns ✓
- No self-referential language ✓

### Q6-Q11: User Focus
**Score: 3** **Important**

**Strengths:**
- CONCEPT and REFERENCE files include examples ✓
- User-focused language ("you/your") ✓
- Clear explanations ✓

**Weaknesses:**
- No Additional resources sections
- No troubleshooting guidance
- Limited cross-linking

### Q12-Q16: Procedure Quality
**Score: N/A** **Important**

No procedures in scope.

### Q17: Non-RH Link Disclaimers
**Score: 4** ✓ **Important**

- 1 external URL (cyber.gov.au) in code sample ✓
- Authoritative government domain ✓

### Q18: Style Guide Compliance
**Score: 4** ✓ **Required**

- No future tense overuse ✓
- No anthropomorphism ✓
- No possessives of brand names ✓
- No phrasal verbs ✓

### Q19: Tables
**Score: N/A** **Important**

No tables present.

### Q20: Tone
**Score: 4** ✓ **Important**

- No contractions ✓
- No first person ✓
- No informal language ✓
- Professional, technical tone ✓

### Q21-Q22: Images
**Score: N/A** **Important**

No images present.

### Q23: Conscious Language
**Score: 4** ✓ **Required**

- No exclusionary terms ✓
- Clean across all tier checks ✓

### Q24-Q25: Content Journey
**Score: 3** **Important**

- Logical assembly structure ✓
- **Issue:** No Additional resources sections
- **Issue:** Limited cross-references

---

## Tab 3: Onboarding Assessment

### O1: Product Names
**Score: 4** ✓ **Required**

- All product names use attributes ✓

### O2: Legal Notices
**Score: 4** ✓ **Required**

- LICENSE file present ✓
- Publishing pipeline injects legal notices

### O3: Official Product Names
**Score: 4** ✓ **Required**

- Consistent attribute usage ✓

### O4: Conscious Language
**Score: 4** ✓ **Required**

- No violations ✓

### O5: Tech Preview Disclaimers
**Score: N/A** **Required**

No TP/DP features.

### O6: TOC Structure
**Score: 4** ✓ **Required**

- Logical flow: concept → reference ✓
- Scannable structure ✓

### O7: Metadata Complete
**Score: 4** ✓ **Required**

- Content type declarations ✓
- ID anchors ✓
- Abstracts ✓
- Product attributes ✓

### O8: Search Keywords
**Score: 4** ✓ **Required**

- Titles include key terms ✓
- Abstracts searchable ✓

### O9: Content Builds
**Score: 4** ✓ **Required**

- Vale: 0 errors, 0 warnings ✓
- All includes resolve ✓
- Valid AsciiDoc syntax ✓

### O10: Rendering
**Score: 4** ✓ **Required**

- Source validation complete ✓
- Structural elements correct ✓

---

## Score Summary by Tab

| Tab | Score | Status |
|-----|-------|--------|
| **Pre-migration (P1-P19)** | 3.5/4.0 | Good |
| **Quality (Q1-Q25)** | 3.7/4.0 | Good |
| **Onboarding (O1-O10)** | 4.0/4.0 | Excellent |
| **Overall** | **3.6/4.0** | **90%** |

---

## Recommendations

### High Priority (Required Parameters)

1. **Shorten assembly abstract** (P5, P8, P9)
   - Current: 66 words / 450 characters
   - Target: ≤50 words / 50-300 characters
   - Recommendation: Condense to 1-2 sentences focusing on WHAT + WHY

2. **Add WHY to abstracts** (P8)
   - Assembly: Explain why admins need this information
   - CONCEPT: Why understanding profiles matters
   - REFERENCE: Why knowing profile types is important

3. **Shorten long sentence** (Q1)
   - Line 64 in compliance-profiles.adoc (43 words)
   - Split at logical break point

### Medium Priority (Important Parameters)

4. **Add Additional resources sections** (P17, Q24-Q25)
   - Link to related procedures (running scans, remediating compliance issues)
   - Link to Red Hat knowledge base articles
   - Cross-reference to other Compliance Operator documentation

5. **Consider simpler assembly title** (P11)
   - Current: "Understanding the Compliance Operator"
   - Suggested: "Compliance Operator overview" or "The Compliance Operator"

---

## Compliance by Level

### Required (Must Pass)
- **Passing:** P1, P2, P4, P6, P13, P14, P15, P18, Q1, Q18, Q23, O1-O4, O6-O10
- **Needs Work:** P3 (prefixes), P5 (abstract length), P8-P9 (abstract quality), P11 (title)

### Important (Should Pass)
- **Passing:** P7, P10, Q2-Q5, Q17, Q20
- **Needs Work:** P17, Q6-Q11, Q24-Q25 (cross-linking)

---

## Conclusion

This assembly demonstrates high-quality modular documentation with strong compliance across most CQA 2.1 parameters. The content is well-structured, legally compliant, and follows Red Hat editorial standards. The main improvements needed are shortening the assembly abstract and adding Additional resources sections to support the user's content journey.

**Recommended Next Steps:**
1. Shorten assembly abstract to meet 50-word limit
2. Add WHY statements to all abstracts
3. Split 43-word sentence in CONCEPT file
4. Add Additional resources sections with cross-references
5. Re-run Vale validation after edits

