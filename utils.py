from collections import Counter, defaultdict, deque
# eg. d = defaultdict(list) then d['a'].append(n), or d = defaultdict(int) then d['a'] += 1 

from copy import deepcopy
from functools import cache # @cache decorator
from heapq import heapify, heappop, heappush # min heap

from os import path
# from tqdm import tqdm

import math # eg. math.gcd(x, y)
# import pyperclip
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

# reverse any iterable
def reverse(line):
    return line[::-1]

# get integers from lines
def ints(lines):
    ints = []
    for l in lines:
        ints.append(list(map(int, re.findall(r'-?\d+',l))))
    return ints

def words(lines):
    words = []
    for l in lines:
        words.append(re.findall(r'-?[a-zA-Z]+',l))
    return words

# parse grid as list of lists
def grid(lines):
    grid = []
    for l in lines:
        grid.append(list(l))
    return grid

def gok(grid, r, c):
    return 0<=r<len(grid) and 0<=c<len(grid[0])

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

def dijkstra(graph, start):
    n = len(graph)
    dists = [float("inf")]*n
    parents = [-1]*n
    
    dists[start] = 0
    q = [(0, start)] # use heap (priority queue), formatted (dist, node)
    while q:
        dist, curr = heappop(q)
        if dist == dists[curr]:
            for nbr, weight in graph[curr]: # formatted (node, weight)
                if weight + dist < dists[nbr]:
                    dists[nbr] = weight + dist
                    parents[nbr] = curr
                    heappush(q, (dists[nbr], nbr))
    return dists, parents