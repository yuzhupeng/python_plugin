
import pandas as pd
 
d1 = {'Name': ['Pankaj', 'Lisa'], 'ID': [1, 2]}
 
df = pd.DataFrame.from_dict(d1)
 
print(df)
 
 

dicts = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print (f"dict['Name']:{dicts['Name']}")
print (f"dict['Age']: {dicts['Age']}") 

print('22222222222222222')

aaa=dict(aw='1')
bbb={'key':1}
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(aaa)
print(bbb)
print(dict)

lists=['1','21','34','123','45']
list=[1,2,3,4,5,6]
print(max(list))
print(max(lists))
list.append('111')
lists.append('111')
print(lists)
print(list)




print('处理可变参数-----------')

def kebian(*agrs):
    total=0
    for item in agrs:
        if type(item) in(int,float):
           total+=item 
        
    print(total)
    



kebian(1,2,2,3,4,5,6,'111','2')


#from module1 import play

 
 
import module1
module1.play(1,2,3,4)

from module2 import plays
plays(1,2,3,4,5,5)


import module1 as m1
m1.play(12,12,12,12,12)


# import sc.log4 

import sc.log4 as log4
log = log4.get_logger()
log.debug('I am a debug message')
log.info('I am a info message')
log.warning('I am a warning message')
log.error('I am a error message')
log.critical('I am a critical message')