from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap/priority queue)
# deepcopy, cache (@cache), reduce, math
# consts: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: gok, gflip, grotcw, grotccw, shoelace, picks
# graphs (grid): dfs (dfs2), bfs (bfs2), dijkstra (dijkstra2)


# !! this isn't cacheable because the parameters always change

# !! maybe I do need to do interval math... find all the different relevant values for x,m,a,s and test

# !! also I should probably pre-parse the decision tree... was too lazy to last night
# !! wow, that still isn't fast enough

# !! next year get a powerfully computing machine lol

# !! try getting rid of eval
# so much faster without eval

# !! try collapsing rules that have double A,A results or double R,R results, even if eventual
# done, could collapse even further, propogate up to parent rules

# !! this might now solve overnight, actually, current eta is 22.5 hours

# def parse(rules):

class Node:
    def __init__(self,val,l,r):
        self.val = val
        self.l = l
        self.r = r
        
    def __repr__(self):
        return f'({self.val}:{self.l},{self.r})'

# @cache
# def r(x,m,a,s,curr='in'):
#     if curr == 'A':
#         return True
#     elif curr == 'R':
#         return False
#     if curr in rules: # new rule
#         curr,next = rules[curr].split(':',1)
#     else: # still within a rule
#         curr,next = curr.split(':',1)
#     if eval(curr):
#         return r(x,m,a,s,next.split(',',1)[0])
#     else:
#         return r(x,m,a,s,next.split(',',1)[1])
    
def r(x,m,a,s,curr='in'):
    if curr == 'A':
        return True
    elif curr == 'R':
        return False
    if type(curr) == Node: # expression
        letter = curr.val[0]
        symb = curr.val[1]
        n = int(curr.val[2:])
        d = {'x':x,'m':m,'a':a,'s':s}
        # if eval(curr.val):
        if symb == '>':
            if d[letter] > n:
                return r(x,m,a,s,curr.l)
            else:
                return r(x,m,a,s,curr.r)
        elif symb == '<':
            if d[letter] < n:
                return r(x,m,a,s,curr.l)
            else:
                return r(x,m,a,s,curr.r)
    return r(x,m,a,s,rules[curr]) # name
    
def parse(s):
    expr,s = s.split(':',1)
    l,r = s.split(',',1)
    if ':' in r: # recursive node
        r = parse(r)
    if l in rules and type(rules[l]) == str: # !! don't help?
        l = rules[l]
    if r in rules and type(rules[r]) == str:
        r = rules[r]
    if l == r:
        return r
    conds.append(expr)
    return Node(expr,l,r)

def part1(lines):
    global rules
    rules = {}
    parts = []
    ok = True
    for l in lines:
        if l == '': # delimiter
            ok = False
            continue
        if ok:
            rule,s = l.split('{')
            rules[rule] = parse(s[:-1]) # build tree
        else:
            parts.append(list(map(int,re.findall(r'-?\d+',l)))) # find ints
    print(len(rules))
    tot = 0
    for part in parts:
        if r(*part):
            tot += sum(part)
    return tot

# !! I'm in the right order of magnitude, but still not right

def part2(lines):
    # return
    global rules,conds
    rules = {}
    ok = True
    xmas = [[],[],[],[]]
    st = 'xmas'
    conds = [] # parse all conditions
    for l in lines:
        if l == '':
            ok = False
            break
        if ok:
            rule,s = l.split('{')
            rules[rule] = parse(s[:-1])    
    # for steps in rules.values():
    #     steps = steps.split(',')
    #     for step in steps:
    #         if ':' in step:
    #             conds.append(step.split(':')[0])
    for cond in conds:
        c = cond[0]
        n = int(cond[2:])
        xmas[st.index(c)] += [n-1,n]
    for l in xmas: # !! this works because of pass by reference
        l += [0,4000] # bounds
        l.sort()
    tot = 0
    # print(len(xmas[0]))
    print(len(xmas[1]))
    # print(len(xmas[2]))
    # print(len(xmas[3]))
    for mi in range(1,len(xmas[1])): # rearranged so slightly faster?
        print(mi)
        for ai in range(1,len(xmas[2])):
            # print(ai)
            for xi in range(1,len(xmas[0])):
                for si in range(1,len(xmas[3])):
                    if r(xmas[0][xi],xmas[1][mi],xmas[2][ai],xmas[3][si]):
                        tot += (xmas[0][xi]-xmas[0][xi-1])*(xmas[1][mi]-xmas[1][mi-1])*(xmas[2][ai]-xmas[2][ai-1])*(xmas[3][si]-xmas[3][si-1])
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)