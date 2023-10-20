#!/bin/bash

# Use this with the get-updated-distros.sh script:
# ./scripts/get-updated-distros.sh | ./scripts/build-distros.sh

while read -r FILENAME; do
    case "$FILENAME" in
        "_topic_maps/_topic_map.yml")
            python3 build.py --distro openshift-enterprise --product "OpenShift Container Platform" --version 4.14 --no-upstream-fetch
            ;;
        "_topic_maps/_topic_map_osd.yml")
            python3 build.py --distro openshift-dedicated --product "OpenShift Dedicated" --version 4 --no-upstream-fetch
            ;;
        "_topic_maps/_topic_map_ms.yml")
            python3 build.py --distro microshift --product "Microshift" --version 4 --no-upstream-fetch
            ;;
        "_topic_maps/_topic_map_rosa.yml")
            python3 build.py --distro openshift-rosa --product "Red Hat OpenShift Service on AWS" --version 4 --no-upstream-fetch
            ;;
        "_distro_map.yml")
            python3 build.py --distro openshift-enterprise --product "OpenShift Container Platform" --version 4.14 --no-upstream-fetch
            ;;
        *)
            echo "Error: Unrecognized filename: $FILENAME" >&2
            exit 1
            ;;
    esac
done
