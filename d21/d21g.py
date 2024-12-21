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

# Setting up the grids for the search
numerics = {(0, 0) : "7", (0, 1): "8", (0, 2): "9", (1, 0): "4", (1, 1): "5", (1, 2): "6", (2, 0): "1", (2, 1): "2", (2, 2): "3", (3, 1):  "0", (3, 2): "A"}
numericsBackwards = {"0": (3, 1), "1": (2, 0), "2": (2, 1), "3": (2, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (0, 0), "8": (0, 1), "9": (0, 2), "A": (3, 2)}
robotPad = {(0, 1): "^", (0, 2): "A", (1, 0): "<", (1, 1): "v", (1, 2): ">"}
robotPadBackwards = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}
dirs = {(-1, 0) : "^", (1, 0): "v", (0, 1): ">", (0, -1): "<"}
vals = {"A": 0, "<": 1, "^": 2, "v":3, ">":4}

# Minimum turns heuristic
def evaluation(code):
    return sum(1 if code[i] != code[i+1] else 0 for i in range(len(code)-1))

# Directin heuristic (< then ^ then v then >
def orderEvaluation(code):
    return sum((1<<(len(code)-1-i)*vals[char] for i, char in enumerate(code)))

# Use BFS to get the possible paths from start to end on a given board (numeric or robot)
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

# Sort through all paths gathered, and apply the minimum corners heuristic and direction preference heuristic
def getBestPathOnGrid(start, end, valids):
    paths = getPathOnGrid(start, end, valids)
    hvals = {(npath := path + "A"): evaluation(npath) for path in paths}
    minimum = min(hvals.values())
    paths2 = set(k for k, v in hvals.items() if v == minimum)
    hvals2 = {path : orderEvaluation(path) for path in paths2}
    minimum2 = min(hvals2.values())
    return [k for k, v in hvals2.items() if v == minimum2][0]

# Get best numeric pad path
@lru_cache
def getBestNumericPath(start, end):
    return getBestPathOnGrid(start, end, numerics)

# Get best robot path
@lru_cache
def getBestRobotPath(start, end):
    return getBestPathOnGrid(start, end, robotPad)

# First convert the numeric pad into a sequence of arrow moves for first robot
@lru_cache
def controlNumeric(code):
    output = ""
    code = "A" + code
    for i in range(len(code)-1):
        if code[i] != code[i+1]:
            output += getBestNumericPath(numericsBackwards[code[i]], numericsBackwards[code[i+1]])
    return output

# Assuming we start with an A, get the next robot's sequence of moves for this segment
@lru_cache
def controlRobotSegment(code):
    output = []
    for i in range(len(code)-1):
        output.append(getBestRobotPath(robotPadBackwards[code[i]], robotPadBackwards[code[i+1]]))
    return output

# Function used to get the sequence after numRobots turns are passed
def sequence(code, numRobots):
    output = {}
    for i in range(numRobots+1):
        if i == 0:
            ncode = "A" + code
            for i in range(len(ncode)-1):
                for seg in controlRobotSegment(ncode[i:i+2]):
                    if seg not in output:
                        output[seg] = 1
                    else:
                        output[seg] += 1
        else:
            newOutput = {}
            for segment, times in output.items():
                for seg in controlRobotSegment("A" + segment):
                    if seg not in newOutput:
                        newOutput[seg] = times
                    else:
                        newOutput[seg] += times
            output = newOutput
    return output

total = 0
for code in data:
    curr = controlNumeric(code)
    curr = sequence(curr, 25)
    numericPart = int(code[:-1])
    length = sum(curr.values())
    total += numericPart*length
print(total)

