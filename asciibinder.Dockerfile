FROM registry.access.redhat.com/ubi8/ruby-27

ENV LANG=en_US.UTF-8

USER root

RUN gem install listen:3.0.8 ascii_binder && \
    yum clean all

LABEL url="http://www.asciibinder.org" \
      summary="a documentation system built on Asciidoctor" \
      description="Run the asciibinder container image from the local docs repo, which is mounted into the container. Pass asciibinder commands to run the build. Generated files are owned by root." \
      RUN="docker run -it --rm \
          -v `pwd`:/src:z \
          IMAGE"

WORKDIR /src