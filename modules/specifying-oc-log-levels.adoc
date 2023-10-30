// Module included in the following assemblies:
//
// * support/troubleshooting/diagnosing-oc-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="specifying-oc-log-levels_{context}"]
= Specifying OpenShift CLI (`oc`) log levels

You can investigate OpenShift CLI (`oc`) issues by increasing the command's log level.

The {product-title} user's current session token is typically included in logged `curl` requests where required. You can also obtain the current user's session token manually, for use when testing aspects of an `oc` command's underlying process step-by-step.

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

* Specify the `oc` log level when running an `oc` command:
+
[source,terminal]
----
$ oc <command> --loglevel <log_level>
----
+
where:
+
--
<command>:: Specifies the command you are running.
<log_level>:: Specifies the log level to apply to the command.
--

* To obtain the current user's session token, run the following command:
+
[source,terminal]
----
$ oc whoami -t
----
+
.Example output
[source,text]
----
sha256~RCV3Qcn7H-OEfqCGVI0CvnZ6...
----
