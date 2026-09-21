from simulation.mission import (
    create_mission,
    advance_day,
    check_mission_status,
    validate_mission_data,
    show_status
)
from simulation.actions import (
    improve_system,
    player_action
)
from simulation.events import (
    record_event,
    solar_storm,
    equipment_failure,
    random_event
)
from storage.logger import (
    record_day,
    save_history,
    save_events,
    save_runs,
    record_mission_run,
    mission_summary
)



mission = create_mission()
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

    if not check_mission_status(mission):
        record_day(mission, daily_metrics)
        break

    record_day(mission, daily_metrics)
   
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


