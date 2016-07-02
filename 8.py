#!/usr/bin/python
#-*-coding:utf-8-*-

#所谓反序数，即有这样成对的数，其特点是其中一个数的数字排列顺序完全颠倒过来，就变成另一个数，如102和201，36和63等，简单的理解就是顺序相反的两个数，我们把这种成对的数互称为反序数。反序数唯一不可能出现以0结尾的数。
#
#一个3位数各位上的数字都不相同，它和它的反序数的乘积是280021，这个3位数应是多少？

for a in range(1,10):
	for b in range(0,10):
		for c in range(a,10):
			x=a*100+b*10+c
			y=a+b*10+c*100
			if x*y ==280021 and a < c :
				print x,y
