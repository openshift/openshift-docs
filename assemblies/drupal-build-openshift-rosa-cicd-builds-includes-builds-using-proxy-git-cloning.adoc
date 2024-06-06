// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-using-proxy-git-cloning_{context}"]
= Using a proxy

If your Git repository can only be accessed using a proxy, you can define the proxy to use in the `source` section of the build configuration. You can configure both an HTTP and HTTPS proxy to use. Both fields are optional. Domains for which no proxying should be performed can also be specified in the `NoProxy` field.

[NOTE]
====
Your source URI must use the HTTP or HTTPS protocol for this to work.
====

[source,yaml]
----
source:
  git:
    uri: "https://github.com/openshift/ruby-hello-world"
    ref: "master"
    httpProxy: http://proxy.example.com
    httpsProxy: https://proxy.example.com
    noProxy: somedomain.com, otherdomain.com
----

[NOTE]
====
For Pipeline strategy builds, given the current restrictions with the Git plugin for Jenkins, any Git operations through the Git plugin do not leverage the HTTP or HTTPS proxy defined in the `BuildConfig`. The Git plugin only uses the proxy configured in the Jenkins UI at the Plugin Manager panel. This proxy is then used for all git interactions within Jenkins, across all jobs.
====

[role="_additional-resources"]
.Additional resources

* You can find instructions on how to configure proxies through the Jenkins UI at link:https://wiki.jenkins-ci.org/display/JENKINS/JenkinsBehindProxy[JenkinsBehindProxy].
