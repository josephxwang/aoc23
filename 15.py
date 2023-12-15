from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), reduce, heappop/push, math, also dirs, adjs, letters, digits, symbols, also reverse, gok


def part1(lines):
    steps = lines[0].split(',')
    tot = 0
    for step in steps:
        curr = 0
        for c in step:
            curr = (curr+ord(c))*17%256
        tot += curr
    return tot

def part2(lines):
    # return
    steps = lines[0].split(',')
    boxs = [[] for _ in range(256)] # list of labels for each box
    ns = [{} for _ in range(256)] # hash map of lenses for each box
    for step in steps:
        if step[-1].isdigit(): # parse
            n = int(step[-1])
            op = step[-2]
            label = step[:-2]
        else:
            op = step[-1]
            label = step[:-1]
        i = 0 # box number
        for c in label:
            i = (i+ord(c))*17%256        
        if op == '-': # remove
            if label in boxs[i]:
                boxs[i].remove(label)
                ns[i].pop(label)
        elif op == '=':
            if label in boxs[i]:
                ns[i][label] = n
            else:
                boxs[i].append(label)
                ns[i][label] = n
    tot = 0
    for i,box in enumerate(boxs):
        for j,label in enumerate(box):
            tot += (i+1)*(j+1)*ns[i][label]
    return tot


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)