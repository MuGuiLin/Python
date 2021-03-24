'''
从键盘输入一个整数，判断该整数是3N型（3的倍数），3N+1型（除以3余1），还是3N+2型（除以3余2）
'''
num = eval(input('请输入一个整数：'))

if num % 3 == 0:
    print(num, '是3的倍数！')

elif num % 3 == 1:
    print(num, '除以3余1')

else:
    print(num, '除以3余2')