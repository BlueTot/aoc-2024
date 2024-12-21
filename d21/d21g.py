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
vals = {"A": 0, "<": 1, "^": 2, "v":3, ">":4}

def evaluation(code):
    return sum(1 if code[i] != code[i+1] else 0 for i in range(len(code)-1))

def orderEvaluation(code):
    return sum((1<<(len(code)-1-i)*vals[char] for i, char in enumerate(code)))

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

def getBestPathOnGrid(start, end, valids):
    paths = getPathOnGrid(start, end, valids)
    hvals = {(npath := path + "A"): evaluation(npath) for path in paths}
    minimum = min(hvals.values())
    paths2 = set(k for k, v in hvals.items() if v == minimum)
    hvals2 = {path : orderEvaluation(path) for path in paths2}
    minimum2 = min(hvals2.values())
    return [k for k, v in hvals2.items() if v == minimum2][0]

@lru_cache
def getBestNumericPath(start, end):
    return getBestPathOnGrid(start, end, numerics)

@lru_cache
def getBestRobotPath(start, end):
    return getBestPathOnGrid(start, end, robotPad)

@lru_cache
def controlNumeric(code):
    output = ""
    code = "A" + code
    for i in range(len(code)-1):
        output += getBestNumericPath(numericsBackwards[code[i]], numericsBackwards[code[i+1]])
    return output

@lru_cache
def controlRobot(code):
    output = ""
    code = "A" + code
    for i in range(len(code)-1):
        output += getBestRobotPath(robotPadBackwards[code[i]], robotPadBackwards[code[i+1]])
    return output

total = 0
for code in data:
    curr = controlNumeric(code)
    for _ in range(2):
        curr = controlRobot(curr)
        print(_, len(curr))
    numericPart = int(code[:-1])
    length = len(curr)
    print(numericPart, length)
    total += numericPart*length
print(total)

