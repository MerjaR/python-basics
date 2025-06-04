# "Programming language executor". Takes in a file with lines of commands in a certain format. Prints all the print commands.
import string

def get_value(x, letter_dict):
    return letter_dict[x] if x in letter_dict else int(x)

def run(program):
    prints = []
    letter_dict = {letter: 0 for letter in string.ascii_uppercase}
    location = {}


    for i in range(len(program)):
        line = program[i].strip()
        if line.endswith(":"):
            label = line.rstrip(":")
            location[label] = i 
    
    i = 0
    while i < len(program):
        line = program[i].strip()
        if line.endswith(":"):
            i += 1
            continue

        command = line.split()
        if command[0] ==  "PRINT":
            if command[0] ==  "PRINT":
                prints.append(get_value(command[1], letter_dict))
    
        elif command[0] == "MOV":
            letter_dict[command[1]] = get_value(command[2], letter_dict)

        elif command[0] == "ADD":
            letter_dict[command[1]] += get_value(command[2], letter_dict)
        
        elif command[0] == "SUB":
            letter_dict[command[1]] -= get_value(command[2], letter_dict)
        
        elif command[0] == "MUL":
            letter_dict[command[1]] *= get_value(command[2], letter_dict)
        elif command[0] == "JUMP":
            if command[1] in location:
                i = location[command[1]]
                continue
        elif command[0] == "IF":
            var = command[1]
            op = command[2]
            value = get_value(command[3], letter_dict)
            label = command[5]

            condition = False
            if op == "==":
                condition = letter_dict[var] == value
            elif op == "!=":
                condition = letter_dict[var] != value
            elif op == "<":
                condition = letter_dict[var] < value
            elif op == ">":
                condition = letter_dict[var] > value
            elif op == "<=":
                condition = letter_dict[var] <= value
            elif op == ">=":
                condition = letter_dict[var] >= value

            if condition and label in location:
                i = location[label]
                continue

        elif command[0] == "END":
            return prints
       
        i += 1
    
    return prints




        
