# AIML House Price Predictor

This repository contains my AIML internship Task 1 project: **Build and Evaluate a Linear Regression Model using the California Housing Dataset**.

## Objective

To understand the full Machine Learning workflow:

1. Load dataset
2. Explore the dataset
3. Visualize the data
4. Split data into training and testing data
5. Train a Linear Regression model
6. Evaluate the model using MAE, RMSE and R² Score
7. Save the model
8. Create a short project report

## Dataset

The project uses the California Housing dataset from scikit-learn.

Target column: `MedHouseVal`

Features:

- MedInc
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude
- Longitude

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## Folder Structure

```text
AIML-House-Price-Predictor/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── notebook/
│   └── task1_ml_linear_regression.ipynb
├── report/
│   └── task1_linear_regression_report.pdf
├── model/
│   └── README.md
├── src/
│   ├── train_model.py
│   ├── predict_house_price.py
│   └── utils.py
├── images/
│   ├── correlation_heatmap.png
│   ├── actual_vs_predicted.png
│   └── residual_plot.png
└── dataset/
    └── README.md
```

## How to Run

Install requirements:

```bash
pip install -r requirements.txt
```

Open notebook:

```bash
jupyter notebook notebook/task1_ml_linear_regression.ipynb
```

Train model:

```bash
python src/train_model.py
```

Predict new house price:

```bash
python src/predict_house_price.py
```

## Deliverables

- Jupyter Notebook
- PDF Report
- Python training script
- Prediction script
- Requirements file
- Graph images

## Future Improvements

- Try Random Forest Regressor
- Try Polynomial Regression
- Improve feature engineering
- Build a Streamlit UI

## Conclusion

This project helped me understand the basic Machine Learning lifecycle from data loading to model evaluation and prediction.
