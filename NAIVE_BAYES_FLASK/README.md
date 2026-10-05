# 🎓 Student Result Prediction System

A web-based machine learning application built with **Flask** and **Gaussian Naive Bayes** that predicts whether a student is likely to **Pass** or **Fail** based on academic indicators.

---

## 📌 Features

- **Gaussian Naive Bayes Classification:** Probabilistic machine learning model trained on continuous academic metrics.
- **Flask Web Interface:** Clean and responsive UI built with HTML and CSS for direct browser-based input.
- **Model Persistence:** Serialized model and label encoder saved using Python's `pickle`.
- **Instant Inference:** Real-time classification results returned immediately upon form submission.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn (GaussianNB, LabelEncoder, train_test_split)
- **Data Manipulation:** Pandas
- **Frontend:** HTML5, CSS3
- **Serialization:** Pickle

---

## 📊 Dataset & Input Features

The model evaluates three numerical parameters to predict the academic outcome:

| Feature | Description | Range |
| :--- | :--- | :--- |
| `study_hours` | Average study hours per day | Continuous (e.g., 1.0 – 10.0) |
| `attendance` | Percentage of attendance | 0 – 100% |
| `previous_marks` | Previous examination score | 0 – 100 |

**Target Class:** `Pass` / `Fail`

---

## 📂 Project Structure

```text
NAIVE_BAYES_FLASK/
│
├── student_data.csv       # Training dataset
├── train_model.py         # Data preprocessing and model training script
├── model.pkl              # Serialized trained model & encoder
├── app.py                 # Flask server and routing
├── requirements.txt       # Project dependencies
│
├── static/
│   └── style.css          # Form and layout styling
│
└── templates/
    ├── index.html         # User input form
    └── result.html        # Prediction display page
