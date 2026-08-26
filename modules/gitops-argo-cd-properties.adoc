// Module included in the following assemblies:
//
// * argo-cd-custom-resource-properties.adoc

:_mod-docs-content-type: REFERENCE
[id="argo-cd-properties_{context}"]
= Argo CD custom resource properties

[role="_abstract"]
The Argo CD Custom Resource consists of the following properties:

|===
|**Name** |**Description** |**Default** | **Properties**
|`ApplicationInstanceLabelKey` |The `metadata.label` key name where Argo CD injects the app name as a tracking label.|`app.kubernetes.io/instance` |
|`ApplicationSet`
|`ApplicationSet` controller configuration options.
| `_<Object>_`
a|* _<Image>_ - The container image for the `ApplicationSet` controller. This overrides the `ARGOCD_APPLICATIONSET_IMAGE` environment variable.
  * _<Version>_ - The tag to use with the `ApplicationSet` container image.
  * _<Resources>_ - The container compute resources.
  * _<LogLevel>_ - The log level used by the Argo CD Application Controller component. Valid options are `debug`, `info`, `error`, and `warn`.
  * _<LogFormat>_ - The log format used by the Argo CD Application Controller component. Valid options are `text` or `json`.
  * _<PrallelismLimit>_ - The kubectl parallelism limit to set for the controller `(--kubectl-parallelism-limit flag)`.
|`ConfigManagementPlugins`    |Add a configuration management plugin.| `__<empty>__` |
|`Controller`    |Argo CD Application Controller options.| `__<Object>__`
a|* _<Processors.Operation>_ - The number of operation processors.
  * _<Processors.Status>_ - The number of status processors.
  * _<Resources>_ - The container compute resources.
  * _<LogLevel>_ - The log level used by the Argo CD Application Controller component. Valid options are `debug`, `info`, `error`, and `warn`.
  * _<AppSync>_ - AppSync is used to control the sync frequency of Argo CD applications
  * _<Sharding.enabled>_ - Enable sharding on the Argo CD Application Controller component. This property is used to manage a large number of clusters to relieve memory pressure on the controller component.
  * _<Sharding.replicas>_ - The number of replicas that will be used to support sharding of the Argo CD Application Controller.
  * _<Env>_ - Environment to set for the application controller workloads.
|`DisableAdmin`    |Disables the built-in admin user.|`false` |
|`GATrackingID`    |Use a Google Analytics tracking ID.|`__<empty>__` |
|`GAAnonymizeusers`    |Enable hashed usernames sent to google analytics.|`false` |
|`HA`    |High availablity options.| `__<Object>__`
a|* _<Enabled>_ - Toggle high availability support globally for Argo CD.
  * _<RedisProxyImage>_ - The Redis HAProxy container image. This overrides the `ARGOCD_REDIS_HA_PROXY_IMAGE` environment variable.
  * _<RedisProxyVersion>_ - The tag to use for the Redis HAProxy container image.
|`HelpChatURL`    |URL for getting chat help (this will typically be your Slack channel for support).|`https://mycorp.slack.com/argo-cd` |
|`HelpChatText`    |The text that appears in a text box for getting chat help.|`Chat now!`|
|`Image`    |The container image for all Argo CD components. This overrides the `ARGOCD_IMAGE` environment variable.|`argoproj/argocd` |
|`Ingress`    |Ingress configuration options.| `__<Object>__` |
|`InitialRepositories`    |Initial Git repositories to configure Argo CD to use upon creation of the cluster.|`__<empty>__` |
|`Notifications`    |Notifications controller configuration options.|`__<Object>__`
a|* _<Enabled>_ - The toggle to start the notifications-controller.
  * _<Image>_ - The container image for all Argo CD components. This overrides the `ARGOCD_IMAGE` environment variable.
  * _<Version>_ - The tag to use with the Notifications container image.
  * _<Resources>_ - The container compute resources.
  * _<LogLevel>_ - The log level used by the Argo CD Application Controller component. Valid options are `debug`, `info`, `error`, and `warn`.
|`RepositoryCredentials`    |Git repository credential templates to configure Argo CD to use upon creation of the cluster.| `__<empty>__` |
|`InitialSSHKnownHosts`    |Initial SSH Known Hosts for Argo CD to use upon creation of the cluster.| `__<default_Argo_CD_Known_Hosts>__` |
|`KustomizeBuildOptions`    |The build options and parameters to use with `kustomize build`.|`__<empty>__` |
|`OIDCConfig` |The OIDC configuration as an alternative to Dex.|`__<empty>__` |
|`NodePlacement` |Add the `nodeSelector` and the `tolerations`.|`__<empty>__` |
|`Prometheus` |Prometheus configuration options.|`__<Object>__`
a|* _<Enabled>_ - Toggle Prometheus support globally for Argo CD.
  * _<Host>_ - The hostname to use for Ingress or Route resources.
  * _<Ingress>_ - Toggles Ingress for Prometheus.
  * _<Route>_ - Route configuration options.
  * _<Size>_ - The replica count for the Prometheus `StatefulSet`.
