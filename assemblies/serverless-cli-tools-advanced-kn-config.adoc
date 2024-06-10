:_mod-docs-content-type: ASSEMBLY
[id="advanced-kn-config"]
= Configuring the Knative CLI
:context: advanced-kn-config
include::_attributes/common-attributes.adoc[]

toc::[]

You can customize your Knative (`kn`) CLI setup by creating a `config.yaml` configuration file. You can provide this configuration by using the `--config` flag, otherwise the configuration is picked up from a default location. The default configuration location conforms to the https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html[XDG Base Directory Specification], and is different for UNIX systems and Windows systems.

For UNIX systems:

* If the `XDG_CONFIG_HOME` environment variable is set, the default configuration location that the Knative (`kn`) CLI looks for is `$XDG_CONFIG_HOME/kn`.

* If the `XDG_CONFIG_HOME` environment variable is not set, the Knative (`kn`) CLI looks for the configuration in the home directory of the user at `$HOME/.config/kn/config.yaml`.

For Windows systems, the default Knative (`kn`) CLI configuration location is `%APPDATA%\kn`.

.Example configuration file
[source,yaml]
----
plugins:
  path-lookup: true <1>
  directory: ~/.config/kn/plugins <2>
eventing:
  sink-mappings: <3>
  - prefix: svc <4>
    group: core <5>
    version: v1 <6>
    resource: services <7>
----
<1> Specifies whether the Knative (`kn`) CLI should look for plugins in the `PATH` environment variable. This is a boolean configuration option. The default value is `false`.
<2> Specifies the directory where the Knative (`kn`) CLI looks for plugins. The default path depends on the operating system, as described previously. This can be any directory that is visible to the user.
<3> The `sink-mappings` spec defines the Kubernetes addressable resource that is used when you use the `--sink` flag with a Knative (`kn`) CLI command.
<4> The prefix you want to use to describe your sink. `svc` for a service, `channel`, and `broker` are predefined prefixes for the Knative (`kn`) CLI.
<5> The API group of the Kubernetes resource.
<6> The version of the Kubernetes resource.
<7> The plural name of the Kubernetes resource type. For example, `services` or `brokers`.
