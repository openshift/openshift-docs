FROM alpine:3.21.3

ARG BUILD_DATE

LABEL architecture="amd64/x86_64" \
    alpine-version="3.21.3" \
    org.opencontainers.image.title="dicso-docs" \
    org.opencontainers.image.description="Alpine with Nginx for hosting disconnected version of the OpenShift docs" \
    org.opencontainers.image.base.name="docker.io/library/alpine:3.21.3" \
    org.opencontainers.image.created=$BUILD_DATE

RUN \
  runtime_pkgs="nginx ca-certificates openssl pcre zlib tzdata" && \
  apk --no-cache add ${runtime_pkgs} && \
  mkdir -p /nginx/data && \
  chown -R nginx:nginx /nginx/data && \
  rm -rf /var/cache/apk/*

VOLUME ["/nginx/data"]

COPY files/nginx.conf /etc/nginx/nginx.conf
COPY files/_stylesheets /etc/nginx/data/_stylesheets
COPY files/_images /etc/nginx/data/_images
COPY files/_javascripts /etc/nginx/data/_javascripts

EXPOSE 8080 8443

CMD ["nginx"]