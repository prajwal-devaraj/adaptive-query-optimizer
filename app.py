from flask import Flask, render_template, request, jsonify
from database.workload_queries import QUERIES
from ml.feature_extractor import feature_vector
from services.executor_service import execute_query
from services.logging_service import init_log_file, log_query
from services.optimizer_service import choose_strategy
from ml.predict import predict_runtime
import os
import pandas as pd

app = Flask(__name__)
init_log_file()


@app.route("/")
def home():
    return render_template("index.html", queries=QUERIES)


@app.route("/run", methods=["POST"])
def run_query():
    query = request.form.get("query", "").strip()
    if not query:
        return render_template("results.html", error="Please enter a SQL query.")

    vector, features = feature_vector(query)
    strategy_info = choose_strategy(query)
    predicted = predict_runtime(query)
    predicted_time = round(predicted[0], 3) if predicted else None

    rows, actual_time = execute_query(query)
    log_query(query, features, actual_time)

    preview_rows = rows[:10] if rows else []

    return render_template(
        "results.html",
        query=query,
        features=features,
        predicted_time=predicted_time,
        actual_time=actual_time,
        strategy=strategy_info["strategy"],
        reason=strategy_info["reason"],
        rows=preview_rows,
        row_count=len(rows)
    )


@app.route("/dashboard")
def dashboard():
    if not os.path.exists("logs/query_logs.csv"):
        return render_template("dashboard.html", stats={})

    df = pd.read_csv("logs/query_logs.csv")
    stats = {
        "total_queries": int(len(df)),
        "avg_latency": round(float(df["execution_time_ms"].mean()), 3) if len(df) else 0,
        "max_latency": round(float(df["execution_time_ms"].max()), 3) if len(df) else 0,
        "min_latency": round(float(df["execution_time_ms"].min()), 3) if len(df) else 0,
        "slow_queries": df.sort_values("execution_time_ms", ascending=False).head(5).to_dict(orient="records")
    }
    return render_template("dashboard.html", stats=stats)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)