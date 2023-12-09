from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols


# !! hmm maybe my new goal is just top 20 (top 10%) in Smarty Leaderboard 002

def part1(lines):
    lines = ints(lines)
    tot = 0
    for line in lines:
        seqs = [line]
        ok = False
        while not ok:
            seq = []
            last = seqs[-1]
            for i in range(len(last)-1):
                seq.append(last[i+1]-last[i])
            seqs.append(seq)
            if seq.count(0) == len(seq): # messed up this line of code :(, originally, if sum(seq) == 0
                ok = True
        
        seqs = reverse(seqs)
        for i in range(1,len(seqs)):
            seqs[i].append(seqs[i][-1]+seqs[i-1][-1])
        tot += seqs[-1][-1]
    return tot

def part2(lines):
    # return
    lines = ints(lines)
    tot = 0
    for line in lines:
        seqs = [line]
        ok = False
        while not ok:
            seq = []
            last = seqs[-1]
            for i in range(len(last)-1):
                seq.append(last[i+1]-last[i])
            seqs.append(seq)
            if seq.count(0) == len(seq):
                ok = True
                
        seqs = reverse(seqs) # reverse for simplicity
        for i in range(1,len(seqs)):
            seqs[i].append(seqs[i][0]-seqs[i-1][-1]) # actually store in back for efficiency
        tot += seqs[-1][-1]
    return tot

day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)