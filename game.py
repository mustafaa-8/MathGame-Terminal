import random
from inputimeout import inputimeout, TimeoutOccurred


hp1 = 50
hp2 = 50

equations = {
    "20 % 7": 6, "48 + 25": 73, "21 * 7": 147, "10 * 11": 110, "31 * 22": 682, "28 % 10": 8,
    "22 + 2": 24, "42 + 23": 65, "13 / 2": 6.5, "30 + 2": 32, "23 / 1": 23.0, "30 ** 2": 900,
    "32 * 14": 448, "11 ** 2": 121, "49 - 23": 26, "20 + 3": 23, "17 * 11": 187, "46 / 2": 23.0,
    "22 % 6": 4, "19 - 4": 15, "28 % 9": 1, "47 + 1": 48, "14 * 21": 294, "17 + 20": 37,
    "41 + 25": 66, "38 - 2": 36, "16 ** 2": 256, "34 % 11": 1, "49 % 9": 4, "49 % 18": 13,
    "29 * 13": 377, "24 % 13": 11, "47 - 2": 45, "45 % 6": 3, "28 + 12": 40, "24 - 12": 12,
    "28 / 4": 7.0, "43 - 22": 21, "20 - 19": 1, "18 * 14": 252, "38 * 22": 836, "34 - 22": 12,
    "45 - 2": 43, "35 % 14": 7, "17 * 8": 136, "49 / 7": 7.0, "32 % 21": 11, "21 * 20": 420,
    "50 ** 2": 2500, "42 / 6": 7.0, "48 - 24": 24, "34 + 16": 50, "12 * 2": 24, "14 - 5": 9,
    "26 + 15": 41, "48 / 12": 4.0, "29 + 6": 35, "34 * 6": 204, "19 % 18": 1, "39 % 18": 3,
    "15 - 4": 11, "11 - 25": -14, "23 + 19": 42, "33 % 24": 9, "15 - 17": -2, "31 - 4": 27,
    "20 * 23": 460, "10 * 2": 20, "31 % 8": 7, "50 * 8": 400, "10 - 17": -7, "38 / 15": 2.5,
    "11 % 3": 2, "35 / 1": 35.0, "33 ** 2": 1089, "25 % 18": 7, }

questions = [
    "20 % 7", "48 + 25", "21 * 7", "10 * 11", "31 * 22", "28 % 10", "22 + 2", "42 + 23",
    "13 / 2", "30 + 2", "23 / 1", "30 ** 2", "32 * 14", "11 ** 2", "49 - 23", "20 + 3",
    "17 * 11", "46 / 2", "22 % 6", "19 - 4", "28 % 9", "47 + 1", "14 * 21", "17 + 20",
    "41 + 25", "38 - 2", "16 ** 2", "34 % 11", "49 % 9", "49 % 18", "29 * 13", "24 % 13",
    "47 - 2", "45 % 6", "28 + 12", "24 - 12", "28 / 4", "43 - 22", "20 - 19", "18 * 14",
    "38 * 22", "34 - 22", "45 - 2", "35 % 14", "17 * 8", "49 / 7", "32 % 21", "21 * 20",
    "50 ** 2", "42 / 6", "48 - 24", "34 + 16", "12 * 2", "14 - 5", "26 + 15", "48 / 12",
    "29 + 6", "34 * 6", "19 % 18", "39 % 18", "15 - 4", "11 - 25", "23 + 19", "33 % 24",
    "15 - 17", "31 - 4", "20 * 23", "10 * 2", "31 % 8", "50 * 8", "10 - 17", "38 / 15",
    "11 % 3", "35 / 1", "33 ** 2", "25 % 18"]

print("Hello! Players")
print("Welcome to the game\n")
print("Both players choose one team")
print("Red  OR  Blue")
print("Remember!")
print("The RED team always goes first")
input("Enter Any Key To Start The Game: ")


