# data = """Register A: 10
# Register B: 0
# Register C: 0

# Program: 5,0,5,1,5,4""".split("\n\n")

data = """Register A: 48744869
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0""".split("\n\n")

# data = """Register A: 117440
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0""".split("\n\n")

import re

registers = [int(re.findall(r"\d+", row)[0]) for row in data[0].splitlines()]
program = [*map(int, re.findall(r"\d+", data[1]))]

def checkProgram(registers, program, target):

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
                if len(output) > len(target):
                    return False, output
                if output[-1] != target[len(output)-1]:
                    return False, output
                pc += 2
            case 6:
                registers[1] = registers[0] >> comboOperand(operand)
                pc += 2
            case 7:
                registers[2] = registers[0] >> comboOperand(operand)
                pc += 2
    return output == target, output

# print(target)
# print()
for num in range(0, 40000000, 4):
    check, output = checkProgram([num, 0, 0], program[:], program[:])
    if output[0] == 2 and output[1] == 4 and output[2] == 1 and output[3] == 2 and output[4] == 7 and output[5] == 5 and output[6] == 1:
        print(num, bin(num), output)
        with open("d17/analysis3.txt", "a") as f:
            f.write(f"{num}, {bin(num)}, {output}\n")
    if check:
        print("We FOUND IT")
        print(num)
        break
    
    # if (output := runProgram([num, 0, 0], program[:])) == target:
    #     print(num)
    #     print(output)
    # print(runProgram(registers[:], program[:]))