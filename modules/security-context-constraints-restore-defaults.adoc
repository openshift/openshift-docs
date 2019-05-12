// Module included in the following assemblies:
//
// * orphaned

[id="security-context-constraints-restore-defaults_{context}"]
= Restoring the default Security Context Constraints

If the default Security Context Constraints (SCCs)  are not present when the
master restarts, they are created again. To reset SCCs to the default values or
update existing SCCs to new default definitions after an upgrade you can either:

. Delete any SCC you want to reset and restart the master.
. Use the `oc adm policy reconcile-sccs` command.

The `oc adm policy reconcile-sccs` command sets all SCC policies to the default
values but retains any additional users, groups, labels, annotations, and
priorities you set.

To view which SCCs will be changed, you can run the command with no options or
by specifying your preferred output with the `-o <format>` option.

After reviewing it is recommended that you back up your existing SCCs and then
use the `--confirm` option to persist the data.

[NOTE]
====
If you want to reset priorities and grants, use the `--additive-only=false` option.
====

[NOTE]
====
If you customized settings other than priority, users, groups, labels, or annotations in an
SCC, you lose those settings when you reconcile.
====
