from collections import deque
import copy
from pathlib import Path

import numpy as np
import tqdm


def find_connected_boxes(grid, start_index,only_down):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    connected_boxes = []
    dirs = []
    if only_down:
        dirs = [(0, 1), (0, -1), (1, 0)]
    else:
        dirs = [(0, 1), (0, -1), (-1, 0)]

    x, y = start_index
    if grid[x][y] in ['[', ']'] and not visited[x][y]:
        queue = deque([(x, y)])
        visited[x][y] = True
        boxes = [(y,x)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    if grid[nx][ny] in ['[', ']']:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        boxes.append((ny,nx))

        connected_boxes.extend(boxes)

    return connected_boxes


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
            line = line.replace("#", "##")
            line = line.replace(".", "..")
            line = line.replace("@", "@.")
            line = line.replace("O", "[]")
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
    current_position = list(list(zip(*np.where(room == "@")))[0])
    current_position.reverse()
    for i, movement in tqdm.tqdm(enumerate(movements)):
        if i ==201:
            a = 0
        #print(i)
        new_pos = [current_position[0]+movement[0],current_position[1]+movement[1]]
        if room[new_pos[1]][new_pos[0]] == '#':
            continue
        elif room[new_pos[1]][new_pos[0]] == '.':
            room[new_pos[1]][new_pos[0]] = "@"
            room[current_position[1]][current_position[0]] = "."
            current_position = new_pos
        elif room[new_pos[1]][new_pos[0]] in ['[',']'] and movement in [[1,0],[-1,0]]:
            box_pos = copy.deepcopy(new_pos)
            box_pos_orig = copy.deepcopy(new_pos)
            do_nothing = False
            while True:
                next_box =  [box_pos[0]+movement[0],box_pos[1]+movement[1]]
                if room[next_box[1]][next_box[0]] in ['[',']']:
                    box_pos = next_box
                elif room[next_box[1]][next_box[0]] == ".":
                    room[box_pos_orig[1]][box_pos_orig[0]] = "."
                    s =  movement == [1,0]
                    for i in range(abs(box_pos_orig[0]-next_box[0])):
                        box_pos_orig[0] += movement[0]
                        if s:
                            s = False
                            room[box_pos_orig[1]][box_pos_orig[0]] = "["
                        else:
                            s= True
                            room[box_pos_orig[1]][box_pos_orig[0]] = "]"
                    break
                elif room[next_box[1]][next_box[0]] == "#":
                    do_nothing = True
                    break
            if not do_nothing:
                room[new_pos[1]][new_pos[0]] = "@"
                room[current_position[1]][current_position[0]] = "."
                current_position = new_pos
        elif room[new_pos[1]][new_pos[0]] in ['[',']'] and movement in [[0,1],[0,-1]]:
            only_down = movement == [0,1]
            bs = []
            if room[new_pos[1]][new_pos[0]] == "[":
                pos2 = [new_pos[0]+1,new_pos[1]]
            else:
                pos2 = [new_pos[0]-1,new_pos[1]]
            if room[new_pos[1]+movement[1],new_pos[0]] in ['[',']']:
                bs = find_connected_boxes(room, (new_pos[1]+movement[1],new_pos[0]), only_down)
            elif room[pos2[1]+movement[1]][pos2[0]] in ['[',']']:
                bs = find_connected_boxes(room, (pos2[1]+movement[1],pos2[0]), only_down)
            bs.append((new_pos[0], new_pos[1]))
            bs.append((pos2[0], pos2[1]))
            bs_re = []
            bs_re.append((new_pos[0], new_pos[1]))
            bs_re.append((pos2[0], pos2[1]))
            for box in bs:
                bq = (box[0],box[1]-movement[1])
                if room[box[1]][box[0]] == "[":
                    bq2 = (box[0]+1,box[1]-movement[1])
                else:
                    bq2 = (box[0]-1,box[1]-movement[1])
                if bq in bs_re or bq2 in bs_re:
                    bs_re.append(box)
            do_nothing = False
            next_bs = []
            for box in bs_re:
                next_bs.append([box[0], box[1]+movement[1], room[box[1]][box[0]]])
            for box in next_bs:
                if room[box[1]][box[0]] == "#":
                    do_nothing = True
                    break
            if not do_nothing:
                for box in bs_re:
                    room[box[1]][box[0]] = "."
                for box in next_bs:
                    room[box[1]][box[0]] = box[2]
                room[new_pos[1]][new_pos[0]] = "@"
                room[current_position[1]][current_position[0]] = "."
                current_position = new_pos    

    box_positions = list(zip(*np.where(room == "[")))
    for pos in box_positions:
        point_sum += (100* pos[0] + pos[1])
        
    print(point_sum)
    


if __name__ == '__main__':
    do_main(False)