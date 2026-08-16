////
This module included in the following assemblies:
* service_mesh/v2x/ossm-federation.adoc
////
:_mod-docs-content-type: PROCEDURE
[id="ossm-federation-config-importedserviceset-failover_{context}"]
= Configuring an ImportedServiceSet for failover

Locality-weighted load balancing allows administrators to control the distribution of traffic to endpoints based on the localities of where the traffic originates and where it will terminate. These localities are specified using arbitrary labels that designate a hierarchy of localities in {region}/{zone}/{sub-zone} form.

In the examples in this section, the `green-mesh` is located in the `us-east` region, and the `red-mesh` is located in the `us-west` region.

.Example `ImportedServiceSet` resource from red-mesh to green-mesh
[source,yaml]
----
kind: ImportedServiceSet
apiVersion: federation.maistra.io/v1
metadata:
  name: red-mesh #name of mesh that exported the service
  namespace: green-mesh-system #mesh namespace that service is being imported into
spec:
  importRules: # first matching rule is used
  # import ratings.bookinfo as ratings.bookinfo
  - type: NameSelector
    importAsLocal: true
    nameSelector:
      namespace: bookinfo
      name: ratings
      alias:
        # service will be imported as ratings.bookinfo.svc.red-mesh-imports.local
        namespace: bookinfo
        name: ratings
  #Locality within which imported services should be associated.
  locality:
    region: us-west
----

.`ImportedServiceLocality` fields table
|===
| Name | Description | Type

|region:
|Region within which imported services are located.
|string

|subzone:
|Subzone within which imported services are located.  I Subzone is specified, Zone must also be specified.
|string

|zone:
|Zone within which imported services are located.  If Zone is specified, Region must also be specified.
|string
|===


.Procedure

. Log in to the {product-title} CLI as a user with the `cluster-admin` role, enter the following command:
+
[source,terminal]
----
$ oc login --username=<NAMEOFUSER> <API token> https://<HOSTNAME>:6443
----
+
. Change to the project where you installed the {SMProductShortName} control plane, enter the following command:
+
[source,terminal]
----
$ oc project <smcp-system>
----
+
For example, `green-mesh-system`.
+
[source,terminal]
----
$ oc project green-mesh-system
----
+
.  Edit the `ImportedServiceSet` file, where `<ImportedServiceSet.yaml>` includes a full path to the file you want to edit, enter the following command:
+
[source,terminal]
----
$ oc edit -n <smcp-system> -f <ImportedServiceSet.yaml>
----
+
For example, if you want to modify the file that imports from the red-mesh-system to the green-mesh-system as shown in the previous `ImportedServiceSet` example.
+
[source,terminal]
----
$ oc edit -n green-mesh-system -f import-from-red-mesh.yaml
----
. Modify the file:
.. Set `spec.importRules.importAsLocal` to `true`.
.. Set `spec.locality` to a `region`, `zone`, or `subzone`.
.. Save your changes.
