import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('wildfire_model.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="Wildfire Risk Predictor",
    page_icon="🔥",
    layout="centered"
)

# Header
st.title("🔥 Wildfire Risk Predictor")
st.markdown("Enter environmental conditions below to predict wildfire risk level.")
st.divider()

# Input form
col1, col2 = st.columns(2)

with col1:
    temp  = st.slider("🌡️ Temperature (°C)", 2, 34, 18)
    RH    = st.slider("💧 Relative Humidity (%)", 15, 100, 44)
    wind  = st.slider("💨 Wind Speed (km/h)", 0, 10, 4)
    FFMC  = st.slider("FFMC Index", 18.0, 97.0, 91.0)
    DMC   = st.slider("DMC Index", 1.0, 292.0, 108.0)

with col2:
    DC    = st.slider("DC Index", 7.0, 861.0, 547.0)
    ISI   = st.slider("ISI Index", 0.0, 57.0, 9.0)
    X_coord = st.slider("📍 X Coordinate", 1, 9, 4)
    Y_coord = st.slider("📍 Y Coordinate", 2, 9, 4)
    month = st.selectbox("📅 Month", list(range(12)),
                format_func=lambda x: ['Jan','Feb','Mar','Apr','May',
                                       'Jun','Jul','Aug','Sep','Oct',
                                       'Nov','Dec'][x])
    day   = st.selectbox("📆 Day", list(range(7)),
                format_func=lambda x: ['Mon','Tue','Wed',
                                       'Thu','Fri','Sat','Sun'][x])

st.divider()

# Predict button
if st.button("🔍 Predict Wildfire Risk", use_container_width=True):
    features = np.array([[X_coord, Y_coord, month, day,
                          FFMC, DMC, DC, ISI,
                          temp, RH, wind]])
    prediction = model.predict(features)[0]

    # Display result
    if prediction == 'High':
        st.error("🔴 Risk Level: HIGH — Immediate alert recommended!")
    elif prediction == 'Medium':
        st.warning("🟠 Risk Level: MEDIUM — Monitor conditions closely.")
    elif prediction == 'Low':
        st.info("🟡 Risk Level: LOW — Conditions are manageable.")
    else:
        st.success("🟢 Risk Level: NO RISK — Conditions are safe.")

    # Show input summary
    st.divider()
    st.markdown("**Input Summary:**")
    st.write(f"Temperature: {temp}°C | Humidity: {RH}% | Wind: {wind} km/h | Month: {['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][month]}")
