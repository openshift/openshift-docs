// Module included in the following assemblies:
//
// * networking/ingress_operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-configuring-router-compression_{context}"]
= Using router compression

You configure the HAProxy Ingress Controller to specify router compression globally for specific MIME types. You can use the `mimeTypes` variable to define the formats of MIME types to which compression is applied. The types are: application, image, message, multipart, text, video, or a custom type prefaced by "X-". To see the full notation for MIME types and subtypes, see link:https://datatracker.ietf.org/doc/html/rfc1341#page-7[RFC1341].

[NOTE]
====
Memory allocated for compression can affect the max connections. Additionally, compression of large buffers can cause latency, like heavy regex or long lists of regex.

Not all MIME types benefit from compression, but HAProxy still uses resources to try to compress if instructed to.  Generally, text formats, such as html, css, and js, formats benefit from compression, but formats that are already compressed, such as image, audio, and video, benefit little in exchange for the time and resources spent on compression.
====

.Procedure

. Configure the `httpCompression` field for the Ingress Controller.
.. Use the following command to edit the `IngressController` resource:
+
[source,terminal]
----
$ oc edit -n openshift-ingress-operator ingresscontrollers/default
----
+
.. Under `spec`, set the `httpCompression` policy field to `mimeTypes` and specify a list of MIME types that should have compression applied:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpCompression:
    mimeTypes:
    - "text/html"
    - "text/css; charset=utf-8"
    - "application/json"
   ...
----
