import csv

# 1. split, strip (rstrip, lstrip)
with open('lunch.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))

# 2. csv.reader
with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)