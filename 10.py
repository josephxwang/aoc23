from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), heappop/push, math, sys, also dirs, adjs, letters, digits, symbols, also reverse, gok


def part1(lines):
    g = grid(lines)
    # R = len(g)
    # C = len(g[0])
    # for r in range(R):
    #     for c in range(C):
    #         if g[r][c] == 'S':
    #             start = (r,c)
    # print(start)
    # start = (2,0)
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

def part2(lines):
    lines2 = [l.strip() for l in open('10.out')]
    g = grid(lines)
    g2 = grid(lines2)
    R = len(g)
    C = len(g[0])
    # count = 0
    for r in range(R):
        for c in range(C):
            if g2[r][c] == 'O':
                g[r][c] = 'O'
    with open('10.in','w') as f:
        for row in g:
            f.write(''.join(row) + '\n')
    f.close()
    return 1
    #         if g[r][c] != 'X' and g[r][c] != 'O':
    #             count += 1
    # return count
    # count = 0
    # seen = set()
    # s = [(0,0)]
    # # s = [(68,72)] # center chunk is 270
    # while s:
    #     r,c = s.pop()
    #     if (r,c) in seen:
    #         continue
    #     seen.add((r,c))
    #     g[r][c] = ' '
    #     # count += 1
        
    #     for dr,dc in adjs:
    #         if gok(g,r+dr,c+dc) and g[r+dr][c+dc] != 'X':
    #             s.append((r+dr,c+dc))
    # with open('10.out','w') as f:
    #     for row in g:
    #         f.write(''.join(row) + '\n')
    # f.close()
    # return 1 # 635 too high, 553 too high, 461 wrong
        
    
    # count = 0
    # for r in range(R):
    #     for c in range(C):
    #         ok = True
    #         for dr,dc in adjs:
    #             if gok(g,r+dr,c+dc) and g[r+dr][c+dc] != 'X':
    #                 ok = False
    #                 break
    #         if ok and g[r][c] != 'X':
    #             count += 1
    # return count # 331 too low
                
    # start = (107,110) # manually found start S and set to correct pipe
    # r,c = start
    # seen = set([start])
    # for steps in range(100000):
    #     if steps > 2 and start in seen:
    #         seen.remove(start)
    #     symbol = g[r][c]
    #     if symbol == 'F':
    #         if (r,c+1) not in seen:
    #             c += 1
    #         else:
    #             r += 1
    #     elif symbol == 'J':
    #         if (r-1,c) not in seen:
    #             r -= 1
    #         else:
    #             c -= 1
    #     elif symbol == '7':
    #         if (r+1,c) not in seen:
    #             r += 1
    #         else:
    #             c -= 1
    #     elif symbol == 'L':
    #         if (r,c+1) not in seen:
    #             c += 1
    #         else:
    #             r -= 1
    #     elif symbol == '-':
    #         if (r,c+1) not in seen:
    #             c += 1
    #         else:
    #             c -= 1
    #     elif symbol == '|':
    #         if (r-1,c) not in seen:
    #             r -= 1
    #         else:
    #             r += 1
    #     seen.add((r,c))
            
    #     if (r,c) == start:
    #         for r,c in seen:
    #             g[r][c] = 'X'
    #         print(steps)
    #         with open('10.out','w') as f:
    #             for row in g:
    #                 f.write(''.join(row) + '\n')
    #         f.close()
    #         return 1
            # return math.ceil(steps/2)


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)