import pandas as pd


def extract_mission_history():

    file_path = "data/raw/mission_history.csv"

    df = pd.read_csv(file_path)

    return df

