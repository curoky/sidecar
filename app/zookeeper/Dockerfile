FROM curoky/sidecar:ubuntu22.10-sre

RUN mkdir /opt/zookeeper \
  && curl -sSL https://archive.apache.org/dist/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz \
    | tar -xz --strip-components=1 -C /opt/zookeeper

COPY app/zookeeper/conf/* /opt/zookeeper/conf/
COPY app/zookeeper/entrypoint.sh /opt/zookeeper/entrypoint.sh

WORKDIR /opt/zookeeper

CMD ["/opt/zookeeper/entrypoint.sh"]
