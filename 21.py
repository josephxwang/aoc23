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

# !! I really like this code..

# !! ok, the last partial layer has mixed even/odd parity...
# dangit, I thought that would have solved it...

# !! wow I did finally solve it... this problem was actually easier than I thought...
# I mean at least compared to my 21_2 code hahaha
# but I still don't understand the weird off by 1 between even-3809 vs 3902

def part2(lines):
    g,R,C = grid(lines,to_int=False)
    n = 26501365 # odd
    even,odd = 7712,7675 # manually found
    layers = n//R
    tot = odd # initial square will have odd parity
    for i in range(1,layers+1):
        if i%2 == 1:
            tot += 4*i*even
        else:
            tot += 4*i*odd
    tot -= layers*(odd-3911) # remove odd corners
    # tot += layers*(even-3809) # add even corners
    tot += layers*3902
    tot -= odd-3911 # last (partial) layer has *mainly* odd parity?
    return tot # 629714316966378,629714316966538 too low, 629720542538809,629720542538911,629720655017711,629720557509009,629720557509046,629720557516778,629720570658611 not right


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)