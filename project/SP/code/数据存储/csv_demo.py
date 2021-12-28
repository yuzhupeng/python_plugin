import csv

# with open('classroo1.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     # titles = next(reader)
#     for x in reader:
#         print(x)


headers = ['name','age','classroom']
values = [
    {"name":'wenn',"age":20,"classroom":'222'},
    {"name":'abc',"age":30,"classroom":'333'}
]
with open('test.csv','w',newline='', encoding='utf-8') as fp:
    writer = csv.DictWriter(fp,headers)
    writer.writeheader()
    # writer.writerow(headers)
    writer.writerows(values)
