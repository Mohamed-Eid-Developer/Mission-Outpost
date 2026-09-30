import pandas as pd


def get_mission_runs(connection):
    query = """
        SELECT
            run_id,
            start_time,
            final_day,
            crew,
            status
        FROM mission_runs
        ORDER BY start_time DESC
    """

    return pd.read_sql(query, connection)


def get_daily_metrics(connection):
    query = """
        SELECT
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
        FROM mission_daily_metrics
        ORDER BY day
    """

    return pd.read_sql(query, connection)


def get_mission_events(connection):
    query = """
        SELECT
            run_id,
            day,
            event,
            outcome
        FROM mission_events
        ORDER BY day
    """

    return pd.read_sql(query, connection)

