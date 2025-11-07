import streamlit as st
import pandas as pd
from joblib import load

# ---- Load trained artifacts ----
# Make sure these files exist in student_stress_project/models/
model = load("models/logreg_pipeline.joblib")     # Logistic Regression pipeline (with scaler inside)
encoder = load("models/label_encoder.joblib")     # To map numbers -> "Low/Medium/High"

st.set_page_config(page_title="Student Stress Predictor", page_icon="🎓")
st.title("🎓 Student Stress Level Predictor")
st.write("Enter the student details and click **Predict** to get the stress level.")

# ---- Input controls ----
sleep_hours = st.slider("Sleep Hours", 3.0, 10.0, 7.0, step=0.1)
study_hours = st.slider("Study Hours", 0.0, 10.0, 3.0, step=0.1)
academic_pressure = st.slider("Academic Pressure (1–10)", 1, 10, 5)
peer_pressure = st.slider("Peer Pressure (1–10)", 1, 10, 5)
financial_stress = st.slider("Financial Stress (1–10)", 1, 10, 5)
physical_activity = st.slider("Physical Activity (hours/day)", 0.0, 6.0, 1.0, step=0.1)
diet_quality = st.slider("Diet Quality (1–5)", 1, 5, 3)
screen_time = st.slider("Screen Time (hours/day)", 0.0, 12.0, 5.0, step=0.1)
attendance = st.slider("Attendance (%)", 40.0, 100.0, 85.0, step=0.5)
social_support = st.slider("Social Support (1–10)", 1, 10, 5)

# Create input row matching training feature order
input_df = pd.DataFrame([{
    "sleep_hours": sleep_hours,
    "study_hours": study_hours,
    "academic_pressure": academic_pressure,
    "peer_pressure": peer_pressure,
    "financial_stress": financial_stress,
    "physical_activity": physical_activity,
    "diet_quality": diet_quality,
    "screen_time": screen_time,
    "attendance": attendance,
    "social_support": social_support
}])

if st.button("Predict"):
    # model outputs encoded integers (0/1/2). Convert to label string.
    pred_encoded = model.predict(input_df)[0]
    pred_label = encoder.inverse_transform([pred_encoded])[0]

    st.success(f"**Predicted Stress Level:** {pred_label}")
    # Optional: show class probabilities
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_df)[0]
        # encoder.classes_ gives order of labels for inverse mapping
        st.write("Class probabilities:")
        for label_idx, label_name in enumerate(encoder.classes_):
            st.write(f"- {label_name}: {proba[label_idx]:.2f}")
