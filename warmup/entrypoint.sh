#!/usr/bin/env bash
# Copyright (c) 2022-2022 curoky(cccuroky@gmail.com).
#
# This file is part of sidecar.
# See https://github.com/curoky/sidecar for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -xeuo pipefail

sudo service ssh start

if [[ ! -d /var/log/app/warmup ]]; then
  sudo mkdir -p /var/log/app/warmup
fi
sudo chown -R door:door /var/log/app/warmup

while ! nc -zv redis 6379; do
  sleep 1
done
/opt/redis/warmup/test-set-get.py >/var/log/app/warmup/redis.log 2>&1

while ! nc -zv mongo 27017; do
  sleep 1
done
/opt/mongodb/warmup/test-set-get.py >/var/log/app/warmup/mongodb.log 2>&1

while ! nc -zv kafka 40800; do
  sleep 1
done

/opt/kafka/warmup/create-test-topic.py >/var/log/app/warmup/kafka-create-test-topic.log 2>&1
/opt/kafka/warmup/test-producer.py >/var/log/app/warmup/kafka-producer.log 2>&1 &
/opt/kafka/warmup/test-consumer.py >/var/log/app/warmup/kafka-consumer.log 2>&1 &

while ! nc -zv hadoop 42016; do
  sleep 1
done
/opt/hadoop/warmup/prepare-test-data.sh >/var/log/app/warmup/hadoop.log 2>&1

while ! nc -zv spark 43201; do
  sleep 1
done
/opt/spark/warmup/word_count.py /LICENSE.txt >/var/log/app/warmup/spark.log 2>&1

while true; do sleep 1000; done
