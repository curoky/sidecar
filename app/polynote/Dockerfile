FROM curoky/sidecar:ubuntu22.10-sre

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

RUN mkdir /opt/hadoop \
  && curl -sSL https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hadoop

COPY app/hadoop/conf/* /opt/hadoop/etc/hadoop/
COPY app/hadoop/entrypoint.sh /opt/hadoop/entrypoint.sh

###############################################################################

RUN mkdir /opt/polynote \
  && curl -sSL https://github.com/polynote/polynote/releases/download/0.5.0/polynote-dist.tar.gz \
    | tar -xz --strip-components=1 -C /opt/polynote

COPY app/polynote/conf/* /opt/polynote/
COPY app/polynote/entrypoint.sh /opt/polynote/entrypoint.sh

WORKDIR /opt/polynote

RUN sed -i 's/==1.2.5//g' ./requirements.txt \
  && pip install -r ./requirements.txt

CMD ["/opt/polynote/entrypoint.sh"]
