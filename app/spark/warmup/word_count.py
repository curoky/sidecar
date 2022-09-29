#!/usr/bin/env python3
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

import sys
import logging
from operator import add
import pyspark


def main():
    sc = pyspark.SparkContext()

    logging.info('sys.argv[1] = %s' % sys.argv[1])
    lines = sc.textFile(sys.argv[1])

    result = lines.flatMap(lambda line:  line.split(' ')) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(add)

    result.saveAsHadoopFile('/LICENSE.txt.count-result.txt',
                            outputFormatClass='org.apache.hadoop.mapred.TextOutputFormat')

    for key, value in result.collect():
        logging.info('%s %i' % (key, value))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
