import os.path
import pathlib

'''How would you use the os module’s functions to take a path to a file called test.log and
create a new file path in the same directory for a file called test.log.old? How would you
do the same thing by using the pathlib module?'''

#using os.path
old_path=os.path.abspath('test.log')#returns the absolute path of the file or directory 
print('path:',old_path)
new_path='{}.{}'.format(old_path,'old')
print(new_path)

#using pathlib
path=pathlib.Path('test.log')
print(path)#test.log
old_path=path.resolve()#add current working directory to the bigining of path
print(old_path)
new_path=str(old_path)+'.old'
print(new_path)


'''What path would you get if you created a pathlib Path object from os .pardir? Try it
to find out.'''

test=pathlib.Path(os.pardir)
print('test ',test)
print(test.resolve())