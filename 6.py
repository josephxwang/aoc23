from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), tqdm, math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols


# !! I got on the global leaderboard!!!!!
# 135/42
# I was honestly losing hope. My earliest top performance was rank 644, so I wasn't even sure if my goal was still realistic.

# !! new goal: get on the overall leaderboard

def part1(lines):
    lines = ints(lines)
    ts = lines[0]
    dists = lines[1]
    res = 1
    for i,t in enumerate(ts):
        tot = 0
        for hold in range(t):
            if (t-hold)*hold > dists[i]:
                tot += 1
        res *= tot
    return res

# !! I just manually modified the input
def part2(lines):
    return


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