// Module included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift.adoc

[id="configuring-groups-and-argocd-rbac_{context}"]
= Configure groups and Argo CD RBAC

Role-based access control (RBAC) allows you to provide relevant permissions to users.

.Prerequisites 

* You have created the `ArgoCDAdmins` group in Keycloak.

* The user you want to give permissions to has logged in to Argo CD.
 
.Procedure

. In the Keycloak dashboard navigate to *Users* -> *Groups*. Add the user to the Keycloak group `ArgoCDAdmins`. 

. Ensure that `ArgoCDAdmins` group has the required permissions in the `argocd-rbac` config map. 
** Edit the config map:  
+
[source,terminal]
----
$ oc edit configmap argocd-rbac-cm -n <namespace>
----
+
.Example of a config map that defines `admin` permissions. 
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-rbac-cm
data:
  policy.csv: |
    g, /ArgoCDAdmins, role:admin
----
