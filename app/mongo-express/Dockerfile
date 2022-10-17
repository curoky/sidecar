FROM curoky/sidecar:ubuntu22.04-sre

USER cicada

ENV ME_CONFIG_MONGODB_ENABLE_ADMIN="true" \
    ME_CONFIG_MONGODB_ADMINUSERNAME="root" \
    ME_CONFIG_MONGODB_ADMINPASSWORD="example" \
    ME_CONFIG_MONGODB_URL="mongodb://root:example@mongo:27017" \
    ME_CONFIG_BASICAUTH_USERNAME='' \
    ME_CONFIG_BASICAUTH_PASSWORD='' \
    VCAP_APP_HOST="0.0.0.0"

RUN sudo yarn add mongo-express \
  && mkdir /opt/mongo-express

COPY app/mongo-express/entrypoint.sh /opt/mongo-express/entrypoint.sh

WORKDIR /opt/mongo-express

CMD ["/opt/mongo-express/entrypoint.sh"]
