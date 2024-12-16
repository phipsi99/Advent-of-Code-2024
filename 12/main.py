from pathlib import Path
from typing import OrderedDict


def find_indexes(grid, target):
    indexes = []
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value == target:
                indexes.append((col_index, row_index))
    return indexes


def find_all_connected(indexes, visited, directions, current_index, group):
    visited.add(current_index)
    group.append(current_index)
    for direction in directions:
        new_index = (current_index[0] + direction[0], current_index[1] + direction[1])
        if new_index in indexes and new_index not in visited:
            find_all_connected(indexes, visited, directions, new_index, group)


def split_into_groups(indexes, directions):
    visited = set()
    groups = []
    for index in indexes:
        if index not in visited:
            group = []
            find_all_connected(indexes, visited, directions, index, group)
            groups.append(group)
    return groups


def calculate_border_length_and_sides(group, map_size, directions):
    border_length = 0
    sides = 0
    found_borders = {}
    for index in group:
        for direction in directions:
            new_index = (index[0] + direction[0], index[1] + direction[1])
            if (
                new_index[0] < 0
                or new_index[0] >= map_size[0]
                or new_index[1] < 0
                or new_index[1] >= map_size[1]
                or new_index not in group
            ):
                border_length += 1
                if index not in found_borders:
                    found_borders[index] = []
                found_borders[index].append(directions.index(direction))

    found_borders = OrderedDict(sorted(found_borders.items(), key=lambda x: x[0][0]))
    found_borders = OrderedDict(sorted(found_borders.items(), key=lambda x: x[0][1]))
    found_sides = {}
    sides = 0
    for found_border, ori in found_borders.items():
        x, y = found_border
        for orient in ori:
            for dir in directions:
                adjectant_border = (x + dir[0], y + dir[1])
                if (
                    adjectant_border in found_sides
                    and orient in found_sides[adjectant_border]
                ):
                    if found_border not in found_sides:
                        found_sides[found_border] = []
                    found_sides[found_border].append(orient)
            if not (
                found_border in found_sides and orient in found_sides[found_border]
            ):
                sides += 1
                if found_border not in found_sides:
                    found_sides[found_border] = []
                found_sides[found_border].append(orient)
    return border_length, sides


def do_main(debug_mode=False):
    with open(Path("12/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("12/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    point_sum2 = 0

    for line_index, line in enumerate(lines):
        lines[line_index] = [i for i in line]
    expanded_lines = [["."] * (len(lines[0]) + 2)]
    for line in lines:
        expanded_lines.append(["."] + line + ["."])
    expanded_lines.append(["."] * (len(lines[0]) + 2))

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    already_visited = []
    for (
        row_index,
        row,
    ) in enumerate(lines):
        for col_index, col in enumerate(row):
            if col in already_visited:
                continue
            already_visited.append(col)
            indexes = find_indexes(lines, col)
            groups = split_into_groups(indexes, directions)
            for group in groups:
                length, sides = calculate_border_length_and_sides(
                    group, (len(lines), len(row)), directions
                )
                point_sum += length * len(group)
                print(f"{col}: {sides}")
                point_sum2 += sides * len(group)

    print(point_sum)
    print(point_sum2)


if __name__ == "__main__":
    do_main(False)
