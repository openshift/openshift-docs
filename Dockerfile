# Dockerfile
FROM centos:8
RUN dnf install git python3 python3-devel ruby rubygems -y
RUN gem install asciidoctor asciidoctor-diagram
COPY . $HOME/src/
RUN pip3 install pyyaml /src/aura.tar.gz
