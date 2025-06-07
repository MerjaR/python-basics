# Taking in strings, counting characters, showing characters that were in the string the minimum number of times, in order.
characters = {}
while True:
    strings = input("Enter a string: ")
    if strings == " ":
        break
    
    i = 0
    
    while i < len(strings):
        character = strings[i]
        if character not in characters:
            count = 1
            characters[character] = count
        elif character in characters:
            characters[character] = characters[character] + 1
        
        i += 1

    # Print for testing the first part print(characters)

number = int(input("Minimum number of characters: "))

print("Caharacters in order of occurrence: ")
#values = []
result_values = {}
#values_sorted = []
result = {}
#position = 0

for character in characters:
    if characters[character] >= number:
        result_values[character] = characters[character]
        #values.append(characters[character])

result = dict(sorted(result_values.items(), key=lambda key_val: key_val[1], reverse = True))

for character in result:           
    print(f'Character "{character}" was entered {result_values[character]} times')
    
#Print for testing the second part print(result)
           
            

        
    
