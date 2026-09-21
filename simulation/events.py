import random


def record_event(mission, event_name, outcome):

    event_record = {
        "run_id": mission["run_id"],
        "day": mission["day"],
        "event": event_name,
        "outcome": outcome
    }

    mission["events"].append(event_record)


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
            record_event(mission,"Solar Storm","Emergency shielding activated")

        else:
            print("❌ Not enough power!")
            print("The outpost cannot activate emergency shielding")
            record_event(mission,"Solar Storm","Emergency shielding failed - insufficient power")

    elif choice == "2":

        mission["power"] += 5

        radiation_damage = 15 - mission["shielding"] * 0.2
        radiation_damage = max(0, radiation_damage)

        mission["life_support"] = max(0,mission["life_support"] - radiation_damage)

        print("⚡ Non-essential systems shut down")
        print("Power was conserved.")
        print(f"Radiation impact: {radiation_damage:.1f}")
        record_event(mission,"Solar Storm","Non-essential systems shut down")

    elif choice == "3":

        radiation_damage = 20 - mission["shielding"] * 0.2
        radiation_damage = max(0, radiation_damage)

        mission["life_support"] = max(0,mission["life_support"] - radiation_damage)

        print("🚨 The crew decided to do nothing")
        print(f"Radiation impact: {radiation_damage:.1f}")
        record_event(mission,"Solar Storm","No action taken")

    else:
        print("❌ Invalid choice!")    


def equipment_failure(mission):

    print("\n🔧 EQUIPMENT FAILURE!")
    print("A critical system has stopped working")

    print("\nChoose your response:")
    print("1. 🔧 Repair immediately")
    print("2. ⚡ Use backup system")
    print("3. ⏳ Delay the repair")

    choice = input("Choose a response: ")

    if choice == "1":

        if mission["power"] >= 15:
            mission["power"] -= 15
            print("🔧 Equipment repaired successfully")
            record_event(mission,"Equipment Failure","Equipment repaired immediately")

        else:
            print("❌ Not enough power to repair the equipment")
            record_event(mission,"Equipment Failure","Repair failed - insufficient power")

    elif choice == "2":

        if mission["power"] >= 5:
            mission["power"] -= 5
            mission["life_support"] = max(0,mission["life_support"] - 3)

            print("⚡ Backup system activated")
            print("The system is temporarily operating at reduced efficiency")
            record_event(mission,"Equipment Failure","Backup system activated")

        else:
            print("❌ Not enough power for the backup system")
            record_event(mission,"Equipment Failure","Repair failed - insufficient power")

    elif choice == "3":

        mission["life_support"] = max(0,mission["life_support"] - 8)

        print("⏳ Repair delayed.")
        print("Life support efficiency has decreased")
        record_event(mission,"Equipment Failure","Repair delayed")

    else:
        print("❌ Invalid choice!")


def random_event(mission):

    event_roll = random.random()

    if event_roll < 0.15:
        solar_storm(mission)

    elif event_roll < 0.30:
        equipment_failure(mission)

    else:
        print("✅ No major event today") 

