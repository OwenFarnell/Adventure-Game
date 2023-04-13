import time

def intro():
    print("Welcome to the Adventure Game!\n")
    time.sleep(1)
    print("You find yourself in a dark forest. There are two paths ahead of you.")
    time.sleep(1)
    print("One leads to the left and the other leads to the right.")
    time.sleep(1)

def choose_path():
    path = input("Which path will you take? (L/R)").upper()
    while path != "L" and path != "R":
        path = input("Please choose a valid path (L/R)").upper()
    if path == "L":
        print("You chose the left path.")
        time.sleep(1)
        return "LEFT"
    else:
        print("You chose the right path.")
        time.sleep(1)
        return "RIGHT"

def encounter_enemy():
    print("You encounter a fierce enemy!")
    time.sleep(1)
    print("What will you do?")
    time.sleep(1)
    action = input("Fight or flee? (F/F)").upper()
    while action != "F" and action != "F":
        action = input("Please choose a valid action (F/F)").upper()
    if action == "F":
        print("You engage the enemy in battle!")
        time.sleep(1)
        print("After a fierce fight, you emerge victorious!")
        time.sleep(1)
    else:
        print("You run away from the enemy, narrowly escaping.")
        time.sleep(1)

def treasure():
    print("You have found a treasure chest!")
    time.sleep(1)
    print("Inside, you find a valuable gemstone.")
    time.sleep(1)
    print("Congratulations, you have completed the game!")

def main():
    intro()
    path = choose_path()
    if path == "LEFT":
        encounter_enemy()
        treasure()
    else:
        treasure()

if __name__ == "__main__":
    main()
