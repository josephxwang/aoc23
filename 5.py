from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols

# !! lol brute forced/guessed part 2 by finding relatively close answer and then trying

# the destination range start, the source range start, and the range length

def part1(lines):
    curr = set(map(int,lines[0].split()[1:]))
    next = set()
    for i in range(2,len(lines)):
        if lines[i] == '':
            curr = next | curr # add all non-matches, they stay the same
            next = set()
        elif lines[i][0].isdigit():
            dest,src,length = map(int,lines[i].split())
            for n in deepcopy(curr):
                if 0 <= n-src < length: # within range
                    next.add(n-src+dest)
                    curr.remove(n)
        
    curr = next | curr

    return min(curr) # 388071289


def loc_to_seed(n, lines):
    lines = lines[2:][::-1] # reverse input
    is_next = False
    for i in range(2,len(lines)):
        if lines[i] == '':
            is_next = False
        elif lines[i][0].isalpha():
            continue
        else:
            dest,src,length = map(int,lines[i].split())
            if not is_next and 0 <= n-dest < length:
                n = n-dest+src
                is_next = True            
    return n


# !! actually good part 2 uses interval math (does whole intervals at a time)

def part2(lines):
    # return
    seeds = list(map(int,lines[0].split()[1:]))
    curr = set()
    
    step = 50000
    for i in range(0,len(seeds),2): # step 1, find rough answer
        start = seeds[i]
        length = seeds[i+1]
        for j in range(0,length,step): # evenly spaced inputs
            curr.add(start+j)
    
    # print(loc_to_seed(84233979,lines)) # step 2, backtrack
        
    for i in range(step): # step 3, search solution space
        curr.add(2605011189+i)
        curr.add(2605011189-i)
        
    next = set()
    for i in range(2,len(lines)):
        if lines[i] == '':
            curr = next | curr
            next = set()
        elif lines[i][0].isdigit():
            dest,src,length = map(int,lines[i].split())
            for n in deepcopy(curr):
                if 0 <= n-src < length:
                    next.add(n-src+dest)
                    curr.remove(n)

    curr = next | curr
    
    return min(curr) # 84206669


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
    pyperclip.copy(p2)
if not p2:
    p1 = part1(ls)
    print(p1)
    pyperclip.copy(p1)