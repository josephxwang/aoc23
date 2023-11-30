from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,
from os import path

day = path.splitext(path.basename(__file__))[0]

part2 = False

def part1(ls):
    ns = []
    for l in ls:
        pass
    
    for i in range(0, len(ns), 4):
        if ns[i] == 1:
            ns[ns[i+3]] = ns[ns[i+1]] + ns[ns[i+2]]
        elif ns[i] == 2:
            ns[ns[i+3]] = ns[ns[i+1]] * ns[ns[i+2]]
        elif ns[i] == 3:
            pass
        elif ns[i] == 4:
            print(ns[ns[i+1]])
        elif ns[i] == 99:
            break
    return

def part2(ls):
    # part2 = True
    return

ls = [l.strip() for l in open(f"{day}.in")]

if not part2:
    p1 = part1(ls)
    print(p1)
    pyperclip.copy(p1)

if part2:
    p2 = part2(ls)
    print(p2)
    pyperclip.copy(p2)