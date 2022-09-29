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

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

RUN mkdir /opt/hadoop \
  && curl -sSL https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz \
    | tar -xz --strip-components=1 -C /opt/hadoop

COPY app/hadoop/conf/* /opt/hadoop/etc/hadoop/
COPY app/hadoop/entrypoint.sh /opt/hadoop/entrypoint.sh

###############################################################################

RUN mkdir /opt/spark \
  && curl -sSL https://dlcdn.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3-scala2.13.tgz \
    | tar -xz --strip-components=1 -C /opt/spark

###############################################################################

RUN sudo apt-get install -y -qq --no-install-recommends \
    python3-pip \
  && pip3 install --user kafka-python pyspark[sql]

RUN mkdir /opt/warmup

COPY app/ /opt/
COPY warmup/entrypoint.sh /opt/warmup/entrypoint.sh

WORKDIR /opt/warmup

CMD ["/opt/warmup/entrypoint.sh"]