// Module included in the following assemblies:
//
// * nodes/nodes-nodes-jobs.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-nodes-jobs-creating_{context}"]
= Creating jobs

You create a job in {product-title} by creating a job object.

.Procedure

To create a job:

. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  parallelism: 1    <1>
  completions: 1    <2>
  activeDeadlineSeconds: 1800 <3>
  backoffLimit: 6   <4>
  template:         <5>
    metadata:
      name: pi
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: OnFailure    <6>
#...
----
<1> Optional: Specify how many pod replicas a job should run in parallel; defaults to `1`.
* For non-parallel jobs, leave unset. When unset, defaults to `1`.
<2> Optional: Specify how many successful pod completions are needed to mark a job completed.
* For non-parallel jobs, leave unset. When unset, defaults to `1`.
* For parallel jobs with a fixed completion count, specify the number of completions.
* For parallel jobs with a work queue, leave unset. When unset defaults to the `parallelism` value.
<3> Optional: Specify the maximum duration the job can run.
<4> Optional: Specify the number of retries for a job. This field defaults to six.
<5> Specify the template for the pod the controller creates.
<6> Specify the restart policy of the pod:
* `Never`. Do not restart the job.
* `OnFailure`. Restart the job only if it fails.
* `Always`. Always restart the job.
+
For details on how {product-title} uses restart policy with failed containers, see
the link:https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#example-states[Example States] in the Kubernetes documentation.

. Create the job:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

[NOTE]
====
You can also create and launch a job from a single command using `oc create job`. The following command creates and launches a job similar to the one specified in the previous example:

[source,terminal]
----
$ oc create job pi --image=perl -- perl -Mbignum=bpi -wle 'print bpi(2000)'
----
====
