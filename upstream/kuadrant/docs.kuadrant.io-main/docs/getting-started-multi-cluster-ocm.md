## Kuadrant Getting Started - Multi Cluster


### Prerequisites

- [Docker](https://docs.docker.com/engine/install/)
- [Kind](https://kind.sigs.k8s.io/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/)
- OpenSSL >= 3
- AWS account with Route 53 enabled or GCP with Cloud DNS enabled
- [Docker Mac Net Connect](https://github.com/chipmk/docker-mac-net-connect) (macOS users only)

### DNS Environmental Variables

Export environment variables with the keys listed below for your desired provider. Fill in your own values as appropriate. Note that you will need to have created a root domain in AWS Route 53 or in GCP Cloud DNS:

### AWS

| Env Var                      | Example Value               | Description                                                                                                 |
|------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------|
| `MGC_ZONE_ROOT_DOMAIN`       | `jbloggs.hcpapps.net`       | Hostname for the root Domain                                                                                |
| `MGC_AWS_DNS_PUBLIC_ZONE_ID` | `Z01234567US0IQE3YLO00`     | AWS Route 53 Zone ID for specified `MGC_ZONE_ROOT_DOMAIN`                                                   |
| `MGC_AWS_ACCESS_KEY_ID`      | `AKIA1234567890000000`      | Access Key ID, for user with permissions to Route 53 in the account where root domain is created            |
| `MGC_AWS_SECRET_ACCESS_KEY`  | `Z01234567US0000000`        | Access Secret Access Key, for user with permissions to Route 53 in the account where root domain is created |
| `MGC_AWS_REGION`             | `eu-west-1`                 | AWS Region                                                                                                  |

### GCP

   | Env Var                 | Example Value          | Description                                                    |
   |-------------------------|------------------------|----------------------------------------------------------------|
   | `GOOGLE`     | `{"client_id": "00000000-00000000000000.apps.googleusercontent.com","client_secret": "d-FL95Q00000000000000","refresh_token": "00000aaaaa00000000-AAAAAAAAAAAAKFGJFJDFKDK","type": "authorized_user"}` |  This is the JSON created from either the JSON credentials created by the Google Cloud CLI or a Service account             |
   | `PROJECT_ID` | `my_project_id`   | ID to the google project |
   | `ZONE_NAME`       | `jbloggs-google`   | Zone name                          |
   | `ZONE_DNS_NAME` | `jbloggs.google.hcpapps.net`   | DNS name                        |
   | `LOG_LEVEL`              | `1`                     | Log level for the Controller                          |

>Alternatively, to set defaults, add the above environment variables to your `.zshrc` or `.bash_profile`.

### Set the release you want to use 

```bash
export MGC_BRANCH=release-0.3
```

### Set Up Clusters and install Kuadrant

Run the following:

```bash
curl "https://raw.githubusercontent.com/kuadrant/multicluster-gateway-controller/${MGC_BRANCH}/hack/quickstart-setup.sh" | bash
```

### What's Next

Now that you have two Kind clusters configured with Kuadrant installed you are ready to begin [the Multicluster Gateways walkthrough.](/multicluster-gateway-controller/docs/gateways/define-and-place-a-gateway/)
