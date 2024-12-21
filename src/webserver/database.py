from dataclasses import dataclass
from typing import Any, List

import pymysql


@dataclass
class QueryResult:
    affected_rows: int
    result: Any


class DatabaseUtil:
    def __init__(self, host: str, password: str) -> None:
        self.db_conn = pymysql.connect(
            host=host,
            user="",
            passwd=password,
            db=""
        )
        self.cursor = self.db_conn.cursor()

    def query(self, sql: str, **kwargs) -> QueryResult:
        affected = self.cursor.execute(sql, kwargs)
        result = self.cursor.fetchall()
        return QueryResult(affected, result)

    def query_many(self, sql: str, args: List[Any]) -> QueryResult:
        affected = self.cursor.executemany(sql, args)
        result = self.cursor.fetchall()
        return QueryResult(affected, result)

    def commit(self) -> None:
        self.db_conn.commit()

    def close(self) -> None:
        self.db_conn.close()