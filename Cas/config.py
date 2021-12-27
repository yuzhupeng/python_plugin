 
import configparser
import os

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            root_dir =os.path.dirname(os.path.abspath("__file__"))# 当前目录
            configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_db(self, param):
        value = self.cf.get("Mysql-Database", param)
        return value
    def get_other(self, param):
        value = self.cf.get("other", param)
        return value

if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_db("host")
    print(t)
 
 