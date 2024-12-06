import copy
from pathlib import Path

import tqdm

def simulate_moves(lines):
    arr_size = len(lines[0]) * len(lines)
    directions = [(0,-1), (1,0),(0,1),(-1,0)]
    sel_dir = 0
    is_inf = False
    
    x = 0
    y = 0
    for line_index, line in enumerate(lines):
        for  char_index, char in enumerate(line):
            if char == '^':
                x = char_index
                y = line_index
    i = 0
    while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        i += 1
        if i >= arr_size:
            is_inf  = True
            break
        lines[y][x] = 'X'
        new_x = x + directions[sel_dir][0]
        new_y = y + directions[sel_dir][1]
        if 0 <= new_x < len(lines[0]) and new_y < len(lines):
            c = lines[new_y][new_x]
            if c == '#':
                sel_dir = (sel_dir + 1) % 4
            else:
                x = new_x
                y = new_y
        else:
            break
    return lines, is_inf

def do_main(debug_mode=False):
    with open(Path('06/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('06/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        lines[line_index] = list(line)
    o_lines = copy.deepcopy( lines)
    

    lines, _ = simulate_moves(lines)
    for line in lines:
        for  c in line:
            if c == 'X':
                point_sum += 1

    print(point_sum)

    inf_cnt = 0
    for mod_line_index, line in tqdm.tqdm(enumerate(lines),  total=len(lines)):
        for  mod_char_index, char in tqdm.tqdm( enumerate(line),  total=len(line)):
            mod_lines =  copy.deepcopy( o_lines)
            if mod_lines[mod_line_index][mod_char_index] == '#':
                continue
            mod_lines[mod_line_index][mod_char_index] = '#'

            _, is_inf = simulate_moves(mod_lines)
            if is_inf:
                inf_cnt += 1
    print(inf_cnt)


if __name__ == '__main__':
    do_main(False)