""" 2019 Day 2 Solver"""
import os
import sys
from typing import Tuple, List
from multiprocessing import Manager, Process
from multiprocessing.managers import ValueProxy

INPUT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


def solve():
    """ Solve https://adventofcode.com/2019/day/2"""
    print("Generating map")
    value_map = [(x, y) for x in range(0, 100) for y in range(0, 100)]
    data = [int(module) for module in open(INPUT_PATH, 'r').read().split(',')]

    finish = Manager().Value(bool, False)
    procs = []
    for tile in value_map:
        procs.append(Process(target=run_intcode, args=(data, tile, finish)))

    print(f'Starting {len(procs)} subprocesses')
    for proc in procs:
        if not finish.get():
            proc.start()
            proc.join()

    sys.exit()


def run_intcode(data: List[int], tile: Tuple[int, int], finish: ValueProxy):
    """ This runs intcode base on a data list a tile from the value map
        :param data
        :returns void
    """
    initial_noun, initial_verb = tile

    data[1] = initial_noun
    data[2] = initial_verb

    for i in range(0, len(data) - 1, 4):
        if finish.get():
            sys.exit()
        opcode, noun, verb, out = data[i:i + 4]

        if opcode == 1:
            data[out] = data[noun] + data[verb]
        elif opcode == 2:
            data[out] = data[noun] * data[verb]
        elif opcode == 99:
            if data[0] == 19690720:
                print(f'Result: {100 * initial_noun + initial_verb}')
                finish.set(True)
                sys.exit()
