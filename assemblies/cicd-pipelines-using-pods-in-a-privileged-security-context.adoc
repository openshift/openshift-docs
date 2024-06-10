:_mod-docs-content-type: ASSEMBLY
[id="using-pods-in-a-privileged-security-context"]
= Using pods in a privileged security context
include::_attributes/common-attributes.adoc[]
:context: using-pods-in-a-privileged-security-context

toc::[]

The default configuration of {pipelines-shortname} 1.3.x and later versions does not allow you to run pods with privileged security context, if the pods result from pipeline run or task run.
For such pods, the default service account is `pipeline`, and the security context constraint (SCC) associated with the `pipeline` service account is `pipelines-scc`. The `pipelines-scc` SCC is similar to the `anyuid` SCC, but with minor differences as defined in the YAML file for the SCC of pipelines:

.Example `pipelines-scc.yaml` snippet
[source,yaml,subs="attributes+"]
----
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
...
allowedCapabilities:
  - SETFCAP
...
fsGroup:
  type: MustRunAs
...
----

In addition, the `Buildah` cluster task, shipped as part of the {pipelines-shortname}, uses `vfs` as the default storage driver.

include::modules/op-running-pipeline-and-task-run-pods-with-privileged-security-context.adoc[leveloffset=+1]

include::modules/op-running-pipeline-run-and-task-run-with-custom-scc-and-service-account.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-references_using-pods-in-a-privileged-security-context"]
== Additional resources

* For information on managing SCCs, refer to xref:../../authentication/managing-security-context-constraints.adoc[Managing security context constraints].
