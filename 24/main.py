from collections import deque
from pathlib import Path
import re


def do_main(debug_mode=False):
    with open(Path('24/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('24/test.txt')) as file:
            lines = [line.rstrip() for line in file]
    db = {}
    i = 0
    for line in lines:
        if ":" in line:
            key = line.split(":")[0].strip()
            value = line.split(":")[1].strip()
            db[key] = int(value)
            i +=1

    point_sum = 0
    queue = deque(lines[i:])
    selected_item = None

    while len(queue) > 0:
        for item in queue:
            not_all_inputs = False
            li = re.findall(r'[a-z\d]{3}', item.split("->")[0])
            for c in li:
                if c not in db:
                    not_all_inputs = True
                    break
            if not_all_inputs:
                continue
            selected_item = item
            break
        queue.remove(selected_item)
        line = selected_item
        if "AND" in line:
            x = line.split("->")[0].split("AND")[0].strip()
            xx = line.split("->")[0].split("AND")[1].strip()
            xxx = line.split("->")[1].strip()
            db[xxx] = db[x] & db[xx]
        elif "XOR" in line:
            x = line.split("->")[0].split("XOR")[0].strip()
            xx = line.split("->")[0].split("XOR")[1].strip()
            xxx = line.split("->")[1].strip()
            db[xxx] = db[x] ^ db[xx]
        elif "OR" in line:
            x = line.split("->")[0].split("OR")[0].strip()
            xx = line.split("->")[0].split("OR")[1].strip()
            xxx = line.split("->")[1].strip()
            db[xxx] = db[x] | db[xx]
    
    for x in ["x", "y", "z"]:
        z_vals = []
        for key, value in db.items():
            if key.startswith(x):
                z_vals.append((key, value))
        z_vals.sort()
        z_vals= z_vals[::-1]
        z = "".join([str(x[1]) for x in z_vals])
        print(z)
        print(int(z, 2))


if __name__ == '__main__':
    do_main(False)