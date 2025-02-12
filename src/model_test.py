import joblib
import numpy as np
from feature_engineering import preprocess_data
from data_load import load_data

model = joblib.load("models/calories_model.pkl")

sample_data = np.array([[1, 25, 175.0, 70.0, 20.0, 110.0, 39.5]])

df = load_data()
_, _, scaler = preprocess_data(df)
sample_data_scaled = scaler.transform(sample_data)
predicted_calories = model.predict(sample_data_scaled)
print("Predicted Calories Burned:", predicted_calories[0])
