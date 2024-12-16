from pathlib import Path

import tqdm

def do_main(debug_mode=False):
    with open(Path('14/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('14/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    room = []
    # r_h = 7
    # r_w = 11
    r_h = 103
    r_w = 101
    for i in range(r_h): #103
        room.append([])
        for j in range(r_w): #101
            room[i].append(0)

    all_p = []
    all_v = []
    f = Path('14/tree.txt')
    
    for line_index, line in enumerate(lines):
        p = [int(x) for x in line.split(" ")[0].split("=")[1].split(",")]
        v = [int(x) for x in line.split(" ")[1].split("=")[1].split(",")]
        room[p[1]][p[0]] = 1
        all_p.append(p)
        all_v.append(v)

    for t in tqdm.tqdm(range(10000)): # 100 for part 1
        for i in range(len(all_p)):
            if room[all_p[i][1]][all_p[i][0]] > 0:
                room[all_p[i][1]][all_p[i][0]] -= 1
            new_px = all_p[i][0]+all_v[i][0]
            new_py = all_p[i][1]+all_v[i][1]
            if new_px < 0:
                new_px = len(room[0])+new_px
            elif new_px > len(room[0])-1:
                new_px = new_px - len(room[0])
            if new_py < 0:
                new_py = len(room)+new_py
            elif new_py > len(room)-1:
                new_py = new_py - len(room)
            all_p[i][0] = new_px
            all_p[i][1] = new_py
            room[all_p[i][1]][all_p[i][0]] += 1
        # Did not come up with a density analysis, so i manually assesed the first 10k images
        with f.open("a", encoding="utf-8") as file:
            file.write(f"\n\n\n\n\n\n{t+1}\n")
            for inner_list in room:
                li = "".join("█" if x== 1 else ' ' for x in inner_list)
                file.write(f"{li}\n")
    
    lu, ru, ld, rd = 0,0,0,0

    r_h2 = (r_h-1)/2
    r_w2 = (r_w-1)/2

    for i, r in enumerate(room):
        for j, l in enumerate(r):
            if l > 0:
                if j < r_w2: #50
                    if i < r_h2: #51
                        lu += l
                    elif i > r_h2:
                        ld += l
                elif j > r_w2: #50
                    if i < r_h2: #51
                        ru += l
                    elif i > r_h2:
                        rd += l    

    point_sum = lu * ld * ru * rd    
    
    print(point_sum)

    

if __name__ == '__main__':
    do_main(False)