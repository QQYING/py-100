#!/usr/bin/python
#-*-coding:utf-8-*-

#完全数（Perfect number)，又称完美数或完备数，是一些特殊的自然数。它所有的真因子(即除了自身以外的约数）的和（即因子函数），恰好等于它本身。例如，第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

#编程求10000以内的完全数
#思路一
#for i in range(1000):
#	lit=[]
#	for a in range(i+1):
#		for b in range(i+1):
#			if a*b == i and a <= b and a != i:
#				lit.append(a)
#				if b != i:
#					lit.append(b)
#	m=0
#	for n in lit:
#		m=m+n
#	if m == i and i != 0:
#		print i

#思路二
for i in range(1,10000):
	lit=[]
	n=i/2
	for a in range(1,n+1):
		if i%a == 0:
			b=i/a
			if a <= b:
				lit.append(a)
				if b != i and a != b:
					lit.append(b)
	m=0
	for n in lit:
		m=m+n
	if m == i:
		print i
