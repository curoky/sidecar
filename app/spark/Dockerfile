FROM curoky/sidecar:ubuntu22.04-sre

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

RUN mkdir /opt/hadoop \
  && curl -sSL https://archive.apache.org/dist/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hadoop

COPY app/hadoop/conf/* /opt/hadoop/etc/hadoop/
COPY app/hadoop/entrypoint.sh /opt/hadoop/entrypoint.sh

###############################################################################

ENV SPARK_HOME=/opt/spark

RUN mkdir /opt/spark \
  && curl -sSL https://archive.apache.org/dist/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz \
    | tar -xz --strip-components=1 -C /opt/spark

RUN wget -P /opt/spark/jars \
  https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.3.0/spark-sql-kafka-0-10_2.12-3.3.0.jar \
  https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10-assembly_2.12/3.3.0/spark-streaming-kafka-0-10-assembly_2.12-3.3.0.jar \
  https://repo1.maven.org/maven2/org/apache/hudi/hudi-spark3.3-bundle_2.12/0.12.0/hudi-spark3.3-bundle_2.12-0.12.0.jar \
  https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar

COPY app/spark/entrypoint.sh /opt/spark/entrypoint.sh

RUN cp /opt/spark/conf/log4j2.properties.template /opt/spark/conf/log4j2.properties

WORKDIR /opt/spark

CMD ["/opt/spark/entrypoint.sh"]
