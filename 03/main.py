from pathlib import Path
import re

def mult(scan_str):
    result = 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    all_muls = re.findall(regex, scan_str)
    for mul in all_muls:
        num1 = int(mul[0])
        num2 = int(mul[1])
        result += num1 * num2
    return result
def do_main():
    with open(Path('03/input.txt')) as file:
        line = str(file.read())

    point_sum = 0
    point_sum = mult(line)
    print(point_sum)

    point_sum = 0
    scan_str = line
    do_mult = True
    regex_do = r"(do|don't)\(\)"
    t = re.finditer(regex_do, scan_str)
    end_before = 0
    for m in t:
        e = m.end()
        mul_str = scan_str[end_before:e]
        end_before = e
        if do_mult:
            point_sum += mult(mul_str)
        if m.group(0)== "do()":
            do_mult = True
        else:
            do_mult = False
    if do_mult:
        mul_str = scan_str[end_before:]
        point_sum += mult(mul_str)
    print(point_sum)

    # Different approach part 2
    point_sum = 0
    all_donts = line.split("don't()")
    point_sum += mult(all_donts[0])
    for dont in all_donts:
        all_dos = dont.split("do()")
        for do in all_dos[1:]:
            point_sum += mult(do)
    print(point_sum)
        
if __name__ == '__main__':
    do_main()