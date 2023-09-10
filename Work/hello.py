

prices = {}

with open('Data/prices.csv', 'rt') as f: 
    for line in f: 
        row = line.split(',')
        if len(row) == 1: 
            continue 
        prices[row[0]] = float(row[1])

print(prices)