import re

registers = {}
count = len(registers)
output = []

def fileread():
    f = open('code_gen_input.txt', 'r')
    lines = f.read().splitlines()
    return lines

def save_to_file():
    f = open('code_gen_output.txt', 'w')
    for code in output:
        f.writelines(code + '\n')

def assign_reg(operand):
    global count

    if operand in registers.values():
        for key, value in registers.items():
            if operand == value:
                return key
    else:
        reg_name = 'R' + str(count)
        registers['R' + str(count)] = operand
        output.append('MOV ' + operand + ', ' + 'R' + str(count))
        count += 1
        return reg_name

def change_reg(location, operand):
    global count
    if operand in registers.values():
        for key, value in registers.items():
            if operand == value:
                registers[key] = location


if __name__ == "__main__":
    lines = fileread()
    index = 0
    for line in lines:
        new_line = re.split("([\=\+\-\*\/])", line)
        operand1, eq, operand2, operator, operand3 = new_line
        if operand3 in registers.values():
            operand3 = assign_reg(operand3)
        assign_reg(operand2)
        if(index == len(lines) - 1):
            if(operator == '+'):
                reg_name = assign_reg(operand2)
                output.append('ADD ' + operand3 + ', ' + reg_name)
            elif(operator == '-'):
                reg_name = assign_reg(operand2)
                output.append('SUB ' + operand3 + ', ' + reg_name)
            operand2 = assign_reg(operand2)
            output.append('MOV ' + operand2 + ', ' + operand1)
            break
        if(operator == '+'):
            reg_name = assign_reg(operand2)
            output.append('ADD ' + operand3 + ', ' + reg_name)
            change_reg(operand1, operand2)
        elif(operator == '-'):
            reg_name = assign_reg(operand2)
            output.append('SUB ' + operand3 + ', ' + reg_name)
            change_reg(operand1, operand2)
        index += 1
    save_to_file()