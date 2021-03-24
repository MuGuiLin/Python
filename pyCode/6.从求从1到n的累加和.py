# 求从求从1到n的累加和sum=1+2+……+n

sum = 0

num = eval(input('请输入一个整数：'))

for i in range(1, num + 1):
    sum = sum + i

print(sum)