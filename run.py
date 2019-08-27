from flask import Flask
from Model import db
from app import api_bp


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    app.register_blueprint(api_bp, prefix="/api/v1")
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)