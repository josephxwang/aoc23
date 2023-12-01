from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,

day = path.splitext(path.basename(__file__))[0]


def part1(lines):
    for line in lines:
        pass
    return

def part2(lines):
    return


lines = [l.strip() for l in open(f"{day}.in")]

p2 = part2(lines)
if p2:
    print(p2)
    pyperclip.copy(p2)

if not p2:
    p1 = part1(lines)
    print(p1)
    pyperclip.copy(p1)