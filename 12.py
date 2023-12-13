from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), heappop/push, math, sys, also dirs, adjs, letters, digits, symbols, also reverse, gok

# @cache
# def smartr(l,groups,i,j): # for pure ?s, ended up not needing
#     if i-2 < l and j == len(groups):
#         return 1
#     if i >= l:
#         return 0
#     tot = 0
#     tot += smartr(l,groups,i+groups[j]+1,j+1) # set a group
#     tot += smartr(l,groups,i+1,j) # increment
#     return tot

@cache # this is the way
def smartterr(s,groups,i,j): # smarter recursive :)
    if j == len(groups):
        if s[i:].count('#') == 0: # no remaining #s
            return 1
        return 0
    if i >= len(s):
        return 0
    tot = 0
    if s[i:i+groups[j]].count('#') + s[i:i+groups[j]].count('?') == groups[j] and (i+groups[j] == len(s) or s[i+groups[j]] != '#'): # all #s or ?s, very proud of this line
        tot += smartterr(s,groups,i+groups[j]+1,j+1) # set a group and skip one (also don't actually need to modify s)
    if s[i] != '#':
        tot += smartterr(s,groups,i+1,j) # increment
    return tot

def r(s,groups,i): # 2^n, try all
    if s.count('?') == 0: # base case
        ns = [len(group) for group in s.split('.') if group != '']
        if ns == groups:
            return 1
        return 0
    tot = 0
    if s[i] == '?': # try both
        tot += r(s[:i]+'.'+s[i+1:],groups,i+1)
        tot += r(s[:i]+'#'+s[i+1:],groups,i+1)
    else:
        tot = r(s,groups,i+1)
    return tot

def part1(lines):
    rows = [l.split()[0] for l in lines]
    groups = [l.split()[1] for l in lines]
    groups = ints(groups)
    tot = 0
    for i in range(len(rows)):
        tot += r(rows[i],groups[i], 0)
    return tot

def part2(lines):
    # return
    rows = [l.split()[0] for l in lines]
    groups = [l.split()[1] for l in lines]
    groups = ints(groups)
    tot = 0
    for i in range(len(rows)):
        # if i % 10 == 0:
        #     print(i)
        tot += smartterr(((rows[i]+'?')*5)[:-1],tuple(groups[i]*5),0,0)
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)