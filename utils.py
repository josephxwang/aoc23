from collections import Counter,defaultdict,deque
# eg. d = defaultdict(list) then d['a'].append(n), or d = defaultdict(int) then d['a'] += 1 

from copy import deepcopy
from functools import cache,reduce # @cache decorator
from heapq import heapify,heappop,heappush # min heap

from os import path
# from tqdm import tqdm

import math # eg. math.gcd(x, y)
# import pyperclip
import re
import string
import sys # eg. sys.setrecursionlimit(3000)

# normal is for graph representation (edge list), 2 is for grid

def dfs(graph,start):
    s = [start]
    seen = set()
    while s:
        curr = s.pop()
        if curr in seen:
            continue
        seen.add(curr)
                
        # do something

        for nbr in graph[curr]:
            s.append(nbr)
            
def dfs2(g,r,c):
    s = [(r,c)]
    seen = set()
    while s:
        r,c = s.pop()
        if (r,c) in seen:
            continue
        seen.add((r,c))
                
        # do something

        for dr,dc in dirs:
            if gok(g,r+dr,c+dc):
                s.append((r+dr,c+dc))
        
def bfs(graph,start):
    q = deque([start]) # changing to priority queue (if a weighted graph) basically makes dijkstra
    seen = set()
    while q:
        curr = q.popleft()
        if curr in seen:
            continue
        seen.add(curr)

        # do something

        for nbr in graph[curr]:
            q.append(nbr)

def bfs2(g,r,c):
    q = deque([(r,c)])
    seen = set()
    while q:
        r,c = q.popleft()
        if (r,c) in seen:
            continue
        seen.add((r,c))
                
        # do something

        for dr,dc in dirs:
            if gok(g,r+dr,c+dc):
                q.append((r+dr,c+dc))

def dijkstra(graph,start):
    n = len(graph)
    dists = [float('inf')]*n
    parents = [-1]*n
    
    dists[start] = 0
    q = [(0,start)] # heap (priority queue), formatted (dist,node)
    while q:
        dist,curr = heappop(q)
        if dist == dists[curr]:
            for nbr,weight in graph[curr]: # formatted (node,weight)
                if weight+dist < dists[nbr]:
                    dists[nbr] = weight+dist
                    parents[nbr] = curr
                    heappush(q,(dists[nbr],nbr))
    return dists,parents

# dijkstra more simply, for a grid
def dijkstra2(g):
    R = len(g)
    C = len(g[0])
    q = [(0,0,0)] # (dist,r,c), start at top left, no cost to get there
    seen = set()
    while q:
        dist,r,c = heappop(q) # priority queue (heap)
        if (r,c) == (R-1,C-1): # lower right
            return dist
        if (r,c) in seen:
            continue
        seen.add((r,c))
        for dr,dc in dirs:
            if gok(g,r+dr,c+dc):
                heappush(q,(dist+int(g[r+dr][c+dc]),r+dr,c+dc))

dirs = [(0,-1),(0,1),(-1,0),(1,0)]
adjs = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),(0,1),
    (1,-1),(1,0),(1,1)
]

alphabet = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation

# reverse any iterable
def reverse(line):
    return line[::-1]

def gok(grid,r,c): # grid ok
    return 0<=r<len(grid) and 0<=c<len(grid[0])

# flip grid along diagonal
def gflip(grid):
    return list(map(list,zip(*grid)))

# rotate grid 90 deg clockwise
def grotcw(grid):
    return list(map(list,zip(*grid[::-1])))

# rotate grid 90 deg counterclockwise
def grotccw(grid):
    return list(map(list,zip(*grid)))[::-1]
                
# shoelace theorem, area of simple polygon (within it)
def shoelace(vertices):
    n = len(vertices)
    sum1 = sum2 = 0
    for i in range(n):
        x1,y1 = vertices[i]
        x2,y2 = vertices[(i+1)%n]
        sum1 += x1*y2
        sum2 += y1*x2
    return abs(sum1-sum2)/2

# Pick's theorem, area of simple polygon, given number of points interior to it and on its boundary
def picks(interiors,boundaries):
    return interiors+boundaries/2-1

# get integers from lines
def ints(lines):
    ints = []
    for l in lines:
        ints.append(list(map(int,re.findall(r'-?\d+',l)))) # -? optional minus sign for negative numbers
    return ints

def words(lines):
    words = []
    for l in lines:
        words.append(re.findall(r'-?[a-zA-Z]+',l))
    return words

# parse grid as list of lists
def grid(lines,to_int=False):
    grid = []
    for l in lines:
        if to_int:
            l = map(int,list(l))
        grid.append(list(l))
    return grid,len(grid),len(grid[0])