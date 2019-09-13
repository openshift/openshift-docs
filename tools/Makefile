all: build

PACKAGE=github.com/openshift-docs/tools
BIN=$(lastword $(subst /, ,$(PACKAGE)))

GO=GO111MODULE=on GOFLAGS=-mod=vendor go
GO_BUILD_RECIPE=CGO_ENABLED=0 $(GO) build -o $(BIN) .

TEST ?= .*

.PHONY: build
build:
	$(GO_BUILD_RECIPE)

.PHONY: test
test:
	$(GO) test ./...
