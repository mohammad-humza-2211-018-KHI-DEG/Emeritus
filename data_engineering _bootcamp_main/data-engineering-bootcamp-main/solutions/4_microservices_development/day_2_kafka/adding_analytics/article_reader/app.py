import json
import os
from flask import Flask, render_template
from kafka import KafkaProducer

app = Flask(__name__, template_folder="templates")

producer = KafkaProducer(
    bootstrap_servers=os.environ["KAFKA_SERVER"],
    acks=1,
    value_serializer=lambda v: json.dumps(v, default=str).encode("ascii"),
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/article/<int:article_id>")
def article(article_id: int):
    producer.send(os.environ["TOPIC_NAME"], value={"article_id": article_id})
    producer.flush()

    return render_template("article.html", article_id=article_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
