from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra


def part1(lines):
    d = 500
    g = [[[-1]*d for _ in range(d)] for _ in range(d)]
    bricks = defaultdict(set)
    for i,l in enumerate(lines):
        l = l.split('~')
        x1,y1,z1 = map(int,l[0].split(','))
        x2,y2,z2 = map(int,l[1].split(','))
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    g[x][y][z] = i
                    bricks[i].add((x,y,z))
    moved = True
    while moved:
        moved = False
        for i in bricks: # try to move all bricks down
            ok = True
            for x,y,z in bricks[i]:
                if z-1 < 1 or (g[x][y][z-1] != -1 and g[x][y][z-1] != i): # not empty and not self (other brick)
                    ok = False
            if ok:
                for x,y,z in deepcopy(bricks[i]):
                    bricks[i].remove((x,y,z))
                    bricks[i].add((x,y,z-1))
                    g[x][y][z-1] = g[x][y][z]
                    g[x][y][z] = -1
                moved = True
    parents = defaultdict(set) # bricks below
    for i in bricks:
        for x,y,z in bricks[i]:
            if g[x][y][z-1] != -1 and g[x][y][z-1] != i: # brick below
                parents[i].add(g[x][y][z-1])
    solos = set()
    for i in parents:
        if len(parents[i]) == 1: # only one parent
            solos |= parents[i]
    return len(bricks)-len(solos)

def f(i,childs,parents):
    if i not in childs:
        return 0
    tot = 0
    for j in childs[i]:
        parents[j].remove(i)
        if len(parents[j]) == 0: # no more parents
            tot += 1 + f(j,childs,parents)
    return tot

def part2(lines):
    # return
    d = 500
    g = [[[-1]*d for _ in range(d)] for _ in range(d)]
    bricks = defaultdict(set)
    for i,l in enumerate(lines):
        l = l.split('~')
        x1,y1,z1 = map(int,l[0].split(','))
        x2,y2,z2 = map(int,l[1].split(','))
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    g[x][y][z] = i
                    bricks[i].add((x,y,z))
    moved = True
    while moved:
        moved = False
        for i in bricks: # try to move all bricks down
            ok = True
            for x,y,z in bricks[i]:
                if z-1 < 1 or (g[x][y][z-1] != -1 and g[x][y][z-1] != i):
                    ok = False
            if ok:
                for x,y,z in deepcopy(bricks[i]):
                    bricks[i].remove((x,y,z))
                    bricks[i].add((x,y,z-1))
                    g[x][y][z-1] = g[x][y][z]
                    g[x][y][z] = -1
                moved = True
    parents = defaultdict(set) # bricks below
    childs = defaultdict(set) # bricks above
    for i in bricks:
        for x,y,z in bricks[i]:
            if g[x][y][z-1] != -1 and g[x][y][z-1] != i: # brick below
                parents[i].add(g[x][y][z-1])
            if g[x][y][z+1] != -1 and g[x][y][z+1] != i: # brick above
                childs[i].add(g[x][y][z+1])
    tot = 0
    for i in childs:
        curr = f(i,deepcopy(childs),deepcopy(parents))
        tot += curr
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)