FROM registry.access.redhat.com/ubi8/ruby-30:latest

ENV LANG=en_US.UTF-8

WORKDIR /go/src/github.com/openshift/openshift-docs

CMD ["/bin/bash"]
