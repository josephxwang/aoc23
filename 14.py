from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), reduce, heappop/push, math, also dirs, adjs, letters, digits, symbols, also reverse, gok


def part1(lines):
    g = grid(lines)
    R = len(g)
    C = len(g[0])
    for r in range(R): # tilt N
        for c in range(C):
            orig = r
            if g[r][c] == 'O':
                while r>0 and g[r-1][c] == '.':
                    r -= 1
                g[orig][c] = '.'
                g[r][c] = 'O'
            r = orig
    # for row in g: print(row)
    tot = 0
    for i,row in enumerate(g):
        tot += row.count('O') * (C-i)
    return tot

# !! maybe somehow track all the horizontal and vertical intervals between #s?
# !! or give ids to the rocks and see when an individual rock begins to cycle (I don't think this is robust though)
# !! or somehow use 0s and 1s and do bit math
# !! what about a partial cycle (a cycle after a certain point?)

def part2(lines): # current eta is 27 hours
    # return
    g = grid(lines)
    R = len(g)
    C = len(g[0])
    rocks = [] # track all rocks
    for r in range(R): # also convert to binary
        for c in range(C):
            if g[r][c] == 'O':
                g[r][c] = 0
                rocks.append((r,c))
            elif g[r][c] == '#':
                g[r][c] = 1
            elif g[r][c] == '.':
                g[r][c] = None
    out = []
    for i in range(1000):
        if i%1000 == 0: print(i)
        rocks.sort()
        next = []
        for curr in rocks: # tilt N
            r,c = curr
            orig = r
            while r>0 and g[r-1][c] == None:
                r -= 1
            g[orig][c] = None
            g[r][c] = 0
            next.append((r,c))
        rocks = next
        rocks.sort()
        next = []
        for curr in rocks: # tilt W
            r,c = curr
            orig = c
            while c>0 and g[r][c-1] == None:
                c -= 1
            g[r][orig] = None
            g[r][c] = 0
            next.append((r,c))
        rocks = next
        rocks.sort(reverse=True)
        next = []
        for curr in rocks: # tilt S
            r,c = curr
            orig = r
            while r<R-1 and g[r+1][c] == None:
                r += 1
            g[orig][c] = None
            g[r][c] = 0
            next.append((r,c))
        rocks = next
        rocks.sort(reverse=True)
        next = []
        for curr in rocks: # tilt E
            r,c = curr
            orig = c
            while c<C-1 and g[r][c+1] == None:
                c += 1
            g[r][orig] = None
            g[r][c] = 0
            next.append((r,c))
        rocks = next
        # curr = 0
        # for i,row in enumerate(g):
        #     curr += row.count(0) * (C-i)
        # out.append(curr)
    # with open('14.out','w') as f: # manually found cycle
    #     for n in out:
    #         f.write(str(n)+'\n')
    tot = 0
    for i,row in enumerate(g):
        tot += row.count(0) * (C-i)
    return tot # 100778 too low


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)