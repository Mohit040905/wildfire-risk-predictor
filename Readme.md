# 🔥 India Wildfire Intensity Predictor

> Predicting wildfire intensity across India using NASA satellite data and Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue)
![ML](https://img.shields.io/badge/Model-Random%20Forest-green)
![Accuracy](https://img.shields.io/badge/Accuracy-79%25-orange)
![Streamlit](https://img.shields.io/badge/Deployed-Streamlit%20Cloud-red)

---

## 📌 Problem Statement
Every year, forest fires devastate India's ecologically sensitive regions —
Uttarakhand, Odisha, and Northeast India. Current fire detection methods
are slow and reactive. This project uses NASA satellite data to classify
wildfire intensity in real time, enabling faster disaster response.

---

## 🎯 Solution
A Machine Learning model trained on 4.4 million real NASA VIIRS satellite
fire records from India (2012–2020) that classifies wildfire intensity as:
- 🟢 **Low** — Minor fire activity
- 🟠 **Medium** — Moderate fire, monitor closely  
- 🔴 **High** — Severe fire, immediate action needed

---

## 🌐 Live Demo
👉 [Click here to try the app](https://wildfire-risk-predictor-jl6iskbz5wmzum6alyrxuv.streamlit.app/)

---

## 📂 Dataset
- **Source:** NASA VIIRS Active Fire Data (via Kaggle)
- **Size:** 4.4 million fire records
- **Period:** 2012 – 2020
- **Region:** India
- **Features:** Latitude, Longitude, Brightness Temperature (Ti4/Ti5),
  Fire Radiative Power (FRP), Confidence, Date

---

## 🔧 Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.12 |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| ML Models | Scikit-learn |
| Class Balancing | SMOTE (imbalanced-learn) |
| Model Saving | Pickle |
| Web App | Streamlit |
| Deployment | Streamlit Cloud |

---

## 🗂️ Project Structure

wildfire-risk-predictor/
├── app.py                      ← Streamlit web application
├── india_wildfire_model.pkl    ← Trained Random Forest model
├── requirements.txt            ← Python dependencies
└── README.md                   ← Project documentation

---

## ⚙️ Data Pipeline

Raw NASA Data (4.4M rows)
↓
Filter vegetation fires only (3.8M rows)
↓
Drop irrelevant columns
↓
Extract month & year from date
↓
Encode confidence (low=0, nominal=1, high=2)
↓
Create intensity labels from FRP values
↓
Smart sampling (116K rows)
↓
SMOTE oversampling (balance 3 classes)
↓
Train/Test Split (80/20)
↓
Train & Compare 3 Models
↓
Random Forest Selected ✅

---

## 📊 Model Results
| Model | Accuracy |
|---|---|
| Decision Tree | 75% |
| **Random Forest** | **79% ✅** |
| Gradient Boosting | 77% |

**Key Metrics (Random Forest):**
- Overall Accuracy: **79%**
- High Intensity Recall: **89%** ← most critical for disaster response
- Classes: Low / Medium / High (balanced via SMOTE)

**Top 5 Features:**
1. Longitude
2. Brightness Temperature Ti4
3. Brightness Temperature Ti5
4. Latitude
5. Month

---

## 🚀 Run Locally
```bash
# Clone the repo
git clone https://github.com/Mohit040905/wildfire-risk-predictor.git
cd wildfire-risk-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🔮 Future Scope
- Integrate NASA FIRMS live API for real-time satellite data fetching
- Map-based pin drop interface for citizen use
- Retrain model with 2020–2025 data
- Predict fire spread direction and estimated burn area

---

## ⚠️ Limitations
- Dataset covers 2012–2020 only
- Satellite input values require technical knowledge
- Model predicts intensity only, not fire spread

---

## 👨‍💻 Built With
- NASA VIIRS Satellite Data
- Python & Scikit-learn
- Streamlit Cloud

---

*Internship Project Submission*
