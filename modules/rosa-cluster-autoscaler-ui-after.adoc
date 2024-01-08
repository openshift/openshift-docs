// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc
// * osd_cluster_admin/osd-cluster-autoscaling.adoc

:_mod-docs-content-type: REFERENCE
[id="rosa-enable-cluster-autoscale-ui-after_{context}"]
= Enable autoscaling after cluster creation with OpenShift Cluster Manager

You can use OpenShift Cluster Manager to autoscale after cluster creation.

.Procedure

. In OpenShift Cluster Manager, click the name of the cluster you want to autoscale. The Overview page for the cluster has a *Autoscaling* item that indicates if it is enabled or disabled.

. Click the *Machine Pools* tab.

. Click the *Edit cluster autoscaling* button. The *Edit cluster autoscaling* settings window is shown.

. Click the *Autoscale cluster* toggle at the top of the window. All the settings are now editable.

. Edit any settings you want and then click *Save*.

. Click the *x* at the top right of the screen to close the settings window.

To revert all autoscaling settings to the defaults if they have been changed, click the *Revert all to defaults* button.