from collections import Counter
import copy
from pathlib import Path

import tqdm


def do_main(debug_mode=False):
    with open(Path("11/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("11/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        blinks = 25
        r = [int(i) for i in line.split(" ")]
        new_list = []
        for i in tqdm.tqdm(range(blinks)):
            new_list = []
            for num in r:
                if num == 0:
                    new_list.append(1)
                elif len(str(num)) % 2 == 0:
                    s = str(num)
                    l = int(len(s) / 2)
                    s1 = s[:l]
                    s2 = s[l:]
                    new_list.append(int(s1))
                    new_list.append(int(s2))
                else:
                    new_list.append(num * 2024)
            r = new_list[:]
        print(len(r))

        blinks = 75
        r = [int(i) for i in line.split(" ")]
        r = Counter(r)
        for i in range(blinks):
            new_list = Counter()
            for num, count in r.items():
                if num == 0:
                    new_list[1] += count
                elif len(str(num)) % 2 == 0:
                    s = str(num)
                    l = int(len(s) / 2)
                    s1 = s[:l]
                    s2 = s[l:]
                    new_list[int(s1)] += count
                    new_list[int(s2)] += count
                else:
                    new_list[num * 2024] += count
            r = copy.deepcopy(new_list)
        print(sum(r.values()))


if __name__ == "__main__":
    do_main(False)
