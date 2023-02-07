// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

[id="templates-writing_{context}"]
= Writing templates

You can define new templates to make it easy to recreate all the objects of your application. The template defines the objects it creates along with some metadata to guide the creation of those objects.

The following is an example of a simple template object definition (YAML):

[source,yaml]
----
apiVersion: template.openshift.io/v1
kind: Template
metadata:
  name: redis-template
  annotations:
    description: "Description"
    iconClass: "icon-redis"
    tags: "database,nosql"
objects:
- apiVersion: v1
  kind: Pod
  metadata:
    name: redis-master
  spec:
    containers:
    - env:
      - name: REDIS_PASSWORD
        value: ${REDIS_PASSWORD}
      image: dockerfile/redis
      name: master
      ports:
      - containerPort: 6379
        protocol: TCP
parameters:
- description: Password used for Redis authentication
  from: '[A-Z0-9]{8}'
  generate: expression
  name: REDIS_PASSWORD
labels:
  redis: master
----
