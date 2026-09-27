import pandas as pd


def load_processed_data():

    file_path = "data/processed/mission_daily_metrics.csv"

    df = pd.read_csv(file_path)

    return df


def calculate_mission_metrics(df):

    metrics = {}

    metrics["total_days"] = df["day"].max()

    metrics["final_power"] = df["power"].iloc[-1]

    metrics["final_food"] = df["food"].iloc[-1]

    metrics["final_life_support"] = (
        df["life_support"].iloc[-1]
    )

    metrics["final_shielding"] = (
        df["shielding"].iloc[-1]
    )

    metrics["total_power_consumed"] = (
        df["power_consumed"].sum()
    )

    metrics["total_food_consumed"] = (
        df["food_consumed"].sum()
    )

    metrics["total_life_support_consumed"] = (
        df["life_support_consumed"].sum()
    )

    metrics["total_power_saved"] = (
        df["power_saved"].sum()
    )

    return metrics


def show_resource_trends(df):

    print("\n📈 Resource Trends")
    print("=" * 40)

    print(
        df[
            [
                "day",
                "power",
                "food",
                "life_support",
                "shielding"
            ]
        ]
    )


def find_lowest_resources(df):

    resources = [
        "power",
        "food",
        "life_support",
        "shielding"
    ]

    print("\n⚠️  Lowest Resource Levels")
    print("=" * 40)

    for resource in resources:

        minimum = df[resource].min()

        print(
            f"{resource}: {minimum:.1f}"
        )    



if __name__ == "__main__":

    df = load_processed_data()

    print("\n📊 Mission Data")
    print("=" * 40)

    print(df)

    print("\n📐 Dataset Shape")
    print("=" * 40)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n🔤 Data Types")
    print("=" * 40)

    print(df.dtypes)

    metrics = calculate_mission_metrics(df)

    print("\n🚀 Mission Metrics")
    print("=" * 40)

    for name, value in metrics.items():
        print(f"{name}: {value}")

    show_resource_trends(df)
    find_lowest_resources(df)

