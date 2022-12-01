# Dockerfile for build tools
FROM fedora
# the ruby dependencies are needed to install asciidoctor and ascii_binder
# gcc-c++ is needed to build native versions of some ruby plugins
# git is needed by ascii_binder to find the branches in a repo
RUN dnf install -y rubygems ruby-devel gcc-c++ make git
RUN gem install asciidoctor asciidoctor-diagram ascii_binder
