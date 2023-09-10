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
    '''returns total cost (num_shares * share_price) of portfolio'''     
    cost = 0
    f = open(filename)
    rows = csv.reader(f)
    header = next(rows)
    for index, line in enumerate(rows, start=1): 
        position = dict(zip(header, line))
        print(position)
        try: 
            cost += int(position["shares"]) * float(position["price"]) #num_shares * share_price
        except ValueError: 
            print(f"row {index} : couldn't convert: {line}")
    f.close()
    return cost 


filename = 'Data/portfolio.csv'
if len(sys.argv) == 2: 
    filename = sys.argv[1]

cost = portfolio_cost(filename)
print("cost: ", cost)