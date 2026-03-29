from ml.predict import predict_runtime


def choose_strategy(query: str):
    result = predict_runtime(query)
    if result is None:
        return {
            "predicted_time_ms": None,
            "strategy": "static-default",
            "reason": "Model not trained yet"
        }

    predicted_time_ms, _ = result

    if predicted_time_ms > 300:
        strategy = "adaptive-review"
        reason = "Predicted as high-latency query; mark for adaptive handling"
    else:
        strategy = "fast-path"
        reason = "Predicted as low-latency query"

    return {
        "predicted_time_ms": round(predicted_time_ms, 3),
        "strategy": strategy,
        "reason": reason
    }