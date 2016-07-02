#!/usr/bin/python
#-*-coding:utf-8-*-

#如果某个数的平方的末尾几位等于这个数，那么就称这个数为自守数。显然，5和6是一位自守数（5*5=25，6*6=36)。 25*25=625,76*76=5776，所以25和76是两位自守数。
#求10000以内的自守数。

#for i in range(1,10000):
#	k=i**2
#	n=str(i)
#	x=len(n)
#	m=str(k)
#	y=len(m)
#	z=y-x
#	if int(m[z:]) == i:
#		print i,k

for i in range(1,10000):
	x=len(str(i))
	y=i*i%(10**x)
	if y == i:
		print i,i*i
