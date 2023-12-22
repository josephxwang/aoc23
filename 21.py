from turtle import done
from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra


def part1(lines):
    g,R,C = grid(lines,to_int=False)
    # curr = set([(0,0)]) # even parity
    # even = set()
    # odd = set()
    # i = 0
    # while curr: # fill every other, in layers
    #     next = set()
    #     for r,c in curr:
    #         if (r,c) in even or (r,c) in odd:
    #             continue
    #         if i%2 == 0:
    #             even.add((r,c))
    #             g[r][c] = 'O'
    #         else:
    #             odd.add((r,c))
    #         for dr,dc in dirs:
    #             if gok(g,r+dr,c+dc) and g[r+dr][c+dc] != '#':
    #                 next.add((r+dr,c+dc))
    #     curr = next
    #     i += 1
    # for row in g: print(''.join(row))
    return
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


# !! made lots of progress (I think), but it's still slow and something is a little off...
# !! nvm fixed that bug

def dfs(done,even,odd):
    s = [(0,0)]
    tot = 0
    seen = set()
    while s:
        r,c = s.pop()
        if (r,c) in seen:
            continue
        seen.add((r,c))
        if (r+c)%2 == 0: # verified manually with data
            tot += even
        else:
            tot += odd
        for dr,dc in dirs:
            if (r+dr,c+dc) not in done:
                s.append((r+dr,c+dc))
    return tot

def part2(lines):
    # return
    g,R,C = grid(lines,to_int=False)
    for r in range(R):
        for c in range(C):
            if g[r][c] == 'S':
                start = (r,c)
    r,c = start
    curr = set([(0,0,r,c)]) # grid id (since infinite)
    prev1 = set() # edges 1 ago
    prev2 = set() # edges 2 ago
    for i in range(5000+1): # !! this part is still slow... least it's not a memory hog, it's like O(n)? space, but still O(n^2)? time
        if i%10000 == 0:
            print(i)
        edges = set() # find edges
        next = set()
        for ri,ci,r,c in curr:
            edges.add((ri,ci,r,c))
            for dr,dc in dirs:
                if ((r+dr)//R,(c+dc)//C,r+dr,c+dc) not in prev1 and g[(r+dr)%R][(c+dc)%C] != '#': # ignore inner edge, not rock
                    next.add(((r+dr)//R,(c+dc)//C,r+dr,c+dc))
        prev2 = prev1
        prev1 = edges
        curr = next
    print("done")
    # even,odd = 7712,7675
    even,odd = 42,39
    curr = edges
    tot = 0
    seen1 = set() # good
    seen2 = set() # every other
    i = 0
    start_gs = set() # initial seen grids
    for ri,ci,_,_ in edges:
        start_gs.add((ri,ci))
    done = set()
    while curr: # fill every other, in layers
        next = set()
        for ri,ci,r,c in curr:
            if (ri,ci,r,c) in seen1 or (ri,ci,r,c) in seen2:
                continue
            if (ri,ci) not in start_gs:
                if (ri,ci) not in done:
                    if (ri+ci)%2 == 0:
                        tot += even
                    else: # odd parity
                        tot += odd
                    done.add((ri,ci))
            else:
                if i%2 == 0:
                    seen1.add((ri,ci,r,c))
                    tot += 1
                else:
                    seen2.add((ri,ci,r,c))
                for dr,dc in dirs:
                    if ((r+dr)//R,(c+dc)//C,r+dr,c+dc) not in edges and g[(r+dr)%R][(c+dc)%C] != '#': # keep within edges
                        next.add(((r+dr)//R,(c+dc)//C,r+dr,c+dc))
        if i == 0:
            next = prev2 # inner edge
        curr = next
        i += 1
    tot += dfs(done,even,odd) # fill interior interior
    return tot

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