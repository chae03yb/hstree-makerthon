import os
from dataclasses import dataclass
from typing import Any, List

import sqlite3


@dataclass
class QueryResult:
    affected_rows: int
    result: list[Any]


class DatabaseUtil:
    def __init__(self, database: os.PathLike | str) -> None:
        self.__db_conn = sqlite3.connect(database)
        self.__cursor = self.__db_conn.cursor()

    def query(self, sql: str, *args) -> QueryResult:
        self.__cursor.execute(sql, args)
        result = self.__cursor.fetchall()
        return QueryResult(len(result), result)

    def query_many(self, sql: str, args: List[Any]) -> QueryResult:
        self.__cursor.executemany(sql, args)
        result = self.__cursor.fetchall()
        return QueryResult(len(result), result)

    def commit(self) -> None:
        self.__db_conn.commit()

    def rollback(self) -> None:
        self.__db_conn.rollback()

    def close(self) -> None:
        self.__db_conn.close()