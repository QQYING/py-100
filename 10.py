#!/usr/bin/python
#-*-coding:utf-8-*-

#若两个素数之差为2，则这两个素数就是孪生素数。

#编写程序找出1~100之间的所有孪生素数。

def main(i):
	lit=[]
	for x in range(1,i+1):
		if i%x == 0:
			lit.append(x)
	if len(lit) == 2:
		return i

for i in range(1,100):
	if main(i) == i:
		if main(i+2) == i+2 and i+2 < 100:
			print i,i+2
