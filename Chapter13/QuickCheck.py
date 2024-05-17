'''What is the significance of adding a "b" to the file open mode string, as in
open("file", "wb")?'''



'''with open('test3.txt','wb')as file_object:
    file_object.write('ksfldkf\nlskdfld\n')'''
#you’re trying to write a string to a file that was opened in binary mode ('wb'). In Python, binary mode expects data to be in bytes, not as a string


# convert your string to bytes before writing:
with open('test3.txt','wb')as file_object:
    file_object.write(b'ksfldkf\nlskdfld\n')

'''Suppose that you want to open a file named myfile.txt and write additional data on
the end of it. What command would you use to open myfile.txt? What command
would you use to reopen the file to read from the beginning?'''

with open('myfile','a')as file_object:
    file_object.write('lskdf\nkdjfksl\nskfk\n')