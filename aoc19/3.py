from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,
from os import path

day = path.splitext(path.basename(__file__))[0]

# find the intersection point closest to the central port

# !! could be so much cleaner hahah, use something like:
# DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
# DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

def solve(ls):
    distance = 10000
    grid = [[0] * distance for _ in range(distance)]
    r0 = c0 = distance // 2
    r2 = r1 = r0
    c2 = c1 = c0
    w1 = ls[0].split(',')
    w2 = ls[1].split(',')
    inters = []
    for c in w1:
        d = int(c[1:])
        if c[0] == "R":
            for i in range(d):
                c1 += 1
                if r1 < distance and c1 < distance:
                    grid[r1][c1] = 1
        if c[0] == "L":
            for i in range(d):
                c1 -= 1
                if r1 < distance and c1 < distance:
                    grid[r1][c1] = 1
        if c[0] == "U":
            for i in range(d):
                r1 -= 1
                if r1 < distance and c1 < distance:
                    grid[r1][c1] = 1
        if c[0] == "D":
            for i in range(d):
                r1 += 1
                if r1 < distance and c1 < distance:
                    grid[r1][c1] = 1
    
    for c in w2:
        d = int(c[1:])
        if c[0] == "R":
            for i in range(d):
                c2 += 1
                if r2 < distance and c2 < distance:
                    if grid[r2][c2] == 1:
                        inters.append((r2,c2))
        if c[0] == "L":
            for i in range(d):
                c2 -= 1
                if r2 < distance and c2 < distance:
                    if grid[r2][c2] == 1:
                        inters.append((r2,c2))
        if c[0] == "U":
            for i in range(d):
                r2 -= 1
                if r2 < distance and c2 < distance:
                    if grid[r2][c2] == 1:
                        inters.append((r2,c2))
        if c[0] == "D":
            for i in range(d):
                r2 += 1
                if r2 < distance and c2 < distance:
                    if grid[r2][c2] == 1:
                        inters.append((r2,c2))
    
    closest = distance * 2
    for inter in inters:
        dist = abs(inter[0] - r0) + abs(inter[1] - c0)
        if dist < closest:
            closest = dist
        
    return closest

def solve2(ls):
    distance = 10000
    grid = [[0] * distance for _ in range(distance)]
    steps = [[0] * distance for _ in range(distance)]
    r0 = c0 = distance // 2
    r2 = r1 = r0
    c2 = c1 = c0
    w1 = ls[0].split(',')
    w2 = ls[1].split(',')
    inters = set()
    s = 0
    for c in w1:
        d = int(c[1:])
        if c[0] == "R":
            for i in range(d):
                c1 += 1
                s += 1
                if r1 < distance and c1 < distance:
                    grid[r1][c1] = 1
                    if steps[r1][c1] == 0:
                        steps[r1][c1] = s
        if c[0] == "L":
            for i in range(d):
                c1 -= 1
                s += 1
                if r1 < distance and c1 < distance:
                    grid[r1][c1] = 1
                    if steps[r1][c1] == 0:
                        steps[r1][c1] = s
        if c[0] == "U":
            for i in range(d):
                r1 -= 1
                s += 1
                if r1 < distance and c1 < distance:
                    grid[r1][c1] = 1
                    if steps[r1][c1] == 0:
                        steps[r1][c1] = s
        if c[0] == "D":
            for i in range(d):
                r1 += 1
                s += 1
                if r1 < distance and c1 < distance:
                    grid[r1][c1] = 1
                    if steps[r1][c1] == 0:
                        steps[r1][c1] = s
    
    s = 0
    for c in w2:
        d = int(c[1:])
        if c[0] == "R":
            for i in range(d):
                c2 += 1
                s += 1
                if r2 < distance and c2 < distance:
                    if grid[r2][c2] == 1:
                        if (r2,c2) not in inters:
                            steps[r2][c2] += s
                            inters.add((r2,c2))
        if c[0] == "L":
            for i in range(d):
                c2 -= 1
                s += 1
                if r2 < distance and c2 < distance:
                    if grid[r2][c2] == 1:
                        if (r2,c2) not in inters:
                            steps[r2][c2] += s
                            inters.add((r2,c2))
        if c[0] == "U":
            for i in range(d):
                r2 -= 1
                s += 1
                if r2 < distance and c2 < distance:
                    if grid[r2][c2] == 1:
                        if (r2,c2) not in inters:
                            steps[r2][c2] += s
                        inters.add((r2,c2))
        if c[0] == "D":
            for i in range(d):
                r2 += 1
                s += 1
                if r2 < distance and c2 < distance:
                    if grid[r2][c2] == 1:
                        if (r2,c2) not in inters:
                            steps[r2][c2] += s
                        inters.add((r2,c2))
    
    closest = distance * 2
    for inter in inters:
        dist = steps[inter[0]][inter[1]]
        if dist < closest:
            closest = dist
        
    return closest

ls = [l.strip() for l in open(f"{day}.in")]
print(solve(ls))
print(solve2(ls))