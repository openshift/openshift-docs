// Module included in the following assemblies:
// * backup_and_restore/application_backup_and_restore/troubleshooting.adoc

:_mod-docs-content-type: CONCEPT
[id="migration-combining-must-gather_{context}"]
= Combining options when using the must-gather tool

Currently, it is not possible to combine must-gather scripts, for example specifying a timeout threshold while permitting insecure TLS connections. In some situations, you can get around this limitation by setting up internal variables on the must-gather command line, such as the following example:

[source,terminal]
----
$ oc adm must-gather --image=brew.registry.redhat.io/rh-osbs/oadp-oadp-mustgather-rhel8:1.1.1-8  -- skip_tls=true /usr/bin/gather_with_timeout <timeout_value_in_seconds>
----

In this example, set the `skip_tls` variable before running the `gather_with_timeout` script. The result is a combination of `gather_with_timeout` and `gather_without_tls`.

The only other variables that you can specify this way are the following:

* `logs_since`, with a default value of `72h`
* `request_timeout`, with a default value of `0s`
