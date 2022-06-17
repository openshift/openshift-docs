// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/using-sample-applications.adoc

[id="odo-sample-applications-binary_{context}"]
= Binary example applications

Use the following commands to build and run sample applications from a binary file for a particular runtime.

[id="odo-sample-applications-binary-java_{context}"]
== java

Java can be used to deploy a binary artifact as follows:

[source,terminal]
----
$ git clone https://github.com/spring-projects/spring-petclinic.git
$ cd spring-petclinic
$ mvn package
$ odo create java test3 --binary target/*.jar
$ odo push
----


//Commenting out as it doesn't work for now. https://github.com/openshift/odo/issues/4623
////
[id="odo-sample-applications-binary-wildfly_{context}"]
== wildfly

WildFly can be used to deploy a binary application as follows:

[source,terminal]
----
$ git clone https://github.com/openshiftdemos/os-sample-java-web.git
$ cd os-sample-java-web
$ mvn package
$ cd ..
$ mkdir example && cd example
$ mv ../os-sample-java-web/target/ROOT.war example.war
$ odo create wildfly --binary example.war
----
////
