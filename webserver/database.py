import os
from dataclasses import dataclass
from typing import Any, List

import sqlite3


@dataclass
class QueryResult:
    affected_rows: int
    result: list[Any]


class DatabaseUtil:
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __init__(self, database: os.PathLike | str) -> None:
        self.db_conn = sqlite3.connect(database)
        self.db_conn.row_factory = self.dict_factory
        self.cursor = self.db_conn.cursor()

    def query(self, sql: str, *args) -> QueryResult:
        self.cursor.execute(sql, args)
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