from utils import * # deque, Counter, defaultdict, deepcopy, cache (@cache), math, sys, also ints(ls), letters, digits,
from os import path

day = path.splitext(path.basename(__file__))[0]

# opcode - either 1, 2, or 99

def solve(ls):
    ns = ints(ls)[0]
    ns[1] = 12
    ns[2] = 2
    # print(ns)
    for i in range(0, len(ns), 4):
        if ns[i] == 1:
            ns[ns[i+3]] = ns[ns[i+1]] + ns[ns[i+2]]
        elif ns[i] == 2:
            ns[ns[i+3]] = ns[ns[i+1]] * ns[ns[i+2]]
        elif ns[i] == 99:
            break
    return ns[0]

# 100 * noun + verb

def solve2(ls):
    orig = ints(ls)[0]
    
    # print(ns)
    for a1 in range(100):
        for a2 in range(100):
            ns = deepcopy(orig)
            ns[1] = a1
            ns[2] = a2
            
            for i in range(0, len(ns), 4):
                if ns[i] == 1:
                    ns[ns[i+3]] = ns[ns[i+1]] + ns[ns[i+2]]
                elif ns[i] == 2:
                    ns[ns[i+3]] = ns[ns[i+1]] * ns[ns[i+2]]
                elif ns[i] == 99:
                    break
            
            if ns[0] == 19690720:
                return 100 * a1 + a2
            
ls = [l.strip() for l in open(f"{day}.in")]
print(solve(ls))
print(solve2(ls))