from collections import Counter,defaultdict,deque # eg. d = defaultdict(list) then d['a'].append(n), or d = defaultdict(int) then d['a'] += 1 
from copy import deepcopy
from functools import cache,reduce # @cache decorator
from heapq import heapify,heappop,heappush # min heap (priority queue)
from os import path
# from tqdm import tqdm
import math # eg. math.gcd(x, y)
# import pyperclip
import re
import string
import sys # eg. sys.setrecursionlimit(3000)


# !! add topological sort
# !! rewrite dijkstra

# normal is for graph representation (adjacency list), g is for grid

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
            
def gdfs(g,r,c):
    s = [(r,c)]
    seen = set()
    while s:
        r,c = s.pop()
        if (r,c) in seen:
        # if g[r][c] == '':
            continue
        seen.add((r,c))
        # g[r][c] = ''
                
        # do something

        for dr,dc in dirs:
            if gok(g,r+dr,c+dc):
                s.append((r+dr,c+dc))
        
def bfs(graph,start):
    q = deque([start]) # changing to priority queue (if weighted graph) basically makes dijkstra
    seen = set()
    while q:
        curr = q.popleft()
        if curr in seen:
            continue
        seen.add(curr)

        # do something

        for nbr in graph[curr]:
            q.append(nbr)

def gbfs(g,r,c):
    q = deque([(r,c)])
    seen = set()
    while q:
        r,c = q.popleft()
        if (r,c) in seen:
        # if g[r][c] == '':
            continue
        seen.add((r,c))
        # g[r][c] = ''
                
        # do something

        for dr,dc in dirs:
            if gok(g,r+dr,c+dc):
                q.append((r+dr,c+dc))

def dijkstra(graph,start): # classic
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
def gdijkstra(g):
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
                heappush(q,(dist+g[r+dr][c+dc],r+dr,c+dc))


class Node:
    def __init__(self,val,l=None,r=None):
        self.val = val
        self.l = l
        self.r = r
        
    # def __repr__(self):
    #     return f'{self.val}:({self.l},{self.r})'

dirs = [(0,-1),(0,1),(-1,0),(1,0)]
adjs = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),(0,1),
    (1,-1),(1,0),(1,1)
]

alphabet = string.ascii_lowercase
ALPHABET = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

def isprime(n):
    if n == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def factors(n):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def pfactors(n): # prime factors
    pfactors = []
    for i in range(1,n+1):
        if n % i == 0 and isprime(i):
            pfactors.append(i)
    return pfactors

# # reverse any iterable
# def reverse(line):
#     return line[::-1]

def gok(grid,r,c): # grid ok
    return 0<=r<len(grid) and 0<=c<len(grid[0])

# # flip grid along diagonal
# def gflip(grid):
#     return list(map(list,zip(*grid)))

# rotate grid 90 deg clockwise
def grotcw(grid):
    return list(map(list,zip(*grid[::-1])))

# rotate grid 90 deg counterclockwise
def grotccw(grid):
    return list(map(list,zip(*grid)))[::-1]

# shoelace theorem, area of simple polygon (within it)
def shoelace(vertices: list[tuple[int]]):
    n = len(vertices)
    sum1 = sum2 = 0
    for i in range(n):
        x1,y1 = vertices[i]
        x2,y2 = vertices[(i+1)%n]
        sum1 += x1*y2
        sum2 += y1*x2
    return abs(sum1-sum2)//2

# Pick's theorem, interior and boundary points of a simple polygon given its area and boundary
def picks(area: int,boundaries: int):
    return area+boundaries//2+1

def intersect(line1: tuple[tuple[int]], line2: tuple[tuple[int]]): # each line as tuple of 2 points
    (x1,y1),(x2,y2) = line1
    (x3,y3),(x4,y4) = line2
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if denom == 0: # lines parallel
        return None
    x = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)) / denom
    y = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)) / denom
    return x,y

def overlap1d(range1: tuple[int], range2: tuple[int]): # 1D
    l = max(range1[0],range2[0])
    r = min(range1[1],range2[1])
    if l >= r:
        return None
    return l,r
    
def overlap2d(rect1: tuple[tuple[int]], rect2: tuple[tuple[int]]): # each rect as tuple of 2 points
    (r1x1,r1y1),(r1x2,r1y2) = rect1
    (r2x1,r2y1),(r2x2,r2y2) = rect2
    x1 = max(r1x1,r2x1)
    y1 = max(r1y1,r2y1)
    x2 = min(r1x2,r2x2)
    y2 = min(r1y2,r2y2)
    if x1 >= x2 or y1 >= y2:
        return None
    return (x1,y1),(x2,y2)

def overlap3d(cube1: tuple[tuple[int]], cube2: tuple[tuple[int]]): # each cube as tuple of 2 3D points
    (c1x1,c1y1,c1z1),(c1x2,c1y2,c1z2) = cube1
    (c2x1,c2y1,c2z1),(c2x2,c2y2,c2z2) = cube2
    x1 = max(c1x1,c2x1)
    y1 = max(c1y1,c2y1)
    z1 = max(c1z1,c2z1)
    x2 = min(c1x2,c2x2)
    y2 = min(c1y2,c2y2)
    z2 = min(c1z2,c2z2)
    if x1 >= x2 or y1 >= y2 or z1 >= z2:
        return None
    return (x1,y1,z1),(x2,y2,z2)

# get integers from lines
def ints(lines):
    ints = []
    for l in lines:
        ints.append(list(map(int,re.findall(r'-?\d+',l)))) # -? optional minus sign for negative numbers
    return ints

def words(lines):
    words = []
    for l in lines:
        words.append(re.findall(r'[a-zA-Z]+',l))
    return words

# parse grid as list of lists
def grid(lines,to_int=False):
    grid = []
    for l in lines:
        if to_int:
            l = map(int,list(l))
        grid.append(list(l))
    return grid,len(grid),len(grid[0])

# so many of these functions are written by sgpt lol