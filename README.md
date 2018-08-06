Zhejiang University ACM-ICPC Rating System (Version 2)
===

This is an easy rating system for Zhejiang University ACM-ICPC team.


Usage
---

1. Add teams into ```data/team.txt```
2. For each contest, make a file named ```data/contest[*].txt```, which starts from 1. In the contest file, add total number of teams in the first line. From the second line on, add data as the format ```team_name problem_passed rank penalty``` with rank number ascending. Pay attention that only the winner team and teams you concerned that matters, you don't need to add all the teams. 
3. run ```python3 rating.py``` in the terminal.