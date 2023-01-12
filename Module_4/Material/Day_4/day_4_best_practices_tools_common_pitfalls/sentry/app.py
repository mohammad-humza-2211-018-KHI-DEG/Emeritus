import os
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://86775e23ebf44681a60bb57a64261226@o4504365950107648.ingest.sentry.io/4504365952991232",
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0,
)

app = Flask(__name__)


@app.route("/test-sentry")
def trigger_error():
    division_by_zero = str(1 / 2)
    return division_by_zero


if __name__ == "__main__":
    app.run()
