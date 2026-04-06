# OpenShift GitOps - All Job Statements
**Total Jobs**: 171
**Generated**: 2026-04-06

---

## Unknown

**Jobs**: 171

### Main Jobs

1. **When managing OpenShift nodes through GitOps workflows with machine configurations, I want to understand how MCO auto-reboots interact with Argo CD sync operations, so I can anticipate and prevent disruptions to my GitOps automation.**
   - Persona: Platform engineer
   - Stage: Troubleshoot

2. **When managing multiple users accessing Argo CD, I want to configure single sign-on integration, so I can centralize authentication and leverage existing identity providers**
   - Persona: Cluster administrator
   - Stage: Prepare

3. **When deploying Argo CD in a namespace with resource quotas, I want to configure resource requests and limits for Argo CD workloads, so I can ensure successful deployment and prevent quota-related failures.**
   - Persona: Cluster administrator
   - Stage: Configure

4. **When I need to troubleshoot GitOps deployments or understand system behavior, I want to access and view Argo CD logs, so I can diagnose issues and monitor the health of my GitOps workflows.**
   - Persona: Platform engineer
   - Stage: Observe

5. **When setting up GitOps environments, I want to configure proper labels and annotations on application and namespace manifests, so I can ensure the environment displays correctly in the OpenShift web console**
   - Persona: Platform Engineer
   - Stage: Prepare

6. **When operating GitOps-managed applications, I want to monitor the health and synchronization status of all environment deployments, so I can quickly identify and address issues impacting application availability**
   - Persona: DevOps Engineer
   - Stage: Monitor

7. **When I encounter issues with my GitOps deployment, I want to collect comprehensive diagnostic information, so I can provide Red Hat Support with the data needed to resolve my issue quickly.**
   - Persona: Cluster administrator
   - Stage: Troubleshoot

8. **When setting up GitOps infrastructure, I want to understand the Argo CD custom resource properties, so I can configure my Argo CD cluster to meet my organization's requirements**
   - Persona: Platform Engineer
   - Stage: Define

9. **When configuring Argo CD components, I want to reference comprehensive property specifications, so I can customize ApplicationSet, Controller, HA, Notifications, Server, SSO, and other components correctly**
   - Persona: Platform Engineer
   - Stage: Prepare

10. **When configuring repository server component, I want to set resource limits, TLS settings, timeouts, and replicas, so I can ensure reliable Git repository access and rendering performance**
   - Persona: Platform Engineer
   - Stage: Prepare

11. **When setting up GitOps alerting, I want to enable the Argo CD notifications controller, so I can receive alerts about application sync status and operational events**
   - Persona: Platform Engineer
   - Stage: Prepare

12. **When I need to understand what OpenShift GitOps is and its capabilities, I want to learn about its features and relationship to Argo CD, so I can determine if it meets my GitOps workflow needs.**
   - Persona: Platform administrator
   - Stage: Get Started

13. **When planning a GitOps deployment or upgrade, I want to verify component compatibility with my OpenShift version, so I can ensure all features will work correctly in my environment.**
   - Persona: Platform Administrator
   - Stage: Plan

14. **When evaluating new GitOps features, I want to identify which features are in Technology Preview versus General Availability, so I can decide whether they are safe to use in production.**
   - Persona: Platform Administrator
   - Stage: Plan

15. **When a new GitOps version is released, I want to understand what new capabilities are available, so I can determine if they solve my current pain points or enable new use cases.**
   - Persona: Platform Administrator
   - Stage: What's New

16. **When planning an upgrade, I want to know which features are being deprecated or removed, so I can prepare for migration and avoid breaking my existing deployments.**
   - Persona: Platform Administrator
   - Stage: Plan

17. **When experiencing issues with the current version, I want to check if my problem is a known bug that has been fixed in the new release, so I can decide if upgrading will resolve my issue.**
   - Persona: Platform Administrator
   - Stage: Troubleshoot

18. **When planning to deploy or upgrade GitOps, I want to be aware of known issues and their workarounds, so I can avoid or mitigate problems proactively.**
   - Persona: Platform Administrator
   - Stage: Troubleshoot

19. **When implementing continuous deployment for cloud native applications, I want to understand what GitOps can help me achieve, so I can determine if it fits my use case.**
   - Persona: DevOps Engineer
   - Stage: Plan

20. **When I need to manage cluster-scoped resources with GitOps, I want to configure my Argo CD instance with appropriate permissions, so I can automate cluster configuration through Git without manual intervention.**
   - Persona: Cluster administrator
   - Stage: Configure

21. **When planning my Argo CD deployment, I want to understand the default permission model, so I can determine what additional permissions I need to configure.**
   - Persona: Cluster administrator
   - Stage: Plan

