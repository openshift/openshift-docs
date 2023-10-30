// Module included in the following assemblies:
//
// applications/application-health

:_mod-docs-content-type: PROCEDURE
[id="odc-editing-health-checks"]
= Editing health checks using the Developer perspective

You can use the *Topology* view to edit health checks added to your application, modify them, or add more health checks.

.Prerequisites:
* You have switched to the *Developer* perspective in the web console.
* You have created and deployed an application on {product-title} using the *Developer* perspective.
* You have added health checks to your application.

.Procedure
. In the *Topology* view, right-click your application and select *Edit Health Checks*. Alternatively, in the side panel, click the *Actions* drop-down list and select *Edit Health Checks*.
. In the *Edit Health Checks* page:

* To remove a previously added health probe, click the *Remove* icon adjoining it.
* To edit the parameters of an existing probe:
+
.. Click the *Edit Probe* link next to a previously added probe to see the parameters for the probe.
.. Modify the parameters as required, and click the check mark to save your changes.
+
* To add a new health probe, in addition to existing health checks, click the add probe links. For example, to add a Liveness probe that checks if your container is running:
+
.. Click *Add Liveness Probe*, to see a form containing the parameters for the probe.
.. Edit the probe parameters as required.
+
[NOTE]
====
The `Timeout` value must be lower than the `Period` value. The `Timeout` default value is `1`. The `Period` default value is `10`.
====
.. Click the check mark at the bottom of the form. The *Liveness Probe Added* message is displayed.

. Click *Save* to save your modifications and add the additional probes to your container. You are redirected to the *Topology* view.
. In the side panel, verify that the probes have been added by clicking on the deployed pod under the *Pods* section.
. In the *Pod Details* page, click the listed container in the *Containers* section.
. In the *Container Details* page, verify that the Liveness probe - `HTTP Get 10.129.4.65:8080/` has been added to the container, in addition to the earlier existing probes.
