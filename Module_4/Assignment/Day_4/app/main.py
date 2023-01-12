from flask import Flask, render_template, request

import config
import persistence


app = Flask(__name__)
app.debug = config.DEBUG


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        persistence.add_todo_item(content)

    return render_template("index.html", todo_items=persistence.list_todo_items())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
