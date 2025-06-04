# Created as an example of a module 
def change_case(orig_string: str):
    new_string = ""
    for i in range(0, len(orig_string)):
        if orig_string[i].isupper():
            new_string = new_string + orig_string[i].lower()
        elif orig_string[i].islower:
            new_string = new_string + orig_string[i].upper()
    return new_string

def split_in_half(orig_string:str):
    mid = len(orig_string) // 2

    first_half = orig_string[:mid]
    second_half = orig_string[mid:]

    return (first_half, second_half)

def remove_special_characters(orig_string:str):
    new_string = ""
    for i in range(0, len(orig_string)):
        if orig_string[i].isupper() or orig_string[i].islower() or orig_string[i].isdigit() or orig_string[i] == " ":
            new_string = new_string + orig_string[i]
            
    return new_string
