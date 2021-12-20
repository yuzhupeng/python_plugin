import pymssql #引入pymssql模块 链接SQL server数据库


class SQLHelp(object):
    """数据库链接操作类"""
    def __init__(self, host, user, password, database, charset="UTF-8", port=1433, as_dict=True):
         '''
         实例化
         host:链接
         user：用户名
         password：密码
         database：数据库名
         charset：链接编码格式，默认"UTF-8"
         port： 数据库链接端口，默认1433
         as_dict：数据返回是否为字典，默认True
         '''
         self.__conn_path={
               'host':host,
               'user':user,
               'password':password,
               'database':database,
            }
  
    def update_data(self,Sql ,arge=''):
        """类方法
            sql:字符串sql单条更新语句
            return：插入影响行数
            arge:多数据，list()----->[(1, 'John Smith', 'John Doe')]
                 单条数据，元组
            error:-1
            eg：
            单数据：
                sql="INSERT INTO persons VALUES(1, 'John Smith', 'John Doe')"
            多数据：
                sql="INSERT INTO persons VALUES (%d, %s, %s)",
                arge=[(1, 'John Smith', 'John Doe'),
                 (2, 'Jane Doe', 'Joe Dog'),
                 (3, 'Mike T.', 'Sarah H.')]
        """
        try:
            with pymssql.connect(**self.__conn_path) as conn:# with语句与连接和游标一起使用。这使您不必显式关闭游标和连接。
                with conn.cursor(as_dict=True) as cursor:
                    if isinstance(arge,list):
                        cursor.executemany(Sql,arge)
                    else:
                        cursor.execute(Sql,arge)
                    effectRow = cursor.rowcount
                    conn.commit()
            return effectRow
        except Exception as ex:
            print("---------->更新操作error:",ex)
            return -1
        
    def update_datalist(self,Sql ,arge=''):
        """类方法
            sql:字符串sql单条更新语句
            return：插入影响行数
            arge:多数据，list()----->[(1, 'John Smith', 'John Doe')]
                 单条数据，元组
            error:-1
            eg：
            单数据：
                sql="INSERT INTO persons VALUES(1, 'John Smith', 'John Doe')"
            多数据：
                sql="INSERT INTO persons VALUES (%d, %s, %s)",
                arge=[(1, 'John Smith', 'John Doe'),
                 (2, 'Jane Doe', 'Joe Dog'),
                 (3, 'Mike T.', 'Sarah H.')]
        """
        try:
            with pymssql.connect(**self.__conn_path) as conn:# with语句与连接和游标一起使用。这使您不必显式关闭游标和连接。
                with conn.cursor(as_dict=True) as cursor:
                    
                    for item in Sql:
                        cursor.execute(item)
                     
                    effectRow = cursor.rowcount
                    conn.commit()
            return effectRow
        except Exception as ex:
            print("---------->更新操作error:",ex)
            return -1
   
    def get_data(self,Sql,arge=tuple()):
        """
        类方法
            sql:字符串sql查询语句
            return：数据list列表,无数据返回空列表
            arge:元组参数
            error:None
        """
        try:
            if not isinstance(arge,tuple):
                raise Exception("type类型错误,异常")
            with pymssql.connect(**self.__conn_path) as conn:# with语句与连接和游标一起使用。这使您不必显式关闭游标和连接。
                with conn.cursor() as cursor:
                    print(arge[:-1])
                    cursor.execute(Sql,arge)
                    return cursor.fetchall()
        except BaseException as ex:
            print("------------>查询操作error：",ex)
            return None
        
    class SqlClass(object):
        """复杂sql数据存储类"""
        def __init__(self, sql, arge):
            '''sql:sql
               arge:所需参数
                        插入为列表list[]
                        其他为元组()
            '''
            self.sql = sql
            self.arge = arge


    def transaction_sql(self, sql):
        '''
        数据库复杂sql操作，提供事务
        sql:sql操作语句类(SqlClass)列表
        return:影响行数
        error：-1
        使用方式
            sqlhelp=SQLHelp("localhost","sa","123",'GuiYang_UniversityTown_New')
            lists = list()
            lists.append(sqlhelps.SqlClass('delete from T_Model where code=%s','5201612032090000000165'))
            n = sqlhelps.transaction_sql(lists)
        '''
        try:
            if not isinstance(sql,list):
                raise Exception("参数type类型错误,异常")
            else:
                n = 0#默认0，失败
            with pymssql.connect(**self.__conn_path) as conn:
                with conn.cursor() as cursor:
                    for x in sql:
                        if isinstance(x.arge,list):
                            cursor.executemany(x.sql,x.arge)
                        else:
                            cursor.execute(x.sql,x.arge)
                        n+=cursor.rowcount
                    if n:
                        conn.commit()
            return n
        except BaseException as ex:
            print("------------>操作error:",ex)
            return -1

    def transaction_sqlist(self, sql):
        '''
        数据库复杂sql操作，提供事务
        sql:sql操作语句类(SqlClass)列表
        return:影响行数
        error：-1
        使用方式
            sqlhelp=SQLHelp("localhost","sa","123",'GuiYang_UniversityTown_New')
            lists = list()
            lists.append(sqlhelps.SqlClass('delete from T_Model where code=%s','5201612032090000000165'))
            n = sqlhelps.transaction_sql(lists)
        '''
        try:
            if not isinstance(sql,list):
                raise Exception("参数type类型错误,异常")
            else:
                n = 0#默认0，失败
            with pymssql.connect(**self.__conn_path) as conn:
                with conn.cursor() as cursor:
                    for x in sql:
                        if isinstance(x,list):
                            for item in x:
                                cursor.execute(item)
                        else:
                            cursor.execute(x)
                        n+=cursor.rowcount
                    if n:
                        conn.commit()
            return n
        except BaseException as ex:
            print("------------>操作error:",ex)
            return -1




if __name__ == '__main__':
    sqlhelps = SQLHelp("localhost","sa","1",'GuiYang_UniversityTown_New')
    lists = list()
    lists.append(sqlhelps.SqlClass(r"INSERT INTO [dbo].[T_Model]( [Code],[VillageCode], [Lon], [Lat], [3DMLName], [VillageName]) VALUES ( %s, %s,%s, %s, %s, %s);",
                                                              [( '5201412032090000000165', None,106.579311, 26.414393, '3DML_DT\G48H077147B_DT', None),
                                                               ( '5201612032090000000165', None,106.579311, 26.414393,'3DML_DT\G48H077147B_DT', None)]))
    lists.append(sqlhelps.SqlClass('delete from T_Model where code=%s and VillageCode=%s',('5201612032090000000165',None)))
    n = sqlhelps.transaction_sql(lists)
    print("复杂事务sql测试---------\n",n)
