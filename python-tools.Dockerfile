FROM registry.access.redhat.com/ubi8/ubi-minimal

RUN microdnf install -y git python39 python39-pip which && microdnf clean all && rm -rf /var/cache/yum

WORKDIR /src

RUN git config --system --add safe.directory '*'

COPY ./aura.tar.gz /src

RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel pyyaml && pip install --no-cache-dir /src/aura.tar.gz

CMD ["/bin/bash"]
