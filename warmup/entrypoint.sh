#!/usr/bin/env bash
# Copyright (c) 2018-2022 curoky(cccuroky@gmail.com).
#
# This file is part of my-own-x.
# See https://github.com/curoky/my-own-x for further info.
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

while ! nc -zv kafka 40800; do
  sleep 1
done

/opt/kafka/warmup/create-test-topic.py
/opt/kafka/warmup/test-producer.py &
/opt/kafka/warmup/test-consumer.py &

while ! nc -zv hadoop 42016; do
  sleep 1
done
/opt/hadoop/warmup/prepare-test-data.sh

while ! nc -zv spark 43201; do
  sleep 1
done
/opt/spark/warmup/word_count.py /LICENSE.txt

while true; do sleep 1000; done
