users = ['nordul','admin','lendul','bei cheng','bai ming']
user = input('输入用户名')
if user in users:
    print(f'Welcome {user.title()}')
else:
    print('No such user')
