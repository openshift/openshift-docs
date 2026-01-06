# Development Guide

## Technology stack required for development

* [operator-sdk] version v1.28.1
* [kind] version v0.22.0
* [git][git_tool]
* [go] version 1.21+
* [kubernetes] version v1.19+
* [kubectl] version v1.19+

## Build

```sh
make build
```

## Deploy on local kubernetes cluster

Run local Kubernetes cluster using Docker container using [Kind](https://kind.sigs.k8s.io/) and deploy kuadrant operator (and *all* dependencies) in a single command.

```shell
make local-setup
```

The `make local-setup` target accepts the following variables:

| **Makefile Variable** | **Description** | **Default value** |
| --- | --- |--- |
| `GATEWAYAPI_PROVIDER` | GatewayAPI provider name. Accepted values: [*istio*] | *istio* |

## Run as a local process

Run local Kubernetes cluster using Docker container using [Kind](https://kind.sigs.k8s.io/) and deploy *all* dependencies in a single command.

```shell
make local-env-setup
```

The `make local-env-setup` target accepts the following variables:

| **Makefile Variable** | **Description** | **Default value** |
| --- | --- |--- |
| `GATEWAYAPI_PROVIDER` | GatewayAPI provider name. Accepted values: [*istio*] | *istio* |

Then, run the operator locally

```shell
make run
```

## Deploy on existing kubernetes cluster

**Requirements**:
* Active session open to the kubernetes cluster.
* GatewayAPI installed
* GatewayAPI provider installed. Currently only Istio supported.
* [Cert Manager](https://cert-manager.io/) installed

Before running the kuadrant operator, some dependencies needs to be deployed.

```
make install
make deploy-dependencies
```

Then, deploy the operator

```sh
make deploy
```

## Deploy kuadrant operator using OLM

You can deploy kuadrant using OLM just running few commands.
No need to build any image. Kuadrant engineering team provides `latest` and
release version tagged images. They are available in
the [Quay.io/Kuadrant](https://quay.io/organization/kuadrant) image repository.

Create kind cluster

```sh
make kind-create-cluster
```

Deploy OLM system

```sh
make install-olm
```

Deploy kuadrant using OLM. The `make deploy-catalog` target accepts the following variables:

| **Makefile Variable** | **Description**                     | **Default value**                                   |
|-----------------------|-------------------------------------|-----------------------------------------------------|
| `CATALOG_IMG`         | Kuadrant operator catalog image URL | `quay.io/kuadrant/kuadrant-operator-catalog:latest` |

```sh
make deploy-catalog [CATALOG_IMG=quay.io/kuadrant/kuadrant-operator-catalog:latest]
```

## Build custom OLM catalog

If you want to deploy (using OLM) a custom kuadrant operator, you need to build your own catalog.
Furthermore, if you want to deploy a custom limitador or authorino operator, you also need
to build your own catalog. The kuadrant operator bundle includes the authorino or limtador operator
dependency version, hence using other than `latest` version requires a custom kuadrant operator
bundle and a custom catalog including the custom bundle.

### Build kuadrant operator bundle image

The `make bundle` target accepts the following variables:

| **Makefile Variable**           | **Description**               | **Default value**                                   | **Notes**                                                                                          |
|---------------------------------|-------------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `IMG`                           | Kuadrant operator image URL   | `quay.io/kuadrant/kuadrant-operator:latest`         | `TAG` var could be use to build this URL, defaults to _latest_  if not provided                    |
| `VERSION`                       | Bundle version                | `0.0.0`                                             |                                                                                                    |
| `LIMITADOR_OPERATOR_BUNDLE_IMG` | Limitador operator bundle URL | `quay.io/kuadrant/limitador-operator-bundle:latest` | `LIMITADOR_OPERATOR_VERSION` var could be used to build this, defaults to _latest_ if not provided |
| `AUTHORINO_OPERATOR_BUNDLE_IMG` | Authorino operator bundle URL | `quay.io/kuadrant/authorino-operator-bundle:latest` | `AUTHORINO_OPERATOR_VERSION` var could be used to build this, defaults to _latest_ if not provided |
| `DNS_OPERATOR_BUNDLE_IMG`       | DNS operator bundle URL       | `quay.io/kuadrant/dns-operator-bundle:latest`       | `DNS_OPERATOR_BUNDLE_IMG` var could be used to build this, defaults to _latest_ if not provided    |
| `RELATED_IMAGE_WASMSHIM`        | WASM shim image URL           | `oci://quay.io/kuadrant/wasm-shim:latest`           | `WASM_SHIM_VERSION` var could be used to build this, defaults to _latest_ if not provided          |

* Build the bundle manifests

```bash

make bundle [IMG=quay.io/kuadrant/kuadrant-operator:latest] \
            [VERSION=0.0.0] \
            [LIMITADOR_OPERATOR_BUNDLE_IMG=quay.io/kuadrant/limitador-operator-bundle:latest] \
            [AUTHORINO_OPERATOR_BUNDLE_IMG=quay.io/kuadrant/authorino-operator-bundle:latest] \
            [DNS_OPERATOR_BUNDLE_IMG=quay.io/kuadrant/dns-operator-bundle:latest] \
            [RELATED_IMAGE_WASMSHIM=oci://quay.io/kuadrant/wasm-shim:latest]
```

* Build the bundle image from the manifests

| **Makefile Variable** | **Description**                    | **Default value**                                  |
|-----------------------|------------------------------------|----------------------------------------------------|
| `BUNDLE_IMG`          | Kuadrant operator bundle image URL | `quay.io/kuadrant/kuadrant-operator-bundle:latest` |

```sh
make bundle-build [BUNDLE_IMG=quay.io/kuadrant/kuadrant-operator-bundle:latest]
```

* Push the bundle image to a registry

| **Makefile Variable** | **Description**                    | **Default value**                                  |
|-----------------------|------------------------------------|----------------------------------------------------|
| `BUNDLE_IMG`          | Kuadrant operator bundle image URL | `quay.io/kuadrant/kuadrant-operator-bundle:latest` |

```sh
make bundle-push [BUNDLE_IMG=quay.io/kuadrant/kuadrant-operator-bundle:latest]
```

Frequently, you may need to build custom kuadrant bundle with the default (`latest`) Limitador and
Authorino bundles. These are the example commands to build the manifests, build the bundle image
and push to the registry.

In the example, a new kuadrant operator bundle version `0.8.0` will be created that references
the kuadrant operator image `quay.io/kuadrant/kuadrant-operator:v0.5.0` and latest Limitador and
Authorino bundles.

```sh
# manifests
make bundle IMG=quay.io/kuadrant/kuadrant-operator:v0.5.0 VERSION=0.8.0

# bundle image
make bundle-build BUNDLE_IMG=quay.io/kuadrant/kuadrant-operator-bundle:my-bundle

# push bundle image
make bundle-push BUNDLE_IMG=quay.io/kuadrant/kuadrant-operator-bundle:my-bundle
```

### Build custom catalog

The catalog's format will be [File-based Catalog](https://olm.operatorframework.io/docs/reference/file-based-catalogs/).

Make sure all the required bundles are pushed to the registry. It is required by the `opm` tool.

The `make catalog` target accepts the following variables:

| **Makefile Variable**           | **Description**                    | **Default value**                                   |
|---------------------------------|------------------------------------|-----------------------------------------------------|
| `BUNDLE_IMG`                    | Kuadrant operator bundle image URL | `quay.io/kuadrant/kuadrant-operator-bundle:latest`  |
| `LIMITADOR_OPERATOR_BUNDLE_IMG` | Limitador operator bundle URL      | `quay.io/kuadrant/limitador-operator-bundle:latest` |
| `AUTHORINO_OPERATOR_BUNDLE_IMG` | Authorino operator bundle URL      | `quay.io/kuadrant/authorino-operator-bundle:latest` |
| `DNS_OPERATOR_BUNDLE_IMG`       | DNS operator bundle URL            | `quay.io/kuadrant/dns-operator-bundle:latest`       |

```sh
make catalog [BUNDLE_IMG=quay.io/kuadrant/kuadrant-operator-bundle:latest] \
            [LIMITADOR_OPERATOR_BUNDLE_IMG=quay.io/kuadrant/limitador-operator-bundle:latest] \
            [AUTHORINO_OPERATOR_BUNDLE_IMG=quay.io/kuadrant/authorino-operator-bundle:latest] \
            [DNS_OPERATOR_BUNDLE_IMG=quay.io/kuadrant/dns-operator-bundle:latest]
```

* Build the catalog image from the manifests

| **Makefile Variable** | **Description**                     | **Default value**                                   |
|-----------------------|-------------------------------------|-----------------------------------------------------|
| `CATALOG_IMG`         | Kuadrant operator catalog image URL | `quay.io/kuadrant/kuadrant-operator-catalog:latest` |

```sh
make catalog-build [CATALOG_IMG=quay.io/kuadrant/kuadrant-operator-catalog:latest]
```

* Push the catalog image to a registry

```sh
make catalog-push [CATALOG_IMG=quay.io/kuadrant/kuadrant-operator-bundle:latest]
```

You can try out your custom catalog image following the steps of the
[Deploy kuadrant operator using OLM](#deploy-kuadrant-operator-using-olm) section.

## Cleaning up

```sh
make local-cleanup
```

## Run tests

### Unittests

```sh
make test-unit
```

Optionally, add `TEST_NAME` makefile variable to run specific test

```sh
make test-unit TEST_NAME=TestLimitIndexEquals
```

or even subtest

```sh
make test-unit TEST_NAME=TestLimitIndexEquals/empty_indexes_are_equal
```

### Integration tests

Multiple controller integration tests are defined

| Golang package | Required environment | Makefile env setup target | Makefile test run target |
| --- | --- | --- | --- |
| `github.com/kuadrant/kuadrant-operator/tests/bare_k8s` | no gateway provider, no GatewayAPI CRDs. Just Kuadrant API and Kuadrant dependencies. | `make local-k8s-env-setup` | `make test-bare-k8s-integration` |
| `github.com/kuadrant/kuadrant-operator/tests/gatewayapi` | no gateway provider. GatewayAPI CRDs, Kuadrant API and Kuadrant dependencies. | `make local-gatewayapi-env-setup` | `make test-gatewayapi-env-integration` |
| `github.com/kuadrant/kuadrant-operator/controllers` | at least one gatewayapi provider. It can be any: istio, envoygateway, ...  | `make local-env-setup GATEWAYAPI_PROVIDER=[istio]` (Default *istio*) | `make test-integration` |
| `github.com/kuadrant/kuadrant-operator/tests/istio` | GatewayAPI CRDs, Istio, Kuadrant API and Kuadrant dependencies.  | `make local-env-setup GATEWAYAPI_PROVIDER=istio` | `make test-istio-env-integration` |

### Lint tests

```sh
make run-lint
```

## (Un)Install Kuadrant CRDs

You need an active session open to a kubernetes cluster.

Remove CRDs

```sh
make uninstall
```

[git_tool]:https://git-scm.com/downloads
[operator-sdk]:https://github.com/operator-framework/operator-sdk
[go]:https://golang.org/
[kind]:https://kind.sigs.k8s.io/
[kubernetes]:https://kubernetes.io/
[kubectl]:https://kubernetes.io/docs/tasks/tools/#kubectl
