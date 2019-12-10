import os
import sys
from multiprocessing import Pool, Manager

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")

def solve():

    pool = Pool(20)

    print("Generating map")
    map = [[x, y] for x in range(0, 100) for y in range(0, 100)]

    print("RUNNING")
    pool.map(run_intcode, map)



def run_intcode(params):

    x, y = params
    
    data =  [int(module) for module in open(input_path, 'r').read().split(',')]
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
            if(data[0] == 19_690_720):
                info(f'X: {x}')
                info(f'Y`: {y}')
                info(100 * x  + y)
                sys.exit()
            else:
                break

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

