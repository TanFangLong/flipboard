from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from config import config_dict, Config
from flask_session import Session
import logging
from logging.handlers import RotatingFileHandler


db = SQLAlchemy()
# decode_responses 对取出的数据解码为字符串 (取出的数据为bytes类型)
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG) # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    '''
    工厂函数, 产生app实例
    :return: 返回app对象
    '''
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])
    Session(app)
    # 初始化数据库类
    db.init_app(app)

    return app
