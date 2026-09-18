import random
import csv
import uuid
from datetime import datetime

mission = {
    "run_id": str(uuid.uuid4()),
    "start_time": datetime.now().isoformat(),
    "day": 1,
    "crew": 6,
    "power": 100,
    "food": 80,
    "life_support": 70,
    "shielding": 50,
    "power_saving": False,
    "status": "RUNNING",
    "history": [],
    "events": []
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

    daily_metrics = {
    "food_consumed": food_consumption,
    "life_support_consumed": life_support_consumption,
    "power_consumed": power_consumption
}
   
    # Move to the next day
    mission["day"] += 1

    return daily_metrics


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


def check_mission_status(mission):

    if mission["food"] <= 0:
        mission["status"] = "FAILED"
        print("❌ Mission failed: No food remaining")
        return False

    if mission["life_support"] <= 0:
        mission["status"] = "FAILED"
        print("❌ Mission failed: Life support is critical")
        return False

    if mission["power"] <= 0:
        mission["status"] = "FAILED"
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
        print("✅ No major event today")      


def record_day(mission,food_consumed,life_support_consumed,power_consumed) :

    daily_record = {
        "run_id": mission["run_id"],
        "day": mission["day"],
        "crew": mission["crew"],
        "power": mission["power"],
        "food": mission["food"],
        "life_support": mission["life_support"],
        "shielding": mission["shielding"],

        "power_consumed": power_consumed,
        "food_consumed": food_consumed,
        "life_support_consumed": life_support_consumed,

        "status": mission["status"]
    }

    mission["history"].append(daily_record)   


def save_history(mission):

    with open("mission_history.csv", "w", newline="") as file:

        fieldnames = [
            "run_id",
            "day",
            "crew",
            "power",
            "food",
            "life_support",
            "shielding"
        ]

        writer = csv.DictWriter(file,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(mission["history"])  


def save_events(mission):

    with open("mission_events.csv", "w", newline="") as file:

        fieldnames = [
            "run_id",
            "day",
            "event",
            "outcome"
        ]

        writer = csv.DictWriter(file,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(mission["events"])  


def save_runs(run_record):

    with open("mission_runs.csv", "a", newline="") as file:

        fieldnames = [
            "run_id",
            "start_time",
            "final_day",
            "crew",
            "status"
        ]

        writer = csv.DictWriter(file,fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(run_record)                        


def record_event(mission, event_name, outcome):

    event_record = {
        "run_id": mission["run_id"],
        "day": mission["day"],
        "event": event_name,
        "outcome": outcome
    }

    mission["events"].append(event_record)


def mission_summary(mission):

    print("\n" + "=" * 40)
    print("🚀 MISSION SUMMARY")
    print("=" * 40)

    print(f"🆔 Run ID: {mission['run_id']}")
    print(f"📅 Final Day: {mission['day']}")
    print(f"👨‍🚀 Crew: {mission['crew']}")

    print(f"⚡ Final Power: {mission['power']:.1f}")
    print(f"🍎 Final Food: {mission['food']:.1f}")
    print(f"🫁 Final Life Support: {mission['life_support']:.1f}")
    print(f"🛡️ Final Shielding: {mission['shielding']:.1f}")

    print(f"📊 Mission Status: {mission['status']}")

    print(f"📝 Days Recorded: {len(mission['history'])}")
    print(f"⚠️ Events Recorded: {len(mission['events'])}")

    print("=" * 40)    


def record_mission_run(mission):

    run_record = {
        "run_id": mission["run_id"],
        "start_time": mission["start_time"],
        "final_day": mission["day"],
        "crew": mission["crew"],
        "status": mission["status"]
    }

    return run_record    


def validate_mission_data(mission):

    errors = []

    if mission["power"] < 0:
        errors.append("Power cannot be negative.")

    if mission["food"] < 0:
        errors.append("Food cannot be negative.")

    if mission["life_support"] < 0:
        errors.append("Life support cannot be negative.")

    if mission["shielding"] < 0:
        errors.append("Shielding cannot be negative.")

    if mission["crew"] <= 0:
        errors.append("Crew must be greater than zero.")

    if mission["day"] < 1:
        errors.append("Day must be greater than zero.")

    valid_statuses = ["RUNNING", "COMPLETED", "FAILED"]

    if mission["status"] not in valid_statuses:
        errors.append("Invalid mission status.")

    if errors:
        print("\n⚠️ Data Quality Issues:")

        for error in errors:
            print(f"- {error}")

        return False

    return True


mission_completed = False

while mission["day"] <= 30:

    # 1. Show current status
    show_status(mission)

    # 2. Player chooses an action
    player_action(mission)

    # 3. Check if the action caused a problem
    if not validate_mission_data(mission):
        mission["status"] = "FAILED"
        break

    # 4. Random event
    random_event(mission)

    # 5. Check again after the event
    if not validate_mission_data(mission):
        mission["status"] = "FAILED"
        break

    record_day(mission)

    # 6. End the day
    advance_day(mission)

    # 7. Check resources after daily consumption
    if not check_mission_status(mission):
        break

    if mission["day"] > 30 :
        mission_completed = True


if mission["day"] > 30 and mission["status"] == "RUNNING":
    mission["status"] = "COMPLETED"

mission_summary(mission)

if mission_completed:
    print("\n🎉 Mission Complete!")
    print("Your crew survived 30 days on Mars")

else:
    print("\n🏁 Mission Failed")


save_history(mission)
save_events(mission)

run_record = record_mission_run(mission)
save_runs(run_record)

print("\nMission data saved successfully")


