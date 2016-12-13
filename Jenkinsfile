#!/usr/bin/env groovy

// Pipeline variables
def isPR=false                   // true if the branch being tested belongs to a PR
def project=""                   // project where build and deploy will occur
def projectCreated=false         // true if a project was created by this build and needs to be cleaned up
def repoUrl=""                   // the URL of this project's repository
def appName="openshift-docs"     // name of application to create

// uniqueName returns a name with a 16-character random character suffix
def uniqueName = { String prefix ->
  sh "cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 16 | head -n 1 > suffix"
  suffix = readFile("suffix").trim()
  return prefix + suffix
}

// setBuildStatus sets a status item on a GitHub commit
def setBuildStatus = { String url, String context, String message, String state, String backref ->
  step([
    $class: "GitHubCommitStatusSetter",
    reposSource: [$class: "ManuallyEnteredRepositorySource", url: url ],
    contextSource: [$class: "ManuallyEnteredCommitContextSource", context: context ],
    errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
    statusBackrefSource: [ $class: "ManuallyEnteredBackrefSource", backref: backref ],
    statusResultSource: [ $class: "ConditionalStatusResultSource", results: [
        [$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

// getRepoURL retrieves the origin URL of the current source repository
def getRepoURL = {
  sh "git config --get remote.origin.url > originurl"
  return readFile("originurl").trim()
}

// getRouteHostname retrieves the host name from the given route in an
// OpenShift namespace
def getRouteHostname = { String routeName, String projectName ->
  sh "oc get route ${routeName} -n ${projectName} -o jsonpath='{ .spec.host }' > apphost"
  return readFile("apphost").trim()
}

// Initialize variables in default node context
node {
  isPR        = env.BRANCH_NAME ? env.BRANCH_NAME.startsWith("PR") : false
  baseProject = env.PROJECT_NAME
  project     = env.PROJECT_NAME
}

try { // Use a try block to perform cleanup in a finally block when the build fails

  node {
    stage ('Checkout') {
      checkout scm
      repoUrl = getRepoURL()
    }

    // When testing a PR, create a new project to perform the build 
    // and deploy artifacts.
    if (isPR) {
      stage ('Create PR Project') {
        setBuildStatus(repoUrl, "ci/app-preview", "Building application", "PENDING", "")
        setBuildStatus(repoUrl, "ci/approve", "Aprove after testing", "PENDING", "") 
        project = uniqueName("${appName}-")
        sh "oc new-project ${project}"
        projectCreated=true
        sh "oc policy add-role-to-group view system:authenticated -n ${project}"
      }
    }

    stage ('Apply object configurations') {
      sh "oc process -f _openshift/docs-template.yaml -n ${project} | oc apply -f - -n ${project}"
    }

    stage ('Build') {
      sh "oc start-build ${appName} -n ${project} --from-repo=. --follow"
    }
      

    if (isPR) {
      stage ('Verify Service') {
        openshiftVerifyService serviceName: appName, namespace: project
      }
      def appHostName = getRouteHostname(appName, project)
      setBuildStatus(repoUrl, "ci/app-preview", "The application is available", "SUCCESS", "http://${appHostName}")
      setBuildStatus(repoUrl, "ci/approve", "Approve after testing", "PENDING", "${env.BUILD_URL}input/") 
      stage ('Manual Test') {
        input "Is everything OK?"
      }
      setBuildStatus(repoUrl, "ci/app-preview", "Application previewed", "SUCCESS", "")
      setBuildStatus(repoUrl, "ci/approve", "Manually approved", "SUCCESS", "")
    }
  }
} 
finally {
  if (projectCreated) {
    node {
      stage('Delete PR Project') {
        sh "oc delete project ${project}"
      }
    }
  }
}
