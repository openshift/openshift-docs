# DNS Health Checks
DNS Health Checks are a tool provided by some DNS Providers for ensuring the availability and reliability of your DNS Records and only publishing DNS Records that resolve to healthy workloads. Kuadrant offers a powerful feature known as DNSPolicy, which allows you to configure these health checks for all the managed DNS endpoints created as a result of that policy. This guide provides a comprehensive overview of how to set up, utilize, and understand these DNS health checks.

## Supported Providers

we currently only support [AWS Route53 DNS Health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html).

## Configuration of Health Checks

To configure a DNS health check, you need to specify the `healthCheck` section of the DNSPolicy, which includes important properties such as:

* `endpoint`: This is the path where the health checks take place, usually represented as '/healthz' or something similar.
* `port`: Specific port for the connection to be checked.
* `protocol`: Type of protocol being used, like HTTP or HTTPS.
* `FailureThreshold`: How many times we can tolerate a failure on this endpoint, before removing the related DNS entry.

```bash
apiVersion: kuadrant.io/v1alpha1
kind: DNSPolicy
metadata:
  name: prod-web
  namespace: multi-cluster-gateways
spec:
  targetRef:
    name: prod-web
    group: gateway.networking.k8s.io
    kind: Gateway
  loadBalancing: simple
  healthCheck:
    endpoint: "/health"
    port: 443
    protocol: "HTTPS"
    failureThreshold: 5
```

This configuration sets up a DNS health check in AWS Route53 which will connect by HTTPS on port 443 and request the path /health.

## Reviewing the status of Health Checks
The DNS Record CR will show whether the health check has been created or not in the DNS Provider, and will also show any errors encountered when trying to create or update the health check configuration.

To see the status of the executing health check requires logging in to the Route53 console to view the current probe results.

## Reconfiguring Health Checks
To reconfigure the health checks,  update the HealthCheck section of the DNS Policy, this will be reflected into all the health checks created as a result of this policy.

## Removing Health Checks

To remove the health checks created in AWS, delete the healthcheck section of the DNS Policy. All health checks will be deleted automatically, if the DNS Policy is deleted.

## Limitations

As Route53 will only perform health checks on an IP address, currently do not create health checks on DNS Policies that target gateways with hostname addresses.

## Other Providers

Although we intend to support integrating with the DNS Health checks provided by other DNS Providers in the future, we currently only support AWS Route53.
