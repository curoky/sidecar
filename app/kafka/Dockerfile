# https://kafka.apache.org/quickstart

FROM ubuntu:22.04

LABEL org.opencontainers.image.authors="cccuroky@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN apt-get update -qq \
  && apt-get install -y -qq --no-install-recommends \
    sudo ca-certificates curl git openssh-server openssh-client \
    netcat iputils-ping net-tools iproute2 ncdu \
    openjdk-11-jdk python3

RUN groupadd -g 1000 -o door \
  && useradd -m -u 1000 -g 1000 door \
  && usermod -aG sudo door \
  && echo "door:door" | chpasswd \
  && chown door:door -R /opt \
  && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY app/ssh/ssh.conf /etc/ssh/ssh_config.d/door.conf
COPY app/ssh/sshd.conf /etc/ssh/sshd_config.d/door.conf

USER door

# passwordless ssh
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \
  && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
  && chmod 0600 ~/.ssh/authorized_keys

###############################################################################

RUN mkdir /opt/kafka \
  && curl -L https://downloads.apache.org/kafka/3.2.3/kafka_2.13-3.2.3.tgz \
    | tar -xz --strip-components=1 -C /opt/kafka

COPY app/kafka/conf/zookeeper.properties /opt/kafka/config/zookeeper.properties
COPY app/kafka/conf/server.properties /opt/kafka/config/server.properties
COPY app/kafka/entrypoint.sh /opt/kafka/entrypoint.sh

WORKDIR /opt/kafka

CMD ["/opt/kafka/entrypoint.sh"]
