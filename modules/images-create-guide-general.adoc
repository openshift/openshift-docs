// Module included in the following assemblies:
// * openshift_images/create-images.adoc

[id="images-create-guide-general_{context}"]
= General container image guidelines

The following guidelines apply when creating a container image in general, and are independent of whether the images are used on {product-title}.

[discrete]
== Reuse images

Wherever possible, base your image on an appropriate upstream image using the `FROM` statement. This ensures your image can easily pick up security fixes from an upstream image when it is updated, rather than you having to update your dependencies directly.

In addition, use tags in the `FROM` instruction, for example, `rhel:rhel7`, to make it clear to users exactly which version of an image your image is based on. Using a tag other than `latest` ensures your image is not subjected to breaking changes that might go into the `latest` version of an upstream image.

[discrete]
== Maintain compatibility within tags

When tagging your own images, try to maintain backwards compatibility within a tag. For example, if you provide an image named `image` and it currently includes version `1.0`, you might provide a tag of `image:v1`. When you update the image, as long as it continues to be compatible with the original image, you can continue to tag the new image `image:v1`, and downstream consumers of this tag are able to get updates without being broken.

If you later release an incompatible update, then switch to a new tag, for example `image:v2`. This allows downstream consumers to move up to the new version at will, but not be inadvertently broken by the new incompatible image. Any downstream consumer using `image:latest` takes on the risk of any incompatible changes being introduced.

[discrete]
== Avoid multiple processes

Do not start multiple services, such as a database and `SSHD`, inside one container. This is not necessary because containers are lightweight and can be easily linked together for orchestrating multiple processes. {product-title} allows you to easily colocate and co-manage related images by grouping them into a single pod.

This colocation ensures the containers share a network namespace and storage for communication. Updates are also less disruptive as each image can be updated less frequently and independently. Signal handling flows are also clearer with a single process as you do not have to manage routing signals to spawned processes.

[discrete]
== Use `exec` in wrapper scripts

Many images use wrapper scripts to do some setup before starting a process for the software being run. If your image uses such a script, that script uses `exec` so that the script's process is replaced by your software. If you do not use `exec`, then signals sent by your container runtime go to your wrapper script instead of your software's process. This is not what you want.

If you have a wrapper script that starts a process for some server. You start your container, for example, using `podman run -i`, which runs the wrapper script, which in turn starts your process. If you want to close your container with `CTRL+C`. If your wrapper script used `exec` to start the server process, `podman` sends SIGINT to the server process, and everything works as you expect. If you did not use `exec` in your wrapper script, `podman` sends SIGINT to the process for the wrapper script and your process keeps running like nothing happened.

Also note that your process runs as `PID 1` when running in a container. This means that if your main process terminates, the entire container is stopped, canceling any child processes you launched from your `PID 1` process.

////
See the http://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/["Docker and the `PID 1` zombie reaping problem"] blog article for additional implications.
Also see the https://felipec.wordpress.com/2013/11/04/init/["Demystifying the init system (PID 1)"] blog article for a deep dive on PID 1 and `init`
systems.
////

[discrete]
== Clean temporary files

Remove all temporary files you create during the build process. This also includes any files added with the `ADD` command.  For example, run the `yum clean` command after performing `yum install` operations.

You can prevent the `yum` cache from ending up in an image layer by creating your `RUN` statement as follows:

[source,terminal]
----
RUN yum -y install mypackage && yum -y install myotherpackage && yum clean all -y
----

Note that if you instead write:

[source,terminal]
----
RUN yum -y install mypackage
RUN yum -y install myotherpackage && yum clean all -y
----

Then the first `yum` invocation leaves extra files in that layer, and these files cannot be removed when the `yum clean` operation is run later. The extra files are not visible in the final image, but they are present in the underlying layers.

The current container build process does not allow a command run in a later layer to shrink the space used by the image when something was removed in an earlier layer. However, this may change in the future. This means that if you perform an `rm` command in a later layer, although the files are hidden it does not reduce the overall size of the image to be downloaded. Therefore, as with the `yum clean` example, it is best to remove files in the same command that created them, where possible, so they do not end up written to a layer.

In addition, performing multiple commands in a single `RUN` statement reduces the number of layers in your image, which improves download and extraction time.

[discrete]
== Place instructions in the proper order

