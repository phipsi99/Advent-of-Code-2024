import copy
from pathlib import Path


def count_paths(grid,consider_visited):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def search_for_target(r, c, target, visited, consider_visited):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == target:
            if target == 9:
                if (r, c) not in visited:
                    if consider_visited:
                        visited.add((r, c))
                    return 1
            else:
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    count += search_for_target(nr, nc, target + 1, visited, consider_visited)
                return count
        return 0

    total_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                visited = set()
                if consider_visited:
                    count = search_for_target(r, c, 0, visited, consider_visited)
                    total_count += len(visited)
                else:
                    count = search_for_target(r, c, 0, set(), consider_visited)
                    total_count += count
    return total_count

def do_main(debug_mode=False):
    with open(Path('10/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    if debug_mode:
        with open(Path('10/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    for line_index, line in enumerate(lines):
        lines[line_index] = [int(i) for i in line]
    o_lines = copy.deepcopy( lines)

    print(count_paths(o_lines, consider_visited= True))
    print(count_paths(o_lines, consider_visited= False))

if __name__ == '__main__':
    do_main(False)