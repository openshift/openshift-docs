// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins-agent.adoc

:_mod-docs-content-type: REFERENCE
[id="images-other-jenkins-agent-env-var_{context}"]
= Jenkins agent environment variables

Each Jenkins agent container can be configured with the following environment variables.

[options="header"]
|===
| Variable | Definition | Example values and settings

|`JAVA_MAX_HEAP_PARAM`,
`CONTAINER_HEAP_PERCENT`,
`JENKINS_MAX_HEAP_UPPER_BOUND_MB`
|These values control the maximum heap size of the Jenkins JVM. If `JAVA_MAX_HEAP_PARAM` is set, its value takes precedence. Otherwise, the maximum heap size is dynamically calculated as `CONTAINER_HEAP_PERCENT` of the container memory limit, optionally capped at `JENKINS_MAX_HEAP_UPPER_BOUND_MB` MiB.

By default, the maximum heap size of the Jenkins JVM is set to 50% of the container memory limit with no cap.
|`JAVA_MAX_HEAP_PARAM` example setting: `-Xmx512m`

`CONTAINER_HEAP_PERCENT` default: `0.5`, or 50%

`JENKINS_MAX_HEAP_UPPER_BOUND_MB` example setting: `512 MiB`

|`JAVA_INITIAL_HEAP_PARAM`,
`CONTAINER_INITIAL_PERCENT`
|These values control the initial heap size of the Jenkins JVM. If `JAVA_INITIAL_HEAP_PARAM` is set, its value takes precedence. Otherwise, the initial heap size is dynamically calculated as `CONTAINER_INITIAL_PERCENT` of the dynamically calculated maximum heap size.

By default, the JVM sets the initial heap size.
|`JAVA_INITIAL_HEAP_PARAM` example setting: `-Xms32m`

`CONTAINER_INITIAL_PERCENT` example setting: `0.1`, or 10%

|`CONTAINER_CORE_LIMIT`
|If set, specifies an integer number of cores used for sizing numbers of internal
JVM threads.
|Example setting: `2`

|`JAVA_TOOL_OPTIONS`
|Specifies options to apply to all JVMs running in this container. It is not recommended to override this value.
|Default: `-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -Dsun.zip.disableMemoryMapping=true`

|`JAVA_GC_OPTS`
|Specifies Jenkins JVM garbage collection parameters. It is not recommended to override this value.
|Default: `-XX:+UseParallelGC -XX:MinHeapFreeRatio=5 -XX:MaxHeapFreeRatio=10 -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90`

|`JENKINS_JAVA_OVERRIDES`
|Specifies additional options for the Jenkins JVM. These options are appended to all other options, including the Java options above, and can be used to override any of them, if necessary. Separate each additional option with a space and if any option contains space characters, escape them with a backslash.
|Example settings: `-Dfoo -Dbar`; `-Dfoo=first\ value -Dbar=second\ value`

|`USE_JAVA_VERSION`
|Specifies the version of Java version to use to run the agent in its container. The container base image has two versions of java installed: `java-11` and `java-1.8.0`. If you extend the container base image, you can specify any alternative version of java using its associated suffix.
|The default value is `java-11`.

Example setting: `java-1.8.0`

|===
