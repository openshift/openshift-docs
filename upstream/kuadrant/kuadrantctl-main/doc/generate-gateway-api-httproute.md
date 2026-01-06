## Generate Gateway API HTTPRoute object from OpenAPI 3

The `kuadrantctl generate gatewayapi httproute` command generates an [Gateway API HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/)
from your [OpenAPI Specification (OAS) 3.x](https://spec.openapis.org/oas/latest.html) powered with [kuadrant extensions](openapi-kuadrant-extensions.md).

### OpenAPI specification

An OpenAPI document resource can be provided to the cli by one of the following channels:

* Filename in the available path.
* URL format (supported schemes are HTTP and HTTPS). The CLI will try to download from the given address.
* Read from stdin standard input stream.

### Usage

```shell
$ kuadrantctl generate gatewayapi httproute -h
Generate Gateway API HTTPRoute from OpenAPI 3.0.X

Usage:
  kuadrantctl generate gatewayapi httproute [flags]

Flags:
  -h, --help          help for httproute
  --oas string        Path to OpenAPI spec file (in JSON or YAML format), URL, or '-' to read from standard input (required)
  -o Output format:   'yaml' or 'json'. (default "yaml")

Global Flags:
  -v, --verbose   verbose output
```

> Under the example folder there are examples of OAS 3 that can be used to generate the resources

As an AuthPolicy and RateLimitPolicy both require a HTTPRoute to target, the user guides for generating those policies include examples of running the `kuadrantctl generate gatewayapi httproute` command.

You can find those guides here:

* [Generate Kuadrant AuthPolicy](./generate-kuadrant-auth-policy.md)
* [Generate Kuadrant RateLimitPolicy](./generate-kuadrant-rate-limit-policy.md)
