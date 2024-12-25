from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('25/input.txt')) as file:
        a = file.read()
        blocks = [b.split("\n") for b in a.strip().split("\n\n")]
    
    if debug_mode:
        with open(Path('25/test.txt')) as file:
            a = file.read()
        blocks = [b.split("\n") for b in a.strip().split("\n\n")]
            

    point_sum = 0
    locks = []
    keys = []

    for block in blocks:
        columns = zip(*block)
        hash_counts = [column.count('#') -1 for column in columns]
        if "#" == block[0][0]:
            locks.append(hash_counts)
        else:
            keys.append(hash_counts)
        
    for key in keys:
        for lock in locks:
            if len(key) == len(lock) and all(k + l <= 5 for k, l in zip(key, lock)):
                point_sum += 1
    
    print(point_sum)

if __name__ == '__main__':
    do_main(False)