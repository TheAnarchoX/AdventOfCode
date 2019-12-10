import os
import sys
from multiprocessing import Pool, Manager

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


def solve():
    pool = Pool(5)

    print("Generating map")
    map = [[x, y] for x in range(0, 1000) for y in range(0, 1000)]

    print("RUNNING")
    pool.map(run_intcode, map, 10)

    sys.exit()


def run_intcode(params):
    x, y = params

    data = [int(module) for module in open(input_path, 'r').read().split(',')]
    data[1] = x
    data[2] = y

    for i in range(0, len(data) - 1, 4):
        opcode, noun, verb, out = data[i:i + 4]

        if opcode == 1:
            try:
                data[out] = data[noun] + data[verb]
            except IndexError:
                break
        elif opcode == 2:
            try:
                data[out] = data[noun] * data[verb]
            except IndexError:
                break
        elif opcode == 99:
            if (data[0] == 19_690_720):
                info(f'X: {x}')
                info(f'Y: {y}')
                info(f'Result: {100 * x + y}')

                import signal

                os.kill(os.getppid(), signal.SIGTERM)
            else:
                break


def info(title):
    print(title)

