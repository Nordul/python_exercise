age=input('输入您的年龄：')
age=int (age)
if age<4:
    print('您可以免费进入\n')
elif age>=4 and age<18:
    print('您需要缴纳25$\n')
elif age>=18:
    print('您需要缴纳40$\n')