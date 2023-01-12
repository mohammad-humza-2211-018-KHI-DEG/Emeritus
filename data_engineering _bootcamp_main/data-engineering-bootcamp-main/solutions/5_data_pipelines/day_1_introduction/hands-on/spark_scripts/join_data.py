import sys
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.config("Airflow Example - join data").getOrCreate()


def join_data(data_path: str) -> None:
    links_df = sparkSession.read.csv(f"{data_path}/links.csv", header=True)
    movies_df = sparkSession.read.csv(f"{data_path}/movies.csv", header=True)
    ratings_df = sparkSession.read.csv(f"{data_path}/ratings.csv", header=True)
    wanted_ids = [i for i in range(1, 11)]
    joined_df = (
        movies_df.join(ratings_df.filter(ratings_df.userId.isin(wanted_ids)), "movieId")
        .join(links_df, "movieId")
        .drop("movieId", "tmdbId")
        .select("imdbId", "title", "genres", "userId", "rating", "date_time")
    )
    joined_df.show()
    joined_df.write.option("header", True).csv(
        f"{data_path}/joined_df.csv", mode="overwrite"
    )


def main():
    data_path = sys.argv[1]
    join_data(data_path)


if __name__ == "__main__":
    main()
