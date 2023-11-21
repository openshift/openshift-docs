FROM ruby:3.1.2-alpine

RUN apk add --update --no-cache git bash

WORKDIR /go/src/github.com/openshift/openshift-docs

CMD ["/bin/bash"]
