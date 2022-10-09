FROM fluent/fluentd:v1.15-debian-1
LABEL org.opencontainers.image.authors="cccuroky@gmail.com"

USER root

COPY app/fluentd/conf /fluentd/etc

RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.2.4"]

# USER fluent
