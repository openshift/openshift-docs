## Kuadrant Getting Started - Multi Cluster

## Overview

In this quick start, we will cover the setup of Kuadrant in multiple local kind clusters.
This document is intended as a follow on to the single cluster guide.
It can be used for adding 1 or more clusters to your local setup.

### Prerequisites

- Completed the [Single-cluster Quick Start](https://docs.kuadrant.io/getting-started-single-cluster/)

### Environmental Variables

The same environment variable requirements from the [Single-cluster Quick Start](https://docs.kuadrant.io/getting-started-single-cluster/) apply to this document,
including the `KUADRANT_REF` variable.

### Set Up a kind cluster and install Kuadrant

Run the same quickstart script from the single cluster quick start:

```bash
curl "https://raw.githubusercontent.com/kuadrant/kuadrant-operator/${KUADRANT_REF}/hack/quickstart-setup.sh" | bash
```

The script will detect if you already have a cluster from the single cluster setup running, and prompt you for a multi cluster setup.
This will setup an additional kind cluster, install Istio and install Kuadrant.
You can re-run the script multiple times to add more clusters.
Each cluster will have a number suffix in the name. For example: `kuadrant-local-1`, `kuadrant-local-2`, `kuadrant-local-3`.
The original cluster from the single cluster setup will keep its name of just `kuadrant-local`.

### Clean Up

To ensure that any DNS records are removed, you should remove any `DNSPolicy` and `TLSPolicy` resources before deleting the local cluster.

### What's Next

The next step is to setup and use the policies provided by Kuadrant. 

[Secure, Protect and Connect your Gateway](kuadrant-operator/doc/user-guides/secure-protect-connect.md)
