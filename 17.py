from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra


# !! I don't think dijkstra fundamentally works: the assumption that subsequent nodes can be related to the min distance of the previous node is false
# because the path to the previous node may change possible paths to susbequent nodes

# !! actually dijkstra would've worked, just need to track seen

# print(dijkstra2())

def dijkstra(g): # !! this is such an odd dijkstra, it doesn't do the dists and parents, it's just a bfs with a priority queue
    R = len(g)
    C = len(g[0])
    q = [(0,0,0,0,0,0)]
    seen = set()
    res = 1278
    while q:
        dist,r,c,dr1,dc1,count = heappop(q)
        if (r,c) == (R-1,C-1) and dist < res:
            res = dist
        if (r,c,dr1,dc1,count) in seen: # same configuration
            continue
        seen.add((r,c,dr1,dc1,count))
        for dr,dc in dirs:
            if (dr1,dc1) == (dr,dc) and count >= 3: # change direction
                continue
            if (dr,dc) == (-dr1,-dc1): # can't reverse
                continue
            if gok(g,r+dr,c+dc):
                if (dr1,dc1) == (dr,dc): # same direction
                    heappush(q,(dist+int(g[r+dr][c+dc]),r+dr,c+dc,dr,dc,count+1))
                else:
                    heappush(q,(dist+int(g[r+dr][c+dc]),r+dr,c+dc,dr,dc,1))
    return res

def part1(lines):
    g,R,C = grid(lines)
    return dijkstra(g)


def bfs2(g):
    R = len(g)
    C = len(g[0])
    
    q = deque([(0,0,0,0,1,0)])
    seen = {}
    res = 1380
    while q:
        dist,r,c,dr1,dc1,count = q.popleft()
        if dist >= res: # heuristic
            continue
        if (r,c) == (R-1,C-1) and dist < res and count >= 3:
            res = dist
            print(res)
        if (r,c,dr1,dc1,count) in seen and dist >= seen[(r,c,dr1,dc1,count)]: # exact same configuration but worse
            continue
        seen[(r,c,dr1,dc1,count)] = dist
        for dr,dc in dirs: # fewer options than in part1?
            if count < 3 and (dr,dc) != (dr1,dc1):
                continue
            if (dr1,dc1) == (dr,dc) and count == 9: # change direction
                continue
            if (dr,dc) == (-dr1,-dc1): # can't reverse
                continue
            if gok(g,r+dr,c+dc):
                if (dr1,dc1) == (dr,dc): # same direction
                    q.append((dist+int(g[r+dr][c+dc]),r+dr,c+dc,dr,dc,count+1))
                else:
                    q.append((dist+int(g[r+dr][c+dc]),r+dr,c+dc,dr,dc,0))
    return res

def part2(lines):
    return
    g,R,C = grid(lines)
    return bfs2(g)


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)