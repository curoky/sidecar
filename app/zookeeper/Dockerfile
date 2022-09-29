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

RUN mkdir /opt/zookeeper \
  && curl -sSL https://dlcdn.apache.org/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz \
    | tar -xz --strip-components=1 -C /opt/zookeeper

COPY app/zookeeper/conf/* /opt/zookeeper/conf/
COPY app/zookeeper/entrypoint.sh /opt/zookeeper/entrypoint.sh

WORKDIR /opt/zookeeper

CMD ["/opt/zookeeper/entrypoint.sh"]
