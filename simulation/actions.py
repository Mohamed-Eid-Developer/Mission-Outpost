
def improve_system(mission, shielding=0, life_support=0):
    power_needed = shielding + life_support

    if power_needed > mission["power"]:
        print("❌ Not enough power!")
        return False

    mission["power"] -= power_needed
    mission["shielding"] += shielding
    mission["life_support"] += life_support

    return True


def player_action(mission):

    print("\nWhat do you want to do?")
    print("1. 🛡️  Improve Shielding")
    print("2. 🫁  Improve Life Support")
    print("3. 🍎 Improve Food")
    print("4. ⚡ Conserve Power")

    choice = input("Choose an action: ")

    if choice == "1":
        improve_system(mission, shielding=10)

    elif choice == "2":
        improve_system(mission, life_support=10)

    elif choice == "3":
        if mission["power"] >= 10 :            
            mission["power"] -= 10
            mission["food"] += 20
        else :
            print("Not enough power")    

    elif choice == "4":
        mission["power_saving"] = True
        print("Power saving activated for today!")

    else:
        print("❌ Invalid choice!")


