import csv
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


def train_model():
    df = pd.read_csv("logs/query_logs.csv")
    feature_cols = [
        "length", "num_joins", "num_where", "num_and", "has_group_by",
        "has_order_by", "has_limit", "has_avg", "has_sum", "has_count", "num_tables_hint"
    ]
    target = "execution_time_ms"

    X = df[feature_cols]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=120, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, preds))
    print("R2:", r2_score(y_test, preds))

    joblib.dump(model, "ml/model.pkl")
    print("Model saved to ml/model.pkl")


if __name__ == "__main__":
    train_model()