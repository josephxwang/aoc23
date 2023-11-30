from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,
from os import path

day = path.splitext(path.basename(__file__))[0]

# take its mass, divide by three, round down, and subtract 2

def part1(ls):
    sum = 0
    for l in ls:
        sum += int(l) // 3 - 2
    return sum

def part2(ls):
    sum = 0
    for l in ls:
        curr = int(l) // 3 - 2
        while curr > 0:
            sum += curr
            curr = curr // 3 - 2
    return sum

ls = [l.strip() for l in open(f"{day}.in")]

p2 = part2(ls)
if p2:
    print(p2)
    pyperclip.copy(p2)

if not p2:
    p1 = part1(ls)
    print(p1)
    pyperclip.copy(p1)