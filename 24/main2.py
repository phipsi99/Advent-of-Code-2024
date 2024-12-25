from pathlib import Path
import re
from graphviz import Digraph
import re
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

def parse_wire(expression):
    match = re.match(r'(\w+)\s+(\w+)\s+(\w+)\s*->\s*(\w+)', expression)
    return match.groups()  

def generate_circuit_diagram(wire_list):
    output_file = f"./circuits/circuit"
    graph = Digraph(comment="Logic Circuit", format="png")
    graph.attr(rankdir="LR")
    graph.attr("node", shape="circle", fontsize="10")
    
    nodes = set() 

    for instruction in wire_list:
        op1, operation, op2, output = parse_wire(instruction)
        
        if op1 not in nodes:
            graph.node(op1, op1)
            nodes.add(op1)
        if op2 not in nodes:
            graph.node(op2, op2)
            nodes.add(op2)
        if output not in nodes:
            graph.node(output, output)
            nodes.add(output)
        
        gate_name = f"{operation}_{output}"
        graph.node(gate_name, operation, shape="rectangle")
        
        graph.edge(op1, gate_name)
        graph.edge(op2, gate_name)
        graph.edge(gate_name, output)
    
    graph.render(output_file, cleanup=True)


def do_main(debug_mode=False):
    with open(Path('24/input_swapped.txt')) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path('24/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    generate_circuit_diagram(lines[91:])
    # By manual visual assesing, with some heuristics, like XOR has to be before zXX and so on
    # z07,vmv z20,kfm z28,hnv hth,tqr
    # hnv,hth,kfm,tqr,vmv,z07,z20,z28


if __name__ == '__main__':
    do_main(False)
