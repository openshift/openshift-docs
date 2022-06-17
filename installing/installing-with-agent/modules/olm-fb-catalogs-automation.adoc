// Module included in the following assemblies:
//
// * operators/understanding/olm-packaging-format.adoc

[id="olm-fb-catalogs-automation_{context}"]
= Automation

Operator authors and catalog maintainers are encouraged to automate their catalog maintenance with CI/CD workflows. Catalog maintainers can further improve on this by building GitOps automation to accomplish the following tasks:

* Check that pull request (PR) authors are permitted to make the requested changes, for example by updating their package's image reference.
* Check that the catalog updates pass the `opm validate` command.
* Check that the updated bundle or catalog image references exist, the catalog images run successfully in a cluster, and Operators from that package can be successfully installed.
* Automatically merge PRs that pass the previous checks.
* Automatically rebuild and republish the catalog image.
