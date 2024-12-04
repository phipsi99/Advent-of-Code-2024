from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('10/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('10/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line.split(" ")]

if __name__ == '__main__':
    do_main(False)