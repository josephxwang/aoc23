from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols


def part1(lines):
    # lines = ints(lines)
    # lines = words(lines)
    # g = grid(lines)
    
    # sum = 0
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
    pyperclip.copy(p2)
if not p2:
    p1 = part1(ls)
    print(p1)
    pyperclip.copy(p1)