|`RBAC` |RBAC configuration options.|`__<Object>__`
a|* _<DefaultPolicy>_ - The `policy.default` property in the `argocd-rbac-cm` config map. The name of the default role which Argo CD will fall back to, when authorizing API requests.
  * _<Policy>_ - The `policy.csv` property in the `argocd-rbac-cm` config map. CSV data containing user-defined RBAC policies and role definitions.
  * _<Scopes>_ - The scopes property in the `argocd-rbac-cm` config map. Controls which OIDC scopes to examine during RBAC enforcement (in addition to sub scope).
|`Redis` |Redis configuration options.|`__<Object>__`
a|* _<AutoTLS>_ - Use the provider to create the Redis server's TLS certificate (one of: openshift). Currently only available for {product-title}.
  * _<DisableTLSVerification>_ - Define whether the Redis server should be accessed using strict TLS validation.
  * _<Image>_ - The container image for Redis. This overrides the `ARGOCD_REDIS_IMAGE` environment variable.
  * _<Resources>_ - The container compute resources.
  * _<Version>_ - The tag to use with the Redis container image.
|`ResourceCustomizations` |Customize resource behavior.|`__<empty>__` |
|`ResourceExclusions` |Completely ignore entire classes of resource group.|`__<empty>__` |
|`ResourceInclusions` |The configuration to configure which resource group/kinds are applied.|`__<empty>__` |
|`Server` |Argo CD Server configuration options.|`__<Object>__`
a|* _<Autoscale>_ - Server autoscale configuration options.
  * _<ExtraCommandArgs>_ - List of arguments added to the existing arguments set by the Operator.
  * _<GRPC>_ - GRPC configuration options.
  * _<Host>_ - The hostname used for Ingress or Route resources.
  * _<Ingress>_ - Ingress configuration for the Argo CD server component.
  * _<Insecure>_ - Toggles the insecure flag for Argo CD server.
  * _<Resources>_ - The container compute resources.
  * _<Replicas>_ - The number of replicas for the Argo CD server. Must be greater than or equal to `0`. If `Autoscale` is enabled, `Replicas` is ignored.
  * _<Route>_ - Route configuration options.
  * _<Service.Type>_ - The `ServiceType` used for the service resource.
  * _<LogLevel>_ - The log level to be used by the Argo CD Server component. Valid options are  `debug`, `info`, `error`, and `warn`.
  * _<LogFormat>_ - The log format used by the Argo CD Application Controller component. Valid options are `text` or `json`.
  * _<Env>_ - Environment to set for the server workloads.
|`SSO` |Single Sign-on options.|`__<Object>__`
a|* _<Image>_ - The container image for Keycloak. This overrides the `ARGOCD_KEYCLOAK_IMAGE` environment variable.
  * _<Keycloak>_ - Configuration options for Keycloak SSO provider.
  * _<Dex>_ - Configuration options for Dex SSO provider.
  * _<Provider>_ - The name of the provider used to configure Single Sign-on. For now the supported options are Dex and Keycloak.
  * _<Resources>_ - The container compute resources.
  * _<VerifyTLS>_ - Whether to enforce strict TLS checking when communicating with Keycloak service.
  * _<Version>_ - The tag to use with the Keycloak container image.
|`StatusBadgeEnabled` |Enable application status badge.|`true` |
|`TLS` |TLS configuration options.|`__<Object>__`
a|* _<CA.ConfigMapName>_ - The name of the `ConfigMap` which contains the CA certificate.
  * _<CA.SecretName>_ - The name of the secret which contains the CA Certificate and Key.
  * _<InitialCerts>_ - Initial set of certificates in the `argocd-tls-certs-cm` config map for connecting Git repositories via HTTPS.
|`UserAnonyousEnabled` |Enable anonymous user access.|`true` |
|`Version` |The tag to use with the container image for all Argo CD components.|Latest Argo CD version|
|`Banner` |Add a UI banner message.|`__<Object>__`
a|* _<Banner.Content>_ - The banner message content (required if a banner is displayed).
  * _<Banner.URL.SecretName>_ - The banner message link URL (optional).
|===



