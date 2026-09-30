from database.connection import get_connection
from database.queries import (
    get_mission_runs,
    get_daily_metrics,
    get_mission_events
)


connection = get_connection()

print("\n=== MISSION RUNS ===")
print(get_mission_runs(connection))

print("\n=== DAILY METRICS ===")
print(get_daily_metrics(connection))

print("\n=== EVENTS ===")
print(get_mission_events(connection))

connection.close()



