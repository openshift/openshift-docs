FROM ruby:3.1.2-alpine AS builder

RUN apk update && apk add --virtual build-dependencies build-base

RUN gem install listen asciidoctor asciidoctor-diagram ascii_binder

FROM ruby:3.1.2-alpine

COPY --from=builder /usr/local/bundle /usr/local/bundle

RUN apk add --update --no-cache git bash

CMD ["/bin/bash"]
