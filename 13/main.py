from pathlib import Path
import numpy as np
import tqdm


def find_min_a_b(target_x, target_y, a_x, a_y, b_x, b_y):
    # target_x = a * a_x + b * b_x
    # target_y = a * a_y + b * b_y
    A = np.array([[a_x, b_x], [a_y, b_y]])
    T = np.array([target_x, target_y])
    solution = np.linalg.solve(A, T)
    a, b = solution
    a = a.round().astype(int)
    b = b.round().astype(int)
    if a * a_y + b * b_y == target_y and a * a_x + b * b_x == target_x:
        return a, b
    return None, None


def do_main(debug_mode=False):
    with open(Path("13/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("13/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    point_sum2 = 0
    machines = {}

    for line_index, line in tqdm.tqdm(enumerate(lines)):
        index_mach = 0
        if index_mach not in machines:
            machines[index_mach] = {}
        if "A" in line:
            parts = line.strip().split(": ")[1].split(", ")
            x = int(parts[0].split("+")[1])
            y = int(parts[1].split("+")[1])
            machines[index_mach]["A"] = {"X": x, "Y": y}
        elif "B" in line:
            parts = line.strip().split(": ")[1].split(", ")
            x = int(parts[0].split("+")[1])
            y = int(parts[1].split("+")[1])
            machines[index_mach]["B"] = {"X": x, "Y": y}
        elif "Prize" in line:
            parts = line.strip().split(": ")[1].split(", ")
            x2 = int(parts[0].split("=")[1]) + 10000000000000
            y2 = int(parts[1].split("=")[1]) + 10000000000000
            x = int(parts[0].split("=")[1])
            y = int(parts[1].split("=")[1])
            machines[index_mach]["Prize"] = {"X": x, "Y": y}
            machines[index_mach]["Prize_2"] = {"X": x2, "Y": y2}
        elif line.strip() == "":
            min_press_a, min_press_b = find_min_a_b(
                machines[index_mach]["Prize"]["X"],
                machines[index_mach]["Prize"]["Y"],
                machines[index_mach]["A"]["X"],
                machines[index_mach]["A"]["Y"],
                machines[index_mach]["B"]["X"],
                machines[index_mach]["B"]["Y"],
            )
            if min_press_a and min_press_b:
                point_sum += 3 * min_press_a + min_press_b
            min_press_a, min_press_b = find_min_a_b(
                machines[index_mach]["Prize_2"]["X"],
                machines[index_mach]["Prize_2"]["Y"],
                machines[index_mach]["A"]["X"],
                machines[index_mach]["A"]["Y"],
                machines[index_mach]["B"]["X"],
                machines[index_mach]["B"]["Y"],
            )
            if min_press_a and min_press_b:
                point_sum2 += 3 * min_press_a + min_press_b
            index_mach += 1
    print(point_sum)
    print(point_sum2)


if __name__ == "__main__":
    do_main(True)
