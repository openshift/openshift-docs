// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

:_mod-docs-content-type: CONCEPT
[id="images-other-jenkins-config-kubernetes_{context}"]
= Configuring the Jenkins Kubernetes plugin

The OpenShift Jenkins image includes the preinstalled link:https://wiki.jenkins-ci.org/display/JENKINS/Kubernetes+Plugin[Kubernetes plugin for Jenkins] so that Jenkins agents can be dynamically provisioned on multiple container hosts using Kubernetes and {product-title}.

To use the Kubernetes plugin, {product-title} provides an OpenShift Agent Base image that is suitable for use as a Jenkins agent.

[IMPORTANT]
====
{product-title} 4.11 moves the OpenShift Jenkins and OpenShift Agent Base images to the `ocp-tools-4` repository at `registry.redhat.io` so that Red Hat can produce and update the images outside the {product-title} lifecycle. Previously, these images were in the {product-title} install payload and the `openshift4` repository at `registry.redhat.io`.

The OpenShift Jenkins Maven and NodeJS Agent images were removed from the {product-title} 4.11 payload. Red Hat no longer produces these images, and they are not available from the `ocp-tools-4` repository at `registry.redhat.io`. Red Hat maintains the 4.10 and earlier versions of these images for any significant bug fixes or security CVEs, following the link:https://access.redhat.com/support/policy/updates/openshift[{product-title} lifecycle policy].

For more information, see the "Important changes to OpenShift Jenkins images" link in the following "Additional resources" section.
====

The Maven and Node.js agent images are automatically configured as Kubernetes pod template images within the {product-title} Jenkins image configuration for the Kubernetes plugin. That configuration includes labels for each image that you can apply to any of your Jenkins jobs under their `Restrict where this project can be run` setting. If the label is applied, jobs run under an {product-title} pod running the respective agent image.

[IMPORTANT]
====
In {product-title} 4.10 and later, the recommended pattern for running Jenkins agents using the Kubernetes plugin is to use pod templates with both `jnlp` and `sidecar` containers. The `jnlp` container uses the {product-title} Jenkins Base agent image to facilitate launching a separate pod for your build. The `sidecar` container image has the tools needed to build in a particular language within the separate pod that was launched. Many container images from the Red Hat Container Catalog are referenced in the sample image streams in the `openshift` namespace. The {product-title} Jenkins image has a pod template named `java-build` with sidecar containers that demonstrate this approach. This pod template uses the latest Java version provided by the `java` image stream in the `openshift` namespace.
====

The Jenkins image also provides auto-discovery and auto-configuration of additional agent images for the Kubernetes plugin.

With the {product-title} sync plugin, on Jenkins startup, the Jenkins image searches within the project it is running, or the projects listed in the plugin's configuration, for the following items:

* Image streams with the `role`  label set to `jenkins-agent`.
* Image stream tags with the `role` annotation set to `jenkins-agent`.
* Config maps with the `role` label set to `jenkins-agent`.

When the Jenkins image finds an image stream with the appropriate label, or an image stream tag with the appropriate annotation, it generates the corresponding Kubernetes plugin configuration. This way, you can assign your Jenkins jobs to run in a pod running the container image provided by the image stream.

The name and image references of the image stream, or image stream tag, are mapped to the name and image fields in the Kubernetes plugin pod template. You can control the label field of the Kubernetes plugin pod template by setting an annotation on the image stream, or image stream tag object, with the key `agent-label`. Otherwise, the name is used as the label.

[NOTE]
====
Do not log in to the Jenkins console and change the pod template configuration. If you do so after the pod template is created, and the {product-title} Sync plugin detects that the image associated with the image stream or image stream tag has changed, it replaces the pod template and overwrites those configuration changes. You cannot merge a new configuration with the existing configuration.

Consider the config map approach if you have more complex configuration needs.
====

When it finds a config map with the appropriate label, the Jenkins image assumes that any values in the key-value data payload of the config map contain Extensible Markup Language (XML) consistent with the configuration format for Jenkins and the Kubernetes plugin pod templates. One key advantage of config maps over image streams and image stream tags is that you can control all the Kubernetes plugin pod template parameters.

.Sample config map for `jenkins-agent`
[source,yaml]
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: jenkins-agent
  labels:
    role: jenkins-agent
