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
    
    #将DTO转化为sql
    def dictToTO(self,travelobject):
        insertsqllist=[]
        try:
            print("create insertsql")
            detiallist=travelobject['TravelDetial']
            if len(detiallist)>0 and len(detiallist)==1:
                castravel=[]
                uid = str(uuid.uuid4())
                suid = ''.join(uid.split('-'))
                castraveldid=(suid)
                castravel.append(castraveldid)#DID
                castravel.append((travelobject['applyno'])+'-'+(detiallist[0]['usedate']))#派车单号
                castravel.append(travelobject['applyno'])# bwf管理序号
                castravel.append(1)# 1 待派车 状态
                castravel.append(travelobject['applytype'])#申请状态类型
                castravel.append(travelobject['bwfstatus'])#bwf状态
                castravel.append(travelobject['Peoples'])#人数
                castravel.append(travelobject['AcutalUser'])#实际使用者
                castravel.append(travelobject['InSideLine'])#内线
                castravel.append(detiallist[0]['FlightNo'])#车次/航班编号
                castravel.append(detiallist[0]['OstartTime'])#出发时间
                castravel.append(detiallist[0]['ReturnTime'])#返回时间
                castravel.append(detiallist[0]['FlightTime'])# 开车/起飞到达时间
                castravel.append(travelobject['reason'])#变更取消理由
                castravel.append(detiallist[0]['usedate'])#用车日期
                castravel.append('公司车')#用车类型
                castravel.append(travelobject['userason'])#用车理由
                castravel.append(travelobject['DetailedAddres'])#行程详细地址
                castravel.append(travelobject['Company'])#公司
                castravel.append(travelobject['CostDepartment'])#经费负担部门
                castravel.append(travelobject['ShareCore'])#经费负担代码
                castravel.append('system')#CreateID
                castravel.append((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))#CreateDate
                castravel.append((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))#ModifyDate
                castravel.append('system')#ModifyID
                castravel.append(1)#Enables
                castravel.append('')#PhonePassenger
                castravel.append(travelobject['applyperson'])#申请人
                castravel.append(travelobject['applydate'])#申请日期
                castravel.append('')#合并代码
                castravel.append('')#审批信息
                castravel.append('')#司机model关联ID
                castravel.append('')#车辆model关联id
                castravel.append(0)#路桥费
                castravel.append(0)#公里数
                castravel.append('')#备注
                castravel.append(0)#行程总用时
                castravel.append(0)#类型：多日期行程的类型
                castravel.append('')#父id
                
                castravel.append(travelobject['phone1'])
                castravel.append(travelobject['passenger1'])
                castravel.append(travelobject['phone2'])
                castravel.append(travelobject['passenger2'])
                castravel.append(travelobject['phone3'])
                castravel.append(travelobject['passenger3'])
                castravel.append(travelobject['phone4'])
                castravel.append(travelobject['passenger4'])
                castravel.append(travelobject['phone5'])
                castravel.append(travelobject['passenger5'])
                
                castravel.append('')#司机姓名
                castravel.append('')#车牌
                
                
                excutesql=f'insert into CasTravel values ({castravel})'
                insertsqllist.append(excutesql)
                CasTravelDetial=[]
      
                
                
                for item in range(1,6):
                         
                    if len(detiallist[0]['travel'+item])>0:
                       start=''
                       end=''
                       if item==1:
                           start=detiallist[0]['start']
                       else:
                           start=detiallist[0][('travel'+item-1)]
                       end=detiallist[0]['travel'+item]
                       
                       CasTravelDetials=[]
                       CasTravelDetials.append(str(uuid.uuid1()))
                       CasTravelDetials.append(castraveldid)
                       CasTravelDetials.append(start)
                       CasTravelDetials.append(end)
                       CasTravelDetials.append(start)
                       CasTravelDetials.append(end)
                       CasTravelDetials.append('')#CasDestinationDID
                       CasTravelDetials.append(0)#preUseTime
                       CasTravelDetials.append('')#经度
                       CasTravelDetials.append('')#维度
                       CasTravelDetials.append('')#公里数
                       CasTravelDetials.append('')#cqf
                       CasTravelDetials.append(1)#Enables
                       CasTravelDetials.append(1)#顺序
                       
                       
                       excutedetialsql=f'insert into CasTravel values({CasTravelDetials})'
                       insertsqllist.append(excutedetialsql)
                       
                
               
                      
      
      
      
      
        except BaseException as e:
         log.error(f"将派车单号{travelobject['applyno']}转化为sql出错：Unexpected Error: {e}")
           
    def aaaa(self,abs):
        print(abs)

def baidupaiPorcess(travelobject):
    detiallist=travelobject['TravelDetial']
   
    