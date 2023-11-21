// Module included in the following assemblies:
//
// * microshift/running_applications/microshift-deploy-with-mirror-registry.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-uploading-container-images-to-mirror_{context}"]
= Uploading container images to a mirror registry

To use your container images at an air-gapped site, upload them to the mirror registry using the following procedure.

.Prerequisites

* You are logged into a host with access to `microshift-quay`.
* The `.pull-secret-mirror.json` file is available locally.
* The `microshift-containers` directory contents are available locally.

.Procedure

. Install the `skopeo` tool used for copying the container images by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y skopeo
----

. Set the environment variables pointing to the pull secret file:
+
[source,terminal]
----
$ IMAGE_PULL_FILE=~/.pull-secret-mirror.json
----

. Set the environment variables pointing to the local container image directory:
+
[source,terminal]
----
$ IMAGE_LOCAL_DIR=~/microshift-containers
----

. Set the environment variables pointing to the mirror registry URL for uploading the container images:
+
[source,terminal]
----
$ TARGET_REGISTRY=<registry_host>:<port> <1>
----
<1> Replace `<registry_host>:<port>` with the host name and port of your mirror registry server.

. Run the following script to upload the container images to the `${TARGET_REGISTRY}` mirror registry:
+
[source,terminal]
----
image_tag=mirror-$(date +%y%m%d%H%M%S)
image_cnt=1
   # Uses timestamp and counter as a tag on the target images to avoid
   # their overwrite by the 'latest' automatic tagging

pushd "${IMAGE_LOCAL_DIR}" >/dev/null
while read -r src_manifest ; do
   # Remove the manifest.json file name
   src_img=$(dirname "${src_manifest}")
   # Add the target registry prefix and remove SHA
   dst_img="${TARGET_REGISTRY}/${src_img}"
   dst_img=$(echo "${dst_img}" | awk -F'@' '{print $1}')

   # Run the image upload command
   echo "Uploading '${src_img}' to '${dst_img}'"
   skopeo copy --all --quiet \
      --preserve-digests \
      --authfile "${IMAGE_PULL_FILE}" \
      dir://"${IMAGE_LOCAL_DIR}/${src_img}" docker://"${dst_img}:${image_tag}-${image_cnt}"
   # Increment the counter
   (( image_cnt += 1 ))

done < <(find . -type f -name manifest.json -printf '%P\n')
popd >/dev/null
----
