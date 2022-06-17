// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-cronjobs_{context}"]
= Pruning cron jobs

Cron jobs can perform pruning of successful jobs, but might not properly handle
failed jobs. Therefore, the cluster administrator should perform regular cleanup of
jobs manually. They should also restrict the access to cron jobs to a small
group of trusted users and set appropriate quota to prevent the cron job from
creating too many jobs and pods.
