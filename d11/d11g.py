data = "125 17".split(" ")
data = "5178527 8525 22 376299 3 69312 0 275".split(" ")
numBlinks = 75

class MultiSet:
    def __init__(self):
        self.__set = {}
    
    def add_item(self, item, times=1):
        if item not in self.__set:
            self.__set[item] = times
        else:
            self.__set[item] += times
    
    def get_length(self):
        return sum(self.__set.values())
    
    def items(self):
        for k, v in self.__set.items():
            yield k, v
    
    def __repr__(self):
        return str(self.__set)

state = MultiSet()
for s in data:
    state.add_item(int(s))

for _ in range(numBlinks):
    newState = MultiSet()
    for num, times in state.items():
        if num == 0:
            newState.add_item(1, times)
        elif (length := len(str(num))) % 2 == 0:
            newState.add_item(int(str(num)[:length//2]), times)
            newState.add_item(int(str(num)[length//2:]), times)
        else:
            newState.add_item(num*2024, times)
    state = newState
print(state.get_length())