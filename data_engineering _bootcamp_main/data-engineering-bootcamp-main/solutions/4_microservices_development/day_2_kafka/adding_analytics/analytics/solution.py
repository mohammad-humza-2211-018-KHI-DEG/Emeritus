import os
import sys
import json

from kafka import KafkaConsumer

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]


def main():
    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_SERVER,
        value_deserializer=lambda v: json.loads(v.decode("ascii")),
        max_poll_records=10,
        auto_offset_reset="earliest",
        session_timeout_ms=6000,
        heartbeat_interval_ms=3000,
    )
    consumer.subscribe(topics=[TOPIC_NAME])

    article_statistics = {}
    for message in consumer:
        if message.value["article_id"] not in article_statistics:
            article_statistics[message.value["article_id"]] = 0

        article_statistics[message.value["article_id"]] += 1

        print("=========")
        for article in sorted(list(article_statistics.keys())):
            print(f"Article {article}: {article_statistics[article]} view(s)")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
