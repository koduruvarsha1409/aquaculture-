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

    # Create input data
    input_data = pd.DataFrame([{
        "Sector": sector,
        "Species": species,
        "State": state,
        "Farm_Age_Years": farm_age,
        "Farm_Area_Acres": farm_area,
        "Water_Temperature_C": water_temperature,
        "Water_pH": water_ph,
        "Dissolved_Oxygen_mg_L": dissolved_oxygen,
        "Ammonia_mg_L": ammonia,
        "Rainfall_mm": rainfall,
        "Humidity_Percent": humidity,
        "Feed_Quantity_kg_Per_Day": feed_quantity,
        "Feed_Quality_Score": feed_quality,
        "Feed_Conversion_Ratio": feed_conversion,
        "Daily_Feed_Cost": daily_feed_cost,
        "Disease_Type": disease_type,
        "Disease_Onset": disease_onset,
        "Mortality_Rate_Percent": mortality_rate,
        "Productivity_Score": productivity_score,
        "Water_Quality_Score": water_quality_score
    }])

    if disease_model is not None:

        try:
            prediction = disease_model.predict(input_data)[0]

            st.subheader("🦠 Disease Risk Level")

            if str(prediction).lower() == "high":
                st.error("🔴 HIGH RISK")

            elif str(prediction).lower() == "medium":
                st.warning("🟡 MEDIUM RISK")

            elif str(prediction).lower() == "low":
                st.success("🟢 LOW RISK")

            else:
                st.info(f"Predicted Disease Risk Level: {prediction}")

        except Exception as e:
            st.error(f"Prediction error: {e}")

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

    # Water-quality fields are not applicable to livestock
    input_data = pd.DataFrame([{
        "Sector": sector,
        "Species": species,
        "State": state,
        "Farm_Age_Years": farm_age,
        "Farm_Area_Acres": 0,
        "Water_Temperature_C": np.nan,
        "Water_pH": np.nan,
        "Dissolved_Oxygen_mg_L": np.nan,
        "Ammonia_mg_L": np.nan,
        "Rainfall_mm": rainfall,
        "Humidity_Percent": humidity,
        "Feed_Quantity_kg_Per_Day": feed_quantity,
        "Feed_Quality_Score": feed_quality,
        "Feed_Conversion_Ratio": feed_conversion,
        "Daily_Feed_Cost": daily_feed_cost,
        "Disease_Type": disease_type,
        "Disease_Onset": disease_onset,
        "Mortality_Rate_Percent": mortality_rate,
        "Productivity_Score": productivity_score,
        "Water_Quality_Score": np.nan
    }])

    if disease_model is not None:

        try:
            prediction = disease_model.predict(input_data)[0]

            st.subheader("🦠 Disease Risk Level")

            if str(prediction).lower() == "high":
                st.error("🔴 HIGH RISK")

            elif str(prediction).lower() == "medium":
                st.warning("🟡 MEDIUM RISK")

            elif str(prediction).lower() == "low":
                st.success("🟢 LOW RISK")

            else:
                st.info(f"Predicted Disease Risk Level: {prediction}")

        except Exception as e:
            st.error(f"Prediction error: {e}")

    # Livestock prediction here
