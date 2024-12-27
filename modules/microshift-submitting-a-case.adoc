// Module included in the following assemblies:
//
// * microshift_support/microshift-getting-support.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-support-submitting-a-case_{context}"]
= Submitting a support case

.Prerequisites

* The {microshift-short} service is running.
* You have installed the OpenShift CLI (`oc`).
* You have a Red Hat Customer Portal account.
* You have a Red Hat Standard or Premium subscription.

.Procedure

. Log in to link:https://access.redhat.com/support/cases/#/case/list[the *Customer Support* page] of the Red Hat Customer Portal.

. Click *Get support*.

. On the *Cases* tab of the *Customer Support* page:

.. Optional: Change the pre-filled account and owner details if needed.

.. Select the appropriate category for your issue, such as *Bug or Defect*, and click *Continue*.

. Enter the following information:

.. In the *Summary* field, enter a concise but descriptive problem summary and further details about the symptoms being experienced, as well as your expectations.

.. Select *{op-system-bundle}* from the *Product* drop-down menu.

.. Select *{rhde-version}* from the *Version* drop-down.

. Review the list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that is being reported. If the suggested articles do not address the issue, click *Continue*.

. Review the updated list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that is being reported. The list is refined as you provide more information during the case creation process. If the suggested articles do not address the issue, click *Continue*.

. Ensure that the account information presented is as expected, and if not, amend accordingly.

. Complete the following questions where prompted. Include which type of install type you are using, either RPM or embedded-image. Click *Continue*:
+
* What are you experiencing? What are you expecting to happen?
* Define the value or impact to you or the business.
* Where are you experiencing this behavior? What environment?
* When does this behavior occur? Frequency? Repeatedly? At certain times?

. Upload relevant diagnostic data files and click *Continue*. Include data gathered using the `sos` tool or etcd as a starting point, plus any issue-specific data that is not collected in those logs.

. Add relevant case management details and click *Continue*.

. Preview the case details and click *Submit*.
