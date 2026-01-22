// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-cr_{context}"]
= Generating 3scale custom resources

The adapter includes a tool that allows you to generate the `handler`, `instance`, and `rule` custom resources.

.Usage
|===
|Option |Description |Required | Default value

|`-h, --help`
|Produces help output for available options
|No
|

|`--name`
|Unique name for this URL, token pair
|Yes
|

|`-n, --namespace`
|Namespace to generate templates
|No
|istio-system

|`-t, --token`
|3scale access token
|Yes
|

|`-u, --url`
|3scale Admin Portal URL
|Yes
|

|`--backend-url`
|3scale backend URL. If set, it overrides the value that is read from system configuration
|No
|

|`-s, --service`
|3scale API/Service ID
|No
|

|`--auth`
|3scale authentication pattern to specify (1=API Key, 2=App Id/App Key, 3=OIDC)
|No
|Hybrid

|`-o, --output`
|File to save produced manifests to
|No
|Standard output

|`--version`
|Outputs the CLI version and exits immediately
|No
|
|===
