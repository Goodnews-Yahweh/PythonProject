#!/bin/python3

items = ['A', 'B', 'C', 'D', 'E']

for item in items:
    if item == 'B':
        items.remove('B')
    else:
        print(item)
