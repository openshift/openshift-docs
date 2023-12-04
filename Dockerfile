FROM registry.access.redhat.com/ubi8/ruby-30:latest

ENV LANG=en_US.UTF-8

USER root

RUN yum update -y && yum install -y jq && yum clean all

WORKDIR /go/src/github.com/openshift/openshift-docs

CMD ["/bin/bash"]
