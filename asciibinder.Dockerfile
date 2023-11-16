FROM registry.ci.openshift.org/ocp/ubi-ruby-27:8

ENV LANG=en_US.UTF-8

USER root

RUN gem install listen ascii_binder && yum clean all

WORKDIR /src

RUN git config --system --add safe.directory '*'

CMD ["/bin/bash"]
