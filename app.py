
import streamlit as st
import pandas as pd
import numpy as np
import joblib


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

MODEL_FILE = "aquaculture_livestock_best_model.pkl"

try:
    model = joblib.load(MODEL_FILE)
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()


# ============================================================
# APPLICATION TITLE
# ============================================================

st.title("🐟 Aquaculture & Livestock Disease Risk Classification")

st.write(
    """
    Enter farm, water-quality, disease and feed information
    to predict the disease risk level.
    """
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("Farm Information")


sector = st.sidebar.selectbox(
    "Sector",
    ["Aquaculture", "Livestock"]
)

species = st.sidebar.text_input(
    "Species",
    "Tilapia"
)

state = st.sidebar.text_input(
    "State",
    "Andhra Pradesh"
)

farm_age = st.sidebar.number_input(
    "Farm Age (Years)",
    min_value=0.0,
    value=4.0
)

farm_area = st.sidebar.number_input(
    "Farm Area (Acres)",
    min_value=0.0,
    value=5.2
)


# ============================================================
# WATER QUALITY
# ============================================================

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
        min_value=0.0,
        value=5.2
    )


col4, col5 = st.columns(2)

with col4:
    ammonia = st.number_input(
        "Ammonia (mg/L)",
        min_value=0.0,
        value=0.3
    )

with col5:
    water_quality_score = st.number_input(
        "Water Quality Score",
        min_value=0.0,
        max_value=100.0,
        value=76.0
    )


# ============================================================
# STOCKING AND FEED
# ============================================================

st.subheader("🌾 Stocking & Feed")

col1, col2, col3 = st.columns(3)

with col1:
    stocking_density = st.number_input(
        "Stocking Density (Animals/Acre)",
        min_value=0.0,
        value=2500.0
    )

with col2:
    feed_quantity = st.number_input(
        "Feed Quantity (kg/day)",
        min_value=0.0,
        value=55.0
    )

with col3:
    feed_quality = st.number_input(
        "Feed Quality Score",
        min_value=0.0,
        max_value=100.0,
        value=82.0
    )


col4, col5 = st.columns(2)

with col4:
    daily_feed_cost = st.number_input(
        "Daily Feed Cost",
        min_value=0.0,
        value=2800.0
    )

with col5:
    feed_conversion_ratio = st.number_input(
        "Feed Conversion Ratio",
        min_value=0.0,
        value=1.6
    )


# ============================================================
# ENVIRONMENTAL FACTORS
# ============================================================

st.subheader("🌦 Environmental Factors")

col1, col2 = st.columns(2)

with col1:
    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=120.0
    )

with col2:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=72.0
    )


# ============================================================
# DISEASE INFORMATION
# ============================================================

st.subheader("🦠 Disease Information")

col1, col2, col3 = st.columns(3)

with col1:
    body_condition = st.number_input(
        "Body Condition Score",
        min_value=0.0,
        max_value=100.0,
        value=78.0
    )

with col2:
    disease_type = st.selectbox(
        "Disease Type",
        [
            "Bacterial",
            "Viral",
            "Fungal",
            "Parasitic",
            "Other"
        ]
    )

with col3:
    disease_onset = st.selectbox(
        "Disease Onset",
        [0, 1]
    )


col4, col5, col6 = st.columns(3)

with col4:
    mortality_rate = st.number_input(
        "Mortality Rate (%)",
        min_value=0.0,
        value=4.5
    )

with col5:
    productivity_score = st.number_input(
        "Productivity Score",
        min_value=0.0,
        max_value=100.0,
        value=82.0
    )

with col6:
    disease_risk_score = st.number_input(
        "Disease Risk Score",
        min_value=0.0,
        max_value=100.0,
        value=70.5
    )


# ============================================================
# CREATE INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame({

    "Sector": [sector],

    "Species": [species],

    "State": [state],

    "Farm_Age_Years": [farm_age],

    "Farm_Area_Acres": [farm_area],

    "Water_Temperature_C": [water_temperature],

    "Water_pH": [water_ph],

    "Dissolved_Oxygen_mg_L": [dissolved_oxygen],

    "Ammonia_mg_L": [ammonia],

    "Stocking_Density_Animals_Per_Acre": [
        stocking_density
    ],

    "Feed_Quantity_kg_Per_Day": [
        feed_quantity
    ],

    "Feed_Quality_Score": [
        feed_quality
    ],

    "Rainfall_mm": [
        rainfall
    ],

    "Humidity_Percent": [
        humidity
    ],

    "Body_Condition_Score": [
        body_condition
    ],

    "Disease_Type": [
        disease_type
    ],

    "Disease_Onset": [
        disease_onset
    ],

    "Mortality_Rate_Percent": [
        mortality_rate
    ],

    "Feed_Conversion_Ratio": [
        feed_conversion_ratio
    ],

    "Daily_Feed_Cost": [
        daily_feed_cost
    ],

    "Productivity_Score": [
        productivity_score
    ],

    "Water_Quality_Score": [
        water_quality_score
    ],

    "Disease_Risk_Score": [
        disease_risk_score
    ]
})


# ============================================================
# DISPLAY INPUT DATA
# ============================================================

with st.expander("View Input Data"):

    st.dataframe(
        input_data,
        use_container_width=True
    )


# ============================================================
# PREDICTION
# ============================================================

if st.button(
    "🔍 Predict Disease Risk",
    type="primary",
    use_container_width=True
):

    try:

        prediction = model.predict(input_data)[0]

        # ----------------------------------------------------
        # DISPLAY PREDICTION
        # ----------------------------------------------------

        st.subheader("Prediction Result")

        if prediction == "Low":

            st.success(
                "🟢 Disease Risk Level: LOW"
            )

        elif prediction == "Medium":

            st.warning(
                "🟡 Disease Risk Level: MEDIUM"
            )

        elif prediction == "High":

            st.error(
                "🔴 Disease Risk Level: HIGH"
            )

        else:

            st.info(
                f"Predicted Disease Risk: {prediction}"
            )


        # ----------------------------------------------------
        # PREDICTION PROBABILITY
        # ----------------------------------------------------

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(
                input_data
            )[0]

            classes = model.classes_

            probability_df = pd.DataFrame({

                "Disease Risk Level": classes,

                "Probability (%)":
                    probabilities * 100

            })

            probability_df[
                "Probability (%)"
            ] = probability_df[
                "Probability (%)"
            ].round(2)


            st.subheader(
                "Prediction Confidence"
            )

            st.dataframe(
                probability_df,
                use_container_width=True,
                hide_index=True
            )


            # Confidence
            confidence = (
                np.max(probabilities) * 100
            )

            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )


    except Exception as e:

        st.error(
            f"Prediction error: {e}"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Aquaculture + Livestock Disease Risk Classification ML System"
)
