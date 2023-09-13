// Text snippet included in the following files
//
// * serverless/knative-serving/config-custom-domains/serverless-custom-domains.adoc
// * modules/serverless-domain-mapping-odc-admin.adoc

Knative services are automatically assigned a default domain name based on your cluster configuration. For example, `<service_name>-<namespace>.example.com`. You can customize the domain for your Knative service by mapping a custom domain name that you own to a Knative service.

You can do this by creating a `DomainMapping` resource for the service. You can also create multiple `DomainMapping` resources to map multiple domains and subdomains to a single service.
