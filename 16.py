from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra


def part1(lines):
    g,R,C = grid(lines)
    seen = [[[] for _ in range(C)] for _ in range(R)] # track seen as dirs
    tot = 0
    s = [(0,0,0,1)] # (position,direction)
    while s:
        r,c,dr,dc = s.pop()
        if not gok(g,r,c):
            continue
        if (dr,dc) in seen[r][c]:
            continue
        seen[r][c].append((dr,dc))
        tile = g[r][c]
        if tile == '/':
            dr,dc = -dc,-dr
        elif tile == '\\':
            dr,dc = dc,dr
        elif tile == '|':
            if dc: # going L or R
                dr,dc = 1,0
                s.append((r-1,c,-1,0))
        elif tile == '-':
            if dr: # going U or D
                dr,dc = 0,1
                s.append((r,c-1,0,-1))
        s.append((r+dr,c+dc,dr,dc))
    for row in seen:
        tot += C-row.count([])
    return tot

def part2(lines):
    # return
    g,R,C = grid(lines)
    res = 0
    starts = [] # all possible start tiles
    for r in range(R):
        starts.append((r,0,0,1))
        starts.append((r,C-1,0,-1))
    for c in range(C):
        starts.append((0,c,1,0))
        starts.append((R-1,c,-1,0))
    for start in starts:
        seen = [[[] for _ in range(C)] for _ in range(R)] # track seen as dirs
        tot = 0
        s = [start] # (position,direction)
        while s:
            r,c,dr,dc = s.pop()
            if not gok(g,r,c):
                continue
            if (dr,dc) in seen[r][c]:
                continue
            seen[r][c].append((dr,dc))
            tile = g[r][c]
            if tile == '/':
                dr,dc = -dc,-dr
            elif tile == '\\':
                dr,dc = dc,dr
            elif tile == '|':
                if dc: # going L or R
                    dr,dc = 1,0
                    s.append((r-1,c,-1,0))
            elif tile == '-':
                if dr: # going U or D
                    dr,dc = 0,1
                    s.append((r,c-1,0,-1))
            s.append((r+dr,c+dc,dr,dc))
        for row in seen:
            tot += C-row.count([])
        if tot > res:
            res = tot
    return res


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)