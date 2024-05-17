# with open('test.txt','w',newline='\n') as file_object:
#    file_object.write('Hello!\nIs every thing okay?\nsee you')


# list=[]
# with open('test.txt','r',newline='\n') as file_object:
#     list=file_object.readlines()
#     print(list)


# with open('test2.txt','w') as file_object:
#     file_object.writelines(list)


# with open('test2.txt','rb')as file_object:
#     data=file_object.read()
#     print(data)

import sys

with open('test.txt','a') as file_object:
    file_object.write(sys.stdin.read())