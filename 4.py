from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols


# first match makes the card worth one point and each match after the first doubles the point value of that card

def part1(lines):
    sum = 0
    for l in lines:
        x, y = l.split('|')
        x = x.split()
        y = y.split()
        n = len(set(x) & set(y))
        if n > 0:
            sum += 2**(n-1)
    return sum

# def part1(lines):
#     lines = ints(lines)
#     sum = 0
#     for l in lines:
#         n = 0
#         w = set()
#         for i in range(1,11):
#             w.add(l[i])
#         for i in range(11,len(l)):
#             if l[i] in w:
#                 n += 1
#         if n > 0:
#             sum += 2**(n-1)
#     return sum

def part2(lines):
    # return
    m = defaultdict(int) # number of each card
    for i, l in enumerate(lines):
        m[i] += 1
        x, y = l.split('|')
        x = x.split()
        y = y.split()
        n = len(set(x) & set(y))
        for j in range(n):
            m[i+j+1] += m[i]
    return sum(m.values())

# def part2(lines):
#     lines = ints(lines)
#     sum = 0
#     m = defaultdict(int)
#     for i, l in enumerate(lines):
#         m[i+1] += 1
#         for k in range(m[i+1]):
#             score = 0
#             w = set()
#             for j in range(1,11):
#                 w.add(l[j])
#             for j in range(11,len(l)):
#                 if l[j] in w:
#                     score += 1
#             for j in range(1, score+1):
#                 m[i+j+1] += 1
#             sum += 1
#     return sum


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