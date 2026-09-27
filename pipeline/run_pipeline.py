from extract import extract_mission_history
from transform import transform_mission_history
from load import load_processed_data
from quality import validate_mission_data


def run_pipeline():

    print("🚀 Starting ETL Pipeline...")

    # Extract
    print("\n📥 Extracting data...")
    df = extract_mission_history()

    print(f"Rows extracted: {len(df)}")

    # Data Quality
    print("\n🔎 Checking data quality...")

    if not validate_mission_data(df):
        print("\n🛑 Pipeline stopped because data quality checks failed.")
        return

    # Transform
    print("\n🔄 Transforming data...")
    transformed_df = transform_mission_history(df)

    print("Transformation completed")

    # Load
    print("\n📤 Loading processed data...")
    output_file = load_processed_data(transformed_df)

    print(f"Processed data saved to: {output_file}")

    print("\n✅ ETL Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()

    