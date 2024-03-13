from flask import Flask
from log_config import get_logger

app = Flask(__name__)
app.logger = get_logger()
app.config.from_object('config.Config')
app.app_context().push()

from register import register
app.register_blueprint(register)


@app.route("/healthCheck", methods=["GET"])
def health_check():
    app.logger.info("Workiing")
    app.logger.info(f"Secret: {app.config['SECRET']}")
    return {"message": "app is working"}




