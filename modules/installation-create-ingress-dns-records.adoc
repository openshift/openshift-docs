// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

:_mod-docs-content-type: PROCEDURE
[id="installation-create-ingress-dns-records_{context}"]
= Creating the Ingress DNS Records

If you removed the DNS Zone configuration, manually create DNS records that point to the Ingress load balancer.
You can create either a wildcard record or specific records. While the following procedure uses A records, you can use other record types that you require, such as CNAME or alias.

.Prerequisites

* You deployed an {product-title} cluster on Amazon Web Services (AWS) that uses infrastructure that you provisioned.
* You installed the OpenShift CLI (`oc`).
* You installed the `jq` package.
* You downloaded the AWS CLI and installed it on your computer. See
link:https://docs.aws.amazon.com/cli/latest/userguide/install-bundle.html[Install the AWS CLI Using the Bundled Installer (Linux, macOS, or Unix)].

.Procedure

. Determine the routes to create.
** To create a wildcard record, use `*.apps.<cluster_name>.<domain_name>`, where `<cluster_name>` is your cluster name, and `<domain_name>` is the Route 53 base domain for your {product-title} cluster.
** To create specific records, you must create a record for each route that your cluster uses, as shown in the output of the following command:
+
[source,terminal]
----
$ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{.host}{"\n"}{end}{end}' routes
----
+
.Example output
[source,terminal]
----
oauth-openshift.apps.<cluster_name>.<domain_name>
console-openshift-console.apps.<cluster_name>.<domain_name>
downloads-openshift-console.apps.<cluster_name>.<domain_name>
alertmanager-main-openshift-monitoring.apps.<cluster_name>.<domain_name>
prometheus-k8s-openshift-monitoring.apps.<cluster_name>.<domain_name>
----

. Retrieve the Ingress Operator load balancer status and note the value of the external IP address that it uses, which is shown in the `EXTERNAL-IP` column:
+
[source,terminal]
----
$ oc -n openshift-ingress get service router-default
----
+
.Example output
[source,terminal]
----
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP                            PORT(S)                      AGE
router-default   LoadBalancer   172.30.62.215   ab3...28.us-east-2.elb.amazonaws.com   80:31499/TCP,443:30693/TCP   5m
----

. Locate the hosted zone ID for the load balancer:
+
[source,terminal]
----
$ aws elb describe-load-balancers | jq -r '.LoadBalancerDescriptions[] | select(.DNSName == "<external_ip>").CanonicalHostedZoneNameID' <1>
----
<1> For `<external_ip>`, specify the value of the external IP address of the Ingress Operator load balancer that you obtained.
+
.Example output
[source,terminal]
----
Z3AADJGX6KTTL2
----

+
The output of this command is the load balancer hosted zone ID.

. Obtain the public hosted zone ID for your cluster's domain:
+
[source,terminal]
----
$ aws route53 list-hosted-zones-by-name \
            --dns-name "<domain_name>" \ <1>
            --query 'HostedZones[? Config.PrivateZone != `true` && Name == `<domain_name>.`].Id' <1>
            --output text
----
<1> For `<domain_name>`, specify the Route 53 base domain for your {product-title} cluster.
+
.Example output
[source,terminal]
----
/hostedzone/Z3URY6TWQ91KVV
----
+
The public hosted zone ID for your domain is shown in the command output. In this example, it is `Z3URY6TWQ91KVV`.

. Add the alias records to your private zone:
+
[source,terminal]
----
$ aws route53 change-resource-record-sets --hosted-zone-id "<private_hosted_zone_id>" --change-batch '{ <1>
>   "Changes": [
>     {
>       "Action": "CREATE",
>       "ResourceRecordSet": {
>         "Name": "\\052.apps.<cluster_domain>", <2>
>         "Type": "A",
>         "AliasTarget":{
>           "HostedZoneId": "<hosted_zone_id>", <3>
>           "DNSName": "<external_ip>.", <4>
>           "EvaluateTargetHealth": false
>         }
>       }
>     }
>   ]
> }'
----
<1> For `<private_hosted_zone_id>`, specify the value from the output of the CloudFormation template for DNS and load balancing.
<2> For `<cluster_domain>`, specify the domain or subdomain that you use with your {product-title} cluster.
<3> For `<hosted_zone_id>`, specify the public hosted zone ID for the load balancer that you obtained.
<4> For `<external_ip>`, specify the value of the external IP address of the Ingress Operator load balancer. Ensure that you include the trailing period (`.`) in this parameter value.

. Add the records to your public zone:
+
[source,terminal]
----
$ aws route53 change-resource-record-sets --hosted-zone-id "<public_hosted_zone_id>"" --change-batch '{ <1>
>   "Changes": [
>     {
>       "Action": "CREATE",
>       "ResourceRecordSet": {
>         "Name": "\\052.apps.<cluster_domain>", <2>
>         "Type": "A",
>         "AliasTarget":{
>           "HostedZoneId": "<hosted_zone_id>", <3>
>           "DNSName": "<external_ip>.", <4>
>           "EvaluateTargetHealth": false
>         }
>       }
>     }
>   ]
> }'
----
<1> For `<public_hosted_zone_id>`, specify the public hosted zone for your domain.
<2> For `<cluster_domain>`, specify the domain or subdomain that you use with your {product-title} cluster.
<3> For `<hosted_zone_id>`, specify the public hosted zone ID for the load balancer that you obtained.
<4> For `<external_ip>`, specify the value of the external IP address of the Ingress Operator load balancer. Ensure that you include the trailing period (`.`) in this parameter value.
