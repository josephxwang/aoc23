from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra




def part1(lines):
    g,R,C = grid(lines,to_int=False)
    for r in range(R):
        for c in range(C):
            if g[r][c] == 'S':
                start = (r,c)
    curr = [start] # do step by step
    for i in range(64+1):
        seen = set()
        next = []
        for r,c in curr:
            if (r,c) in seen:
                continue
            seen.add((r,c))
            for dr,dc in dirs:
                if gok(g,r+dr,c+dc) and g[r+dr][c+dc] != '#':
                    next.append((r+dr,c+dc))
        curr = next
        # print(i,len(seen))
    return len(seen)

# !! idea was to check when a grid is maxed, because then it just flip flops between two numbers

# !! maybe somehow I can cache all the grid states?

# !! maybe have a set containing all the grids that are maxed? 

# !! maybe need to expand boundaries by 1 on all sides, because grids have weird interactivity

# !! this kind of works, but still slow, also a memory hog

# !! I can't cache the whole grid, right?
# well, I could cache the grid start states to eventual "end" states, when they start spilling over into other grids

# !! or some absolute set of seen across the whole entire map across steps
# that way I only deal with the absolute frontier (single "line")

# !! ok, only do very edge, then go back and fill center

# !! also there is this thing called odd or even parity...

# !! this is a hard problem for both time and space

def part2(lines):
    # return
    g,R,C = grid(lines,to_int=False)
    for r in range(R):
        for c in range(C):
            if g[r][c] == 'S':
                start = (r,c)
    r,c = start
    # print(len(even))
    # print(len(odd))
    curr = [(0,0,r,c)] # grid id (since infinite)
    seen = set() # !! optimize this, currently O(n^4)?
    for i in range(5000+1):
        prev = set()
        edges = set() # find edges
        next = []
        for ri,ci,r,c in curr:
            if (ri,ci,r,c) in seen:
                continue
            seen.add((ri,ci,r,c))
            edges.add((ri,ci,r,c))
            for dr,dc in dirs:
                if g[(r+dr)%R][(c+dc)%C] != '#': # not rock
                    next.append(((r+dr)//R,(c+dc)//C,r+dr,c+dc))
        curr = next
    print("done")
    curr = [(0,0)] # even parity
    even = set()
    odd = set()
    i = 0
    while curr: # fill every other, in layers
        next = []
        for r,c in curr:
            if (r,c) in even or (r,c) in odd:
                continue
            if i%2 == 0:
                even.add((r,c))
            else:
                odd.add((r,c))
            for dr,dc in dirs:
                if gok(g,r+dr,c+dc) and g[r+dr][c+dc] != '#':
                    next.append((r+dr,c+dc))
        curr = next
        i += 1
    curr = list(edges)
    tot = 0
    seen1 = set() # good
    seen2 = set() # every other
    i = 0
    gs = set() # initial seen grids
    for ri,ci,_,_ in edges:
        gs.add((ri,ci))
    done = set()
    while curr: # fill every other, in layers
        next = []
        for ri,ci,r,c in curr:
            if (ri,ci,r,c) in seen1 or (ri,ci,r,c) in seen2:
                continue
            if (ri,ci) not in gs and (ri,ci) not in done:
                if (r,c) in even: # even parity
                    tot += len(even)
                else: # odd parity
                    tot += len(even)
                done.add((ri,ci))
            else:
                if i%2 == 0:
                    seen1.add((ri,ci,r,c))
                    tot += 1
                else:
                    seen2.add((ri,ci,r,c))
                for dr,dc in dirs:
                    if ((r+dr)//R,(c+dc)//C,r+dr,c+dc) in seen:
                        next.append(((r+dr)//R,(c+dc)//C,r+dr,c+dc))
        curr = next
        i += 1
    return len(seen1)

# def part2(lines):
#     # return
#     g,R,C = grid(lines,to_int=False)
#     for r in range(R):
#         for c in range(C):
#             if g[r][c] == 'S':
#                 start = (r,c)
#     r,c = start
#     curr = [(0,0,r,c)] # grid id (since infinite)
#     m = defaultdict(list) # map of lengths of each grid id
#     done = set()
#     for i in range(26501365+1): # !! this scales very badly
#         if i%100 == 0:
#             print(i,len(done))
#         tot = 0
#         seen = set()
#         next = []
#         for k in m:
#             if k in done:
#                 tot += m[k][-2]
#                 m[k][-2],m[k][-1] = m[k][-1],m[k][-2] # swap
#                 # m[k].append(m[k][-2])
#         for ri,ci,r,c in curr:
#             if (ri,ci) in done:
#                 if r not in {0,R-1} and c not in {0,C-1}: #  allow edges
#                     continue
#                 else:
#                     for dr,dc in dirs:
#                         if g[(r+dr)%R][(c+dc)%C] != '#' and ((r+dr)//R,(c+dc)//C) not in done: # not rock
#                             next.append(((r+dr)//R,(c+dc)//C,r+dr,c+dc)) # !! some version of this line of code does work, it is just uncomputably slow
#             else:
#                 if (ri,ci,r,c) in seen:
#                     continue
#                 seen.add((ri,ci,r,c))
#                 tot += 1
#                 if (ri,ci) not in m:
#                     m[(ri,ci)] = [0]
#                 m[(ri,ci)][-1] += 1
#                 for dr,dc in dirs:
#                     if g[(r+dr)%R][(c+dc)%C] != '#' and ((r+dr)//R,(c+dc)//C) not in done: # not rock
#                         next.append(((r+dr)//R,(c+dc)//C,r+dr,c+dc)) # !! some version of this line of code does work, it is just uncomputably slow
#         curr = next
#         for k in m:
#             # print(k)
#             if k not in done and len(m[k]) > 2 and m[k][-1] == m[k][-3]: # repeating
#                 done.add(k)
#                 m[k] = m[k][-2:]
#             elif k not in done:
#                 m[k].append(0)
#     # print(done)
#     return tot

# def part2(lines):
#     # return
#     g,R,C = grid(lines,to_int=False)
#     for r in range(R):
#         for c in range(C):
#             if g[r][c] == 'S':
#                 start = (r,c)
#     r,c = start
#     curr = [(0,0,r,c)] # grid id (since infinite)
#     for i in range(50+1):
#         seen = set()
#         next = []
#         for ri,ci,r,c in curr:
#             if (ri,ci,r,c) in seen:
#                 continue
#             seen.add((ri,ci,r,c))
#             for dr,dc in dirs:
#                 if g[(r+dr)%R][(c+dc)%C] != '#': # not rock
#                     next.append(((r+dr)//R,(c+dc)//C,r+dr,c+dc)) # !! some version of this line of code does work, it is just uncomputably slow
#         curr = next
#     return len(seen)


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)