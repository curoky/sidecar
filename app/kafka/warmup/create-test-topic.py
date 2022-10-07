#!/usr/bin/env python3
# Copyright (c) 2022-2022 curoky(cccuroky@gmail.com).
#
# This file is part of sidecar.
# See https://github.com/curoky/sidecar.git for further info.
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

from kafka.admin import KafkaAdminClient, NewTopic


def main():
    admin_client = KafkaAdminClient(bootstrap_servers='kafka:40800', client_id='test')

    topic_list = []
    topic_list.append(NewTopic(name='hello', num_partitions=2, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
