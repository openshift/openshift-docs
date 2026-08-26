:_mod-docs-content-type: REFERENCE
[id="odo-json-output_{context}"]
= JSON output

The `odo` commands that output content generally accept a `-o json` flag to output this content in JSON format, suitable for other programs to parse this output more easily.

The output structure is similar to Kubernetes resources, with the `kind`, `apiVersion`, `metadata`, `spec`, and `status` fields.

_List_ commands return a `List` resource, containing an `items` (or similar) field listing the items of the list, with each item also being similar to Kubernetes resources.

_Delete_ commands return a `Status` resource; see the link:https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/[Status Kubernetes resource].

Other commands return a resource associated with the command, for example, `Application`, `Storage`, `URL`, and so on.

The full list of commands currently accepting the `-o json` flag is:

|===
| Commands | Kind (version) | Kind (version) of list items | Complete content?

| odo application describe
| Application (odo.dev/v1alpha1)
| _n/a_
| no

| odo application list
| List (odo.dev/v1alpha1)
| Application (odo.dev/v1alpha1)
| ?

| odo catalog list components
| List (odo.dev/v1alpha1)
| _missing_
| yes

| odo catalog list services
| List (odo.dev/v1alpha1)
| ClusterServiceVersion (operators.coreos.com/v1alpha1)
| ?

| odo catalog describe component
| _missing_
| _n/a_
| yes

| odo catalog describe service
| CRDDescription (odo.dev/v1alpha1)
| _n/a_
| yes

| odo component create
| Component (odo.dev/v1alpha1)
| _n/a_
| yes

| odo component describe
| Component (odo.dev/v1alpha1)
| _n/a_
| yes

| odo component list
| List (odo.dev/v1alpha1)
| Component (odo.dev/v1alpha1)
| yes

| odo config view
| DevfileConfiguration (odo.dev/v1alpha1)
| _n/a_
| yes

| odo debug info
| OdoDebugInfo (odo.dev/v1alpha1)
| _n/a_
| yes

| odo env view
| EnvInfo (odo.dev/v1alpha1)
| _n/a_
| yes

| odo preference view
| PreferenceList (odo.dev/v1alpha1)
| _n/a_
| yes

| odo project create
| Project (odo.dev/v1alpha1)
| _n/a_
| yes

| odo project delete
| Status (v1)
| _n/a_
| yes

| odo project get
| Project (odo.dev/v1alpha1)
| _n/a_
| yes

| odo project list
| List (odo.dev/v1alpha1)
| Project (odo.dev/v1alpha1)
| yes

| odo registry list
| List (odo.dev/v1alpha1)
| _missing_
| yes

| odo service create
| Service
| _n/a_
| yes

| odo service describe
| Service
| _n/a_
| yes

| odo service list
| List (odo.dev/v1alpha1)
| Service
| yes

| odo storage create
| Storage (odo.dev/v1alpha1)
| _n/a_
| yes

| odo storage delete
| Status (v1)
| _n/a_
| yes

| odo storage list
| List (odo.dev/v1alpha1)
| Storage (odo.dev/v1alpha1)
| yes

| odo url list
| List (odo.dev/v1alpha1)
| URL (odo.dev/v1alpha1)
| yes
|===
