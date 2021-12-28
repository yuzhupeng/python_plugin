class DefaultConfig(object):
    """
    默认配置
    """
    # production development testing
    # 环境配置
    ENV = 'development'
    DEBUG = True

    # 数据库配置
    HOST = 'localhost'
    PORT = '3306'
    DATABASE = 'xhx_study'
    USERNAME = 'root'
    PASSWORD = '940628'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(username=USERNAME, password=PASSWORD,
                                                                               host=HOST, port=PORT, db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
