import streamlit as st
import pandas as pd
from datetime import date, timedelta

# --- Local data imports ---
from strength_schedule_data import STRENGTH_SCHEDULE
from cardio_schedule_data import CARDIO_SCHEDULE

st.set_page_config(page_title="CHOPS Protocol Planner", page_icon="💪", layout="wide")

st.title("Custom CHOPS Protocol Planner")

# --- User Inputs ---
gym_access = st.radio("Do you have gym access?", ["Yes", "No"], horizontal=True)
beta_blockers = st.radio("Are you on Beta Blockers?", ["Yes", "No"], horizontal=True)
start_date = st.date_input("When do you want to start the protocol?", date.today())

# --- Helper functions ---
def get_durations(low, high):
    """Return protocol duration values without modification."""
    try:
        low = int(low) if low not in [None, ""] else 0
        high = int(high) if high not in [None, ""] else 0
    except Exception:
        return (low, high)

    return (low, high)

def parse_custom(value):
    """Convert custom low/high to int if possible, else 0."""
    if value is None:
        return 0
    try:
        return int(float(str(value).strip()))
    except Exception:
        return 0

# --- Strength Schedule ---
strength_rows = []
for row in STRENGTH_SCHEDULE:
    row_norm = {str(k).strip().lower(): v for k, v in row.items()}

    # filter gym/no-gym
    if row_norm.get("gym access") != (gym_access == "Yes"):
        continue

    # Prefer custom low/high if available
    custom_low = parse_custom(row_norm.get("custom low"))
    custom_high = parse_custom(row_norm.get("custom high"))

    if custom_low and custom_high:
        duration_display = f"{custom_low}–{custom_high} sec"
    else:
        d_low, d_high = get_durations(
            row_norm.get("duration low", 0),
            row_norm.get("duration high", 0)
        )
        duration_display = f"{d_low}–{d_high} sec" if d_low and d_high else ""

    week = int(row_norm.get("week", 0))
    day = int(row_norm.get("day", 0))
    session_date = start_date + timedelta(days=((week - 1) * 7 + (day - 1)))

    strength_rows.append({
        "Date": session_date,
        "Type": "Strength",
        "Week": week,
        "Day": day,
        "Exercise": row_norm.get("exercise", ""),
        "Sets": row_norm.get("sets", ""),
        "Hold": row_norm.get("hold", ""),
        "Duration": duration_display,
        "Custom Low": custom_low,
        "Custom High": custom_high,
        "Order": 0,  # ensures Strength appears before Cardio for same day
    })

df_strength = pd.DataFrame(strength_rows)

# --- Cardio Schedule ---
cardio_rows = []
for row in CARDIO_SCHEDULE:
    row_norm = {str(k).strip().lower(): v for k, v in row.items()}

    if not row_norm.get("training mode"):
        continue

    custom_low = parse_custom(row_norm.get("custom low"))
    custom_high = parse_custom(row_norm.get("custom high"))

    if custom_low and custom_high:
        duration_display = f"{custom_low}–{custom_high} min"
    else:
        d_low, d_high = get_durations(
            row_norm.get("duration low", 0),
            row_norm.get("duration high", 0)
        )
        duration_display = f"{d_low}–{d_high} min" if d_low and d_high else ""

    week = int(row_norm.get("week", 0))
    day = int(row_norm.get("day", 0))

    # ensure Order is numeric with fallback
    raw_order = row_norm.get("order", None)
    try:
        order = int(str(raw_order).strip())
    except Exception:
        order = 999

    session_date = start_date + timedelta(days=((week - 1) * 7 + (day - 1)))

    cardio_rows.append({
        "Date": session_date,
        "Type": "Cardio",
        "Week": week,
        "Day": day,
        "Exercise": row_norm.get("step", ""),
        "Training Mode": row_norm.get("training mode", ""),
        "Order": order,
        "Duration": duration_display,
        "Custom Low": custom_low,
        "Custom High": custom_high,
    })

# 🔑 Sort list before DataFrame
cardio_rows.sort(key=lambda r: (r["Week"], r["Day"], r["Order"]))

df_cardio = pd.DataFrame(cardio_rows)

# --- Combined Schedule ---
combined = (
    pd.concat([df_strength, df_cardio], ignore_index=True)
      .sort_values(by=["Date", "Week", "Day", "Type", "Order"], kind="mergesort")
      .reset_index(drop=True)
)

st.subheader("Combined Schedule")
if not combined.empty:
    st.dataframe(combined, use_container_width=True)
    st.download_button(
        "Download Combined Schedule (CSV)",
        combined.to_csv(index=False).encode("utf-8"),
        "combined_schedule.csv",
        "text/csv",
        key="download_combined"  # 🔑 unique key avoids duplicate ID errors
    )

# --- Disclaimer ---
st.caption("This tool is for educational purposes only and is not medical advice. Consult your clinician before making exercise changes.")
