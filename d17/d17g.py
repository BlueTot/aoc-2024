data = """Register A: 48744869
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0""".split("\n\n")

import re

registers = [int(re.findall(r"\d+", row)[0]) for row in data[0].splitlines()]
program = [*map(int, re.findall(r"\d+", data[1]))]

# function that emulates the program
def runProgram(registers, program):

    def comboOperand(num):
        if 0 <= num <= 3:
            return num
        elif 4 <= num <= 6:
            return registers[num - 4]
        else:
            raise Exception("this should not happen!")

    output = []
    pc = 0
    while pc < len(program):
        opcode, operand = program[pc], program[pc+1]
        match opcode:
            case 0:
                registers[0] >>= comboOperand(operand)
                pc += 2
            case 1:
                registers[1] ^= operand
                pc += 2
            case 2:
                registers[1] = comboOperand(operand) % 8
                pc += 2
            case 3:
                if registers[0] != 0:
                    pc = operand
                else:
                    pc += 2
            case 4:
                registers[1] ^= registers[2]
                pc += 2
            case 5:
                output.append(comboOperand(operand) % 8)
                pc += 2
            case 6:
                registers[1] = registers[0] >> comboOperand(operand)
                pc += 2
            case 7:
                registers[2] = registers[0] >> comboOperand(operand)
                pc += 2
    return output

# backtracking method that finds the right numbers from the back to the front
# motivation: the last number in the program is only affected by the last 3 bits of the answer, so we go from back to front
def searchNum(nums):
    if not nums:
        return [0]
    poss = []
    for curr in searchNum(nums[1:]):
        for next in range(8):
            output = runProgram([nnum := (curr << 3) + next, 0, 0], program[:])
            if output == nums:
                poss.append(nnum)
    return poss

found = searchNum(program[:])
print(min(found))