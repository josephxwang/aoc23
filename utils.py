from collections import Counter, defaultdict, deque
# eg. d = defaultdict(list) then d['a'].append(n), or d = defaultdict(int) then d['a'] += 1 

from copy import deepcopy
from functools import cache # @cache decorator
from heapq import heapify, heappop, heappush # min heap

from os import path

import math # eg. math.gcd(x, y)
import pyperclip
import re
import string
import sys # eg. sys.setrecursionlimit(3000)

letters = string.ascii_lowercase
digits = string.digits

# Get integers from lines
def ints(ls):
    ints = []
    for l in ls:
        ints.append(list(map(int, re.findall(r"-?\d+", l))))
    return ints

def dfs(graph, curr):
    s = [curr]
    visited = set()
    while s:
        curr = s.pop()
        if curr in visited:
            continue
        visited.add(curr)
                
        # Do something
        print(curr)

        for nbr in graph[curr]:
            s.append(nbr)
        
def bfs(graph, curr):
    q = deque([curr])
    visited = set()
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        visited.add(curr)
                
        # Do something
        print(curr)

        for nbr in graph[curr]:
            q.append(nbr)