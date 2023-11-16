FROM ruby:3.1.2-alpine3.16 AS builder

RUN apk update && apk add --virtual build-dependencies build-base

RUN gem install listen ascii_binder

FROM ruby:3.1.2-alpine3.16

COPY --from=builder /usr/local/bundle /usr/local/bundle

RUN apk add --update --no-cache diffutils findutils git

RUN git config --system --add safe.directory '*'

WORKDIR /src

CMD ["/bin/sh"]
