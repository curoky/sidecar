FROM curoky/sidecar:ubuntu22.10-sre

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

RUN mkdir /opt/hadoop \
  && curl -sSL https://archive.apache.org/dist/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hadoop

COPY app/hadoop/conf/* /opt/hadoop/etc/hadoop/
COPY app/hadoop/entrypoint.sh /opt/hadoop/entrypoint.sh

###############################################################################

RUN mkdir /opt/flink \
  && curl -sSL https://archive.apache.org/dist/flink/flink-1.16.0/flink-1.16.0-bin-scala_2.12.tgz \
    | tar -xz --strip-components=1 -C /opt/flink

RUN wget -P /opt/flink/lib/ \
  https://repo1.maven.org/maven2/org/apache/kafka/kafka_2.12/3.3.1/kafka_2.12-3.3.1.jar \
  https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.3.1/kafka-clients-3.3.1.jar \
  https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka/1.16.0/flink-connector-kafka-1.16.0.jar
  https://repo1.maven.org/maven2/org/apache/flink/flink-sql-connector-kafka/1.16.0/flink-sql-connector-kafka-1.16.0.jar \

COPY app/flink/conf/* /opt/flink/conf/
COPY app/flink/entrypoint.sh /opt/flink/entrypoint.sh

WORKDIR /opt/flink

CMD ["/opt/flink/entrypoint.sh"]
