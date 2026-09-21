import csv
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

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
        "power_saved": daily_metrics["power_saved"],
        "food_consumed": daily_metrics["food_consumed"],
        "life_support_consumed": daily_metrics["life_support_consumed"],

        "status": mission["status"]
    }

    mission["history"].append(daily_record)


def save_history(mission):

    file_path = DATA_DIR / "mission_history.csv"

    with open(file_path, "w", newline="") as file:

        fieldnames = [
            "run_id",
            "day",
            "crew",
            "power",
            "food",
            "life_support",
            "shielding",
            "power_consumed",
            "power_saved",
            "food_consumed",
            "life_support_consumed",
            "status"
        ]

        writer = csv.DictWriter(file,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(mission["history"])


def save_events(mission):

    file_path = DATA_DIR / "mission_events.csv"

    with open(file_path, "w", newline="") as file :

        fieldnames = [
            "run_id",
            "day",
            "event",
            "outcome"
        ]

        writer = csv.DictWriter(file,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(mission["events"]) 


def record_mission_run(mission):

    run_record = {
        "run_id": mission["run_id"],
        "start_time": mission["start_time"],
        "final_day": mission["day"],
        "crew": mission["crew"],
        "status": mission["status"]
    }

    return run_record 

def save_runs(run_record):

    file_path = DATA_DIR / "mission_runs.csv"

    file_exists = file_path.exists()

    with open(file_path, "a", newline="") as file:

        fieldnames = [
            "run_id",
            "start_time",
            "final_day",
            "crew",
            "status"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(run_record)


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


    

