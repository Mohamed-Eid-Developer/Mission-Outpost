from simulation.mission import (
    create_mission,
    advance_day,
    check_mission_status,
    validate_mission_data,
    show_status
)
from simulation.actions import (improve_system,player_action)
import random
import csv


mission = create_mission()

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


def record_day(mission, daily_metrics):

    daily_record = {
        "run_id": mission["run_id"],
        "day": daily_metrics["day"],
        "crew": mission["crew"],

        "power": mission["power"],
        "food": mission["food"],
        "life_support": mission["life_support"],
        "shielding": mission["shielding"],

        "power_consumed": daily_metrics["power_consumed"],
        "food_consumed": daily_metrics["food_consumed"],
        "life_support_consumed": daily_metrics["life_support_consumed"],

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
            "shielding",
            "power_consumed",
            "food_consumed",
            "life_support_consumed",
            "status"
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
    print(f"🫁  Final Life Support: {mission['life_support']:.1f}")
    print(f"🛡️  Final Shielding: {mission['shielding']:.1f}")

    print(f"📊 Mission Status: {mission['status']}")

    print(f"📝 Days Recorded: {len(mission['history'])}")
    print(f"⚠️  Events Recorded: {len(mission['events'])}")

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

    daily_metrics = advance_day(mission)

    record_day(mission,daily_metrics)
   
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


