class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/base'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENCODING = "utf-8"
