

value_titleS=[["申请单号","实际使用者","用车日期","行程","详细地址"]]

newlist3=[" "]
f3 = open("html.txt","r",encoding='utf-8')  
original_list3 = f3.readlines()       #读取全部内容 ，并以列表方式返回 
for i in original_list3:          #遍历去重
  if not i in newlist3:
      newlist3.append(i)
newtxt3="".join(newlist3)
 
 
for item in newlist3:
    sts="".join(item)
    sss=len(sts.strip())
    if sss>0 and sss!=15:
       str_to_dict = eval(sts)
       applyno=str_to_dict['applyno']
       AcutalUser=str_to_dict['AcutalUser']
       usedate=str_to_dict['TravelDetial'][0]['usedate']
       travel=str_to_dict['TravelDetial'][0]['travel']
       DetailedAddress=str_to_dict['DetailedAddress']
       op=[]
       op.append(applyno)
       op.append(AcutalUser)
       op.append(usedate)
       op.append(travel)
       op.append(DetailedAddress)
       value_titleS.append(op)


 
 
import xlwt
 
def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数(value是个二维数组)
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")
 
# 保存到当前工程目录
book_name_xls = 'test2.xls'
 
sheet_name_xls = 'xls格式测试表'
 
value_title = [["姓名", "性别", "年龄", "城市", "职业"],
          ["111", "女", "66", "石家庄", "运维工程师"],
          ["222", "男", "55", "南京", "饭店老板"],
          ["333", "女", "27", "苏州", "保安"]]
 
write_excel_xls(book_name_xls, sheet_name_xls, value_titleS)