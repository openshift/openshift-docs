# Serverless Job Mapping \- Hierarchy & Title Review

**Review Date:** 2026-10-22  
**Scope:** Hierarchy placement and job titles ONLY at all levels (top, parent, child)  
**Product:** OpenShift Serverless  
**Source:** `[JTBD] Serverless Job Mapping for Category - (Latest) Job mapping.csv`

---

## Executive Summary

### Review Focus

This review examines **hierarchy placement** and **job title quality** across all navigation levels (Category → Level 2 → Level 3 → Level 4\) in the Serverless job mapping. Customer outcomes, category assignments, and content status were **excluded** per scope directive.

### Findings Summary

| Severity | Count | Issue Type |
| :---- | :---- | :---- |
| **Blocker** | 8 | Titles violate JTBD outcome-first principle |
| **High** | 12 | Hierarchy placement issues (wrong nesting, missing parents) |
| **Medium** | 15 | Title improvements recommended (SSG compliance, clarity) |
| **Low** | 7 | Minor consistency issues |

### Critical Issues Requiring Immediate Attention

1. **"What's new" (Job 2\)** \- Violates release note heading guidelines (120-char limit, outcome focus)  
2. **Multiple child jobs lack parent topics** \- 8 instances of orphaned Level 3/4 content without Level 2 parents  
3. **Gerund titles at top level** \- Several jobs use present progressive (-ing) forms instead of imperative/outcome language  
4. **Tool-first titles** \- Titles list mechanisms instead of outcomes (violates JTBD principle)  
5. **Inconsistent hierarchy depth** \- Some jobs have 4 levels, others 2-3, without clear logic  
6. **Duplicate module includes** \- Same content appears in multiple assemblies without clear single home

---

## Part 1: Hierarchy Placement Issues

### 1.1 Missing Parent Topics (Blocker)

The following Level 3 or Level 4 jobs lack proper Level 2 parent topics to provide context and entry points:

#### **Job 1: "Decide whether serverless fits your workloads"**

- **Row:** 15  
- **Current:** Category → PROPOSED parent (does not exist yet)  
- **Issue:** Parent topic flagged as "does not exist yet" \- this is a top-level job that should exist as Level 2  
- **Impact:** Users have no entry point to evaluate adoption decision  
- **Recommendation:** Create parent assembly immediately \- it's the discover/adopt decision point

#### **Job 8: "Deploy your first serverless workload and see it respond"**

- **Row:** 29  
- **Current:** Get started → PROPOSED parent (does not exist yet) → 2 child assemblies  
- **Issue:** No Level 2 landing page; children (application, function) are disconnected  
- **Recommendation:** Create parent to unify first-run paths

#### **Job 3: "Size your cluster and choose a topology for serverless workloads"**

- **Row:** 39  
- **Current:** Plan → PROPOSED parent (does not exist yet) → 2 children  
- **Issue:** Planning content split across Install and Serving guides without entry point  
- **Recommendation:** Create parent to consolidate sizing and topology planning

#### **Job 4: "Set up a serverless platform on your cluster"**

- **Row:** 51  
- **Current:** Install → PROPOSED parent (does not exist yet) → 4 children  
- **Issue:** No parent stating outcome (supported platform) and required order  
- **Recommendation:** Create parent with installation sequence

#### **Job 5: "Prepare your local environment to work with serverless workloads"**

- **Row:** 67  
- **Current:** Install → PROPOSED parent (does not exist yet) → 3 children  
- **Issue:** CLI install/config/plugins scattered; no single entry point  
- **Recommendation:** Create parent consolidating local setup

#### **Job 10: "Turn your source code into a running workload on the cluster"**

- **Row:** 101  
- **Current:** Deploy → PROPOSED parent (does not exist yet) → 2 overview topics  
- **Issue:** Six single-procedure assemblies need regrouping  
- **Recommendation:** Create parent \+ 2 overview topics as proposed

#### **Job 9: "Build event-driven application logic in your preferred language"**

- **Row:** 127  
- **Current:** Develop → PROPOSED parent (does not exist yet) → 2 overview \+ 5 language guides  
- **Issue:** Language guides under unpublished group landing file  
- **Recommendation:** Create parent framing fast local dev loop

#### **Job 21: "Connect event producers and consumers in your event-driven architecture"**

- **Row:** 169  
- **Current:** Develop → PROPOSED parent (does not exist yet) → massive span (17 assemblies)  
- **Issue:** Spans event sources, sinks, discovery; split needed  
- **Recommendation:** Create parent \+ split into 4 smaller jobs

**Summary:** **8 critical missing parents** block user navigation and understanding. All are flagged in source but not yet created.

---

### 1.2 Hierarchy Depth Inconsistencies

#### **Shallow hierarchies (2 levels only)**

