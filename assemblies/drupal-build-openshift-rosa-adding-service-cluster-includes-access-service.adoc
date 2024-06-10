// Module included in the following assemblies:
//
// * assemblies/adding-service.adoc

:_mod-docs-content-type: PROCEDURE
[id="access-service_{context}"]

= Accessing installed add-on services on your cluster

After you successfully install an add-on service on your {product-title}
ifdef::openshift-rosa[]
(ROSA)
endif::openshift-rosa[]
cluster, you can access the service by using the OpenShift web console.

.Prerequisites

* You have successfully installed a service on your {product-title} cluster.

.Procedure

. Navigate to the *Clusters* page in {cluster-manager-url}.

. Select the cluster with an installed service you want to access.

. Navigate to the *Add-ons* tab, and locate the installed service that you want to access.

. Click *View on console* from the service option to open the OpenShift web console.

. Enter your credentials to log in to the OpenShift web console.

. Click the *Red Hat Applications* menu by clicking the three-by-three matrix icon in the upper right corner of the main screen.

. Select the service you want to open from the drop-down menu. A new browser tab opens and you are required to authenticate through Red Hat Single Sign-On.

You have now accessed your service and can begin using it.
