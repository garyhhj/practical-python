# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint 

def parse_csv(filename : str, select : list = None, types : list = None, hasHeader : bool = False, delimiter : str = ",") -> list: 
    '''
    reads file and returns list of records
    '''
    records = []
    with open(filename, "rt") as f: 
        rows = csv.reader(f, delimiter=delimiter)

        if hasHeader:
            header = next(rows)
            indices = [header.index(colname) for colname in select]
            header = [header[index] for index in indices]

        for row in rows: 
            if not row: 
                continue

            if hasHeader: 
                row = [row[index] for index in indices]
                record = {headerVal : type(rowVal) for type, headerVal, rowVal in zip(types, header, row)}
            else: 
                record = tuple(row)
            records.append(record)
    
    return records

records = parse_csv("Data/portfolio.csv", ["price"], [float])
pprint(records)