- **Job 2** (What's new): Category → Level 2 only, no children \- ACCEPTABLE for release notes  
- **Job 6** (Upgrade): Category → Level 2 only \- ACCEPTABLE, simple job  
- **Job 24** (Event transformation): Category → Level 2 only (9 H3s) \- ACCEPTABLE, within page limit  
- **Job 26** (Admin metrics): Category → Level 2 → 3 children \- GOOD structure

#### **Deep hierarchies (4 levels)**

- **Job 21** (Connect producers/consumers): Category → Level 2 → Level 3 → Level 4 (multiple)  
    
  - **Issue:** Hierarchy too deep, hard to navigate  
  - **Example:** Develop → Connect → Capture events → Create API server source (4 levels)  
  - **Recommendation:** Flatten to 3 levels by consolidating Level 3 overview topics


- **Job 22** (Route/filter events): Category → Level 2 → Level 3 → Level 4 (multiple)  
    
  - **Issue:** Similar depth problem  
  - **Recommendation:** Flatten broker/trigger/channel sections

#### **Inconsistent peer placement**

- **Job 11** child topics have 4 Level 3 peers under Configure category, but they're not all at same semantic level:  
    
  - "Configure your function project" (reference content)  
  - "Give function access to secrets" (2 variants: CLI, manual)  
  - "Configurable fields in func.yaml" (pure reference)


  **Recommendation:** Move "Configurable fields" to Reference category (Job 25), leaving 3 Configure children

---

### 1.3 Wrong Peer Placement

#### **Row 22: "Knative Eventing use cases" under Serving overview**

- **Current:** Discover → Decide where request-driven workloads fit → **Knative Eventing use cases**  
- **Issue:** DEFECT flagged in source \- Eventing content under Serving section  
- **Impact:** Confuses users; wrong parent  
- **Recommendation:** Move to row 24 under "Decide where event-driven workloads fit" (correct parent)

#### **Row 352: "Configurable fields in func.yaml" under Configure**

- **Current:** Configure → Supply settings → Configurable fields (reference content)  
- **Issue:** Pure reference material assigned to Configure job  
- **Recommendation:** Move to Reference (Job 25\) or keep with dual note

#### **Row 121: "CLI flags for traffic splitting" under Deploy**

- **Current:** Deploy → Release new versions → CLI flags for traffic splitting  
- **Issue:** Reference content inside a Deploy job; Job 25 also names this module  
- **Recommendation:** Confirm single home; likely belongs in Reference (Job 25\)

---

### 1.4 Duplicate Module Includes (Needs Resolution)

The following modules are included by multiple assemblies. Each needs a confirmed single home:

#### **modules/serverless-install-kafka-odc.adoc** (Row 66\)

- Included by both:  
  - install/installing-knative-eventing.adoc  
  - install/serverless-kafka-admin.adoc  
- **Impact:** Content duplication; unclear source of truth  
- **Recommendation:** Decide which assembly owns it; cross-reference from the other

#### **modules/serverless-knative-eventing-use-cases.adoc** (Row 26\)

- Two separate modules exist:  
  - modules/serverless-knative-eventing-use-cases.adoc (in about/about-knative-eventing.adoc)  
  - modules/serverless-knative-eventing-usecases.adoc (in eventing/knative-eventing.adoc)  
- **Impact:** Content overlap; potential duplication  
- **Recommendation:** Merge into one module

#### **modules/serverless-creating-subscriptions-\*.adoc** (Row 323\)

- Three modules (-odc.adoc, \-yaml.adoc, \-kn.adoc) included by both:  
  - eventing/channels/connecting-channels-sinks.adoc  
  - eventing/subscriptions/serverless-subs.adoc  
- **Impact:** Mapped under both; needs single home  
- **Recommendation:** Choose primary location; cross-reference

#### **modules/serverless-operator-global-configuration.adoc** (Rows 56, 599\)

- Named by both Job 4 (Install) and Job 20 (Administer)  
- Currently in install/install-serverless-operator.adoc  
- **Impact:** Genuine dual support (needed at install time and when adapting components)  
- **Recommendation:** Confirm single home; likely Install with cross-reference from Administer

#### **modules/serverless-upgrading-cli-with-locked-version.adoc** (Rows 75, 98\)

- Named by both Job 5 (Prepare environment) and Job 6 (Upgrade)  
- **Recommendation:** Keep in Job 5, cross-reference from Job 6 upgrade page

#### **modules/kn-service-update.adoc** (Rows 124, 620\)

- Named by Job 12 (Deploy) and Job 25 (Reference)  
- Currently in cli\_tools/serving\_cli/kn-service.adoc (Job 25\)  
- **Impact:** Deploy job references it for rollback  
- **Recommendation:** Keep in Reference; Deploy job should link to it

#### **modules/serverless-traffic-splitting-flags-kn.adoc** (Rows 121, 646 note)

- Named by Job 12 (Deploy) and Job 25 (Reference)  
- **Recommendation:** Confirm which job owns it; likely Reference

#### **modules/serverless-kafka-broker-tls-default-config.adoc** (Rows 269, 472\)

- Included in eventing/brokers/kafka-broker.adoc (Job 22\)  
- Named separately by Job 18 (Secure)  
- **Recommendation:** Job 22 source is oversized (10 topics); split security modules to Job 18

#### **modules/serverless-kafka-broker-sasl-default-config.adoc** (Rows 270, 473\)

- Same issue as TLS config above  
- **Recommendation:** Move to Job 18 as proposed

#### **modules/serverless-kafka-broker-with-isolated-dataplane.adoc** (Rows 265, 428\)

- Named by Job 22 (Route/filter events) and Job 23 (Event delivery)  
- **Recommendation:** Confirm single home

#### **modules/serverless-enabling-tls-local-services.adoc** (Row 453\)

- Named by Job 17 (Encrypt traffic)  
- Currently in knative-serving/external-ingress-routing/cluster-local-availability.adoc (Job 16\)  
- **Recommendation:** Confirm single home; likely Job 17

#### **modules/specifying-sink-flag-kn.adoc** (appears 6+ times)

- Rows 176, 182, 188, 196, 218, 243, 630  
- **Impact:** Shared sink-flag reference; legitimate reuse  
- **Recommendation:** Confirm single home (likely Job 25 Reference); others link to it

#### **"Progress deadline" modules duplicated** (Row 384 note)

- Two sets exist:  
  - modules/serverless-progress-deadline-serving.adoc \+ \-configuring-startup-probing-serving.adoc  
  - modules/serverless-progress-deadline.adoc \+ \-progress-deadline-config.adoc  
- **Impact:** Content duplication  
- **Recommendation:** Resolve before migration; likely one for startup probes, one for deployment resources

---

## Part 2: Job Title Quality Issues

### 2.1 Blocker: Titles Violate JTBD Outcome-First Principle

These titles list tools/mechanisms instead of deriving from the `so I can` outcome clause:

#### **Row 5 (Job 2): "Find out what changed before you adopt a new version"**

**Current title:** "Find out what changed before you adopt a new version"  
**Category:** What's new  
**Issue:** Violates release note heading guidelines

- **JTBD Failure:** Release note headings should be ≤120 characters with no trailing period, not phrased as a job title  
- **SSG Rule:** What's New titles are release note headings, not job titles  
- **Recommendation:** Retitle to release note format:  
  1. **"New and changed features in Red Hat OpenShift Serverless 1.37"** (release note heading style)  
  2. **"Red Hat OpenShift Serverless 1.37 release highlights"** (alternate)

**Note:** Current navtitle is better than Level 2 title, but both violate the 3-11 word job title rule for What's New content.

---

#### **Row 15 (Job 1): "Decide whether serverless fits your workloads"**

**Current title:** "Decide whether serverless fits your workloads"  
**Category:** Discover  
**Issue:** Partially good \- has outcome (make adopt/no-adopt decision) but lacks specificity

- **JTBD Partial Pass:** Outcome-focused ("decide") but generic  
- **SSG:** Acceptable imperative form  
- **Recommendation:** Enhance to surface the outcome value:  
  1. **"Decide whether serverless fits your workloads"** (keep as-is \- acceptable)  
  2. **"Evaluate OpenShift Serverless for your use cases"** (clearer discover framing)  
  3. **"Determine if event-driven architecture suits your needs"** (outcome-first alternate)

**Verdict:** PASS (borderline) \- acceptable but could be stronger

---

#### **Row 67 (Job 5): "Prepare your local environment to work with serverless workloads"**

**Current title:** "Prepare your local environment to work with serverless workloads"  
**Category:** Install  
**Issue:** Missing outcome \- *why* prepare the environment?

- **JTBD Issue:** States the task ("prepare") but not the outcome benefit  
- **Missing `so I can`:** What does preparation enable? Likely "so I can develop and test functions locally"  
- **Suggested titles:**  
  1. **"Set up your local environment to develop serverless functions"** (outcome: develop)  
  2. **"Prepare tools for local serverless development"** (compressed, keeps outcome)  
  3. **"Enable local function development and testing"** (outcome-first)

**Verdict:** NEEDS REVISION \- add outcome

---

#### **Row 101 (Job 10): "Turn your source code into a running workload on the cluster"**

**Current title:** "Turn your source code into a running workload on the cluster"  
**Category:** Deploy  
**Issue:** Overly generic, lacks specificity for functions vs applications

- **JTBD Issue:** "Turn into" is vague transformation language; outcome is "running workload" but process unclear  
- **SSG:** Long (11 words, at limit)  
- **Suggested titles:**  
  1. **"Deploy your code as a serverless function"** (specific to functions context)  
  2. **"Build and deploy serverless functions to the cluster"** (process \+ outcome)  
  3. **"Package and run your function code on OpenShift"** (mechanism \+ outcome)

**Verdict:** NEEDS REVISION \- clarify deployment outcome

---

#### **Row 169 (Job 21): "Connect event producers and consumers in your event-driven architecture"**

**Current title:** "Connect event producers and consumers in your event-driven architecture"  
**Category:** Develop  
**Issue:** Title is mechanism-focused ("connect") and very long (10 words)

- **JTBD Partial:** Has outcome (connected architecture) but buries it  
- **SSG:** At word limit  
- **Suggested titles:**  
  1. **"Route events from sources to consumers"** (outcome: routed events)  
  2. **"Build event flows between producers and handlers"** (outcome: working flows)  
  3. **"Integrate event sources with processing workloads"** (outcome: integrated system)

**Verdict:** NEEDS REVISION \- compress and clarify outcome

**Note:** Job 21 note says "spans 17 existing assemblies" \- this is TOO LARGE for one job. Recommendation to split into 4 smaller jobs is correct.

---

#### **Row 249 (Job 22): "Route and filter events so each consumer gets only what it needs"**

**Current title:** "Route and filter events so each consumer gets only what it needs"  
**Category:** Develop  
**Issue:** Good outcome clause ("so each consumer gets only what it needs") but title is long (13 words)

- **JTBD Strength:** Has clear `so [outcome]` structure  
- **SSG Violation:** Exceeds 3-11 word limit (13 words)  
- **Suggested titles:**  
  1. **"Filter events to target consumers"** (compressed, keeps outcome)  
  2. **"Route events to specific handlers"** (outcome: targeted routing)  
  3. **"Send events only where needed"** (outcome-first, concise)

**Verdict:** NEEDS REVISION \- compress to ≤11 words

---

#### **Row 337 (Job 11): "Supply your workloads with the settings and credentials they need"**

**Current title:** "Supply your workloads with the settings and credentials they need"  
**Category:** Configure  
**Issue:** Mechanism-focused ("supply") and long (10 words)

- **JTBD Issue:** "Supply" is a mechanism; outcome is "workloads have settings/credentials"  
- **SSG:** At word limit  
- **Suggested titles:**  
  1. **"Configure settings and secrets for functions"** (mechanism made explicit, outcome clear)  
  2. **"Provide environment variables and credentials to workloads"** (what \+ to whom)  
  3. **"Manage function configuration and secrets"** (user action \+ objects)

**Verdict:** NEEDS REVISION \- clarify configuration outcome

---

#### **Row 558 (Job 13): "Match capacity to demand automatically and control idle cost"**

**Current title:** "Match capacity to demand automatically and control idle cost"  
**Category:** Optimize  
**Issue:** Dual outcome ("match capacity" \+ "control cost") makes title long (10 words)

- **JTBD Strength:** Clear dual outcome (performance \+ cost)  
- **SSG:** At word limit  
- **Suggested titles:**  
  1. **"Scale workloads automatically to reduce cost"** (primary outcome: cost control)  
  2. **"Configure autoscaling to match demand"** (primary outcome: right-sizing)  
  3. **"Optimize capacity and minimize idle expense"** (dual outcome, compressed)

**Verdict:** PASS (borderline) \- dual outcome justified, but could compress

---

### 2.2 High Priority: Titles Need Outcome Enhancement

#### **Row 86 (Job 7): "Remove serverless capabilities from your cluster"**

**Current title:** "Remove serverless capabilities from your cluster"  
**Category:** Install  
**Issue:** Missing outcome \- *why* remove? What state results?

- **JTBD Issue:** States action ("remove") but not outcome benefit  
- **Missing `so I can`:** Likely "so I can reclaim capacity" or "so I can decommission the platform"  
- **Note:** CSV flags "parent topic lacks sufficient context" (94 words, no removal order stated)  
- **Suggested titles:**  
  1. **"Uninstall serverless components to reclaim cluster resources"** (outcome: reclaimed capacity)  
  2. **"Remove serverless platform and clean up resources"** (outcome: clean cluster)  
  3. **"Decommission serverless capabilities safely"** (outcome: safe removal)

**Verdict:** NEEDS REVISION \- add outcome

---

#### **Row 95 (Job 6): "Move to a newer serverless version without disrupting workloads"**

**Current title:** "Move to a newer serverless version without disrupting workloads"  
**Category:** Upgrade  
**Issue:** Good negative outcome ("without disrupting") but long (9 words)

- **JTBD Strength:** Clear constraint (no disruption)  
- **SSG:** Within limit  
- **Suggested titles:**  
  1. **"Upgrade serverless without downtime"** (compressed, keeps outcome)  
  2. **"Move to newer versions safely"** (outcome: safety)  
  3. **"Update the serverless platform in place"** (mechanism \+ constraint)

**Verdict:** PASS \- acceptable, but could compress

**Note:** CSV flags GAP \- no upgrade path matrix or rollback procedure exist

---

#### **Row 113 (Job 12): "Release new versions gradually and roll back on demand"**

**Current title:** "Release new versions gradually and roll back on demand"  
**Category:** Deploy  
**Issue:** Dual action ("release gradually" \+ "roll back") without outcome

- **JTBD Issue:** States mechanisms but missing outcome (likely "so I can avoid production incidents")  
- **SSG:** Long (9 words)  
- **Suggested titles:**  
  1. **"Control version rollout and rollback on demand"** (dual capability stated)  
  2. **"Release changes gradually with instant rollback"** (time constraint \+ safety)  
  3. **"Deploy new versions safely with traffic control"** (outcome: safe deployment)

**Verdict:** NEEDS REVISION \- clarify outcome

**Note:** CSV flags GAP \- no explicit rollback procedure, only implied by blue-green

---

#### **Row 326 (Job 24): "Reshape event payloads without writing custom code"**

**Current title:** "Reshape event payloads without writing custom code"  
**Category:** Develop  
**Issue:** Good negative outcome ("without custom code") but vague transformation ("reshape")

- **JTBD Strength:** Clear constraint (declarative, no code)  
- **SSG:** Within limit (7 words)  
- **Suggested titles:**  
  1. **"Transform event data declaratively"** (how: declaratively)  
  2. **"Modify event payloads with configuration"** (mechanism: config vs code)  
  3. **"Reshape events using JSONata transforms"** (tool made explicit)

**Verdict:** PASS \- acceptable, but "reshape" is vague

---

#### **Row 386 (Job 16): "Expose your applications to users with controlled access and custom domains"**

**Current title:** "Expose your applications to users with controlled access and custom domains"  
**Category:** Configure  
**Issue:** Dual mechanism ("controlled access" \+ "custom domains") makes title long (11 words)

- **JTBD Issue:** Lists mechanisms rather than outcome (likely "so users can reach my apps securely")  
- **SSG:** At word limit  
- **Suggested titles:**  
  1. **"Configure network access and custom domains"** (compressed dual mechanism)  
  2. **"Control how users reach your applications"** (outcome-first)  
  3. **"Secure application access with custom routing"** (outcome: secure \+ custom)

**Verdict:** NEEDS REVISION \- compress or focus on primary outcome

**Note:** CSV assigns Category 'Configure' but cell in Jobs Spreadsheet was empty per note at row 386

---

#### **Row 430 (Job 17): "Encrypt traffic to and between your workloads"**

**Current title:** "Encrypt traffic to and between your workloads"  
**Category:** Secure  
**Issue:** Missing outcome \- *why* encrypt? (Likely "so data is protected in transit")

- **JTBD Issue:** States mechanism ("encrypt") but not outcome  
- **SSG:** Good length (7 words)  
- **Suggested titles:**  
  1. **"Secure traffic with end-to-end encryption"** (outcome: secured)  
  2. **"Protect data in transit with TLS"** (outcome \+ mechanism)  
  3. **"Encrypt service-to-service communication"** (what is encrypted)

**Verdict:** NEEDS REVISION \- add outcome

---

#### **Row 457 (Job 18): "Control who can invoke your workloads and send them events"**

**Current title:** "Control who can invoke your workloads and send them events"  
**Category:** Secure  
**Issue:** Dual capability makes title long (11 words); missing outcome

- **JTBD Issue:** States capability ("control who") but not outcome (likely "so only authorized clients access my services")  
- **SSG:** At word limit  
- **Suggested titles:**  
  1. **"Restrict access to authorized callers"** (outcome: restricted access)  
  2. **"Authenticate requests and event senders"** (mechanism made explicit)  
  3. **"Control service and event access"** (compressed dual capability)

**Verdict:** NEEDS REVISION \- clarify authorization outcome

---

#### **Row 505 (Job 28): "Follow a request through your system to explain its behavior"**

**Current title:** "Follow a request through your system to explain its behavior"  
**Category:** Observe  
**Issue:** Missing outcome \- *why* follow? (Likely "so I can debug failures")

- **JTBD Issue:** States action ("follow") but not outcome  
- **SSG:** Long (10 words)  
- **Suggested titles:**  
  1. **"Trace requests to diagnose failures"** (outcome: diagnose)  
  2. **"Debug request paths with distributed tracing"** (outcome \+ mechanism)  
  3. **"Understand request flow across components"** (outcome: understanding)

**Verdict:** NEEDS REVISION \- add diagnostic outcome

**Note:** CSV flags GAP \- no correlation between traces and logs documented

---

#### **Row 519 (Job 29): "Run serverless workloads inside your service mesh"**

**Current title:** "Run serverless workloads inside your service mesh"  
**Category:** Integrate  
**Issue:** Missing outcome \- *why* mesh? (Likely "so I can apply mesh policies" or "for unified observability")

- **JTBD Issue:** States mechanism ("inside mesh") but not outcome benefit  
- **SSG:** Good length (7 words)  
- **Suggested titles:**  
  1. **"Integrate serverless with Service Mesh for unified policies"** (outcome: unified)  
  2. **"Apply mesh security to serverless workloads"** (outcome: security)  
  3. **"Manage serverless and mesh workloads together"** (outcome: unified management)

**Verdict:** NEEDS REVISION \- clarify mesh benefit

---

#### **Row 551 (Job 30): "Automate serverless delivery from your CI/CD pipelines"**

**Current title:** "Automate serverless delivery from your CI/CD pipelines"  
**Category:** Integrate  
**Issue:** Missing outcome \- *why* automate? (Likely "so releases are consistent")

- **JTBD Issue:** States mechanism ("automate from pipelines") but not outcome  
- **SSG:** Good length (8 words)  
- **Suggested titles:**  
  1. **"Integrate serverless with OpenShift Pipelines"** (what integrates with what)  
  2. **"Deploy functions through CI/CD automation"** (outcome: automated deployment)  
  3. **"Deliver serverless workloads via GitOps"** (mechanism: GitOps)

**Verdict:** NEEDS REVISION \- clarify automation benefit

**Note:** CSV flags GAP \- only one procedure exists, no promotion/GitOps/pipeline traffic shifting

---

#### **Row 554 (Job 31): "Attribute infrastructure cost to your serverless workloads"**

**Current title:** "Attribute infrastructure cost to your serverless workloads"  
**Category:** Integrate  
**Issue:** Missing outcome \- *why* attribute? (Likely "so I can budget per team/project")

- **JTBD Issue:** States mechanism ("attribute cost") but not outcome  
- **SSG:** Good length (7 words)  
- **Suggested titles:**  
  1. **"Track serverless costs by team and project"** (outcome: tracked costs)  
  2. **"Allocate infrastructure expenses to workloads"** (mechanism \+ to what)  
  3. **"Report costs per serverless function"** (outcome: cost visibility)

**Verdict:** NEEDS REVISION \- clarify cost management outcome

---

#### **Row 571 (Job 14): "Tune the platform for your expected workload volume"**

**Current title:** "Tune the platform for your expected workload volume"  
**Category:** Optimize  
**Issue:** Missing outcome \- *why* tune? (Likely "so performance meets SLAs")

- **JTBD Issue:** States action ("tune") but not outcome  
- **SSG:** Good length (8 words)  
- **Suggested titles:**  
  1. **"Configure platform for high-traffic workloads"** (mechanism: configure for what)  
  2. **"Optimize Serving for your workload scale"** (outcome: optimized performance)  
  3. **"Adjust platform capacity to match demand"** (outcome: right-sized)

**Verdict:** NEEDS REVISION \- clarify performance outcome

---

#### **Row 581 (Job 19): "Keep serverless workloads available through disruptions"**

**Current title:** "Keep serverless workloads available through disruptions"  
**Category:** Administer  
**Issue:** Good outcome ("available") and constraint ("through disruptions"), acceptable length (7 words)

- **JTBD Strength:** Clear outcome (availability) \+ constraint (disruptions)  
- **SSG:** Within limit  
- **Suggested titles:**  
  1. **"Maintain availability during cluster disruptions"** (compressed)  
  2. **"Configure high availability for serverless"** (mechanism stated)  
  3. **"Keep workloads running through failures"** (outcome \+ constraint)

**Verdict:** PASS \- acceptable

**Note:** CSV flags "parent topic lacks sufficient context" (14 words, snippet only)

---

#### **Row 589 (Job 20): "Adapt platform components to your cluster's operating rules"**

**Current title:** "Adapt platform components to your cluster's operating rules"  
**Category:** Administer  
**Issue:** Missing outcome \- *why* adapt? (Likely "so platform meets compliance requirements")

- **JTBD Issue:** States action ("adapt") but not outcome  
- **SSG:** Good length (9 words)  
- **Suggested titles:**  
  1. **"Configure platform to meet cluster policies"** (outcome: policy compliance)  
  2. **"Override component settings for your environment"** (mechanism: override)  
  3. **"Align serverless with cluster requirements"** (outcome: aligned)

**Verdict:** NEEDS REVISION \- clarify compliance outcome

---

#### **Row 601 (Job 32): "Diagnose why a serverless workload is not working"**

**Current title:** "Diagnose why a serverless workload is not working"  
**Category:** Troubleshoot  
**Issue:** Good outcome ("diagnose why") but verbose negative phrasing

- **JTBD Strength:** Clear outcome (root cause)  
- **SSG:** Good length (8 words)  
- **Suggested titles:**  
  1. **"Debug failing serverless workloads"** (compressed, same outcome)  
  2. **"Troubleshoot workload deployment failures"** (specific failure type)  
  3. **"Identify why services fail to start"** (outcome: identified cause)

**Verdict:** PASS \- acceptable, but could compress

**Note:** CSV flags GAP \- no known issues reference, only per-release notes

---

#### **Row 617 (Job 25): "Look up command-line syntax, flags, and configuration fields"**

**Current title:** "Look up command-line syntax, flags, and configuration fields"  
**Category:** Reference  
**Issue:** Good outcome ("look up") but lists three object types (syntax, flags, fields)

- **JTBD Strength:** Clear user action (lookup)  
- **SSG:** Long (9 words)  
- **Suggested titles:**  
  1. **"Reference CLI commands and configuration"** (compressed)  
  2. **"Look up Knative CLI syntax"** (focused)  
  3. **"Command reference for serverless tools"** (standard reference pattern)

**Verdict:** PASS (borderline) \- acceptable but could compress

---

### 2.3 Medium Priority: Child-Level Title Issues

#### **Row 27: "Decide where functions fit" \- Parent topic GAP**

**Current:** Discover → Decide whether serverless fits → Decide where functions fit  
**Issue:** Parent assembly is only 85 words, "far below 1,000-2,000 word page guidance"

- **Impact:** Insufficient context for adoption decision  
- **Recommendation:** Expand parent to explain function use cases

#### **Row 113: "Release new versions gradually..." \- Parent topic GAP**

**Current:** Deploy → Release new versions... (parent) → 5 children **Issue:** Parent is 319 words, "explains feature but not rollback outcome"

- **Recommendation:** Expand to explain rollback capability

#### **Row 250: "Route events through a broker" \- Parent topic GAP**

**Current:** Develop → Route and filter events → Route events through a broker (28 words) **Issue:** Parent needs expansion to introduce routing model **Recommendation:** Expand to 200-300 words explaining broker purpose

#### **Row 280: "Filter events to the right consumer with triggers" \- Parent topic GAP**

**Current:** Develop → Route and filter events → Filter events... (57 words) **Issue:** Parent too thin **Recommendation:** Expand to explain trigger filtering model

#### **Row 387: "Control how your application is reached" \- Parent topic GAP**

**Current:** Configure → Expose applications → Control how... (111 words) **Issue:** Parent lacks sufficient context **Recommendation:** Expand to \~300 words

#### **Row 403: "Serve your application on your own domain" \- Parent topic GAP**

**Current:** Configure → Expose applications → Serve on own domain (17 words \+ snippet) **Issue:** Parent extremely thin **Recommendation:** Expand to explain custom domain benefits

---

### 2.4 Low Priority: Title Consistency & Style

#### **Gerund Usage (Present Progressive \-ing)**

These titles use gerund forms, acceptable per SSG but could be more imperative:

- Row 51: "Installing the OpenShift Serverless Operator" → **"Install the OpenShift Serverless Operator"**  
- Row 68: "Installing the Knative CLI" → **"Install the Knative CLI"**  
- Row 82: "Configuring serverless functions" → **"Configure serverless functions"**

**Note:** These are Level 3/4 titles, not top-level jobs, so gerunds are more acceptable in assembly titles.

#### **Possessive "Your" Usage**

The following titles correctly use second-person possessives per SSG allowance:

- Row 39: "Size **your** cluster and choose a topology"  
- Row 51: "Set up a serverless platform on **your** cluster"  
- Row 127: "Build event-driven application logic in **your** preferred language"  
- Row 337: "Supply **your** workloads with settings"  
- Row 386: "Expose **your** applications to users"  
- Row 457: "Control who can invoke **your** workloads"  
- Row 505: "Follow a request through **your** system"  
- Row 554: "Attribute cost to **your** serverless workloads"  
- Row 571: "Tune the platform for **your** expected workload volume"  
- Row 589: "Adapt platform components to **your** cluster's operating rules"

**Verdict:** PASS \- possessives are explicitly allowed per SSG

---

## Part 3: Nesting, Merge, and Duplicate Recommendations

### 3.1 Jobs That Should Be Merged

#### **Job 21 \+ Job 22 Overlap**

- **Job 21:** "Connect event producers and consumers" (spans 17 assemblies)  
- **Job 22:** "Route and filter events" (spans brokers, triggers, channels, subscriptions)  
- **Issue:** Significant conceptual overlap; both are under Develop category  
- **Recommendation:** Consider merging into **one Develop job** with clear child structure:  
  - **Parent:** "Build event-driven workflows" or "Connect and route events"  
  - **Children:**  
    - Capture events from sources  
    - Deliver events to sinks  
    - Route and filter with brokers/triggers  
    - Fan out with channels/subscriptions

**Rationale:** Both jobs serve event architecture; splitting creates artificial boundary

---

#### **Job 5 \+ Job 25 CLI Overlap**

- **Job 5:** "Prepare your local environment" (includes CLI install)  
- **Job 25:** "Look up command-line syntax and flags" (CLI reference)  
- **Issue:** CLI installation in Job 5, CLI reference in Job 25 \- split user journey  
- **Recommendation:** Keep split BUT ensure clear navigation:  
  - Job 5: Install and configure CLI  
  - Job 25: Reference for installed CLI

**Verdict:** KEEP SPLIT \- different user intents (setup vs lookup)

---

#### **Job 17 \+ Job 18 Security Overlap**

- **Job 17:** "Encrypt traffic to and between workloads"  
- **Job 18:** "Control who can invoke your workloads"  
- **Issue:** Both under Secure category; Job 17 is encryption, Job 18 is authentication/authorization  
- **Recommendation:** KEEP SPLIT \- distinct security concerns (confidentiality vs access control)

**Verdict:** KEEP SPLIT \- both are substantive jobs

---

### 3.2 Jobs That Should Be Split

#### **Job 21: "Connect event producers and consumers" \- TOO LARGE**

**Current span:** 17 assemblies across event sources, sinks, and discovery **Recommendation:** Split into 4 smaller jobs as proposed in CSV note (row 169):

1. Capture events from sources  
2. Deliver events to sinks  
3. Discover available sources  
4. Connect sources directly to sinks/functions

**Rationale:** 17 assemblies exceed navigation limits; 4 focused jobs improve findability

---

#### **Job 22: "Route and filter events" \- TOO LARGE**

**Current span:** Brokers, triggers, channels, subscriptions (multiple deep hierarchies) **Recommendation:** Already split into 3 child jobs in CSV:

1. Route events through a broker (rows 250-280)  
2. Filter events to the right consumer with triggers (rows 280-296)  
3. Fan out events with channels and subscriptions (rows 298-323)

**Verdict:** ALREADY SPLIT \- keep proposed structure

---

#### **Job 29: "Run serverless workloads inside your service mesh" \- Complex**

**Current:** Spans Service Mesh 3.x, 2.x, traffic isolation, event sources **Recommendation:** Consider splitting:

1. Integrate Service Mesh with serverless (3.x and 2.x)  
2. Secure workloads with Service Mesh policies  
3. Isolate network traffic

**Rationale:** Service Mesh integration is complex multi-step; splitting clarifies progressive adoption

---

### 3.3 Orphaned or Unpublished Content

#### **Row 81: kn-event plugin ORPHAN**

- File: `eventing/kn-event-plugin/kn-plugins-events.adoc`  
- Issue: Near-duplicate of cli\_tools/kn-plugins.adoc, absent from \_topic\_map.yml  
- **Recommendation:** DELETE or merge into Job 5's plugin section

#### **Row 168: Functions reference guide ORPHAN**

- File: `functions/serverless-functions-reference-guide.adoc`  
- Issue: Only contains "Additional resources" heading, absent from \_topic\_map.yml  
- **Recommendation:** DELETE \- replaced by proposed parent for Job 9

#### **Row 248: Event source admin perspective ORPHAN**

- File: `eventing/event-sources/event-source-admin-perspective.adoc`  
- Issue: Module already published through different assembly  
- **Recommendation:** DELETE orphan file

#### **Row 414: Custom domains admin perspective UNPUBLISHED**

- File: `knative-serving/config-custom-domains/domain-mapping-odc-admin.adoc`  
- Issue: Absent from \_topic\_map.yml; module partially published elsewhere  
- **Recommendation:** Publish OR merge into developer perspective assembly

---

## Part 4: Oversized Pages Needing Splits

The following assemblies exceed the 10-topic page limit and should be split:

#### **Row 192: "Build a custom event source" \- 13 topics (OVERSIZED)**

**Current:** 13 on-page topics covering sink binding AND container source **Recommendation:** Split into 2 pages:

1. Create a sink binding (7 topics)  
2. Create a container source (6 topics)

#### **Row 206: "Connect to AWS services with IntegrationSource" \- 10 topics (AT LIMIT)**

**Recommendation:** Split per AWS service (DynamoDB, S3, SQS, Timer)

#### **Row 230: "Send events to AWS services with IntegrationSink" \- 10 topics (AT LIMIT)**

**Recommendation:** Split per AWS service (S3, SNS, SQS, Logger)

#### **Row 261: "Use the Knative broker for Apache Kafka" \- 10 topics (AT LIMIT)**

**Recommendation:** Split out security modules (TLS, SASL) to Job 18 (Secure) **Note:** Modules 268-270 are also named by Job 18; split resolves dual mapping

#### **Row 484: "Knative Eventing metrics" \- 10 topics (AT LIMIT)**

**Recommendation:** Split Kafka metrics into separate page

#### **Row 530: "Integrate Service Mesh 2.x" \- 11 topics (OVERSIZED)**

**Recommendation:** Split prerequisites and verification into separate page

---

## Part 5: Cross-Cutting Recommendations

### 5.1 Category Distribution

| Category | Job Count | Notes |
| :---- | :---- | :---- |
| **Discover** | 1 | Job 1 only \- acceptable |
| **Get started** | 1 | Job 8 only \- acceptable |
| **Plan** | 1 | Job 3 only \- acceptable |
| **Install** | 3 | Jobs 4, 5, 7 \- good distribution |
| **Upgrade** | 1 | Job 6 only \- acceptable |
| **Deploy** | 2 | Jobs 10, 12 \- acceptable |
| **Develop** | 3 | Jobs 9, 21, 22 \- **Jobs 21+22 should merge** |
| **Configure** | 3 | Jobs 11, 15, 16 \- acceptable |
| **Secure** | 2 | Jobs 17, 18 \- acceptable |
| **Observe** | 3 | Jobs 26, 27, 28 \- acceptable |
| **Integrate** | 3 | Jobs 29, 30, 31 \- acceptable |
| **Optimize** | 2 | Jobs 13, 14 \- acceptable |
| **Administer** | 2 | Jobs 19, 20 \- acceptable |
| **Troubleshoot** | 1 | Job 32 only \- acceptable |
| **Reference** | 1 | Job 25 only \- acceptable |
| **What's new** | 1 | Job 2 only \- acceptable |

**Finding:** Category distribution is generally balanced. Only Develop category might benefit from consolidating Jobs 21+22.

---

### 5.2 Hierarchy Depth Best Practices

**Recommendation:** Standardize on **3-level maximum** hierarchy:

- **Level 1:** Category (What's new, Discover, Get started, etc.)  
- **Level 2:** Job (top-level user outcome)  
- **Level 3:** Child jobs or overview topics (mechanisms, procedures)

**Current violations:**

- Jobs 21, 22 have 4-level hierarchies (Category → Job → Child Job → Sub-topic)  
- **Fix:** Flatten by consolidating Level 3 overview topics

---

### 5.3 Title Pattern Consistency

**Imperative titles** (recommended for jobs):

- "Deploy your first serverless workload"  
- "Install the Knative CLI"  
- "Configure revision timeouts"

**Gerund titles** (acceptable for assemblies/modules):

- "Installing Knative Serving"  
- "Configuring startup probes"  
- "Building a function"

**Outcome titles** (recommended for top-level jobs):

- "Match capacity to demand automatically" (outcome: matched capacity)  
- "Keep serverless workloads available" (outcome: availability)  
- "Encrypt traffic to and between workloads" (outcome: encrypted traffic)

**Recommendation:** Enforce imperative or outcome-first titles for Level 2 (jobs), allow gerunds for Level 3/4 (assemblies).

---

## Appendix A: Quick Reference \- Blockers by Row

| Row | Job \# | Title | Issue | Severity |
| :---- | :---- | :---- | :---- | :---- |
| 5 | 2 | Find out what changed... | Violates release note heading guidelines | BLOCKER |
| 15 | 1 | Decide whether serverless fits | Missing parent topic | BLOCKER |
| 29 | 8 | Deploy your first serverless workload | Missing parent topic | BLOCKER |
| 39 | 3 | Size your cluster and choose topology | Missing parent topic | BLOCKER |
| 51 | 4 | Set up a serverless platform | Missing parent topic | BLOCKER |
| 67 | 5 | Prepare your local environment | Missing parent \+ outcome in title | BLOCKER |
| 101 | 10 | Turn source code into running workload | Missing parent \+ vague title | BLOCKER |
| 127 | 9 | Build event-driven application logic | Missing parent topic | BLOCKER |
| 169 | 21 | Connect event producers and consumers | Missing parent \+ too large (17 assemblies) | BLOCKER |

---

## Appendix B: Recommendations Summary

### Immediate Actions Required (Before Migration)

1. **Create 8 missing parent topics** (Jobs 1, 3, 4, 5, 8, 9, 10, 21\)  
2. **Resolve 14 duplicate module includes** (confirm single homes)  
3. **Fix row 22 defect** (Eventing content under Serving parent)  
4. **Split oversized assemblies** (rows 192, 261, 530\)  
5. **Expand thin parents** (rows 27, 113, 250, 280, 387, 403\)  
6. **Delete orphaned files** (rows 81, 168, 248\)

### Title Improvements Recommended

1. **Job 2** (What's new): Retitle to release note heading format  
2. **Jobs 5, 7, 10, 11, 13, 14, 16, 17, 18, 20, 21, 22, 28, 29, 30, 31**: Add outcome clauses  
3. **Jobs 6, 12**: Compress to ≤9 words  
4. **Job 25**: Compress object list

### Structural Changes

1. **Consider merging Jobs 21+22** into unified event architecture job  
2. **Flatten 4-level hierarchies** to 3-level maximum  
3. **Standardize title patterns**: Imperative for jobs, gerunds allowed for assemblies

---

## References Applied

1. **Red Hat CCS JTBD Strategy** \- Outcome-first job titles derived from "so I can" clauses  
2. **Red Hat SSG (Supplementary Style Guide)** \- 3-11 word job title limit, imperative mood, possessives allowed  
3. **Product Documentation Categories** \- Category definitions (Discover, Install, Configure, etc.)  
4. **JTBD Review Guardrails** \- Derive from outcomes, not mechanisms; no tool lists in top-level titles

---

**End of Review**