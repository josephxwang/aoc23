from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,

def getn(g, r, c):
    n = g[r][c]
    g[r][c] = '.'
    dc = -1
    while gok(g,r,c+dc) and g[r][c+dc].isdigit():
        n = g[r][c+dc]+n
        g[r][c+dc] = '.'
        dc -= 1
    dc = 1
    while gok(g,r,c+dc) and g[r][c+dc].isdigit():
        n = n+g[r][c+dc]
        g[r][c+dc] = '.'
        dc += 1
    return int(n)

def part1(lines):
    ps = symbols.replace('.','')
    sum = 0
    g = grid(lines)
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] in ps:
                for dr, dc in adjs:
                    if gok(g,r+dr,c+dc) and g[r+dr][c+dc].isdigit():
                        sum += getn(g,r+dr,c+dc)
    return sum

def part2(lines):
    # return
    sum = 0
    g = grid(lines)
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == '*':
                ns = []
                for dr,dc in adjs:
                    if gok(g,r+dr,c+dc) and g[r+dr][c+dc].isdigit():
                        ns.append(getn(g,r+dr,c+dc))
                if len(ns) == 2:
                    sum += math.prod(ns)
    return sum


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f"{day}.in")]
p2 = part2(ls)
if p2:
    print(p2)
    pyperclip.copy(p2)
if not p2:
    p1 = part1(ls)
    print(p1)
    pyperclip.copy(p1)