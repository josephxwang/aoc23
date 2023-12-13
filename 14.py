from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), heappop/push, math, sys, also dirs, adjs, letters, digits, symbols, also reverse, gok


def part1(lines):
    # lines = ints(lines)
    # lines = words(lines)
    # g = grid(lines)
    
    # tot = 0
    for l in lines:
        pass
    return

def part2(lines):
    return


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)