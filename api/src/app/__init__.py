from flask import Flask
from config import Config
from src.routes import movies_bp
from src.routes.redis import redis_bp
from src.app.module import AppModule
from injector import Injector
from flask_injector import FlaskInjector


def create_config() -> Config:
    return Config()


def create_app(name: str) -> Flask:
    app = Flask(name)

    app.config.from_object(create_config())
    app.url_map.strict_slashes = False

    app.register_blueprint(redis_bp, url_prefix='/redis')
    app.register_blueprint(movies_bp, url_prefix="/movies")

    with app.app_context():
        injector = Injector([AppModule(app)])

    FlaskInjector(app=app, injector=injector)

    return app
