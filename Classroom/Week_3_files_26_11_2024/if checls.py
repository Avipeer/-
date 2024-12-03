num = int(input("Enter a number between 1-10:"))

x9 = num * 9
num1 = x9 % 10#ahadot
num2 = x9 % 100 // 10#asarot
num3 = x9 // 100#hunderds
#131
#num3 = 1
sum1 = num1 * int( 1 - num3/(num3 + 1)) + num2 + num3

print(" 1.",x9 ,"\n 2.",sum1 ,"\n 3.",sum1)