#!/usr/bin/python
#-*-coding:utf-8-*-

#水仙花数是指一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。
#例如：1^3+5^3+3^3=153。

#求100~999之间所有的水仙花数。
m=0
for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			i=a*100+b*10+c
			n=a**3+b**3+c**3
			if i == n:
				print i
				m+=1
print 'count:',m
