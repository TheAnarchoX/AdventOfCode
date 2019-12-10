import os
from math import floor
input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

def solve():
    data = [int(module) for module in open(input_path, 'r').read().split('\n')]

    result = 0

    for module in data:
        result = result + getFuel(module)

    print(result)

def getFuel(module):
    res = 0
    fuel = module
    while fuel > 0:
        fuel = ((floor(fuel/3)) - 2)
        if fuel > 0:
            res += fuel

    return res
