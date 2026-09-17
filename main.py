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

    print("\n☀️  SOLAR STORM DETECTED!")
    print("Radiation levels are increasing.")

    print("\nChoose your response:")
    print("1. 🛡️  Activate emergency shielding")
    print("2. ⚡ Shut down non-essential systems")
    print("3. 🚫 Do nothing")

    choice = input("Choose a response: ")

    if choice == "1":

        if mission["power"] >= 10:
            mission["power"] -= 10

            radiation_damage = 20 - mission["shielding"] * 0.2
            radiation_damage = max(0, radiation_damage)

            mission["life_support"] = max(0,mission["life_support"] - radiation_damage)

            print("🛡️  Emergency shielding activated.")
            print(f"Radiation impact: {radiation_damage:.1f}")

        else:
            print("❌ Not enough power!")
            print("The outpost cannot activate emergency shielding.")

    elif choice == "2":

        mission["power"] += 5

        radiation_damage = 15 - mission["shielding"] * 0.2
        radiation_damage = max(0, radiation_damage)

        mission["life_support"] = max(0,mission["life_support"] - radiation_damage)

        print("⚡ Non-essential systems shut down.")
        print("Power was conserved.")
        print(f"Radiation impact: {radiation_damage:.1f}")

    elif choice == "3":

        radiation_damage = 20 - mission["shielding"] * 0.2
        radiation_damage = max(0, radiation_damage)

        mission["life_support"] = max(0,mission["life_support"] - radiation_damage)

        print("🚨 The crew decided to do nothing.")
        print(f"Radiation impact: {radiation_damage:.1f}")

    else:
        print("❌ Invalid choice!")


def equipment_failure(mission):

    print("\n🔧 EQUIPMENT FAILURE!")
    print("A critical system has stopped working.")

    print("\nChoose your response:")
    print("1. 🔧 Repair immediately")
    print("2. ⚡ Use backup system")
    print("3. ⏳ Delay the repair")

    choice = input("Choose a response: ")

    if choice == "1":

        if mission["power"] >= 15:
            mission["power"] -= 15
            print("🔧 Equipment repaired successfully.")
        else:
            print("❌ Not enough power to repair the equipment.")

    elif choice == "2":

        if mission["power"] >= 5:
            mission["power"] -= 5
            mission["life_support"] = max(0,mission["life_support"] - 3)

            print("⚡ Backup system activated.")
            print("The system is temporarily operating at reduced efficiency")

        else:
            print("❌ Not enough power for the backup system.")

    elif choice == "3":

        mission["life_support"] = max(0,mission["life_support"] - 8)

        print("⏳ Repair delayed.")
        print("Life support efficiency has decreased")

    else:
        print("❌ Invalid choice!")


def check_mission_status(mission):

    if mission["food"] <= 0:
        print("❌ Mission failed: No food remaining")
        return False

    if mission["life_support"] <= 0:
        print("❌ Mission failed: Life support is critical")
        return False

    if mission["power"] <= 0:
        print("❌ Mission failed: No power remaining")
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


def random_event(mission):

    event_roll = random.random()

    if event_roll < 0.15:
        solar_storm(mission)

    elif event_roll < 0.30:
        equipment_failure(mission)

    else:
        print("✅ No major event today.")         


mission_completed = False

while mission["day"] <= 30:

    # 1. Show current status
    show_status(mission)

    # 2. Player chooses an action
    player_action(mission)

    # 3. Check if the action caused a problem
    if not check_mission_status(mission):
        break

    # 4. Random event
    random_event(mission)

    # 5. Check again after the event
    if not check_mission_status(mission):
        break

    # 6. End the day
    advance_day(mission)

    # 7. Check resources after daily consumption
    if not check_mission_status(mission):
        break

    if mission["day"] > 30 :
        mission_completed = True


if mission_completed:
    print("\n🎉 Mission Complete!")
    print("Your crew survived 30 days on Mars")

else:
    print("\n🏁 Mission Failed")




