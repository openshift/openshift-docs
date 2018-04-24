all:
	./_update_rest_api.py
.PHONY: all

master-node-api:
	# this invocation assumes you have origin's code available in GOPATH
	go run main.go github.com/openshift/origin/pkg/cmd/server/apis/config/v1>install_config/master_node_configuration_api.adoc
.PHONY: master-node-api
