// Module included in the following assemblies:
//
// administering_a_cluster/dedicated-admin-role.adoc

[id="dedicated-managing-dedicated-readers-group_{context}"]
= Managing the dedicated-readers group

Users with a `dedicated-reader` role are granted edit and view access to the
`dedicated-reader` project and view-only access to the other projects.

To view a list of current dedicated readers by user name, you can use the
following command:

----
$ oc describe group dedicated-readers
----

To add a new member to the `dedicated-readers` group, if you have
`dedicated-admin` access:

----
$ oc adm groups add-users dedicated-readers <user_name>
----

To remove an existing user from the `dedicated-readers` group, if you have
`dedicated-admin` access:

----
$ oc adm groups remove-users dedicated-readers <user_name>
----
