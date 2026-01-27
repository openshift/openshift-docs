import os
import subprocess

# ---------------------------------------
# Step 1: Prompt user for ACS directory
# ---------------------------------------
acs_path = input("Enter the full path to the ACS directory: ").strip()

if not os.path.isdir(acs_path):
    print(f"❌ The path '{acs_path}' is not a valid directory.")
    exit(1)

# ---------------------------------------
# Step 2: List of required .adoc file paths
# ---------------------------------------
target_files = [
    "installing/installing_other/init-bundle-other.adoc",
    "installing/installing_ocp/install-central-config-options-ocp.adoc",
    "installing/installing_other/verify-installation-rhacs-other.adoc",
    "installing/installing_helm/install-helm-quick.adoc",
    "installing/installing_ocp/install-secured-cluster-ocp.adoc",
    "installing/installing_ocp/verify-installation-rhacs-ocp.adoc",
    "installing/acs-recommended-requirements.adoc",
    "installing/installing_helm/install-helm-customization.adoc",
    "installing/installing_ocp/init-bundle-ocp.adoc",
    "architecture/acs-architecture.adoc",
    "installing/installing_ocp/install-secured-cluster-config-options-ocp.adoc",
    "installing/installing_other/install-rhacs-other.adoc",
    "installing/installing_other/install-secured-cluster-other.adoc",
    "installing/installing_ocp/install-central-ocp.adoc",
    "installing/acs-high-level-overview.adoc",
    "installing/installing_other/install-central-other.adoc",
    "installing/acs-default-requirements.adoc",
    "installing/uninstall-acs.adoc",
    "upgrading/upgrade-operator.adoc",
    "upgrading/upgrade-helm.adoc",
    "backup_and_restore/restore-acs.adoc",
    "backup_and_restore/backing-up-acs.adoc",
    "release_notes/49-release-notes.adoc",
    "support/getting-support.adoc",
    "upgrading/upgrade-roxctl.adoc",
    "welcome/index.adoc",
    "cli/managing-secured-clusters.adoc",
    "cli/checking-policy-compliance.adoc",
    "cli/command-reference/roxctl-deployment.adoc",
    "cli/installing-the-roxctl-cli.adoc",
    "cli/command-reference/roxctl-declarative-config.adoc",
    "cli/command-reference/roxctl-completion.adoc",
    "cli/command-reference/roxctl-helm.adoc",
    "cli/command-reference/roxctl-cluster.adoc",
    "cli/command-reference/roxctl-netpol.adoc",
    "cli/command-reference/roxctl-image.adoc",
    "cli/command-reference/roxctl-sensor.adoc",
    "cli/command-reference/roxctl-central.adoc",
    "cli/command-reference/roxctl-version.adoc",
    "cli/debugging-issues.adoc",
    "cloud_service/installing_cloud_ocp/configuring-the-proxy-for-secured-cluster-services-in-rhacs-cloud-service.adoc",
    "cloud_service/installing_cloud_ocp/verify-installation-cloud-ocp.adoc",
    "cloud_service/installing_cloud_ocp/cloud-create-instance-ocp.adoc",
    "cli/image-scanning-by-using-the-roxctl-cli.adoc",
    "cli/command-reference/roxctl-scanner.adoc",
    "cli/command-reference/roxctl.adoc",
    "cloud_service/installing_cloud_ocp/cloud-install-operator.adoc",
    "cli/using-the-roxctl-cli.adoc",
    "cli/command-reference/roxctl-collector.adoc",
    "cloud_service/installing_cloud_ocp/init-bundle-cloud-ocp-apply.adoc",
    "cloud_service/installing_cloud_other/install-secured-cluster-cloud-other.adoc",
    "cloud_service/installing_cloud_other/verify-installation-cloud-other.adoc",
    "cloud_service/installing_cloud_ocp/cloud-ocp-create-project.adoc",
    "cloud_service/installing_cloud_other/init-bundle-cloud-other-apply.adoc",
    "cloud_service/acscs-recommended-requirements.adoc",
    "cloud_service/acs-cloud-responsibility-matrix.adoc",
    "cloud_service/acscs-default-requirements.adoc",
    "cloud_service/installing_cloud_other/cloud-create-instance-other.adoc",
    "cloud_service/upgrading-cloud/upgrade-cloudsvc-helm.adoc",
    "cloud_service/installing_cloud_ocp/init-bundle-cloud-ocp-generate.adoc",
    "cloud_service/installing_cloud_ocp/install-secured-cluster-cloud-ocp.adoc",
    "cloud_service/upgrading-cloud/upgrade-cloudsvc-roxctl.adoc",
    "cloud_service/upgrading-cloud/upgrade-cloudsvc-operator.adoc",
    "cloud_service/installing_cloud_other/init-bundle-cloud-other-generate.adoc",
    "cloud_service/rhacs-cloud-service-service-description.adoc",
    "cloud_service/getting-started-rhacs-cloud-ocp.adoc",
    "cloud_service/acscs-architecture.adoc",
    "configuration/configuring-and-integrating-the-rhacs-plugin-with-red-hat-developer-hub.adoc",
    "configuration/add-trusted-ca.adoc",
    "configuration/configure-inactive-cluster-deletion.adoc",
    "configuration/add-custom-certificates.adoc",
    "configuration/managing-preview-features.adoc",
    "configuration/declarative-configuration-using.adoc",
    "configuration/configure-api-token.adoc",
    "configuration/inviting-users-to-your-rhacs-instance.adoc",
    "configuration/configure-endpoints.adoc",
    "configuration/reissue-internal-certificates.adoc",
    "configuration/enable-offline-mode.adoc",
    "configuration/customizing-platform-components.adoc",
    "configuration/using-rhacs-with-gitops.adoc",
    "configuration/add-security-notices.adoc",
    "configuration/internal-certificate-authority-rotation-for-rhacs.adoc",
    "configuration/generate-diagnostic-bundle.adoc",
    "configuration/monitor-acs.adoc",
    "configuration/enable-alert-data-retention.adoc",
    "configuration/expose-portal-over-http.adoc",
    "integration/integrate-with-google-cloud-storage.adoc",
    "integration/integrate-with-jira.adoc",
    "configuration/configure-automatic-upgrades.adoc",
    "configuration/configure-audit-logging.adoc",
    "integration/integrate-with-email.adoc",
    "integration/integrate-with-amazon-s3.adoc",
    "integration/integrate-with-splunk.adoc",
    "integration/integrate-with-qradar.adoc",
    "configuration/configure-proxy.adoc",
    "integration/integrate-with-cloud-management-platforms.adoc",
    "integration/integrate-using-short-lived-tokens.adoc",
    "integration/integrate-with-s3-api-compatible-services.adoc",
    "integration/integrating-with-microsoft-sentinel-notifier.adoc",
    "integration/integrate-using-generic-webhooks.adoc",
    "integration/integrate-with-google-cloud-scc.adoc",
    "integration/integrate-with-image-vulnerability-scanners.adoc",
    "integration/integrate-with-pagerduty.adoc",
    "integration/integrate-with-ci-systems.adoc",
    "integration/integrate-with-image-registries.adoc",
    "operating/manage-network-policies.adoc",
    "integration/integrate-with-sumologic.adoc",
    "integration/integrate-using-syslog-protocol.adoc",
    "integration/integrate-with-servicenow.adoc",
    "integration/integrate-with-slack.adoc",
    "operating/manage-user-access/configuring-identity-providers/configure-ocp-oauth.adoc",
    "operating/manage-user-access/manage-role-based-access-control-3630.adoc",
    "operating/manage-user-access/configuring-identity-providers/configure-google-workspace-identity.adoc",
    "operating/manage-user-access/configuring-identity-providers/connecting-azure-ad-to-rhacs-using-sso-configuration.adoc",
    "operating/manage-user-access/configuring-identity-providers/configure-okta-identity-cloud.adoc",
    "operating/manage-user-access/remove-admin-user.adoc",
    "operating/manage-user-access/configure-short-lived-access.adoc",
    "operating/manage-user-access/understanding-multi-tenancy.adoc",
    "operating/manage-vulnerabilities/vulnerability-management-dashboard.adoc",
    "operating/manage-user-access/enable-pki-authentication.adoc",
    "operating/manage-vulnerabilities/scan-rhcos-node-host.adoc",
    "operating/manage-user-access/understanding-authentication-providers.adoc",
    "operating/manage-vulnerabilities/vulnerability-management.adoc",
    "operating/manage-vulnerabilities/common-vuln-management-tasks.adoc",
    "operating/manage-compliance/using-openshift-compliance.adoc",
    "operating/manage-compliance/compliance-feature-overview.adoc",
    "operating/create-use-collections.adoc",
    "operating/manage-compliance/using-the-compliance-dashboard.adoc",
    "operating/manage_security_policies/about-security-policies.adoc",
    "operating/using-the-administration-events-page.adoc",
    "operating/manage_security_policies/security-policy-reference.adoc",
    "operating/manage_security_policies/managing-policies-as-code.adoc",
    "operating/use-system-health-dashboard.adoc",
    "operating/manage_security_policies/use-admission-controller-enforcement.adoc",
    "operating/manage_security_policies/custom-security-policies.adoc",
    "operating/manage-vulnerabilities/scanner-generate-sbom.adoc",
    "operating/manage-vulnerabilities/vulnerability-reporting.adoc",
    "operating/build-time-network-policy-tools.adoc",
    "operating/compliance-operator-rhacs.adoc",
    "operating/examine-images-for-vulnerabilities.adoc",
    "operating/respond-to-violations.adoc",
    "operating/audit-listening-endpoints.adoc",
    "operating/review-cluster-configuration.adoc",
    "operating/evaluate-security-risks.adoc",
    "telemetry/opting-out-of-telemetry.adoc",
    "operating/visualizing-external-entities.adoc",
    "troubleshooting/commonly-occurring-error-conditions.adoc",
    "operating/verify-image-signatures.adoc",
    "troubleshooting/retrieving-and-analyzing-the-collector-logs-and-pod-status.adoc",
    "troubleshooting_central/backing-up-central-database-by-using-the-roxctl-cli.adoc",
    "operating/search-filter.adoc",
    "operating/using-collector-runtime-configuration.adoc",
    "telemetry/about-telemetry.adoc",
    "troubleshooting_central/restoring-central-database-by-using-the-roxctl-cli.adoc",
    "operating/view-dashboard.adoc",
    "modules/install-helm-customization-overview.adoc",
    "modules/rhcos-enable-node-scan-scannerv4.adoc",
    "modules/central-services-public-config.adoc",
    "modules/custom-cert-prerequisites.adoc",
    "modules/distinguishing-between-syntactic-and-semantic-difference-outputs.adoc",
    "modules/retrieving-the-logs-with-the-oc-or-kubectl-command.adoc",
    "modules/search-syntax.adoc",
    "modules/semantic-difference-output.adoc",
    "modules/syntactic-difference-output.adoc",
    "modules/verify-central-cluster-upgrade.adoc",
    "modules/using-an-authentication-provider-to-authenticate-with-roxctl.adoc",
    "modules/analyzing-the-collector-pod-status.adoc",
    "modules/roxctl-central-db-restore.adoc",
    "modules/roxctl-central-db-restore-status.adoc",
    "modules/roxctl-central-debug.adoc",
    "modules/roxctl-central-debug-db-stats.adoc",
    "modules/roxctl-central-debug-db-stats-reset.adoc",
    "modules/roxctl-central-generate-interactive.adoc",
    "modules/roxctl-central-init-bundles-list.adoc",
    "modules/roxctl-central-init-bundles-revoke.adoc",
    "modules/roxctl-central-userpki.adoc",
    "modules/roxctl-declarative-config-create-auth-provider-openshift-auth.adoc",
    "modules/roxctl-helm-output.adoc",
    "modules/roxctl-generate-netpol.adoc",
    "modules/roxctl-netpol-connectivity.adoc",
    "modules/roxctl-helm-derive-local-values.adoc",
    "modules/roxctl-sensor-generate-certs.adoc",
    "modules/roxctl-sensor-get-bundle.adoc",
    "modules/operator-upgrade-fail-to-deploy.adoc",
    "modules/migrating-sccs-during-the-manual-upgrade.adoc",
    "modules/azure-workload-identity-federation-aks.adoc",
    "modules/backup-considerations-for-external-databases-and-cloud-users.adoc",
    "modules/configure-minimum-access-role.adoc",
    "modules/crs-generate-roxctl.adoc",
    "modules/enabling-scanner-v4-helm-central.adoc",
    "modules/roxctl-central-crs-revoke.adoc",
    "modules/roxctl-central-crs-list.adoc",
    "modules/roxctl-central-crs.adoc",
    "modules/roxctl-central-init-bundles-generate.adoc"
]

