// Module included in the following assemblies:
//
// * TBD


[id="configuration-resource-configure_{context}"]
= Configure the Configuration Resource

To configure the Configuration Resource, you customize the Custom Resource Definition (CRD) that controls its Operator and deploy it to your cluster.

.Prerequisites
* Deploy an {product-title} cluster.
* Review the CRD for the resource and provision any resources that your changes require.
* Access to the right user to do this thing.

.Procedure

. From some specific computer, modify the CRD for the resource to describe your intended configuration. Save the file in `whatever-the-location-is`.

. Run the following command to update the CRD in your cluster:
+
----
$ oc something or other --<file> <1> --<cluster><2>
----
<1> The CRD file that contains customizations for your resource.
<2> However you specify the cluster you’re changing.

. Confirm that the resource reflects your changes. Run the following command and review the output:
+
----
$ oc something or other

Output
Output
Output
----
+
If the output includes <thing>, the resource redeployed on your cluster.
