#!/usr/bin/env python3
from random import randint
import csv
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))

K1 = 100

team = {}

with open(os.path.join(fileDir, 'data/team.txt'), 'r') as a:
	s = a.read().split()
	for row in s:
		team[row] = []

zjurating = open('rating.csv', 'w')
	
for i in range(1, 100):
	try:
		ftext = open(os.path.join(fileDir, 'data/contest' + str(i) + '.txt'), 'r').read().split('\n')
		for key in team:
			team[key].append('-')
		cnt_team = int(ftext[0])
		cnt_prob_top, _, __ = map(int, ftext[1].split()[1:])
		for row in ftext[2:]:
			lst = row.split()
			nm = lst[0]
			cnt_p, rk, pen = map(int, lst[1:])
			rt = K1 * 1.0 * cnt_p / cnt_prob_top * (2 * cnt_team - 2) / (cnt_team + rk - 2)
			if nm in team:
				team[nm][-1] = rt
	except:
		print("QAQ :: " + str(i))
		break
	
final_standing = []
for x in team:
	f = list(filter(lambda x : x != '-', team[x]))
	f.sort()
	ans = 0
	if len(f) == 0:
		ans = 0
	else:
		m = len(f)
		m -= m // 4
		ans = sum(f[-m:]) / m
	final_standing.append([-ans, x])
	
final_standing.sort()

zjuhtml = open("rating.html", "w")
temp1 = open(os.path.join(fileDir, "html/template.1"), "r").read()
zjuhtml.write(temp1)

cnt_contest = 0
if (len(final_standing) != 0):
	x = final_standing[0]
	cnt_contest = len(team[x[1]])

dli_th = """</th><th class="stnd">"""
dli_td = """</td><td class="stnd">"""
zjuhtml.write('<tr><th class="stnd">' + (dli_th.join(['Place', 'Name'] + list(map(lambda x : "Contest " + str(x), range(1, cnt_contest + 1))) + ['Rating'])) + '</th><tr>\n')
	
for (pac, x) in enumerate(final_standing):
	print(-x[0], x[1], team[x[1]])
	zjurating.write(str(-x[0]) + ', ' + x[1] + ', ' + ', '.join(map(str, team[x[1]])) + '\n')
	sss = ['-' if y == '-' else ("%.3f" % y) for y in team[x[1]]]
	COL = ""
	for i in range(6):
		COL += hex(randint(0, 15))[2:]
	zjuhtml.write('<tr><td class="stnd">' + (dli_td.join([str(pac+1), "<font color=" + COL + ">" + x[1] + "</font>"] + sss + ["%.10f" % (-x[0])])) + '</td></tr>\n')

temp2 = open(os.path.join(fileDir, "html/template.2"), "r").read()
zjuhtml.write(temp2)
zjurating.close()
zjuhtml.close()
