// Module included in the following assemblies:
//
//* authentication/configmaps.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-configmap-creating-from-files_{context}"]
= Creating a config map from a file

You can create a config map from a file by using the `--from-file` flag. You can pass the `--from-file` option multiple times to the CLI.

You can also specify the key to set in a config map for content imported from a file by passing a `key=value` expression to the `--from-file` option. For example:

[source,terminal]
----
$ oc create configmap game-config-3 --from-file=game-special-key=example-files/game.properties
----

[NOTE]
====
If you create a config map from a file, you can include files containing non-UTF8 data that are placed in this field without corrupting the non-UTF8 data. {product-title} detects binary files and transparently encodes the file as `MIME`. On the server, the `MIME` payload is decoded and stored without corrupting the data.
====

.Prerequisite

* You must have a directory with files that contain the data you want to populate a config map with.
+
The following procedure uses these example files: `game.properties` and `ui.properties`:
+
[source,terminal]
----
$ cat example-files/game.properties
----
+
.Example output
[source,terminal]
----
enemies=aliens
lives=3
enemies.cheat=true
enemies.cheat.level=noGoodRotten
secret.code.passphrase=UUDDLRLRBABAS
secret.code.allowed=true
secret.code.lives=30
----
+
[source,terminal]
----
$ cat example-files/ui.properties
----
+
.Example output
[source,terminal]
----
color.good=purple
color.bad=yellow
allow.textmode=true
how.nice.to.look=fairlyNice
----

.Procedure

* Create a config map by specifying a specific file:
+
[source,terminal]
----
$ oc create configmap game-config-2 \
    --from-file=example-files/game.properties \
    --from-file=example-files/ui.properties
----

* Create a config map by specifying a key-value pair:
+
[source,terminal]
----
$ oc create configmap game-config-3 \
    --from-file=game-special-key=example-files/game.properties
----

.Verification

* Enter the `oc get` command for the object with the `-o` option to see the values of the keys from the file:
+
[source,terminal]
----
$ oc get configmaps game-config-2 -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
data:
  game.properties: |-
    enemies=aliens
    lives=3
    enemies.cheat=true
    enemies.cheat.level=noGoodRotten
    secret.code.passphrase=UUDDLRLRBABAS
    secret.code.allowed=true
    secret.code.lives=30
  ui.properties: |
    color.good=purple
    color.bad=yellow
    allow.textmode=true
    how.nice.to.look=fairlyNice
kind: ConfigMap
metadata:
  creationTimestamp: 2016-02-18T18:52:05Z
  name: game-config-2
  namespace: default
  resourceVersion: "516"
  selflink: /api/v1/namespaces/default/configmaps/game-config-2
  uid: b4952dc3-d670-11e5-8cd0-68f728db1985
----

* Enter the `oc get` command for the object with the `-o` option to see the values of the keys from the key-value pair:
+
[source,terminal]
----
$ oc get configmaps game-config-3 -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
data:
  game-special-key: |- <1>
    enemies=aliens
    lives=3
    enemies.cheat=true
    enemies.cheat.level=noGoodRotten
    secret.code.passphrase=UUDDLRLRBABAS
    secret.code.allowed=true
    secret.code.lives=30
kind: ConfigMap
metadata:
  creationTimestamp: 2016-02-18T18:54:22Z
  name: game-config-3
  namespace: default
  resourceVersion: "530"
  selflink: /api/v1/namespaces/default/configmaps/game-config-3
  uid: 05f8da22-d671-11e5-8cd0-68f728db1985
----
<1> This is the key that you set in the preceding step.
