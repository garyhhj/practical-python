# report.py
#
# Exercise 2.4

import csv 
import sys
from pprint import pprint 

def read_portfolio(filename : str) -> list: 
    '''return a list of dictionary (name, num_shares, share_price) with portfolio info'''
    portfolio = []
    with open(filename, 'rt') as f: 
        rows = csv.reader(f)
        header = next(rows)
        for line in rows: 
            position = dict(zip(header, line))
            try: 
                portfolio.append({"name": position["name"], "shares":int(position["shares"]), "price":float(position["price"])})
            except ValueError: 
                print("can not parse line: ", line)
    return portfolio

def read_price(filename : str) -> dict: 
    '''return a dict of "stock_name": prices (string: float)'''
    prices = {}
    with open(filename, 'rt') as f: 
        rows = csv.reader(f)
        for line in rows: 
            try: 
                prices[str(line[0])] = float(line[1])
            except: 
                #print("can not parse line: ", line)
                pass
    return prices

def current_value(portfolio: list, prices: dict) -> float: 
    '''takes in a portfolio (list with tuples(name, num_shares, price)) with 
       a dictionary of prices returns current value of portfolio '''
    value = 0
    for position in portfolio: 
        try: 
            value += position["shares"] * prices[position["name"]]
        except: 
            print("can not evalute value of position: ", position)
    return value 

def gain(portfolio: list, prices: dict) -> float: 
    '''returns portfolio returns 
       positive number if portfolio made money, negative otherwise'''
    gain = 0
    for position in portfolio: 
        try: 
            gain += (prices[position["name"]] - position["price"]) * position["shares"] 
        except:
            print("can not evalute gain of position: ", position)
    return gain 

def make_report(portfolio: list, prices: dict) -> list: 
    '''takes in 
        portfolio - list of dict with keys "name", "shares", "price" 
        prices - dict with keys "price"
        and returns list of tuples(Name, Shares, price, change)
    '''
    report = []
    for position in portfolio: 
        report.append((position["name"], position["shares"],
                        prices[position["name"]], prices[position["name"]] - position["price"]))
    return report 

def pretty_print(report: list) -> None: 
    '''
    prints in a nice looking format 
    
    example: 
      ticker     shares      price       gain
    -------- ---------- ---------- ----------
         AA        100      $9.22     -22.98
        IBM         50    $106.28      15.18
        CAT        150     $35.46     -47.98
    '''
    #header 
    header = ("ticker", "shares", "price", "gain")
    print(f'{header[0]:>8s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')

    #separator 
    print(('-' * 8 + " ") + ('-' * 10 + " ") * 3) 
    for position in report: 
        print(f'{position[0]:>8s} {position[1]:>10d} {"$" + str(round(position[2], 2)):>10s} {position[3]:>10.2f}')

filename = 'Data/portfolio.csv'
if len(sys.argv) == 2: 
    filename = sys.argv[1]

portfolio = read_portfolio(filename)
prices = read_price('Data/prices.csv')
print("current value: ", current_value(portfolio, prices))
print("gain: ", gain(portfolio, prices))

report = make_report(portfolio, prices)
pprint(report)
pretty_print(report)
