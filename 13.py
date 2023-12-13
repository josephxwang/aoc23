from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), heappop/push, math, sys, also dirs, adjs, letters, digits, symbols, also reverse, gok


# !! so tired today
# I'm learning to just run my code and debug that way instead of trying to pre-empt bugs too much

# !! also I should learn to use zip() and reduce(), might save me a lot of effort

def part1(lines):
    # lines = ints(lines)
    # lines = words(lines)
    g = []
    gs = []
    for l in lines:
        if l == '':
            gs.append(grid(g))
            g = []
        else:
            g.append(l)
    gs.append(grid(g))
    tot = 0
    for g in gs:
        R = len(g)
        C = len(g[0])
        for r in range(R-1): # horizontal line
            ok = True
            for dr in range(0,r+1):
                for c in range(C):
                    if r+dr+1 < R and g[r-dr][c] != g[r+dr+1][c]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                tot += (r+1)*100
                break
        for c in range(C-1): # vertical line
            ok = True
            for dc in range(0,c+1):
                for r in range(R):
                    if c+dc+1 < C and g[r][c-dc] != g[r][c+dc+1]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                tot += (c+1)
                break
    return tot

def part2(lines):
    # return
    g = []
    gs = []
    for l in lines:
        if l == '':
            gs.append(grid(g))
            g = []
        else:
            g.append(l)
    gs.append(grid(g))
    tot = 0
    lines = {} # original lines
    for i,g in enumerate(gs):
        R = len(g)
        C = len(g[0])
        for r in range(R-1): # horizontal line
            ok = True
            for dr in range(0,r+1):
                for c in range(C):
                    if r+dr+1 < R and g[r-dr][c] != g[r+dr+1][c]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                lines[i] = ['r',r+1]
                break
        if not ok:
            for c in range(C-1): # vertical line
                ok = True
                for dc in range(0,c+1):
                    for r in range(R):
                        if c+dc+1 < C and g[r][c-dc] != g[r][c+dc+1]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    lines[i] = ['c',c+1]
                    break        
        ok2 = False
        for r1 in range(R): # try all smudges
            for c1 in range(C):
                g[r1][c1] = '.' if g[r1][c1] == '#' else '#' # smudge
                for r in range(R-1): # horizontal line
                    ok = True
                    for dr in range(0,r+1):
                        for c in range(C):
                            if r+dr+1 < R and g[r-dr][c] != g[r+dr+1][c]:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok and (lines[i][0] != 'r' or lines[i][1] != r+1):
                        tot += (r+1)*100
                        ok2 = True
                        break
                for c in range(C-1): # vertical line
                    ok = True
                    for dc in range(0,c+1):
                        for r in range(R):
                            if c+dc+1 < C and g[r][c-dc] != g[r][c+dc+1]:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok and (lines[i][0] != 'c' or lines[i][1] != c+1):
                        tot += (c+1)
                        ok2 = True
                        break
                g[r1][c1] = '.' if g[r1][c1] == '#' else '#' # reset
                if ok2:
                    break
            if ok2:
                break
    return tot # 25373 too low


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)