FROM curoky/sidecar:ubuntu22.04-sre

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

RUN mkdir /opt/hadoop \
  && curl -sSL https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hadoop

COPY app/hadoop/conf/* /opt/hadoop/etc/hadoop/
COPY app/hadoop/entrypoint.sh /opt/hadoop/entrypoint.sh

###############################################################################

ENV HIVE_HOME=/opt/hive

RUN mkdir /opt/hive \
  && curl -sSL https://dlcdn.apache.org/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hive

COPY app/hive/conf/* /opt/hive/conf/
COPY app/hive/entrypoint.sh /opt/hive/entrypoint.sh

WORKDIR /opt/hive

CMD ["/opt/hive/entrypoint.sh"]
