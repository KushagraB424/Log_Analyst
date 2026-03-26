from spark.preprocess import create_spark_session, parse_logs
from spark.analytics import compute_metrics
from spark.anomaly_detection import detect_anomalies

def main():
    spark = create_spark_session()

    log_path = "../data/raw/nasa_logs.txt"

    df = parse_logs(spark, log_path)

    # Save sample for UI
    df.limit(10000).toPandas().to_csv(
        "../data/processed/logs_sample.csv", index=False
    )

    metrics = compute_metrics(df)

    # Convert Spark DF to Pandas/JSON
    metrics["requests_over_time"].toPandas().to_json(
        "../data/processed/requests_over_time.json", orient="records"
    )

    metrics["top_endpoints"].toPandas().to_json(
        "../data/processed/top_endpoints.json", orient="records"
    )

    metrics["status_counts"].toPandas().to_json(
        "../data/processed/status_counts.json", orient="records"
    )

    # Save error rate
    with open("../data/processed/aggregated_metrics.json", "w") as f:
        import json
        json.dump({"error_rate": metrics["error_rate"]}, f)

    # Detect anomalies
    anomalies = detect_anomalies(metrics["requests_over_time"])
    anomalies.toPandas().to_json(
        "../data/processed/anomalies.json", orient="records"
    )

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    main()