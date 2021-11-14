x = input('输入第一个数字')
x = int(x)
y = input('输入第二个数字')
y = int(y)
n = input('输入运算符,1为加，2为减，3为乘，4为除:\n')
n = int(n)

if n == 1:
    print(x+y)
elif n == 2:
    print(x-y)
elif n == 3:
    print(x*y)
elif n == 4:
    print(x/y)
elif n != 1 or n != 2 or n != 3 or n != 4:
    print('运算符输入有误')
