#!/usr/bin/python
#-*-coding:utf-8-*-

#黑洞数又称陷阱数，是类具有奇特转换特性的整数。任何一个数字不全相同的整数，经有限“重排求差”操作，总会得到某一个或一些数，这些数即为黑洞数。“重排求差”操作即把组成该数的数字重排后得到的最大数减去重排后得到的最小数。
#举个例子，3位数的黑洞数为495.
#简易推导过程：随便找个数，如297,3个位上的数从小到大和从大到小各排一次，为972和279，相减得693。按上面做法再做一次，得到594，再做一次，得到495，之后反复都得到495。

#验证4位数的黑洞数为6174。

def main(n):
	if len(str(n)) == 4:
		m=[i for i in str(n)]
		m.sort()
		x=int(m[3])*1000+int(m[2])*100+int(m[1])*10+int(m[0])
		y=int(m[0])*1000+int(m[1])*100+int(m[2])*10+int(m[3])
		return x-y
lit=[]
n=int(input("请输入一个互不相同的四位数:"))
while True:
	n=main(n)
	if n not in lit:
		lit.append(n)
	else:
		print n
		break