def redturn():
    global hp2
    input("RED'S TURN!\nEnter Any Key To Start The Turn: ")
    a = random.randint(0, 75)
    eq = questions[a]
    print(eq)

    def get_input():
        global user_answer
        try:
            user_answer = float(inputimeout(prompt="Solve within 5 seconds: ", timeout=3))
            b = equations.get(eq)
            accuracy = (user_answer/b)*100
            if accuracy == 100.0:
                damage = 10
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 10 damage")
            elif accuracy <= 109.9 and accuracy >= 100.1:
                damage = 9
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 9 damage")
            elif accuracy <= 119.9 and accuracy >= 110.0:
                damage = 8
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 8 damage")
            elif accuracy <= 129.9 and accuracy >= 120.0:
                damage = 7
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 7 damage")
            elif accuracy <= 139.9 and accuracy >= 130.0:
                damage = 6
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 6 damage")
            elif accuracy <= 149.9 and accuracy >= 140.0:
                damage = 5
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 5 damage")
            elif accuracy <= 159.9 and accuracy >= 150.0:
                damage = 4
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 4 damage")
            elif accuracy <= 169.9 and accuracy >= 160.0:
                damage = 3
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 3 damage")
            elif accuracy <= 179.9 and accuracy >= 170.0:
                damage = 2
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 2 damage")
            elif accuracy <= 189.9 and accuracy >= 180.0:
                damage = 1
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 1 damage")
            elif accuracy >= 190.0:
                damage = 0
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 0 damage")
            elif accuracy <= 99.9 and accuracy >= 90.0:
                damage = 9
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 9 damage")
            elif accuracy <= 89.9 and accuracy >= 80.0:
                damage = 8
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 8 damage")
            elif accuracy <= 79.9 and accuracy >= 70.0:
                damage = 7
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 7 damage")
            elif accuracy <= 69.9 and accuracy >= 60.0:
                damage = 6
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 6 damage")
            elif accuracy <= 59.9 and accuracy >= 50.0:
                damage = 5
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 5 damage")
            elif accuracy <= 49.9 and accuracy >= 40.0:
                damage = 4
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 4 damage")
            elif accuracy <= 39.9 and accuracy >= 30.0:
                damage = 3
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 3 damage")
            elif accuracy <= 29.9 and accuracy >= 20.0:
                damage = 2
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 2 damage")
            elif accuracy <= 19.9 and accuracy >= 10.0:
                damage = 1
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 1 damage")
            elif accuracy <= 9.9:
                damage = 0
                hp2 = hp2 - damage
                print("Blue's Updated HP:", hp2)
                print("You dealt 0 damage")
        except ValueError:
            print("Enter Numbers Only!")
    
    try:
        get_input()
    except TimeoutOccurred:
        print("\nTime's up!")
        damage = 0
        hp2 = hp2-damage
        print("Blue's Updated HP:", hp2)

def blueturn():
    global hp1
    input("BLUE'S TURN!\nEnter Any Key To Start The Turn: ")
    a = random.randint(0, 75)
    eq = questions[a]
    print(eq)

    def get_input():
        global user_answer
        try:
            user_answer = float(inputimeout("Solve within 5 seconds: ", timeout=3))
            b = equations.get(eq)
            accuracy = (user_answer/b)*100
            if accuracy == 100.0:
                damage = 10
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 10 damage")
            elif accuracy <= 99.9 and accuracy >= 90.0:
                damage = 9
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 9 damage")
            elif accuracy <= 89.9 and accuracy >= 80.0:
                damage = 8
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 8 damage")
            elif accuracy <= 79.9 and accuracy >= 70.0:
                damage = 7
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 7 damage")
            elif accuracy <= 69.9 and accuracy >= 60.0:
                damage = 6
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 6 damage")
            elif accuracy <= 59.9 and accuracy >= 50.0:
                damage = 5
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 5 damage")
            elif accuracy <= 49.9 and accuracy >= 40.0:
                damage = 4
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 4 damage")
            elif accuracy <= 39.9 and accuracy >= 30.0:
                damage = 3
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 3 damage")
            elif accuracy <= 29.9 and accuracy >= 20.0:
                damage = 2
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 2 damage")
            elif accuracy <= 19.9 and accuracy >= 10.0:
                damage = 1
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 1 damage")
            elif accuracy <= 9.9:
                damage = 0
                hp1 = hp1-damage
                print("Red's Updated HP:", hp1)
                print("You dealt 0 damage")
            elif accuracy <= 109.9 and accuracy >= 100.1:
                damage = 9
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 9 damage")
            elif accuracy <= 119.9 and accuracy >= 110.0:
                damage = 8
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 8 damage")
            elif accuracy <= 129.9 and accuracy >= 120.0:
                damage = 7
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 7 damage")
            elif accuracy <= 139.9 and accuracy >= 130.0:
                damage = 6
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 6 damage")
            elif accuracy <= 149.9 and accuracy >= 140.0:
                damage = 5
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 5 damage")
            elif accuracy <= 159.9 and accuracy >= 150.0:
                damage = 4
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 4 damage")
            elif accuracy <= 169.9 and accuracy >= 160.0:
                damage = 3
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 3 damage")
            elif accuracy <= 179.9 and accuracy >= 170.0:
                damage = 2
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 2 damage")
            elif accuracy <= 189.9 and accuracy >= 180.0:
                damage = 1
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 1 damage")
            elif accuracy >= 190.0:
                damage = 0
                hp1 = hp1-damage
                print("Red's Updated HP:", hp2)
                print("You dealt 0 damage")
        except ValueError:
            print("Enter Numbers Only!")
    
    try:    
        get_input()
    except TimeoutOccurred:
        print("\nTime's up!")
        damage = 0
        hp1 = hp1-damage
        print("Red's Updated HP:", hp1)
        


i = 0
while hp1 > 0 and hp2 > 0:
    print("\t     Turn", i)
    print("Red Team\t\tBlue Team")
    print("Health:", hp1, "\t\tHealth:", hp2)
    i = i+1
    print("\t  Red's Turn:", i)
    redturn()
    print("\t Blue's Turn:", i)
    blueturn()

print("\t   Final Score")
print("Red Team\t\tBlue Team")
print("Health:", hp1, "\t\tHealth:", hp2)

if hp1 <= 0 or hp2 <= 0:
    print("Game Tied!")
elif hp1 <= 0:
    hp1 = 0
    print("\n\nCongratulation! Blue Team Won")
elif hp2 <= 0:
    hp2 = 0
    print("\n\nCongratulation! Red Team Won")
