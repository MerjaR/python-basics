# Finds specific parts from a recipe in certain format (see txt file)
def search_by_name(filename: str, search_term: str):
    results = []
    with open(filename) as f:
        lines = f.read().splitlines()
        
    i = 0
    while i < len(lines):
        if lines[i].strip() == "":
            i += 1
            continue

        name = lines[i].strip()
        i += 1

        if i < len(lines) and lines[i].isdigit():
            i += 1

        while i < len(lines) and lines[i].strip() != "":
            i += 1

        if search_term.lower() in name.lower():
            results.append(name)
      
        while i < len(lines) and lines[i].strip() != "":
            i += 1
            
    return results
            
def search_by_time(filename: str, prep_time: int):
    results = []
    with open(filename) as file:
        lines = [line.strip() for line in file]
    
    i = 0
    while i < len(lines):
        name = lines[i]
        cooking_time = int(lines[i + 1])
        if cooking_time <= prep_time:
            results.append(f"{name}, preparation time {cooking_time} min")

        i +=2
        while i < len(lines) and lines[i] !="":
            i += 1
        i += 1
    return results

def search_by_ingredient(filename: str, ingredient: str):
    results = []
    with open(filename) as file:
        lines = [line.strip() for line in file]
    
    i = 0
    while i <len(lines):
        if lines[i] == "":
            i += 1
            continue
        
        name = lines[i]
        i += 1

        prep_time = int(lines[i])
        i += 1

        ingredients = []
        while i < len(lines) and lines[i] !="":
            ingredients.append(lines[i])
            i += 1

        if ingredient.lower() in [item.lower() for item in ingredients]:
            results.append(f"{name}, preparation time {prep_time} min")

        i += 1

    return results
