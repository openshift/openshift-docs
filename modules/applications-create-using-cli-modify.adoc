[id="applications-create-using-cli-modify_{context}"]
= Modifying application creation

The `new-app` command generates {product-title} objects that build, deploy, and run the application that is created. Normally, these objects are created in the current project and assigned names that are derived from the input source repositories or the input images. However, with `new-app` you can modify this behavior.

.`new-app` output objects
[cols="2,8",options="header"]
|===

|Object |Description

|`BuildConfig`
|A `BuildConfig` object is created for each source repository that is specified in the command line. The `BuildConfig` object specifies the strategy to use, the source location, and the build output location.

|`ImageStreams`
|For the `BuildConfig` object, two image streams are usually created. One represents the input image. With source builds, this is the builder image.
ifndef::openshift-online[]
With `Docker` builds, this is the *FROM* image.
endif::[]
The second one represents the output image. If a container image was specified as input to `new-app`, then an image stream is created for that image as well.

|`DeploymentConfig`
|A `DeploymentConfig` object is created either to deploy the output of a build, or a specified image. The `new-app` command creates `emptyDir` volumes for all Docker volumes that are specified in containers included in the resulting `DeploymentConfig` object .

|`Service`
|The `new-app` command attempts to detect exposed ports in input images. It uses the lowest numeric exposed port to generate a service that exposes that port. To expose a different port, after `new-app` has completed, simply use the `oc expose` command to generate additional services.

|Other
|Other objects can be generated when instantiating templates, according to the template.

|===

[id="specifying-environment-variables"]
== Specifying environment variables

When generating applications from a template, source, or an image, you can use the `-e|--env` argument to pass environment variables to the application container at run time:

[source,terminal]
----
$ oc new-app openshift/postgresql-92-centos7 \
    -e POSTGRESQL_USER=user \
    -e POSTGRESQL_DATABASE=db \
    -e POSTGRESQL_PASSWORD=password
----

The variables can also be read from file using the `--env-file` argument. The following is an example file called `postgresql.env`:

[source,terminal]
----
POSTGRESQL_USER=user
POSTGRESQL_DATABASE=db
POSTGRESQL_PASSWORD=password
----

Read the variables from the file:

[source,terminal]
----
$ oc new-app openshift/postgresql-92-centos7 --env-file=postgresql.env
----

Additionally, environment variables can be given on standard input by using `--env-file=-`:

[source,terminal]
----
$ cat postgresql.env | oc new-app openshift/postgresql-92-centos7 --env-file=-
----

[NOTE]
====
Any `BuildConfig` objects created as part of `new-app` processing are not updated with environment variables passed with the `-e|--env` or `--env-file` argument.
====

[id="specifying-build-environment-variables"]
== Specifying build environment variables

When generating applications from a template, source, or an image, you can use the `--build-env` argument to pass environment variables to the build container at run time:

[source,terminal]
----
$ oc new-app openshift/ruby-23-centos7 \
    --build-env HTTP_PROXY=http://myproxy.net:1337/ \
    --build-env GEM_HOME=~/.gem
----

The variables can also be read from a file using the `--build-env-file` argument. The following is an example file called `ruby.env`:

[source,terminal]
----
HTTP_PROXY=http://myproxy.net:1337/
GEM_HOME=~/.gem
----

Read the variables from the file:

[source,terminal]
----
$ oc new-app openshift/ruby-23-centos7 --build-env-file=ruby.env
----

Additionally, environment variables can be given on standard input by using `--build-env-file=-`:

[source,terminal]
----
$ cat ruby.env | oc new-app openshift/ruby-23-centos7 --build-env-file=-
----

[id="specifying-labels"]
== Specifying labels

When generating applications from source, images, or templates, you can use the `-l|--label` argument to add labels to the created objects. Labels make it easy to collectively select, configure, and delete objects associated with the application.

[source,terminal]
----
$ oc new-app https://github.com/openshift/ruby-hello-world -l name=hello-world
----

[id="viewing-output-without-creation"]
== Viewing the output without creation

To see a dry-run of running the `new-app` command, you can use the `-o|--output` argument with a `yaml` or `json` value. You can then use the output to preview the objects that are created or redirect it to a file that you can edit. After you are satisfied, you can use `oc create` to create the {product-title} objects.

To output `new-app` artifacts to a file, run the following:

[source,terminal]
----
$ oc new-app https://github.com/openshift/ruby-hello-world \
    -o yaml > myapp.yaml
----

Edit the file:

[source,terminal]
----
$ vi myapp.yaml
----

Create a new application by referencing the file:

[source,terminal]
----
$ oc create -f myapp.yaml
----

[id="creating-objects-different-names"]
== Creating objects with different names

Objects created by `new-app` are normally named after the source repository, or the image used to generate them. You can set the name of the objects produced by adding a `--name` flag to the command:

[source,terminal]
----
$ oc new-app https://github.com/openshift/ruby-hello-world --name=myapp
----

[id="creating-objects-different-project"]
== Creating objects in a different project

Normally, `new-app` creates objects in the current project. However, you can create objects in a different project by using the `-n|--namespace` argument:

[source,terminal]
----
$ oc new-app https://github.com/openshift/ruby-hello-world -n myproject
----

[id="creating-multiple-objects"]
== Creating multiple objects

The `new-app` command allows creating multiple applications specifying multiple parameters to `new-app`. Labels specified in the command line apply to all objects created by the single command. Environment variables apply to all components created from source or images.

To create an application from a source repository and a Docker Hub image:

[source,terminal]
----
$ oc new-app https://github.com/openshift/ruby-hello-world mysql
----

[NOTE]
====
If a source code repository and a builder image are specified as separate arguments, `new-app` uses the builder image as the builder for the source code repository. If this is not the intent, specify the required builder image for the source using the `~` separator.
====

[id="grouping-images-source-single-pod"]
== Grouping images and source in a single pod

The `new-app` command allows deploying multiple images together in a single pod. To specify which images to group together, use the `+` separator. The `--group` command line argument can also be used to specify the images that should be grouped together. To group the image built from a source repository with other images, specify its builder image in the group:

[source,terminal]
----
$ oc new-app ruby+mysql
----

To deploy an image built from source and an external image together:

[source,terminal]
----
$ oc new-app \
    ruby~https://github.com/openshift/ruby-hello-world \
    mysql \
    --group=ruby+mysql
----

[id="searching-for-images-templates-other-inputs"]
== Searching for images, templates, and other inputs

To search for images, templates, and other inputs for the `oc new-app` command, add the `--search` and `--list` flags. For example, to find all of the images or templates that include PHP:

[source,terminal]
----
$ oc new-app --search php
----

[id="setting-the-import-mode"]
== Setting the import mode 

To set the import mode when using `oc new-app`, add the `--import-mode` flag. This flag can be appended with `Legacy` or `PreserveOriginal`, which provides users the option to create image streams using a single sub-manifest, or all manifests, respectively. 

[source,terminal]
----
$ oc new-app --image=registry.redhat.io/ubi8/httpd-24:latest  --import-mode=Legacy --name=test
----

[source,terminal]
----
$ oc new-app --image=registry.redhat.io/ubi8/httpd-24:latest  --import-mode=PreserveOriginal --name=test
----
