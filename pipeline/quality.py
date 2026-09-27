import pandas as pd


def validate_mission_data(df):

    errors = []

    required_columns = [
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

    # Check required columns
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        errors.append(
            f"Missing columns: {missing_columns}"
        )

    # Check missing values
    if df.isnull().any().any():
        errors.append("Dataset contains missing values")

    # Check duplicate rows
    if df.duplicated().any():
        errors.append("Dataset contains duplicate rows")

    # Check invalid resource values
    resource_columns = [
        "power",
        "food",
        "life_support",
        "shielding"
    ]

    for column in resource_columns:
        if (df[column] < 0).any():
            errors.append(
                f"{column} contains negative values"
            )

    # Check crew
    if (df["crew"] <= 0).any():
        errors.append(
            "Crew contains invalid values."
        )

    # Check day
    if (df["day"] < 1).any():
        errors.append(
            "Day contains invalid values."
        )

    if errors:

        print("\n❌ Data Quality Check Failed:")

        for error in errors:
            print(f"- {error}")

        return False

    print("\n✅ Data Quality Check Passed!")

    return True

