import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

import streamlit as st

st.set_page_config(
    page_title="Aquaculture & Livestock Disease Risk Classification",
    page_icon="🐟",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("🐟 Aquaculture & Livestock Disease Risk Classification")

st.write(
    "Enter farm, environmental, feed and disease information "
    "to assess disease risk."
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("🏠 Farm Information")

sector = st.sidebar.selectbox(
    "Sector",
    ["Aquaculture", "Livestock"]
)

# =========================================================
# AQUACULTURE
# =========================================================

if sector == "Aquaculture":

    st.header("🐟 Aquaculture Information")

    # -----------------------------
    # BASIC FARM INFORMATION
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        species = st.selectbox(
            "Species",
            [
                "Pangasius",
                "Rohu",
                "Catla",
                "Shrimp",
                "Tilapia"
            ]
        )

    with col2:
        state = st.selectbox(
            "State",
            [
                "Andhra Pradesh",
                "Karnataka",
                "Tamil Nadu",
                "Kerala",
                "West Bengal",
                "Odisha"
            ]
        )

    with col3:
        farm_age = st.number_input(
            "Farm Age (Years)",
            min_value=0.0,
            max_value=100.0,
            value=4.0
        )

    farm_area = st.number_input(
        "Farm Area (Acres)",
        min_value=0.1,
        value=5.2
    )

    # =====================================================
    # WATER QUALITY
    # =====================================================

    st.subheader("💧 Water Quality")

    col1, col2, col3 = st.columns(3)

    with col1:
        water_temperature = st.number_input(
            "Water Temperature (°C)",
            value=29.5
        )

    with col2:
        water_ph = st.number_input(
            "Water pH",
            value=7.4
        )

    with col3:
        dissolved_oxygen = st.number_input(
            "Dissolved Oxygen (mg/L)",
            value=5.2
        )

    col1, col2 = st.columns(2)

    with col1:
        ammonia = st.number_input(
            "Ammonia (mg/L)",
            value=0.30
        )

    with col2:
        water_quality_score = st.number_input(
            "Water Quality Score",
            min_value=0.0,
            max_value=100.0,
            value=76.0
        )

    # =====================================================
    # STOCKING & FEED
    # =====================================================

    st.subheader("🌾 Stocking & Feed")

    col1, col2, col3 = st.columns(3)

    with col1:
        stocking_density = st.number_input(
            "Stocking Density (Animals/Acre)",
            value=50.0
        )

    with col2:
        feed_quantity = st.number_input(
            "Feed Quantity (kg/day)",
            value=30.0
        )

    with col3:
        feed_quality = st.number_input(
            "Feed Quality Score",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

    col1, col2 = st.columns(2)

    with col1:
        feed_conversion = st.number_input(
            "Feed Conversion Ratio",
            value=1.60
        )

    with col2:
        daily_feed_cost = st.number_input(
            "Daily Feed Cost",
            min_value=0.0,
            value=50.0
        )

    # =====================================================
    # ENVIRONMENT
    # =====================================================

    st.subheader("🌦️ Environmental Information")

    col1, col2 = st.columns(2)

    with col1:
        rainfall = st.number_input(
            "Rainfall (mm)",
            value=50.0
        )

    with col2:
        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=70.0
        )

    # =====================================================
    # AQUACULTURE DISEASE
    # =====================================================

    st.subheader("🦠 Aquaculture Disease Information")

    disease_type = st.selectbox(
        "Disease Type",
        [
            "No Disease",
            "White Spot Disease",
            "Bacterial Infection",
            "Parasitic Infection",
            "Early Mortality Syndrome"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        disease_onset = st.selectbox(
            "Disease Onset",
            ["No", "Yes"]
        )

    with col2:
        mortality_rate = st.number_input(
            "Mortality Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

    # =====================================================
    # AQUACULTURE PRODUCTIVITY
    # =====================================================

    st.subheader("📈 Productivity")

    productivity_score = st.number_input(
        "Productivity Score",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

    # =====================================================
    # BUTTON
    # =====================================================

    if st.button("🔍 Assess Aquaculture Disease Risk"):

        st.success("Aquaculture information submitted successfully!")

        st.write("### 🦠 Disease Information")

        st.write(f"**Disease Type:** {disease_type}")
        st.write(f"**Disease Onset:** {disease_onset}")
        st.write(f"**Mortality Rate:** {mortality_rate}%")

        # Simple display logic
        if disease_type == "No Disease":
            st.info("✅ No disease reported.")
        else:
            st.warning(
                f"⚠️ Reported disease: {disease_type}"
            )


# =========================================================
# LIVESTOCK
# =========================================================

elif sector == "Livestock":

    st.header("🐄 Livestock Information")

    # -----------------------------
    # BASIC FARM INFORMATION
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        species = st.selectbox(
            "Animal Species",
            [
                "Cattle",
                "Buffalo",
                "Sheep",
                "Goat",
                "Poultry"
            ]
        )

    with col2:
        state = st.selectbox(
            "State",
            [
                "Andhra Pradesh",
                "Karnataka",
                "Tamil Nadu",
                "Kerala",
                "West Bengal",
                "Odisha"
            ]
        )

    with col3:
        farm_age = st.number_input(
            "Farm Age (Years)",
            min_value=0.0,
            max_value=100.0,
            value=4.0
        )

    if sector == "Livestock":
        st.subheader("🐄 Livestock Information")

    animal_count = st.number_input(
        "Animal Count",
        min_value=1,
        max_value=10000,
        value=10
    )

    age = st.number_input(
        "Animal Age (years)",
        min_value=0.0,
        max_value=30.0,
        value=3.0
    )

    feed_type = st.selectbox(
        "Feed Type",
        ["Grass", "Hay", "Silage", "Concentrate", "Mixed"]
    )

    # =====================================================
    # ANIMAL HEALTH
    # =====================================================

    st.subheader("🐄 Animal Health")

    col1, col2 = st.columns(2)

    with col1:
        body_condition = st.number_input(
            "Body Condition Score",
            min_value=0.0,
            max_value=5.0,
            value=2.5
        )

    with col2:
        mortality_rate = st.number_input(
            "Mortality Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

    # =====================================================
    # ENVIRONMENT
    # =====================================================

    st.subheader("🌦️ Environmental Information")

    col1, col2 = st.columns(2)

    with col1:
        rainfall = st.number_input(
            "Rainfall (mm)",
            value=50.0
        )

    with col2:
        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=70.0
        )

    # =====================================================
    # LIVESTOCK FEED
    # =====================================================

    st.subheader("🌾 Feed Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        feed_quantity = st.number_input(
            "Feed Quantity (kg/day)",
            value=30.0
        )

    with col2:
        feed_quality = st.number_input(
            "Feed Quality Score",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

    with col3:
        feed_conversion = st.number_input(
            "Feed Conversion Ratio",
            value=1.60
        )

    daily_feed_cost = st.number_input(
        "Daily Feed Cost",
        min_value=0.0,
        value=50.0
    )

    # =====================================================
    # LIVESTOCK DISEASE
    # =====================================================

    st.subheader("🦠 Livestock Disease Information")

    disease_type = st.selectbox(
        "Disease Type",
        [
            "No Disease",
            "Respiratory Infection",
            "Mastitis",
            "Parasitic Infection",
            "Foot and Mouth Disease"
        ]
    )

    disease_onset = st.selectbox(
        "Disease Onset",
        ["No", "Yes"]
    )

    # =====================================================
    # PRODUCTIVITY
    # =====================================================

    st.subheader("📈 Productivity")

    productivity_score = st.number_input(
        "Productivity Score",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

    # =====================================================
    # BUTTON
    # =====================================================

    if st.button("🔍 Assess Livestock Disease Risk"):

        st.success("Livestock information submitted successfully!")

        st.write("### 🦠 Disease Information")

        st.write(f"**Disease Type:** {disease_type}")
        st.write(f"**Disease Onset:** {disease_onset}")
        st.write(f"**Mortality Rate:** {mortality_rate}%")

        if disease_type == "No Disease":
            st.info("✅ No disease reported.")
        else:
            st.warning(
                f"⚠️ Reported disease: {disease_type}"
            )
# =====================================================
# RISK ASSESSMENT
# =====================================================

st.write("### 🎯 Risk Assessment")

if prediction.lower() == "low":
    st.success("🟢 Risk Level: LOW")

elif prediction.lower() == "medium":
    st.warning("🟡 Risk Level: MEDIUM")

elif prediction.lower() == "high":
    st.error("🔴 Risk Level: HIGH")

else:
    st.info(f"Risk Level: {prediction}")

    # Livestock prediction here
