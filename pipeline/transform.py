import pandas as pd


def transform_mission_history(df):

    # Make a copy so we don't modify the original data
    transformed_df = df.copy()

    # Calculate remaining resource percentage
    transformed_df["resource_total"] = (
        transformed_df["power"]
        + transformed_df["food"]
        + transformed_df["life_support"]
        + transformed_df["shielding"]
    )

    # Calculate total daily consumption
    transformed_df["total_consumption"] = (
        transformed_df["power_consumed"]
        + transformed_df["food_consumed"]
        + transformed_df["life_support_consumed"]
    )

    return transformed_df