22. **When operating a production cluster with infrastructure nodes, I want to run Argo CD on dedicated infrastructure nodes, so I can isolate GitOps workloads from application workloads and ensure predictable performance.**
   - Persona: Platform engineer
   - Stage: Configure

23. **When I need to deploy cluster configurations via GitOps, I want to create an Argo CD application pointing to my Git repository, so I can manage cluster state declaratively.**
   - Persona: Cluster administrator
   - Stage: Deploy

24. **When my Argo CD application is created with manual sync policy, I want to trigger synchronization, so I can apply Git repository changes to the cluster in a controlled manner.**
   - Persona: Cluster administrator
   - Stage: Execute

25. **When default Argo CD permissions are insufficient, I want to create custom cluster roles and bindings, so I can enable Argo CD to manage additional cluster resources securely.**
   - Persona: Cluster administrator
   - Stage: Configure

26. **When managing cluster configuration as code, I want to automate Operator installation via GitOps, so I can eliminate manual Operator installation procedures and ensure consistent Operator deployments across clusters.**
   - Persona: Cluster administrator
   - Stage: Deploy

27. **When I need to implement continuous deployment for cloud-native applications, I want to use a declarative approach that manages infrastructure and application configurations through Git, so I can create repeatable processes across multi-cluster Kubernetes environments and automate complex deployments**
   - Persona: Platform Engineer
   - Stage: Define

28. **When deploying applications to multiple clusters in different environments, I want to ensure consistency using a GitOps tool that maintains cluster resources through continuous monitoring and reconciliation, so I can keep configurations in sync with their desired state**
   - Persona: Cluster Administrator
   - Stage: Execute

### User Stories

