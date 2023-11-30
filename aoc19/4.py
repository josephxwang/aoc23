from utils import * # deque, Counter, defaultdict, cache (@cache), math, sys, also ints(ls), letters, digits,
from os import path

day = path.splitext(path.basename(__file__))[0]

# !! there are more efficient solutions
# such as using sort to check non-decreasing condition
# and then counting number of each digits (need one to be 2)

def solve(ls):
    count = 0
    n1, n2 = map(int, ls[0].split("-"))
    for n in range(n1, n2+1):
        s = str(n)
        isValid = True
        for i in range(1, len(s)):
            if s[i-1] > s[i]:
                isValid = False
                break
        
        hasAdj = False
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                hasAdj = True
        
        if isValid and hasAdj:
            count += 1
            
    return count

def solve2(ls):
    count = 0
    n1, n2 = map(int, ls[0].split("-"))
    for n in range(n1, n2+1):
        s = str(n)
        isValid = True
        for i in range(1, len(s)):
            if s[i-1] > s[i]:
                isValid = False
                break
        
        hasAdj = False
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                if 0 <= i-2 and s[i-2] == s[i-1]:
                    continue
                if i+1 < len(s) and s[i] == s[i+1]:
                    continue
                hasAdj = True
        
        if isValid and hasAdj:
            count += 1
            
    return count

ls = [l.strip() for l in open(f"{day}.in")]
print(solve(ls))
print(solve2(ls))