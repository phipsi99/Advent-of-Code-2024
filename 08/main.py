import copy
from pathlib import Path
import re

def calc_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def do_main(debug_mode=False):
    with open(Path('08/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('08/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0


    for line_index, line in enumerate(lines):
        lines[line_index] = list(line)
    o_lines = copy.deepcopy(lines)

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if re.match(r'[a-zA-Z0-9]', char):
                for line_index2, line2 in enumerate(lines):
                    for char_index2, char2 in enumerate(line2):
                        if line_index != line_index2 and char_index != char_index2 and char == char2:
                            x_dif = char_index2 - char_index
                            y_dif = line_index2 - line_index
                            a1_index_x = char_index - x_dif
                            a1_index_y = line_index - y_dif
                            a2_index_x = char_index2 + x_dif
                            a2_index_y = line_index2 + y_dif
                            if a1_index_x >= 0 and a1_index_y >= 0 and a1_index_x  < len(lines[0]) and a1_index_y < len(lines):
                                o_lines[a1_index_y][a1_index_x] = '#'
                            if a2_index_x >= 0 and a2_index_y >= 0 and a2_index_x  < len(lines[0]) and a2_index_y < len(lines):
                                o_lines[a2_index_y][a2_index_x] = '#'

    for line in o_lines:
        for  c in line:
            if c == '#':
                point_sum += 1
    
    print(o_lines)
    print(point_sum)

    #PArt2

    point_sum = 0
    for line_index, line in enumerate(lines):
        lines[line_index] = list(line)
    o_lines = copy.deepcopy(lines)

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if re.match(r'[a-zA-Z0-9]', char):
                for line_index2, line2 in enumerate(lines):
                    for char_index2, char2 in enumerate(line2):
                        if line_index != line_index2 and char_index != char_index2 and char == char2:
                            x_dif = char_index2 - char_index
                            y_dif = line_index2 - line_index
                            a1_index_x  = char_index 
                            a1_index_y = line_index
                            while a1_index_x >= 0 and a1_index_y >= 0 and a1_index_x  < len(lines[0]) and a1_index_y < len(lines):
                                o_lines[a1_index_y][a1_index_x] = '#'
                                a1_index_x -= x_dif
                                a1_index_y -= y_dif
                            a1_index_x  = char_index 
                            a1_index_y = line_index
                            while a1_index_x >= 0 and a1_index_y >= 0 and a1_index_x  < len(lines[0]) and a1_index_y < len(lines):
                                o_lines[a1_index_y][a1_index_x] = '#'
                                a1_index_x += x_dif
                                a1_index_y += y_dif

    for line in o_lines:
        for  c in line:
            if c == '#':
                point_sum += 1
    
    print(o_lines)
    print(point_sum)


if __name__ == '__main__':
    do_main(False)