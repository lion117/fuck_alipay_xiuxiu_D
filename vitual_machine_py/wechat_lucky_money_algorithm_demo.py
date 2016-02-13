# -*- coding: utf-8 -*-
"""
@author: Administrator
Date:  16-2-14
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

#coding=gbk
import random
import sys
#print random.randint(0, 99)
#print "====", random.uniform(0, 0.99)

def calRandomValue(min, max, total, num):
	print min, max, total, num
	total = float(total)
	num = int(num)
	min = 0.01
	if(num < 1):
		return
	if num == 1:
		print u"第%d个人拿到红包数为：%.2f" %(num, total)
		return

	i = 1
	total_money = total
	#rtotal = (total*100 - min*num*100)/100
	while( i < num ):
		max = total_money - min*(num- i)
		k = int((num-i)/2)
		if num -i <= 2:
			k = num -i
		max = max/k
		monney = random.randint(int(min*100), int(max*100))
		monney = float(monney)/100
		total_money = total_money - monney
		print u"第%d个人拿到红包数为：%.2f, 余额为: %.2f" %(i, monney, total_money)
		i += 1

	print u"第%d个人拿到红包数为：%.2f, 余额为: %.2f" %(i, total_money, 0.0)
if __name__ == "__main__":
	# min = sys.argv[1]
	# max = sys.argv[2]
	# total = sys.argv[3]
	# num = sys.argv[4]
	# calRandomValue(min, max, total, num)
    calRandomValue(0.01 , 50 ,150,100)