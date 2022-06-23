// Module included in the following assemblies:
//
//* builds/build-strategies.adoc
// * openshift_images/create-images.adoc

[id="images-create-s2i-scripts_{context}"]
= How to write source-to-image scripts

You can write source-to-image (S2I) scripts in any programming language, as long as the scripts are executable inside the builder image. S2I supports multiple options providing `assemble`/`run`/`save-artifacts` scripts. All of these locations are checked on each build in the following order:

. A script specified in the build configuration.
. A script found in the application source `.s2i/bin` directory.
. A script found at the default image URL with the `io.openshift.s2i.scripts-url` label.

Both the `io.openshift.s2i.scripts-url` label specified in the image and the script specified in a build configuration can take one of the following forms:

* `image:///path_to_scripts_dir`: absolute path inside the image to a directory where the S2I scripts are located.
* `$$file:///path_to_scripts_dir$$`: relative or absolute path to a directory on the host where the S2I scripts are located.
* `http(s)://path_to_scripts_dir`: URL to a directory where the S2I scripts are located.

.S2I scripts
[cols="3a,8a",options="header"]
|===

|Script |Description

|`assemble`
|The `assemble` script builds the application artifacts from a source and places them into appropriate directories inside the image. This script is required. The workflow for this script is:

. Optional: Restore build artifacts. If you want to support incremental builds, make sure to define `save-artifacts` as well.
. Place the application source in the desired location.
. Build the application artifacts.
. Install the artifacts into locations appropriate for them to run.

|`run`
|The `run` script executes your application. This script is required.

|`save-artifacts`
|The `save-artifacts` script gathers all dependencies that can speed up the build processes that follow. This script is optional. For example:

* For Ruby, `gems` installed by Bundler.
* For Java, `.m2` contents.

These dependencies are gathered into a `tar` file and streamed to the standard output.

|`usage`
|The `usage` script allows you to inform the user how to properly use your image. This script is optional.

|`test/run`
|The `test/run` script allows you to create a process to check if the image is working correctly. This script is optional. The proposed flow of that process is:

. Build the image.
. Run the image to verify the `usage` script.
. Run `s2i build` to verify the `assemble` script.
. Optional: Run `s2i build` again to verify the `save-artifacts` and `assemble` scripts save and restore artifacts functionality.
. Run the image to verify the test application is working.

[NOTE]
====
The suggested location to put the test application built by your `test/run` script is the `test/test-app` directory in your image repository.
====
|===

*Example S2I scripts*

The following example S2I scripts are written in Bash. Each example assumes its `tar` contents are unpacked into the `/tmp/s2i` directory.

.`assemble` script:
[source,bash]
----
#!/bin/bash

# restore build artifacts
if [ "$(ls /tmp/s2i/artifacts/ 2>/dev/null)" ]; then
    mv /tmp/s2i/artifacts/* $HOME/.
fi

# move the application source
mv /tmp/s2i/src $HOME/src

# build application artifacts
pushd ${HOME}
make all

# install the artifacts
make install
popd
----

.`run` script:
[source,bash]
----
#!/bin/bash

# run the application
/opt/application/run.sh
----


.`save-artifacts` script:
[source,bash]
----
#!/bin/bash

pushd ${HOME}
if [ -d deps ]; then
    # all deps contents to tar stream
    tar cf - deps
fi
popd
----

.`usage` script:
[source,bash]
----
#!/bin/bash

# inform the user how to use the image
cat <<EOF
This is a S2I sample builder image, to use it, install
https://github.com/openshift/source-to-image
EOF
----

[role="_additional-resources"]
.Additional resources
* link:https://blog.openshift.com/create-s2i-builder-image/[S2I Image Creation Tutorial]

////
* See the link:https://docs.docker.com/engine/reference/builder/#onbuild[Docker
documentation] for more information on `ONBUILD`.
////
