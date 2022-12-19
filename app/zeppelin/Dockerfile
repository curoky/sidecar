FROM curoky/sidecar:ubuntu22.10-sre

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

RUN mkdir /opt/hadoop \
  && curl -sSL https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hadoop

COPY app/hadoop/conf/* /opt/hadoop/etc/hadoop/
COPY app/hadoop/entrypoint.sh /opt/hadoop/entrypoint.sh

###############################################################################

ENV ZEPPELIN_HOME=/opt/zeppelin

RUN mkdir /opt/zeppelin \
  && curl -sSL https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz \
    | tar -xz --strip-components=1 -C /opt/zeppelin

COPY app/zeppelin/conf/* /opt/zeppelin/conf/
COPY app/zeppelin/entrypoint.sh /opt/zeppelin/entrypoint.sh

WORKDIR /opt/zeppelin

CMD ["/opt/zeppelin/entrypoint.sh"]
