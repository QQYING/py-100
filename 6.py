#!/usr/bin/python
#-*-coding:utf-8-*-

#所谓勾股数，一般是指能够构成直角三角形3条边的3个正整数（a,b,c)。
#即a²+b²=c²，a，b，cΣN
#求1000以内的勾股数。

def main(i):
	n=i**2
	return n

for a in range(1,1000):
	x=main(a)
	for b in range(a,1000):
		y=main(b)
		#①
		z=x+y
		import math
		c=int(math.sqrt(z))
		if c**2 == z and c <= 1000:
			print a,b,c
		#②
		#z=x+y
		#c=int(z**0.5)
		#if c**2 == z and c <= 1000:
		#	print a,b,c
		#③
		#for c in range(b,1000):
		#	z=main(c)
		#	if x+y == z:
		#		print a,b,c
