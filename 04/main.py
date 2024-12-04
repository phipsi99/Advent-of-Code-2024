from pathlib import Path


def do_main(debug_mode=False):
    grid = [[]]
    with open(Path("04/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("04/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    point_sum2 = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == "X":
                for dx, dy in directions:
                    if 0 <= line_index + 3 * dy < len(
                        lines
                    ) and 0 <= char_index + 3 * dx < len(line):
                        if (
                            lines[line_index + dy][char_index + dx] == "M"
                            and lines[line_index + 2 * dy][char_index + 2 * dx] == "A"
                            and lines[line_index + 3 * dy][char_index + 3 * dx] == "S"
                        ):
                            point_sum += 1

    directions_a = [(1, 1), (-1, -1)]
    directions_b = [(1, -1), (-1, 1)]
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == "A":
                found = False
                if 0 < line_index < len(lines) - 1 and 0 < char_index < len(line) - 1:
                    for dx, dy in directions_a:
                        if (
                            lines[line_index + dy][char_index + dx] == "M"
                            and lines[line_index - dy][char_index - dx] == "S"
                        ):
                            for dx2, dy2 in directions_b:
                                if (
                                    lines[line_index + dy2][char_index + dx2] == "M"
                                    and lines[line_index - dy2][char_index - dx2] == "S"
                                ):
                                    point_sum2 += 1
                                    found = True
                                    break
                        if found:
                            break

    print(point_sum)
    print(point_sum2)


if __name__ == "__main__":
    do_main(False)
