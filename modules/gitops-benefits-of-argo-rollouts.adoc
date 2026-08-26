// Module is included in the following assemblies:
//
// * cicd/gitops/using-argo-rollouts-for-progressive-deployment-delivery.adoc

:_mod-docs-content-type: CONCEPT
[id="gitops-benefits-of-argo-rollouts_{context}"]
= Benefits of Argo Rollouts

Managing and coordinating advanced deployment strategies in traditional infrastructure often involves long maintenance windows. Automation with tools like {product-title} and {gitops-title} can reduce these windows, but setting up these strategies can still be challenging. With Argo Rollouts, you simplify this process by allowing application teams to define their rollout strategy declaratively. Teams no longer need to define multiple deployments and services or create automation for traffic shaping and integration of tests. Using Argo Rollouts, you can encapsulate all the required definitions for a declarative rollout strategy, automate and manage the process.

Using Argo Rollouts as a default workload in {gitops-title} provides the following benefits:

* Automated progressive delivery as part of the {gitops-shortname} workflow
* Advanced deployment capabilities
* Optimize the existing advanced deployment strategies such as blue-green or canary
* Zero downtime updates for deployments
* Fine-grained, weighted traffic shifting
* Able to test without any new traffic hitting the production environment
* Automated rollbacks and promotions
* Manual judgment
* Customizable metric queries and analysis of business key performance indicators (KPIs)
* Integration with ingress controller and {SMProductName} for advanced traffic routing
* Integration with metric providers for deployment strategy analysis
* Usage of multiple providers

With Argo Rollouts, users can more easily adopt progressive delivery in end-user environments. This provides structure and guidelines without requiring teams to learn about traffic managers and complex infrastructure. With automated rollouts, the {gitops-title} Operator provides security to your end-user environments and helps manage the resources, cost, and time effectively. Existing users who use Argo CD with security and automated deployments get feedback early in the process and avoid problems that impact them.