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
        
    return tot

def part2(lines):
    return


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)