// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-complying-with-psa.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-ensuring-operator-workloads-run-restricted-psa_{context}"]
= Ensuring Operator workloads run in namespaces set to the restricted pod security level

To ensure your Operator project can run on a wide variety of deployments and environments, configure the Operator's workloads to run in namespaces set to the `restricted` pod security level.

[WARNING]
====
You must leave the `runAsUser` field empty. If your image requires a specific user, it cannot be run under restricted security context constraints (SCC) and restricted pod security enforcement.
====

.Procedure

* To configure Operator workloads to run in namespaces set to the `restricted` pod security level, edit your Operator's namespace definition similar to the following examples:
+
[IMPORTANT]
====
It is recommended that you set the seccomp profile in your Operator's namespace definition. However, setting the seccomp profile is not supported in {product-title} 4.10.
====

** For Operator projects that must run in only {product-title} 4.11 and later, edit your Operator's namespace definition similar to the following example:
+
.Example `config/manager/manager.yaml` file
[source,yaml]
----
...
spec:
 securityContext:
   seccompProfile:
     type: RuntimeDefault <1>
   runAsNonRoot: true
 containers:
   - name: <operator_workload_container>
     securityContext:
       allowPrivilegeEscalation: false
       capabilities:
         drop:
           - ALL
...
----
<1> By setting the seccomp profile type to `RuntimeDefault`, the SCC defaults to the pod security profile of the namespace.

** For Operator projects that must also run in {product-title} 4.10, edit your Operator's namespace definition similar to the following example:
+
.Example `config/manager/manager.yaml` file
[source,yaml]
----
...
spec:
 securityContext: <1>
   runAsNonRoot: true
 containers:
   - name: <operator_workload_container>
     securityContext:
       allowPrivilegeEscalation: false
       capabilities:
         drop:
           - ALL
...
----
<1> Leaving the seccomp profile type unset ensures your Operator project can run in {product-title} 4.10.
