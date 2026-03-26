# spark/anomaly_detection.py

from pyspark.sql.functions import mean, stddev, col


def detect_anomalies(requests_df):
    stats = requests_df.select(
        mean("count").alias("mean"),
        stddev("count").alias("std")
    ).collect()[0]

    mean_val = stats["mean"]
    std_val = stats["std"]

    threshold = mean_val + 2 * std_val

    anomalies = requests_df.filter(col("count") > threshold)

    return anomalies