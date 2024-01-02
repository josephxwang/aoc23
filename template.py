from utils import * 
# Counter, defaultdict, deque, heap(ify|pop|push), Node
# deepcopy, cache, reduce, math
# constants: dirs, adjs, alphabet, ALPHABET, digits, punctuation
# functions: isprime, (p)factors, gok, grot(cw|ccw), shoelace, picks, intersect, overlap(1d|2d|3d)
# graph functions: (g)dfs, (g)bfs, (g)dijkstra


def part1(ls):
    # ls = ints(ls)
    # ls = words(ls)
    # g,R,C = grid(ls,to_int=False)
    
    tot = 0
    # prod = 1
    for i,l in enumerate(ls):
    # for l in ls:
        
    return tot

def part2(ls):
    return


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)