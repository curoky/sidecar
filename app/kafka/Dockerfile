FROM curoky/sidecar:ubuntu22.10-sre

# https://kafka.apache.org/quickstart

RUN mkdir /opt/kafka \
  && curl -L https://dlcdn.apache.org/kafka/3.2.3/kafka_2.12-3.2.3.tgz \
    | tar -xz --strip-components=1 -C /opt/kafka

COPY app/kafka/conf/* /opt/kafka/config/
COPY app/kafka/entrypoint.sh /opt/kafka/entrypoint.sh

WORKDIR /opt/kafka

CMD ["/opt/kafka/entrypoint.sh"]
