FROM curoky/sidecar:ubuntu22.04-sre

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

RUN mkdir /opt/hadoop \
  && curl -sSL https://archive.apache.org/dist/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hadoop

COPY app/hadoop/conf/* /opt/hadoop/etc/hadoop/
COPY app/hadoop/entrypoint.sh /opt/hadoop/entrypoint.sh

###############################################################################

RUN mkdir /opt/flink \
  && curl -sSL https://archive.apache.org/dist/flink/flink-1.15.2/flink-1.15.2-bin-scala_2.12.tgz \
    | tar -xz --strip-components=1 -C /opt/flink

COPY app/flink/conf/* /opt/flink/conf/
COPY app/flink/entrypoint.sh /opt/flink/entrypoint.sh

WORKDIR /opt/flink

CMD ["/opt/flink/entrypoint.sh"]
