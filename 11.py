from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), heappop/push, math, sys, also dirs, adjs, letters, digits, symbols, also reverse, gok


def part1(lines):
    g = grid(lines)
    R = len(g)
    C = len(g[0])
    r = 0 # add rows
    while r < R:
        if g[r].count('.') == C:
            g.insert(r,['.']*C)
            R += 1
            r += 1
        r += 1
    c = 0 # add columns
    while c < C:
        ok = True
        for r in range(R):
            if g[r][c] != '.':
                ok = False
                break
        if ok:
            for r in range(R):
                g[r].insert(c,'.')
            C += 1
            c += 1
        c += 1
    gals = []
    for r in range(R):
        for c in range(C):
            if g[r][c] == '#':
                gals.append((r,c))
    tot = 0
    for i in range(len(gals)):
        r1,c1 = gals[i]
        for r2,c2 in gals[i+1:]:
            tot += abs(r2-r1)+abs(c2-c1)
    return tot

def part2(lines):
    # return
    g = grid(lines)
    R = len(g)
    C = len(g[0])
    rs = set() # find empty rows
    for r in range(R):
        if g[r].count('.') == C:
            rs.add(r)
    cs = set() # find empty columns
    for c in range(C):
        ok = True
        for r in range(R):
            if g[r][c] != '.':
                ok = False
                break
        if ok:
            cs.add(c)
    gals = []
    for r in range(R):
        for c in range(C):
            if g[r][c] == '#':
                gals.append((r,c))
    tot = 0
    for i in range(len(gals)):
        r1,c1 = gals[i]
        for r2,c2 in gals[i+1:]:
            tot += abs(r2-r1)+abs(c2-c1)
            for r in range(min(r1,r2)+1,max(r1,r2)):
                if r in rs: # empty rows
                    tot += (1000000-1)
            for c in range(min(c1,c2)+1,max(c1,c2)):
                if c in cs: # empty columns
                    tot += (1000000-1)
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)