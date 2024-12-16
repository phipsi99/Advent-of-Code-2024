from pathlib import Path

import numpy as np

def do_main(debug_mode=False):
    with open(Path('15/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('15/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    room = []
    movements = []

    done  = False
    for line_index, line in enumerate(lines):
        if line.strip() == "":
            done = True
            continue
        if not done:
            room.append([])
            for li in line:
                room[line_index].append(li)
        else:
            for c in line:
                if c == "<":
                    movements.append([-1,0])
                elif c == ">":
                    movements.append([1,0])
                elif c == "^":
                    movements.append([0,-1])
                elif c == "v":
                    movements.append([0,1])

    room = np.array(room)
    current_position = list(zip(*np.where(room == "@")))[0]
    for movement in movements:
        new_pos = [current_position[0]+movement[0],current_position[1]+movement[1]]
        if room[new_pos[1]][new_pos[0]] == '#':
            continue
        elif room[new_pos[1]][new_pos[0]] == '.':
            room[new_pos[1]][new_pos[0]] = "@"
            room[current_position[1]][current_position[0]] = "."
            current_position = new_pos
        elif room[new_pos[1]][new_pos[0]] == 'O':
            box_pos = new_pos
            box_pos_orig = new_pos
            do_nothing = False
            while True:
                next_box =  [box_pos[0]+movement[0],box_pos[1]+movement[1]]
                if room[next_box[1]][next_box[0]] == "O":
                    box_pos = next_box
                elif room[next_box[1]][next_box[0]] == ".":
                    room[next_box[1]][next_box[0]] = "O"
                    room[box_pos_orig[1]][box_pos_orig[0]] = "."
                    break
                elif room[next_box[1]][next_box[0]] == "#":
                    do_nothing = True
                    break
            if not do_nothing:
                room[new_pos[1]][new_pos[0]] = "@"
                room[current_position[1]][current_position[0]] = "."
                current_position = new_pos


    box_positions = list(zip(*np.where(room == "O")))
    for pos in box_positions:
        point_sum += (100* pos[0] + pos[1])
        
    print(point_sum)
    


if __name__ == '__main__':
    do_main(False)