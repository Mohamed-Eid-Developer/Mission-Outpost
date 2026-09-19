import uuid
from datetime import datetime


def create_mission() :

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

    return mission


def advance_day(mission):
    # Crew consumption
    food_consumption = mission["crew"] * 2
    life_support_consumption = mission["crew"] * 1
    current_day = mission["day"]

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
    "day": current_day,     
    "food_consumed": food_consumption,
    "life_support_consumed": life_support_consumption,
    "power_consumed": power_consumption
}
   
    # Move to the next day
    mission["day"] += 1

    return daily_metrics


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


def show_status(mission):

    print("\n" + "=" * 35)
    print(f"🌍 Day {mission['day']}")
    print("=" * 35)

    print(f"👨‍🚀 Crew: {mission['crew']}")
    print(f"⚡ Power: {mission['power']:.1f}")
    print(f"🍎 Food: {mission['food']:.1f}")
    print(f"🫁  Life Support: {mission['life_support']:.1f}")
    print(f"🛡️  Shielding: {mission['shielding']:.1f}")


    