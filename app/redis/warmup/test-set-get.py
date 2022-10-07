#!/usr/bin/env python3

import redis


def main():
    r = redis.Redis(host='redis', port=6379, db=0)
    assert r.set('hello', 'world')
    assert r.get('hello') == b'world'
    print(f'get: ' + str(r.get('hello')))


if __name__ == '__main__':
    main()
