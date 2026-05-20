# Callout rewrite ruleset (DITA migration)

Canonical examples: [openshift/openshift-docs#102276](https://github.com/openshift/openshift-docs/pull/102276) — *[DO NOT MERGE] Callout rewrite examples* (Andrea Hoffer). Use this file with **`/fix-dita-callouts`**.

## Goal

Remove AsciiDoc callout markers (`<1>`, `<2>`, `# <1>`, …) from `[source,...]` blocks and replace trailing numbered callout lines with DITA-safe prose. **Never leave** `<n>` lists after a code block.

## Preserve source wording (required)

**Do not rewrite callout prose.** This pass is a **structural and minimal wording** fix for DITA, not an editorial rewrite.

| Allowed | Not allowed |
| --- | --- |
| Remove `<n>` markers from examples | Paraphrase, shorten, or expand explanations |
| Move text into Pattern A–F structure (`where:`, lead-in sentence, bullets) | Change meaning, tone, or examples the author chose |
| Set the correct **term** on the left of `::` (full path, placeholder, or flag) | Replace precise product terms or links |
| Change leading **Specify** to **Specifies** on `::` definitions (and keep **Replace** / **For** / **In this example** openings where Pattern A–C require them) | Reword the rest of the sentence “for clarity” |
| **Slightly** adjust the opening of a callout so the `::` definition starts with **Specifies** and reads as a complete sentence | Rewrite the middle or end of the explanation |

### Starting definitions with **Specifies** (Pattern E)

Every Pattern E definition (text after `::`) must begin with **Specifies** and be a **grammatically correct** complete sentence.

The YAML path on the left of `::` already identifies the field or section. The definition should state what that path **means** or **does**—not repeat the path, section name, or “this field” in the prose after **Specifies**.

### Avoid redundant framing (concise definitions)

Do **not** mirror the old callout’s scaffolding (“this specification”, “the \`strategy\` section”, “the \`runPolicy\` field”, “this field”) when the `::` term already names what you are documenting. Strip that framing and lead with the **substance** after **Specifies**.

| Pattern in original callout | Too wordy (do not use) | Prefer |
| --- | --- | --- |
| This specification creates a new \`BuildConfig\` named … | Specifies that this specification creates a new \`BuildConfig\` named … | **Specifies a new \`BuildConfig\` named …** |
| The \`strategy\` section describes the build strategy … | Specifies that the \`strategy\` section describes the build strategy … | **Specifies the build strategy …** (keep following sentences that add detail) |
| The \`source\` section defines the source … | Specifies that the \`source\` section defines the source … | **Specifies the source …** |
| The \`runPolicy\` field controls whether … | Specifies that the \`runPolicy\` field controls whether … | **Specifies whether …** (when the path is \`spec.runPolicy\`) |
| Name of the policy. | Specifies the name of the policy. | Already concise—keep |
| Pushed into the repository described in the \`output\` section | …described in the \`output\` section | **…pushed into the repository.** (path is \`spec.output\`) |

Use **Specifies that** only when the sentence needs **that** for grammar or meaning (for example, a condition: **Specifies that {lvms} wipes… when set to \`true\`.**), not to introduce “the X section/field/specification”.

1. If the callout starts with **Specify** or **Set this field to**, drop the redundant field reference and open with **Specifies** + the value or behavior (see table below).
2. If the callout starts with **Specify the** (direct object), change only **Specify** → **Specifies** and keep the rest.
3. If the callout starts with **If this field is set to**, reorder minimally so **Specifies** leads and the condition still reads naturally (often **when set to** at the end).
4. For other openings (**The**, **You can**, **To retain**, **Configure**, …), make the **smallest** edit so the line starts with **Specifies**, stays grammatical, and preserves meaning.

### Optional parameters (Pattern E)

When the original callout begins with **Optional:** (see [openshift/openshift-docs#102276](https://github.com/openshift/openshift-docs/pull/102276)):

1. **Drop** the leading **Optional:** from the rewritten text.
2. Rewrite the explanation in one or more complete sentences that start with **Specifies** (same minimal rules as above). Multiple sentences are allowed.
3. If the word **optional** does **not** appear in the rewritten description, add a **second sentence** at the end: **This parameter is optional.** or **This field is optional.** or **This value is optional.** (match the term you use elsewhere in the topic when sensible).
4. If you already used **optional** in the description (for example, **Specifies an optional** description), do **not** add the extra sentence.

| Original callout | Acceptable after `::` | Unacceptable |
| --- | --- | --- |
| `Optional: If you do not use \`dhcp\`, you can either set a static IP or leave the interface without an IP address.` | `Specifies a static IP. Leave the interface without an IP address if you do not use \`dhcp\`. This field is optional.` | `Specifies an optional static IP…` only; or one long **Specifies that you can…** sentence |
| `Optional: Create a Liveness probe.` | `Specifies a Liveness probe. This parameter is optional.` | `Specifies an optional Liveness probe.` (redundant **optional** in the same line—pick one approach) |
| `Optional: If you do not include the \`nodeSelector\` parameter, the policy applies to all nodes in the cluster.` | `Specifies that the policy applies to all nodes in the cluster if you do not include the \`nodeSelector\` parameter. This parameter is optional.` | Omitting **This parameter is optional.** when **optional** is not in the body |
| `Optional: Human-readable description of the interface.` | `Specifies a human-readable description of the interface. This field is optional.` | `Specifies an optional human-readable description…` **and** `This field is optional.` (duplicate) |

**Minimal wording change examples:**

| Original callout | Acceptable after `::` | Unacceptable |
| --- | --- | --- |
| `Specify the bucket name; for example, \`oadp-backup\`.` | `Specifies the bucket name; for example, \`oadp-backup\`.` | `Specifies the S3 bucket that stores backup data, such as \`oadp-backup\`.` |
| `Set this field to the name of a VG from the previous {lvms} installation.` | `Specifies the name of a VG from the previous {lvms} installation.` | `Specifies setting this field to the name of a VG…` |
| `Set this field to \`ext4\` or \`xfs\`. By default, this field is set to \`xfs\`.` | `Specifies \`ext4\` or \`xfs\`. By default, this field is set to \`xfs\`.` | `Specifies setting this field to \`ext4\` or \`xfs\`…` |
| `If this field is set to \`true\`, {lvms} wipes all the data on the devices that are added to the VG.` | `Specifies that {lvms} wipes all the data on the devices that are added to the VG when set to \`true\`.` | `Specifies that if this field is set to \`true\`, {lvms} wipes…` (awkward **if** after **Specifies that**) |
| `Specify the provider for Velero. If you are using bare metal and MinIO, you can use \`aws\` as the provider.` | `Specifies the provider for Velero. If you are using bare metal and MinIO, you can use \`aws\` as the provider.` | Condensing into different guidance about providers |
| `The bucket region in this example is \`minio\`, which is a storage provider that is compatilble with the S3 API.` | `Specifies that the bucket region in this example is \`minio\`, which is a storage provider that is compatible with the S3 API.` | Rewriting the compatibility explanation |
| `You can specify the size of the disk to use in GB. Minimum recommendation for control plane nodes is 1024 GB.` | `Specifies the size of the disk to use in GB. Minimum recommendation for control plane nodes is 1024 GB.` | `Specifies that you can specify the size of the disk…` |
| `You can optionally provide the \`sshKey\` value that you use to access the machines in your cluster.` | `Specifies the \`sshKey\` value that you use to access the machines in your cluster. This parameter is optional.` | `Specifies the optional \`sshKey\` value…` **and** `This parameter is optional.` (duplicate) |

**Do not** repeat **you can**, **specify**, **this field**, or **the \`…\` section/field** after **Specifies** when the `::` term already identifies it (avoid **Specifies that you can specify**, **Specifies setting this field to**, **Specifies that this specification creates**, **Specifies that the \`strategy\` section describes**, and similar).

When the original callout uses **Replace**, **For**, or is a general note (**In this example**, …), use Pattern A, B, or C instead of Pattern E, and keep the original opening (**Replace**, **For**, **In this example**) unchanged.

## Step 1 — Always strip markers from the example

**Before:**

```asciidoc
[source,yaml]
----
  provider: aws # <1>
  bucket: <bucket_name> # <2>
----
```

**After:**

```asciidoc
[source,yaml]
----
  provider: aws
  bucket: <bucket_name>
----
```

Apply to terminal, YAML, JSON, and command output blocks.

---

## Step 2 — Choose a replacement pattern

Use the original callout text and how many markers the block had.

| Callouts in block | Original callout style | Pattern |
| --- | --- | --- |
| **1** | `Replace <placeholder> with …` | **A — Replace sentence** |
| **1** | `For <placeholder>, specify …` / explains one flag or argument | **B — For sentence** |
| **1** | `In this example, …` / general note on the command | **C — Explanatory sentence** |
| **1** | `<placeholder>` is the path/name … (defines one placeholder) | **D — Placeholder lead-in** |
| **2+** | Documents fields, keys, placeholders, or YAML keys | **E — `where:` description list** |
| **2+** | Interprets lines in command **output** (not input) | **F — Output bullet list** |

If a procedure step continues after the explanation, prefix the replacement with `+` on its own line (see [Connection to procedure steps](#connection-to-procedure-steps)).

---

### Pattern A — Single callout: Replace sentence

**Before:**

```asciidoc
[source,terminal]
----
$ oc adm upgrade --to=<version> <1>
----
<1> `<version>` is the update version that you obtained from the output of the `oc adm upgrade recommend` command.
```

**After:**

```asciidoc
[source,terminal]
----
$ oc adm upgrade --to=<version>
----
+
Replace `<version>` with the update version that you obtained from the output of the `oc adm upgrade recommend` command.
```

Keep **Replace** at the start when the original callout used **Replace**.

---

### Pattern B — Single callout: For sentence

**Before:**

```asciidoc
[source,terminal]
----
$ ./openshift-install create install-config --dir <directory> <1>
----
<1> For `<directory>`, specify the directory name to store the files that the installation program creates.
```

**After:**

```asciidoc
[source,terminal]
----
$ ./openshift-install create install-config --dir <directory>
----
+
For `<directory>`, specify the directory name to store the files that the installation program creates.
```

---

### Pattern C — Single callout: Explanatory sentence

**Before:**

```asciidoc
[source,terminal]
----
$ oc adm must-gather --image={must-gather-v1-5} -- /usr/bin/gather --request-timeout 1m # <1>
----
<1> In this example, the timeout is 1 minute.
```

**After:**

```asciidoc
[source,terminal]
----
$ oc adm must-gather --image={must-gather-v1-5} -- /usr/bin/gather --request-timeout 1m
----
+
In this example, the timeout is 1 minute.
```

Use when the callout is not defining a single placeholder or field.

---

### Pattern D — Single callout: Placeholder lead-in

**Before:**

```asciidoc
[source,terminal]
----
$ oc create configmap custom-ca \
  --from-file=ca-bundle.crt=<path> <1>
----
<1> `<path>` is the path to the root CA certificate file on your local file system.
```

**After:**

```asciidoc
[source,terminal]
----
$ oc create configmap custom-ca \
  --from-file=ca-bundle.crt=<path>
----
+
`<path>` is the path to the root CA certificate file on your local file system.
```

---

### Pattern E — Multiple callouts: `where:` description list

Use for **two or more** callouts that document parameters, placeholders, or configuration keys in the **same** preceding example.

**Before:**

```asciidoc
[source,yaml]
----
spec:
  tolerations:
  - key: node-role.kubernetes.io/infra <1>
    value: reserved <2>
----
<1> Specify the key that you added to the node.
<2> Specify the value of the key-value pair taint that you added to the node.
```

**After:**

```asciidoc
[source,yaml]
----
spec:
  tolerations:
  - key: node-role.kubernetes.io/infra
    value: reserved
----
+
where:
+
* `spec.tolerations.key`:: Specifies the key that you added to the node.
* `spec.tolerations.value`:: Specifies the value of the key-value pair taint that you added to the node.
```

#### Term (left side of `::`) — full notation (OpenShift)

**Default:** Use the **full field path** from the example (dot notation from the resource root), not a short key name alone.

| Prefer | Avoid (unless exception below) |
| --- | --- |
| `` `spec.backupLocations.velero.provider` `` | `provider` |
| `` `spec.backupLocations.velero.objectStorage.bucket` `` | `bucket` or `` `<bucket_name>` `` as the term |

Build the path from the YAML structure in the block:

- Start at `spec` (or `metadata`, `status`, and so on) when the manifest is a Kubernetes CR.
- Walk nested keys in order: `spec.backupLocations.velero.config.region`.
- Use **`velero`**, not `valero`.
- Omit array indexes unless the topic already uses them (for example `spec.backupLocations[0].velero.provider`). Prefer the PR #102276 style without `[]` unless the source already documents indexed paths.

**Exception — placeholder-only blocks:** If **every** callout in the same example documents **only** user-defined placeholders (for example `<bucket_name>`, `<bucket_prefix>`) and not mixed real field names, you may use the placeholder as the term:

```asciidoc
* `<bucket_name>`:: Specifies the bucket name; for example, `oadp-backup`.
* `<bucket_prefix>`:: Specifies the bucket prefix; for example, `hcp`.
```

If the block mixes placeholders and real fields (for example `provider` and `<bucket_name>`), use **full notation for all terms**, including paths to `objectStorage.bucket` and `objectStorage.prefix` rather than `` `<bucket_name>` ``.

**Other cases (from PR #102276):**

| Situation | Term |
| --- | --- |
| Single placeholder in a terminal command (Pattern A/B/D) | `` `<directory>` `` in the lead-in or Replace sentence |
| Command output (Pattern F) | Resource name or field label, not a spec path |

#### Definition (right side of `::`) — OpenShift DITA rule

For field, parameter, and key callouts in Pattern E:

1. Copy the **original callout sentence** after the numbered marker.
2. Ensure the text after `::` begins with **Specifies** and is a complete sentence (see [Starting definitions with **Specifies**](#starting-definitions-with-specifies-pattern-e)).
3. If it begins with **Replace** or another Pattern A opener, use Pattern A instead—do not force a `where:` list.
4. Leave the remainder of the sentence **unchanged** after the opening adjustment (including **specify** lowercase mid-sentence, semicolons, and examples).

```asciidoc
<2> Specify the bucket name; for example, `oadp-backup`.
```

becomes:

```asciidoc
* `spec.backupLocations.velero.objectStorage.bucket`:: Specifies the bucket name; for example, `oadp-backup`.
```

—not a newly written sentence about buckets.

When converting callouts that began with **Replace**, use Pattern A for a **single** placeholder and keep the **Replace** wording. For **multiple** callouts in one block, use Pattern E with **Specifies** at the start of each `::` definition when the source used **Specify**.

**Optional:** A long `where:` list may be wrapped in `--` … `--` when it sits inside a procedure step (see PR `binding-infra-node-workloads-using-taints-tolerations.adoc`).

---

### Pattern F — Multiple callouts: Output interpretation (bullet list)

Use when callouts annotate **command output** lines (pod names, table rows, events), not input the user types.

**Before:**

```asciidoc
[source,terminal]
----
NAME   READY   STATUS
my-lws-0   1/1   Running <1>
my-lws-1   1/1   Running <2>
----
<1> The leader pod for the first group.
<2> The leader pod for the second group.
```

**After:**

```asciidoc
[source,terminal]
----
NAME   READY   STATUS
my-lws-0   1/1   Running
my-lws-1   1/1   Running
----
+
* `my-lws-0` is the leader pod for the first group.
* `my-lws-1` is the leader pod for the second group.
```

For output fields (for example `oc describe` sections), use bullets that name the field, as in PR `nw-metallb-configure-svc.adoc`:

```asciidoc
+
* The `Annotations` field shows the `metallb.io/address-pool` annotation if you request an IP address from a specific pool.
* The `Type` field must indicate `LoadBalancer`.
```

**Specifies** is not required for Pattern F unless you are describing a configurable parameter.

---

## Connection to procedure steps

When the code block is part of a numbered procedure step (`. Create …`), connect the explanation with `+`:

```asciidoc
. Create a manifest file similar to the following example:
+
.Example `dpa.yaml` file
[source,yaml]
----
…
----
+
where:

* `spec.backupLocations.velero.provider`:: Specifies the provider for Velero.
```

- Do **not** put a lone `+` between an example block title (`.Example output`) and `[source,…]` — only between the step and the title, or after the closing `----` of the block.

---

## Anti-patterns

| Do not | Do instead |
| --- | --- |
| Leave `<1>`, `<2>`, … after `----` | Remove all numbered callout lines |
| Leave `# <n>` inside YAML or shell examples | Strip markers only; keep comments that are real config comments |
| Use numbered callout lists in DITA output | Use Pattern A–F |
| Use a short key alone as the `::` term (`provider`, `bucket`) | Use the **full dotted path** (`spec.…`) |
| Use `` `<bucket_name>` `` as the term when other callouts use real field paths | Use `spec.…objectStorage.bucket` unless **all** callouts are placeholder-only |
| Use **Specify** as the first word of a `::` definition | Change only **Specify** → **Specifies** at the start; keep the rest of the source sentence |
| Paraphrase callout explanations | Preserve original callout text; allow only minimal opening edits for **Specifies** (see [Preserve source wording](#preserve-source-wording-required)) |
| Add or remove `ifdef`, `ifndef`, `ifeval`, or other conditionals | Keep all conditional directives and block boundaries unchanged; edit only callout markers and replacement prose inside existing blocks |
| Nest `[source,…]` inside `[%collapsible]` / `====` for DITA | Remove collapsible wrapper; keep example title + source block (see `/fix-dita-vale`) |

---

## Quick decision flow

```text
Strip all <n> markers from the source block
        │
        ├─ One callout?
        │     ├─ "Replace …"     → Pattern A (+ if after procedure step)
        │     ├─ "For …"       → Pattern B
        │     ├─ "In this …"   → Pattern C
        │     └─ defines one placeholder → Pattern D
        │
        └─ Multiple callouts?
              ├─ input / YAML / command args → Pattern E (Specifies…)
              └─ command output interpretation → Pattern F
```

---

## Source modules in PR #102276

| Module | Patterns illustrated |
| --- | --- |
| `ai-adding-worker-nodes-to-cluster.adoc` | A, E (placeholders) |
| `binding-infra-node-workloads-using-taints-tolerations.adoc` | E (`where:` + `--`), F |
| `customize-certificates-replace-default-router.adoc` | D, E, A |
| `installation-gcp-user-infra-shared-vpc-config-yaml.adoc` | E (dotted YAML keys, split across `where:` + admonitions) |
| `installation-initializing.adoc` | B, E |
| `lws-config.adoc` | E, F |
| `nw-metallb-configure-svc.adoc` | F (field bullets) |
| `update-upgrading-cli.adoc` | A |
| `using-must-gather.adoc` | C |
