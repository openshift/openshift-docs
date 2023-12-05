:_mod-docs-content-type: ASSEMBLY
[id="using-devfiles-in-odo"]
= Using devfiles in {odo-title}
include::_attributes/common-attributes.adoc[]
:context: creating-applications-by-using-devfiles

toc::[]

include::modules/developer-cli-odo-about-devfiles-in-odo.adoc[leveloffset=+1]

== Creating a Java application by using a devfile

.Prerequisites

* You have installed `{odo-title}`.
* You must know your ingress domain cluster name. Contact your cluster administrator if you do not know it. For example, `apps-crc.testing` is the cluster domain name for https://access.redhat.com/documentation/en-us/red_hat_openshift_local/[{openshift-local-productname}].

[NOTE]
====
Currently odo does not support creating devfile components with `--git` or `--binary` flags. You can only create S2I components when using these flags.
====

include::modules/developer-cli-odo-creating-a-project.adoc[leveloffset=+2]

include::modules/developer-cli-odo-listing-available-devfile-components.adoc[leveloffset=+2]

include::modules/developer-cli-odo-deploying-a-java-application-using-a-devfile.adoc[leveloffset=+2]

include::modules/developer-cli-odo-converting-an-s2i-component-into-a-devfile-component.adoc[leveloffset=+1]
