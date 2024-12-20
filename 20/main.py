from collections import deque
from pathlib import Path

from collections import deque

def calc_all_distances(start, grid):
    queue = deque([start])
    distances = {start: 0}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if grid[ny][nx] != "#" and (nx, ny) not in distances:
                    distances[(nx, ny)] = distances[(x, y)] + 1
                    queue.append((nx, ny))
    return distances

def do_main(debug_mode=False):
    with open(Path('20/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('20/test.txt')) as file:
            lines = [line.rstrip() for line in file]
            
    track = [list(line) for line in lines]

    start_pos, end_pos = None, None
    for y, cy in enumerate(track):
        for x, cx in enumerate(cy):
            if cx == "S":
                start_pos = (x, y)
            if cx == "E":
                end_pos = (x, y)

    distances = calc_all_distances(start_pos, track)

    point_sum1 = 0
    point_sum2 = 0
    
    positions = list(distances.keys())
    cheats = []
    cheats2 = []
    
    for i, pos1 in enumerate(positions):
        for pos2 in positions[i+1:]:
            distance_pos1_pos2 = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
            
            possible_saving = distances[pos2] - distances[pos1] - distance_pos1_pos2
            if distance_pos1_pos2 == 2 and possible_saving > 0:
                cheats.append(possible_saving)
                
            if distance_pos1_pos2 < 21 and possible_saving> 0:
                cheats2.append(possible_saving)
    cheats.sort()
    cheats2.sort()

    point_sum1 = len([c for c in cheats if c >= 100])
    point_sum2 = len([c for c in cheats2 if c >= 100])

    print(point_sum1)
    print(point_sum2)

if __name__ == '__main__':
    do_main(False)