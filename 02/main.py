from pathlib import Path


def check_valid(r):
    ascending = all(1 <= r[i] - r[i + 1] <= 3 for i in range(len(r) - 1))
    descending = all(-3 <= r[i] - r[i + 1] <= -1 for i in range(len(r) - 1))
    if ascending or descending:
        return True


def do_main():
    with open(Path("02/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    ri = 0
    rii = 0
    for line_index, line in enumerate(lines):
        r = [int(i) for i in line.split(" ")]
        if check_valid(r):
            ri += 1
        for i in range(len(r)):
            nr = r[:i] + r[i+1:]
            if check_valid(nr):
                rii += 1
                break

    print(ri)
    print(rii)


if __name__ == "__main__":
    do_main()
