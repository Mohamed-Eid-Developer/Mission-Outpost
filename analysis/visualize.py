import pandas as pd
import plotly.express as px


def load_processed_data():

    file_path = "data/processed/mission_daily_metrics.csv"

    return pd.read_csv(file_path)


def load_events():

    file_path = "data/raw/mission_events.csv"

    return pd.read_csv(file_path)


def create_resource_chart(df):

    resource_columns = [
        "power",
        "food",
        "life_support",
        "shielding"
    ]

    chart_data = df[
        ["day"] + resource_columns
    ].melt(
        id_vars="day",
        var_name="resource",
        value_name="amount"
    )

    fig = px.line(
        chart_data,
        x="day",
        y="amount",
        color="resource",
        markers=True,
        title="🚀 Mission Resources Over Time",
        labels={
            "day": "Mission Day",
            "amount": "Resource Level",
            "resource": "Resource"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        hovermode="x unified"
    )

    return fig


def create_power_consumption_chart(df):

    fig = px.bar(
        df,
        x="day",
        y="power_consumed",
        title="⚡ Daily Power Consumption",
        labels={
            "day": "Mission Day",
            "power_consumed": "Power Consumed"
        }
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig


def create_power_saving_chart(df):

    fig = px.bar(
        df,
        x="day",
        y="power_saved",
        title="⚡ Power Saved by Conservation",
        labels={
            "day": "Mission Day",
            "power_saved": "Power Saved"
        }
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig


def analyze_events(events_df):

    print("\n🚨 Mission Events")
    print("=" * 40)

    event_counts = (
        events_df["event"]
        .value_counts()
    )

    print(event_counts)

    return event_counts


def create_event_chart(events_df):

    event_counts = (
        events_df["event"]
        .value_counts()
        .reset_index()
    )

    event_counts.columns = [
        "event",
        "count"
    ]

    fig = px.bar(
        event_counts,
        x="event",
        y="count",
        title="🚨 Mission Events",
        labels={
            "event": "Event",
            "count": "Occurrences"
        }
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig


def calculate_average_consumption(df):

    average_power = df["power_consumed"].mean()

    average_food = df["food_consumed"].mean()

    average_life_support = (
        df["life_support_consumed"].mean()
    )

    print("\n📊 Average Daily Consumption")
    print("=" * 40)

    print(f"⚡ Power: {average_power:.2f}")
    print(f"🍎 Food: {average_food:.2f}")
    print(
        f"🫁 Life Support: "
        f"{average_life_support:.2f}"
    )


if __name__ == "__main__":

    df = load_processed_data()
    events_df = load_events()

    calculate_average_consumption(df)

    analyze_events(events_df)

    resource_chart = create_resource_chart(df)
    resource_chart.show()

    power_chart = create_power_consumption_chart(df)
    power_chart.show()

    power_saving_chart = create_power_saving_chart(df)
    power_saving_chart.show()

    event_chart = create_event_chart(events_df)
    event_chart.show()


