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

from sqlalchemy import text
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Person(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    age: int


def main():
    engine = create_engine('mysql+pymysql://root:cicada@mysql:40200', echo=True)

    with engine.connect() as conn:
        conn.execute(text('CREATE DATABASE IF NOT EXISTS MockDB'))

    engine = create_engine('mysql+pymysql://root:cicada@mysql:40200/MockDB')
    SQLModel.metadata.create_all(engine)

    executor = ThreadPoolExecutor(10)
    res = []

    def start_curd_person_table():
        for i in range(10000):
            pid = int(time.time())

            with Session(engine) as session:
                session.add(Person(id=pid, name=str(pid), age=10))
                session.add(Person(id=pid + 1, name=str(pid + 1), age=20))
                session.commit()
            time.sleep(10)

            with Session(engine) as session:
                statement = select(Person).where(Person.id == pid)
                person = session.exec(statement).one()
                person.age = 11
                session.add(person)
                session.commit()

            with Session(engine) as session:
                statement = select(Person).where(Person.id == pid + 1)
                person = session.exec(statement).one()
                session.delete(person)
                session.commit()

    res.append(executor.submit(start_curd_person_table))

    for r in res:
        r.result()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
