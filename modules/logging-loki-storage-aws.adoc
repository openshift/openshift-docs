// Module is included in the following assemblies:
// logging/cluster-logging-loki.adoc
//
:_mod-docs-content-type: PROCEDURE
[id="logging-loki-storage-aws_{context}"]
= AWS storage

.Prerequisites
* You have deployed Loki Operator.
* You have created a link:https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html[bucket] on AWS.
* You have created an link:https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based[AWS IAM Policy and IAM User].

.Procedure
* Create an object storage secret with the name `logging-loki-aws` by running the following command:

[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-aws \
  --from-literal=bucketnames="<bucket_name>" \
  --from-literal=endpoint="<aws_bucket_endpoint>" \
  --from-literal=access_key_id="<aws_access_key_id>" \
  --from-literal=access_key_secret="<aws_access_key_secret>" \
  --from-literal=region="<aws_region_of_your_bucket>"
----
