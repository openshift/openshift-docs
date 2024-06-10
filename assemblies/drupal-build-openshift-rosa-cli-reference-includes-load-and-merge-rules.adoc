// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/managing-cli-profiles.adoc

:_mod-docs-content-type: CONCEPT
[id="load-and-merge-rules_{context}"]
= Load and merge rules

You can follow these rules, when issuing CLI operations for the loading and merging order for the CLI configuration:

* CLI config files are retrieved from your workstation, using the following hierarchy and merge rules:

** If the `--config` option is set, then only that file is loaded. The flag is set once and no merging takes place.
** If the `$KUBECONFIG` environment variable is set, then it is used. The variable can be a list of paths, and if so the paths are merged together. When a value is modified, it is modified in the file that defines the stanza. When a value is created, it is created in the first file that exists. If no files in the chain exist, then it creates the last file in the list.
** Otherwise, the `_~/.kube/config_` file is used and no merging takes place.

* The context to use is determined based on the first match in the following flow:

** The value of the `--context` option.
** The `current-context` value from the CLI config file.
** An empty value is allowed at this stage.

* The user and cluster to use is determined. At this point, you may or may not have a context; they are built based on the first match in the following flow, which is run once for the user and once for the cluster:
** The value of the `--user` for user name and  `--cluster` option for
cluster name.
** If the `--context` option is present, then use the context's value.
** An empty value is allowed at this stage.
* The actual cluster information to use is determined. At this point, you may or may not have cluster information. Each piece of the cluster information is built based on the first match in the following flow:
** The values of any of the following command line options:
*** `--server`,
*** `--api-version`
*** `--certificate-authority`
*** `--insecure-skip-tls-verify`
** If cluster information and a value for the attribute is present, then use it.
** If you do not have a server location, then there is an error.
* The actual user information to use is determined. Users are built using the same rules as clusters, except that you can only have one authentication technique per user; conflicting techniques cause the operation to fail. Command line options take precedence over config file values. Valid command line options are:
** `--auth-path`
** `--client-certificate`
** `--client-key`
** `--token`
* For any information that is still missing, default values are used and prompts are given for additional information.