The container builder reads the `Dockerfile` and runs the instructions from top to bottom. Every instruction that is successfully executed creates a layer which can be reused the next time this or another image is built. It is very important to place instructions that rarely change at the top of your `Dockerfile`. Doing so ensures the next builds of the same image are very fast because the cache is not invalidated by upper layer changes.

For example, if you are working on a `Dockerfile` that contains an `ADD` command to install a file you are iterating on, and a `RUN` command to `yum install` a package, it is best to put the `ADD` command last:

[source,terminal]
----
FROM foo
RUN yum -y install mypackage && yum clean all -y
ADD myfile /test/myfile
----

This way each time you edit `myfile` and rerun `podman build` or `docker build`, the system reuses the cached layer for the `yum` command and only generates the new layer for the `ADD` operation.

If instead you wrote the `Dockerfile` as:

[source,terminal]
----
FROM foo
ADD myfile /test/myfile
RUN yum -y install mypackage && yum clean all -y
----

Then each time you changed `myfile` and reran `podman build` or `docker build`, the `ADD` operation would invalidate the `RUN` layer cache, so the `yum` operation must be rerun as well.

[discrete]
== Mark important ports

The EXPOSE instruction makes a port in the container available to the host system and other containers. While it is possible to specify that a port should be exposed with a `podman run` invocation, using the EXPOSE instruction in a `Dockerfile` makes it easier for both humans and software to use your image by explicitly declaring the ports your software needs to run:

* Exposed ports show up under `podman ps` associated with containers created from your image.
* Exposed ports are present in the metadata for your image returned by `podman inspect`.
* Exposed ports are linked when you link one container to another.

[discrete]
== Set environment variables

It is good practice to set environment variables with the `ENV` instruction. One example is to set the version of your project. This makes it easy for people to find the version without looking at the `Dockerfile`. Another example is advertising a path on the system that could be used by another process, such as `JAVA_HOME`.

[discrete]
== Avoid default passwords

Avoid setting default passwords. Many people extend the image and forget to remove or change the default password. This can lead to security issues if a user in production is assigned a well-known password. Passwords are configurable using an environment variable instead.

If you do choose to set a default password, ensure that an appropriate warning message is displayed when the container is started. The message should inform the user of the value of the default password and explain how to change it, such as what environment variable to set.

[discrete]
== Avoid sshd

It is best to avoid running `sshd` in your image. You can use the `podman exec` or `docker exec` command to access containers that are running on the local host. Alternatively, you can use the `oc exec` command or the `oc rsh` command to access containers that are running on the {product-title} cluster. Installing and running `sshd` in your image opens up additional vectors for attack and requirements for security patching.

[discrete]
== Use volumes for persistent data

Images use a link:https://docs.docker.com/reference/builder/#volume[volume] for persistent data. This way {product-title} mounts the network storage to the node running the container, and if the container moves to a new node the storage is reattached to that node. By using the volume for all persistent storage needs, the content is preserved even if the container is restarted or moved. If your image writes data to arbitrary locations within the container, that content could not be preserved.

All data that needs to be preserved even after the container is destroyed must be written to a volume. Container engines support a `readonly` flag for containers, which can be used to strictly enforce good practices about not writing data to ephemeral storage in a container. Designing your image around that capability now makes it easier to take advantage of it later.

Explicitly defining volumes in your `Dockerfile` makes it easy for consumers of the image to understand what volumes they must define when running your image.

See the link:https://kubernetes.io/docs/concepts/storage/volumes/[Kubernetes
documentation] for more information on how volumes are used in {product-title}.

////
For more information on how Volumes are used in {product-title}, see https://kubernetes.io/docs/concepts/storage/volumes[this documentation]. (NOTE to docs team:  this link should really go to something in the openshift docs, once we have it)
////

[NOTE]
====
Even with persistent volumes, each instance of your image has its own volume, and the filesystem is not shared between instances. This means the volume cannot be used to share state in a cluster.
====

////
[role="_additional-resources"]
.Additional resources

* Docker documentation - https://docs.docker.com/articles/dockerfile_best-practices/[Best practices for writing Dockerfiles]

* Project Atomic documentation - http://www.projectatomic.io/docs/docker-image-author-guidance/[Guidance for Container Image Authors]
////
