import os
from dataclasses import dataclass
from typing import Any, List

import sqlite3


@dataclass
class QueryResult:
    affected_rows: int
    result: list[Any]


class DatabaseUtil:
    def __init__(self, database: os.PathLike) -> None:
        self.db_conn = sqlite3.connect(database)
        self.cursor = self.db_conn.cursor()

    def query(self, sql: str, **kwargs) -> QueryResult:
        self.cursor.execute(sql, kwargs)
        result = self.cursor.fetchall()
        return QueryResult(len(result), result)

    def query_many(self, sql: str, args: List[Any]) -> QueryResult:
        self.cursor.executemany(sql, args)
        result = self.cursor.fetchall()
        return QueryResult(len(result), result)

    def commit(self) -> None:
        self.db_conn.commit()

    def rollback(self) -> None:
        self.db_conn.rollback()

    def close(self) -> None:
        self.db_conn.close()