import re


def extract_features(query: str):
    q = query.lower().strip()
    return {
        "length": len(q),
        "num_joins": q.count(" join "),
        "num_where": q.count(" where "),
        "num_and": q.count(" and "),
        "has_group_by": int("group by" in q),
        "has_order_by": int("order by" in q),
        "has_limit": int("limit" in q),
        "has_avg": int("avg(" in q),
        "has_sum": int("sum(" in q),
        "has_count": int("count(" in q),
        "num_tables_hint": len(set(re.findall(r"from\s+(\w+)|join\s+(\w+)", q)))
    }


def feature_vector(query: str):
    features = extract_features(query)
    return list(features.values()), features