#!/usr/bin/env python3
"""
Fast, comprehensive OKD documentation fixer.
Single-pass per file, tracks conditional/code-block state incrementally.
"""

import os, re, sys
from collections import defaultdict

STATS = defaultdict(int)
CHANGED_FILES = set()

SCAN_DIRS = [
    "modules", "installing", "architecture", "networking",
    "machine_configuration", "security", "updating",
    "post_installation_configuration", "nodes", "operators",
    "registry", "backup_and_restore", "scalability_and_performance",
    "observability", "cli_reference", "applications", "cicd",
    "storage", "authentication", "support", "hosted_control_planes",
    "edge_computing", "openshift_images", "rest_api",
    "hardware_enablement", "migrating_from_ocp_3_to_4", "welcome",
    "hardware_accelerators", "ai_applications", "etcd",
    "disconnected", "extensions", "virt",
]


def process_file(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except:
        return 0

    new_lines = []
    changes = 0
    in_code_block = False
    code_marker = None
    conditional_depth = 0  # depth of ifdef/ifndef blocks that protect content

    for line in lines:
        stripped = line.strip()

        # Track code blocks
        if stripped in ('----', '....', '```'):
            if in_code_block and code_marker == stripped:
                in_code_block = False
                code_marker = None
            elif not in_code_block:
                in_code_block = True
                code_marker = stripped
            new_lines.append(line)
            continue

        # Track conditional blocks
        if re.match(r'ifdef::(openshift-enterprise|openshift-rosa|openshift-dedicated)', stripped):
            conditional_depth += 1
            new_lines.append(line)
            continue
        if re.match(r'ifndef::openshift-origin', stripped):
            conditional_depth += 1
            new_lines.append(line)
            continue
        if re.match(r'ifdef::openshift-origin', stripped):
            conditional_depth += 1
            new_lines.append(line)
            continue
        if stripped.startswith('endif::') and conditional_depth > 0:
            conditional_depth -= 1
            new_lines.append(line)
            continue

        # Skip lines in code blocks, comments, or already-conditioned blocks
        if in_code_block or conditional_depth > 0 or stripped.startswith('//'):
            new_lines.append(line)
            continue

        # Skip attribute definitions and ifdef/endif lines
        if re.match(r':(op-system|product-title|openshift-)', stripped):
            new_lines.append(line)
            continue

        # Skip lines with URLs/links (too risky to modify)
        has_url = bool(re.search(r'https?://|link:|image:', line))

        modified = line
        line_changes = 0

        # --- Category A: "Red Hat Enterprise Linux CoreOS (RHCOS)" → {op-system-first} ---
        if not has_url:
            pat = r'Red\s*(?:\{nbsp\})?\s*Hat\s+Enterprise\s+Linux\s+CoreOS\s*\(RHCOS\)'
            if re.search(pat, modified):
                modified = re.sub(pat, '{op-system-first}', modified)
                line_changes += 1
                STATS['A_RHEL_CoreOS_full'] += 1

        # --- Category B: remaining "Red Hat Enterprise Linux CoreOS" → {op-system-first} ---
        if not has_url:
            pat = r'Red\s*(?:\{nbsp\})?\s*Hat\s+Enterprise\s+Linux\s+CoreOS'
            if re.search(pat, modified):
                modified = re.sub(pat, '{op-system-first}', modified)
                line_changes += 1
                STATS['B_RHEL_CoreOS_short'] += 1

        # --- Category C: standalone "RHCOS" → {op-system} ---
        if not has_url and re.search(r'\bRHCOS\b', modified):
            modified = re.sub(r'\bRHCOS\b', '{op-system}', modified)
            line_changes += 1
            STATS['C_RHCOS'] += 1

        # --- Category D: "OpenShift Container Platform" → {product-title} ---
        if not has_url:
            pat = r'(?:Red\s*(?:\{nbsp\})?\s*Hat\s+)?OpenShift\s+Container\s+Platform'
            if re.search(pat, modified):
                modified = re.sub(pat, '{product-title}', modified)
                line_changes += 1
                STATS['D_product_name'] += 1

        # --- Category E: "Red Hat Enterprise Linux (RHEL)" → {op-system-base-full} ({op-system-base}) ---
        if not has_url:
            pat = r'Red\s*(?:\{nbsp\})?\s*Hat\s+Enterprise\s+Linux\s*\(RHEL\)'
            if re.search(pat, modified):
                modified = re.sub(pat, '{op-system-base-full} ({op-system-base})', modified)
                line_changes += 1
                STATS['E_RHEL_full'] += 1

        # --- Category F: standalone "RHEL" (not RHEL CoreOS, not RHEL AI) → {op-system-base} ---
        if not has_url and re.search(r'\bRHEL\b', modified):
            if not re.search(r'RHEL\s*CoreOS|RHEL\s*AI|rhel-', modified):
                modified = re.sub(r'\bRHEL\b', '{op-system-base}', modified)
                line_changes += 1
                STATS['F_RHEL_standalone'] += 1

        # --- Category G: registry.redhat.io → conditional ---
        if 'registry.redhat.io' in modified:
            okd_line = modified.replace('registry.redhat.io', 'quay.io/openshift-community')
            new_lines.append('ifdef::openshift-enterprise,openshift-rosa,openshift-dedicated[]\n')
            new_lines.append(modified)
            new_lines.append('endif::[]\n')
            new_lines.append('ifdef::openshift-origin[]\n')
            new_lines.append(okd_line)
            new_lines.append('endif::[]\n')
            line_changes += 1
            STATS['G_registry'] += 1
            changes += line_changes
            continue

        # --- Category H: redhat-operators → conditional ---
        if 'redhat-operators' in modified:
            okd_line = modified.replace('redhat-operators', 'community-operators')
            new_lines.append('ifdef::openshift-enterprise,openshift-rosa,openshift-dedicated[]\n')
            new_lines.append(modified)
            new_lines.append('endif::[]\n')
            new_lines.append('ifdef::openshift-origin[]\n')
            new_lines.append(okd_line)
            new_lines.append('endif::[]\n')
            line_changes += 1
            STATS['H_redhat_operators'] += 1
            changes += line_changes
            continue

        # --- Category I: subscription-manager → wrap in ifndef::openshift-origin[] ---
        if re.search(r'subscription-manager|Red\s+Hat\s+Subscription', modified):
            new_lines.append('ifndef::openshift-origin[]\n')
            new_lines.append(modified)
            new_lines.append('endif::openshift-origin[]\n')
            line_changes += 1
            STATS['I_subscription'] += 1
            changes += line_changes
            continue

        new_lines.append(modified)
        changes += line_changes

    if changes > 0:
        with open(filepath, 'w') as f:
            f.writelines(new_lines)
        CHANGED_FILES.add(filepath)
    return changes


def main():
    total_files = 0
    total_fixes = 0

    for scan_dir in SCAN_DIRS:
        if not os.path.isdir(scan_dir):
            continue
        for root, dirs, files in os.walk(scan_dir):
            for fname in files:
                if not fname.endswith('.adoc'):
                    continue
                filepath = os.path.join(root, fname)
                total_files += 1
                fixes = process_file(filepath)
                total_fixes += fixes

    print(f"\n{'='*60}")
    print(f"OKD COMPREHENSIVE DOC FIX REPORT")
    print(f"{'='*60}")
    print(f"\nScanned: {total_files} files")
    print(f"Modified: {len(CHANGED_FILES)} files")
    print(f"Total fixes applied: {total_fixes}")
    print(f"\nBreakdown:")
    for cat in sorted(STATS.keys()):
        print(f"  {cat}: {STATS[cat]}")

    print(f"\nSample modified files (first 30):")
    for f in sorted(CHANGED_FILES)[:30]:
        print(f"  {f}")
    if len(CHANGED_FILES) > 30:
        print(f"  ... and {len(CHANGED_FILES) - 30} more")


if __name__ == '__main__':
    main()
