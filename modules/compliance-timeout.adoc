// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-troubleshooting.adoc

:_mod-docs-content-type: PROCEDURE
[id="compliance-timeout_{context}"]
= Configuring ScanSetting timeout

The `ScanSetting` object has a timeout option that can be specified in the `ComplianceScanSetting` object as a duration string, such as `1h30m`. If the scan does not finish within the specified timeout, the scan reattempts until the `maxRetryOnTimeout` limit is reached.

.Procedure

* To set a `timeout` and `maxRetryOnTimeout` in ScanSetting, modify an existing `ScanSetting` object:
+
[source,yaml]
----
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSetting
metadata:
  name: default
  namespace: openshift-compliance
rawResultStorage:
  rotation: 3
  size: 1Gi
roles:
- worker
- master
scanTolerations:
- effect: NoSchedule
  key: node-role.kubernetes.io/master
  operator: Exists
schedule: '0 1 * * *'
timeout: '10m0s' <1>
maxRetryOnTimeout: 3 <2>
----
<1> The `timeout` variable is defined as a duration string, such as `1h30m`. The default value is `30m`. To disable the timeout, set the value to `0s`.
<2> The `maxRetryOnTimeout` variable defines how many times a retry is attempted. The default value is `3`.