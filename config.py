from redis import StrictRedis


class Config(object):
    """工程配置信息"""
    DEBUG = True
    SECRET_KEY = "dJqqez8m5tiC7lgKJSeN6K2ysgx3Yt0M3LZtAGM2MhJLxqohjc4zzQ=="
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/flipboard"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # 配置session
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 84600


class DevelopConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_dict = {
    'develop': DevelopConfig,
    'production': ProductionConfig
}