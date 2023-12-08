from utils import * # Counter, defaultdict, deque, deepcopy, cache (@cache), math, sys, also gok(grid,r,c), dirs, adjs, letters, digits, symbols


def part1(lines):
    lines = words(lines)
    insts = lines[0][0]
    lines = lines[2:]
    m = {}
    for node,l,r in lines:
        m[node] = (l,r)
    s = 'AAA'
    for i in range(100000):
        inst = insts[i%len(insts)]
        if s == 'ZZZ':
            return i
        if inst == 'R':
            s = m[s][1]
        elif inst == 'L':
            s = m[s][0]

def part2(lines):
    # return
    lines = words(lines)
    insts = lines[0][0]
    lines = lines[2:]
    m = {}
    nodes = []
    for node,l,r in lines:
        m[node] = (l,r)
        if node.endswith('A'):
            nodes.append(node)
    firsts = defaultdict(int)
    for i in range(100000):
        inst = insts[i%len(insts)]
        for j,node in enumerate(deepcopy(nodes)):
            if node.endswith('Z'):
                if firsts[j] == 0:
                    firsts[j] = i
            if inst == 'R':
                nodes[j] = m[node][1]
            elif inst == 'L':
                nodes[j] = m[node][0]
    return math.lcm(*firsts.values()) # for some reason the input works with just lcm

    # for i in range(1,100000000000):
    #     ok = True
    #     for node,dests in firsts.items():
    #         ok_one = False
    #         for node,data in dests.items():
    #             if (i-data[0]) % data[1] == 0: # apparently you can also use Chinese remainder theorem?
    #                 ok_one = True
    #                 break
    #         if not ok_one:
    #             ok = False
    #     if ok:
    #         return i


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)