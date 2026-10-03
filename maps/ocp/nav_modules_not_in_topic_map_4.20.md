# Modules in the nav map but not the topic map — unique to enterprise-4.20

Same comparison as `nav_modules_not_in_topic_map.md` (main), run against
`upstream/enterprise-4.20`, then filtered to drop every module that is already
a finding on main. What remains is specific to this branch.

## Method

* Topic map: 1767 `File:` entries (1753 unique) -> 1753 assemblies -> 6789 distinct modules.
* Nav map: 24 category maps -> 889 wired job maps -> 4140 distinct modules (962 job map files exist under `maps/ocp-jobs/`).
* Raw difference (nav minus topic map): 477 modules.
* Excluded as JTBD-era (adding commit is one of this branch's 38 commits touching `maps/ocp/` or `maps/ocp-jobs/`): 446.
* Findings on this branch: **31**
* Of those, already findings on main (dropped): **30**
* **Unique to enterprise-4.20: 1**

For reference: 10 of main's 40 findings do not appear on this branch at all.

4 shared module(s) land in a different bucket here than on main:
* `modules/monitoring-configuring-a-persistent-volume-claim.adoc` — main: `other-distro-only`, 4.20: `assembly-not-in-topic-map`
* `modules/monitoring-configuring-persistent-storage.adoc` — main: `other-distro-only`, 4.20: `assembly-not-in-topic-map`
* `modules/monitoring-modifying-retention-time-and-size-for-prometheus-metrics-data.adoc` — main: `other-distro-only`, 4.20: `assembly-not-in-topic-map`
* `modules/monitoring-resizing-a-persistent-volume.adoc` — main: `other-distro-only`, 4.20: `assembly-not-in-topic-map`

## Summary

* **1** — Only reachable via a commented-out include in a live assembly (`include-commented-out`)

## Only reachable via a commented-out include in a live assembly (1)

The including assembly is live in the OCP topic map, but the `include::` line for this module inside it is commented out.

### authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

* `modules/cco-short-term-creds-component-permissions-gcp.adoc`
  * nav category: secure
  * job map(s): manage-cloud-provider-credentials
  * added by: a8082d1aac Azure role granularity

