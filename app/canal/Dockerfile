FROM curoky/sidecar:ubuntu22.10-sre

RUN mkdir /opt/canal \
  && curl -sSL https://github.com/alibaba/canal/releases/download/canal-1.1.6/canal.deployer-1.1.6.tar.gz \
    | tar -xz --strip-components=0 -C /opt/canal

COPY app/canal/conf/canal.properties /opt/canal/conf/canal.properties
COPY app/canal/conf/example/instance.properties /opt/canal/conf/example/instance.properties
COPY app/canal/entrypoint.sh /opt/canal/entrypoint.sh

WORKDIR /opt/canal

CMD ["/opt/canal/entrypoint.sh"]