# ---------------------------------------
# Step 3: Create output folder
# ---------------------------------------
output_dir = os.path.join(os.getcwd(), "Files")
os.makedirs(output_dir, exist_ok=True)

# ---------------------------------------
# Step 4: Process files using vale + nl
# ---------------------------------------
found_count = 0
missing_files = []

for relative_path in target_files:
    source_file = os.path.join(acs_path, relative_path)

    if os.path.isfile(source_file):
        found_count += 1
        print(f"🔍 Processing: {relative_path}")

        # Create corresponding output dirs
        output_subpath = os.path.join(output_dir, relative_path)
        output_directory = os.path.dirname(output_subpath)
        os.makedirs(output_directory, exist_ok=True)

        # Output file paths
        vale_out = f"{output_subpath}.vale.txt"
        numbered_out = f"{output_subpath}.numbered.txt"

        # ---------------------------------------
        # Run vale (fixed version)
        # ---------------------------------------
        try:
            with open(vale_out, "w") as vf:
                subprocess.run([
                    "vale",
                    "--ext=.adoc",
                    "--no-exit",
                    source_file
                ], stdout=vf, stderr=subprocess.STDOUT)
            print(f"   ✔ vale output saved")
        except Exception as e:
            print(f"   ❌ Error running vale: {e}")

        # ---------------------------------------
        # Run nl -ba
        # ---------------------------------------
        try:
            with open(numbered_out, "w") as nf:
                subprocess.run(["nl", "-ba", source_file],
                               stdout=nf, stderr=subprocess.STDOUT)
            print(f"   ✔ numbered output saved")
        except Exception as e:
            print(f"   ❌ Error running nl: {e}")

    else:
        missing_files.append(relative_path)

# ---------------------------------------
# Step 5: Summary
# ---------------------------------------
print("\n----------------------")
print(f"✅ Total processed: {found_count}")
if missing_files:
    print(f"⚠️ Missing {len(missing_files)} files:")
    for mf in missing_files:
        print(f"   - {mf}")
print("----------------------")
print(f"📂 All TXT output files saved under: {output_dir}")
