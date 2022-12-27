FROM curoky/sidecar:ubuntu22.10-sre

RUN pip install clip-server

RUN mkdir -p ~/.cache/clip \
  && curl -sSL https://clip-as-service.s3.us-east-2.amazonaws.com/models/torch/ViT-B-32.pt -o ~/.cache/clip/ViT-B-32.pt

COPY app/clip-server/entrypoint.sh /opt/clip-server/entrypoint.sh

CMD ["/opt/clip-server/entrypoint.sh"]
