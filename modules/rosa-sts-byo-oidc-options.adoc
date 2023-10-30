// Module included in the following assemblies:
//
// * rosa_architecture/rosa-oidc-overview.adoc
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

:_mod-docs-content-type: CONCEPT
[id="rosa-sts-byo-oidc-options_{context}"]
= Parameter options for creating your own OpenID Connect configuration

The following options may be added to the `rosa create oidc-config` command. All of these parameters are optional. Running the `rosa create oidc-config` command without parameters creates an unmanaged OIDC configuration.

[NOTE]
====
You are required to register the unmanaged OIDC configuration by posting a request to `/oidc_configs` through OpenShift Cluster Manager. You receive an ID in the response. Use this ID to create a cluster.
====

[discrete]
[id="rosa-sts-byo-oidc-raw-files_{context}"]
== raw-files

Allows you to provide raw files for the private RSA key. This key is named `rosa-private-key-oidc-<random_label_of_length_4>.key`. You also receive a discovery document, named `discovery-document-oidc-<random_label_of_length_4>.json`, and a JSON Web Key Set, named `jwks-oidc-<random_label_of_length_4>.json`.

You use these files to set up the endpoint. This endpoint responds to `/.well-known/openid-configuration` with the discovery document and on `keys.json` with the JSON Web Key Set. The private key is stored in Amazon Web Services (AWS) Secrets Manager Service (SMS) as plaintext.

.Example
[source,terminal]
----
$ rosa create oidc-config --raw-files
----

[discrete]
[id="rosa-sts-byo-oidc-mode_{context}"]
== mode

Allows you to specify the mode to create your OIDC configuration. With the `manual` option, you receive AWS commands that set up the OIDC configuration in an S3 bucket. This option stores the private key in the Secrets Manager. With the `manual` option, the OIDC Endpoint URL is the URL for the S3 bucket. You must retrieve the Secrets Manager ARN to register the OIDC configuration with OpenShift Cluster Manager.

You receive the same OIDC configuration and AWS resources as the `manual` mode when using the `auto` option. A significant difference between the two options is that when using the `auto` option, ROSA calls AWS, so you do not need to take any further actions. The OIDC Endpoint URL is the URL for the S3 bucket. The CLI retrieves the Secrets Manager ARN, registers the OIDC configuration with OpenShift Cluster Manager, and reports the second `rosa` command that the user can run to continue with the creation of the STS cluster.

.Example
[source,terminal]
----
$ rosa create oidc-config --mode=<auto|manual>
----

[discrete]
[id="rosa-sts-byo-oidc-managed_{context}"]
== managed

Creates an OIDC configuration that is hosted under Red Hat's AWS account. This command creates a private key that responds directly with an OIDC Config ID for you to use when creating the STS cluster.

.Example
[source,terminal]
----
$ rosa create oidc-config --managed
----

.Sample output
[source,terminal]
----
W: For a managed OIDC Config only auto mode is supported. However, you may choose the provider creation mode
? OIDC Provider creation mode: auto
I: Setting up managed OIDC configuration
I: Please run the following command to create a cluster with this oidc config
rosa create cluster --sts --oidc-config-id 233jnu62i9aphpucsj9kueqlkr1vcgra
I: Creating OIDC provider using 'arn:aws:iam::242819244:user/userName'
? Create the OIDC provider? Yes
I: Created OIDC provider with ARN 'arn:aws:iam::242819244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/233jnu62i9aphpucsj9kueqlkr1vcgra'
----