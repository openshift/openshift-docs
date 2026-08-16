:_mod-docs-content-type: CONCEPT
[id="about-the-devfile-in-odo"]
= About the devfile in {odo-title}

The devfile is a portable file that describes your development environment.
With the devfile, you can define a portable developmental environment without the need for reconfiguration.

With the devfile, you can describe your development environment, such as the source code, IDE tools, application runtimes, and predefined commands. To learn more about the devfile, see link:https://redhat-developer.github.io/devfile/[the devfile documentation].

With `{odo-title}`, you can create components from the devfiles. When creating a component by using a devfile, `{odo-title}` transforms the devfile into a workspace consisting of multiple containers that run on {product-title}, Kubernetes, or Docker.
`{odo-title}` automatically uses the default devfile registry but users can add their own registries.
