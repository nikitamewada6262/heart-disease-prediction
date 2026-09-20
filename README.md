# 🫀 Heart Disease Prediction

This project is a **Machine Learning-based Heart Disease Prediction web application** built with **Python and Streamlit**. It uses a trained **K-Nearest Neighbors (KNN)** model to predict whether a person has a **low or high risk of heart disease** based on health information such as age, sex, chest pain type, blood pressure, cholesterol, fasting blood sugar, maximum heart rate, exercise-induced angina, oldpeak, and ST slope.

## How to Run

1. Clone or download the project.
2. Open a terminal in the project folder.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
streamlit run app.py
```

5. Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## Dependencies

The project requires:

* **Python**
* **Streamlit** — for the web application
* **Pandas** — for data handling
* **NumPy** — for numerical operations
* **Scikit-learn** — for the machine learning model and preprocessing
* **Joblib** — for loading the trained model, scaler, and feature columns

The application also requires these trained model files:

```text
KNN_heart.pkl
scaler.pkl
columns.pkl
```

This project is intended for **educational and demonstration purposes** and should not be used as a substitute for professional medical diagnosis.
