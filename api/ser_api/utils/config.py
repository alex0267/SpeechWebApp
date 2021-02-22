import os
from pathlib import Path

CONFIG_ENV = os.getenv("CONFIG","dev")


class Config:
    VERSION = "v0.1"
    HOST = "0.0.0.0"
    PORT = 8081
    DB_URL = ""
    GOOGLE_APPLICATION_CREDENTIALS_PATH = str(Path(Path(__file__).parent.parent.parent,"credentials.json"))
    POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "test_db")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
    PROJECT_ID = "wewyse-centralesupelec-ftv"

    # default value is localhost recaptcha's site key:
    # https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha.-what-should-i-do
    RECAPTCHA_SECRET = os.getenv("RECAPTCHA_SECRET",  "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe")

    @classmethod
    def db_url_string(cls):
        return f"postgresql+psycopg2://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}@{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}"


class DevConfig(Config):
    CONFIG_ENV = "dev"
    BUCKET_NAME = "swa-dev-bucket"


class TestConfig(Config):
    CONFIG_ENV = "test"
    BUCKET_NAME = "swa-test-bucket"


class ProdConfig(Config):
    CONFIG_ENV = "prod"
    BUCKET_NAME = "swa-prod-bucket"


config = dict(dev=DevConfig, test=TestConfig, prod=ProdConfig)

EXT_TO_MIMETYPE = {
    ".ogg" : "audio/ogg",
    ".ogv": "audio/ogg",
    ".oga": "audio/ogg",
    ".ogx": "audio/ogg",
    ".ogm": "audio/ogg",
    ".spx": "audio/ogg",
    ".opus": "audio/ogg",
    ".weba":	"audio/webm",
    ".webm":	"video/webm",
    ".wav":    "audio/wav"}
