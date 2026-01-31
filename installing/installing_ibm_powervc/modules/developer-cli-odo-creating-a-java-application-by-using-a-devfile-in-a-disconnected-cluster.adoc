// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/

:_mod-docs-content-type: PROCEDURE
[id="developer-cli-odo-creating-a-java-application-by-using-a-devfile-in-a-disconnected-cluster_{context}"]

= Creating a Java application by using a devfile in a disconnected cluster

[WARNING]
====
This procedure is using external dependencies such as `quay.io/eclipse/che-java11-maven:nightly` or an example application `springboot-ex` that are not maintained by Red Hat. These dependencies are not maintained with the documentation and their functionality cannot be guaranteed.
====

.Prerequisites
* You have created and logged into a disconnected cluster.
* You have added `quay.io`, `registry.access.redhat.com`, `apache.org`, `quayio-production-s3.s3.amazonaws.com` URLs in your proxy configuration.

.Procedure

. Define your Java application in a devfile:
+
.Example of a devfile
[source,yaml]
----
schemaVersion: 2.0.0
metadata:
  name: java-maven
  version: 1.1.0
starterProjects:
  - name: springbootproject
    git:
      remotes:
        origin: "https://github.com/odo-devfiles/springboot-ex.git"
components:
  - name: tools
    container:
      image: quay.io/eclipse/che-java11-maven:nightly
      memoryLimit: 512Mi
      mountSources: true
      endpoints:
        - name: 'http-8080'
          targetPort: 8080
      volumeMounts:
        - name: m2
          path: /home/user/.m2
  - name: m2
    volume: {}
commands:
  - id: mvn-package
    exec:
      component: tools
      commandLine: "mvn -Dmaven.repo.local=/home/user/.m2/repository -Dhttp.proxyHost=<proxy-host> -Dhttp.proxyPort=<proxy-port> -Dhttps.proxyHost=<proxy-host> -Dhttps.proxyPort=<proxy-port> package"
      group:
        kind: build
        isDefault: true
  - id: run
    exec:
      component: tools
      commandLine: "java -jar target/*.jar"
      group:
        kind: run
        isDefault: true
  - id: debug
    exec:
      component: tools
      commandLine: "java -Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=${DEBUG_PORT},suspend=n -jar target/*.jar"
      group:
        kind: debug
        isDefault: true
----

. Create a Java application:
+
[source,terminal]
----
$ odo create java-maven --devfile <path-to-your-devfile> --starter
----
+
.Example output
[source,terminal]
----
Validation
 ✓  Checking devfile existence [87716ns]
 ✓  Creating a devfile component from registry: DefaultDevfileRegistry [107247ns]
 ✓  Validating devfile component [396971ns]

 Starter Project
 ✓  Downloading starter project springbootproject from https://github.com/odo-devfiles/springboot-ex.git [2s]

Please use `odo push` command to create the component with source deployed
----

. Push the changes to the cluster:
+
[source,terminal]
----
$ odo push
----
+
.Example output
[source,terminal]
----
I0224 14:43:18.802512   34741 util.go:727] HTTPGetRequest: https://raw.githubusercontent.com/openshift/odo/master/build/VERSION
I0224 14:43:18.833631   34741 context.go:115] absolute devfile path: '/Users/pkumari/go/src/github.com/openshift/odo/testim/devfile.yaml'
[...]
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.2.1/plexus-utils-3.2.1.jar (262 kB at 813 kB/s)
[INFO] Replacing main artifact with repackaged archive
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  19.638 s
[INFO] Finished at: 2021-02-24T08:59:30Z
[INFO] ------------------------------------------------------------------------
 ✓  Executing mvn-package command "mvn -Dmaven.repo.local=/home/user/.m2/repository -Dhttp.proxyHost=<proxy-host> -Dhttp.proxyPort=<proxy-port> -Dhttps.proxyHost=<proxy-host> -Dhttps.proxyPort=<proxy-port> package" [23s]
 •  Executing run command "java -jar target/*.jar"  ...
I0224 14:29:30.557676   34426 exec.go:27] Executing command [/opt/odo/bin/supervisord ctl start devrun] for pod: java-maven-5b8f99fcdb-9dnk6 in container: tools
devrun: started
 ✓  Executing run command "java -jar target/*.jar" [3s]

Pushing devfile component java-maven
 ✓  Changes successfully pushed to component
----

. Display the logs to verify that the application has started:
+
[source,terminal]
----
$ odo log
----
+
.Example output
[source,terminal]
----
time="2021-02-24T08:58:58Z" level=info msg="create process:devrun"
time="2021-02-24T08:58:58Z" level=info msg="create process:debugrun"
time="2021-02-24T08:59:32Z" level=debug msg="no auth required"
time="2021-02-24T08:59:32Z" level=debug msg="succeed to find process:devrun"
time="2021-02-24T08:59:32Z" level=info msg="try to start program" program=devrun
time="2021-02-24T08:59:32Z" level=info msg="success to start program" program=devrun
ODO_COMMAND_RUN is java -jar target/*.jar
Executing command  java -jar target/*.jar
[...]
----

. Create storage for your application:
+
[source,terminal]
----
$ odo storage create storage-name --path /data --size 5Gi
----
+
.Example output
[source,terminal]
----
✓  Added storage storage-name to java-maven

Please use `odo push` command to make the storage accessible to the component
----

. Push the changes to the cluster:
+
[source,terminal]
----
$ odo push
----
+
.Output
[source,terminal]
----
✓  Waiting for component to start [310ms]

Validation
 ✓  Validating the devfile [100798ns]

Creating Kubernetes resources for component java-maven
 ✓  Waiting for component to start [30s]
 ✓  Waiting for component to start [303ms]

Applying URL changes
 ✓  URLs are synced with the cluster, no changes are required.

Syncing to component java-maven
 ✓  Checking file changes for pushing [5ms]
 ✓  Syncing files to the component [4s]

Executing devfile commands for component java-maven
 ✓  Waiting for component to start [526ms]
 ✓  Executing mvn-package command "mvn -Dmaven.repo.local=/home/user/.m2/repository -Dhttp.proxyHost=<proxy-host> -Dhttp.proxyPort=<proxy-port> -Dhttps.proxyHost=<proxy-host> -Dhttps.proxyPort=<proxy-port> package" [10s]
 ✓  Executing run command "java -jar target/*.jar" [3s]

Pushing devfile component java-maven
 ✓  Changes successfully pushed to component
----
