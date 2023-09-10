# pcost.py
#
# Exercise 1.27
'''
file = open('Data/portfolio.csv', 'rt')
header = next(file)
cost = 0
for line in file: 
    row = line.split(',')
    cost += int(row[1]) * float(row[2])

print("cost: ", cost)
file.close()
'''
import csv 
import sys 

def portfolio_cost(filename : str) -> float:     
    cost = 0
    f = open(filename)
    rows = csv.reader(f)
    header = next(rows)
    for line in rows: 
        try: 
            cost += int(line[1]) * float(line[2]) #num_shares * share_price
        except ValueError: 
            print("can not parse line: ", line)

    f.close()
    return cost 

if len(sys.argv) == 2: 
    filename = sys.argv[1]
else: 
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("cost: ", cost)