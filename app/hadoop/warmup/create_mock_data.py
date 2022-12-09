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
import random
import subprocess
import sys
from pathlib import Path

ANIMAL_WORDS = [
    'shark', 'dolphin', 'whale', 'tortoise', 'turtle', 'jellyfish', 'crab', 'alligator',
    'crocodile', 'lizard', 'rat', 'mouse'
]


def main():
    one_word_one_line_file = Path('/tmp/one_word_one_line')
    one_word_one_line_file.write_text('\n'.join(random.choices(ANIMAL_WORDS, k=1000)),
                                      encoding='utf8')

    multi_word_one_line_file = Path('/tmp/multi_word_one_line')
    multi_word_one_line_file.write_text('\n'.join(
        [' '.join(random.choices(ANIMAL_WORDS, k=1000)) for _ in range(1000)]),
                                        encoding='utf8')

    subprocess.run(['/opt/hadoop/bin/hadoop', 'fs', '-mkdir', '/mock-data'],
                   stdout=sys.stdout,
                   stderr=sys.stderr,
                   check=False)
    subprocess.run([
        '/opt/hadoop/bin/hadoop', 'fs', '-put',
        one_word_one_line_file.as_posix(), f'/mock-data/{one_word_one_line_file.name}'
    ],
                   stdout=sys.stdout,
                   stderr=sys.stderr,
                   check=True).check_returncode()
    subprocess.run([
        '/opt/hadoop/bin/hadoop', 'fs', '-put',
        multi_word_one_line_file.as_posix(), f'/mock-data/{multi_word_one_line_file.name}'
    ],
                   stdout=sys.stdout,
                   stderr=sys.stderr,
                   check=True).check_returncode()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
