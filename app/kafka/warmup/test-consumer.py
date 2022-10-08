#!/usr/bin/env python3
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

import logging
import time

from kafka import KafkaProducer


def main():
    producer = KafkaProducer(bootstrap_servers='kafka:40800', acks='all')

    while True:
        producer.send(topic='hello', value=b'hello world!')
        producer.flush()
        time.sleep(2)

    producer.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
