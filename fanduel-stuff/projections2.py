import csv, sys
import urllib2
import itertools
from itertools import chain
from operator import methodcaller

data = []

fieldnames = ['Name', 'Position', 'Salary', 'Projected Value', 'Floor Value', 'Team']
names = []
salary = []
pos = []
exp_val = []
floor_val = []
#team = []
#team = ['SAC','ORL','BKN','OKC','CLE','SAS','BOS','LAL','NYK','GSW']
#https://rotogrinders.com/projected-stats/nba-player.csv?site=draftkings'
url = 'https://rotogrinders.com/projected-stats/nba-player.csv?site=fanduel'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    # if(row[2] in team):
    names.append(row[0])
    salary.append(row[1])
    # team.append(row[2])
    exp_val.append(row[7])
    floor_val.append(row[6])
    pos.append(row[3])



# print(names)
# print(salary)
# print(exp_val)
# print(pos)

path = "projections.csv"

f = open(path, 'wb')
out = csv.writer(f, delimiter=",")
out.writerow(fieldnames)
for row in zip(names, pos, salary, exp_val, floor_val):
    out.writerow(row)

f.close()
# print(csv.__file__)
