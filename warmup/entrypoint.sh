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
sudo chown -R cicada:cicada /var/log/app/warmup

while ! nc -zv kafka 40800; do
  sleep 5
done
/opt/kafka/warmup/create_mock_data.py >/var/log/app/warmup/kafka-create_mock_data.log 2>&1 &

while ! nc -zv mysql 40200; do
  sleep 5
done
/opt/mysql/warmup/create_mock_data.py >/var/log/app/warmup/mysql-create_mock_data.log 2>&1 &

while ! nc -zv hadoop 42016; do
  sleep 5
done
/opt/hadoop/warmup/create_mock_data.py >/var/log/app/warmup/hadoop-create_mock_data.log 2>&1 &

while true; do sleep 1000; done
