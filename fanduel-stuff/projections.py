import csv, sys
import urllib2
import itertools
from itertools import chain
from operator import methodcaller

data = []

fieldnames = ['Name', 'Position', 'Salary', 'Projected Value', 'Team']
names = []
salary = []
pos = []
exp_val = []
team = []
#team = ['MIA','DET','WAS','ORL','PHI','IND', 'HOU', 'CLE', 'GSW', 'DEN', 'UTA', 'SAS', 'NOP', 'MIN', 'DAL', 'SAC']
#'https://rotogrinders.com/projected-stats/nba-player.csv?site=draftkings'
url = 'https://rotogrinders.com/projected-stats/nba-player.csv?site=fanduel'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
#    if(row[2] in team):
    names.append(row[0])
    salary.append(row[1])
    team.append(row[2])
    exp_val.append(row[7])
    pos.append(row[3])



# print(names)
# print(salary)
# print(exp_val)
# print(pos)

path = "projections.csv"

f = open(path, 'wb')
out = csv.writer(f, delimiter=",")
out.writerow(fieldnames)
for row in zip(names, pos, salary, exp_val, team):
    out.writerow(row)

f.close()
# print(csv.__file__)
