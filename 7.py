from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), tqdm, math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

def part1(lines):
    bids = {}
    scores = []
    for l in lines:
        hand,bid = l.split()
        hand = hand.replace('A','E').replace('K','D').replace('Q','C').replace('J','B').replace('T','A')
        bids[hand] = int(bid)
        
        counts = [e[1] for e in Counter(hand).most_common()]
        score = [[1,1,1,1,1],[2,1,1,1],[2,2,1],[3,1,1],[3,2],[4,1],[5]].index(counts)
        scores.append((score,hand))

    tot = 0
    rank = 1
    for _,hand in sorted(scores):
        tot += bids[hand]*rank
        rank += 1
    return tot

def part2(lines):
    # return
    bids = {}
    scores = []
    for l in lines:
        hand,bid = l.split()
        hand = hand.replace('A','E').replace('K','D').replace('Q','C').replace('J','1').replace('T','A')
        bids[hand] = int(bid)
        
        orig = hand
        if hand != '11111': # except for all J card instance, JJJJJ
            card,_ = Counter(hand.replace('1','')).most_common()[0] # find most common non-J card
            hand = hand.replace('1',card)
        
        counts = [e[1] for e in Counter(hand).most_common()]
        match counts:
            case [5]:
                scores.append((6,orig))
            case [4,1]:
                scores.append((5,orig))
            case [3,2]:
                scores.append((4,orig))
            case [3,1,1]:
                scores.append((3,orig))
            case [2,2,1]:
                scores.append((2,orig))
            case [2,1,1,1]:
                scores.append((1,orig))
            case [1,1,1,1,1]:
                scores.append((0,orig))
    
    tot = 0
    rank = 1
    for _,hand in sorted(scores):
        tot += bids[hand]*rank
        rank += 1    
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)