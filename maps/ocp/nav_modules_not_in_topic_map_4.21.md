# Modules in the nav map but not the topic map — unique to enterprise-4.21

Same comparison as `nav_modules_not_in_topic_map.md` (main), run against
`upstream/enterprise-4.21`, then filtered to drop every module that is already
a finding on main. What remains is specific to this branch.

## Method

* Topic map: 1778 `File:` entries (1764 unique) -> 1764 assemblies -> 6815 distinct modules.
* Nav map: 24 category maps -> 894 wired job maps -> 4226 distinct modules (966 job map files exist under `maps/ocp-jobs/`).
* Raw difference (nav minus topic map): 484 modules.
* Excluded as JTBD-era (adding commit is one of this branch's 36 commits touching `maps/ocp/` or `maps/ocp-jobs/`): 451.
* Findings on this branch: **33**
* Of those, already findings on main (dropped): **33**
* **Unique to enterprise-4.21: 0**

For reference: 7 of main's 40 findings do not appear on this branch at all.

## Summary

No findings unique to this branch. Everything the nav map references but the
topic map does not is also a finding on main.
