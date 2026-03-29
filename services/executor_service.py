import time
from database.db import get_connection


def execute_query(query: str):
    conn = get_connection()
    cur = conn.cursor()

    start = time.perf_counter()
    cur.execute(query)
    rows = []
    try:
        rows = cur.fetchall()
    except Exception:
        rows = []
    end = time.perf_counter()

    cur.close()
    conn.close()

    execution_time_ms = round((end - start) * 1000, 3)
    return rows, execution_time_ms