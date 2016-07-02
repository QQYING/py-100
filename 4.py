#!/usr/bin/python
#-*-coding:utf-8-*-

#220的真因数之和为1+2+4+5+10+11+20+22+44+55+110=284
#$284的真因数之和为1+2+4+71+142=220
#毕达哥拉斯把这样的数对A、B称为相亲数：A的真因数之和为B，而B的真因数之和为A。

#求100000以内的相亲数

def main(i):
	lit=[]
	n=i/2
	for a in range(1,n+1):
		b=i/a
		if i%a == 0 and b >= a:
			lit.append(a)
			if b > a and b != i:
				lit.append(b)
		elif a > b:
			break
	m=0
	for v in lit:
		m=m+v
	return m

for i in range(100000):
	x=main(i)
	if x > i and x <= 100000:
		y=main(x)
		if y == i:
			print i,x
