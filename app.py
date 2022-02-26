import json
import os
import sys

choice = int
move = int

def initData(): 
    f = open('mastermanga.json', 'r')
    data = json.load(f)
    return data

data = initData()

def clear():
    os.system('clear')

clear()
print("Master Manga")
print("by simplesentai")
print("----------------------------------------------------------------")
while choice != 7:

    print("What do you want to do?")
    print("1. Show read manga")
    print("2. Show unread manga")
    print("3. Show reading manga")
    print("4. Move manga")
    print("5. Add manga to Unread")
    print("6. Drop a manga")
    print("7. Exit")
    choice = int(input(">>> "))

    if choice == 1:
        clear()
        print("Read manga:")
        for i in data["read"]:
            print(i)
        print("")
    elif choice == 2:
        clear()
        print("Unread manga:")
        for i in data["unread"]:
            print(i)
        print("")
    elif choice == 3:
        clear()
        print("Reading manga:")
        for i in data["reading"]:
            print(i)
        print("")
    elif choice == 4:
        clear()
        print("Move manga")
        print("1. Read manga")
        print("2. Unread manga")
        print("3. Reading manga")
        move = int(input(">>> "))
        if move == 1:
            print("Read manga:")
            for i in data["read"]:
                print(i)
            print("")
            print("Which manga do you want to move?")
            move = input(">>> ")
            if move in data["read"]:
                print("You've already read these, you can't move them!")
        elif move == 2:
            print("Unread manga:")
            for i in data["unread"]:
                print(i)
            print("")
            print("Which manga do you want to move?")
            move = input(">>> ")
            if move in data["unread"]:
                data["unread"].remove(move)
                data["reading"].append(move)
                print("Manga moved")
            else:
                print("Manga not found")
        elif move == 3:
            print("Reading manga:")
            for i in data["reading"]:
                print(i)
            print("")
            print("Which manga do you want to move?")
            move = input(">>> ")
            if move in data["reading"]:
                data["reading"].remove(move)
                data["read"].append(move)
                print("Manga moved")
            else:
                print("Manga not found")
    elif choice == 5:
        clear()
        print("Add manga to Unread")
        print("Which manga do you want to add?")
        move = input(">>> ")
        if move in data["unread"]:
            print("Manga already in Unread")
        else:
            data["unread"].append(move)
            print("Manga added")
    elif choice == 6:
        clear()
        print("Drop a manga")
        print("1. Read manga")
        print("2. Unread manga")
        print("3. Reading manga")
        move = int(input(">>> "))
        if move == 1:
            print("Read manga:")
            for i in data["read"]:
                print(i)
            print("")
            print("Which manga do you want to drop?")
            move = input(">>> ")
            if move in data["read"]:
                data["read"].remove(move)
                print("Manga dropped")
            else:
                print("Manga not found")
        elif move == 2:
            print("Unread manga:")
            for i in data["unread"]:
                print(i)
            print("")
            print("Which manga do you want to drop?")
            move = input(">>> ")
            if move in data["unread"]:
                data["unread"].remove(move)
                print("Manga dropped")
            else:
                print("Manga not found")
        elif move == 3:
            print("Reading manga:")
            for i in data["reading"]:
                print(i)
            print("")
            print("Which manga do you want to drop?")
            move = input(">>> ")
            if move in data["reading"]:
                data["reading"].remove(move)
                print("Manga dropped")
            else:
                print("Manga not found")
    else:
        clear()
        break

with open('mastermanga.json', 'w') as outfile:
    outfile.write(json.dumps(data))
    
# EOF
sys.exit()
