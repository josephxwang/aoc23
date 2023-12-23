from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra


def part1(lines):
    # lines = ints(lines)
    # lines = words(lines)
    # g,R,C = grid(lines,to_int=False)
    
    tot = 0
    # prod = 1
    for i,l in enumerate(lines):
    # for l in lines:
        pass
    return tot

def part2(lines): # !! need to do a few more calculations, mine are off by a bit
    g,R,C = grid(lines,to_int=False)
    for r in range(R):
        for c in range(C):
            if g[r][c] == 'S':
                start = (r,c)
    rs,cs = start
    n = 26501365
    even,odd = 7712,7675 # manually found
    length = (n*2)//R
    tot = even # initial square
    for i in range(1,length//2):
        if i%2 == 0:
            tot += 4*i*even
        else:
            tot += 4*i*odd
    tot += 1+2*length*odd
    return tot # 2518869718987313 too high


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)