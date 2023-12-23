from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra

# !! ok, try using a diamond

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

def part2(lines):
    g,R,C = grid(lines,to_int=False)
    for r in range(R):
        for c in range(C):
            if g[r][c] == 'S':
                start = (r,c)
    # print(start)
    rs,cs = start
    # calculate a diamond, every other
    tot = 0
    n = 26501365
    cl = cs-n
    cr = cs+n
    for c in range(cl,cr+1): # first row
        if g[rs%R][c%C] != '#' and (r+c)%2 == 0:
            tot += 1
    cl += 1
    cr -= 1
    # print(tot)
    print(R,C)
    
    m = {0: 66, 1: 59, 2: 58, 3: 59, 4: 63, 5: 57, 6: 62, 7: 59, 8: 61, 9: 60, 10: 55, 11: 59, 12: 60, 13: 59, 14: 60, 15: 58, 16: 57, 17: 58, 18: 59, 19: 56, 20: 58, 21: 62, 22: 56, 23: 59, 24: 61, 25: 56, 26: 58, 27: 59, 28: 60, 29: 58, 30: 56, 31: 52, 32: 61, 33: 60, 34: 56, 35: 61, 36: 57, 37: 58, 38: 65, 39: 60, 40: 59, 41: 58, 42: 64, 43: 61, 44: 62, 45: 59, 46: 62, 47: 58, 48: 61, 49: 60, 50: 59, 51: 55, 52: 60, 53: 51, 54: 59, 55: 59, 56: 64, 57: 58, 58: 58, 59: 61, 60: 60, 61: 56, 62: 55, 63: 62, 64: 53, 65: 65, 66: 55, 67: 58, 68: 57, 69: 60, 70: 59, 71: 55, 72: 61, 73: 56, 74: 62, 75: 61, 76: 62, 77: 62, 78: 56, 79: 57, 80: 62, 81: 58, 82: 55, 83: 60, 84: 59, 85: 62, 86: 60, 87: 57, 88: 55, 89: 60, 90: 56, 91: 56, 92: 60, 93: 59, 94: 58, 95: 59, 96: 60, 97: 59, 98: 54, 99: 59, 100: 60, 101: 61, 102: 59, 103: 63, 104: 56, 105: 56, 106: 61, 107: 61, 108: 58, 109: 59, 110: 59, 111: 59, 112: 62, 113: 55, 114: 60, 115: 58, 116: 60, 117: 53, 118: 60, 119: 53, 120: 55, 121: 56, 122: 60, 123: 58, 124: 61, 125: 57, 126: 60, 127: 61, 128: 62, 129: 57, 130: 66}
    
    r1 = rs-1 # two rows, expanding from middle
    r2 = rs+1
    # done = {}
    # print(r1,r2,c1,c2)
    while cl <= cr:
        rows = 0 # !! calculate intermediate rows
        c1 = cs
        c2 = cs+1
        if cl < 0:
            c1 = -((cl-cs)%C)
            c2 = (cr-cs)%C
            rows += abs((cl-cs)//C)-1
            rows += (cr-cs)//C
            rows += 1
            print(rows,r1,r2)
        tot += rows*(m[r1]+m[r2])
        
        for c in range(cl,c1+1):
            if g[r1%R][c%C] != '#' and (r1+c)%2 == 0:
                tot += 1
            if g[r2%R][c%C] != '#' and (r2+c)%2 == 0:
                tot += 1
        for c in range(c2,cr+1):
            if g[r1%R][c%C] != '#' and (r1+c)%2 == 0:
                tot += 1
            if g[r2%R][c%C] != '#' and (r2+c)%2 == 0:
                tot += 1
        cl += 1
        cr -= 1
        r1 -= 1
        r2 += 1
        # print(tot)
    # print(r1,r2,c1,c2)
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)