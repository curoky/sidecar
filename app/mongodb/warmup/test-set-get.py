#!/usr/bin/env python3

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
