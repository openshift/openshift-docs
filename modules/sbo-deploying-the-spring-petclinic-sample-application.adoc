// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/getting-started-with-service-binding.adoc

:_mod-docs-content-type: PROCEDURE
[id="sbo-deploying-the-spring-petclinic-sample-application_{context}"]
= Deploying the Spring PetClinic sample application

To deploy the Spring PetClinic sample application on an {product-title} cluster, you must use a deployment configuration and configure your local environment to be able to test the application.

[discrete]
.Procedure

. Deploy the `spring-petclinic` application with the `PostgresCluster` custom resource (CR) by running the following command in shell:
+
[source,terminal]
----
$ oc apply -n my-petclinic -f - << EOD
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spring-petclinic
  labels:
    app: spring-petclinic
spec:
  replicas: 1
  selector:
    matchLabels:
      app: spring-petclinic
  template:
    metadata:
      labels:
        app: spring-petclinic
    spec:
      containers:
        - name: app
          image: quay.io/service-binding/spring-petclinic:latest
          imagePullPolicy: Always
          env:
          - name: SPRING_PROFILES_ACTIVE
            value: postgres
          ports:
          - name: http
            containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: spring-petclinic
  name: spring-petclinic
spec:
  type: NodePort
  ports:
    - port: 80
      protocol: TCP
      targetPort: 8080
  selector:
    app: spring-petclinic
EOD
----
+
The output verifies that the Spring PetClinic sample application is created and deployed:
+
.Example output
[source,terminal]
----
deployment.apps/spring-petclinic created
service/spring-petclinic created
----
+
[NOTE]
====
If you are deploying the application using *Container images* in the *Developer* perspective of the web console, you must enter the following environment variables under the *Deployment* section of the *Advanced options*:


* Name: SPRING_PROFILES_ACTIVE
* Value: postgres
====

. Verify that the application is not yet connected to the database service by running the following command:
+
[source,terminal]
----
$ oc get pods -n my-petclinic
----
+
The output takes a few minutes to display the `CrashLoopBackOff` status:
+
.Example output
[source,terminal]
----
NAME                                READY   STATUS             RESTARTS      AGE
spring-petclinic-5b4c7999d4-wzdtz   0/1     CrashLoopBackOff   4 (13s ago)   2m25s
----
+
At this stage, the pod fails to start. If you try to interact with the application, it returns errors.
+
. Expose the service to create a route for your application:
+
[source,terminal]
----
$ oc expose service spring-petclinic -n my-petclinic
----
+
The output verifies that the `spring-petclinic` service is exposed and a route for the Spring PetClinic sample application is created:
+
.Example output
[source,terminal]
----
route.route.openshift.io/spring-petclinic exposed
----

You can now use the {servicebinding-title} to connect the application to the database service.