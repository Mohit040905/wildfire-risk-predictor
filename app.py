import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('india_wildfire_model.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="India Wildfire Intensity Predictor",
    page_icon="🔥",
    layout="centered"
)

# Header
st.title("🔥 India Wildfire Intensity Predictor")
st.markdown("Based on **NASA VIIRS Satellite Data** across India (2012–2020)")
st.markdown("Enter satellite observation details to predict fire intensity level.")
st.divider()

# Input form
col1, col2 = st.columns(2)

with col1:
    latitude   = st.slider("📍 Latitude", 6.0, 35.0, 20.0)
    longitude  = st.slider("📍 Longitude", 68.0, 97.0, 80.0)
    bright_ti4 = st.slider("🌡️ Brightness Temp Ti4 (Kelvin)", 200.0, 370.0, 320.0)
    bright_ti5 = st.slider("🌡️ Brightness Temp Ti5 (Kelvin)", 0.0, 380.0, 295.0)

with col2:
    scan       = st.slider("📡 Scan Size", 0.3, 0.8, 0.4)
    track      = st.slider("📡 Track Size", 0.3, 0.8, 0.4)
    confidence = st.selectbox("🛰️ Detection Confidence",
                               options=[0, 1, 2],
                               format_func=lambda x: ['Low','Nominal','High'][x])
    month      = st.selectbox("📅 Month", list(range(1, 13)),
                               format_func=lambda x: ['Jan','Feb','Mar','Apr','May',
                                                       'Jun','Jul','Aug','Sep','Oct',
                                                       'Nov','Dec'][x-1])
    year       = st.slider("📆 Year", 2012, 2030, 2024)

st.divider()

# Predict
if st.button("🔍 Predict Fire Intensity", use_container_width=True):
    features = np.array([[latitude, longitude, bright_ti4,
                          scan, track, confidence,
                          bright_ti5, month, year]])
    prediction = model.predict(features)[0]

    if prediction == 'High':
        st.error("🔴 Intensity: HIGH — Severe wildfire! Immediate action needed.")
        st.markdown("**Recommended:** Alert forest department, deploy firefighting teams immediately.")
    elif prediction == 'Medium':
        st.warning("🟠 Intensity: MEDIUM — Moderate wildfire detected.")
        st.markdown("**Recommended:** Monitor closely, keep firefighting resources on standby.")
    else:
        st.success("🟢 Intensity: LOW — Minor fire activity detected.")
        st.markdown("**Recommended:** Routine monitoring sufficient.")

    st.divider()
    st.markdown("**📊 Input Summary:**")
    col1, col2, col3 = st.columns(3)
    col1.metric("Latitude", f"{latitude}°")
    col2.metric("Longitude", f"{longitude}°")
    col3.metric("Brightness Ti4", f"{bright_ti4}K")

# Footer
st.divider()
st.caption("Data Source: NASA VIIRS Satellite | Model: Random Forest (82% accuracy) | 3.8M Indian fire records")
st.divider()
st.markdown("### 🧪 Try a Real Recorded Fire Event")

examples = {
    "Northeast India Fire 2012 🔴": {
        "lat": 22.83762, "lon": 92.52300, "ti4": 367.0,
        "ti5": 338.8, "conf": 2, "month": 3, "year": 2012,
        "scan": 0.39, "track": 0.36
    },
    "Odisha/Chhattisgarh Fire 2013 🟠": {
        "lat": 19.52095, "lon": 80.90150, "ti4": 351.8,
        "ti5": 283.5, "conf": 1, "month": 3, "year": 2013,
        "scan": 0.41, "track": 0.61
    },
    "Kerala Forest Fire 2017 🟢": {
        "lat": 10.8, "lon": 76.5, "ti4": 312.1,
        "ti5": 291.8, "conf": 0, "month": 2, "year": 2017,
        "scan": 0.4, "track": 0.4
    }
}

selected = st.selectbox("Select a real fire event:", list(examples.keys()))

if st.button("🔍 Test This Event", use_container_width=True):
    e = examples[selected]
    features = np.array([[e['lat'], e['lon'], e['ti4'],
                          e['scan'], e['track'], e['conf'],
                          e['ti5'], e['month'], e['year']]])
    prediction = model.predict(features)[0]

    if prediction == 'High':
        st.error(f"🔴 Predicted Intensity: HIGH")
    elif prediction == 'Medium':
        st.warning(f"🟠 Predicted Intensity: MEDIUM")
    else:
        st.success(f"🟢 Predicted Intensity: LOW")
