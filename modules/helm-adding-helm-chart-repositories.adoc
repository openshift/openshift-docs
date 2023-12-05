:_mod-docs-content-type: PROCEDURE
[id="adding-helm-chart-repositories_{context}"]
= Adding custom Helm chart repositories

As a cluster administrator, you can add custom Helm chart repositories to your cluster and enable access to the Helm charts from these repositories in the *Developer Catalog*.

.Procedure

. To add a new Helm Chart Repository, you must add the Helm Chart Repository custom resource (CR) to your cluster.
+
.Sample Helm Chart Repository CR

[source,yaml]
----
apiVersion: helm.openshift.io/v1beta1
kind: HelmChartRepository
metadata:
  name: <name>
spec:
 # optional name that might be used by console
 # name: <chart-display-name>
  connectionConfig:
    url: <helm-chart-repository-url>
----
+
For example, to add an Azure sample chart repository, run:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: helm.openshift.io/v1beta1
kind: HelmChartRepository
metadata:
  name: azure-sample-repo
spec:
  name: azure-sample-repo
  connectionConfig:
    url: https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs
EOF
----
+
. Navigate to  the *Developer Catalog* in the web console to verify that the Helm charts from the chart repository are displayed.
+
For example, use the *Chart repositories* filter to search for a Helm chart from the repository.
+
.Chart repositories filter
image::odc_helm_chart_repo_filter.png[]
+
[NOTE]
====
If a cluster administrator removes all of the chart repositories, then you cannot view the Helm option in the *+Add* view, *Developer Catalog*, and left navigation panel.
====
