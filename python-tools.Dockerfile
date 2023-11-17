FROM registry.access.redhat.com/ubi8/ubi-minimal AS base

COPY . /src/

WORKDIR /src

RUN microdnf install -y git python39 python39-pip which && microdnf clean all && rm -rf /var/cache/yum

RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel pyyaml && pip install --no-cache-dir /src/aura.tar.gz

RUN git config --system --add safe.directory '*'

CMD ["/bin/bash"]
