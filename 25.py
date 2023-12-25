from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra

# !! I got rank 95/83 lol!!
# plotted the graph with networkx hahahaha


def dfs(graph,start):
    count = 0
    s = [start]
    seen = set()
    while s:
        curr = s.pop()
        if curr in seen:
            continue
        seen.add(curr)
        count += 1
        for nbr in graph[curr]:
            s.append(nbr)
    return count

def part1(lines):
    lines = words(lines) 
    m = defaultdict(set)
    for l in lines:
        curr = l[0]
        for next in l[1:]:
            m[curr].add(next)
            m[next].add(curr)
    # fqn/dgc
    # htp/vps
    # ttj/rpd
    m['fqn'].remove('dgc')
    m['dgc'].remove('fqn')
    m['htp'].remove('vps')
    m['vps'].remove('htp')
    m['ttj'].remove('rpd')
    m['rpd'].remove('ttj')
    return dfs(m,'fqn')*dfs(m,'dgc')

def part2(lines): # !! no part 2!!!
    return


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)