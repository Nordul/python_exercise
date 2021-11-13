year = input('输入要判断的年份：')
year = int(year)
if year%4==0 or year%400==0:
    print(f"{year}是闰年\n")
    exit(0)
else:
    print(f"{year}不是闰年\n")
    exit(0)