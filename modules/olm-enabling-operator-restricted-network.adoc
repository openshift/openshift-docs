// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-enabling-operator-for-restricted-network_{context}"]
= Enabling your Operator for restricted network environments

As an Operator author, your Operator must meet additional requirements to run properly in a restricted network, or disconnected, environment.

.Operator requirements for supporting disconnected mode

* Replace hard-coded image references with environment variables.
* In the cluster service version (CSV) of your Operator:
** List any _related images_, or other container images that your Operator might require to perform their functions.
** Reference all specified images by a digest (SHA) and not by a tag.
* All dependencies of your Operator must also support running in a disconnected mode.
* Your Operator must not require any off-cluster resources.
// TODO: Include more info w/ better steps on how to do this:
//* You must understand the {product-title} proxy configuration.

.Prerequisites

* An Operator project with a CSV. The following procedure uses the Memcached Operator as an example for Go-, Ansible-, and Helm-based projects.

.Procedure

. Set an environment variable for the additional image references used by the Operator in the `config/manager/manager.yaml` file:
+
.Example `config/manager/manager.yaml` file
[%collapsible]
====
[source,yaml]
----
...
spec:
  ...
    spec:
      ...
      containers:
      - command:
        - /manager
        ...
        env:
        - name: <related_image_environment_variable> <1>
          value: "<related_image_reference_with_tag>" <2>
----
<1> Define the environment variable, such as `RELATED_IMAGE_MEMCACHED`.
<2> Set the related image reference and tag, such as `docker.io/memcached:1.4.36-alpine`.
====

. Replace hard-coded image references with environment variables in the relevant file for your Operator project type:

* For Go-based Operator projects, add the environment variable to the `controllers/memcached_controller.go` file as shown in the following example:
+
.Example `controllers/memcached_controller.go` file
[%collapsible]
====
[source,diff]
----
  // deploymentForMemcached returns a memcached Deployment object

...

	Spec: corev1.PodSpec{
        	Containers: []corev1.Container{{
-			Image:   "memcached:1.4.36-alpine", <1>
+			Image:   os.Getenv("<related_image_environment_variable>"), <2>
			Name:    "memcached",
			Command: []string{"memcached", "-m=64", "-o", "modern", "-v"},
			Ports: []corev1.ContainerPort{{

...
----
<1> Delete the image reference and tag.
<2> Use the `os.Getenv` function to call the `<related_image_environment_variable>`.

[NOTE]
=====
The `os.Getenv` function returns an empty string if a variable is not set. Set the `<related_image_environment_variable>` before changing the file.
=====
====

* For Ansible-based Operator projects, add the environment variable to the `roles/memcached/tasks/main.yml` file as shown in the following example:
+
.Example `roles/memcached/tasks/main.yml` file
[%collapsible]
====
[source,diff]
----
spec:
  containers:
  - name: memcached
    command:
    - memcached
    - -m=64
    - -o
    - modern
    - -v
-   image: "docker.io/memcached:1.4.36-alpine" <1>
+   image: "{{ lookup('env', '<related_image_environment_variable>') }}" <2>
    ports:
      - containerPort: 11211

...
----
<1> Delete the image reference and tag.
<2> Use the `lookup` function to call the `<related_image_environment_variable>`.
====

* For Helm-based Operator projects, add the `overrideValues` field to the `watches.yaml` file as shown in the following example:
+
.Example `watches.yaml` file
[%collapsible]
====
[source,yaml]
----
...
- group: demo.example.com
  version: v1alpha1
  kind: Memcached
  chart: helm-charts/memcached
  overrideValues: <1>
    relatedImage: ${<related_image_environment_variable>} <2>
----
<1> Add the `overrideValues` field.
<2> Define the `overrideValues` field by using the `<related_image_environment_variable>`, such as `RELATED_IMAGE_MEMCACHED`.
====

.. Add the value of the `overrideValues` field to the `helm-charts/memchached/values.yaml` file as shown in the following example:
+
.Example `helm-charts/memchached/values.yaml` file
[source,yaml]
----
...
relatedImage: ""
----

.. Edit the chart template in the `helm-charts/memcached/templates/deployment.yaml` file as shown in the following example:
+
.Example `helm-charts/memcached/templates/deployment.yaml` file
[%collapsible]
====
[source,yaml]
----
containers:
  - name: {{ .Chart.Name }}
    securityContext:
      - toYaml {{ .Values.securityContext | nindent 12 }}
    image: "{{ .Values.image.pullPolicy }}
    env: <1>
      - name: related_image <2>
        value: "{{ .Values.relatedImage }}" <3>
----
<1> Add the `env` field.
<2> Name the environment variable.
<3> Define the value of the environment variable.
====

. Add the `BUNDLE_GEN_FLAGS` variable definition to your `Makefile` with the following changes:
+
.Example `Makefile`
[source,diff]
----
   BUNDLE_GEN_FLAGS ?= -q --overwrite --version $(VERSION) $(BUNDLE_METADATA_OPTS)

   # USE_IMAGE_DIGESTS defines if images are resolved via tags or digests
   # You can enable this value if you would like to use SHA Based Digests
   # To enable set flag to true
   USE_IMAGE_DIGESTS ?= false
   ifeq ($(USE_IMAGE_DIGESTS), true)
         BUNDLE_GEN_FLAGS += --use-image-digests
   endif

...

-  $(KUSTOMIZE) build config/manifests | operator-sdk generate bundle -q --overwrite --version $(VERSION) $(BUNDLE_METADATA_OPTS) <1>
+  $(KUSTOMIZE) build config/manifests | operator-sdk generate bundle $(BUNDLE_GEN_FLAGS) <2>

...
----
<1> Delete this line in the `Makefile`.
<2> Replace the line above with this line.

. To update your Operator image to use a digest (SHA) and not a tag, run the `make bundle` command and set `USE_IMAGE_DIGESTS` to `true` :
+
[source,terminal]
----
$ make bundle USE_IMAGE_DIGESTS=true
----

. Add the `disconnected` annotation, which indicates that the Operator works in a disconnected environment:
+
[source,yaml]
----
metadata:
  annotations:
    operators.openshift.io/infrastructure-features: '["disconnected"]'
----
+
Operators can be filtered in OperatorHub by this infrastructure feature.
