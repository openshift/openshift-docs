#!/bin/bash

# Red Hat Advanced Cluster Security for Kubernetes
# Retrieve root certificates and create a private value yaml file.

create_certificate_values_file() {
    if [[ "$#" -ne 1 ]]; then
        echo "wrong args. usage: create_certificate_values_file <path_to_values_file>"
        exit 1
    fi

    local cert_path="$1"
    echo "Create root certificates values file"
    # get root ca
    caKey=$(kubectl -n stackrox get secret central-tls -o go-template='{{ index .data "ca-key.pem" }}' | base64 --decode)
    caPem=$(kubectl -n stackrox get secret central-tls -o go-template='{{ index .data "ca.pem" }}' | base64 --decode)

    # create root certificates value file
    yq e -n ".ca.cert = \"${caPem}\" | .ca.key = \"${caKey}\"" > "$cert_path"
}

create_certificate_values_file "$@"
