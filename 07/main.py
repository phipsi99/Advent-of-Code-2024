import itertools
from pathlib import Path

import tqdm

def solve(res, vals, op_combo):
    result = vals[0]
    for i in range(len(op_combo)):
        if op_combo[i] == '+':
            result += vals[i + 1]
        elif op_combo[i] == '*':
            result *= vals[i + 1]
        elif op_combo[i] == '||':
            t = str(result)
            t += str(vals[i + 1])
            result = int(t)
    return result == res

def do_main(debug_mode=False):
    with open(Path('07/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('07/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    operators = ['+', '*']

    for line in tqdm.tqdm(lines):
        res = int(line.split(":")[0].strip())
        vals = [int(i) for i in line.split(" ")[1:]]
        for op_combo in itertools.product(operators, repeat=len(vals) - 1):
            if solve(res, vals, op_combo):
                point_sum += res
                break
    
    print(point_sum)

    point_sum = 0
    operators = ['+', '*', '||']

    for line in tqdm.tqdm(lines):
        res = int(line.split(":")[0].strip())
        vals = [int(i) for i in line.split(" ")[1:]]
        for op_combo in itertools.product(operators, repeat=len(vals) - 1):
            if solve(res, vals, op_combo):
                point_sum += res
                break
    
    print(point_sum)

if __name__ == '__main__':
    do_main(False)