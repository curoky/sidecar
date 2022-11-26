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
from concurrent.futures import ThreadPoolExecutor

from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic


def main():
    admin_client = KafkaAdminClient(bootstrap_servers='kafka:40800', client_id='test')

    builtin_topics = ['builtin-value.str-interval.2s']
    exists_topics = admin_client.list_topics()
    for name in builtin_topics:
        if name not in exists_topics:
            admin_client.create_topics(
                new_topics=[NewTopic(name=name, num_partitions=5, replication_factor=1)],
                validate_only=False)
            logging.info('created topic: %s', name)

    executor = ThreadPoolExecutor(10)
    res = []

    def start_producer_1():
        producer = KafkaProducer(bootstrap_servers='kafka:40800', acks='all')

        for i in range(100000):
            producer.send(topic=builtin_topics[0], value=f'hahaha-{i}'.encode())
            producer.flush()
            time.sleep(2)

        producer.close()

    res.append(executor.submit(start_producer_1))

    def start_cusumer_1():
        consumer = KafkaConsumer(bootstrap_servers='kafka:40800',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000,
                                 group_id='builtin-' + builtin_topics[0])
        consumer.subscribe([builtin_topics[0]])
        for i in range(100000):
            message = consumer.poll(2000)
            if message and i % 30 == 0:
                logging.info('%s: receive %s', builtin_topics[0], message)
        consumer.close()

    res.append(executor.submit(start_cusumer_1))

    for r in res:
        r.result()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
