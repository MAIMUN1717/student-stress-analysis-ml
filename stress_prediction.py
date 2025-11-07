import pandas as pd
from joblib import load

# Load your saved model and encoder
model = load("models/logreg_pipeline.joblib")
encoder = load("models/label_encoder.joblib")

def predict_stress(
    sleep_hours,
    study_hours,
    academic_pressure,
    peer_pressure,
    financial_stress,
    physical_activity,
    diet_quality,
    screen_time,
    attendance,
    social_support
):
    # Create dataframe for prediction
    input_df = pd.DataFrame([[
        sleep_hours, study_hours, academic_pressure, peer_pressure, financial_stress,
        physical_activity, diet_quality, screen_time, attendance, social_support
    ]], columns=[
        "sleep_hours", "study_hours", "academic_pressure", "peer_pressure", "financial_stress",
        "physical_activity", "diet_quality", "screen_time", "attendance", "social_support"
    ])

    # Predict encoded label
    pred_encoded = model.predict(input_df)[0]

    # Convert number back to "Low/Medium/High"
    pred_label = encoder.inverse_transform([pred_encoded])[0]

    return pred_label


# Example usage (test it)
if __name__ == "__main__":
    result = predict_stress(
        sleep_hours=6.5,
        study_hours=4,
        academic_pressure=8,
        peer_pressure=7,
        financial_stress=6,
        physical_activity=1,
        diet_quality=3,
        screen_time=6,
        attendance=82,
        social_support=4
    )

    print("Predicted Stress Level:", result)
