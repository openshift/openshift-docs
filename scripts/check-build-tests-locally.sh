#!/bin/bash

# Define an array of local script names
local_scripts=("./scripts/check-rn-link-perms.sh" "./scripts/check-asciidoctor-build.sh")

# Function to run a local script and report pass/fail
run_local_script() {
  local script_name=$1
  echo "Running $script_name..."
  ./$script_name   # Execute the local script
  
  # Check the exit status of the last command
  if [ $? -eq 0 ]; then
    echo "$script_name: Pass"
    echo ""
  else
    echo "$script_name: Fail"
    echo "Build check failed, exiting."
    exit 1
  fi
}

# Iterate through the array and run each local script
for script in "${local_scripts[@]}"; do
  run_local_script "$script"
done

# Ask the user to enter the version number
read -p "Enter the version number of the target branch, for example '4.13': " version_number

# Validate if the version number is not empty
if [ -z "$version_number" ]; then
  echo "Version number cannot be empty. Exiting."
  exit 1
fi

./scripts/get-updated-distros.sh |
            while read -r filename; do
              if [ "$filename" == "_topic_maps/_topic_map.yml" ]; then podman run --rm -it -v `pwd`:/openshift-docs-build:Z quay.io/openshift-cs/openshift-docs-build python3 build_for_portal.py --distro openshift-enterprise --product "OpenShift Container Platform" --version "$version_number" --no-upstream-fetch && python3 makeBuild.py

              elif [ "$filename" == "_topic_maps/_topic_map_osd.yml" ]; then podman run --rm -it -v `pwd`:/openshift-docs-build:Z quay.io/openshift-cs/openshift-docs-build python3 build_for_portal.py --distro openshift-enterprise --product "OpenShift Container Platform" --version "$version_number" --no-upstream-fetch && python3 makeBuild.py

              elif [ "$filename" == "_topic_maps/_topic_map_ms.yml" ]; then podman run --rm -it -v `pwd`:/openshift-docs-build:Z quay.io/openshift-cs/openshift-docs-build python3 build_for_portal.py --distro openshift-enterprise --product "OpenShift Container Platform" --version "$version_number" --no-upstream-fetch && python3 makeBuild.py

              elif [ "$filename" == "_topic_maps/_topic_map_rosa.yml" ]; then podman run --rm -it -v `pwd`:/openshift-docs-build:Z quay.io/openshift-cs/openshift-docs-build python3 build_for_portal.py --distro openshift-enterprise --product "OpenShift Container Platform" --version "$version_number" --no-upstream-fetch && python3 makeBuild.py

              elif [ "$filename" == "_distro_map.yml" ]; then podman run --rm -it -v `pwd`:/openshift-docs-build:Z quay.io/openshift-cs/openshift-docs-build python3 build_for_portal.py --distro openshift-enterprise --product "OpenShift Container Platform" --version "$version_number" --no-upstream-fetch && python3 makeBuild.py
              fi
            done

