import os
from math import floor
input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

def solve():
    print(f'Solving AoC Day 1: https://adventofcode.com/2019/day/1')

    data = [int(module) for module in open(input_path, 'r').read().split('\n')]

    result = 0

    for index, module in enumerate(data):
        print(f'Generating fuel requirement for: module no.{index}')
        result = result + get_fuel(module)
    print("Result: ", result)

def get_fuel(module):
    res = 0
    fuel = module
    while fuel > 0:
        fuel = ((floor(fuel/3)) - 2)
        if fuel > 0:
            res += fuel

    return res
