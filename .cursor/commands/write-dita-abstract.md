# write-dita-abstract

Rewrite DITA short descriptions (`[role="_abstract"]`) for OpenShift modular topics.

Use on its own, when Vale reports **AsciiDocDITA.ShortDescription**, or as **step 2** of **`/prepare-dita`** (required for every assembly and module in scope—not only when Vale fails).

**Formerly:** `/write-abstract`

**Instructions:** Scan the file. If it is a module (`CONCEPT`, `PROCEDURE`, or `REFERENCE`), read the parent assembly for context. **Rewrite** the short description; do not only add `[role="_abstract"]` to copy that was written as a generic intro paragraph.

**Style:** Two concise sentences when possible. Purpose-first **“To…”** for procedures; **“You can…”** when natural. Active voice, present tense, second person. FK Grade 12 or lower. 50–300 characters (roughly 40–75 words).

1. **Format:** Begin with `[role="_abstract"]` on its own line, then the abstract paragraph. No bullets or admonitions in the abstract.

2. **Module type:**
   - **Procedure:** “To *goal*, you can *action*.”
   - **Concept:** Define the concept, then why it matters.
   - **Reference:** What the item is used for.

3. **Forbidden:** “This topic covers…”, repeating the module title, “helps you” (use “you can”), anthropomorphism, feature-forward “This product allows you…”

4. **Search:** If `{product-title}` is not in the title, include it in the first sentence.

5. **Style validation (required):**

```bash
echo 'Your abstract text here' | python3 .cursor/resources/style-guide/check-ibm-style.py --no-spell
```

Revise until clean. Only then add the abstract to the `.adoc` file.

## Example

[role="_abstract"]
To keep your image streams clean and maintain organized image references in {product-title}, you can remove unused or outdated image stream tags. Remove tags by using the `oc delete istag` or `oc tag -d` commands.
