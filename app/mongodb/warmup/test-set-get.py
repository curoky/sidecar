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

from random import random

from pymongo import MongoClient


def main():
    CONNECTION_STRING = 'mongodb://root:example@mongo:27017/'

    client = MongoClient(CONNECTION_STRING)

    datebase = client['helloworld']
    collection = datebase['v1']

    item = {
        '_id': str(random()),
        'item_name': 'Blender',
        'max_discount': '10%',
        'batch_number': 'RR450020FRG',
        'price': 340,
        'category': 'kitchen appliance'
    }
    res = collection.insert_one(item)
    print(f'inserted_id={res.inserted_id}')


if __name__ == '__main__':
    main()
