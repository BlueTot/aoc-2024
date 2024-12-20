data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".splitlines()

data = [[i for i in row] for row in data]

from collections import deque

for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == "S":
            start = (r, c)
        if char == "E":
            end = (r, c)

def shortestTime(data, start, end):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        curr, moves = queue.popleft()
        if curr == end:
            return moves
        if curr in visited:
            continue
        visited.add(curr)
        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nr, nc = curr[0]+dr, curr[1]+dc
            if 0<=nr<len(data) and 0<=nc<len(data[0]) and (nr, nc) not in visited:
                if data[nr][nc] != "#" and (data[r][c] != "2" or data[r][c] == "2" and data[nr][nc] != "1"):
                    queue.append(((nr, nc), moves+1))

shortest = shortestTime(data, start, end)
cheats = {}
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == "#":
            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                er, ec = r+dr, c+dc
                if 0<=er<len(data) and 0<=ec<len(data[0]) and data[er][ec] != "#":
                    data[r][c] = "1"
                    origsecond = data[er][ec]
                    data[er][ec] = "2"
                    newTime = shortestTime(data, start, end)
                    data[r][c] = "#"
                    data[er][ec] = origsecond
                    if newTime is None:
                        print(r, c)
                        continue
                    saving = shortest - newTime
                    if saving == 64:
                        print(r, c, er, ec)
                    if saving > 0:
                        if saving not in cheats:
                            cheats[saving] = 1
                        else:
                            cheats[saving] += 1
                '''
                if 0<=er<len(data) and 0<=ec<len(data[0]) and (t := tuple(sorted([(r, c), (er, ec)]))) not in seen:
                    seen.add(t)
                    data[r][c] = "."
                    isWall = data[er][ec] == "#"
                    if isWall:
                        data[er][ec] = "."
                    saving = shortest - shortestTime(data, start, end)
                    if saving == 64:
                        for r in range(len(data)):
                            for c in range(len(data[0])):
                                print(data[r][c], end="")
                            print()
                        print(r, c, er, ec)
                    data[r][c] = "#"
                    if isWall:
                        data[er][ec] = "#"
                    if saving > 0:
                        if saving not in cheats:
                            cheats[saving] = 1
                        else:
                            cheats[saving] += 1'''
print(cheats)

