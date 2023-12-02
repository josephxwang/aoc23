from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,


# 12 red cubes, 13 green cubes, and 14 blue cubes
def part1(lines):
    # lines = ints(lines)
    lines = words(lines)
    sum = 0
    for l in lines:
        id = int(l[1][:-1])
        ok = True
        for i in range(2, len(l), 2):
            n = int(l[i])
            c = l[i+1][0]
            if n > {'r':12,'g':13,'b':14}.get(c):
                ok = False
                break
        if ok:
            sum += id
    return sum

# !! old
# def part1(lines):
#     # lines = ints(lines)
#     lines = words(lines)
#     sum = 0
#     for l in lines:
#         id = int(l[1][:-1])
#         ok = True
#         for i in range(2, len(l), 2):
#             n = int(l[i])
#             c = l[i+1][0]
#             if c == "r" and n > 12:
#                 ok = False
#                 break
#             if c == "g" and n > 13:
#                 ok = False
#                 break
#             if c == "b" and n > 14:
#                 ok = False
#                 break
#         if ok:
#             sum += id
#     return sum

# sum of the power
def part2(lines):
    # return
    lines = words(lines)
    sum = 0
    for l in lines:
        m = defaultdict(int)
        for i in range(2, len(l), 2):
            n = int(l[i])
            c = l[i+1][0]
            m[c] = max(m[c], n)
        sum += math.prod(m.values())
    return sum

# def part2(lines):
#     # return
#     lines = words(lines)
#     sum = 0
#     for l in lines:
#         m = {'r':0,'g':0,'b':0}
#         for i in range(2, len(l), 2):
#             n = int(l[i])
#             c = l[i+1][0]
#             if n > m.get(c):
#                 m[c] = n
#         sum += math.prod(m.values())
#     return sum

# !! old
# def part2(lines):
#     # return
#     lines = words(lines)
#     sum = 0
#     for l in lines:
#         rm = gm = bm = 0
#         for i in range(2, len(l), 2):
#             n = int(l[i])
#             c = l[i+1][0]
#             if c == "r" and n > rm:
#                 rm = n
#             if c == "g" and n > gm:
#                 gm = n
#             if c == "b" and n > bm:
#                 bm = n
#         sum += rm*gm*bm
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