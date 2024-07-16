#

print("\n"
    "\n"
    "** Welcome to the City Gym! **"
    "\n")

def main_menu():
     input = ""

while True:
    "\n"
    print("Please select one of the 4 options below:")
    print("1. Membership plans")
    print("2. Optional extras")
    print("3. Gym Challenge")
    print("4. Exit the program")
    "\n"
    user_input = input("Enter an option")

    if user_input in main_menu:
        break

print("\033c", end="", flush=True) #clear console

if user_input == "1":
    membership_plans = ("1", "2", "3", "4", "5")
    while True:
        "\n"
        print("Membership plans")
        "\n"
        print("1. Basic")
        print("2. Regular")
        print("3. Premium")
        print("4. Return to main menu")
        print("5. Exit")
        "\n"
        user_input = input("Enter an option")
        
        if user_input in membership_plans:
            break
            
    if user_input == "1":
        prices = ("1", "2", "3", "4", "5")
        while True:
            print("1. Basic is $10 a week")
            user_input = input("Enter an option")

    if user_input == "2":
            print("2. Regular is $15 a week")
            user_input = input("Enter an option")

    if user_input == "3":
            print("3. Premium is $20 a week")
            user_input = input("Enter an option")

    elif user_input == '5': #test
         print('🥲')

#             if user_input in prices:
#                  break

if user_input == "2":
    "\n"
    print("2. Optional extras 2")
    "\n"

if user_input == "3":
    "\n"
    print("3. Gym Challenge")
    "\n"

elif user_input == "4":
     exit()

