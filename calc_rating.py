#!/usr/bin/env python3
from random import randint
import csv
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))

K1 = 100
	
for i in range(1, 100):
	try:
		ftext = open(os.path.join(fileDir, 'data/contest' + str(i) + '.csv'), 'r').read().split('\n')
		rating = open(os.path.join(fileDir, 'data/rating' + str(i) + '.csv'), 'w')
		while ftext[-1] == "":
			ftext = ftext[:-1]
		ftext = ftext[1:]
		cnt_team = len(ftext)
		cnt_prob_top= int(ftext[0].split(',')[1])
		rk = 0
		for row in ftext:
			lst = row.split(',')
			rk += 1
			nm = lst[0]
			cnt_p, pen = map(int, lst[1:])
			rt = K1 * 1.0 * cnt_p / cnt_prob_top * (2 * cnt_team - 2) / (cnt_team + rk - 2)
			rating.write(nm + ',' + str(rt) + '\n')
		rating.close()
	except:
		print("QAQ :: " + str(i))
		break
