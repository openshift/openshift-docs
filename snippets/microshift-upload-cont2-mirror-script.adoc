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