from utils import * 
# Counter, defaultdict, deque, heapify/pop/push (min heap)
# deepcopy, cache (@cache), reduce, math
# constants: dirs, adjs, alphabet (lowercase), digits, punctuation
# functions: reverse, gok, gflip, grotcw, grotccw, dfs, bfs, dijkstra

from sympy import symbols, Eq, solve

def part1(lines):
    lines = ints(lines)
    tot = 0
    for i,l in enumerate(lines):
        if i%10 == 0:
            print(i)
        px1,py1,_,vx1,vy1,_ = l
        for j in range(i,len(lines)): # all pairs
            px2,py2,_,vx2,vy2,_ = lines[j]
            if vy1/vx1 == vy2/vx2: # same slope
                continue
            n1,n2 = symbols('n1,n2')
            eq1 = Eq(px1+n1*vx1,px2+n2*vx2) # the two equations
            eq2 = Eq(py1+n1*vy1,py2+n2*vy2)
            res = solve((eq1,eq2),(n1,n2))
            if res[n1]<0 or res[n2]<0: # in past
                continue
            x = px1+res[n1]*vx1
            y = py1+res[n1]*vy1
            if 200000000000000<=x<=400000000000000 and 200000000000000<=y<=400000000000000:
            # if 7<=x<=27 and 7<=y<=27:
                tot += 1
    return tot

# !! this is tough

# !! I could start with a position along a single stone's at various times
# shifting other stones to match the time
# and then pick another stone and another time to make an intersection
# then see if that trajectory is valid
# but there are wayyy too many options

# !! or find one line that intersects three other lines?
# or 4
# or 6

def part2(lines): # !! I assume this will incorporate z
    lines = ints(lines)
    px1,py1,pz1,vx1,vy1,vz1 = lines[0]
    px2,py2,pz2,vx2,vy2,vz2 = lines[1]
    px3,py3,pz3,vx3,vy3,vz3 = lines[2]
    px,py,pz,vx,vy,vz = symbols('px,py,pz,vx,vy,vz',integer=True) # 9 variables
    t = symbols('t',positive=True)
    dt2,dt3 = symbols('dt2,dt3')
    eq1 = Eq(px+t*vx,px1+t*vx1)
    eq2 = Eq(py+t*vy,py1+t*vy1)
    eq3 = Eq(pz+t*vz,pz1+t*vz1)
    eq4 = Eq(px+(t+dt2)*vx,px2+(t+dt2)*vx2)
    eq5 = Eq(py+(t+dt2)*vy,py2+(t+dt2)*vy2)
    eq6 = Eq(pz+(t+dt2)*vz,pz2+(t+dt2)*vz2)
    eq7 = Eq(px+(t+dt3)*vx,px3+(t+dt3)*vx3)
    eq8 = Eq(py+(t+dt3)*vy,py3+(t+dt3)*vy3)
    eq9 = Eq(pz+(t+dt3)*vz,pz3+(t+dt3)*vz3)
    res = solve((eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9),(px,py,pz,vx,vy,vz,t,dt2,dt3),dict=True)
    res = res[0]
    return res[px]+res[py]+res[pz]


day = path.splitext(path.basename(__file__))[0]
ls = [l.strip() for l in open(f'{day}.in')]
p2 = part2(ls)
if p2:
    print(p2)
if not p2:
    p1 = part1(ls)
    print(p1)