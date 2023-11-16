FROM registry.ci.openshift.org/ocp/ubi-minimal:8

WORKDIR /src

RUN microdnf install -y git ruby which && microdnf clean all && rm -rf /var/cache/yum

RUN gem install asciidoctor asciidoctor-diagram

RUN git config --system --add safe.directory '*'

CMD ["/bin/bash"]
