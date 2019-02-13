#!/usr/bin/env python3
from random import randint
import csv
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
	
nico = []

for i in range(1, 100):
	try:
		ftext = open(os.path.join(fileDir, 'data/rating' + str(i) + '.csv'), 'r').read().split('\n')
		contest = {}
		while ftext[-1] == "":
			ftext = ftext[:-1]
		for row in ftext:
			name, rating = row.split(',')
			rating = float(rating)
			contest[name] = rating
		nico.append(contest)
	except:
		print("QAQ :: " + str(i))
		break

team = {}
for contest in nico:
	for name in contest:
		team[name] = []

for name in team:
	rating = []
	for contest in nico:
		if name in contest:
			rating.append(contest[name])
		else:
			rating.append(-1)
	team[name] = rating

rating = open(os.path.join(fileDir, 'data/rating_merge.csv'), 'w')
for name in team:
	rating.write(name + "," + ','.join(map(str,team[name])) + "\n")
rating.close()