1. When experiencing performance issues or sync failures due to MCO node reboots during Argo CD operations, I want to prevent auto-reboots from interrupting GitOps workflows, so I can ensure reliable and complete application deployments.
2. When setting up SSO integration, I want to register Argo CD as a client in Keycloak, so I can establish the trust relationship for authentication
3. When managing user permissions through SSO, I want to configure group claims in the authentication token, so I can map organizational groups to Argo CD roles
4. When connecting Argo CD to Keycloak, I want to configure OIDC settings with client credentials, so I can enable Keycloak-based authentication for Argo CD users
5. When leveraging existing OpenShift authentication, I want to configure Keycloak as an identity broker for OpenShift, so I can enable single sign-on between OpenShift cluster and Keycloak
6. When enabling identity brokering, I want to register a Keycloak OAuth client in OpenShift, so I can allow Keycloak to authenticate users against the OpenShift identity provider
7. When controlling user access in Argo CD, I want to map Keycloak groups to Argo CD roles, so I can enforce role-based access control based on organizational groups
8. When understanding Argo CD's access scope, I want to review the in-built permissions granted to Argo CD, so I can assess what cluster resources Argo CD can manage
9. As a cluster administrator, when I need to integrate Argo CD with existing OpenShift users and groups, I want to enable Dex with OpenShift OAuth connector, so I can leverage platform authentication without managing separate user databases.
10. As a cluster administrator, when I need to grant admin privileges to specific users in Argo CD, I want to map OpenShift users to Argo CD roles through groups, so I can control access permissions without direct ClusterRoleBinding.
11. As a cluster administrator, when I want to use an alternative SSO provider or disable SSO entirely, I want to disable Dex in the GitOps Operator, so I can configure authentication according to my security requirements.
12. As a cluster administrator, when I need to manage Dex SSO configuration, I want to use the .spec.sso parameter in the ArgoCD custom resource, so I can enable or disable SSO using the current recommended approach.
13. When deploying Argo CD to a quota-restricted namespace, I want to specify resource requests and limits for each workload component in the custom resource definition, so I can satisfy quota requirements and ensure proper resource allocation.
14. When resource requirements change after Argo CD deployment, I want to update resource requests and limits using kubectl patch, so I can adjust allocations without recreating the entire instance.
15. When resource quotas are no longer enforced or need to be removed, I want to delete resource requests and limits from Argo CD workloads, so I can restore default resource behavior.
16. When I need to troubleshoot GitOps issues, I want to use the Kibana dashboard to store and retrieve Argo CD logs with custom filters, so I can quickly find relevant log entries for specific namespaces or pods.
17. When creating GitOps application manifests, I want to set matching environment labels and namespace destinations, so I can link applications to their deployment environments in the console
18. When creating GitOps namespace manifests, I want to annotate with version control source details, so I can track the Git repository and branch for each environment
19. When checking application health via the OpenShift console, I want to view all environments and their synchronization status in one page, so I can get a quick overview of deployment health across environments
20. When investigating application health issues via the OpenShift console, I want to drill down into specific applications and view resource status details, so I can identify which resources are degraded or delayed
21. When auditing or troubleshooting deployments via the OpenShift console, I want to view the deployment history with commit details, so I can correlate application changes with Git commits and identify what changed when
22. When I need to understand what diagnostic data can be collected, I want to learn about the must-gather tool's capabilities and options, so I can choose the appropriate collection method for my issue.
23. When I have a GitOps-specific issue, I want to collect targeted diagnostic data for the GitOps Operator and ArgoCD components, so I can provide support with GitOps-focused troubleshooting information.
24. When configuring Argo CD, I want to know which command-line tools are supported, so I can avoid using unsupported methods and use the correct interface
25. When configuring ApplicationSet controller, I want to set image, version, resources, log level, log format, and parallelism limits, so I can optimize ApplicationSet operations for my cluster
26. When scaling Argo CD for large cluster counts, I want to configure controller sharding and resource allocations, so I can relieve memory pressure and process applications efficiently
27. When ensuring Argo CD resilience, I want to enable high availability mode with Redis HAProxy, so I can prevent GitOps outages and maintain continuous operations
28. When configuring Argo CD server component, I want to set autoscaling, replicas, routes, and resource limits, so I can handle varying load and expose the UI securely
29. When integrating enterprise authentication, I want to configure SSO with Keycloak or Dex, so I can centralize user access and enforce organizational identity policies
30. When enforcing access controls, I want to define RBAC policies and default roles, so I can restrict API operations to authorized users and teams
31. When ensuring secure repository access, I want to configure TLS verification and auto-TLS for repo server, so I can prevent man-in-the-middle attacks and encrypt Git communications
32. When managing progressive application rollouts, I want to understand how to use ApplicationSet Progressive Rollout Strategy, so I can deploy updates incrementally instead of simultaneously.
33. When running GitOps on ARM architecture, I want to understand platform compatibility and limitations, so I can deploy successfully on ARM-based OpenShift clusters.
34. When monitoring Argo CD components, I want to enable workload monitoring and alerts for my instances, so I can detect when component replicas drift from desired state.
35. When managing large Git repositories with manifests, I want to configure repo server arguments for maximum manifest size, so I can prevent failures when processing large directory structures.
36. When upgrading GitOps versions, I want to understand how the skipRange annotation affects my upgrade path, so I can plan for direct upgrades skipping intermediate versions.
37. When integrating Argo CD with OpenShift authentication, I want to use RH-SSO to log in with OpenShift credentials including kube:admin, so I can provide seamless access using existing identity infrastructure.
38. When addressing security vulnerabilities, I want to know what security updates are included in the release, so I can prioritize upgrades based on CVE severity.
39. As a cluster administrator, when configuring Argo CD for cluster-scoped management, I want to use the web console to edit the Subscription, so I can visually configure permissions without writing YAML.
40. As a cluster administrator, when I've configured Argo CD permissions, I want to verify the cluster role assignment, so I can confirm Argo CD can manage cluster-scoped resources before deploying applications.
41. As a cluster administrator, when creating an Argo CD application, I want to use the web dashboard, so I can configure the application visually without writing YAML manifests.
42. As a cluster administrator, after creating an Argo CD application, I want to label the target namespace for management, so I can ensure the Argo CD instance has permission to deploy resources there.
43. As a platform engineer, when creating an Argo CD application, I want to use the oc CLI tool, so I can automate application creation and manage it as code.
44. As a cluster administrator, after synchronizing cluster configurations, I want to verify the changes in the OpenShift console, so I can confirm the configurations were applied correctly.
45. When planning cluster configuration via GitOps, I want to understand what cluster-scoped resources Argo CD can manage by default, so I can determine if additional permissions are needed.
46. As a cluster administrator, when granting additional permissions, I want to use the web console to create cluster roles and bindings, so I can configure permissions without writing RBAC YAML.
47. As a cluster administrator, when installing cluster-scoped Operators via GitOps, I want to only manage the Subscription resource in Git, so I can leverage the default global-operators OperatorGroup and simplify my GitOps repository.
48. As a cluster administrator, when installing namespace-scoped Operators via GitOps, I want to manage both Subscription and OperatorGroup resources in Git, so I can ensure Operators are installed in the correct namespace with proper targeting.
49. When deploying multiple Operators to the same namespace via GitOps, I want to ensure only one OperatorGroup exists, so I can prevent CSV transition failures and ensure successful Operator installation.
50. When managing multiple OpenShift clusters, I want to automate configuration management tasks including state synchronization, change application/reversion, and application promotion, so I can efficiently manage cluster configurations and application deployments at scale

---

