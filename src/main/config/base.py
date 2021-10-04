import os

HOST_DB = os.getenv("HOST_DB")
USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
DATABASE = os.getenv("DATABASE")
DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}/{DATABASE}"


class Config:
    DEBUG = True


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)
