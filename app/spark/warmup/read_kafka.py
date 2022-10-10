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

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
from pyspark.streaming import StreamingContext


def main():
    spark = SparkSession \
        .builder \
        .appName('ReadKafka') \
        .getOrCreate()

    lines = spark \
        .readStream \
        .format('kafka') \
        .option('auto.offset.reset', 'earliest') \
        .option('max.poll.records', 100) \
        .option('kafka.bootstrap.servers', 'kafka:40800') \
        .option('kafka.group.id	', 'warmup-read-kafkas') \
        .option('subscribe', 'hello') \
        .load() \
        .selectExpr('CAST(value AS STRING)')
    # .option('kafka.cluster', '') \
    # .option('kafka.group.id', '')  \
    # .option('kafka.topic', 'hello') \

    words = lines.select(explode(split(lines.value, ' ')).alias('word'))

    query = words  \
        .groupBy(words.word)  \
        .count()  \
        .writeStream  \
        .format('console')  \
        .trigger(processingTime='10 seconds')  \
        .outputMode('update')  \
        .option('checkpointLocation', '${hdfs checkpoint location}')  \
        .start()
    query.awaitTermination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
