// Module included in the following assemblies:
//
// cli_reference/developer_cli_odo/creating-a-java-application-using-devfile

:_mod-docs-content-type: PROCEDURE
[id="listing-available-devfile-components_{context}"]
= Listing available devfile components

With `{odo-title}`, you can display all the components that are available for you on the cluster. Components that are available depend on the configuration of your cluster.

.Procedure

. To list available devfile components on your cluster, run:
+
[source,terminal]
----
$ odo catalog list components
----
+
The output lists the available `{odo-title}` components:
+
[source,terminal]
----
Odo Devfile Components:
NAME                 DESCRIPTION                            REGISTRY
java-maven           Upstream Maven and OpenJDK 11          DefaultDevfileRegistry
java-openliberty     Open Liberty microservice in Java      DefaultDevfileRegistry
java-quarkus         Upstream Quarkus with Java+GraalVM     DefaultDevfileRegistry
java-springboot      Spring Boot® using Java                DefaultDevfileRegistry
nodejs               Stack with NodeJS 12                   DefaultDevfileRegistry

Odo OpenShift Components:
NAME        PROJECT       TAGS                                                                           SUPPORTED
java        openshift     11,8,latest                                                                    YES
dotnet      openshift     2.1,3.1,latest                                                                 NO
golang      openshift     1.13.4-ubi7,1.13.4-ubi8,latest                                                 NO
httpd       openshift     2.4-el7,2.4-el8,latest                                                         NO
nginx       openshift     1.14-el7,1.14-el8,1.16-el7,1.16-el8,latest                                     NO
nodejs      openshift     10-ubi7,10-ubi8,12-ubi7,12-ubi8,latest                                         NO
perl        openshift     5.26-el7,5.26-ubi8,5.30-el7,latest                                             NO
php         openshift     7.2-ubi7,7.2-ubi8,7.3-ubi7,7.3-ubi8,latest                                     NO
python      openshift     2.7-ubi7,2.7-ubi8,3.6-ubi7,3.6-ubi8,3.8-ubi7,3.8-ubi8,latest                   NO
ruby        openshift     2.5-ubi7,2.5-ubi8,2.6-ubi7,2.6-ubi8,2.7-ubi7,latest                            NO
wildfly     openshift     10.0,10.1,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,8.1,9.0,latest     NO
----
