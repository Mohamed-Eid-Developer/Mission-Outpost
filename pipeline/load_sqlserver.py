from pathlib import Path
import pandas as pd
from database.connection import get_connection


BASE_DIR = Path(__file__).resolve().parent.parent

RUNS_FILE = BASE_DIR / "data" / "raw" / "mission_runs.csv"
DAILY_FILE = BASE_DIR / "data" / "processed" / "mission_daily_metrics.csv"
EVENTS_FILE = BASE_DIR / "data" / "raw" / "mission_events.csv"


def load_mission_runs(connection):
    df = pd.read_csv(RUNS_FILE)

    cursor = connection.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            IF NOT EXISTS (
                SELECT 1
                FROM mission_runs
                WHERE run_id = ?
            )
            BEGIN
                INSERT INTO mission_runs
                (
                    run_id,
                    start_time,
                    final_day,
                    crew,
                    status
                )
                VALUES (?, ?, ?, ?, ?)
            END
            """,
            str(row["run_id"]),
            str(row["run_id"]),
            row["start_time"],
            int(row["final_day"]),
            int(row["crew"]),
            row["status"]
        )

    connection.commit()
    cursor.close()

    print(f"✅ Mission runs loaded: {len(df)}")


def load_daily_metrics(connection):
    df = pd.read_csv(DAILY_FILE)

    cursor = connection.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            IF NOT EXISTS (
                SELECT 1
                FROM mission_daily_metrics
                WHERE run_id = ?
                AND day = ?
            )
            BEGIN
                INSERT INTO mission_daily_metrics
                (
                    run_id,
                    day,
                    crew,
                    power,
                    food,
                    life_support,
                    shielding,
                    power_consumed,
                    power_saved,
                    food_consumed,
                    life_support_consumed,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            END
            """,
            str(row["run_id"]),
            int(row["day"]),
            str(row["run_id"]),
            int(row["day"]),
            int(row["crew"]),
            float(row["power"]),
            float(row["food"]),
            float(row["life_support"]),
            float(row["shielding"]),
            float(row["power_consumed"]),
            float(row["power_saved"]),
            float(row["food_consumed"]),
            float(row["life_support_consumed"]),
            row["status"]
        )

    connection.commit()
    cursor.close()

    print(f"✅ Daily metrics loaded: {len(df)}")


def load_mission_events(connection):
    df = pd.read_csv(EVENTS_FILE)

    cursor = connection.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            IF NOT EXISTS (
                SELECT 1
                FROM mission_events
                WHERE run_id = ?
                AND day = ?
                AND event = ?
                AND outcome = ?
            )
            BEGIN
                INSERT INTO mission_events
                (
                    run_id,
                    day,
                    event,
                    outcome
                )
                VALUES (?, ?, ?, ?)
            END
            """,
            str(row["run_id"]),
            int(row["day"]),
            row["event"],
            row["outcome"],
            str(row["run_id"]),
            int(row["day"]),
            row["event"],
            row["outcome"]
        )

    connection.commit()
    cursor.close()

    print(f"✅ Mission events loaded: {len(df)}")


def main():
    print("🚀 Starting SQL Server Load...")

    connection = get_connection()

    try:
        load_mission_runs(connection)
        load_daily_metrics(connection)
        load_mission_events(connection)

        print("🎉 SQL Server loading completed successfully!")

    finally:
        connection.close()
        print("🔒 Database connection closed.")


if __name__ == "__main__":
    main()    