from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), heappop/push, math, sys, also dirs, adjs, letters, digits, symbols, also reverse, gok


def part1(lines):
    g = grid(lines)
    # for r in range(R):
    #     for c in range(C):
    #         if g[r][c] == 'S':
    #             start = (r,c)
    # print(start)
    start = (107,110) # manually found start S and set to correct pipe
    r,c = start
    seen = set([start])
    for steps in range(100000):
        if steps > 2 and start in seen:
            seen.remove(start)
        symbol = g[r][c]
        if symbol == 'F':
            if (r,c+1) not in seen:
                c += 1
            else:
                r += 1
        elif symbol == 'J':
            if (r-1,c) not in seen:
                r -= 1
            else:
                c -= 1
        elif symbol == '7':
            if (r+1,c) not in seen:
                r += 1
            else:
                c -= 1
        elif symbol == 'L':
            if (r,c+1) not in seen:
                c += 1
            else:
                r -= 1
        elif symbol == '-':
            if (r,c+1) not in seen:
                c += 1
            else:
                c -= 1
        elif symbol == '|':
            if (r-1,c) not in seen:
                r -= 1
            else:
                r += 1
        seen.add((r,c))
            
        if (r,c) == start:
            return math.ceil(steps/2)
        
# !! maybe I somehow track the "side" of the pipe
# thereby tracking inner and outer tiles

# !! maybe convert to <>^v

# !! my solution worked
# alternatives included expanding the grid to double resolution (dealing with the "squeezing between" pipes)
# or traversing the grid where interior nodes are those with odd lines between them and the outside (odd parity)

def dfs(g,seen,r,c):
    count = 0
    s = [(r,c)]
    while s:
        r,c = s.pop()
        if (r,c) in seen:
            continue
        seen.add((r,c))
        g[r][c] = 'I'
        count += 1
        
        for dr,dc in dirs:
            if gok(g,r+dr,c+dc) and g[r+dr][c+dc] not in '<>^v': # interior nodes
                s.append((r+dr,c+dc))
    return count

def part2(lines):
    g = grid(lines)
    start = (107,110) # manually found start S and set to correct pipe
    dr,dc = (-1,0)
    r,c = start
    tot = 0
    seen = set([start])
    seen2 = set()
    for steps in range(100000): # set to <>^v
        if steps > 2 and start in seen:
            seen.remove(start)
        symbol = g[r][c]
        if symbol == 'F':
            if (r,c+1) not in seen:
                g[r][c] = '>'
                c += 1
            else:
                g[r][c] = 'v'
                r += 1
        elif symbol == 'J':
            if (r-1,c) not in seen:
                g[r][c] = '^'
                r -= 1
            else:
                g[r][c] = '<'
                c -= 1
        elif symbol == '7':
            if (r+1,c) not in seen:
                g[r][c] = 'v'
                r += 1
            else:
                g[r][c] = '<'
                c -= 1
        elif symbol == 'L':
            if (r,c+1) not in seen:
                g[r][c] = '>'
                c += 1
            else:
                g[r][c] = '^'
                r -= 1
        elif symbol == '-':
            if (r,c+1) not in seen:
                g[r][c] = '>'
                c += 1
            else:
                g[r][c] = '<'
                c -= 1
        elif symbol == '|':
            if (r-1,c) not in seen:
                g[r][c] = '^'
                r -= 1
            else:
                g[r][c] = 'v'
                r += 1
        seen.add((r,c))
        if (r,c) == start:
            break
    r,c = start
    seen = set([start])
    for steps in range(100000):
        if steps > 2 and start in seen:
            seen.remove(start)
        symbol = g[r][c]
        if gok(g,r+dr,c+dc) and g[r+dr][c+dc] not in '<>^v': # area enclosed
            tot += dfs(g,seen2,r+dr,c+dc)
        if symbol == '<':
            c -= 1
            if gok(g,r+dr,c+dc) and g[r+dr][c+dc] not in '<>^v':
                tot += dfs(g,seen2,r+dr,c+dc)
            if g[r][c] == '^' and (dr,dc) == (1,0):
                dr,dc = (0,-1)
            elif g[r][c] == '^' and (dr,dc) == (-1,0):
                dr,dc = (0,1)
            elif g[r][c] == 'v' and (dr,dc) == (1,0):
                dr,dc = (0,1)
            elif g[r][c] == 'v' and (dr,dc) == (-1,0):
                dr,dc = (0,-1)
        elif symbol == '>':
            c += 1
            if gok(g,r+dr,c+dc) and g[r+dr][c+dc] not in '<>^v':
                tot += dfs(g,seen2,r+dr,c+dc)
            if g[r][c] == '^' and (dr,dc) == (1,0):
                dr,dc = (0,1)
            elif g[r][c] == '^' and (dr,dc) == (-1,0):
                dr,dc = (0,-1)
            elif g[r][c] == 'v' and (dr,dc) == (1,0):
                dr,dc = (0,-1)
            elif g[r][c] == 'v' and (dr,dc) == (-1,0):
                dr,dc = (0,1)
        elif symbol == '^':
            r -= 1
            if gok(g,r+dr,c+dc) and g[r+dr][c+dc] not in '<>^v':
                tot += dfs(g,seen2,r+dr,c+dc)
            if g[r][c] == '>' and (dr,dc) == (0,1):
                dr,dc = (1,0)
            elif g[r][c] == '>' and (dr,dc) == (0,-1):
                dr,dc = (-1,0)
            elif g[r][c] == '<' and (dr,dc) == (0,1):
                dr,dc = (-1,0)
            elif g[r][c] == '<' and (dr,dc) == (0,-1):
                dr,dc = (1,0)
        elif symbol == 'v':
            r += 1
            if gok(g,r+dr,c+dc) and g[r+dr][c+dc] not in '<>^v': # area enclosed
                tot += dfs(g,seen2,r+dr,c+dc)
            if g[r][c] == '>' and (dr,dc) == (0,1):
                dr,dc = (-1,0)
            elif g[r][c] == '>' and (dr,dc) == (0,-1):
                dr,dc = (1,0)
            elif g[r][c] == '<' and (dr,dc) == (0,1):
                dr,dc = (1,0)
            elif g[r][c] == '<' and (dr,dc) == (0,-1):
                dr,dc = (-1,0)
        seen.add((r,c))
        if (r,c) == start:
            break
    # with open('10.in','w') as f:
    #     for row in g:
    #         f.write(''.join(row) + '\n')
    # f.close()
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)