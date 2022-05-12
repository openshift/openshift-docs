# Dockerfile
FROM fedora:latest AS builder

RUN dnf install -y git make gcc-c++ ruby rubygems ruby-devel \
    && gem install asciidoctor ascii_binder asciidoctor-diagram --no-document

FROM fedora:latest

ENV LC_ALL=C.UTF-8

RUN dnf install -y git ruby \
    && dnf clean all \
    && mkdir -p {/usr/local/share/gems,/usr/share/rubygems,/opt/openshift-docs}

COPY --from=builder /usr/local/lib64/gems /usr/local/lib64/gems/
COPY --from=builder /usr/local/share/gems /usr/local/share/gems/
COPY --from=builder /usr/local/bin/ascii* /usr/local/bin/

WORKDIR /opt/openshift-docs
