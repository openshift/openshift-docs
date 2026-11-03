# Nav map vs topic map — cross-version roll-up

Modules referenced by `maps/ocp/navigation.adoc` but not by `_topic_maps/_topic_map.yml`,
per branch, after excluding JTBD-era modules. "Unique" means the module is not already
a finding on main.

* **main** — 40 findings (baseline; see `nav_modules_not_in_topic_map.md`)
* **enterprise-4.20** — 31 findings, 30 shared with main, **1 unique**
* **enterprise-4.21** — 33 findings, 33 shared with main, **0 unique**
* **enterprise-4.22** — 34 findings, 34 shared with main, **0 unique**
* **enterprise-5.0** — 282 findings, 40 shared with main, **242 unique**

## Unique findings by bucket

### enterprise-4.20 (1 unique)

* 1 — Only reachable via a commented-out include in a live assembly

### enterprise-4.21 (0 unique)

None.

### enterprise-4.22 (0 unique)

None.

### enterprise-5.0 (242 unique)

* 242 — Assembly's topic-map entry is commented out

## Scale of each branch

* enterprise-4.20: 6789 topic-map modules, 4140 nav modules, 889 wired job maps, 87 commented-out topic-map entries
* enterprise-4.21: 6815 topic-map modules, 4226 nav modules, 894 wired job maps, 87 commented-out topic-map entries
* enterprise-4.22: 7156 topic-map modules, 4355 nav modules, 900 wired job maps, 88 commented-out topic-map entries
* enterprise-5.0: 6792 topic-map modules, 4358 nav modules, 900 wired job maps, 142 commented-out topic-map entries
* main: 7168 topic-map modules, 4359 nav modules, 900 wired job maps, 90 commented-out topic-map entries

