# Modules in the nav map but not the topic map — unique to enterprise-4.22

Same comparison as `nav_modules_not_in_topic_map.md` (main), run against
`upstream/enterprise-4.22`, then filtered to drop every module that is already
a finding on main. What remains is specific to this branch.

## Method

* Topic map: 1819 `File:` entries (1805 unique) -> 1805 assemblies -> 7156 distinct modules.
* Nav map: 24 category maps -> 900 wired job maps -> 4355 distinct modules (971 job map files exist under `maps/ocp-jobs/`).
* Raw difference (nav minus topic map): 486 modules.
* Excluded as JTBD-era (adding commit is one of this branch's 32 commits touching `maps/ocp/` or `maps/ocp-jobs/`): 452.
* Findings on this branch: **34**
* Of those, already findings on main (dropped): **34**
* **Unique to enterprise-4.22: 0**

For reference: 6 of main's 40 findings do not appear on this branch at all.

## Summary

No findings unique to this branch. Everything the nav map references but the
topic map does not is also a finding on main.
