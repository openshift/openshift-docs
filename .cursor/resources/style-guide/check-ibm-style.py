#!/usr/bin/env python3
"""
IBM / Red Hat / OpenShift documentation style checker.

Loads reference corpus from files next to this script (must be present for full validation):
  - IBMQuickStyle.pdf (IBM Style quick reference; full IBM Style PDF is not shipped in-repo)
  - red-hat-supplementary-style-guide.pdf (Red Hat supplementary guidance)
  - ocp-documentation-guidelines.md (OpenShift repo modular-docs rules)

Checks are pattern-based heuristics aligned with those sources (plus Hunspell for typos).
At startup the script confirms each file was read (character counts on stderr).

Examples:
  python3 check-ibm-style.py /home/stevsmit/pp/openshift-docs
  python3 check-ibm-style.py modules/foo.adoc
  python3 check-ibm-style.py --max-files 100 /home/stevsmit/pp/openshift-docs
  python3 check-ibm-style.py --no-spell …   # style only
  cat snippet.adoc | python3 check-ibm-style.py
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

QUICK_PDF_PATH = SCRIPT_DIR / "IBMQuickStyle.pdf"
RH_SUPP_PDF_PATH = SCRIPT_DIR / "red-hat-supplementary-style-guide.pdf"
OCP_GUIDELINES_PATH = SCRIPT_DIR / "ocp-documentation-guidelines.md"

DEFAULT_SCAN_ROOT = Path("/home/stevsmit/pp/openshift-docs")

# Technical terms common in OpenShift docs (Hunspell personal dictionary baseline)
TECH_WORDS_BASE = frozenset({
    "openshift", "kubernetes", "kubectl", "jsonpath", "namespaces", "namespace",
    "hostname", "hostnames", "fqdn", "distro", "okd", "redhat", "crc", "kubelet",
    "kubeadm", "etcd", "multus", "subresource", "finalizer", "finalizers",
    "imagestream", "imagestreams", "istag", "machineconfig", "machineconfigs",
    "machineset", "machinesets", "daemonset", "daemonsets", "statefulset",
    "statefulsets", "configmap", "configmaps", "persistentvolume", "persistentvolumeclaim",
    "deployable", "virtualization", "virtualized", "nullable", "hostname", "kubeconfig",
    "apiserver", "oauth", "oauthclient", "clusterrole", "clusterroles", "rolebinding",
    "rolebindings", "clusterrolebinding", "clusterrolebindings", "subscription",
    "subscriptions", "operand", "operands", "hyperconverged", "operands", "kubevirt",
    "cri-o", "crio", "kube-proxy", "iptables", "ipvs", "sdn", "ovn", "vlan",
    "macvlan", "ipvlan", "multicast", "unicast", "metadata", "filesystem",
    "filesystems", "filesystem's", "misconfigured", "preconfigured", "namespace",
    "namespaced", "rollout", "rollouts", "readme", "asciidoc", "adoc", "toc",
    "distros", "hostname", "hostname's", "regex", "grep", "sudo", "chmod", "chown",
    "journalctl", "firewalld", "selinux", "systemd", "cgroups", "cgroup", "uuid",
    "uids", "tls", "ssl", "http", "https", "dns", "tcp", "udp", "ipv", "ipv4", "ipv6",
    "api", "apis", "uri", "urls", "url", "cli", "gui", "jq", "yaml", "yml", "json",
    "etcd", "grpc", "websocket", "websockets", "middleware", "middleware's",
    "hostname", "sudoers", "nfs", "iscsi", "ceph", "gluster", "vmware", "aws",
    "azure", "gcp", "ibm", "z", "ppc", "aarch", "x86", "amd", "gpu", "gpus",
    "nvidia", "intel", "vlan", "mtu", "vxlan", "geneve", "iptables", "netfilter",
    "iptables", "sysctl", "kube", "k8s", "kubernetes'", "openshift's",
    "customizable", "unschedulable", "schedulable", "toleration", "tolerations",
    "affinity", "anti-affinity", "webhook", "webhooks", "namespaced", "subpath",
    "subpaths", "priorityclass", "priorityclasses", "runtimeclass", "runtimeclasses",
    "podsecurity", "securitycontext", "securitycontextconstraints", "healthcheck",
    "healthchecks", "readiness", "liveness", "ingress", "ingresses", "route", "routes",
    "passthrough", "edge", "reencrypt", "wildcards", "wildcard", "namespaced",
    "quotas", "limitrange", "limitranges", "resourcequota", "resourcequotas",
    "horizontalpodautoscaler", "verticalpodautoscaler", "poddisruptionbudget",
    "poddisruptionbudgets", "networkpolicy", "networkpolicies", "endpointslice",
    "endpointslices", "servicemonitor", "servicemonitors", "prometheus", "alertmanager",
    "alertmanagers", "thanos", "jaeger", "istio", "knative", "tekton", "argocd",
    "gitops", "helm", "charts", "chart's", "operators", "operand", "olm", "csv",
    "installplan", "subscription", "catalogsource", "catalogsources",
    "konnectivity", "kube-apiserver", "openshift-apiserver", "machine-api",
    "baremetal", "baremetal's", "metal3", "pxe", "ipxe", "bmc", "bios", "uefi",
    "raid", "luks", "dm-crypt", "cryptsetup", "dnf", "rpm", "rpms", "yum",
    "bootloader", "initrd", "dracut", "grub", "kernel", "kernels", "kdump",
    "journald", "rsyslog", "logrotate", "auditd", "sssd", "ldap", "ldaps", "kerberos",
    "oidc", "saml", "rbac", "rbac's", "csr", "csrs", "csr's", "csrapproval",
    "machines", "machine's", "baremetalhost", "baremetalhosts", "installconfig",
    "pullsecret", "pullsecrets", "mirror-registry", "imagecontentsourcepolicy",
    "clusterversion", "clusterversions", "machineconfiguration", "containerruntimeconfig",
    "kubeletconfig",     "apicasts", "apicast", "config", "configs",
    "openshift", "s2i", "ifndef", "endif", "ifdef",
    "dpa", "velero", "minio", "uploader", "kopia", "restic", "oadp", "hypershift",
})


def extract_pdf_text(pdf_path: Path) -> str | None:
    if not pdf_path.exists():
        return None
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", "-nopgbrk", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Warning: could not read {pdf_path.name}: {e}", file=sys.stderr)
        return None


def load_ocp_guidelines_text() -> str:
    if not OCP_GUIDELINES_PATH.exists():
        return ""
    try:
        return OCP_GUIDELINES_PATH.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"Warning: could not read {OCP_GUIDELINES_PATH}: {e}", file=sys.stderr)
        return ""


def collect_adoc_files(targets: list[Path]) -> list[Path]:
    files: list[Path] = []
    skip_parts = {".git", "_preview", "node_modules", "vendor"}
    for t in targets:
        p = t.expanduser().resolve()
        if p.is_file():
            if p.suffix.lower() == ".adoc":
                files.append(p)
        elif p.is_dir():
            for child in p.rglob("*.adoc"):
                if any(part in skip_parts for part in child.parts):
                    continue
                files.append(child)
        else:
            print(f"Warning: not found: {p}", file=sys.stderr)
    return sorted(set(files))


def strip_asciidoc_for_spelling(line: str) -> str:
    """Remove AsciiDoc markup from a single line for spell checking."""
    s = line
    if s.strip().startswith("//"):
        return ""
    st = s.strip()
    if re.match(r"^(ifdef|ifndef|endif)::", st):
        return ""
    if re.match(r"^include::", st):
        return ""
    if re.match(r"^image::", st):
        return ""
    s = re.sub(r"\{nbsp\}", " ", s, flags=re.IGNORECASE)
    # Inline markup
    s = re.sub(r"link:[^\[]*\[([^\]]*)\]", r"\1", s)
    s = re.sub(r"xref:[^\[]*\[[^\]]*\]", " ", s)
    s = re.sub(r"https?://[^\s\[\]]+", " ", s)
    s = re.sub(r"\{([^}]+)\}", r" \1 ", s)
    s = re.sub(r"`[^`]+`", " ", s)
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    s = re.sub(r"_([^_]+)_", r"\1", s)
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.sub(r"\+[^+\s][^+]*\+", " ", s)
    return s


def spell_line_plain(line: str) -> str:
    """Strip non-prose bits; keep words hunspell can digest."""
    s = strip_asciidoc_for_spelling(line)
    s = re.sub(r"^<\d+>\s*", "", s)
    s = re.sub(r"[=:][^\s]+", " ", s)
    s = re.sub(r"\b([A-Za-z]{2,})\d+\b", r"\1", s)
    s = re.sub(r"\bs21\b", " ", s, flags=re.IGNORECASE)
    return s


def extract_attr_words(text: str) -> set[str]:
    """Words inside {attribute} or :attribute: definitions."""
    found: set[str] = set()
    for m in re.finditer(r"\{([^}]+)\}", text):
        for part in re.split(r"[^\w]+", m.group(1)):
            if len(part) >= 3:
                found.add(part.lower())
    for m in re.finditer(r"^:([a-zA-Z0-9_-]+):", text, re.MULTILINE):
        if len(m.group(1)) >= 3:
            found.add(m.group(1).lower())
    return found


def build_personal_dict(extra: set[str]) -> Path:
    """Hunspell personal dict entries (lower + common product capitalization)."""
    lower_extra = {w.lower() for w in extra if w}
    brand_spellings = {
        "OpenShift",
        "Kubernetes",
        "KubeVirt",
        "GitLab",
        "GitHub",
        "Ansible",
        "DevOps",
        "Microservices",
        "Velero",
        "MinIO",
        "DPA",
    }
    words_set = set(TECH_WORDS_BASE) | lower_extra | brand_spellings
    for w in list(words_set):
        if isinstance(w, str) and w.islower() and len(w) > 3:
            words_set.add(w.capitalize())
    words = sorted(words_set)
    tmp = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        prefix="ibm-style-hunspell-",
        suffix=".dic",
        delete=False,
    )
    try:
        for w in words:
            if w and not w.startswith("#"):
                tmp.write(w + "\n")
        tmp.close()
        return Path(tmp.name)
    except Exception:
        Path(tmp.name).unlink(missing_ok=True)
        raise


def hunspell_suggestion(word: str, personal: Path) -> str | None:
    """First Hunspell suggestion for a misspelled word, if any."""
    try:
        r = subprocess.run(
            ["hunspell", "-a", "-d", "en_US", "-p", str(personal)],
            input=word + "\n",
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    for line in r.stdout.splitlines():
        if line.startswith("&"):
            # & word n len: sug1, sug2, ...
            parts = line.split(":", 1)
            if len(parts) == 2:
                sugs = [s.strip() for s in parts[1].split(",") if s.strip()]
                if sugs:
                    return sugs[0]
    return None


def hunspell_misspellings(text: str, personal: Path) -> list[str]:
    if not text.strip():
        return []
    try:
        r = subprocess.run(
            ["hunspell", "-l", "-d", "en_US", "-p", str(personal)],
            input=text,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except FileNotFoundError:
        return []
    except subprocess.TimeoutExpired:
        print("Warning: hunspell timed out", file=sys.stderr)
        return []
    out = [w.strip() for w in r.stdout.splitlines() if w.strip()]
    # Drop tokens that are mostly digits / hex / paths
    filtered = []
    for w in out:
        if re.match(r"^[0-9a-fA-F.-]+$", w) and len(w) > 8:
            continue
        if "/" in w or "\\" in w:
            continue
        filtered.append(w)
    return filtered


def issue(
    rule: str,
    description: str,
    source: str,
    line: int,
    column: int = 0,
    text: str = "",
    suggestion: str | None = None,
    path: str | None = None,
) -> dict:
    d = {
        "rule": rule,
        "description": description,
        "source": source,
        "line": line,
        "column": column,
        "text": text,
    }
    if suggestion:
        d["suggestion"] = suggestion
    if path:
        d["path"] = path
    return d


def check_lines_anthropomorphism(lines: list[str], path: str | None) -> list[dict]:
    patterns = [
        (
            r"\b(the|a|an)\s+\w+\s+(knows|thinks|decides|chooses|wants|likes|hates|feels|sees|hears)\b",
            "Object appears to have human cognitive abilities",
        ),
        (
            r"\b(the|a|an)\s+\w+\s+(tries|attempts|fails|succeeds)\b",
            "Object appears to have human agency",
        ),
        (
            r"\b(the|a|an)\s+\w+\s+(allows|enables|permits)\s+you\b",
            'Avoid stating that inanimate objects grant abilities; prefer "you can ..."',
        ),
    ]
    issues: list[dict] = []
    src = "ibm-style"
    for ln, line in enumerate(lines, 1):
        for pat, desc in patterns:
            for m in re.finditer(pat, line, re.IGNORECASE):
                issues.append(
                    issue(
                        "anthropomorphism",
                        desc,
                        src,
                        ln,
                        m.start(),
                        m.group(),
                        "Rephrase to avoid attributing human traits to objects",
                        path,
                    )
                )
    return issues


def check_lines_future_tense(lines: list[str], path: str | None) -> list[dict]:
    pats = [
        (r"\bwill\s+\w+", 'Future tense: "will"'),
        (r"\bshall\s+\w+", 'Future tense: "shall"'),
        (r"\bgoing\s+to\s+\w+", 'Future tense: "going to"'),
    ]
    issues: list[dict] = []
    for ln, line in enumerate(lines, 1):
        for pat, desc in pats:
            for m in re.finditer(pat, line, re.IGNORECASE):
                issues.append(
                    issue(
                        "future_tense",
                        desc + " — use present tense where possible",
                        "ibm-style",
                        ln,
                        m.start(),
                        m.group(),
                        "Use present tense",
                        path,
                    )
                )
    return issues


def check_lines_passive_voice(lines: list[str], path: str | None) -> list[dict]:
    # Narrow pattern: "is configured by" style (avoids flagging every "is used")
    pats = [
        (r"\b(is|are|was|were|been)\s+\w+ed\s+(by|with)\b", "Passive voice (agent with by/with)"),
    ]
    issues: list[dict] = []
    for ln, line in enumerate(lines, 1):
        if line.strip().startswith("//"):
            continue
        for pat, desc in pats:
            for m in re.finditer(pat, line, re.IGNORECASE):
                issues.append(
                    issue(
                        "passive_voice",
                        desc,
                        "ibm-style",
                        ln,
                        m.start(),
                        m.group()[:80],
                        "Prefer active voice",
                        path,
                    )
                )
    return issues


def check_lines_expletive(lines: list[str], path: str | None) -> list[dict]:
    pats = [
        (r"\bIt\s+is\b", 'Expletive "It is" hides the subject'),
        (r"\bThere\s+are\b", 'Expletive "There are" hides the subject'),
        (r"\bThere\s+is\b", 'Expletive "There is" hides the subject'),
    ]
    issues: list[dict] = []
    for ln, line in enumerate(lines, 1):
        if line.strip().startswith("//"):
            continue
        for pat, desc in pats:
            if re.search(pat, line, re.IGNORECASE):
                issues.append(
                    issue(
                        "expletive_constructions",
                        desc,
                        "ibm-style",
                        ln,
                        0,
                        line.strip()[:120],
                        "Make the subject explicit",
                        path,
                    )
                )
                break
    return issues


def check_lines_phrasal_verbs(lines: list[str], path: str | None) -> list[dict]:
    pv = {
        r"\bfind\s+out\b": "discover",
        r"\blook\s+up\b": "search",
        r"\bpoint\s+out\b": "indicate",
        r"\bset\s+up\b": "configure",
        r"\bturn\s+on\b": "enable",
        r"\bturn\s+off\b": "disable",
        r"\bgo\s+through\b": "review",
        r"\bcarry\s+out\b": "execute",
    }
    issues: list[dict] = []
    for ln, line in enumerate(lines, 1):
        if line.strip().startswith("//"):
            continue
        for pat, repl in pv.items():
            for m in re.finditer(pat, line, re.IGNORECASE):
                issues.append(
                    issue(
                        "phrasal_verbs",
                        f'Consider one-word alternative for "{m.group()}"',
                        "ibm-style",
                        ln,
                        m.start(),
                        m.group(),
                        f'Consider "{repl}"',
                        path,
                    )
                )
    return issues


def check_lines_first_person(lines: list[str], path: str | None) -> list[dict]:
    pats = [
        r"\bI\s+",
        r"\bwe\s+",
        r"\bus\s+",
        r"\bour\s+",
    ]
    issues: list[dict] = []
    for ln, line in enumerate(lines, 1):
        if line.strip().startswith("//"):
            continue
        for pat in pats:
            if re.search(pat, line, re.IGNORECASE):
                issues.append(
                    issue(
                        "first_person",
                        "First person (I/we/us/our) — use with caution in product docs",
                        "ibm-style",
                        ln,
                        0,
                        line.strip()[:120],
                        "Prefer second person (you) or imperative",
                        path,
                    )
                )
                break
    return issues


def check_lines_gender_pronouns(lines: list[str], path: str | None) -> list[dict]:
    pats = [
        r"\bhe\s+",
        r"\bshe\s+",
        r"\bhim\s+",
        r"\bhis\s+",
        r"\bhers\b",
    ]
    issues: list[dict] = []
    for ln, line in enumerate(lines, 1):
        if line.strip().startswith("//"):
            continue
        for pat in pats:
            if re.search(pat, line, re.IGNORECASE):
                issues.append(
                    issue(
                        "gender_specific_pronouns",
                        "Possible gender-specific pronoun — prefer inclusive wording",
                        "ibm-style",
                        ln,
                        0,
                        line.strip()[:120],
                        'Use "they/their", "you", or plural nouns',
                        path,
                    )
                )
                break
    return issues


def check_rh_supplementary_lines(lines: list[str], path: str | None) -> list[dict]:
    """Patterns called out in Red Hat supplementary style guide (prose)."""
    issues: list[dict] = []
    patterns = [
        (
            r"This topic covers",
            'Self-referential phrasing ("This topic covers…")',
        ),
        (
            r"This section (describes|covers|explains)",
            "Self-referential section phrasing",
        ),
        (
            r"Use this procedure to",
            'Self-referential procedural lead-in ("Use this procedure to…")',
        ),
        (
            r"This product allows you to",
            'Feature-focused phrasing ("This product allows you to…")',
        ),
    ]
    for ln, line in enumerate(lines, 1):
        if line.strip().startswith("//"):
            continue
        for pat, desc in patterns:
            if re.search(pat, line, re.IGNORECASE):
                issues.append(
                    issue(
                        "rh_supplementary_prose",
                        desc,
                        "red-hat-supplementary",
                        ln,
                        0,
                        line.strip()[:120],
                        "Focus on user goals; avoid meta-documentation phrasing",
                        path,
                    )
                )
                break
    return issues


def check_ocp_structure(lines: list[str], path: str | None) -> list[dict]:
    """Structural checks from ocp-documentation-guidelines.md."""
    issues: list[dict] = []
    if not path or not path.endswith(".adoc"):
        return issues

    title_optional = re.compile(r'^=+\s*"?Optional:\s?', re.IGNORECASE)
    overview_heading = re.compile(r"^=+\s*Overview\s*$", re.IGNORECASE)
    # Require whitespace after the run of `=` so `====` block delimiters do not match.
    h3_or_lower = re.compile(r"^={3,}\s+\S")

    for ln, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("//"):
            continue
        if overview_heading.match(stripped):
            issues.append(
                issue(
                    "ocp_heading",
                    'Do not use "Overview" as a heading (OpenShift doc guidelines)',
                    "ocp-documentation-guidelines",
                    ln,
                    0,
                    stripped[:120],
                    "Use a specific descriptive heading",
                    path,
                )
            )
        if title_optional.match(stripped):
            issues.append(
                issue(
                    "ocp_optional_prefix",
                    'Do not prefix assembly/module titles with "Optional:"',
                    "ocp-documentation-guidelines",
                    ln,
                    0,
                    stripped[:120],
                    None,
                    path,
                )
            )
        if h3_or_lower.match(stripped):
            issues.append(
                issue(
                    "ocp_heading_level",
                    "Do not use H3 (`===`) or lower in modular topics",
                    "ocp-documentation-guidelines",
                    ln,
                    0,
                    stripped[:120],
                    "Use `==` sections and leveloffsets",
                    path,
                )
            )
        if re.match(r"^=+\s", stripped) and "`" in stripped:
            issues.append(
                issue(
                    "ocp_title_markup",
                    "Do not use backticks in assembly/module titles",
                    "ocp-documentation-guidelines",
                    ln,
                    0,
                    stripped[:120],
                    None,
                    path,
                )
            )
    return issues


def check_spell_lines(
    lines: list[str],
    path: str | None,
    personal: Path,
    skip_spell: bool,
    hunspell_available: bool,
) -> list[dict]:
    if skip_spell or not hunspell_available:
        return []
    issues: list[dict] = []
    in_block = False
    seen_line_word: set[tuple[int, str]] = set()
    for ln, raw in enumerate(lines, 1):
        s = raw.strip()
        if s.startswith("----") and s == "----":
            in_block = not in_block
            continue
        if in_block:
            continue
        plain = spell_line_plain(raw)
        if len(plain.strip()) < 4:
            continue
        bad = hunspell_misspellings(plain, personal)
        for w in bad:
            if len(w) <= 2:
                continue
            key = (ln, w.lower())
            if key in seen_line_word:
                continue
            seen_line_word.add(key)
            sug = hunspell_suggestion(w, personal)
            suggestion = (
                f'Consider "{sug}"'
                if sug and sug.lower() != w.lower()
                else "Verify spelling or add domain term to project glossary"
            )
            issues.append(
                issue(
                    "possible_typo",
                    f'Possible misspelling: "{w}"',
                    "hunspell-en_US",
                    ln,
                    plain.find(w) if w in plain else 0,
                    w,
                    suggestion,
                    path,
                )
            )
    return issues


def run_all_checks(
    lines: list[str],
    path: str | None,
    personal: Path,
    skip_spell: bool,
    hunspell_available: bool,
) -> list[dict]:
    agg: list[dict] = []
    agg.extend(check_lines_anthropomorphism(lines, path))
    agg.extend(check_lines_future_tense(lines, path))
    agg.extend(check_lines_passive_voice(lines, path))
    agg.extend(check_lines_expletive(lines, path))
    agg.extend(check_lines_phrasal_verbs(lines, path))
    agg.extend(check_lines_first_person(lines, path))
    agg.extend(check_lines_gender_pronouns(lines, path))
    agg.extend(check_rh_supplementary_lines(lines, path))
    agg.extend(check_ocp_structure(lines, path))
    agg.extend(check_spell_lines(lines, path, personal, skip_spell, hunspell_available))
    return agg


def format_report(all_issues: list[dict], rules_meta: str) -> None:
    if not all_issues:
        print("✓ No issues reported.")
        return
    print(f"\n⚠ {len(all_issues)} issue(s) ({rules_meta})\n")
    by_key: dict[str, list[dict]] = {}
    for i in all_issues:
        key = i["rule"]
        by_key.setdefault(key, []).append(i)

    for rule_name in sorted(by_key.keys()):
        bucket = by_key[rule_name]
        print(f"\n{rule_name.upper().replace('_', ' ')} ({len(bucket)})")
        for i in bucket[:50]:
            loc = i.get("path") or "<stdin>"
            print(f"  {loc}:{i['line']}: {i['description']}")
            if i.get("suggestion"):
                print(f"    → {i['suggestion']}")
            if i.get("text"):
                print(f"    … {i['text'][:100]}")
        if len(bucket) > 50:
            print(f"  … {len(bucket) - 50} more")


def load_reference_corpus() -> tuple[str, str, str]:
    """Load PDF/Markdown sources (for validation + future expansion)."""
    quick = extract_pdf_text(QUICK_PDF_PATH) or ""
    rh = extract_pdf_text(RH_SUPP_PDF_PATH) or ""
    ocp = load_ocp_guidelines_text()
    return quick, rh, ocp


def scan_adoc_paths(
    paths: list[Path],
    rules_meta: str,
    no_spell: bool,
    hunspell_available: bool,
) -> None:
    all_issues: list[dict] = []
    for p in paths:
        try:
            content = p.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"Skip {p}: {e}", file=sys.stderr)
            continue
        lines = content.splitlines()
        extra = extract_attr_words(content)
        personal = build_personal_dict(extra)
        try:
            all_issues.extend(
                run_all_checks(lines, str(p), personal, no_spell, hunspell_available)
            )
        finally:
            personal.unlink(missing_ok=True)
    format_report(all_issues, rules_meta)
    sys.exit(1 if all_issues else 0)


def verify_sources_loaded(quick: str, rh: str, ocp: str) -> bool:
    ok = False
    if quick:
        print(f"  ✓ {QUICK_PDF_PATH.name} ({len(quick)} chars)", file=sys.stderr)
        ok = True
    else:
        print(f"  — missing {QUICK_PDF_PATH.name}", file=sys.stderr)
    if rh:
        print(f"  ✓ {RH_SUPP_PDF_PATH.name} ({len(rh)} chars)", file=sys.stderr)
        ok = True
    else:
        print(f"  — missing {RH_SUPP_PDF_PATH.name}", file=sys.stderr)
    if ocp:
        print(f"  ✓ {OCP_GUIDELINES_PATH.name} ({len(ocp)} chars)", file=sys.stderr)
        ok = True
    else:
        print(f"  — missing {OCP_GUIDELINES_PATH.name}", file=sys.stderr)
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description="Check AsciiDoc against IBM/RH/OpenShift style heuristics.")
    parser.add_argument(
        "targets",
        nargs="*",
        help="AsciiDoc files or directories to scan (default: stdin or openshift-docs root)",
    )
    parser.add_argument(
        "--no-spell",
        action="store_true",
        help="Disable Hunspell typo checking",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=0,
        help="Stop after N files when scanning directories (0 = no limit)",
    )
    args = parser.parse_args()

    quick, rh, ocp = load_reference_corpus()
    print("Style reference corpus:", file=sys.stderr)
    if not verify_sources_loaded(quick, rh, ocp):
        print("Warning: no style guide files found next to check-ibm-style.py", file=sys.stderr)

    rules_meta = "IBM-quick-style + red-hat-supplementary + ocp-guidelines + hunspell"
    hunspell_ok = bool(shutil.which("hunspell"))
    if not args.no_spell and not hunspell_ok:
        print(
            "Warning: hunspell not found; spelling checks disabled. "
            "Install hunspell and en_US (Fedora: dnf install hunspell-en).",
            file=sys.stderr,
        )
    elif not args.no_spell:
        print("  ✓ hunspell spelling enabled (en_US)", file=sys.stderr)

    if not args.targets:
        if not sys.stdin.isatty():
            text = sys.stdin.read()
            lines = text.splitlines()
            extra = extract_attr_words(text)
            personal = build_personal_dict(extra)
            try:
                issues = run_all_checks(
                    lines, None, personal, args.no_spell, hunspell_ok
                )
                format_report(issues, rules_meta)
            finally:
                personal.unlink(missing_ok=True)
            sys.exit(1 if issues else 0)

        if DEFAULT_SCAN_ROOT.is_dir():
            paths = collect_adoc_files([DEFAULT_SCAN_ROOT])
        else:
            print(
                "Usage: provide files/dirs, pipe AsciiDoc on stdin, "
                f"or install docs under {DEFAULT_SCAN_ROOT}",
                file=sys.stderr,
            )
            sys.exit(2)
        if args.max_files and len(paths) > args.max_files:
            paths = paths[: args.max_files]
        if not paths:
            print("No .adoc files found.", file=sys.stderr)
            sys.exit(0)
        scan_adoc_paths(paths, rules_meta, args.no_spell, hunspell_ok)

    paths = collect_adoc_files([Path(t) for t in args.targets])
    if args.max_files and len(paths) > args.max_files:
        paths = paths[: args.max_files]
    if not paths:
        print("No .adoc files matched.", file=sys.stderr)
        sys.exit(0)
    scan_adoc_paths(paths, rules_meta, args.no_spell, hunspell_ok)


if __name__ == "__main__":
    main()
