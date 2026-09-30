import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))    
from database.connection import get_connection
from database.queries import(
    get_mission_runs,
    get_daily_metrics,
    get_mission_events
)

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Mission Outpost",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Mission Outpost")
st.subheader("Mission Analytics Dashboard")

st.write(
    "Monitor mission resources, consumption, "
    "events and mission performance."
)


# -----------------------------
# Load Data
# -----------------------------

@st.cache_data
def load_mission_data():
    connection = get_connection()

    query = """
        SELECT *
        FROM mission_daily_metrics
        ORDER BY run_id, day
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


@st.cache_data
def load_events():
    connection = get_connection()

    query = """
        SELECT *
        FROM mission_events
        ORDER BY run_id, day
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


df = load_mission_data()
events_df = load_events()

# -----------------------------
# Header
# -----------------------------

st.title("🚀 Mission Outpost")

st.subheader(
    "Interactive Mission Analytics Dashboard"
)

st.write(
    "Monitor mission resources, consumption, "
    "power conservation and mission events."
)


# -----------------------------
# Mission Metrics
# -----------------------------

total_days = int(df["day"].max())

final_power = df["power"].iloc[-1]

final_food = df["food"].iloc[-1]

final_life_support = df["life_support"].iloc[-1]

total_power_consumed = df["power_consumed"].sum()

total_power_saved = df["power_saved"].sum()


# -----------------------------
# KPI Cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "📅 Mission Days",
        total_days
    )


with col2:

    st.metric(
        "⚡ Final Power",
        f"{final_power:.1f}"
    )


with col3:

    st.metric(
        "🍎 Final Food",
        f"{final_food:.1f}"
    )


with col4:

    st.metric(
        "🫁 Life Support",
        f"{final_life_support:.1f}"
    )


# -----------------------------
# Resource Chart
# -----------------------------

st.divider()

st.header("📈 Mission Resources")

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


resource_chart = px.line(
    chart_data,
    x="day",
    y="amount",
    color="resource",
    markers=True,
    title="Resource Levels Over Time",
    labels={
        "day": "Mission Day",
        "amount": "Resource Level",
        "resource": "Resource"
    }
)

resource_chart.update_layout(
    hovermode="x unified"
)

st.plotly_chart(
    resource_chart,
    use_container_width=True
)


# -----------------------------
# Power Analysis
# -----------------------------

st.header("⚡ Power Analysis")

col1, col2 = st.columns(2)


with col1:

    power_chart = px.bar(
        df,
        x="day",
        y="power_consumed",
        title="Daily Power Consumption",
        labels={
            "day": "Mission Day",
            "power_consumed": "Power Consumed"
        }
    )

    st.plotly_chart(
        power_chart,
        use_container_width=True
    )


with col2:

    saving_chart = px.bar(
        df,
        x="day",
        y="power_saved",
        title="Power Saved",
        labels={
            "day": "Mission Day",
            "power_saved": "Power Saved"
        }
    )

    st.plotly_chart(
        saving_chart,
        use_container_width=True
    )


# -----------------------------
# Mission Events
# -----------------------------

st.divider()

st.header("🚨 Mission Events")


if len(events_df) > 0:

    event_counts = (
        events_df["event"]
        .value_counts()
        .reset_index()
    )

    event_counts.columns = [
        "event",
        "count"
    ]

    event_chart = px.bar(
        event_counts,
        x="event",
        y="count",
        title="Mission Events",
        labels={
            "event": "Event",
            "count": "Occurrences"
        }
    )

    st.plotly_chart(
        event_chart,
        use_container_width=True
    )

else:

    st.info(
        "No mission events have been recorded yet."
    )


# -----------------------------
# Mission Summary
# -----------------------------

st.divider()

st.header("📊 Mission Summary")
col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "⚡ Total Power Consumed",
        f"{total_power_consumed:.1f}"
    )


with col2:

    st.metric(
        "💾 Total Power Saved",
        f"{total_power_saved:.1f}"
    )


with col3:

    st.metric(
        "🚨 Total Events",
        len(events_df)
    )

    