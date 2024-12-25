from collections import defaultdict
from itertools import combinations
from pathlib import Path

def find_set2(conn):
    max_set = set()
    for pc in conn:
        current_set = {pc}
        for other_pc in conn[pc]:
            if all(other_pc in conn[n] for n in current_set):
                current_set.add(other_pc)
        if len(current_set) > len(max_set):
            max_set = current_set
    return max_set

def find3sets(conn):
    all = set()
    for pc in conn:
        neighbors = list(conn[pc])
        for a, b in combinations(neighbors, 2):
            if a in conn[b]:
                t = tuple(sorted([pc, a, b]))
                all.add(t)
    return all

def do_main(debug_mode=False):
    with open(Path('23/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('23/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    conn  = defaultdict(set)
    
    for line_index, line in enumerate(lines):
        a = line.split('-')[0]
        b = line.split('-')[1]
        conn[a].add(b)
        conn[b].add(a)

    all = find3sets(conn)
    sel = set()
    for con in all:
        for pc in con:
            if pc.startswith("t"):
                sel.add(con)
    print(len(sel))

    max_set = find_set2(conn)
    pw = ",".join(sorted(list(max_set)))
    print(pw)

if __name__ == '__main__':
    do_main(False)