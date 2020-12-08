import os

CONFIG_ENV = os.getenv("CONFIG")

if CONFIG_ENV is None:
    CONFIG_ENV = "dev"


class Config:
    VERSION = "v0.1"
    HOST = "0.0.0.0"
    PORT = 8081
    DB_URL = ""


class DevConfig(Config):
    DB_URL = "sqlite:///./sql_app.db"


class TestConfig(Config):
    CONFIG_ENV = "test"
    DB_URL = "sqlite:///./sql_app.db"


config = dict(
    dev=DevConfig,
    test=TestConfig
)
