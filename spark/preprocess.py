from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, col, to_timestamp

def create_spark_session():
    return SparkSession.builder \
        .appName("LogAnalytics") \
        .master("local[*]") \
        .config("spark.driver.memory", "2g") \
        .config("spark.executor.memory", "2g") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .getOrCreate()


def parse_logs(spark, log_path):
    df = spark.read.text(log_path)

    log_pattern = r'(\S+) - - \[(.*?)\] "(\S+) (\S+) .*?" (\d{3}) (\S+)'

    parsed_df = df.select(
        regexp_extract('value', log_pattern, 1).alias('ip'),
        regexp_extract('value', log_pattern, 2).alias('timestamp'),
        regexp_extract('value', log_pattern, 3).alias('method'),
        regexp_extract('value', log_pattern, 4).alias('endpoint'),
        regexp_extract('value', log_pattern, 5).cast('int').alias('status'),
        regexp_extract('value', log_pattern, 6).alias('bytes')
    )

    parsed_df = parsed_df.withColumn(
        "bytes",
        col("bytes").cast("int")
    )
    parsed_df = parsed_df.withColumn(
        "timestamp",
        to_timestamp(col("timestamp"), "dd/MMM/yyyy:HH:mm:ss Z")
    )

    return parsed_df.dropna()