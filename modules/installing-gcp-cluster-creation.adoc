// Module included in the following assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-gcp-cluster-creation_{context}"]
= Configuring user-defined labels and tags for GCP

.Prerequisites

* The installation program requires that a service account includes a `TagUser` role, so that the program can create the {product-title} cluster with defined tags at both organization and project levels.

.Procedure

* Update the `install-config.yaml` file to define the list of desired labels and tags.
+
[NOTE]
====
Labels and tags are defined during the `install-config.yaml` creation phase, and cannot be modified or updated with new labels and tags after cluster creation.
====
+
.Sample `install-config.yaml` file
+
[source,yaml]
----
apiVersion: v1
featureSet: TechPreviewNoUpgrade
platform:
 gcp:
   userLabels: <1>
   - key: <label_key><2>
     value: <label_value><3>
   userTags: <4>
   - parentID: <OrganizationID/ProjectID><5>
     key: <tag_key_short_name>
     value: <tag_value_short_name>
----
<1> Adds keys and values as labels to the resources created on GCP.
<2> Defines the label name.
<3> Defines the label content.
<4> Adds keys and values as tags to the resources created on GCP.
<5> The ID of the hierarchical resource where the tags are defined, at the organization or the project level.

The following are the requirements for user-defined labels:

* A label key and value must have a minimum of 1 character and can have a maximum of 63 characters.
* A label key and value must contain only lowercase letters, numeric characters, underscore (`_`), and dash (`-`).
* A label key must start with a lowercase letter.
* You can configure a maximum of 32 labels per resource. Each resource can have a maximum of 64 labels, and 32 labels are reserved for internal use by {product-title}.

The following are the requirements for user-defined tags:

* Tag key and tag value must already exist. {product-title} does not create the key and the value.
* A tag `parentID` can be either `OrganizationID` or `ProjectID`:
** `OrganizationID` must consist of decimal numbers without leading zeros.
** `ProjectID` must be 6 to 30 characters in length, that includes only lowercase letters, numbers, and hyphens.
** `ProjectID` must start with a letter, and cannot end with a hyphen.
* A tag key must contain only uppercase and lowercase alphanumeric characters, hyphen (`-`), underscore (`_`), and period (`.`).
* A tag value must contain only uppercase and lowercase alphanumeric characters, hyphen (`-`), underscore (`_`), period (`.`), at sign (`@`), percent sign (`%`), equals sign (`=`), plus (`+`), colon (`:`), comma (`,`), asterisk (`*`), pound sign (`$`), ampersand (`&`), parentheses (`()`), square braces (`[]`), curly braces (`{}`), and space.
* A tag key and value must begin and end with an alphanumeric character.
* Tag value must be one of the pre-defined values for the key.
* You can configure a maximum of 50 tags.
* There should be no tag key defined with the same value as any of the existing tag keys that will be inherited from the parent resource.
