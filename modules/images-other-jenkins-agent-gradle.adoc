// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins-agent.adoc

:_mod-docs-content-type: REFERENCE
[id="images-other-jenkins-agent-gradle_{context}"]
= Jenkins agent Gradle builds

Hosting Gradle builds in the Jenkins agent on {product-title} presents additional complications because in addition to the Jenkins JNLP agent and Gradle JVMs, Gradle spawns a third JVM to run tests if they are specified.


The following settings are suggested as a starting point for running Gradle builds in a memory constrained Jenkins agent on {product-title}. You can modify these settings as required.

* Ensure the long-lived Gradle daemon is disabled by adding `org.gradle.daemon=false` to the `gradle.properties` file.
* Disable parallel build execution by ensuring `org.gradle.parallel=true` is not set in the `gradle.properties` file and that `--parallel` is not set as a command line argument.
* To prevent Java compilations running out-of-process, set `java { options.fork = false }` in the `build.gradle` file.
* Disable multiple additional test processes by ensuring `test { maxParallelForks = 1 }` is set in the `build.gradle` file.
* Override the Gradle JVM memory parameters by the `GRADLE_OPTS`, `JAVA_OPTS` or `JAVA_TOOL_OPTIONS` environment variables.
* Set the maximum heap size and JVM arguments for any Gradle test JVM by defining the `maxHeapSize` and `jvmArgs` settings in `build.gradle`, or through the `-Dorg.gradle.jvmargs` command line argument.
