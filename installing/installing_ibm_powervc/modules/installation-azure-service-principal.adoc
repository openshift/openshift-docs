// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-account.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

ifeval::["{context}" == "installing-azure-stack-hub-user-infra"]
:ash:
endif::[]
ifeval::["{context}" == "installing-azure-stack-hub-account"]
:ash:
endif::[]
ifeval::["{context}" == "installing-azure-account"]
:ipi:
endif::[]
ifeval::["{context}" == "installing-azure-user-infra"]
:upi:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-azure-user-provisioned"]
:upi:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="installation-azure-service-principal_{context}"]
= Creating a service principal

Because {product-title} and its installation program create Microsoft Azure resources by using the Azure Resource Manager, you must create a service principal to represent it.

.Prerequisites

* Install or update the link:https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest[Azure CLI].
* Your Azure account has the required roles for the subscription that you use.
ifdef::ipi[]
* If you want to use a custom role, you have created a link:https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles[custom role] with the required permissions listed in the _Required Azure permissions for installer-provisioned infrastructure_ section.
endif::ipi[]
ifdef::upi[]
* If you want to use a custom role, you have created a link:https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles[custom role] with the required permissions listed in the _Required Azure permissions for user-provisioned infrastructure_ section.
endif::upi[]

.Procedure

ifdef::ash[]
. Register your environment:
+
[source,terminal]
----
$ az cloud register -n AzureStackCloud --endpoint-resource-manager <endpoint> <1>
----
<1> Specify the Azure Resource Manager endpoint, \`https://management.<region>.<fqdn>/`.
+
See the link:https://docs.microsoft.com/en-us/azure-stack/mdc/azure-stack-version-profiles-azurecli-2-tzl#connect-to-azure-stack-hub[Microsoft documentation] for details.

. Set the active environment:
+
[source,terminal]
----
$ az cloud set -n AzureStackCloud
----

. Update your environment configuration to use the specific API version for Azure Stack Hub:
+
[source,terminal]
----
$ az cloud update --profile 2019-03-01-hybrid
----
endif::ash[]

. Log in to the Azure CLI:
+
[source,terminal]
----
$ az login
----
ifdef::ash[]
+
If you are in a multitenant environment, you must also supply the tenant ID.
endif::ash[]

. If your Azure account uses subscriptions, ensure that you are using the right
subscription:

.. View the list of available accounts and record the `tenantId` value for the
subscription you want to use for your cluster:
+
[source,terminal]
----
$ az account list --refresh
----
+
.Example output
[source,terminal]
----
[
  {
ifndef::ash[]
    "cloudName": "AzureCloud",
endif::[]
ifdef::ash[]
    "cloudName": AzureStackCloud",
endif::[]
    "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
    "isDefault": true,
    "name": "Subscription Name",
    "state": "Enabled",
    "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee",
    "user": {
      "name": "you@example.com",
      "type": "user"
    }
  }
]
----

.. View your active account details and confirm that the `tenantId` value matches
the subscription you want to use:
+
[source,terminal]
----
$ az account show
----
+
.Example output
[source,terminal]
----
{
ifndef::ash[]
  "environmentName": "AzureCloud",
endif::[]
ifdef::ash[]
  "environmentName": AzureStackCloud",
endif::[]
  "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
  "isDefault": true,
  "name": "Subscription Name",
  "state": "Enabled",
  "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee", <1>
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
----
<1> Ensure that the value of the `tenantId` parameter is the correct subscription ID.

.. If you are not using the right subscription, change the active subscription:
+
[source,terminal]
----
$ az account set -s <subscription_id> <1>
----
<1> Specify the subscription ID.

.. Verify the subscription ID update:
+
[source,terminal]
----
$ az account show
----
+
.Example output
[source,terminal]
----
{
ifndef::ash[]
  "environmentName": "AzureCloud",
endif::[]
ifdef::ash[]
  "environmentName": AzureStackCloud",
endif::[]
  "id": "33212d16-bdf6-45cb-b038-f6565b61edda",
  "isDefault": true,
  "name": "Subscription Name",
  "state": "Enabled",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee",
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
----

. Record the `tenantId` and `id` parameter values from the output. You need these values during the {product-title} installation.

ifdef::ash[]
. Create the service principal for your account:
+
[source,terminal]
----
$ az ad sp create-for-rbac --role Contributor --name <service_principal> \ <1>
  --scopes /subscriptions/<subscription_id> <2>
  --years <years> <3>
----
<1> Specify the service principal name.
<2> Specify the subscription ID.
<3> Specify the number of years. By default, a service principal expires in one year. By using the `--years` option you can extend the validity of your service principal.
+
.Example output
[source,terminal]
----
Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
The output includes credentials that you must protect. Be sure that you do not
include these credentials in your code or check the credentials into your source
control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "ac461d78-bf4b-4387-ad16-7e32e328aec6",
  "displayName": <service_principal>",
  "password": "00000000-0000-0000-0000-000000000000",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee"
}
----
endif::ash[]

ifndef::ash[]
. Create the service principal for your account:
+
[source,terminal]
----
$ az ad sp create-for-rbac --role <role_name> \// <1>
     --name <service_principal> \// <2>
     --scopes /subscriptions/<subscription_id> <3>
----
<1> Defines the role name. You can use the `Contributor` role, or you can specify a custom role which contains the necessary permissions.
<2> Defines the service principal name.
<3> Specifies the subscription ID.
+
.Example output
[source,terminal]
----
Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
The output includes credentials that you must protect. Be sure that you do not
include these credentials in your code or check the credentials into your source
control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "ac461d78-bf4b-4387-ad16-7e32e328aec6",
  "displayName": <service_principal>",
  "password": "00000000-0000-0000-0000-000000000000",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee"
}
----
endif::ash[]

. Record the values of the `appId` and `password` parameters from the previous
output. You need these values during {product-title} installation.

ifndef::ash[]
. If you applied the `Contributor` role to your service principal, assign the `User Administrator Access` role by running the following command:
+
[source,terminal]
----
$ az role assignment create --role "User Access Administrator" \
  --assignee-object-id $(az ad sp show --id <appId> --query id -o tsv) <1>
----
<1> Specify the `appId` parameter value for your service principal.
endif::ash[]

ifeval::["{context}" == "installing-azure-stack-hub-user-infra"]
:!ash:
endif::[]
ifeval::["{context}" == "installing-azure-stack-hub-account"]
:!ash:
endif::[]
ifeval::["{context}" == "installing-azure-account"]
:!ipi:
endif::[]
ifeval::["{context}" == "installing-azure-user-infra"]
:!upi:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-azure-user-provisioned"]
:!upi:
endif::[]
