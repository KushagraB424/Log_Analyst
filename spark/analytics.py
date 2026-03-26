# spark/analytics.py

from pyspark.sql.functions import col, count, window


def compute_metrics(df):
    
    # Requests per hour
    requests_over_time = df.groupBy(
        window(col("timestamp"), "1 hour")
    ).count().orderBy("window")

    # Top endpoints
    top_endpoints = df.groupBy("endpoint") \
        .count() \
        .orderBy(col("count").desc()) \
        .limit(10)

    # Status distribution
    status_counts = df.groupBy("status") \
        .count()

    # Error rate
    total = df.count()
    errors = df.filter(col("status") >= 400).count()

    error_rate = errors / total if total > 0 else 0

    return {
        "requests_over_time": requests_over_time,
        "top_endpoints": top_endpoints,
        "status_counts": status_counts,
        "error_rate": error_rate
    }