
import pandas as pd
import numpy as np
import joblib
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Aquaculture & Livestock Disease Risk",
    page_icon="🐟",
    layout="wide"
)

# ============================================================
# LOAD MODEL
# ============================================================

MODEL_FILE = "aquaculture_livestock_best_model_new.pkl"

try:
    model = joblib.load(MODEL_FILE)
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()

# ============================================================
# TITLE
# ============================================================

st.title("🐟 Aquaculture & Livestock Disease Risk Classification")

sector = st.sidebar.selectbox(
    "Sector",
    ["Aquaculture", "Livestock"]
)

# =========================
# AQUACULTURE
# =========================
if sector == "Aquaculture":

    st.header("🐟 Aquaculture Information")

    species = st.selectbox(
        "Species",
        ["Pangasius", "Rohu", "Tilapia", "Catfish", "Shrimp"]
    )

    state = st.selectbox(
        "State",
        ["Andhra Pradesh", "Tamil Nadu", "Karnataka",
         "West Bengal", "Kerala", "Odisha"]
    )

    farm_age = st.number_input(
        "Farm Age (Years)", min_value=0.0, value=4.0
    )

    farm_area = st.number_input(
        "Farm Area (Acres)", min_value=0.1, value=5.2
    )

    # -------------------------
    # AQUACULTURE ONLY
    # -------------------------
    st.subheader("💧 Water Quality")

    water_temperature = st.number_input(
        "Water Temperature (°C)", value=29.5
    )

    water_ph = st.number_input(
        "Water pH", value=7.4
    )

    dissolved_oxygen = st.number_input(
        "Dissolved Oxygen (mg/L)", value=5.2
    )

    ammonia = st.number_input(
        "Ammonia (mg/L)", value=0.3
    )

    water_quality_score = st.number_input(
        "Water Quality Score", value=76.0
    )

    stocking_density = st.number_input(
        "Stocking Density (Animals/Acre)", value=50.0
    )

    # -------------------------
    # FEED
    # -------------------------
    st.subheader("🌾 Stocking & Feed")

    feed_quantity = st.number_input(
        "Feed Quantity (kg/day)", value=30.0
    )

    feed_quality = st.number_input(
        "Feed Quality Score", value=80.0
    )

    feed_conversion = st.number_input(
        "Feed Conversion Ratio", value=1.6
    )

    daily_feed_cost = st.number_input(
        "Daily Feed Cost", value=50.0
    )

    # Aquaculture prediction here


# =========================
# LIVESTOCK
# =========================
elif sector == "Livestock":

    st.header("🐄 Livestock Information")

    species = st.selectbox(
        "Species",
        ["Cattle", "Buffalo", "Goat", "Sheep", "Poultry"]
    )

    state = st.selectbox(
        "State",
        ["Andhra Pradesh", "Tamil Nadu", "Karnataka",
         "West Bengal", "Kerala", "Odisha"]
    )

    farm_age = st.number_input(
        "Farm Age (Years)", min_value=0.0, value=4.0
    )

    farm_area = st.number_input(
        "Farm Area (Acres)", min_value=0.1, value=5.2
    )

    # -------------------------
    # ENVIRONMENT
    # -------------------------
    st.subheader("🌦️ Environmental Information")

    rainfall = st.number_input(
        "Rainfall (mm)", value=50.0
    )

    humidity = st.number_input(
        "Humidity (%)", value=70.0
    )

    # -------------------------
    # LIVESTOCK ONLY
    # -------------------------
    st.subheader("🐄 Animal Health")

    body_condition = st.number_input(
        "Body Condition Score", value=2.5
    )

    disease_onset = st.selectbox(
        "Disease Onset",
        [0, 1]
    )

    mortality_rate = st.number_input(
        "Mortality Rate (%)", value=2.0
    )

    # -------------------------
    # FEED
    # -------------------------
    st.subheader("🌾 Feed Information")

    feed_quantity = st.number_input(
        "Feed Quantity (kg/day)", value=30.0
    )

    feed_quality = st.number_input(
        "Feed Quality Score", value=80.0
    )

    feed_conversion = st.number_input(
        "Feed Conversion Ratio", value=1.6
    )

    daily_feed_cost = st.number_input(
        "Daily Feed Cost", value=50.0
    )

    # Livestock prediction here
