import random

mission = {
    "day": 1,
    "crew": 6,
    "power": 100,
    "food": 80,
    "life_support": 70,
    "shielding": 50,
    "power_saving": False
}


def improve_system(mission, shielding=0, life_support=0):
    power_needed = shielding + life_support

    if power_needed > mission["power"]:
        print("❌ Not enough power!")
        return False

    mission["power"] -= power_needed
    mission["shielding"] += shielding
    mission["life_support"] += life_support

    return True


def advance_day(mission):
    # Crew consumption
    food_consumption = mission["crew"] * 2
    life_support_consumption = mission["crew"] * 1

    mission["food"] = max(0, mission["food"] - food_consumption)

    mission["life_support"] = max(0,mission["life_support"] - life_support_consumption)

    # Power consumption
    power_consumption = 5

    if mission["power_saving"]:
        power_consumption = 3    

    mission["power"] = max(0,mission["power"] - power_consumption) 
    
    # Reset power saving for the next day
    mission["power_saving"] = False

    # Move to the next day
    mission["day"] += 1


def solar_storm(mission):
    radiation_damage = 20 - mission["shielding"] * 0.2

    if radiation_damage < 0:
        radiation_damage = 0

    mission["life_support"] -= radiation_damage

    print("☀️  Solar storm detected!")
    print(f"Radiation impact: {radiation_damage:.1f}")


def check_mission_status(mission):

    if mission["food"] <= 0:
        print("❌ Mission failed: No food remaining.")
        return False

    if mission["life_support"] <= 0:
        print("❌ Mission failed: Life support is critical.")
        return False

    if mission["power"] <= 0:
        print("❌ Mission failed: No power remaining.")
        return False

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
        mission["food"] += 20

    elif choice == "4":
        mission["power_saving"] = True
        print("Power saving activated for today!")

    else:
        print("❌ Invalid choice!")


def show_status(mission):

    print("\n" + "=" * 35)
    print(f"🌍 Day {mission['day']}")
    print("=" * 35)

    print(f"👨‍🚀 Crew: {mission['crew']}")
    print(f"⚡ Power: {mission['power']:.1f}")
    print(f"🍎 Food: {mission['food']:.1f}")
    print(f"🫁  Life Support: {mission['life_support']:.1f}")
    print(f"🛡️  Shielding: {mission['shielding']:.1f}")


def random_event(mission) :

    if random.random() < 0.2 :
        solar_storm(mission)    


while mission["day"] <= 30:

    show_status(mission)
    player_action(mission)
    random_event(mission)
    advance_day(mission)

    if not check_mission_status(mission):
        break

print("\n🏁 Mission ended.")




