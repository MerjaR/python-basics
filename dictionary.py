# A file that reads in the data from dictionary.txt (task requirement), then allows adding and searching information with updating to file.
dictionary = {}

with open ("dictionary.txt") as file:
    for line in file:
        line = line.strip()
        
        parts = line.split(" - ")
        if len(parts) == 2:
            finnish = parts[0].strip()
            english = parts[1].strip()
            dictionary[finnish] = english

while True:

    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = input("Function: ")

    if choice == "3":
        print("Bye!")
        break
    elif choice == "1":
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
    
        dictionary[finnish_word] = english_word
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish_word} - {english_word}\n")

        print("Dictionary entry added")

    elif choice == "2":
        search_term = input("Search term: ")

        with open("dictionary.txt") as file:
            for line in file:
                pair = line.strip()

                if search_term in pair:
                    print(f"{pair}")
