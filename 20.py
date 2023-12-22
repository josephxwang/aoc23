from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra

# !! got on leaderboard again, rank 84!!
# almost didn't do today's on release--I was tired
# anyhow I kind of just did some rough code for part 1,
# then for part 2 I just lcmed again
# it helped that I also manually hacked the input a little for part 1 (put &s first, did psuedo topological sort),
# so I knew what to look for a bit

def part1(lines):
    lows = 0 # False
    highs = 0 # True
    m = {}
    start = []
    ands = {}
    for l in lines:
        curr,next = [s.strip() for s in l.split('->')]
        next = [s.strip() for s in next.split(',')]
        if curr == 'broadcaster': # button
            start = next
        else:
            m[curr[1:]] = (curr[0],False,next) # (symbol,state,next)
            if curr[0] == '&':
                ands[curr[1:]] = {}
            for mod in next: # manually put &s first in input so this computes
                if mod in ands:
                    ands[mod][curr[1:]] = False # default L
    for _ in range(1000):
        lows += 1 # initial L
        q = deque([(False,mod,None) for mod in start]) # (pulse,curr,prev)
        while q:
            pulse,curr,prev = q.popleft()
            if pulse:
                highs += 1
            else:
                lows += 1
            if curr in m:
                symb,state,next = m[curr]
                if symb == '%' and not pulse: # L
                    m[curr] = (symb,not state,next) # flip state
                    for mod in next:
                        q.append((not state,mod,curr))
                elif symb == '&':
                    ands[curr][prev] = pulse
                    if all(ands[curr].values()): # if all H
                        for mod in next:
                            q.append((False,mod,curr))
                    else:
                        for mod in next:
                            q.append((True,mod,curr))
    return lows*highs

def part2(lines):
    # return
    # print(math.lcm(3761,3931,4049,4079))
    lows = 0
    highs = 0
    m = {}
    start = []
    ands = {}
    for l in lines:
        curr,next = [s.strip() for s in l.split('->')]
        next = [s.strip() for s in next.split(',')]
        if curr == 'broadcaster':
            start = next
        else:
            m[curr[1:]] = (curr[0],False,next) # (symbol,state,next)
            if curr[0] == '&':
                ands[curr[1:]] = {}
            for mod in next: # manually put &s first in input so this computes
                if mod in ands:
                    ands[mod][curr[1:]] = False # default L    
    # !! answer will be within a cycle
    for i in range(10000): # !! recursive?? no, because need to do "layer by layer"
        lows += 1 # initial L
        q = deque([(False,mod,None) for mod in start]) # (pulse,curr,prev)
        while q:
            pulse,curr,prev = q.popleft()
            if pulse:
                highs += 1
            else:
                lows += 1
            if curr in m:
                symb,state,next = m[curr]
                if symb == '%' and not pulse: # L
                    m[curr] = (symb,not state,next) # flip state
                    for mod in next:
                        q.append((not state,mod,curr))
                elif symb == '&':
                    ands[curr][prev] = pulse
                    if all(ands[curr].values()): # if all H
                        for mod in next:
                            q.append((False,mod,curr))
                    else:
                        if 'kh' in next: # sends H to kh, kh goes to rx
                            print(i+1,curr)
                        for mod in next:
                            q.append((True,mod,curr))
    return lows*highs


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)