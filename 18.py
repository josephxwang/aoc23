from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra

def dfs(g,r,c): # fill interior
    s = [(r,c)]
    while s:
        r,c = s.pop()
        if g[r][c] == '#':
            continue
        g[r][c] = '#'
        for dr,dc in dirs:
            s.append((r+dr,c+dc))

def part1(lines):
    R = C = 1000
    tot = 0
    g = [['.']*C for _ in range(R)]
    r,c = R//2,C//2
    for l in lines: # fill boundary
        dir,n,_ = l.split()
        dirs = {
            'U':(-1,0),
            'D':(1,0),
            'L':(0,1),
            'R':(0,-1)
        }
        dr,dc = dirs[dir]
        for _ in range(int(n)):
            g[r][c] = '#'
            r += dr
            c += dc
    dfs(g,595,358) # found manually
    # with open('18.out','w') as f:
    #     for row in g:
    #         f.write(''.join(row)+'\n')
    # f.close()
    for row in g:
        tot += row.count('#')
    return tot

# !! tried shoelace formula
# can also do a representation of the points on each row, O(n) instead of O(n^2), need math

# !! nvm I just needed Pick's theorem!

def part2(lines):
    # return
    r,c = 0,0
    vertices = [(r,c)]
    boundaries = 0
    for l in lines:
        hex = l.split()[-1]
        dir = int(hex[-2])
        n = int(hex[2:-2],16) # convert from hex
        dirs = {
            3:(-1,0),
            1:(1,0),
            2:(0,1),
            0:(0,-1)
        }
        dr,dc = dirs[dir]
        r += dr*n
        c += dc*n
        vertices.append((r,c))
        boundaries += n
    area = shoelace(vertices)
    tot = picks(area,boundaries) # Pick's theorem
    return tot # off by 2 for some reason


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)