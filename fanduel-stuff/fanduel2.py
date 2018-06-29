# Fanduel lineup generator
import sys
import pandas as pd
from pandas import ExcelWriter
import itertools, csv
from itertools import chain
from operator import methodcaller
from collections import defaultdict
import operator


# Widen shell display
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Read and print csv
df = pd.read_csv("projections.csv")
print("Today's Slate")
print(df)

# Add column for needed value, differential, and % differential
df["Needed Value"] = (df["Salary"] / 1000) * float(sys.argv[1])
df["Needed Floor Value"] = (df["Salary"]/1000) * float(sys.argv[2])
df["Differential"] = df["Projected Value"] - df["Needed Value"]
df["% Differential"] = (df["Projected Value"]/df["Needed Value"])*100
print()

# Get best value players
print("Potential Players")
df2 = df[(df["Projected Value"] >= df["Needed Value"]) & (df["Floor Value"] > df["Needed Floor Value"])]
print(df2)

print()

# Sort value players by position
print("Potential players by position:")
print()

print("Point Guards")
pg = df2.loc[df["Position"] == "PG"].sort_values(by = ["% Differential"], ascending = False)
print(pg)
print()
# print(pg.describe())

print("Shooting Guards")
sg = df2.loc[df["Position"] == "SG"].sort_values(by = ["% Differential"], ascending = False)
print(sg)
print()
# print(sg.describe())

print("Small Forwards")
sf = df2.loc[df["Position"] == "SF"].sort_values(by = ["% Differential"], ascending = False)
print(sf)
print()
# print(sf.describe())

print("Power Forwards")
pf = df2.loc[df["Position"] == "PF"].sort_values(by = ["% Differential"], ascending = False)
print(pf)
print()
# print(pf.describe())

print("Centers")
c = df2.loc[df["Position"] == "C"].sort_values(by = ["% Differential"], ascending = False)
print(c)





"""
print("Final Lineup")
# Grabbing 2 PG, 2 SG, 2 SF, 2 PF, 1 C
finalpg = pg.head(2)
finalsg = sg.head(2)
finalsf = sf.head(2)
finalpf = pf.head(2)
finalc = c.head(1)

frames = [finalpg, finalsg, finalsf, finalpf, finalc]
final = pd.concat(frames)
print(final)
print("Salary :", final["Salary"].sum())
print("Expected Scoring:", final["Projected Value"].sum())
"""
print()


def combinations():
    #PG
    pgdict = pg.set_index("Name")["Salary"].to_dict()
    pglist = list(map(dict, itertools.combinations(pgdict.items(), 2)))

    print("PG Combinations: ")
    for combos in pglist:
        print(combos)

    print()

    # SG
    sgdict = sg.set_index("Name")["Salary"].to_dict()
    sglist = list(map(dict, itertools.combinations(sgdict.items(), 2)))

    print("SG Combinations: ")
    for combos in sglist:
        print(combos)

    print()

    # SF
    sfdict = sf.set_index("Name")["Salary"].to_dict()
    sflist = list(map(dict, itertools.combinations(sfdict.items(), 2)))

    print("SF Combinations: ")
    for combos in sflist:
        print(combos)

    print()

    # PF
    pfdict = pf.set_index("Name")["Salary"].to_dict()
    pflist = list(map(dict, itertools.combinations(pfdict.items(), 2)))

    print("PF Combinations: ")
    for combos in pflist:
        print(combos)

    print()

    # C
    cdict = c.set_index("Name")["Salary"].to_dict()
    c.set_index("Name")["Projected Value"].to_dict()
    clist = list(map(dict, itertools.combinations(cdict.items(), 1)))

    print("C Combinations: ")
    for combos in clist:
        print(combos)

    print()





    # Combinations
    print("Lineup Combinations")

    lineups = list(itertools.product(pglist,sglist,sflist,pflist,clist))  # all lineup combinations as a tuple

    lu_count = 0
    players = []
    salaries = []
    p_values = []

    player_count = defaultdict(int)

    for i in lineups:
        b = {k:v for t in i for k,v in t.items()} # converts lineups var (tuple of dicts) to dictionary
        #print(b)
        values_sum = sum(v for v in b.values() if v > 0)

        if 59700 <= values_sum <= 60000: # if all values in dictionary <= 60,000: print
            print(b)
            print("Salary:", values_sum)
            lu_count += 1

            for i in range (0,9):
                player_count[list(b.keys())[i]] += 1 # this number adds 1 to the player counts values for each time a player appears


            players.append(list(b.keys()))

            salary_list = list(b.values())
            summy = sum(salary_list)
            salaries.append(summy)
        else:
            continue

    final_df = pd.DataFrame(players,columns = ["PG","PG","SG","SG","SF","SF","PF","PF","C"])
    s = pd.Series(salaries)
    final_df["Salary"] = s.values
    final_df_by_salary = final_df.sort_values(by = ["Salary"], ascending = False)
    # final_df_by_salary = final_df_by_salary.head(150)
    print()
    print(final_df_by_salary)
    final_df_by_salary.to_csv("Final_Lineups.csv",index = False)
    print("Eligible lineups:", lu_count)
    #print("Player Counts: ", dict(player_count))
    player_count = {k: round((v / lu_count * 100),2) for k, v in player_count.items()}
    player_count = sorted(player_count.items(), key=operator.itemgetter(1), reverse = True)
    print("Player Percentages: ", dict(player_count))



combinations()
