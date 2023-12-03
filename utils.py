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

dirs = [(0,-1),(0,1),(-1,0),(1,0)]
adjs = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),(0,1),
    (1,-1),(1,0),(1,1)
]

letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Get integers from lines
def ints(lines):
    ints = []
    for l in lines:
        ints.append(list(map(int, re.findall(r"-?\d+", l))))
    return ints

def words(lines):
    return [l.split() for l in lines]

def grid(lines):
    grid = []
    for l in lines:
        grid.append(list(l))
    return grid

def gok(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def dfs(graph, curr):
    stack = [curr]
    visited = set()
    while stack:
        curr = stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
                
        # Do something
        print(curr)

        for nbr in graph[curr]:
            stack.append(nbr)
        
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