from collections import deque
from pathlib import Path
import numpy as np

def print_board(board, path):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if (x, y) in path:
                print('\033[92mO\033[0m', end=' ')  # Green color for path
            elif cell:
                print('\033[91m#\033[0m', end=' ')  # Red color for blocked positions
            else:
                print('\033[94m.\033[0m', end=' ')  # Blue color for open positions
        print()
    print()

def do_maze(board):
    end_pos = (len(board) - 1, len(board[0]) - 1)
    queue = deque([((0, 0), [(0, 0)])])  #
    visited = set() 
    all_solutions = []
    low_score = float("inf")
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end_pos:
            score = len(path) - 1
            if score < low_score:
                low_score = score
                all_solutions = [path]
            elif score == low_score:
                all_solutions.append(path)
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == 0:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return low_score

def do_main(debug_mode=False):
    with open(Path('18/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    if debug_mode:
        with open(Path('18/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    dim = 71

    board = [[0] * dim for _ in range(dim)]
    for line_index, line in enumerate(lines):
        if line_index == 1024:
            break
        r = [int(i) for i in line.split(",")]
        board[r[1]][r[0]] = 1
    print(do_maze(board))

    blocked = False
    board = [[0] * dim for _ in range(dim)]
    b = 0
    while not blocked:
        r = [int(i) for i in lines[b].split(",")]
        board[r[1]][r[0]] = 1
        score = do_maze(board)
        if score == np.inf:
            blocked = True
            break     
        print(f"\r{b}", end='', flush=True)
        b+=1
    print()
    print_board(board, [])
    print(f"Iteration {b+1}")
    print(lines[b])

if __name__ == '__main__':
    do_main(False)
