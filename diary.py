# A simple diary that saves one line entries into a txt file.
with open("diary.txt") as file:
    content = file.read()

while True:

    print("1 - add an entry, 2 - read entries, 0 - quit")
    flag = input("Function: ")

    if flag == "0":
        print("Bye now!")
        break

    elif flag == "1":
        entry = input("Diary entry: ")
    
        with open("diary.txt", "a") as file:
            file.write("\n" + entry + "\n")
    
        print("Diary saved")

    elif flag == "2":
        with open("diary.txt") as file:
            content = file.read()
        print("Entries: ")
        print(content)
