import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, mean, desc
from pyspark.sql.types import FloatType

sparkSession = SparkSession.builder.config(
    "Airflow Example - transform data"
).getOrCreate()


def transform_data(data_path: str) -> None:
    df = sparkSession.read.csv(f"{data_path}/joined_df.csv", header=True)
    df = df.withColumn("date", to_date("date_time")).drop("date_time")
    grouped_by_rating = df.groupby("rating").count().sort("rating")
    grouped_by_rating.write.option("header", True).csv(
        f"{data_path}/grouped_by_rating.csv", mode="overwrite"
    )
    mean_u1_rating = df.filter(df["userId"] == 1).select(mean("rating"))
    mean_u1_rating.write.option("header", True).csv(
        f"{data_path}/mean_u1_rating.csv", mode="overwrite"
    )
    df = df.withColumn("rating", df["rating"].cast(FloatType()))
    top_10 = df.groupby("imdbId").mean("rating").sort(desc("avg(rating)")).limit(10)
    top_10.write.option("header", True).csv(f"{data_path}/top_10.csv", mode="overwrite")
    top_10.show()


def main():
    data_path = sys.argv[1]
    transform_data(data_path)


if __name__ == "__main__":
    main()
