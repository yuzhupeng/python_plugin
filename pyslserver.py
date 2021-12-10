import pymssql 

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