data:
  template1: |-
    <org.csanchez.jenkins.plugins.kubernetes.PodTemplate>
      <inheritFrom></inheritFrom>
      <name>template1</name>
      <instanceCap>2147483647</instanceCap>
      <idleMinutes>0</idleMinutes>
      <label>template1</label>
      <serviceAccount>jenkins</serviceAccount>
      <nodeSelector></nodeSelector>
      <volumes/>
      <containers>
        <org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
          <name>jnlp</name>
          <image>openshift/jenkins-agent-maven-35-centos7:v3.10</image>
          <privileged>false</privileged>
          <alwaysPullImage>true</alwaysPullImage>
          <workingDir>/tmp</workingDir>
          <command></command>
          <args>${computer.jnlpmac} ${computer.name}</args>
          <ttyEnabled>false</ttyEnabled>
          <resourceRequestCpu></resourceRequestCpu>
          <resourceRequestMemory></resourceRequestMemory>
          <resourceLimitCpu></resourceLimitCpu>
          <resourceLimitMemory></resourceLimitMemory>
          <envVars/>
        </org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
      </containers>
      <envVars/>
      <annotations/>
      <imagePullSecrets/>
      <nodeProperties/>
    </org.csanchez.jenkins.plugins.kubernetes.PodTemplate>
----

The following example shows two containers that reference image streams in the `openshift` namespace. One container handles the JNLP contract for launching Pods as Jenkins Agents. The other container uses an image with tools for building code in a particular coding language:

[source,yaml]
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: jenkins-agent
  labels:
    role: jenkins-agent
data:
  template2: |-
        <org.csanchez.jenkins.plugins.kubernetes.PodTemplate>
          <inheritFrom></inheritFrom>
          <name>template2</name>
          <instanceCap>2147483647</instanceCap>
          <idleMinutes>0</idleMinutes>
          <label>template2</label>
          <serviceAccount>jenkins</serviceAccount>
          <nodeSelector></nodeSelector>
          <volumes/>
          <containers>
            <org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
              <name>jnlp</name>
              <image>image-registry.openshift-image-registry.svc:5000/openshift/jenkins-agent-base-rhel8:latest</image>
              <privileged>false</privileged>
              <alwaysPullImage>true</alwaysPullImage>
              <workingDir>/home/jenkins/agent</workingDir>
              <command></command>
              <args>\$(JENKINS_SECRET) \$(JENKINS_NAME)</args>
              <ttyEnabled>false</ttyEnabled>
              <resourceRequestCpu></resourceRequestCpu>
              <resourceRequestMemory></resourceRequestMemory>
              <resourceLimitCpu></resourceLimitCpu>
              <resourceLimitMemory></resourceLimitMemory>
              <envVars/>
            </org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
            <org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
              <name>java</name>
              <image>image-registry.openshift-image-registry.svc:5000/openshift/java:latest</image>
              <privileged>false</privileged>
              <alwaysPullImage>true</alwaysPullImage>
              <workingDir>/home/jenkins/agent</workingDir>
              <command>cat</command>
              <args></args>
              <ttyEnabled>true</ttyEnabled>
              <resourceRequestCpu></resourceRequestCpu>
              <resourceRequestMemory></resourceRequestMemory>
              <resourceLimitCpu></resourceLimitCpu>
              <resourceLimitMemory></resourceLimitMemory>
              <envVars/>
            </org.csanchez.jenkins.plugins.kubernetes.ContainerTemplate>
          </containers>
          <envVars/>
          <annotations/>
          <imagePullSecrets/>
          <nodeProperties/>
        </org.csanchez.jenkins.plugins.kubernetes.PodTemplate>
----


[NOTE]
====
Do not log in to the Jenkins console and change the pod template configuration. If you do so after the pod template is created, and the {product-title} Sync plugin detects that the image associated with the image stream or image stream tag has changed, it replaces the pod template and overwrites those configuration changes. You cannot merge a new configuration with the existing configuration.

Consider the config map approach if you have more complex configuration needs.
====

After it is installed, the {product-title} Sync plugin monitors the API server of {product-title} for updates to image streams, image stream tags, and config maps and adjusts the configuration of the Kubernetes plugin.

The following rules apply:

* Removing the label or annotation from the config map, image stream, or image stream tag deletes any existing `PodTemplate` from the configuration of the Kubernetes plugin.
* If those objects are removed, the corresponding configuration is removed from the Kubernetes plugin.
* If you create appropriately labeled or annotated `ConfigMap`, `ImageStream`, or `ImageStreamTag` objects, or add labels after their initial creation, this results in the creation of a `PodTemplate` in the Kubernetes-plugin configuration.
* In the case of the `PodTemplate` by config map form, changes to the config map data for the `PodTemplate` are applied to the `PodTemplate` settings in the Kubernetes plugin configuration. The changes also override any changes that were made to the `PodTemplate` through the Jenkins UI between changes to the config map.

To use a container image as a Jenkins agent, the image must run the agent as an entry point. For more details, see the official https://wiki.jenkins-ci.org/display/JENKINS/Distributed+builds#Distributedbuilds-Launchslaveagentheadlessly[Jenkins documentation].
