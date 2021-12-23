import pandas as pd





a=float(111.22222222,6)


dates=range(20161010,20161114)
pieces=[]
for date in dates:
    try:
        data=pd.read_csv('A_stock/overview-push-%d/stock overview.csv' %date, encoding='gbk')
        pieces.append(data)
    except BaseException as e:
        print(e)
         
     
data=pd.concat(pieces)











def deleteDup(li,key):
    seen = set()
    new_list = []
    for d in li:
#指定键值
        d1=d['a']
        if d1 not in seen:
            new_list.append(d)
            seen.add(d1)
    return new_list
 
if __name__=='__main__':
    l = [{'a': 123, 'b': 1234},
         {'a': 3222, 'b': 1234},
         {'a': 123, 'b': 1234}]
    deleteDup(l)







b=[[], ] 
a = [{'name':'lilei','age':'18'},{'name':'tom','age':'16'},{'name':'lilei','age':'18'}]
c=b+a
# print(list(c))

from functools import reduce

a = [{'name':'lilei','age':'18','c':'18'},{'name':'tom','age':'16'},{'name':'lilei','age':'18','s':'18'}]




run_function = lambda x, y: x if y in x else x + [y]
uniqueList = reduce(run_function, [[], ] + a)

print(list(uniqueList))

print('1')