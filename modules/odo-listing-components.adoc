// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/understanding-odo.adoc

:_mod-docs-content-type: PROCEDURE
[id="odo-listing-components_{context}"]

= Listing components in odo

`odo` uses the portable _devfile_ format to describe components and their related URLs, storage, and services. `odo` can connect to various devfile registries to download devfiles for different languages and frameworks. See the documentation for the `odo registry` command for more information on how to manage the registries used by `odo` to retrieve devfile information.


You can list all the _devfiles_ available of the different registries with the `odo catalog list components` command.

.Procedure

. Log in to the cluster with `{odo-title}`:
+
[source,terminal]
----
$ odo login -u developer -p developer
----

. List the available `{odo-title}` components:
+
[source,terminal]
----
$ odo catalog list components
----
+
.Example output
[source,terminal]
----
Odo Devfile Components:
NAME                             DESCRIPTION                                                         REGISTRY
dotnet50                         Stack with .NET 5.0                                                 DefaultDevfileRegistry
dotnet60                         Stack with .NET 6.0                                                 DefaultDevfileRegistry
dotnetcore31                     Stack with .NET Core 3.1                                            DefaultDevfileRegistry
go                               Stack with the latest Go version                                    DefaultDevfileRegistry
java-maven                       Upstream Maven and OpenJDK 11                                       DefaultDevfileRegistry
java-openliberty                 Java application Maven-built stack using the Open Liberty ru...     DefaultDevfileRegistry
java-openliberty-gradle          Java application Gradle-built stack using the Open Liberty r...     DefaultDevfileRegistry
java-quarkus                     Quarkus with Java                                                   DefaultDevfileRegistry
java-springboot                  Spring Boot® using Java                                             DefaultDevfileRegistry
java-vertx                       Upstream Vert.x using Java                                          DefaultDevfileRegistry
java-websphereliberty            Java application Maven-built stack using the WebSphere Liber...     DefaultDevfileRegistry
java-websphereliberty-gradle     Java application Gradle-built stack using the WebSphere Libe...     DefaultDevfileRegistry
java-wildfly                     Upstream WildFly                                                    DefaultDevfileRegistry
java-wildfly-bootable-jar        Java stack with WildFly in bootable Jar mode, OpenJDK 11 and...     DefaultDevfileRegistry
nodejs                           Stack with Node.js 14                                               DefaultDevfileRegistry
nodejs-angular                   Stack with Angular 12                                               DefaultDevfileRegistry
nodejs-nextjs                    Stack with Next.js 11                                               DefaultDevfileRegistry
nodejs-nuxtjs                    Stack with Nuxt.js 2                                                DefaultDevfileRegistry
nodejs-react                     Stack with React 17                                                 DefaultDevfileRegistry
nodejs-svelte                    Stack with Svelte 3                                                 DefaultDevfileRegistry
nodejs-vue                       Stack with Vue 3                                                    DefaultDevfileRegistry
php-laravel                      Stack with Laravel 8                                                DefaultDevfileRegistry
python                           Python Stack with Python 3.7                                        DefaultDevfileRegistry
python-django                    Python3.7 with Django                                               DefaultDevfileRegistry
----
