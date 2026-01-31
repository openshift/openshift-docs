// Module included in the following assemblies:
//
//* authentication/configmaps.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-configmap-creating-from-literal-values_{context}"]
= Creating a config map from literal values

You can supply literal values for a config map.

The `--from-literal` option takes a `key=value` syntax, which allows literal values to be supplied directly on the command line.

.Procedure

* Create a config map by specifying a literal value:
+
[source,terminal]
----
$ oc create configmap special-config \
    --from-literal=special.how=very \
    --from-literal=special.type=charm
----

.Verification

* Enter the `oc get` command for the object with the `-o` option to see the values of the keys:
+
[source,terminal]
----
$ oc get configmaps special-config -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
data:
  special.how: very
  special.type: charm
kind: ConfigMap
metadata:
  creationTimestamp: 2016-02-18T19:14:38Z
  name: special-config
  namespace: default
  resourceVersion: "651"
  selflink: /api/v1/namespaces/default/configmaps/special-config
  uid: dadce046-d673-11e5-8cd0-68f728db1985
----
