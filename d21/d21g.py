data = """029A
980A
179A
456A
379A""".splitlines()

data = """319A
085A
143A
286A
789A""".splitlines()

from collections import deque
from functools import lru_cache

numerics = {(0, 0) : "7", (0, 1): "8", (0, 2): "9", (1, 0): "4", (1, 1): "5", (1, 2): "6", (2, 0): "1", (2, 1): "2", (2, 2): "3", (3, 1):  "0", (3, 2): "A"}
numericsBackwards = {"0": (3, 1), "1": (2, 0), "2": (2, 1), "3": (2, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (0, 0), "8": (0, 1), "9": (0, 2), "A": (3, 2)}
robotPad = {(0, 1): "^", (0, 2): "A", (1, 0): "<", (1, 1): "v", (1, 2): ">"}
robotPadBackwards = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}
dirs = {(-1, 0) : "^", (1, 0): "v", (0, 1): ">", (0, -1): "<"}

def getPathOnGrid(start, end, valids):
    queue = deque([(start, "", set())])
    paths = set()
    minDist = float("inf")
    while queue:
        curr, path, beenbefore = queue.popleft()
        if curr == end and len(path) <= minDist:
            minDist = len(path)
            paths.add(path)
        if len(path) > minDist:
            continue
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = curr[0]+dr, curr[1]+dc
            if (nr, nc) in valids and (nr, nc) not in beenbefore:
                queue.append(((nr, nc), path+dirs[(dr, dc)], beenbefore | set([(nr, nc)])))
    return paths

@lru_cache
def controlNumeric(code):
    if len(code) == 1:
        return set(poss + "A" for poss in getPathOnGrid(numericsBackwards["A"], numericsBackwards[code[0]], numerics))
    poss = set()
    for pastPoss in controlNumeric(code[:-1]):
        for nextCont in getPathOnGrid(numericsBackwards[code[-2]], numericsBackwards[code[-1]], numerics):
            poss.add(pastPoss + nextCont + "A")
    return poss

@lru_cache
def controlRobot(code):
    if len(code) == 1:
        return set(poss + "A" for poss in getPathOnGrid(robotPadBackwards["A"], robotPadBackwards[code[0]], robotPad))
    poss = set()
    for pastPoss in controlRobot(code[:-1]):
        for nextCont in getPathOnGrid(robotPadBackwards[code[-2]], robotPadBackwards[code[-1]], robotPad):
            poss.add(pastPoss + nextCont + "A")
    return poss

def heuristic(a, b):
    sq1, sq2 = robotPadBackwards[a], robotPadBackwards[b]
    return abs(sq1[0]-sq2[0])+abs(sq1[1]-sq2[1])

def evaluation(code):
    return sum(heuristic(code[i], code[i+1]) for i in range(len(code)-1))

def getMinRobotSeqs(prevs):
    nexts = set()
    for prev in prevs:
        for poss in controlRobot(prev):
            nexts.add(poss)
    minLength = min(len(poss) for poss in nexts)
    return set(poss for poss in nexts if len(poss) == minLength)

def getMinRobotHs(prevs):
    hvals = {k : evaluation(k) for k in getMinRobotSeqs(prevs)}
    minimum = min(hvals.values())
    return set(k for k, v in hvals.items() if v == minimum)

total = 0
for code in data:
    curr = controlNumeric(code)
    for _ in range(2):
        print(_)
        curr = getMinRobotHs(curr)
    numericPart = int(code[:-1])
    minLength = min(len(i) for i in curr)
    print(numericPart, minLength)
    total += numericPart*minLength
print(total)

