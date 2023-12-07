from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), tqdm, math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

def part1(lines):
    tot = 0
    fives = set()
    fours = set()
    fulls = set()
    threes = set()
    twos = set()
    ones = set()
    highs = set()
    
    bids = {}
    for l in lines:
        l = l.replace('A','E').replace('K','D').replace('Q','C').replace('J','B').replace('T','A')
        cards, bid = l.split()
        bids[cards] = int(bid)
        
        counts = [e[1] for e in Counter(cards).most_common()]
        if counts == [5]:
            fives.add(cards)
        elif counts == [4,1]:
            fours.add(cards)
        elif counts == [3,2]:
            fulls.add(cards)
        elif counts == [3,1,1]:
            threes.add(cards)
        elif counts == [2,2,1]:
            twos.add(cards)
        elif counts == [2,1,1,1]:
            ones.add(cards)
        else:
            highs.add(cards)
        # s = set(cards)
        # if len(s) == 1:
        #     fives.add(cards)
        # elif len(s) == 2:
        #     for card in s:
        #         if cards.count(card) == 4:
        #             fours.add(cards)
        #         elif cards.count(card) == 3:
        #             fulls.add(cards)
        # elif len(s) == 3:
        #     for card in s:
        #         if cards.count(card) == 3:
        #             threes.add(cards)
        #         elif cards.count(card) == 2:
        #             twos.add(cards)
        # elif len(s) == 4:
        #     ones.add(cards)
        # elif len(s) == 5:
        #     highs.add(cards)
            
    fives = list(fives)
    fours = list(fours)
    fulls = list(fulls)
    threes = list(threes)
    twos = list(twos)
    ones = list(ones)
    highs = list(highs)
    
    fives.sort(reverse=True); fours.sort(reverse=True); fulls.sort(reverse=True); threes.sort(reverse=True); twos.sort(reverse=True); ones.sort(reverse=True); highs.sort(reverse=True)
        
    rank = len(lines)
    for cards in fives:
        tot += bids[cards] * rank
        rank -= 1
    for cards in fours:
        tot += bids[cards] * rank
        rank -= 1
    for cards in fulls:
        tot += bids[cards] * rank
        rank -= 1
    for cards in threes:
        tot += bids[cards] * rank
        rank -= 1
    for cards in twos:
        tot += bids[cards] * rank
        rank -= 1
    for cards in ones:
        tot += bids[cards] * rank
        rank -= 1
    for cards in highs:
        tot += bids[cards] * rank
        rank -= 1
    
    return tot

def part2(lines):
    return
    tot = 0
    fives = set()
    fours = set()
    fulls = set()
    threes = set()
    twos = set()
    ones = set()
    highs = set()
    
    bids = {}
    for l in lines:
        l = l.replace('A','E').replace('K','D').replace('Q','C').replace('J','1').replace('T','A')
        cards, bid = l.split()
        orig = cards
        
        counts = Counter(cards.replace('1',''))
        if len(counts) > 0:
            most_common, count = counts.most_common(1)[0]
        else:
            most_common = '1'
        if count == 1:
            most_common = sorted(cards)[-1]
        for i,c in enumerate(deepcopy(cards)):
            if c == '1':
                cards = cards[:i] + most_common + cards[i+1:]
        
        s = set(cards)
        if len(s) == 1:
            fives.add(orig)
        elif len(s) == 2:
            for card in s:
                if cards.count(card) == 4:
                    fours.add(orig)
                elif cards.count(card) == 3:
                    fulls.add(orig)
        elif len(s) == 3:
            for card in s:
                if cards.count(card) == 3:
                    threes.add(orig)
                elif cards.count(card) == 2:
                    twos.add(orig)
        elif len(s) == 4:
            ones.add(orig)
        elif len(s) == 5:
            highs.add(orig)
        
        bids[orig] = int(bid)
            
    fives = list(fives)
    fours = list(fours)
    fulls = list(fulls)
    threes = list(threes)
    twos = list(twos)
    ones = list(ones)
    highs = list(highs)
    
    fives.sort(reverse=True); fours.sort(reverse=True); fulls.sort(reverse=True); threes.sort(reverse=True); twos.sort(reverse=True); ones.sort(reverse=True); highs.sort(reverse=True)
    
    rank = len(lines)
    for cards in fives:
        tot += bids[cards] * rank
        rank -= 1
    for cards in fours:
        tot += bids[cards] * rank
        rank -= 1
    for cards in fulls:
        tot += bids[cards] * rank
        rank -= 1
    for cards in threes:
        tot += bids[cards] * rank
        rank -= 1
    for cards in twos:
        tot += bids[cards] * rank
        rank -= 1
    for cards in ones:
        tot += bids[cards] * rank
        rank -= 1
    for cards in highs:
        tot += bids[cards] * rank
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