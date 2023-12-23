from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra

sys.setrecursionlimit(10000000)

# !! part 2 should work with a weighted graph showing distances between intersections and then a longest path traversal

# !! ha that's funny. I barely solved this
# my solution idea was right, no idea why it was so slow

# !! no idea why this doesn't work for part 2, commenting out lines 22-23
def dfs(r,c,steps,seen): # do recursively for seen on each path
    if (r,c) == end:
        paths.append(steps+1)
        print(steps+1)
        return
    if (r,c) in seen:
        return
    seen.add((r,c))
    next = []
    for dr,dc in dirs:
        if gok(g,r+dr,c+dc) and g[r+dr][c+dc] != '#':
            if g[r+dr][c+dc] != '.' and m[g[r+dr][c+dc]] != (dr,dc): # slopes
                continue
            # dfs(r+dr,c+dc,steps+1,deepcopy(seen)) # !! inefficient
            next.append((r+dr,c+dc,steps+1))
    for curr in next:
        if len(next) > 1:
            dfs(*curr,deepcopy(seen))
        else:
            dfs(*curr,seen)


def part1(lines):
    global g,R,C,end,paths,m
    g,R,C = grid(lines,to_int=False)
    R -= 2
    C -= 2
    g = g[1:-1]
    for r in range(R): # strip off edges
        g[r] = g[r][1:-1]
    start = (-1,0)
    end = (R-1,C-1)
    m = {'^':(-1,0),'v':(1,0),'>':(0,1),'<':(0,-1)}
    paths = []
    dfs(*start,0,set())
    return max(paths)

def part2(lines): # new approach, use a graph... 
    # return
    global g,R,C,end,paths,graph
    g,R,C = grid(lines,to_int=False)
    R -= 2
    C -= 2
    g = g[1:-1]
    for r in range(R): # strip
        g[r] = g[r][1:-1]
    intersects = set() # find all intersections
    for r in range(R):
        for c in range(C):
            if g[r][c] != '#':
                count = 0
                for dr,dc in dirs:
                    if gok(g,r+dr,c+dc) and g[r+dr][c+dc] != '#':
                        count += 1
                if count > 2:
                    intersects.add((r,c))
    start = (-1,0)
    end = (R-1,C-1)
    intersects.add(start)
    intersects.add(end)

    graph = defaultdict(set) # build graph
    for ir,ic in intersects:
        q = deque([(ir,ic,0,ir,ic)]) # current location, steps (since last intersection), last intersection
        seen = set()
        while q:
            r,c,steps,ir,ic = q.popleft()
            if (r,c) in seen:
                continue
            seen.add((r,c))
            for dr,dc in dirs:
                if gok(g,r+dr,c+dc) and g[r+dr][c+dc] != '#':
                    if (r+dr,c+dc) in intersects:
                        graph[(ir,ic)].add((steps+1,r+dr,c+dc))
                    else:
                        q.append((r+dr,c+dc,steps+1,ir,ic))
    
    paths = []
    res = 0
    def dfs2(r,c,steps,seen): # do recursively for seen on each path
        nonlocal res
        if (r,c) == end:
            if steps+1 > res:
                res = steps+1
                print(res)
            paths.append(steps+1)
            return
        if (r,c) in seen:
            return
        seen.add((r,c))
        for next_steps,r2,c2 in graph[(r,c)]:
            dfs2(r2,c2,steps+next_steps,deepcopy(seen))
    dfs2(*start,0,set())
    return max(paths)


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)