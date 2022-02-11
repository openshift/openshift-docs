# Dockerfile
FROM fedora:35
RUN yum install -y git python3 python3-pip ruby
RUN gem install asciidoctor asciidoctor-diagram
COPY . $HOME/src/
RUN pip3 install pyyaml /src/aura.tar.gz
