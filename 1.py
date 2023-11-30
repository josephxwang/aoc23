from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,

day = path.splitext(path.basename(__file__))[0]


def part1(ls):
    for l in ls:
        pass
    return

def part2(ls):
    return


ls = [l.strip() for l in open(f"{day}.in")]

p2 = part2(ls)
if p2:
    print(p2)
    pyperclip.copy(p2)

if not p2:
    p1 = part1(ls)
    print(p1)
    pyperclip.copy(p1)