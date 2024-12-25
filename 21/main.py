from collections import deque
import functools
from pathlib import Path

keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

directional_keypad = {"^": (0, 1), "v": (1, 1), "<": (1, 0), ">": (1, 2), "A": (0, 2)}


def find_all_paths(start, end, key_pad):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    start_pos = key_pad[start]
    target_pos = key_pad[end]
    queue = deque([(start_pos, "", [start_pos])])
    paths = []
    while queue:
        (x, y), path, coord_path = queue.popleft()
        if (x, y) == target_pos:
            paths.append(path + "A")
        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if (nx, ny) in key_pad.values() and (nx, ny) not in coord_path:
                queue.append(((nx, ny), path + move, coord_path + [(nx, ny)]))
    return paths


@functools.cache
def find_best_path_directional(pw, num_levels):
    if num_levels == 0:
        return len(pw)
    presses = 0
    for i, c in enumerate("A" + pw[:-1]):
        start, target = (c, pw[i])
        best = None
        for keys in find_all_paths(start, target, directional_keypad):
            n_presses = find_best_path_directional(keys, num_levels - 1)
            if best is None or n_presses < best:
                best = n_presses
        presses += best
    return presses


def find_best_path_keyboard(pw, layers):
    all_presses = 0
    start_target_pairs = []
    for i, c in enumerate("A" + pw[:-1]):
        start_target_pairs.append((c, pw[i]))
    for start, target in start_target_pairs:
        best = None
        for keys in find_all_paths(start, target, keypad):
            n_presses = find_best_path_directional(keys, layers)
            if best is None or best > n_presses:
                best = n_presses
        all_presses += best
    return all_presses


def do_main(debug_mode=False):
    with open(Path("21/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("21/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum1 = 0
    point_sum2 = 0
    pw_to_find = lines

    for pw in pw_to_find:
        presses = find_best_path_keyboard(pw, 2)
        #print(presses)
        point_sum1 += presses * int(pw[:-1])

    for pw in pw_to_find:
        presses = find_best_path_keyboard(pw, 25)
        #print(presses)
        point_sum2 += presses * int(pw[:-1])

    print(point_sum1)
    print(point_sum2)


if __name__ == "__main__":
    do_main(False)
