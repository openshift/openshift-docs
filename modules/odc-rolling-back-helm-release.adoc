:_mod-docs-content-type: PROCEDURE
[id="odc-rolling-back-helm-release_{context}"]
= Rolling back a Helm release

If a release fails, you can rollback the Helm release to a previous version.

.Procedure
To rollback a release using the *Helm* view:

. In the *Developer* perspective, navigate to the *Helm* view to see the *Helm Releases* in the namespace.
. Click the *Options* menu {kebab} adjoining the listed release, and select *Rollback*.
. In the *Rollback Helm Release* page, select the *Revision* you want to rollback to and click *Rollback*.
. In the *Helm Releases* page, click on the chart to see the details and resources for that release.
. Go to the *Revision History* tab to see all the revisions for the chart.
+
.Helm revision history
image::odc_helm_revision_history.png[]
+
. If required, you can further use the *Options* menu {kebab} adjoining a particular revision and select the revision to rollback to.
