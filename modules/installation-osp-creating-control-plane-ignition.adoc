// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

:_mod-docs-content-type: PROCEDURE
[id="installation-osp-creating-control-plane-ignition_{context}"]
= Creating control plane Ignition config files on {rh-openstack}

Installing {product-title} on {rh-openstack-first} on your own infrastructure requires control plane Ignition config files. You must create multiple config files.

[NOTE]
As with the bootstrap Ignition configuration, you must explicitly define a hostname for each control plane machine.

.Prerequisites

* The infrastructure ID from the installation program's metadata file is set as an environment variable (`$INFRA_ID`).
** If the variable is not set, see "Creating the Kubernetes manifest and Ignition config files".

.Procedure

* On a command line, run the following Python script:
+
[source,terminal]
----
$ for index in $(seq 0 2); do
    MASTER_HOSTNAME="$INFRA_ID-master-$index\n"
    python -c "import base64, json, sys;
ignition = json.load(sys.stdin);
storage = ignition.get('storage', {});
files = storage.get('files', []);
files.append({'path': '/etc/hostname', 'mode': 420, 'contents': {'source': 'data:text/plain;charset=utf-8;base64,' + base64.standard_b64encode(b'$MASTER_HOSTNAME').decode().strip(), 'verification': {}}, 'filesystem': 'root'});
storage['files'] = files;
ignition['storage'] = storage
json.dump(ignition, sys.stdout)" <master.ign >"$INFRA_ID-master-$index-ignition.json"
done
----
+
You now have three control plane Ignition files: `<INFRA_ID>-master-0-ignition.json`, `<INFRA_ID>-master-1-ignition.json`,
and `<INFRA_ID>-master-2-ignition.json`.