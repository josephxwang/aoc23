from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,

day = path.splitext(path.basename(__file__))[0]

# first digit and the last digit
def part1(lines):  
    sum = 0
    for line in lines:
        ns = [c for c in line if c.isdigit()]
        sum += int(ns[0]+ns[-1])
    return sum

# !! old
# def part1(lines):  
#     sum = 0
#     for line in lines:
#         for c in line:
#             if c.isdigit():
#                 l = c
#                 break
#         for c in line[::-1]:
#             if c.isdigit():
#                 r = c
#                 break
#         sum += int(l+r)
#     return sum

def part2(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace("one","one1one").replace("two","two2two").replace("three","three3three").replace("four","four4four").replace("five","five5five").replace("six","six6six").replace("seven","seven7seven").replace("eight","eight8eight").replace("nine","nine9nine")
        
    sum = 0
    for line in lines:
        ns = [c for c in line if c.isdigit()]
        sum += int(ns[0]+ns[-1])
    return sum

# !! old
# def part2(lines):
#     # return
#     ns = {
#         "one": "1",
#         "two": "2",
#         "three": "3",
#         "four": "4",
#         "five": "5",
#         "six": "6",
#         "seven": "7",
#         "eight": "8",
#         "nine": "9"
#     }        
#     sum = 0
#     for line in lines:
#         found_l = False
#         found_r = False
#         for i in range(len(line)):
#             if line[i] in digits:
#                 l = line[i]
#                 break
#             for n in ns:
#                 if line[i:].startswith(n):
#                     l = ns[n]
#                     found_l = True
#                     break
#             if found_l:
#                 break
        
#         for i in range(len(line)-1, -1, -1):
#             if line[i] in digits:
#                 r = line[i]
#                 break
#             for n in ns:
#                 if line[:i+1].endswith(n):
#                     r = ns[n]
#                     found_r = True
#                     break
#             if found_r:
#                 break
#         sum += int(l+r)
#     return sum


ls = [l.strip() for l in open(f"{day}.in")]

p2 = part2(ls)
if p2:
    print(p2)
    pyperclip.copy(p2)

if not p2:
    p1 = part1(ls)
    print(p1)
    pyperclip.copy(p1)