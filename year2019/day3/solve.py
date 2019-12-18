""" 2019 Day 3 Solver"""

import os
from typing import List, NewType

import matplotlib.pyplot as plt
import numpy as np

Step = NewType('Step', str)
INPUT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


def solve():
    """ Solve https://adventofcode.com/2019/day/3"""

    print(f'Solving AoC Day 3: https://adventofcode.com/2019/day/3')

    print("Generating paths")
    paths = [path for path in open(INPUT_PATH, 'r').read().split('\n')]
    c_paths = []
    for i in range(len(paths)):
        c_paths.append([Step(step) for step in paths[i].split(',')])

    print("Generating grid")
    grid = np.zeros((11_000, 11_000), dtype=int)

    print(f'Solving {len(c_paths)} paths')
    for i in range(len(c_paths)):
        print(f'Solving path {i}')
        solve_path(grid, c_paths[i])

    print('Finding smallest manhattan distance (this might take a while)')
    grid[int(len(grid) /2) - 100:int(len(grid/2)) + 100, int(len(grid) /2) - 100:int(len(grid/2)) + 100] = 102019
    plt.pcolormesh(grid)
    plt.show()

    print(f'Result: {find_smallest_manhatten_distance(grid)}')



def find_smallest_manhatten_distance(grid: np.ndarray) -> int:
    smallest_manhattan_distance = 0
    start_x, start_y = (int(len(grid) / 2), int(len(grid) / 2))

    intersections = []
    for ix, iy in np.ndindex(grid.shape):
        # print(f'Smallest distance: {smallest_manhattan_distance}')

        if grid[ix, iy] > 1:
            intersections.append((ix, iy))
            d_x = start_x - ix
            d_y = start_y - iy

            manhattan_distance = abs(d_x + d_y)

            if smallest_manhattan_distance == 0:
                smallest_manhattan_distance = manhattan_distance
                print(f'SMDIST: {smallest_manhattan_distance}')
            elif manhattan_distance < smallest_manhattan_distance:
                smallest_manhattan_distance = manhattan_distance
                print(f'SMDIST: {smallest_manhattan_distance}')

    return smallest_manhattan_distance

def readable_direction(direction):
    if direction == 'U':
        return "UP"

    elif direction == 'D':
        return "DOWN"

    elif direction == 'L':
        return "LEFT"

    elif direction == 'R':
        return "RIGHT"
    else:
        return "SOMEWAY"


def solve_path(grid: List, path: List[Step]):
    """Solve a path and update the grid"""
    current_xy = (int(len(grid) / 2), int(len(grid) / 2))
    for step in path:

        x, y = current_xy
        direction = step[0]
        distance = int(step[1:4])
        print(f'Traveling {distance} steps {readable_direction(direction)} from (x = {x}, y = {y})', end='\r')

        if direction == 'U':
            grid[x, y + 1:y + distance] = [cell + 1 for cell in grid[x, y + 1:y + distance]]

            current_xy = (x, y + distance)

        elif direction == 'D':
            grid[x, y - distance:y - 1] = [cell + 1 for cell in grid[x, y - distance:y - 1]]

            current_xy = (x, y - distance)

        elif direction == 'L':
            grid[x - distance:x - 1, y] = [cell + 1 for cell in grid[x - distance:x - 1, y]]

            current_xy = (x - distance, y)

        elif direction == 'R':
            grid[x + 1:x + distance, y] = [cell + 1 for cell in grid[x + 1:x + distance, y]]
            current_xy = (x + distance, y)
    return
