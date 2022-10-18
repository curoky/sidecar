FROM curoky/sidecar:ubuntu22.04-sre

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

RUN mkdir /opt/hadoop \
  && curl -sSL https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hadoop

COPY app/hadoop/conf/* /opt/hadoop/etc/hadoop/
COPY app/hadoop/entrypoint.sh /opt/hadoop/entrypoint.sh

###############################################################################

RUN mkdir /opt/spark \
  && curl -sSL https://dlcdn.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz \
    | tar -xz --strip-components=1 -C /opt/spark

###############################################################################

RUN sudo apt-get install -y -qq --no-install-recommends \
    python3-pip \
  && pip3 install --user kafka-python pyspark[sql] redis[hiredis] pymongo[srv]

RUN mkdir /opt/warmup

COPY app/ /opt/
COPY warmup/entrypoint.sh /opt/warmup/entrypoint.sh

WORKDIR /opt/warmup

CMD ["/opt/warmup/entrypoint.sh"]
