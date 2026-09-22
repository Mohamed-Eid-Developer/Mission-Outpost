from pathlib import Path


def load_processed_data(df):

    output_directory = Path("data/processed")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_file = output_directory / "mission_daily_metrics.csv"

    df.to_csv(output_file, index=False)

    return output_file

