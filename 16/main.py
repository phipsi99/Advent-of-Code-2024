from collections import deque
from pathlib import Path


def do_main(debug_mode=False):
    with open(Path("16/input.txt")) as file:
        lines = [line.rstrip() for line in file]
    if debug_mode:
        with open(Path("16/test.txt")) as file:
            lines = [line.rstrip() for line in file]
    lab = [list(line) for line in lines]

    start_pos, end_pos = None, None
    for y, cy in enumerate(lab):
        for x, cx in enumerate(cy):
            if cx == "S":
                start_pos = (x, y)
            if cx == "E":
                end_pos = (x, y)

    queue = deque([(start_pos, (1, 0), 0, [start_pos])])
    visited = {}
    all_solutions = []
    low_score = float("inf")

    while queue:
        (x, y), prev_dir, turns, path = queue.popleft()
        if (x, y) == end_pos:
            score = turns * 1000 + len(path) - 1
            if score < low_score:
                low_score = score
                all_solutions = [(turns, path)]
            elif score == low_score:
                all_solutions.append((turns, path))
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            new_dir = (dx, dy)
            if 0 <= nx < len(lab[0]) and 0 <= ny < len(lab) and lab[ny][nx] != "#":
                new_turns = turns + (new_dir != prev_dir and prev_dir is not None)
                if (nx, ny, new_dir) not in visited or new_turns <= visited[
                    (nx, ny, new_dir)
                ]:
                    visited[(nx, ny, new_dir)] = new_turns
                    queue.append(((nx, ny), new_dir, new_turns, path + [(nx, ny)]))

    print(low_score)
    unique_points = set()
    for _, path in all_solutions:
        unique_points.update(path)
    print(len(unique_points))


if __name__ == "__main__":
    do_main(False)
