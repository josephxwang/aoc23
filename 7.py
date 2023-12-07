from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), tqdm, math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

def part1(lines):
    bids = {}
    scores = []
    for l in lines:
        l = l.replace('A','E').replace('K','D').replace('Q','C').replace('J','B').replace('T','A')
        hand, bid = l.split()
        bids[hand] = int(bid)
        
        counts = [e[1] for e in Counter(hand).most_common()]
        if counts == [5]:
            scores.append((6,hand))
        elif counts == [4,1]:
            scores.append((5,hand))
        elif counts == [3,2]:
            scores.append((4,hand))
        elif counts == [3,1,1]:
            scores.append((3,hand))
        elif counts == [2,2,1]:
            scores.append((2,hand))
        elif counts == [2,1,1,1]:
            scores.append((1,hand))
        elif counts == [1,1,1,1,1]:
            scores.append((0,hand))
            
    rank = 1
    tot = 0
    for _,hand in sorted(scores):
        tot += bids[hand] * rank
        rank += 1
            
    return tot

def part2(lines):
    # return
    fives = []
    fours = []
    fulls = []
    threes = []
    twos = []
    ones = []
    highs = []
    
    bids = {}
    for l in lines:
        l = l.replace('A','E').replace('K','D').replace('Q','C').replace('J','1').replace('T','A')
        hand, bid = l.split()
        orig = hand
        
        bids[orig] = int(bid)
        
        counts = Counter(hand.replace('1',''))
        if len(counts) > 0:
            most_common, count = counts.most_common(1)[0]
        else:
            most_common = '1'
        if count == 1:
            most_common = sorted(hand)[-1]
        for i,c in enumerate(deepcopy(hand)):
            if c == '1':
                hand = hand[:i] + most_common + hand[i+1:]
        
        counts = [e[1] for e in Counter(hand).most_common()]
        if counts == [5]:
            fives.append(orig)
        elif counts == [4,1]:
            fours.append(orig)
        elif counts == [3,2]:
            fulls.append(orig)
        elif counts == [3,1,1]:
            threes.append(orig)
        elif counts == [2,2,1]:
            twos.append(orig)
        elif counts == [2,1,1,1]:
            ones.append(orig)
        else:
            highs.append(orig)
                
    rank = len(lines)
    tot = 0
    for hand in sorted(fives,reverse=True):
        tot += bids[hand] * rank
        rank -= 1
    for hand in sorted(fours,reverse=True):
        tot += bids[hand] * rank
        rank -= 1
    for hand in sorted(fulls,reverse=True):
        tot += bids[hand] * rank
        rank -= 1
    for hand in sorted(threes,reverse=True):
        tot += bids[hand] * rank
        rank -= 1
    for hand in sorted(twos,reverse=True):
        tot += bids[hand] * rank
        rank -= 1
    for hand in sorted(ones,reverse=True):
        tot += bids[hand] * rank
        rank -= 1
    for hand in sorted(highs,reverse=True):
        tot += bids[hand] * rank
        rank -= 1
    
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)