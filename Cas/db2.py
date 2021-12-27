from logging import log
import pymssql
import log4


class DB:
    log = None

    def __init__(self):
        server = "."  # 连接服务器地址
        user = "sa"  # 连接帐号
        password = "1"  # 连接密码
        self.conn = pymssql.connect(server, user, password, "Skc_Business")
        self.cur = self.conn.cursor()
        log = log4.get_logger()

    def __del__(self):  # 析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        resList = self.cur.fetchall()
        self.conn.close()
        return resList

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))
            log.error('执行sql时发送错误！', e)

    # def check_user(self,name):
    #     result = self.query("select * from user where name='{}'".format(name))
    #     return True if result else False

    # def del_user(self, name):
    #     self.exec("delete from user where name='{}'".format(name))

    def insert_CasTravel(self, travelobject):

        for item in travelobject:
            self.exec("INSERT INTO persons VALUES (%d, %s, %s)",
                      [(1, 'John Smith', 'John Doe'),
                       (2, 'Jane Doe', 'Joe Dog'), (3, 'Mike T.', 'Sarah H.')])

     #更新单号
    def update_CasTravel(self, applynolist):
        print(applynolist)

        #根据单号查询
    def fecth_applyno(self, applyno):

        cursor = self.cursor()  # 获取光标
        # 查询数据
        cursor.execute('SELECT count(*) FROM CasTravel WHERE BwfTravelNo=%s',
                       applyno)
        # 遍历数据（存放到元组中） 方式1
        row = cursor.fetchone()
        if len(row) > 1:
            self.close()
            return True
        else:
            self.close()
            return False


# from db2 import DB:

# db = DB()  # 实例化一个数据库操作对象
# if db.check_user("张三"):
#     db.del_user("张三")