import joblib
import numpy as np
from pathlib import Path

model_path = Path(__file__).resolve().parents[1] / "model" / "california_house_price_model.pkl"

if not model_path.exists():
    raise FileNotFoundError("Model not found. First run: python src/train_model.py")

model = joblib.load(model_path)

features = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms",
    "Population", "AveOccup", "Latitude", "Longitude"
]

print("California House Price Predictor")
values = []
for feature in features:
    values.append(float(input(f"Enter {feature}: ")))

prediction = model.predict(np.array(values).reshape(1, -1))
print(f"Predicted house value: {prediction[0]:.3f} hundred-thousand dollars")
