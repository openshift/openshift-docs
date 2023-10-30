// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc

:_mod-docs-content-type: PROCEDURE
[id="security-context-constraints-psa-label_{context}"]
=  Configuring pod security admission for a namespace

You can configure the pod security admission settings at the namespace level. For each of the pod security admission modes on the namespace, you can set which pod security admission profile to use.

.Procedure

* For each pod security admission mode that you want to set on a namespace, run the following command:

+
[source,terminal]
----
$ oc label namespace <namespace> \                <1>
    pod-security.kubernetes.io/<mode>=<profile> \ <2>
    --overwrite
----
<1> Set `<namespace>` to the namespace to configure.
<2> Set `<mode>` to `enforce`, `warn`, or `audit`. Set `<profile>` to `restricted`, `baseline`, or `privileged`.
