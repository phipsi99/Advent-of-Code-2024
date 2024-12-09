import copy
from pathlib import Path

import tqdm

def find_empty_sequence(arr, length):
    current_sequence = 0
    for i in range(len(arr)):
        if arr[i] == '':
            current_sequence += 1
            if current_sequence == length:
                return i - length + 1
        else:
            current_sequence = 0
    return -1

def do_main(debug_mode=False):
    with open(Path('09/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('09/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    arr = []

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line]
        index = 0
        ii = 0
        for i in tqdm.tqdm(range(len(r))):
            for j in range(r[ii]):
                arr.append(str(index))
            ii += 1
            if  ii >= len(r) - 1:
                break
            for j in range(r[ii]):
                arr.append('')
            index += 1
            ii += 1
        
        new_arr = copy.deepcopy(arr)
        for i in tqdm.tqdm(range(len(arr)-1, 0, -1)):
            test = new_arr.index("")
            if all(t == '' for t in new_arr[test:]):
                break
            if arr[i] == "":
                continue
            for j in range(len(new_arr)):
                if new_arr[j] == "":
                    new_arr[j] = arr[i]
                    new_arr[i] = ""
                    break

        l = [int(i) for i in new_arr if i!= '']
        for i, num in enumerate(l):
            point_sum += i * num

        print(point_sum)
                    
        # Part 2
        point_sum = 0
        new_arr = copy.deepcopy(arr)
        for i in tqdm.tqdm(range(index, 0, -1)):
            if new_arr.index("") > new_arr.index(str(i)):
                break
            space_needed = arr.count(str(i))
            index_space = find_empty_sequence(new_arr[:new_arr.index(str(i))], space_needed)
            if index_space == -1:
                continue
            del_index = new_arr.index(str(i))
            for j in range(space_needed):
                new_arr[index_space + j] = str(i)
                new_arr[del_index + j] = ''
                
        for i, num in enumerate(new_arr):
            if num == '':
                continue
            point_sum += i * int(num)
            
    print(point_sum)

if __name__ == '__main__':
    do_main(False)