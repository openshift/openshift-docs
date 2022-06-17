// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/using-sample-applications.adoc

[id="odo-sample-applications-github_{context}"]
= Git repository example applications

Use the following commands to build and run sample applications from a Git repository for a particular runtime.

[id="odo-sample-applications-github-httpd_{context}"]
== httpd

This example helps build and serve static content using httpd on CentOS 7. For more information about using this builder image, including {product-title} considerations, see the link:https://github.com/sclorg/httpd-container/blob/master/2.4/root/usr/share/container-scripts/httpd/README.md[Apache HTTP Server container image repository].

[source,terminal]
----
$ odo create httpd --git https://github.com/openshift/httpd-ex.git
----

[id="odo-sample-applications-github-java_{context}"]
== java

This example helps build and run fat JAR Java applications on CentOS 7. For more information about using this builder image, including {product-title} considerations, see the link:https://github.com/fabric8io-images/s2i/blob/master/README.md[Java S2I Builder image].

[source,terminal]
----
$ odo create java --git https://github.com/spring-projects/spring-petclinic.git
----

[id="odo-sample-applications-github-nodejs_{context}"]
== nodejs

Build and run Node.js applications on CentOS 7. For more information about using this builder image, including {product-title} considerations, see the link:https://github.com/sclorg/s2i-nodejs-container/blob/master/8/README.md[Node.js 8 container image].

[source,terminal]
----
$ odo create nodejs --git https://github.com/openshift/nodejs-ex.git
----

[id="odo-sample-applications-github-perl_{context}"]
== perl

This example helps build and run Perl applications on CentOS 7. For more information about using this builder image, including {product-title} considerations, see the link:https://github.com/sclorg/s2i-perl-container/blob/master/5.26/README.md[Perl 5.26 container image].

[source,terminal]
----
$ odo create perl --git https://github.com/openshift/dancer-ex.git
----

[id="odo-sample-applications-github-php_{context}"]
== php

This example helps build and run PHP applications on CentOS 7. For more information about using this builder image, including {product-title} considerations, see the link:https://github.com/sclorg/s2i-php-container/blob/master/7.1/README.md[PHP 7.1 Docker image].

[source,terminal]
----
$ odo create php --git https://github.com/openshift/cakephp-ex.git
----

[id="odo-sample-applications-github-python_{context}"]
== python

This example helps build and run Python applications on CentOS 7. For more information about using this builder image, including {product-title} considerations, see the link:https://github.com/sclorg/s2i-python-container/blob/master/3.6/README.md[Python 3.6 container image].

[source,terminal]
----
$ odo create python --git https://github.com/openshift/django-ex.git
----

[id="odo-sample-applications-github-ruby_{context}"]
== ruby

This example helps build and run Ruby applications on CentOS 7. For more information about using this builder image, including {product-title} considerations, see link:https://github.com/sclorg/s2i-ruby-container/blob/master/2.5/README.md[Ruby 2.5 container image].

[source,terminal]
----
$ odo create ruby --git https://github.com/openshift/ruby-ex.git
----

//Commenting out as it doesn't work for now. https://github.com/openshift/odo/issues/4623
////
[id="odo-sample-applications-github-wildfly_{context}"]
== wildfly

This example helps build and run WildFly applications on CentOS 7. For more information about using this builder image, including {product-title} considerations, see the link:https://github.com/wildfly/wildfly-s2i/blob/master/README.md[Wildfly - CentOS Docker images for OpenShift].

[source,terminal]
----
$ odo create wildfly --git https://github.com/openshift/openshift-jee-sample.git
----
////
