#!/usr/bin/pythom
#-*-coding:utf-8-*-

#0~9这10个数字可以组成多少不重复的3位数？
i=0
for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			if a != b and b != c and c != a:
			#	print a,b,c
				i+=1
print i
