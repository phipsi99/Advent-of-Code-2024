from pathlib import Path
import re

def r_o(operand, register_a, register_b, register_c):   
    if 0 <= operand <= 3: return operand
    if operand == 4: return register_a
    if operand == 5: return register_b 
    if operand == 6: return register_c

def run_program(instructions, register_a, register_b, register_c):
    output  = []
    a = 0
    cache = {}
    ip = 0

    while ip < len(instructions):
        opcode = instructions[ip]
        operand = instructions[ip + 1] if ip + 1 < len(instructions) else 0
        if opcode == 0:
            register_a //= 2 ** r_o(operand, register_a, register_b, register_c)
        elif opcode == 1:
            register_b ^= operand
        
        elif opcode == 2:
            register_b = r_o(operand, register_a, register_b, register_c) % 8
        
        elif opcode == 3: 
            if register_a != 0:
                ip = operand
                continue 
        
        elif opcode == 4:
            register_b ^= register_c 
        
        elif opcode == 5: 
            output.append(r_o(operand, register_a, register_b, register_c) % 8)
        
        elif opcode == 6:
            register_b = register_a // (2 ** r_o(operand, register_a, register_b, register_c))
        
        elif opcode == 7:  
            register_c = register_a // (2 ** r_o(operand, register_a, register_b, register_c))        
        ip += 2
    
    return(output)

def do_main(debug_mode=False):
    with open(Path('17/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('17/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    register_a = 0
    register_b = 0
    register_c = 0
    instructions = []

    for line_index, line in enumerate(lines):
        if "Register A" in line:
            register_a = int(re.findall(r'\d+', line)[0])
        if"Register B" in line:
            register_b = int(re.findall(r'\d+', line)[0])
        if "Register C" in line:
            register_c = int(re.findall(r'\d+', line)[0])
        if "Program" in line:
            s = line.split(" ")[1]
            l = s.split(",")
            for i in range(0, len(l), 1):
                instructions.append((int(l[i])))

    for x in range(1000):
        print(str(run_program(instructions, x, 0, 0)))
    
    # By looking at the output, the number at place n change on every 8^n-1 steps of a.
    # so first place every step, second every 8th step, third every 64 steps, and so on.
    # so we can find each place by adding 8^n until we found this place.
    
    a = 8 ** (len(instructions) - 1)
    while True:
        register_b = register_c = 0
        output = run_program(instructions, a, register_b, register_c)
        if output == instructions:
            break
        for index in range(len(instructions) - 1, -1, -1):
            # sometimes overshoots, so always check for all places from back to front
            if index >= len(output) or output[index] != instructions[index]:
                a += 8 ** index
                break

    print(str(run_program(instructions, register_a, register_b, register_c)))
    print(a)

if __name__ == '__main__':
    do_main(False)