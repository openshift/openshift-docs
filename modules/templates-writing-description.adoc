// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

[id="templates-writing-description_{context}"]
= Writing the template description

The template description informs you what the template does and helps you find it when searching in the web console. Additional metadata beyond the template name is optional, but useful to have. In addition to general descriptive information, the metadata also includes a set of tags. Useful tags include the name of the language the template is related to for example, Java, PHP, Ruby, and so on.

The following is an example of template description metadata:

[source,yaml]
----
kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: cakephp-mysql-example <1>
  annotations:
    openshift.io/display-name: "CakePHP MySQL Example (Ephemeral)" <2>
    description: >-
      An example CakePHP application with a MySQL database. For more information
      about using this template, including OpenShift considerations, see
      https://github.com/sclorg/cakephp-ex/blob/master/README.md.


      WARNING: Any data stored will be lost upon pod destruction. Only use this
      template for testing." <3>
    openshift.io/long-description: >-
      This template defines resources needed to develop a CakePHP application,
      including a build configuration, application DeploymentConfig, and
      database DeploymentConfig.  The database is stored in
      non-persistent storage, so this configuration should be used for
      experimental purposes only. <4>
    tags: "quickstart,php,cakephp" <5>
    iconClass: icon-php <6>
    openshift.io/provider-display-name: "Red Hat, Inc." <7>
    openshift.io/documentation-url: "https://github.com/sclorg/cakephp-ex" <8>
    openshift.io/support-url: "https://access.redhat.com" <9>
message: "Your admin credentials are ${ADMIN_USERNAME}:${ADMIN_PASSWORD}" <10>
----
<1> The unique name of the template.
<2> A brief, user-friendly name, which can be employed by user interfaces.
<3> A description of the template. Include enough detail that users understand what is being deployed and any caveats they must know before deploying. It should also provide links to additional information, such as a README file. Newlines can be included to create paragraphs.
<4> Additional template description. This may be displayed by the service catalog, for example.
<5> Tags to be associated with the template for searching and grouping. Add tags that include it into one of the provided catalog categories. Refer to the `id` and `categoryAliases` in `CATALOG_CATEGORIES` in the console constants file.
ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
The categories can also be customized for the whole cluster.
endif::[]
<6> An icon to be displayed with your template in the web console.
+
.Available icons
[%collapsible]
====
* `icon-3scale`
* `icon-aerogear`
* `icon-amq`
* `icon-angularjs`
* `icon-ansible`
* `icon-apache`
* `icon-beaker`
* `icon-camel`
* `icon-capedwarf`
* `icon-cassandra`
* `icon-catalog-icon`
* `icon-clojure`
* `icon-codeigniter`
* `icon-cordova`
* `icon-datagrid`
* `icon-datavirt`
* `icon-debian`
* `icon-decisionserver`
* `icon-django`
* `icon-dotnet`
* `icon-drupal`
* `icon-eap`
* `icon-elastic`
* `icon-erlang`
* `icon-fedora`
* `icon-freebsd`
* `icon-git`
* `icon-github`
* `icon-gitlab`
* `icon-glassfish`
* `icon-go-gopher`
* `icon-golang`
* `icon-grails`
* `icon-hadoop`
* `icon-haproxy`
* `icon-helm`
* `icon-infinispan`
* `icon-jboss`
* `icon-jenkins`
* `icon-jetty`
* `icon-joomla`
* `icon-jruby`
* `icon-js`
* `icon-knative`
* `icon-kubevirt`
* `icon-laravel`
* `icon-load-balancer`
* `icon-mariadb`
* `icon-mediawiki`
* `icon-memcached`
* `icon-mongodb`
* `icon-mssql`
* `icon-mysql-database`
* `icon-nginx`
* `icon-nodejs`
* `icon-openjdk`
* `icon-openliberty`
* `icon-openshift`
* `icon-openstack`
* `icon-other-linux`
* `icon-other-unknown`
* `icon-perl`
* `icon-phalcon`
* `icon-php`
* `icon-play`
* `iconpostgresql`
* `icon-processserver`
* `icon-python`
* `icon-quarkus`
* `icon-rabbitmq`
* `icon-rails`
* `icon-redhat`
* `icon-redis`
* `icon-rh-integration`
* `icon-rh-spring-boot`
* `icon-rh-tomcat`
* `icon-ruby`
* `icon-scala`
* `icon-serverlessfx`
* `icon-shadowman`
* `icon-spring-boot`
* `icon-spring`
* `icon-sso`
* `icon-stackoverflow`
* `icon-suse`
* `icon-symfony`
* `icon-tomcat`
* `icon-ubuntu`
* `icon-vertx`
* `icon-wildfly`
* `icon-windows`
* `icon-wordpress`
* `icon-xamarin`
* `icon-zend`
====
<7> The name of the person or organization providing the template.
<8> A URL referencing further documentation for the template.
<9> A URL where support can be obtained for the template.
<10> An instructional message that is displayed when this template is instantiated. This field should inform the user how to use the newly created resources. Parameter substitution is performed on the message before being displayed so that generated credentials and other parameters can be included in the output. Include links to any next-steps documentation that users should follow.
