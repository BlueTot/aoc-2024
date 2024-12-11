data = "125 17".split(" ")
data = "5178527 8525 22 376299 3 69312 0 275".split(" ")

state = [int(i) for i in data]
numBlinks = 25

for _ in range(numBlinks):
    newState = []
    for num in state:
        if num == 0:
            newState.append(1)
        elif (length := len(str(num))) % 2 == 0:
            newState.append(int(str(num)[:length//2]))
            newState.append(int(str(num)[length//2:]))
        else:
            newState.append(num*2024)
    state = newState
print(len(state))