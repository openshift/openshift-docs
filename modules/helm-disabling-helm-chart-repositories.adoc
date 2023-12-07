:_mod-docs-content-type: PROCEDURE
[id="helm-disabling-helm-chart-repositories_{context}"]
= Disabling Helm Chart repositories

You can disable Helm Charts from a particular Helm Chart Repository in the catalog by setting the `disabled` property in the `HelmChartRepository` custom resource to `true`.

.Procedure

* To disable a Helm Chart repository by using CLI, add the `disabled: true` flag to the custom resource. For example, to remove an Azure sample chart repository, run:
+
----
$ cat <<EOF | oc apply -f -
apiVersion: helm.openshift.io/v1beta1
kind: HelmChartRepository
metadata:
  name: azure-sample-repo
spec:
  connectionConfig:
   url:https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs
  disabled: true
EOF
----

*  To disable a recently added Helm Chart repository by using Web Console:
+
. Go to *Custom Resource Definitions* and search for the `HelmChartRepository` custom resource.

. Go to *Instances*, find the repository you want to disable, and click its name.

. Go to the *YAML* tab, add the `disabled: true` flag in the `spec` section, and click `Save`.
+
.Example
----
spec:
  connectionConfig:
    url: <url-of-the-repositoru-to-be-disabled>
  disabled: true
----
+
The repository is now disabled and will not appear in the catalog.
