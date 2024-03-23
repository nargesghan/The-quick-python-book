dic={}

for i in range(3):
    name=input('name: ')
    phone=input('phone: ')
    dic[name]=phone


user=input('Enter one of names:')

print(f'{user}\'s phone is: {dic[user]}')