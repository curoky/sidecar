FROM curoky/sidecar:ubuntu22.10-sre

USER root
RUN apt-get install -y apt-transport-https ca-certificates dirmngr \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 8919F6BD2B48D754 \
  && echo "deb https://packages.clickhouse.com/deb stable main" | sudo tee \
    /etc/apt/sources.list.d/clickhouse.list \
  && apt-get update \
  && apt-get install -y clickhouse-server clickhouse-client

USER cicada
# sudo service clickhouse-server start
# clickhouse-client # or "clickhouse-client --password" if you've set up a password.

COPY app/clickhouse/entrypoint.sh /opt/clickhouse/entrypoint.sh

# WORKDIR /opt/spark

CMD ["/opt/clickhouse/entrypoint.sh"]
