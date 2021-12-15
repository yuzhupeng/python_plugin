from typing import cast
import pymssql 
import sc.log4 
import json
import time
import uuid
log = sc.log4.get_logger()

class HandCost(object):
    """
    处理数据库中的数据
    """

    def __init__(self, host, user, passwd, dbname, port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = port
        self.charset = charset

    def db_conn(self):
        """
        创建连接
        :return:
        """
        try:
            # 创建连接
            conn = pymssql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.dbname,
                                   charset=self.charset)
            # 创建游标
            cursor = conn.cursor(cursor=pymssql.cursors.DictCursor)
        except BaseException as e:
            print(e)
            return False
        return (conn, cursor)

    def db_close(self, conn, cursor):
        """
        关闭连接
        :param conn:
        :param cursor:
        :return:
        """
        conn.close()
        cursor.close()

    def exeQuery(self, cursor, sql):
        """
        查询
        :param cursor:
        :param sql:
        :return:
        """
        cursor.execute(sql)
        return cursor
        
        #根据单号查询
    def fecth_applyno(applyno):
        server = "."    # 连接服务器地址
        user = "sa" # 连接帐号
        password = "1"# 连接密码
        conn = pymssql.connect(server, user, password, "Skc_Business")  #获取连接
        cursor = conn.cursor() # 获取光标
        # 查询数据
        cursor.execute('SELECT count(*) FROM CasTravel WHERE BwfTravelNo=%s', applyno)
        # 遍历数据（存放到元组中） 方式1
        row = cursor.fetchone()
        if len(row)>1:
            conn.close()
            return True
        else:
            conn.close()
            return False
        
    #新增单号       
    def insert_CasTravel(travelobject):
        server = "."    # 连接服务器地址
        user = "sa" # 连接帐号
        password = "1"# 连接密码
        conn = pymssql.connect(server, user, password, "Skc_Business")  #获取连接
        cursor = conn.cursor() # 获取光标
        for item in travelobject:
            cursor.executemany(
            "INSERT INTO persons VALUES (%d, %s, %s)",
            [(1, 'John Smith', 'John Doe'),
            (2, 'Jane Doe', 'Joe Dog'),
            (3, 'Mike T.', 'Sarah H.')])
    # 你必须调用 commit() 来保持你数据的提交如果你没有将自动提交设置为true
            conn.commit()
    #更新单号
    def update_CasTravel(applynolist):
        print(applynolist)
    
    def dictToTO(travelobject):
        insertsqllist=[]
        try:
            print("create insertsql")
            detiallist=travelobject['TravelDetial']
            if len(detiallist)>0 and len(detiallist)==1:
                castravel=[]
                castraveldid=uuid.uuid1()
                castravel.append(castraveldid)
                castravel.append(travelobject['applyno']+detiallist['usedate'])
                castravel.append(travelobject['applyno'])
                castravel.append('待派车')
                castravel.append(travelobject['applytpye'])
                castravel.append(travelobject['bwfstatus'])
                castravel.append(1)
                castravel.append(travelobject['AcutalUser'])
                castravel.append(travelobject['InSideLine'])
                castravel.append(detiallist['FlightNo'])
                castravel.append(detiallist['OstartTime'])
                castravel.append(detiallist['ReturnTime'])
                castravel.append(detiallist['FlightTime'])
                castravel.append(travelobject['reason'])
                castravel.append(detiallist['usedate'])
                castravel.append('公司车')
                castravel.append(travelobject['DetailedAddres'])
                castravel.append(travelobject['Company'])
                castravel.append(travelobject['CostDepartment'])
                castravel.append(travelobject['ShareCore'])
                castravel.append('system')
                castravel.append((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                castravel.append((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                castravel.append('system')
                castravel.append(1)
                castravel.append(travelobject['PhonePassenger'])
                castravel.append(travelobject['applyperson'])
                castravel.append(travelobject['applydate'])
                castravel.append('')#合并代码
                castravel.append('')#审批信息
                castravel.append('')#司机model关联ID
                castravel.append('')#车辆model关联id
                castravel.append(0)#路桥费
                castravel.append(0)#公里数
                castravel.append(0)#行程总用时
                castravel.append(0)#类型：多日期行程的类型
                castravel.append('')#父id
                excutesql=f'insert into CasTravel values {castravel}'
                
                CasTravelDetial=[]
      
                
                
                for item in range(0,6):
                    if len(detiallist['travel'+item])>0:
                       CasTravelDetials=[]
                       CasTravelDetials.append(uuid.uuid1())
                       CasTravelDetials.append(castraveldid)
                       
                       excutedetialsql=f'insert into CasTravel values{CasTravelDetials}'
                       print('')
                
                
                # print(excutesql)
                      
      
      
      
      
        except BaseException as e:
         log.error(f"将派车单号{travelobject['applyno']}转化为sql出错：Unexpected Error: {e}")
           
 
def baidupaiPorcess(travelobject):
    detiallist=travelobject['TravelDetial']
   
    