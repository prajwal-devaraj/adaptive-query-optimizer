import csv
import os
from datetime import datetime

LOG_FILE = "logs/query_logs.csv"

FIELDS = [
    "timestamp", "query", "length", "num_joins", "num_where", "num_and",
    "has_group_by", "has_order_by", "has_limit", "has_avg", "has_sum",
    "has_count", "num_tables_hint", "execution_time_ms"
]


def init_log_file():
    os.makedirs("logs", exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(FIELDS)


def log_query(query, features, execution_time_ms):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            query,
            features["length"],
            features["num_joins"],
            features["num_where"],
            features["num_and"],
            features["has_group_by"],
            features["has_order_by"],
            features["has_limit"],
            features["has_avg"],
            features["has_sum"],
            features["has_count"],
            features["num_tables_hint"],
            execution_time_ms,
        ])